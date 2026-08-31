"""Shared helpers for the IdeaThinkingFlow pipeline.

OpenRouter direct API (minimax-m3:free) — key from OPENROUTER_API_KEY env.
Streaming, retries with backoff, <final>-fenced answer extraction, CoT strip.
Stdlib only.
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
MODEL = os.environ.get("IDEA_FLOW_MODEL", "minimax/minimax-m3:free")
EFFORT = os.environ.get("IDEA_FLOW_EFFORT", "xhigh")  # highest effort minimax-m3 accepts

THINK_RE = re.compile(r"<think>[\s\S]*?</think>", re.IGNORECASE)
COT_RE = re.compile(r"Here's a thinking process:[\s\S]*?(?=(?:So (?:the|finally)|Therefore|##|###|\Z))", re.IGNORECASE)
FINAL_RE = re.compile(r"<final>([\s\S]*?)</final>")

_KEY_CACHE: list[str] = []


def _key() -> str:
    if not _KEY_CACHE:
        _KEY_CACHE.append(os.environ.get("OPENROUTER_API_KEY", "").strip())
    return _KEY_CACHE[0]


def _headers() -> dict:
    """Built per call (not at import) so late-set env works; key stripped."""
    return {
        "authorization": f"Bearer {_key()}",
        "content-type": "application/json",
        # OpenRouter attribution headers (recommended)
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


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def clean(text: str) -> str:
    text = THINK_RE.sub("", text or "")
    text = COT_RE.sub("", text)
    return text.strip()


async def chat(prompt: str, max_tokens: int = 12288, temperature: float = 0.4, max_attempts: int = 7) -> str:
    """One completion via OpenRouter (model from env, default minimax-m3:free)."""
    key = _key()
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    prompt = prompt + (
        "\n\nIMPORTANT: Reason as long as you need, but your visible output must END with the final "
        "answer wrapped exactly like this:\n<final>\n...final markdown only...\n</final>\n"
        "Nothing may follow </final>."
    )

    loop = asyncio.get_running_loop()
    last_err = "no attempt"
    effort = EFFORT
    for attempt in range(max_attempts):
        body = {
            "model": MODEL,
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
            if m and len(m.group(1).strip()) > 150:
                return clean(m.group(1).strip())
            stripped = clean(raw_out)
            if len(stripped) > 150 and "<final>" not in stripped:
                return stripped
            raise RuntimeError(f"no usable answer ({len(raw_out)} raw chars)")
        except Exception as e:  # noqa: BLE001
            emsg = str(e)
            # reasoning_effort unsupported by this model — drop to high, keep going
            if effort != "high" and ("reasoning" in emsg.lower() or "effort" in emsg.lower()) and ("400" in emsg or "invalid" in emsg.lower()):
                effort = "high"
                log(f"  {MODEL}: reasoning_effort '{EFFORT}' rejected — falling back to high")
                continue
            last_err = redact(f"{MODEL}: {emsg[:140]}")
            wait = min(120, 8 * (attempt + 1) * (attempt + 1))
            log(f"  attempt {attempt + 1}/{max_attempts} failed: {last_err} — retry in {wait}s")
            await asyncio.sleep(wait)
    raise RuntimeError(redact(f"all attempts failed; last: {last_err}"))


async def run_bounded(jobs: list, worker, total_in_flight: int) -> list:
    """Run async worker(job) jobs with a global in-flight cap. Returns results."""
    sem = asyncio.Semaphore(total_in_flight)

    async def wrap(job):
        async with sem:
            return await worker(job)

    return await asyncio.gather(*(wrap(j) for j in jobs))
