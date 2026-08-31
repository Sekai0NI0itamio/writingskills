#!/usr/bin/env python3
"""Extract the complete vocabulary of the 6/7 exemplar corpus.

Tokenizes texts/*.txt (already extracted PDFs), counts every word (connectors
included — "and", "hence" matter), and records dispersion (how many files use
it). Writes vocab/raw_counts.json: {word: {n, files}}.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXTS = ROOT / "texts"
OUT = ROOT / "vocab" / "raw_counts.json"

WORD_RE = re.compile(r"[a-zA-Z][a-zA-Z'\-]*[a-zA-Z]|[a-zA-Z]")


def main() -> None:
    counts: Counter = Counter()
    files_of: defaultdict = defaultdict(set)
    texts = sorted(TEXTS.glob("*.txt"))
    for txt in texts:
        text = txt.read_text(encoding="utf-8", errors="replace").lower()
        for w in WORD_RE.findall(text):
            counts[w] += 1
            files_of[w].add(txt.stem)
    data = {
        w: {"n": n, "files": len(files_of[w])}
        for w, n in counts.most_common()
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(data, indent=0), encoding="utf-8")
    print(f"{len(data)} unique words across {len(texts)} texts -> {OUT}")
    print(f"top 10: {[w for w, _ in counts.most_common(10)]}")
    total = sum(counts.values())
    print(f"total tokens: {total}")


if __name__ == "__main__":
    main()
