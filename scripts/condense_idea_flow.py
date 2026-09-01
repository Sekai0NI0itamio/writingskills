#!/usr/bin/env python3
"""Condense IdeaThinkingFlow.md section-by-section.

The 124KB full build has duplicated topic sections (two merge passes each
produced a full set). This script: (1) merges same-topic sections into one
complete input each, (2) condenses EACH SECTION with its own small model call
(whole sections in, whole sections out — no broken chunks), 10 concurrent,
(3) assembles the final file in canonical order. Light-touch: keep every
rule/skeleton/quote; target ~70-80% of input size per section.

  python3 scripts/condense_idea_flow.py [--in-flight 8] [--max-per 12000]
"""
from __future__ import annotations

import argparse
import asyncio
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import chat, log  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "IdeaThinkingFlow.md"
OUT = ROOT / "IdeaThinkingFlow.md"
CACHE = ROOT / "cache" / "condense"

CANONICAL = [
    "Paragraph Logic-Flow Patterns",
    "Paragraph Skeletons",
    "Express-Idea Vocabulary",
    "Explanation Patterns (Replication Steps)",
    "Introductions & Personal Engagement",
    "Background & Definitions",
    "Methods & Procedures",
    "Data, Calculations & Results",
    "Analysis & Explanation of Ideas",
    "Evaluation, Limitations & Conclusions",
]

HEADER_MAP = [
    ("logic-flow", "Paragraph Logic-Flow Patterns"),
    ("skeleton", "Paragraph Skeletons"),
    ("vocab", "Express-Idea Vocabulary"),
    ("explanation pattern", "Explanation Patterns (Replication Steps)"),
    ("introduction", "Introductions & Personal Engagement"),
    ("background", "Background & Definitions"),
    ("definition", "Background & Definitions"),
    ("method", "Methods & Procedures"),
    ("procedure", "Methods & Procedures"),
    ("data", "Data, Calculations & Results"),
    ("calculation", "Data, Calculations & Results"),
    ("result", "Data, Calculations & Results"),
    ("analysis", "Analysis & Explanation of Ideas"),
    ("evaluation", "Evaluation, Limitations & Conclusions"),
    ("conclusion", "Evaluation, Limitations & Conclusions"),
]


def canonical_of(header: str) -> str:
    low = header.lower()
    for pat, canon in HEADER_MAP:
        if pat in low:
            return canon
    return ""


def parse_sections(text: str) -> list[tuple[str, str]]:
    import re
    parts = re.split(r"(?=^## )", text, flags=re.M)
    out = []
    for p in parts[1:]:
        head = p.splitlines()[0].lstrip("# ").strip()
        out.append((head, p.strip()))
    return out


CONDENSE_PROMPT = """You are condensing ONE section of IdeaThinkingFlow.md — the flow rule file teaching AI agents how 6/7-graded IB students express ideas. This section may contain DUPLICATED subsections (merged from different passes) and repetitive wording.

Condense it:
- Merge duplicated/repeated subsections and rules into one copy each (best quotes and clearest slot instructions win).
- KEEP every distinct rule, skeleton (slot template + fill instructions + original fill + different-idea demonstration), quote, and vocabulary group. Nothing substantive may be lost.
- Tighten only repetitive phrasing.
- Target: at most {max_per} characters, ideally ~70% of the input. NEVER drop content to hit the target — deduplication is where the savings come from.

Output ONLY this section's markdown starting with its `## ` header, wrapped in <final></final>."""


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in-flight", type=int, default=8)
    ap.add_argument("--max-per", type=int, default=12000)
    args = ap.parse_args()

    CACHE.mkdir(parents=True, exist_ok=True)
    text = SRC.read_text(encoding="utf-8")
    sections = parse_sections(text)
    log(f"{len(sections)} raw sections")

    # merge same-topic sections (duplicates from the two merge passes)
    merged: dict[str, list[str]] = {}
    order: list[str] = []
    for head, body in sections:
        canon = canonical_of(head) or head
        if canon not in merged:
            merged[canon] = []
            order.append(canon)
        merged[canon].append(body)
    jobs = []
    for canon in order:
        combined = "\n\n".join(merged[canon])
        jobs.append((canon, combined))
        log(f"  {canon}: {len(merged[canon])} copies -> {len(combined)} chars input")

    sem = asyncio.Semaphore(args.in_flight)

    async def condense(canon: str, body: str) -> tuple[str, str]:
        import hashlib
        cf = CACHE / (hashlib.sha1(body.encode()).hexdigest()[:12] + ".md")
        if cf.exists() and cf.stat().st_size > 400:
            d = cf.read_text(encoding="utf-8")
            log(f"  {canon}: cached ({len(d)} chars)")
            return canon, d
        async with sem:
            log(f"  {canon}: condensing {len(body)} chars...")
            d = await chat(
                CONDENSE_PROMPT.format(max_per=args.max_per) + "\n\n<section>\n" + body + "\n</section>",
                16384, min_len=max(400, len(body) // 6),
            )
        cf.write_text(d, encoding="utf-8")
        log(f"  {canon}: {len(body)} -> {len(d)} chars")
        return canon, d

    results = await asyncio.gather(*(condense(c, b) for c, b in jobs))
    by_canon = dict(results)

    header = text.split("\n\n")[0] + "\n"
    out_blocks = []
    for canon in CANONICAL:
        if canon in by_canon:
            block = by_canon[canon]
            if not block.lstrip().startswith("## "):
                block = f"## {canon}\n\n" + block
            out_blocks.append(block)
    # any non-canonical sections preserved at the end
    for canon in order:
        if canon not in CANONICAL and canon in by_canon:
            out_blocks.append(by_canon[canon])
    final = header + "\n\n" + "\n\n".join(out_blocks) + "\n"
    OUT.write_text(final, encoding="utf-8")
    log(f"FINAL: {OUT} ({len(final)} chars, {'OK < 100KB' if len(final) < 100_000 else 'still over'})")


if __name__ == "__main__":
    asyncio.run(main())
