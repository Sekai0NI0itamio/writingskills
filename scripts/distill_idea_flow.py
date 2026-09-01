#!/usr/bin/env python3
"""Distill the per-part idea-flow notes into ONE IdeaThinkingFlow.md (<100KB).

Map-reduce with OpenRouter minimax-m3:free:
  MAP:    note chunks (~30KB) -> dense distilled rules (skeletons + flow +
          vocab + replication, junk dropped, dupes merged)
  REDUCE: group by SECTION TYPE (intro/background/method/data/analysis/
          evaluation/conclusion/general flow) -> per-topic merge -> one file

Resumable per step (cache/). Run analyze_idea_flow.py first.

  python3 scripts/distill_idea_flow.py [--test-one] [--reset]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import chat, log  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "notes"
INDEX = NOTES / "_index.json"
OUT = ROOT / "IdeaThinkingFlow.md"
CACHE = ROOT / "cache" / "distill"

TOPICS = [
    "General: How an Idea Moves Through a Paragraph",
    "Introductions & Personal Engagement",
    "Background & Definitions",
    "Methods & Procedures",
    "Data, Calculations & Results",
    "Analysis & Explanation of Ideas",
    "Evaluation, Limitations & Conclusions",
]

MAP_PROMPT = """You are distilling per-section analysis notes (written by other agents from 6/7-graded IB exemplar essays) into a general rule file about HOW STUDENTS EXPRESS IDEAS — the logical flow of paragraphs, paragraph skeletons, and how to replicate them with different ideas.

Distill THIS CHUNK. Hard rules:
- MERGE duplicate patterns/skeletons (same flow or same skeleton from different essays = ONE entry; keep the 2 best examples).
- DELETE junk: meta-commentary, planning dumps, repeats, anything without a concrete quote or a concrete skeleton.
- KEEP every distinct: (1) paragraph logic-flow pattern (move-by-move), (2) paragraph SKELETON with slot anatomy + fill instructions + one original fill + one different-idea demonstration, (3) express-idea vocabulary groups (connective + job), (4) explanation patterns with replication steps.
- Compress wording ruthlessly; no praise, no filler.
- Tag every entry with its SECTION TYPE if the notes state one: [intro], [background], [method], [data], [analysis], [evaluation], [conclusion], or [general].

Output ONLY distilled markdown (target <= 5000 characters)."""

REDUCE_PROMPT = """You are assembling the final "{topic}" section of IdeaThinkingFlow.md — a rule file teaching AI agents to express ideas the way 6/7-graded IB students do: paragraph logic flow, replicable paragraph skeletons with slot fill instructions, and express-idea vocabulary.

Below are {n} distilled partial versions of this topic. Merge them into ONE definitive version:
- Merge duplicate patterns/skeletons (best quotes and clearest fill instructions win).
- Order from most common/fundamental to rarest.
- Keep skeletons EXACTLY in their slot-template form with fill instructions, an original fill, and a different-idea demonstration.
- Keep vocabulary as compact groups (connective + job).
- Target <= 9000 characters. Dense, no filler. Output ONLY this section's markdown starting with the header `{topic}`."""

FINAL_TITLE = """# IdeaThinkingFlow — How 6/7-Graded IB Students Express Ideas

> Distilled by AI from {parts} section-part analyses of 80 grade-6/7 IB exemplar essays.
> Every skeleton and flow pattern carries verbatim quotes from the corpus. This file is a
> COMPLIANCE SPEC for expressing ideas: paragraphs follow these flow patterns, skeletons are
> filled per their slot instructions, and explanations use these replication steps. Pair with
> writing-rules (sentence structures) — that file governs sentence construction; this file
> governs how ideas move.

"""


def build_chunks() -> list[str]:
    """Glob the committed note files directly — _index.json can go stale when
    a mining run's final commit races its progress commits."""
    notes = sorted(NOTES.glob("*__part*.md"))
    chunks, cur = [], ""
    for f in notes:
        if f.name.startswith("_"):
            continue
        note = f.read_text(encoding="utf-8", errors="replace")
        head = f"\n\n===== SOURCE: {f.stem.replace('__part', ' — part ')} =====\n"
        if len(cur) + len(head) + len(note) > 30_000 and cur:
            chunks.append(cur)
            cur = ""
        cur += head + note
    if cur.strip():
        chunks.append(cur)
    return chunks


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--test-one", action="store_true")
    ap.add_argument("--reset", action="store_true")
    args = ap.parse_args()

    if args.reset and CACHE.exists():
        shutil.rmtree(CACHE)
        print("cache cleared")
    CACHE.mkdir(parents=True, exist_ok=True)

    chunks = build_chunks()
    n_parts = len([f for f in NOTES.glob("*__part*.md") if not f.name.startswith("_")])
    log(f"{len(chunks)} chunks from {n_parts} part notes")

    distillations = []
    for i, chunk in enumerate(chunks):
        cf = CACHE / f"map_{hashlib.sha1(chunk.encode()).hexdigest()[:12]}.md"
        if cf.exists() and cf.stat().st_size > 400:
            d = cf.read_text(encoding="utf-8")
            log(f"map {i + 1}/{len(chunks)}: cached ({len(d)} chars)")
        else:
            log(f"map {i + 1}/{len(chunks)}: distilling {len(chunk)} chars...")
            d = await chat(MAP_PROMPT + "\n\n<chunk>\n" + chunk + "\n</chunk>", 12288, min_len=200)
            cf.write_text(d, encoding="utf-8")
            log(f"map {i + 1}/{len(chunks)}: -> {len(d)} chars")
        distillations.append(d)
        if args.test_one:
            print("\n===== SAMPLE DISTILLATION =====\n" + d[:3000])
            return

    # group distillations by section tag
    tag_map = {
        "intro": "Introductions & Personal Engagement", "background": "Background & Definitions",
        "definition": "Background & Definitions", "method": "Methods & Procedures",
        "procedure": "Methods & Procedures", "data": "Data, Calculations & Results",
        "results": "Data, Calculations & Results", "analysis": "Analysis & Explanation of Ideas",
        "evaluation": "Evaluation, Limitations & Conclusions", "conclusion": "Evaluation, Limitations & Conclusions",
        "general": "General: How an Idea Moves Through a Paragraph", "flow": "General: How an Idea Moves Through a Paragraph",
    }
    by_topic: dict[str, list[str]] = {t: [] for t in TOPICS}
    unplaced: list[str] = []
    for d in distillations:
        blocks = re.split(r"\n(?=\*\*\[|\[|## )", d)
        for block in blocks:
            if len(block.strip()) < 80:
                continue
            low = block[:400].lower()
            matched = None
            for tag, topic in tag_map.items():
                if f"[{tag}]" in low or f"({tag})" in low:
                    matched = topic
                    break
            if matched is None and ("skeleton" in low or "flow" in low):
                matched = "General: How an Idea Moves Through a Paragraph"
            if matched:
                by_topic[matched].append(block.strip())
            else:
                unplaced.append(block.strip())
    # anything untagged lands in General so nothing is lost
    by_topic[TOPICS[0]].extend(unplaced)

    final_blocks = []
    for ti, topic in enumerate(TOPICS):
        versions = by_topic[topic]
        if not versions:
            log(f"topic '{topic}': nothing — skipped")
            continue
        joined = "\n\n---\n\n".join(versions)
        cf = CACHE / f"topic_{ti:02d}.md"
        if cf.exists() and cf.stat().st_size > 400:
            merged = cf.read_text(encoding="utf-8")
            log(f"topic '{topic}': cached ({len(merged)} chars)")
        else:
            # cap input per call
            inputs = versions if len(joined) < 55_000 else [joined[:55_000]]
            log(f"topic '{topic}': merging {len(versions)} versions ({sum(len(v) for v in versions)} chars)...")
            merged = await chat(
                REDUCE_PROMPT.format(n=len(versions), topic=topic)
                + "\n\n<versions>\n" + "\n\n---\n\n".join(inputs) + "\n</versions>",
                16384,
            )
            cf.write_text(merged, encoding="utf-8")
            log(f"topic '{topic}': -> {len(merged)} chars")
        if not merged.lstrip().startswith("## "):
            merged = topic + "\n\n" + merged
        final_blocks.append(merged)

    header = FINAL_TITLE.format(parts=n_parts)
    final = header + "\n\n" + "\n\n".join(final_blocks) + "\n"
    OUT.write_text(final, encoding="utf-8")
    size = OUT.stat().st_size
    log(f"FINAL: {OUT} ({size} bytes, {'OK < 100KB' if size < 100_000 else 'TOO BIG'})")


if __name__ == "__main__":
    asyncio.run(main())
