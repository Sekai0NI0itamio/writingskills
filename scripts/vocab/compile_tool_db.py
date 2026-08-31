#!/usr/bin/env python3
"""Compile the vocab tree into the runtime database for the vocab-diversity tool.

Reads vocab/tree.json and produces:
  vocab/tool_db.json — {word: {"alts": [[alt, count], ...top 6], "group": name,
                              "category": cat, "n": own count}}
     alternatives = the word's cluster siblings ranked by student frequency.
  vocab/VOCAB-DIVERSITY.md — human-readable summary of the tree.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TREE = ROOT / "vocab" / "tree.json"
DB_OUT = ROOT / "vocab" / "tool_db.json"
MD_OUT = ROOT / "vocab" / "VOCAB-DIVERSITY.md"


def main() -> None:
    tree = json.loads(TREE.read_text())
    clusters = tree["clusters"]
    db: dict = {}
    for c in clusters:
        name, cat = c["name"], c["category"]
        words = c["words"]
        for w, n in words:
            alts = [[aw, an] for aw, an in words if aw != w]
            alts.sort(key=lambda x: -x[1])
            entry = db.setdefault(w, {"alts": [], "groups": []})
            entry["groups"].append({"group": name, "category": cat, "n": n})
            seen = {a for a, _ in entry["alts"]}
            entry["alts"].extend([a, an] for a, an in alts if a not in seen)
            entry["alts"].sort(key=lambda x: -x[1])
            entry["alts"] = entry["alts"][:8]
    # finalize: primary group = the one where the word ranks highest
    for w, e in db.items():
        e["groups"].sort(key=lambda g: -g["n"])
        e["group"] = e["groups"][0]["group"]
        e["category"] = e["groups"][0]["category"]
        e["n"] = e["groups"][0]["n"]
        del e["groups"]
    DB_OUT.write_text(json.dumps(db, indent=0), encoding="utf-8")

    # human-readable summary
    lines = ["# Vocab Diversity — Word Tree (6/7 exemplar corpus)", "",
             f"{len(clusters)} clusters, {len(db)} words with alternatives.", ""]
    by_cat: dict = {}
    for c in clusters:
        by_cat.setdefault(c["category"], []).append(c)
    for cat in sorted(by_cat):
        lines.append(f"## {cat} ({sum(len(c['words']) for c in by_cat[cat])} words)")
        for c in sorted(by_cat[cat], key=lambda c: -sum(n for _, n in c["words"]))[:12]:
            top = ", ".join(f"{w} ({n})" for w, n in c["words"][:8])
            lines.append(f"- **{c['name']}**: {top}")
        if len(by_cat[cat]) > 12:
            lines.append(f"- … and {len(by_cat[cat]) - 12} more clusters")
        lines.append("")
    MD_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"tool_db: {len(db)} words -> {DB_OUT} ({DB_OUT.stat().st_size} bytes)")
    print(f"summary -> {MD_OUT}")


if __name__ == "__main__":
    main()
