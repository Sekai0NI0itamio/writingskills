#!/usr/bin/env python3
"""Build the vocab word-tree with MANY SMALL CATEGORIZERS.

Stage 1 — each AI agent processes ONLY 20 words: assigns each word to a
functional category and clusters near-interchangeable words together.
N categorizers run concurrently (default 20). Resumable: cache keyed by the
chunk's content hash.

Stage 2 — consolidation: per category, agents merge the stage-1 fragments
into canonical clusters (the big tree). Also concurrent + resumable.

Output vocab/tree.json: [{category, name, words: [[word, count], ...]}]

  python3 scripts/vocab/build_tree.py [--min-count 2] [--words-per-agent 20]
      [--in-flight 20] [--test-one] [--reset]
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import chat, log  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "vocab" / "raw_counts.json"
OUT = ROOT / "vocab" / "tree.json"
CACHE = ROOT / "cache" / "vocab_tree"

CATEGORIES = [
    "connectors", "reasoning", "explanatory", "descriptive", "academic",
    "hedges", "quantity", "reporting", "contrast", "function",
]

CATEGORIZE_PROMPT = """You are building a VOCABULARY TREE from words 6/7-graded IB students actually use (corpus counts attached). You get ONLY {n} words — categorize and cluster them precisely.

Cluster the words into groups of NEAR-INTERCHANGEABLE words — words a student could swap for each other in the same sentence slot without changing the meaning. Rules:
- Assign each of the {n} words to exactly ONE cluster. Every input word must appear in the output.
- Cluster by FUNCTION IN A SENTENCE, not topic: "carry, bring, provide, offer" belong together (ways a subject acts on an object); "instruction, direction, guideline" together (things you follow).
- Each cluster gets a "category" from EXACTLY this list:
  connectors | reasoning | explanatory | descriptive | academic | hedges | quantity | reporting | contrast | function
  (connectors = and/or/plus/alongside...; reasoning = therefore/hence/consequently...; contrast = however/whereas/although...; explanatory = defined as/modelled by/which means...; descriptive = qualities and how-to-describe words (odd, noticeable, rapid, substantial...); academic = formal register; hedges = may/perhaps/relatively...; quantity = amount/measurement phrasing; reporting = according to/reveals/suggests...; function = grammatical words with no better home.)
- Keep clusters SMALL and tight (2-8 words). Give each cluster a short reusable name (e.g. "verbs of bringing relief", "connective: addition", "adjectives for noticeable difference").
- Keep words within a cluster ordered most frequent first.
- Do not invent words that are not in the input.

Output STRICT JSON only (wrapped in <final></final>), shaped exactly:
{"category_batches":[{"category":"<category>","clusters":[{"name":"<name>","words":[["word",count],...]}]}]}
Use ONE batch per category you used. Every input word appears exactly once across all batches."""

CONSOLIDATE_PROMPT = """You are consolidating fragments of a VOCABULARY TREE for the category "{category}". Below are cluster fragments produced by many small agents (each fragment: a name and words with corpus counts). Merge them into CANONICAL clusters:

- Merge fragments whose words are near-interchangeable (same sentence-slot function) into ONE canonical cluster; give it the clearest reusable name.
- Split mixed fragments if a fragment genuinely contains two distinct functions.
- Deduplicate words (a word appears in exactly one canonical cluster; keep its max count).
- Keep words within each cluster ordered most frequent first. Do not invent words.
- Target 3-15 words per canonical cluster; a true singleton stays its own cluster.

Output STRICT JSON only (wrapped in <final></final>), shaped exactly:
{"clusters":[{"name":"<name>","words":[["word",count],...]}]}"""


def load_words(min_count: int) -> list[list]:
    d = json.loads(RAW.read_text())
    return [[w, v["n"]] for w, v in d.items() if v["n"] >= min_count]


def parse_final_json(raw: str) -> dict | None:
    m = re.search(r"<final>([\s\S]*?)(?:</final>|\Z)", raw)
    body = (m.group(1) if m else raw).strip()
    if body.startswith("```"):
        body = body.strip("`")
        if body.startswith("json"):
            body = body[4:]
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        s, e = body.find("{"), body.rfind("}")
        if 0 <= s < e:
            try:
                return json.loads(body[s:e + 1])
            except json.JSONDecodeError:
                return None
    return None


def extract_batches(d: dict) -> list[dict]:
    """Normalize: [{"category":..., "clusters":[{"name","words"}]}]."""
    out = []
    for b in d.get("category_batches", []) or d.get("groups", []) or []:
        cat = (b.get("category") or "function").strip().lower()
        if cat not in CATEGORIES:
            cat = "function"
        for c in b.get("clusters", []) or []:
            words = []
            for entry in c.get("words", []):
                if isinstance(entry, (list, tuple)) and len(entry) >= 2:
                    w = str(entry[0] or "").strip().lower()
                    n = entry[1] if isinstance(entry[1], (int, float)) else 0
                elif isinstance(entry, str):
                    w, n = entry.strip().lower(), 0
                else:
                    continue
                if w:
                    words.append([w, int(n)])
            if words:
                out.append({"category": cat, "name": (c.get("name") or "unnamed").strip(), "words": words})
    return out


def _git_commit(done_n: int) -> None:
    """Commit+push finished fragments so a hard timeout loses almost nothing."""
    try:
        import subprocess
        subprocess.run(["git", "add", "cache/vocab_tree"], cwd=ROOT, capture_output=True, timeout=60)
        r = subprocess.run(["git", "commit", "-m", f"vocab tree progress: {done_n} chunks done"], cwd=ROOT, capture_output=True, timeout=60)
        if r.returncode == 0:
            subprocess.run(["git", "pull", "--rebase", "origin", "main"], cwd=ROOT, capture_output=True, timeout=120)
            p = subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=ROOT, capture_output=True, timeout=120)
            log(f"progress commit pushed ({done_n} chunks, rc={p.returncode})")
    except Exception as e:  # noqa: BLE001
        log(f"progress commit failed: {redact(str(e))[:120]}")


def chunk_hash(words: list[list]) -> str:
    h = hashlib.sha1(json.dumps(words, separators=(",", ":")).encode()).hexdigest()[:12]
    return h


async def categorize_word_chunks(words: list[list], per_agent: int, in_flight: int, deadline: float | None = None, commit_every: int = 0) -> list[dict]:
    chunks = [words[i:i + per_agent] for i in range(0, len(words), per_agent)]
    sem = asyncio.Semaphore(in_flight)
    frag_path = CACHE / "fragments.jsonl"

    done_hashes: set[str] = set()
    if frag_path.exists():
        for line in frag_path.read_text().splitlines():
            try:
                done_hashes.add(json.loads(line)["hash"])
            except Exception:
                pass
    todo = [c for c in chunks if chunk_hash(c) not in done_hashes]
    log(f"stage 1: {len(chunks)} categorizers x {per_agent} words ({len(done_hashes)} cached, {len(todo)} to run, in-flight {in_flight})")

    progress = {"done": 0}

    async def run_chunk(chunk: list[list]) -> None:
        if deadline is not None and time.time() > deadline:
            return  # past the graceful stop — this chunk re-runs in the next chained run
        h = chunk_hash(chunk)
        async with sem:
            payload = json.dumps(chunk, separators=(",", ":"))
            d = None
            for try_n in range(2):
                raw = await chat(CATEGORIZE_PROMPT.replace("{n}", str(len(chunk))) + "\n\n<words>\n" + payload + "\n</words>", max_tokens=65536)
                d = parse_final_json(raw)
                if d:
                    break
            if not d:
                log(f"  categorizer failed twice ({chunk[0][0]}...{chunk[-1][0]}) — skipped")
                return
            frags = extract_batches(d)
            covered = sum(len(f["words"]) for f in frags)
            async with _write_lock:
                with frag_path.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({"hash": h, "frags": frags}) + "\n")
            progress["done"] += 1
            if commit_every > 0 and progress["done"] % commit_every == 0:
                await asyncio.get_running_loop().run_in_executor(None, _git_commit, progress["done"])
            if progress["done"] % 25 == 0:
                from common import health_snapshot
                stats = health_snapshot()
                mix = ", ".join(f"{m.split('/')[-1]}={v['ok']}" for m, v in sorted(stats.items(), key=lambda x: -x[1]["ok"]) if v["ok"])
                log(f"  categorizers done: {progress['done']}/{len(todo)} | producing: {mix or 'none yet'}")

    _write_lock = asyncio.Lock()
    await asyncio.gather(*(run_chunk(c) for c in todo))

    fragments: list[dict] = []
    if frag_path.exists():
        for line in frag_path.read_text().splitlines():
            try:
                fragments.extend(json.loads(line)["frags"])
            except Exception:
                continue
    log(f"stage 1 complete: {len(fragments)} cluster fragments")
    return fragments


async def consolidate(fragments: list[dict], in_flight: int) -> list[dict]:
    by_cat: dict[str, list[dict]] = {}
    for f in fragments:
        by_cat.setdefault(f["category"], []).append(f)

    jobs = []
    for cat, frags in by_cat.items():
        # pack fragments into consolidation batches (~40 fragments each)
        for i in range(0, len(frags), 40):
            jobs.append((cat, frags[i:i + 40], i))

    sem = asyncio.Semaphore(in_flight)
    cons_path = CACHE / "consolidated.jsonl"
    done_hashes: set[str] = set()
    if cons_path.exists():
        for line in cons_path.read_text().splitlines():
            try:
                done_hashes.add(json.loads(line)["hash"])
            except Exception:
                pass
    todo = [(cat, frags, i, chunk_hash([[w, n] for f in frags for w, n in f["words"]]))
            for cat, frags, i in jobs
            if chunk_hash([[w, n] for f in frags for w, n in f["words"]]) not in done_hashes]
    log(f"stage 2: {len(jobs)} consolidation batches ({len(done_hashes)} cached, {len(todo)} to run)")

    async def run_batch(cat: str, frags: list[dict], i: int, h: str) -> None:
        async with sem:
            payload = json.dumps([{"name": f["name"], "words": f["words"]} for f in frags], indent=0)
            d = None
            for try_n in range(2):
                raw = await chat(CONSOLIDATE_PROMPT.replace("{category}", cat) + "\n\n<fragments>\n" + payload + "\n</fragments>", max_tokens=65536)
                d = parse_final_json(raw)
                if d and d.get("clusters"):
                    break
            if not d or not d.get("clusters"):
                log(f"  consolidation failed twice ({cat} batch {i}) — keeping raw fragments")
                clusters = frags
            else:
                clusters = [{"category": cat, "name": c.get("name") or "unnamed",
                             "words": [[(w or "").strip().lower(),
                                        int(n) if isinstance(n, (int, float)) else 0]
                                       for w, n in c.get("words", []) if (w or "").strip()]}
                            for c in d["clusters"]]
                clusters = [c for c in clusters if c["words"]]
            async with _c_lock:
                with cons_path.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({"hash": h, "clusters": clusters}) + "\n")

    _c_lock = asyncio.Lock()
    await asyncio.gather(*(run_batch(*j) for j in todo))

    clusters: list[dict] = []
    if cons_path.exists():
        for line in cons_path.read_text().splitlines():
            try:
                clusters.extend(json.loads(line)["clusters"])
            except Exception:
                continue
    return clusters


def dedupe_words(clusters: list[dict]) -> list[dict]:
    """A word lives in exactly one cluster: the one where it ranks highest."""
    best: dict[str, tuple[int, int, dict]] = {}  # word -> (count, -index, cluster)
    for idx, c in enumerate(clusters):
        for w, n in c["words"]:
            rank = sum(1 for _, wn in c["words"] if wn > n)
            prev = best.get(w)
            if prev is None or (n, -rank) > (prev[0], -prev[1]):
                best[w] = (n, rank, c)
    # rebuild: keep each word only in its best cluster, preserve order
    for c in clusters:
        seen: set[str] = set()
        kept = []
        for w, n in c["words"]:
            if w in seen:
                continue
            owner = best.get(w)
            if owner is not None and owner[2] is c:
                kept.append([w, n])
                seen.add(w)
        c["words"] = kept
    return [c for c in clusters if c["words"]]


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-count", type=int, default=2)
    ap.add_argument("--words-per-agent", type=int, default=20)
    ap.add_argument("--in-flight", type=int, default=20)
    ap.add_argument("--test-one", action="store_true")
    ap.add_argument("--reset", action="store_true")
    ap.add_argument("--max-minutes", type=int, default=0, help="graceful stop: finish in-flight, skip new chunks after N minutes (0 = no limit)")
    ap.add_argument("--commit-every", type=int, default=0, help="git commit+push fragments every N new chunks (0 = off)")
    args = ap.parse_args()

    if args.reset and CACHE.exists():
        import shutil
        shutil.rmtree(CACHE)
        log("cache cleared")
    CACHE.mkdir(parents=True, exist_ok=True)

    words = load_words(args.min_count)
    log(f"{len(words)} words (count >= {args.min_count})")
    log(f"providers: ORCA_API_KEY {'set' if os.environ.get('ORCA_API_KEY') else 'MISSING'} | OPENROUTER_API_KEY {'set' if os.environ.get('OPENROUTER_API_KEY') else 'MISSING'}")
    deadline = time.time() + args.max_minutes * 60 if args.max_minutes > 0 else None

    # WORD-LEVEL resume: fragments.jsonl is the source of truth — every word
    # already clustered there is skipped, whatever happens to chunk hashes.
    frag_path = CACHE / "fragments.jsonl"
    done_words: set[str] = set()
    if frag_path.exists():
        for line in frag_path.read_text().splitlines():
            try:
                for f in json.loads(line)["frags"]:
                    for w, _n in f["words"]:
                        done_words.add(w)
            except Exception:
                continue
    todo_words = [w for w in words if w[0] not in done_words]
    log(f"resume: {len(done_words)} words already clustered, {len(todo_words)} remain")
    log(f"providers: ORCA_API_KEY {'set' if os.environ.get('ORCA_API_KEY') else 'MISSING'} | OPENROUTER_API_KEY {'set' if os.environ.get('OPENROUTER_API_KEY') else 'MISSING'}")

    if args.test_one:
        chunk = words[: args.words_per_agent]
        raw = await chat(CATEGORIZE_PROMPT.replace("{n}", str(len(chunk))) + "\n\n<words>\n" + json.dumps(chunk, separators=(",", ":")) + "\n</words>", max_tokens=16384)
        print(json.dumps(extract_batches(parse_final_json(raw) or {}), indent=1)[:2200])
        return

    t0 = time.time()
    fragments = await categorize_word_chunks(todo_words, args.words_per_agent, args.in_flight, deadline, args.commit_every)
    # re-attach the previously cached fragments so consolidation sees everything
    if frag_path.exists():
        for line in frag_path.read_text().splitlines():
            try:
                fragments.extend(json.loads(line)["frags"])
            except Exception:
                continue
    clusters = await consolidate(fragments, args.in_flight)
    raw = json.loads(RAW.read_text())
    for c in clusters:
        c["words"] = [[w, raw.get(w, {}).get("n", n)] for w, n in c["words"]]
    clusters = dedupe_words(clusters)

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({"categories": CATEGORIES, "clusters": clusters}, indent=1), encoding="utf-8")
    by_cat: dict[str, int] = {}
    for c in clusters:
        by_cat[c["category"]] = by_cat.get(c["category"], 0) + len(c["words"])
    log(f"tree: {len(clusters)} canonical clusters, {sum(len(c['words']) for c in clusters)} words, {time.time() - t0:.0f}s -> {OUT}")
    log("words per category: " + ", ".join(f"{k}={v}" for k, v in sorted(by_cat.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    asyncio.run(main())
