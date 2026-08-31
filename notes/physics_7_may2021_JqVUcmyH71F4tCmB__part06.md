# Idea Flow Notes: physics_7_may2021_JqVUcmyH71F4tCmB — Rocket

## Paragraph Flow (move by move)

The text contains no prose paragraphs — only a structured data table with a caption. I therefore map the three structural blocks (header, data body, caption) as "paragraphs."

**Paragraph 1 — Header row (column symbols + units)**

- Move 1: **variable naming** — "`~vb ~hb ∆~hc ~hmax tc tmax`" → declares what each column tracks.
- Handoff: the symbols name the *quantities* but not the *units*, so the next row must resolve this.
- Move 2: **unit specification** — "(ms−1 ) (m) (m) (m) (s) (s)" → pairs each symbol with its measurement scale.
- Handoff: with quantity + unit fixed, the reader is now licensed to read the *numerical* content of the body.

**Paragraph 2 — Data body (rows A → R)**

- Move 1: **ordered entry, high values** — "A 551.9 … P 313.2" → presents rows in a smooth descending gradient.
- Handoff: the gradient *establishes* a trend, so the break at the next row becomes a deliberate contrast.
- Move 2: **transition / break** — "Q 245.8" then "R 147.7" → the row sequence *jumps* downward, signalling an outlier regime.
- Handoff: once the data set terminates, the reader expects a *labelling* move that closes the table.

**Paragraph 3 — Caption**

- Move 1: **table-number claim** — "Table 4" → anchors the artefact in the report's running numbering.
- Handoff: a number alone is uninformative, so the next phrase must say *what* was recorded.
- Move 2: **content description** — "Simulation data retrieved for each rocket" → names the source (simulation) and the sampling unit (each rocket).
- Handoff: caption closes the block; the page number "16" that follows is a navigational artefact, not a logical move.

---

## What This Section Does (content sequence)

A IB data-presentation block of this kind moves in a fixed order:

1. **Variable declaration first** (column symbols across the top row) — sets the *categories* the reader will compare.
2. **Unit declaration second** (units row immediately under symbols) — resolves the *scale* so values are interpretable.
3. **Ordered data third** (rows A→R) — supplies the *instances* the categories will be applied to. Ordering alphabetically by label lets the reader detect a trend by scanning down a single column.
4. **Caption last** — retroactively *labels* the table (number + descriptive phrase) so it can be cross-referenced in the prose.

**Why that order:** declaring variables and units before the numbers prevents the reader from misreading magnitudes; presenting instances before the caption keeps the caption a summary rather than a prerequisite. Another student replicating this sequence on a different topic (e.g. spring constants, pendulum periods) should keep steps 1–4 in this exact order, only changing the symbol names and units.

---

## Paragraph Skeletons (replicable templates)

**Skeleton A — Variable-and-unit header**

```
SKELETON: "~[sym1] ~[sym2] ~[sym3]…    ([unit1])  ([unit2])  ([unit3])…"
```

1. *Slots:* symbol row (LaTeX-style tildes or Greek letters, one per column) and unit row (parenthesised SI units, same column count).
2. *Fill instructions:* list every measured quantity as a compact symbol on line 1; repeat the column count on line 2 using only bracketed SI units. Keep one symbol per column exactly.
3. *Original fill:* "`~vb ~hb ∆~hc ~hmax tc tmax`" / "(ms−1 ) (m) (m) (m) (s) (s)".
4. *Demo fill (different idea — pendulum experiment):* "`~T ~L ~θ ~g`" / "(s) (m) (°) (ms−2)".

**Skeleton B — Ordered data body with descending gradient and tail-break**

```
SKELETON: "Label₁  v₁  v₂  v₃  v₄  v₅  v₆
Label₂  v₁  v₂  v₃  v₄  v₅  v₆
…
Label_n  v₁  v₂  v₃  v₄  v₅  v₆  ← sharp drop"
```

1. *Slots:* a left-hand label column (A, B, C… or trial numbers), followed by six numerical columns matching the header.
2. *Fill instructions:* order rows so the first column descends smoothly; deliberately place a *much* smaller value in the last row to expose the trend break. Keep column widths aligned for readability.
3. *Original fill:* rows "A" through "P" descend gradually (e.g. "551.9" down to "313.2"); row "Q 245.8" then "R 147.7" mark the break.
4. *Demo fill (different idea — solar cell efficiency vs angle):* rows "0° 22.1 5.4 18.9 24.0 30.0 31.2" down to "80° 19.3 4.7 16.5 21.0 26.4 27.5"; tail row "85° 4.2 1.0 3.6 4.5 5.7 6.0" exposes the cut-off.

**Skeleton C — Caption line**

```
SKELETON: "Table [N]: [Source] data [verb] for each [sampling unit]."
```

1. *Slots:* ordinal number, source noun, past-participle verb, sampling-unit noun.
2. *Fill instructions:* begin with `Table` + the running number; name the *origin* of the values (simulation, experiment, literature); end with the per-row entity the reader would recognise.
3. *Original fill:* "Table 4: Simulation data retrieved for each rocket."
4. *Demo fill (different idea):* "Table 7: Laboratory data collected for each spring constant."

---

## Express-Idea Vocabulary

Because the section is a table, almost all "expression" lives in the caption. Connectives do the structural work of the header/body rather than prose transitions.

- **Sequencing (implicit, via row order):** the rows themselves act as sequence — "`A` … `B` … `C`" down to "`R`" — replacing any "firstly/next" connective.
- **Specification (header→unit pairing):** the symbol "`~vb`" is *specified* by "(ms−1 )" directly below it; the table compresses a "that is / in particular" move into vertical alignment.
- **Evidence handling (via caption verb):** "**retrieved for each rocket**" frames every numeric row as an *instance* drawn from the same procedure, doing the job "according to / as recorded by" would do in prose.
- **Cause/consequence:** none explicit — the descending gradient "`551.9` … `147.7`" is left for the reader to interpret, so the section withholds connectives and lets the data "speak."
- **Contrast/concession:** none explicit — but the row-break between "P 313.2" and "Q 245.8" performs a "however" move *visually* rather than verbally.

---

## How to Explain an Idea (replication steps)

This section uses a **structured-data-presentation pattern**, not a prose-explanation pattern. The replication steps are:

1. **Declare the categories.** Write one symbol per measured quantity across the top of the table; choose notation the surrounding report already uses (Greek letters, tildes for estimates, ∆ for differences).
2. **Anchor each category in a unit.** Immediately under the symbol row, write the SI unit in brackets so the reader never has to guess the scale.
3. **Instantiate the categories in rows.** Produce one row per trial/sample, keeping the row label short (letter or number) so the table fits a page. Order rows so a *trend* is visible by scanning down one column.
4. **Engineer a tail-break if a regime change exists.** Place the smallest values last; let the gap between the penultimate and final row act as a visual "however."
5. **Close with a numbered caption.** Use the format `Table N: [source] [verb] for each [unit].` — this is the only sentence the reader needs to recover the table's meaning in isolation.
6. **Resist prose connectives inside the table.** Let vertical alignment and row order do the logical work; save "therefore / however" for the surrounding discussion text that refers back to the table.
