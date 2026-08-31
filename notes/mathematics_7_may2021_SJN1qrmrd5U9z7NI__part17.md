# Idea Flow Notes: mathematics_7_may2021_SJN1qrmrd5U9z7NI — Ratings   Ratings        Error                  Ratings                Error                 Ratings               Error                    Ratings                 Error

## Paragraph Flow (move by move)

**Paragraph 1 — Header band**
- Move 1 (grouping declaration): "(x) Ratings (x) Ratings (x) Ratings" — declares FOUR parallel groups.
- Move 2 (variable specification): "(υA) (υC) (δ)" / "(υA) (δ)" — specifies each group holds a count, two rating measures, and an error.
- Move 3 (nested variable): "(υC)" repeated on a third band — adds a measure only to the rating side.

**Paragraph 2 — Data row band (nine rows)**
- Move 1 (largest n opens): "720  4.34  4.35  0.24%" — highest sample count first.
- Move 2 (descending n): "672, 659, 602, 592…" — n falls as you read down.
- Move 3 (within-row pair): "4.34  4.35" — two ratings sit adjacent to force comparison.
- Move 4 (error verdict): "0.24%, 2.86%, 1.17%, 3.78%" — each row ends on a percentage.
- Move 5 (group restart): "304", "372", "407" — fresh n opens each new group, re-starting the cycle.

## What This Section Does (content sequence)
1. Define parallel column architecture (4 groups).
2. Anchor with the largest n at top.
3. Order rows by descending n.
4. Place two measures side-by-side per row.
5. Close each row with an error %.
6. Restart the (n → rating₁ → rating₂ → error) cycle at every group.

## Paragraph Skeletons (replicable templates)
SKELETON A — Header band: `[Group label × N] / [Variable symbols under each column] / [Nested variable]`
SKELETON B — Row cell group: `[n] [Measure A, 2 dp] [Measure B, 2 dp] [Error %, 2 dp]`
SKELETON C — Row ordering: `n₁ > n₂ > n₃ … with each row following skeleton B.`

Each slot is filled with: an integer count, two float measures of identical precision, and a percentage. Demo fill for B with a different idea: `540  78.42  76.95  1.91%`.

## Express-Idea Vocabulary
Sequencing: implicit descending n "720, 672, 659…"
Specification: "(υA) (υC) (δ)" clusters under "Ratings"/"Error"
Evidence: each numeric cell IS the evidence
Comparison trigger: identical row schema forces υA vs υC pairing
Verdict token: the "%" suffix on the last cell

## How to Explain an Idea (replication steps)
1. Choose number of comparison groups.
2. Write a header band repeating the group label N times.
3. Place variable symbols under each column; nest extras on a third band.
4. Pick a primary ordering axis (here, n).
5. Open row 1 with the largest value of that axis.
6. Put the two compared measures adjacent in every row.
7. End every row with a derived single-number verdict.
8. Restart the (axis → measure₁ → measure₂ → verdict) tuple at each group boundary.
9. Use NO prose connectives; logic comes from repeated column shape.
