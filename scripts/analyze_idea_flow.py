#!/usr/bin/env python3
"""IdeaThinkingFlow analyzer — one AI agent per SECTION PART of each essay.

For every part (from parts/parts.json) an agent dissects HOW the student
expresses ideas in that section:
  - paragraph logic flow, move by move (what each sentence DOES, how each idea
    hands to the next)
  - what to talk about, in what order, for this section type
  - paragraph SKELETONS: slot templates + fill instructions + a filled example
    from THIS text + one "different idea" demonstration
  - express-idea vocabulary (logic-carrying connectives, explanation verbs,
    hedges)
  - the explanation pattern used, with replication steps

Concurrency: 5 agents per file, multiple files in flight (global cap via
--in-flight). Resumable: notes/<file>__partNN.md skipped if present. Live
progress table. Outputs notes/ + flow_index.json.

  python3 scripts/analyze_idea_flow.py [--limit-files N] [--in-flight 15]
      [--per-file 5] [--only FILE_SUBSTR]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import MODEL, chat, log, redact, run_bounded  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "parts" / "parts.json"
NOTES = ROOT / "notes"

PROMPT = """You are analyzing HOW a 6/7-graded IB student expresses ideas in ONE section of their coursework. This is about LOGICAL FLOW and idea expression — not vocabulary lists, not grammar rules, not the topic content itself.

Below is the section text ({heading}, {words} words).

Produce markdown with EXACTLY these five sections:

## Paragraph Flow (move by move)
For EACH paragraph in order: number it, then map it sentence-by-sentence as moves. Name what each sentence DOES (claim, context, definition, evidence, unpack, mechanism, implication, comparison, transition, example, verdict...), quote 3-8 words of it, and state HOW it hands the reader to the next sentence (what makes the next sentence follow logically — answer, cause, contrast, consequence, specification, new instance...). The point: the reader must see the LOGIC PATH of the paragraph, not a summary of it.

## What This Section Does (content sequence)
The ordered list of content moves this section type makes (e.g. for a method section: materials first, then setup, then procedure with reasons inline...). State what comes 1st, 2nd, 3rd... and WHY that order (what each move sets up for the next). Generalize so another student could replicate the sequence with a different topic.

## Paragraph Skeletons (replicable templates)
Extract 2-4 paragraph-level skeletons from this section: a slot template of the WHOLE paragraph, e.g.
   SKELETON: "[Personal observation that puzzled you]. This intrigued me as [why it mattered to you], since [the general principle it touches]. [Term] is defined as [definition]; in [the investigated context] it [application]."
For EACH skeleton give:
   1. What each slot holds (and its grammatical shape).
   2. HOW to fill it with a DIFFERENT idea — concrete instructions (e.g. "slot 1: pick a moment where you personally met the phenomenon; state it in past tense with one concrete detail").
   3. The original filled version (quote/paraphrase from THIS text).
   4. A demonstration fill with a COMPLETELY different idea (different subject, same skeleton).

## Express-Idea Vocabulary
The connectives and verbs THIS section uses to move logic forward, grouped by job: sequencing ("firstly", "following this"), cause/consequence ("therefore", "hence", "as a result"), contrast/concession ("however", "whereas", "although"), specification ("in particular", "that is"), evidence handling ("according to", "this suggests"), and explanation verbs ("defined as", "modelled by", "can be explained by"). Quote the actual phrase + 3-6 words of its sentence.

## How to Explain an Idea (replication steps)
Name THE explanation pattern this section relies on (definition→unpack→example→implication? cause chain? authority→application? worked calculation? comparison?) and give step-by-step instructions to explain a NEW idea with the same pattern (numbered steps, each step one action).

HARD RULES: every claim carries a short verbatim quote from the text; mechanisms not praise; no filler; no comments about the topic's quality; skeletons must be ABSTRACT enough to carry a different idea but SPECIFIC enough to rebuild the rhythm."""

INDEX_NAME = ROOT / "notes" / "_index.json"


def _git_commit(done_n: int) -> None:
    """Commit+push finished notes so a hard timeout loses almost nothing."""
    try:
        subprocess.run(["git", "add", "notes"], cwd=ROOT, capture_output=True, timeout=60)
        r = subprocess.run(["git", "commit", "-m", f"idea-flow progress: {done_n} parts done"],
                           cwd=ROOT, capture_output=True, timeout=60)
        if r.returncode == 0:
            subprocess.run(["git", "pull", "--rebase", "origin", "main"], cwd=ROOT, capture_output=True, timeout=120)
            p = subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=ROOT, capture_output=True, timeout=120)
            log(f"progress commit pushed ({done_n} parts done, rc={p.returncode})")
    except Exception as e:  # noqa: BLE001
        log(f"progress commit failed: {redact(str(e))[:120]}")


def load_jobs(limit_files: int, only: str) -> list[dict]:
    data = json.loads(PARTS.read_text())
    files = sorted({p["file"] for p in data})
    if only:
        files = [f for f in files if only.lower() in f.lower()]
    if limit_files:
        files = files[:limit_files]
    allow = set(files)
    return [p for p in data if p["file"] in allow]


async def analyze_part(job: dict, stats: dict, done_count: dict) -> None:
    slug = f"{job['file']}__part{job['part']:02d}"
    out = NOTES / f"{slug}.md"
    if out.exists() and out.stat().st_size > 600:
        done_count["skipped"] += 1
        stats[job["file"]]["status"] = "cached"
        return
    prompt = PROMPT.format(heading=job["heading"], words=job["words"]) + "\n\n<text>\n" + job["text"][:16000] + "\n</text>"
    try:
        result = await chat(prompt, max_tokens=8192)
        out.write_text(
            f"# Idea Flow Notes: {job['file']} — {job['heading']}\n\n{result}\n",
            encoding="utf-8",
        )
        done_count["done"] += 1
        stats[job["file"]]["status"] = "working"
        stats[job["file"]]["done"] += 1
    except Exception as e:  # noqa: BLE001
        done_count["failed"] += 1
        stats[job["file"]]["status"] = f"err: {str(e)[:28]}"
        log(f"FAILED {slug}: {redact(str(e))[:120]}")


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit-files", type=int, default=0)
    ap.add_argument("--in-flight", type=int, default=15, help="global concurrent agents")
    ap.add_argument("--per-file", type=int, default=5, help="max concurrent agents per file")
    ap.add_argument("--only", type=str, default="", help="process files whose name contains this")
    ap.add_argument("--max-minutes", type=int, default=0, help="graceful stop: finish in-flight, skip new parts after N minutes (0 = no limit)")
    ap.add_argument("--commit-every", type=int, default=0, help="git commit+push notes every N newly analyzed parts (0 = off)")
    args = ap.parse_args()

    NOTES.mkdir(exist_ok=True)
    jobs = load_jobs(args.limit_files, args.only)
    if not jobs:
        print("no jobs — run extract_texts.py and split_sections.py first")
        sys.exit(1)
    files = sorted({j["file"] for j in jobs})
    log(f"{len(jobs)} parts across {len(files)} files | model={MODEL} | in-flight={args.in_flight} (per-file cap {args.per_file})")

    stats: dict[str, dict] = {f: {"status": "queued", "done": 0} for f in files}
    done_count = {"done": 0, "skipped": 0, "failed": 0}
    total = len(jobs)
    start = time.time()
    deadline = start + args.max_minutes * 60 if args.max_minutes > 0 else None
    since_commit = {"n": 0}

    file_sems: dict[str, asyncio.Semaphore] = {f: asyncio.Semaphore(args.per_file) for f in files}
    global_sem = asyncio.Semaphore(args.in_flight)

    async def worker(job: dict):
        if deadline is not None and time.time() > deadline:
            return  # past the graceful stop — this part re-runs in the next chained run
        async with global_sem:
            async with file_sems[job["file"]]:
                await analyze_part(job, stats, done_count)
                if args.commit_every > 0 and done_count["done"] > 0 and done_count["done"] % args.commit_every == 0 \
                        and since_commit["n"] != done_count["done"]:
                    since_commit["n"] = done_count["done"]
                    await asyncio.get_running_loop().run_in_executor(None, _git_commit, done_count["done"])

    stop = False

    async def progress():
        while not stop:
            el = time.time() - start
            sys.stdout.write("\033[2J\033[H")
            left = f" | stop in {max(0, int((deadline - time.time()) / 60))}m" if deadline else ""
            print(f"IdeaThinkingFlow — {len(jobs)} parts | done {done_count['done'] + done_count['skipped']}/{total} "
                  f"(cached {done_count['skipped']}, failed {done_count['failed']}) | {el:.0f}s{left} | model {MODEL}")
            print("-" * 104)
            print(f"{'File':<56} {'Status':<18} {'Parts done':<12}")
            print("-" * 104)
            for f in files:
                s = stats[f]
                print(f"{f[:54]:<56} {s['status']:<18} {s['done']:<12}")
            print("-" * 104)
            sys.stdout.flush()
            await asyncio.sleep(2)

    tasks = [asyncio.create_task(worker(j)) for j in jobs]
    prog = asyncio.create_task(progress())
    await asyncio.gather(*tasks)
    stop = True
    prog.cancel()
    try:
        await prog
    except asyncio.CancelledError:
        pass

    # write index for the distiller
    index = []
    for p in jobs:
        slug = f"{p['file']}__part{p['part']:02d}"
        f = NOTES / f"{slug}.md"
        if f.exists() and f.stat().st_size > 600:
            index.append({"file": p["file"], "part": p["part"], "heading": p["heading"], "note": str(f.relative_to(ROOT))})
    INDEX_NAME.write_text(json.dumps(index, indent=1), encoding="utf-8")
    remaining = sum(1 for j in jobs if not (NOTES / f"{j['file']}__part{j['part']:02d}.md").exists())
    log(f"complete: {done_count['done']} analyzed, {done_count['skipped']} cached, {done_count['failed']} failed — {remaining} parts remain — index at {INDEX_NAME}")
    (NOTES / "_remaining.txt").write_text(str(remaining), encoding="utf-8")


if __name__ == "__main__":
    asyncio.run(main())
