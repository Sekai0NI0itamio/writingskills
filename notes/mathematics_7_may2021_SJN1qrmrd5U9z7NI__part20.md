# Idea Flow Notes: mathematics_7_may2021_SJN1qrmrd5U9z7NI — Ratings                               Ratings                                   Ratings                               Ratings

## Paragraph Flow (move by move)

**Paragraph 1 (Header block — defines the four parallel measurement groups):**

- **Move 1 (column scaffold):** Repeats the labels "(x) Ratings Error" four times across the page. This *defines* the four-column layout the reader will scan. Hand-off: the repetition creates four identical scaffolds that *demand* sub-labels to distinguish them.
- **Move 2 (variable sub-label, row 1):** Prints "(υA)" once under each "Ratings" cell. This *specifies* which quantity lives in the Ratings slot of every group. Hand-off: having named υA, the next line must name the remaining sub-quantities.
- **Move 3 (variable sub-labels, row 2):** Prints "(υC)" and "(δ)" alternating under each group. This *completes the schema* — three measured quantities (υA, υC, δ) plus a paired "Error" column, x4. Hand-off: schema done → the body of data must now populate it.

**Paragraph 2 (Data block — 22 rows of measurements):**

- **Move 1 (first data row):** "629 4.21 4.61 9.52% 372 4.13 4.00 3.23% …" This *instantiates* the scaffold — gives the reader the first concrete set of numbers in the format just defined. Hand-off: the row's pattern (one value, three measurements, one error — ×4) sets a template the eye will repeat.
- **Move 2 (successive rows):** Each new row *extends* the sample with new x values, monotonically changing υA and Error. Hand-off: because the columns are already defined, every additional row is read as a *new instance* of the same observation pattern.
- **Move 3 (final partial row):** "418 4.15 4.40 6.02% 222 4.06 3.97 2.28%" stops at the second group. This *concludes* the dataset — the abrupt truncation signals the table is closed rather than rounded off.

## What This Section Does (content sequence)

This is a **raw-data table** for a 6/7 IB exploration, not prose. The ordered moves are:

1. **Header scaffold** — repeat the column titles so the reader knows the structure before any number appears. *Why first:* the reader cannot parse a data cell without knowing what the cell represents.
2. **Variable specification** — name the quantities (υA, υC, δ) and pair them with their parent column ("Ratings", "Error"). *Why second:* symbols in a header are useless until they are tied to roles.
3. **Group replication** — copy the (x, υA, υC, δ, Error) block four times across the page. *Why third:* enables side-by-side comparison between conditions/groups without forcing the reader to scroll.
4. **Row-by-row data** — present one observation per row, scanning the four groups left-to-right within each row. *Why this order:* reading down a single observation mirrors the "one trial, four conditions" logic of the experiment.
5. **Truncated ending** — the last row may be incomplete; this implicitly *signals closure* to the eye rather than padding with blank cells.

Generalised sequence another student could copy: **define the column structure → label the variables in each column → replicate the measurement unit horizontally → stack observations vertically → stop.**

## Paragraph Skeletons (replicable templates)

**SKELETON 1 (header paragraph — variable declaration):**
> `[Top-row label] [repeated N times] / [Sub-label A under first cell] [repeated N times] / [Sub-label B] [Sub-label C] [Sub-label B] [Sub-label C] …`

1. **Slot 1 (top-row label):** a parent variable name in parentheses, repeated N times across the page.
2. **Slot 2 (first sub-label row):** a Greek or technical symbol written under *each* "Ratings" cell to specify what the rating measures.
3. **Slot 3 (second sub-label row):** two more symbols alternating under the remaining two sub-columns of every group.

*How to fill with a different idea:* keep the repetition-N structure but swap the symbols (e.g. instead of velocity symbols, use temperature symbols (Tₛ, Tₐ, Tᵣ) for a heat-loss table; or use (R₁, R₂, R₃, R₄) for four resistor trials).

- **Original fill:** "(x) Ratings Error (x) Ratings Error … / (υA) (υA) (υA) (υA) / (υC) (δ) (υC) (δ) (υC) (δ) (υC) (δ)"
- **Demo fill (different idea — a pendulum experiment):** "(θ) Period Error (θ) Period Error (θ) Period Error (θ) Period Error / (T₁) (T₁) (T₁) (T₁) / (T₅) (ΔT) (T₅) (ΔT) (T₅) (ΔT) (T₅) (ΔT)"

**SKELETON 2 (data-row paragraph — single observation repeated):**
> `[int₁]  [float₁]  [float₂]  [percent]   [int₂]  [float₃]  [float₄]  [percent]   …  [intN]  [float₂N-1]  [float₂N]  [percent]`

1. **Slot 1 (independent variable):** integer or float — one per group, e.g. sample size, angle, distance.
2. **Slot 2 (two measurement columns):** two decimals representing two quantities (e.g. observed vs. theoretical, or two different methods).
3. **Slot 3 (error column):** a percentage in the form "X.XX%".
4. **Slot 4 (repeat of slots 1–3):** the same four-cell pattern repeated N times across the page to enable horizontal comparison.

*How to fill with a different idea:* swap the four cells for any "one independent variable → two derived values → one percentage-error" pattern, e.g. (mass, spring length, predicted length, %error) for Hooke's law.

- **Original fill:** "629 4.21 4.61 9.52% 372 4.13 4.00 3.23% 383 4.14 4.32 4.40% 236 4.07 3.95 2.97%"
- **Demo fill (different idea — bounce-height experiment):** "0.50 0.42 0.45 7.14% 0.60 0.51 0.54 6.06% 0.70 0.58 0.63 8.70% 0.80 0.65 0.72 10.34%"

## Express-Idea Vocabulary

Because the section is a table, traditional prose connectives are absent. The "vocabulary" is **positional and symbolic**:

- **Sequencing (vertical):** the column order itself — each new row *extends* the dataset. "The next row is `722 4.23 4.44 4.98%`…" — order signals "another trial."
- **Grouping (horizontal):** the fourfold repetition of the header "(x) Ratings Error" *visually parallelises* four experimental conditions; no word is needed.
- **Specification (sub-labels):** "(υA)" under each "Ratings" cell, "(υC)" and "(δ)" in the row below — *specifies* what each column measures without prose.
- **Definition (parenthesised symbols):** every variable is *defined* by enclosure — "(x)", "(υA)", "(υC)", "(δ)" — the parentheses themselves do the defining work that "is defined as" would do in prose.
- **Error signalling:** the trailing "9.52%", "3.23%", "4.40%" — the `%` glyph *flags* the column as a relative-error column; its position at the right of each group *specifies* which group it belongs to.

(There are no connectives such as "however" or "therefore" because the section is data, not argument.)

## How to Explain an Idea (replication steps)

The section uses a **schema-first, then-instantiation** explanation pattern: declare the variables and their layout, *then* pour the numbers in. To replicate this pattern for a NEW idea:

1. **Decide the experimental unit** — what is one "observation" (e.g. one trial, one sample, one time point)?
2. **Choose N (1–4) parallel conditions** you want compared side-by-side in the same table (e.g. four methods, four temperatures, four angles).
3. **For each condition, list the quantities measured** — typically one independent variable, two or three dependent variables, and one error/uncertainty metric. Give each a single-symbol label in parentheses.
4. **Write the top header row** by repeating `[symbol] [Name] [Error]` exactly N times across the page.
5. **Write the sub-label row(s)** placing the dependent-variable symbols directly under their parent "Name" or "Error" cells, again ×N.
6. **Stack the data rows** — one row per observation, scanning the four groups left-to-right so each row reads as "one trial, four conditions."
7. **End the table** at the last full observation; allow the final row to be partial if needed (this signals closure visually, not as an error).
8. **Verification step:** re-read the table top-to-bottom and left-to-right — every cell must be either a parent label, a sub-label, or a number. If a cell is a unit or a stray word, it does not belong in a data table; move it to the caption below the table.

The pattern is: **define the box → label the box → fill the box → close the box**.
