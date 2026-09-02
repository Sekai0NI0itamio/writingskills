#!/usr/bin/env python3
"""Fetch writing-guide source pages with Safari (local, passes bot-walls).

Loads each URL in a background Safari tab, extracts the main article text,
saves to sources/writing-parts/<part>__<site>.txt. Run locally:
  python3 scripts/writing_parts/fetch_sources.py
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "/Users/stevennovak/Desktop/Important/MCP Tool Service Provider/SafariBrowserWebIntegration")
from safari_core import SafariCore  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "sources" / "writing-parts"

PARTS: dict[str, list[str]] = {
    "introduction": [
        "https://writingcenter.fas.harvard.edu/beginnings-and-endings",
        "https://writingcenter.unc.edu/tips-and-tools/introductions/",
    ],
    "thesis": [
        "https://writingcenter.fas.harvard.edu/resource/thesis",
        "https://writingcenter.unc.edu/tips-and-tools/thesis-statements/",
    ],
    "conclusion": [
        "https://writingcenter.fas.harvard.edu/conclusions",
        "https://writingcenter.unc.edu/tips-and-tools/conclusions/",
    ],
    "topic-sentences": [
        "https://writingcenter.fas.harvard.edu/anatomy-body-paragraph",
    ],
    "transitions": [
        "https://writingcenter.fas.harvard.edu/transitions",
    ],
    "essay-structure": [
        "https://writingcenter.fas.harvard.edu/tips-organizing-your-essay",
        "https://writingcenter.fas.harvard.edu/overview-academic-essay",
    ],
    "counterargument": [
        "https://writingcenter.fas.harvard.edu/counterargument",
        "https://writingcenter.unc.edu/tips-and-tools/counterargument/",
    ],
    "summary-close-reading": [
        "https://writingcenter.fas.harvard.edu/summary",
        "https://writingcenter.fas.harvard.edu/how-do-close-reading",
    ],
    "evidence": [
        "https://writingcenter.unc.edu/tips-and-tools/evidence/",
        "https://writingcenter.unc.edu/tips-and-tools/quoting-sources/",
    ],
    "comparison": [
        "https://writingcenter.unc.edu/tips-and-tools/comparing-and-contrasting/",
    ],
    "peel-paragraphs": [
        "https://www.matrix.edu.au/essential-guide-english-techniques/peel-paragraph-structure/",
        "https://libguides.usc.edu/writingguide/paragraph",
    ],
    "analytical-writing": [
        "https://www.phrasebank.manchester.ac.uk/introducing-work/",
        "https://writingcenter.unc.edu/tips-and-tools/analysis/",
    ],
    "revising-editing": [
        "https://writingcenter.fas.harvard.edu/pages/editing-essay-part-one",
        "https://writingcenter.fas.harvard.edu/pages/revising-draft",
    ],
}

EXTRACT_JS = """window.__sl_custom_state__ = 'pending';
window.__sl_custom_result__ = '';
(function(){
  function pick() {
    var cands = Array.prototype.slice.call(document.querySelectorAll('article, main, [role="main"], .node__content, .field--name-body, div[class*="content"]'));
    var best = null, bestLen = 0;
    for (var i = 0; i < cands.length; i++) {
      var t = (cands[i].innerText || '');
      if (t.length > bestLen) { bestLen = t.length; best = cands[i]; }
    }
    if (!best || bestLen < 500) best = document.body;
    return (best.innerText || '').slice(0, 60000);
  }
  window.__sl_custom_result__ = JSON.stringify({title: document.title.slice(0, 120), url: location.href, text: pick()});
  window.__sl_custom_state__ = 'done';
})();
"""


def fetch_all() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    core = SafariCore()
    total = 0
    for part, urls in PARTS.items():
        for url in urls:
            site = url.split("/")[2].replace("www.", "").split(".")[0]
            out = OUT / f"{part}__{site}.txt"
            if out.exists() and out.stat().st_size > 2000:
                total += 1
                continue
            print(f"[{part}] {url}", flush=True)
            try:
                result = core.load(url, budget_s=75, keep_open=True)
                if result.status not in ("loaded", "partial"):
                    print(f"  load failed: {result.status}")
                    continue
                time.sleep(6)  # let the page settle after load
                p = None
                for attempt in range(3):
                    p = core.run_js_in_tab(result.tab_index, result.window_id, EXTRACT_JS, script_timeout=60)
                    if isinstance(p, dict) and p.get("result"):
                        break
                    time.sleep(5)  # retry: page may still be hydrating
                if not isinstance(p, dict) or not p.get("result"):
                    print("  extract failed after retries")
                    continue
                d = json.loads(p["result"])
                body = d.get("text", "")
                if len(body) < 800:
                    print(f"  text too small ({len(body)})")
                    continue
                out.write_text(f"SOURCE: {d.get('url')}\nTITLE: {d.get('title')}\nPART: {part}\n\n{body}", encoding="utf-8")
                total += 1
                print(f"  saved {len(body)} chars")
            except Exception as e:  # noqa: BLE001
                print(f"  error: {str(e)[:120]}")
    print(f"done: {total} source files in {OUT}")


if __name__ == "__main__":
    fetch_all()
