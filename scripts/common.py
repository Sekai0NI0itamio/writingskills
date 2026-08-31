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
MODEL = os.environ.get("IDEA_FLOW_MODEL", "").strip()  # pin one model — empty = auto-free ladder
EFFORT = os.environ.get("IDEA_FLOW_EFFORT", "xhigh")  # highest reasoning effort tier

THINK_RE = re.compile(r"<think>[\s\S]*?</think>", re.IGNORECASE)
COT_RE = re.compile(r"Here's a thinking process:[\s\S]*?(?=(?:So (?:the|finally)|Therefore|##|###|\Z))", re.IGNORECASE)
FINAL_RE = re.compile(r"<final>([\s\S]*?)(?:</final>|\Z)")
META_ECHO_RE = re.compile(r"closing tag|<final>|final answer|wrapped exactly|follow </final>", re.IGNORECASE)

# Known traps in the free pool: safety classifiers, omni/embed/coder variants,
# OpenRouter's own router (resolves to a safety model), tiny models.
EXCLUDE_PATTERNS = ("content-safety", "openrouter/free", "omni", "embed", "lfm-2.5")
# Strong general writers first; everything else trails by context size.
PREFERRED = [
    "minimax/minimax-m3:free",
    "minimax/minimax-m2.7:free",
    "z-ai/glm-5.2:free",
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


async def chat(prompt: str, max_tokens: int = 12288, temperature: float = 0.4) -> str:
    """One completion. Model: IDEA_FLOW_MODEL pin, else the auto-free ladder.
    reasoning.effort = xhigh (drops to high if a model rejects the tier).
    Ladder mode: up to 3 full passes with cooldowns — free-pool saturation
    clears in waves, so persistence across models is what gets work through."""
    if not _key():
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    prompt = (
        "OUTPUT FORMAT (mandatory): your visible output must END with the final answer wrapped "
        "exactly like this:\n<final>\n...final markdown only...\n</final>\n"
        "Never write about these tags — just use them. Nothing may follow </final>.\n\n"
        + prompt
    )

    loop = asyncio.get_running_loop()
    last_err = "no attempt"
    ladder = [MODEL] if MODEL else discover_models()
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


async def _ladder_pass(ladder: list[str], prompt: str, max_tokens: int, temperature: float, loop) -> "str | RuntimeError":
    """One pass over the ladder. Returns the answer string, or the last error."""
    last_err: RuntimeError = RuntimeError("no attempt")
    for model in ladder:
        effort = EFFORT
        for attempt in range(2):
            body = {
                "model": model,
                "stream": True,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "reasoning": {"effort": effort},
                "messages": [{"role": "user", "content": prompt}],
            }
            try:
                def do() -> str:
                    chunks: list[str] = []
                    finish = "stop"
                    req = urllib.request.Request(
                        OPENROUTER_URL, data=json.dumps(body).encode(), headers=_headers(), method="POST"
                    )
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
                    return out

                raw_out = await loop.run_in_executor(None, do)
                m = FINAL_RE.search(raw_out)
                if m and len(m.group(1).strip()) > 5:
                    # explicitly fenced = trusted at any length
                    return clean(m.group(1).strip())
                stripped = clean(raw_out)
                # unfenced fallback only for real answers — never instruction echo
                if len(stripped) > 150 and not META_ECHO_RE.search(stripped):
                    return stripped
                raise RuntimeError(f"no usable answer ({len(raw_out)} raw chars)")
            except Exception as e:  # noqa: BLE001
                emsg = str(e)
                # effort tier unsupported by this model — drop to high, keep going
                if effort != "high" and ("reasoning" in emsg.lower() or "effort" in emsg.lower()) and ("400" in emsg or "invalid" in emsg.lower()):
                    effort = "high"
                    log(f"  {model}: effort '{EFFORT}' rejected — falling back to high")
                    continue
                last_err = RuntimeError(redact(f"{model}: {emsg[:140]}"))
                wait = min(45, 6 * (attempt + 1) * (attempt + 1))
                log(f"  {last_err} — retry in {wait}s")
                await asyncio.sleep(wait)
        log(f"  giving up on {model} — next model")
    return last_err


async def run_bounded(jobs: list, worker, total_in_flight: int) -> list:
    """Run async worker(job) jobs with a global in-flight cap. Returns results."""
    sem = asyncio.Semaphore(total_in_flight)

    async def wrap(job):
        async with sem:
            return await worker(job)

    return await asyncio.gather(*(wrap(j) for j in jobs))
