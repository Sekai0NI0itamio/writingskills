#!/usr/bin/env python3
"""Distill fetched writing-guide sources into one SKILL per writing part.

Reads sources/writing-parts/<part>__<site>.txt, groups by part, and distills
each part into writing-parts/<part>.md — a high-quality rule file: purpose,
structure/moves in order, sentence shapes with slots, dos/don'ts, defects to
fix. Resumable (skips parts that already have a skill file).

  python3 scripts/writing_parts/distill_parts.py [--only part] [--force]
"""
from __future__ import annotations

import argparse
import asyncio
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import chat, log  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "sources" / "writing-parts"
OUT = ROOT / "writing-parts"

PROMPT = """You are writing a COMPLIANCE-GRADE skill file for AI agents on ONE part of academic essay writing: "{part}".

Below are {n} source documents from university writing centers (Harvard, UNC, etc.) about this part.

Produce the definitive skill file for this part:
1. **Purpose** — what this part does in the essay and why it exists (2-3 sentences).
2. **Structure / Moves in order** — the exact sequence of moves, numbered, each with what it accomplishes.
3. **Sentence shapes with slot anatomy** — 3-6 reusable constructions quoted/adapted from the sources, each with its slots described (e.g. "[Claim about X]. [Evidence]. [What the evidence shows].").
4. **Rules** — the concrete do's from the sources (each traceable to a source idea).
5. **Don'ts / Defects to fix** — the explicit anti-patterns the sources name (with WHY).
6. **Quality bar** — 4-6 checkable criteria an AI can verify its own draft against.

Rules: retain the sources' actual guidance (do not invent); quotes from the sources' examples may be adapted; compress wording; no filler. Target 2500-5000 characters. Output ONLY the skill file markdown starting with a `# ` title, wrapped in <final></final>."""


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", type=str, default="")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    groups: dict[str, list[Path]] = {}
    for f in sorted(SRC.glob("*.txt")):
        part = f.stem.split("__")[0]
        if args.only and args.only not in part:
            continue
        groups.setdefault(part, []).append(f)

    for part, files in groups.items():
        out_f = OUT / f"{part}.md"
        if out_f.exists() and out_f.stat().st_size > 1500 and not args.force:
            log(f"{part}: cached")
            continue
        corpus = "\n\n".join(
            f"===== SOURCE: {f.stem} =====\n" + f.read_text(encoding="utf-8", errors="replace")[:14000]
            for f in files
        )
        log(f"{part}: distilling {len(files)} sources ({len(corpus)} chars)...")
        try:
            d = await chat(
                PROMPT.format(part=part.replace("-", " "), n=len(files)) + "\n\n<sources>\n" + corpus + "\n</sources>",
                16384, min_len=1500,
            )
            d = re.sub(r"^<final>\n?|</final>\s*$", "", d).strip()
            if not d.startswith("# "):
                d = f"# Writing Part: {part.replace('-', ' ').title()}\n\n" + d
            out_f.write_text(d, encoding="utf-8")
            log(f"{part}: -> {len(d)} chars")
        except Exception as e:  # noqa: BLE001
            log(f"{part}: FAILED {str(e)[:140]}")


if __name__ == "__main__":
    asyncio.run(main())
