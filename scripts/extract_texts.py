#!/usr/bin/env python3
"""Extract text from all corpus PDFs (grade 6/7 exemplars) into texts/.

Uses pdftotext (poppler-utils). On GitHub Actions: apt-get install poppler-utils.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
TEXTS = ROOT / "texts"


def main() -> None:
    TEXTS.mkdir(exist_ok=True)
    pdfs = sorted(CORPUS.glob("*.pdf"))
    print(f"extracting {len(pdfs)} PDFs")
    ok = 0
    for pdf in pdfs:
        out = TEXTS / (pdf.stem + ".txt")
        if out.exists() and out.stat().st_size > 1000:
            ok += 1
            continue
        try:
            r = subprocess.run(
                ["pdftotext", "-layout", str(pdf), str(out)],
                capture_output=True, timeout=60,
            )
            size = out.stat().st_size if out.exists() else 0
            if r.returncode == 0 and size > 800:
                ok += 1
            else:
                print(f"  FAIL {pdf.name}: rc={r.returncode} size={size}")
                out.unlink(missing_ok=True)
        except Exception as e:  # noqa: BLE001
            print(f"  FAIL {pdf.name}: {e}")
    print(f"done: {ok}/{len(pdfs)} texts extracted -> {TEXTS}")
    if ok < len(pdfs) * 0.9:
        sys.exit(1)


if __name__ == "__main__":
    main()
