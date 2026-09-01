"""Shared helpers for the IdeaThinkingFlow pipeline.

OpenRouter direct API — key from OPENROUTER_API_KEY env. Own "auto free"
system: discover every free text->text reasoning model, rank strong writers
first, fall through the ladder when a model rate-limits. Streaming, retries,
<final>-fenced answer extraction, key redaction. Stdlib only.
"""
from __future__ import annotations

import asyncio
import json
import os
import re
import time
import urllib.error
import urllib.request

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODELS_URL = "https://openrouter.ai/api/v1/models"
ORCA_URL = "https://api.orcarouter.ai/v1/chat/completions"
ORCA_PRICING_URL = "https://api.orcarouter.ai/api/pricing"
NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL = os.environ.get("IDEA_FLOW_MODEL", "").strip()  # pin one model — empty = auto-free ladder
EFFORT = os.environ.get("IDEA_FLOW_EFFORT", "xhigh")  # highest reasoning effort tier

THINK_RE = re.compile(r"<think>[\s\S]*?</think>", re.IGNORECASE)
COT_RE = re.compile(r"Here's a thinking process:[\s\S]*?(?=(?:So (?:the|finally)|Therefore|##|###|\Z))", re.IGNORECASE)
FINAL_RE = re.compile(r"<final>([\s\S]*?)(?:</final>|\Z)")
META_ECHO_RE = re.compile(r"closing tag|<final>|final answer|wrapped exactly|follow </final>", re.IGNORECASE)

# Known traps in the free pool: safety classifiers, omni/embed/coder variants,
# OpenRouter's own router (resolves to a safety model), tiny models.
EXCLUDE_PATTERNS = ("content-safety", "openrouter/free", "omni", "embed", "lfm-2.5", "glm-5.2")
# Strong general writers first; everything else trails by context size.
PREFERRED = [
    "minimax/minimax-m3:free",
    "minimax/minimax-m2.7:free",
    "thinkingmachines/inkling:free",
    "thinkingmachines/inkling-small:free",
    "inclusionai/ling-3.0-flash-fin:free",
    "poolside/laguna-s-2.1:free",
    "google/gemma-4-31b-it:free",
    "google/gemma-4-26b-a4b-it:free",
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    "dots-studio/dots-3-note-preview:free",
    "nvidia/nemotron-3.5-lightning:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
    "poolside/laguna-xs-2.1:free",
]

_model_cache: list[str] = []
_rr = 0

# Runtime model health: models that persistently fail get skipped automatically.
# 403 (forbidden) = blacklisted for the whole process; repeated 429s/soft errors
# = timed cooldown. Success resets the counters.
_health: dict[str, dict] = {}
BLACKLIST_HOURS = 12
COOLDOWN_429_MIN = 6
COOLDOWN_SOFT_MIN = 10
# Observed consistently-dead models in this environment (seeded blacklisted;
# remove from this list if OpenRouter's pool recovers them)
SEED_DEAD = [
    "thinkingmachines/inkling:free",       # 403 always (agentic-endpoint only)
    "thinkingmachines/inkling-small:free", # 403 always
    "google/gemma-4-31b-it:free",          # 429 always
    "google/gemma-4-26b-a4b-it:free",      # 429 always
    "poolside/laguna-s-2.1:free",          # 429 always
    "poolside/laguna-xs-2.1:free",         # 429 always
]
for _dead in SEED_DEAD:
    _health[_dead] = {"fails": 99, "blocked_until": time.time() + BLACKLIST_HOURS * 3600, "reason": "seeded-dead"}


def _model_ok(model: str) -> bool:
    h = _health.get(model)
    return not h or time.time() >= h.get("blocked_until", 0)


def _record_failure(model: str, emsg: str) -> None:
    h = _health.setdefault(model, {"fails": 0, "blocked_until": 0, "reason": ""})
    h["fails"] += 1
    if h.get("blocked_until", 0) > time.time():
        return
    if "403" in emsg or "Forbidden" in emsg:
        h["blocked_until"] = time.time() + BLACKLIST_HOURS * 3600
        h["reason"] = "403"
        log(f"  [health] {model} BLACKLISTED {BLACKLIST_HOURS}h (403 Forbidden)")
    elif "503" in emsg or "Service Temporarily Unavailable" in emsg or "provider_unavailable" in emsg:
        h["fails"] += 1  # weighted: availability failures cool down after 2 hits
        if h["fails"] >= 3:
            h["blocked_until"] = time.time() + COOLDOWN_SOFT_MIN * 60
            h["fails"] = 0
            h["reason"] = "503"
            log(f"  [health] {model} cooling down {COOLDOWN_SOFT_MIN}m (repeated 503s)")
    elif "429" in emsg and h["fails"] >= 3:
        h["blocked_until"] = time.time() + COOLDOWN_429_MIN * 60
        h["fails"] = 0
        h["reason"] = "429"
        log(f"  [health] {model} cooling down {COOLDOWN_429_MIN}m (repeated 429)")
    elif h["fails"] >= 4:
        h["blocked_until"] = time.time() + COOLDOWN_SOFT_MIN * 60
        h["fails"] = 0
        h["reason"] = "soft"
        log(f"  [health] {model} cooling down {COOLDOWN_SOFT_MIN}m (repeated soft failures)")


def _record_success(model: str) -> None:
    h = _health.setdefault(model, {"fails": 0, "blocked_until": 0, "reason": ""})
    h["fails"] = 0
    h["blocked_until"] = 0
    h["successes"] = h.get("successes", 0) + 1


def health_snapshot() -> dict:
    """Per-model success/failure counters for progress reporting."""
    return {m: {"ok": h.get("successes", 0), "blocked": time.time() < h.get("blocked_until", 0)}
            for m, h in _health.items()}


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def _key() -> str:
    return os.environ.get("OPENROUTER_API_KEY", "").strip()


def _headers() -> dict:
    return {
        "authorization": f"Bearer {_key()}",
        "content-type": "application/json",
        "HTTP-Referer": "https://github.com/Sekai0NI0itamio/writingskills",
        "X-Title": "writingskills-idea-flow",
    }


def redact(msg: str) -> str:
    """Never let the key (or fragments of it) reach logs/exceptions."""
    k = _key()
    if k:
        msg = msg.replace(k, "***KEY***")
        if len(k) > 20:
            msg = msg.replace(k[:20], "***KEY***")
    return re.sub(r"[A-Za-z0-9]*sk-or-v1-[A-Za-z0-9]+", "***KEY***", msg)


def clean(text: str) -> str:
    text = THINK_RE.sub("", text or "")
    text = COT_RE.sub("", text)
    return text.strip()


def discover_models() -> list[str]:
    """All free text->text reasoning models, ranked. Fetched once per process."""
    if _model_cache:
        return list(_model_cache)
    pool: list[str] = []
    try:
        req = urllib.request.Request(MODELS_URL, headers={"content-type": "application/json"})
        d = json.loads(urllib.request.urlopen(req, timeout=30).read())
        for m in d.get("data", []):
            p = m.get("pricing", {}) or {}
            arch = m.get("architecture", {}) or {}
            outs = arch.get("output_modalities") or ["text"]
            ins = arch.get("input_modalities") or ["text"]
            if p.get("prompt") != "0" or p.get("completion") != "0":
                continue
            if outs != ["text"] or "text" not in ins:
                continue
            if "reasoning" not in (m.get("supported_parameters") or []):
                continue
            if (m.get("context_length") or 0) < 100_000:
                continue
            if any(pat in m["id"] for pat in EXCLUDE_PATTERNS):
                continue
            pool.append(m["id"])
    except Exception as e:  # noqa: BLE001
        log(f"model discovery failed ({redact(str(e))[:80]}) — using preferred list")
    ranked = [mid for mid in PREFERRED if mid in pool]
    ranked += sorted([mid for mid in pool if mid not in ranked])
    if not ranked:
        ranked = list(PREFERRED)
    _model_cache.extend(ranked)
    return list(_model_cache)


_orca_cache: list[str] = []


def _orca_key() -> str:
    return os.environ.get("ORCA_API_KEY", "").strip()


def _nvidia_key() -> str:
    return os.environ.get("NVIDIA_API_KEY", "").strip()


def discover_orca_models() -> list[str]:
    """OrcaRouter free models (-free, reasoning-capable) from the public catalog."""
    if _orca_cache:
        return list(_orca_cache)
    if not _orca_key():
        log("  [orca] ORCA_API_KEY not set — orca lane disabled")
        return []
    try:
        req = urllib.request.Request(ORCA_PRICING_URL, headers={"content-type": "application/json"})
        d = json.loads(urllib.request.urlopen(req, timeout=30).read())
        models = d.get("data", d)
        if isinstance(models, dict):
            models = models.get("models", [])
        out = []
        for m in models:
            mid = str(m.get("model_name") or m.get("id") or m.get("name") or "")
            if not mid.endswith("-free"):
                continue
            sp = m.get("supported_parameters") or []
            ctx = m.get("context_length") or 0
            if ctx and ctx < 60_000:
                continue
            if "reasoning_effort" in sp or "reasoning" in sp or True:
                out.append(mid)
        _orca_cache.extend(out)
    except Exception as e:  # noqa: BLE001
        log(f"orca discovery failed ({redact(str(e))[:80]})")
    return list(_orca_cache)


NVIDIA_MODEL = os.environ.get("NVIDIA_MODEL", "deepseek-ai/deepseek-v4-flash-0731")

_nvidia_ok: bool | None = None


def build_ladder() -> list[tuple[str, str]]:
    """Combined ladder: OpenRouter minimax-m3 first (the proven primary — the
    shared rate-limit pressure is gone once the other pipeline finishes), then
    the rest of the OpenRouter free pool, then OrcaRouter free, then NVIDIA
    deepseek-v4-flash-0731 (max thinking)."""
    entries: list[tuple[str, str]] = []
    openrouter = [("openrouter", m) for m in discover_models() if _model_ok(m)]
    openrouter.sort(key=lambda pm: 0 if pm[1] == "minimax/minimax-m3:free" else 1)
    entries.extend(openrouter)
    for mid in discover_orca_models():
        if _model_ok(mid):
            entries.append(("orcarouter", mid))
    if _nvidia_key() and _model_ok(NVIDIA_MODEL) and _nvidia_ok is not False:
        entries.append(("nvidia", NVIDIA_MODEL))
        if _nvidia_ok is None:
            _nvidia_ok = True
    if not entries:
        entries = [("openrouter", mid) for mid in PREFERRED]
    return entries


async def chat(prompt: str, max_tokens: int = 12288, temperature: float = 0.4) -> str:
    """One completion. Model: IDEA_FLOW_MODEL pin, else the auto-free ladder.
    reasoning.effort = xhigh (drops to high if a model rejects the tier).
    Ladder mode: up to 3 full passes with cooldowns — free-pool saturation
    clears in waves, so persistence across models is what gets work through."""
    if not _key() and not _orca_key() and not _nvidia_key():
        raise RuntimeError("no provider key set (NVIDIA_API_KEY / ORCA_API_KEY / OPENROUTER_API_KEY)")

    prompt = (
        "OUTPUT FORMAT (mandatory): your visible output must END with the final answer wrapped "
        "exactly like this:\n<final>\n...final markdown only...\n</final>\n"
        "Never write about these tags — just use them. Nothing may follow </final>.\n\n"
        + prompt
    )

    loop = asyncio.get_running_loop()
    last_err = "no attempt"
    if MODEL:
        entries = [("openrouter", MODEL)]
    else:
        entries = build_ladder()
        log(f"  [ladder] using {len(entries)} models: {', '.join(f'{p}/{m.split(chr(47))[-1]}' for p, m in entries[:4])}...")
    # rotate the start position so concurrent agents spread across the whole
    # free pool instead of herding onto one saturated model
    global _rr
    _rr += 1
    ladder = entries[_rr % len(entries):] + entries[:_rr % len(entries)]
    passes = 1 if MODEL else 3
    for p in range(passes):
        if p > 0:
            log(f"  ladder pass {p + 1}/{passes} after 60s cooldown")
            await asyncio.sleep(60)
        result = await _ladder_pass(ladder, prompt, max_tokens, temperature, loop)
        if isinstance(result, str):
            return result
        last_err = result
    raise RuntimeError(redact(f"all ladder models failed; last: {last_err}"))


async def _ladder_pass(ladder: list, prompt: str, max_tokens: int, temperature: float, loop) -> "str | RuntimeError":
    """One pass over the ladder. Returns the answer string, or the last error.
    Each entry is (provider, model)."""
    last_err: RuntimeError = RuntimeError("no attempt")
    for provider, model in ladder:
        if not _model_ok(model):
            continue
        effort = EFFORT
        for attempt in range(2):
            if provider == "orcarouter":
                body = {
                    "model": model,
                    "stream": True,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "reasoning_effort": effort,
                    "messages": [{"role": "user", "content": prompt}],
                }
                url = ORCA_URL
                headers = {"authorization": f"Bearer {_orca_key()}", "content-type": "application/json"}
            elif provider == "nvidia":
                # NVIDIA NIM thinking controls (same mapping the gateway uses):
                # xhigh/max normalize to "max"; enable_thinking via chat_template_kwargs
                effort_nvidia = "max" if effort in ("xhigh", "max") else effort
                body = {
                    "model": model,
                    "stream": True,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "chat_template_kwargs": {"enable_thinking": True, "clear_thinking": False, "reasoning_effort": effort_nvidia},
                    "messages": [{"role": "user", "content": prompt}],
                }
                url = NVIDIA_URL
                headers = {"authorization": f"Bearer {_nvidia_key()}", "content-type": "application/json"}
            else:
                body = {
                    "model": model,
                    "stream": True,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "reasoning": {"effort": effort},
                    "messages": [{"role": "user", "content": prompt}],
                }
                url = OPENROUTER_URL
                headers = _headers()
            try:
                def do() -> tuple[str, dict]:
                    chunks: list[str] = []
                    finish = "stop"
                    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
                    with urllib.request.urlopen(req, timeout=900) as resp:
                        for raw in resp:
                            line = raw.decode("utf-8", errors="replace").strip()
                            if not line.startswith("data:") or "[DONE]" in line:
                                continue
                            try:
                                d = json.loads(line[5:].strip())
                            except json.JSONDecodeError:
                                continue
                            if "error" in d:
                                raise RuntimeError(f"LLM error: {json.dumps(d['error'])[:250]}")
                            for ch in d.get("choices") or []:
                                if ch.get("finish_reason"):
                                    finish = ch["finish_reason"]
                                piece = (ch.get("delta") or {}).get("content")
                                if piece:
                                    chunks.append(piece)
                    out = "".join(chunks)
                    if finish == "length":
                        raise RuntimeError(f"hit token cap ({max_tokens}) — response truncated")
                    return out, dict(resp.headers or {})

                raw_out, _resp_headers = await loop.run_in_executor(None, do)
                _record_success(model)
                m = FINAL_RE.search(raw_out)
                if m and len(m.group(1).strip()) > 5:
                    return clean(m.group(1).strip())
                stripped = clean(raw_out)
                if len(stripped) > 150 and not META_ECHO_RE.search(stripped):
                    return stripped
                raise RuntimeError(f"no usable answer ({len(raw_out)} raw chars)")
            except urllib.error.HTTPError as e:
                emsg = str(e)
                retry_after = (e.headers or {}).get("retry-after") if hasattr(e, "headers") else None
                _record_failure(model, emsg)
                if provider == "orcarouter" and e.code == 429:
                    if retry_after:
                        wait = min(300, float(retry_after))
                        log(f"  {model}: 429 window full — waiting exactly {wait:.0f}s (Retry-After)")
                        await asyncio.sleep(wait)
                        continue  # one clean retry after the window refills
                    # no Retry-After = prompt over the free-tier cap — never retry
                    log(f"  {model}: 429 without Retry-After (prompt over free cap) — next model")
                    break
                last_err = RuntimeError(redact(f"{provider}/{model}: HTTP {e.code} {emsg[:100]}"))
                wait = min(20, 5 * (attempt + 1))
                log(f"  {last_err} — retry in {wait}s")
                await asyncio.sleep(wait)
            except Exception as e:  # noqa: BLE001
                emsg = str(e)
                if effort != "high" and ("reasoning" in emsg.lower() or "effort" in emsg.lower()) and ("400" in emsg or "invalid" in emsg.lower()):
                    effort = "high"
                    log(f"  {model}: effort '{EFFORT}' rejected — falling back to high")
                    continue
                _record_failure(model, emsg)
                last_err = RuntimeError(redact(f"{provider}/{model}: {emsg[:140]}"))
                wait = min(20, 5 * (attempt + 1))
                log(f"  {last_err} — retry in {wait}s")
                await asyncio.sleep(wait)
        log(f"  giving up on {provider}/{model} — next model")
    return last_err


async def run_bounded(jobs: list, worker, total_in_flight: int) -> list:
    """Run async worker(job) jobs with a global in-flight cap. Returns results."""
    sem = asyncio.Semaphore(total_in_flight)

    async def wrap(job):
        async with sem:
            return await worker(job)

    return await asyncio.gather(*(wrap(j) for j in jobs))
