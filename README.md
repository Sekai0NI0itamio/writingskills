# writingskills

AI-mined writing skills from **80 grade-6/7 IB exemplar essays** (PDFs in `corpus/`).

## Two generated skills

| File | What it governs | Pipeline |
|------|-----------------|----------|
| `IdeaThinkingFlow.md` | How IDEAS move: paragraph logic flow, paragraph skeletons with slot fill instructions, express-idea vocabulary, explanation replication steps | `scripts/analyze_idea_flow.py` + `scripts/distill_idea_flow.py` |

## Run it (GitHub Actions)

1. Add repo secret `OPENROUTER_API_KEY` (Settings → Secrets and variables → Actions). Uses OpenRouter free models (`minimax/minimax-m3:free` by default; override with env `IDEA_FLOW_MODEL`).
2. Actions → **IdeaThinkingFlow** → Run workflow:
   - `mode=full` — extract PDFs → split sections → per-section agents (5 concurrent per file) → distill `IdeaThinkingFlow.md`
   - `mode=analyze` — notes only (resume-safe: committed `notes/` are skipped on re-run)
   - `mode=distill` — rebuild the .md from cached notes
3. Results are committed back to the repo by the workflow (`IdeaThinkingFlow.md`, `notes/`, `texts/`, `parts/`).

## Run it locally

```bash
export OPENROUTER_API_KEY=sk-or-...
python3 scripts/extract_texts.py       # needs poppler (pdftotext)
python3 scripts/split_sections.py
python3 scripts/analyze_idea_flow.py --in-flight 15 --per-file 5
python3 scripts/distill_idea_flow.py
```

Flags: `--limit-files N`, `--only SUBSTR`, `--test-one` (distill dry run), `--reset`.
