#!/usr/bin/env python3
"""Split each extracted essay text into section PARTS for per-section analysis.

Heading-aware first (numbered headings / ALL-CAPS headings / common IB section
names); falls back to paragraph-boundary chunks of ~1600 words. Writes
parts/parts.json: [{file, part, heading, text, words}].
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXTS = ROOT / "texts"
PARTS_DIR = ROOT / "parts"

HEADING_RE = re.compile(
    r"^\s*(?:\d+(?:\.\d+)*\s+[A-Z(\[]|[A-Z][A-Z \-/()&,]{4,}$|"
    r"(Introduction|Background|Aim|Hypothesis|Method|Methodology|Materials|Variables|"
    r"Procedure|Results|Raw Data|Data Processing|Data Analysis|Analysis|Discussion|"
    r"Evaluation|Conclusion|Abstract|References|Bibliography|Personal Engagement|"
    r"Exploration|Investigation|Research Question|Literature Review)\s*:?\s*$)",
    re.IGNORECASE,
)
TARGET_WORDS = 1600


def split_text(text: str) -> list[dict]:
    lines = text.splitlines()
    marks = [i for i, l in enumerate(lines) if HEADING_RE.match(l or "")]
    sections: list[tuple[str, list[str]]] = []
    if len(marks) >= 3:
        bounds = marks + [len(lines)]
        for a, b in zip(bounds, bounds[1:]):
            seg = lines[a:b]
            head = seg[0].strip().rstrip(":") or f"Section {a}"
            body = [l for l in seg[1:]]
            if sum(len(l.split()) for l in body) > 80:
                sections.append((head, body))
    if not sections:
        sections = [("Full text", lines)]

    parts: list[dict] = []
    for head, body in sections:
        # split long sections at paragraph boundaries
        words = 0
        chunk: list[str] = []
        chunks: list[list[str]] = []
        for line in body:
            chunk.append(line)
            words += len(line.split())
            if words >= TARGET_WORDS and line.strip() == "":
                chunks.append(chunk)
                chunk, words = [], 0
        if chunk and sum(len(l.split()) for l in chunk) > 60:
            chunks.append(chunk)
        elif chunk and chunks:
            chunks[-1].extend(chunk)
        elif chunk:
            chunks.append(chunk)
        if len(chunks) == 1:
            parts.append({"heading": head, "lines": chunks[0]})
        else:
            for i, c in enumerate(chunks, 1):
                parts.append({"heading": f"{head} (part {i})", "lines": c})

    out = []
    for i, p in enumerate(parts, 1):
        text_p = "\n".join(p["lines"]).strip()
        out.append({
            "part": i,
            "heading": p["heading"],
            "words": len(text_p.split()),
            "text": text_p,
        })
    return [p for p in out if p["words"] > 120]


def main() -> None:
    PARTS_DIR.mkdir(exist_ok=True)
    all_parts = []
    for txt in sorted(TEXTS.glob("*.txt")):
        text = txt.read_text(encoding="utf-8", errors="replace")
        if len(text.split()) < 250:
            continue
        parts = split_text(text)
        for p in parts:
            all_parts.append({"file": txt.stem, **p})
    (PARTS_DIR / "parts.json").write_text(json.dumps(all_parts, indent=1), encoding="utf-8")
    files = sorted({p["file"] for p in all_parts})
    print(f"{len(all_parts)} parts across {len(files)} files -> {PARTS_DIR/'parts.json'}")
    from collections import Counter
    per_file = Counter(p["file"] for p in all_parts)
    print(f"parts/file: min={min(per_file.values())} max={max(per_file.values())} avg={sum(per_file.values())/len(per_file):.1f}")


if __name__ == "__main__":
    main()
