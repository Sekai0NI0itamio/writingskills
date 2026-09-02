#!/usr/bin/env python3
"""Build the vocab tree V2 — established linguist resources as the spine.

Sources (all in vocab/sources/ or vocab/):
  AKL.json   — Academic Keyword List: 930 structuring words by POS
  AVL.json   — COCA academic frequency bands (120M-word academic corpus)
  AWL/NAWL/UWL.json — academic word families
  moby_thesaurus.txt — Moby Thesaurus II synonym groups (30,259 lines)
  raw_counts.json — OUR 6/7 IB corpus: the student-usage signal
  ../tree.json (v1) — the agent-clustered categories, reused where good

Output: vocab/tool_db.json v2 (same schema — drop-in for vocab-diversity) and
vocab/tree-v2.json (the full categorized tree).

Deterministic — no AI calls. Run: python3 scripts/vocab/build_tree_v2.py
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V = ROOT / "vocab"
S = V / "sources"

GRAMMAR = {
    "a", "an", "the", "of", "to", "in", "at", "for", "with", "from", "by", "on",
    "it", "its", "than", "as", "is", "are", "was", "were", "be", "been", "am",
    "this", "these", "those", "that", "which", "who", "and", "or", "if", "not",
    "there", "their", "they", "he", "she", "we", "i", "you", "s", "will",
}

AKL_POS_CATEGORY = {
    "Nouns": "academic",
    "Verbs": "explanatory",
    "Adjectives": "descriptive",
    "Adverbs": "connectors",
    "Others": "function",
}


def norm(w: str) -> str:
    return (w or "").strip().lower()


def main() -> None:
    # ── load sources ────────────────────────────────────────────────────
    akl = json.loads((S / "AKL.json").read_text())
    awl = json.loads((S / "AWL.json").read_text())
    nawl = json.loads((S / "NAWL.json").read_text())
    uwl = json.loads((S / "UWL.json").read_text())
    avl = json.loads((S / "AVL.json").read_text())
    raw = json.loads((V / "raw_counts.json").read_text())
    corpus = {w: v["n"] for w, v in raw.items()}

    # v1 tree: agent-assigned categories + clusters
    v1_clusters: list[dict] = []
    v1_cat: dict[str, str] = {}
    v1_tree = V / "tree.json"
    if v1_tree.exists():
        t = json.loads(v1_tree.read_text())
        v1_clusters = t.get("clusters", [])
        for c in v1_clusters:
            for w, _n in c["words"]:
                v1_cat.setdefault(w, c["category"])

    # ── universe + category assignment ──────────────────────────────────
    info: dict[str, dict] = defaultdict(lambda: {"sources": set(), "corpus": 0, "avl_band": None, "category": None})

    for w, n in corpus.items():
        if n >= 2:
            info[w]["corpus"] = n
            info[w]["sources"].add("corpus")

    for pos, words in akl.items():
        cat = AKL_POS_CATEGORY.get(pos, "academic")
        for w in words:
            w = norm(w)
            if not w:
                continue
            info[w]["sources"].add("AKL")
            if info[w]["category"] is None:
                info[w]["category"] = cat

    def add_families(data: dict, source: str) -> None:
        for _k, fam in data.items():
            if isinstance(fam, dict):
                for head, sub in fam.items():
                    w = norm(head)
                    if w:
                        info[w]["sources"].add(source)
                    subwords = []
                    if isinstance(sub, dict):
                        subwords = sub.get("subwords") or []
                    elif isinstance(sub, list):
                        subwords = sub
                    for sw in subwords or []:
                        sw = norm(sw)
                        if sw:
                            info[sw]["sources"].add(source)
            elif isinstance(fam, list):
                for w in fam:
                    w = norm(w)
                    if w:
                        info[w]["sources"].add(source)

    add_families(awl, "AWL")
    add_families(nawl, "NAWL")
    # UWL is {level: [words]}
    for _lvl, words in uwl.items():
        for w in words:
            w = norm(w)
            if w:
                info[w]["sources"].add("UWL")

    for band in sorted(avl.keys()):
        bnum = int(band.split("_")[1]) if "_" in band else 16
        for w, meta in avl[band].items():
            w = norm(w)
            if not w:
                continue
            info[w]["sources"].add("AVL")
            if info[w]["avl_band"] is None:
                info[w]["avl_band"] = bnum

    # category: v1 agent category > AKL POS > source default > function
    for w, e in info.items():
        if e["category"] is None:
            if w in v1_cat:
                e["category"] = v1_cat[w]
            elif "AWL" in e["sources"] or "NAWL" in e["sources"] or "AVL" in e["sources"] or "UWL" in e["sources"]:
                e["category"] = "academic"
            elif e["corpus"] > 0:
                e["category"] = "function"
    # words with no category and no corpus presence still default sensibly
    for w, e in info.items():
        if e["category"] is None:
            e["category"] = "academic"

    log_words = len(info)
    print(f"universe: {log_words} words")

    # ── synonym structure ───────────────────────────────────────────────
    # Moby: line = comma-separated synonym group. We track CO-OCCURRENCE
    # strength (how many lines contain both words) — words sharing many lines
    # are close synonyms; single-line co-members are loose associations.
    moby: dict[str, set[str]] = defaultdict(set)
    cooc: dict[str, Counter] = defaultdict(Counter)
    moby_path = S / "moby_thesaurus.txt"
    if moby_path.exists():
        for line in moby_path.read_text(encoding="utf-8", errors="replace").splitlines():
            group = [norm(w) for w in line.split(",")]
            group = [g for g in group if g]
            if len(group) > 120:
                continue  # mega-lines are junk associations
            for w in group:
                moby[w].update(g for g in group if g != w)
            for w in set(group):
                for g in group:
                    if g != w:
                        cooc[w][g] += 1

    # v1 cluster siblings
    v1_sib: dict[str, dict[str, int]] = defaultdict(dict)
    for c in v1_clusters:
        ws = [(w, n) for w, n in c["words"]]
        for w, n in ws:
            for ow, on in ws:
                if ow != w:
                    v1_sib[w][ow] = max(v1_sib[w].get(ow, 0), on)

    # ── score helper: student corpus count, else AVL-band proxy ─────────
    def score(w: str) -> int:
        c = info.get(w, {}).get("corpus", 0)
        if c:
            return c
        b = info.get(w, {}).get("avl_band")
        if b:
            return max(1, 4000 // (b * 40))
        return 0

    # ── build the tree + db ─────────────────────────────────────────────
    db: dict[str, dict] = {}
    tree_clusters: list[dict] = []

    for w in sorted(info.keys()):
        e = info[w]
        cat = e["category"]
        # candidate alternatives: ranked by synonym CO-OCCURRENCE strength
        # (Moby lines shared), then corpus frequency. Super-generic words
        # (corpus count > 3000) are excluded — they fit every slot and none.
        cands: Counter = Counter()
        for cand in moby.get(w, set()):
            if cand in info and cand != w and cand not in GRAMMAR and info[cand].get("corpus", 0) <= 3000:
                strength = cooc[w][cand] * 50 + min(score(cand), 200) + 1
                cands[cand] += strength
        for cand, n in v1_sib.get(w, {}).items():
            if cand in info and cand != w and cand not in GRAMMAR:
                cands[cand] += max(n, 100) * 3 + 50  # v1 agent clusters weighted up
        # same-category alternatives first
        same = [(c, s) for c, s in cands.items() if info[c]["category"] == cat]
        other = [(c, s) for c, s in cands.items() if info[c]["category"] != cat]
        same.sort(key=lambda x: -x[1])
        other.sort(key=lambda x: -x[1])
        alts = same[:8] or other[:8]
        if not alts:
            continue
        db[w] = {
            "alts": [[a, s] for a, s in alts],
            "group": cat + " vocabulary",
            "category": cat,
            "n": max(e["corpus"], score(w)),
        }
        tree_clusters.append({"category": cat, "name": f"{cat} set: {w}", "words": [[w, db[w]["n"]]] + [[a, s] for a, s in alts]})

    # merge per-word sets into real clusters (connected components over alt edges)
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for w, e in db.items():
        for a, _s in e["alts"]:
            if a in db:
                rw, ra = find(w), find(a)
                if rw != ra:
                    parent[ra] = rw

    groups: dict[str, list[str]] = defaultdict(list)
    for w in db:
        groups[find(w)].append(w)

    tree_v2 = []
    for _root, members in groups.items():
        cats = Counter(db[m]["category"] for m in members)
        cat = cats.most_common(1)[0][0]
        words = sorted(members, key=lambda m: -db[m]["n"])
        tree_v2.append({"category": cat, "name": f"{cat} family ({len(words)} words)", "words": [[m, db[m]["n"]] for m in words]})
    tree_v2.sort(key=lambda c: -sum(n for _, n in c["words"]))

    (V / "tree-v2.json").write_text(json.dumps({"categories": sorted({c["category"] for c in tree_v2}), "clusters": tree_v2}, indent=1), encoding="utf-8")
    (V / "tool_db.json").write_text(json.dumps(db, indent=0), encoding="utf-8")
    print(f"tool_db v2: {len(db)} words -> {V / 'tool_db.json'} ({(V / 'tool_db.json').stat().st_size} bytes)")
    print(f"tree v2: {len(tree_v2)} families")
    cats = Counter(e["category"] for e in db.values())
    print("by category:", dict(cats.most_common()))


if __name__ == "__main__":
    main()
