# Idea Flow Notes: physics_7_may2021_JqVUcmyH71F4tCmB — Number            Factor              Facor        Increase Factor     Factor        Factor       Factor

## Paragraph Flow (move by move)

**Paragraph 1 — The Table (header row → data rows)**

- **Move 1 (definition of variables):** "N, f vb, f hb, f∆hc, fhmax, f tc, ftmax" — names the seven quantities to be tabulated. Hands to next move by **specifying** exactly what each column will hold, so the reader can read each row with the column key already in mind.
- **Move 2 (ordered evidence from largest to smallest case):** "1490.4 … 0.86 … 0.93 … 0.28 … 0.33 … 0.47 … 0.51" — records the first data row. Hands to next row by **iteration** (same column shape, next case), letting the reader scan a trend as the eye travels down.
- **Move 3 (continued iteration, descending N):** "1216.9 … 0.87 … 0.93 … 0.31" — same template, second case. Hands to subsequent rows by **sequential comparison**, since N falls monotonically and the f-values rise monotonically, so each new row visibly continues the trend.
- **Move 4 (mid-range data point):** "536.4 … 0.90 … 0.97 … 0.44 … 0.49 … 0.62 … 0.66" — a representative row mid-table. Hands to next by **continuation of monotonic pattern**.
- **Move 5 (final, smallest case):** "20.9 … 0.98 … 1.00 … 0.93 … 0.95 … 0.96 … 0.97" — closes the table at the asymptotic end where all factors → 1. Hands to the caption by **completion**: the dataset is finished, so the reader needs the sentence that tells them what to read out of it.

**Paragraph 2 — The Caption**

- **Move 1 (identification of object):** "Table 7:" — labels the artefact. Hands forward by **promising** the reader a one-sentence key to the columns above.
- **Move 2 (scope of calculation):** "Factors calculated for each rocket" — states *what was computed*. Hands forward by **specifying** the unit of the rows (one rocket = one row).
- **Move 3 (linking clause — assignment rule):** "assigned to their corresponding Drag Influence Number" — connects every row to its independent variable. Hands forward to the next page's graph by **mechanism**: the same Drag Influence Number now governs the x-axis of the figure, so the table and figure share a key.

**Paragraph 3 — Graph Axes (setup only, visible part)**

- **Move 1 (left-axis definition):** "v (ms⁻¹)" with scale 0–400 — defines the dependent variable plotted. Hands forward by **inviting** the reader to read the corresponding curve next to it.
- **Move 2 (right-axis definition):** "h (m)" with scale 0–8,000 — defines a second dependent variable sharing the horizontal axis. Hands forward to the abscissa by **dual-axis convention**: two quantities, one shared independent axis.
- **Move 3 (abscissa setup):** "0   10   20   30   40" — exposes the time-like x-range, confirming that the Drag Influence Number from Table 7 is the independent variable here.

---

## What This Section Does (content sequence)

This is a **data presentation section**, so the content sequence is dictated by what the reader needs *before* they can interpret anything.

1. **Column headers first** — without naming the quantities, the numbers are unreadable. The header row *creates the key* that every later row depends on.
2. **Ordered data rows (descending independent variable)** — rows are arranged so the monotonic trend is visible without calculation; the ordering *does analytical work* the prose never has to.
3. **Caption sentence** — sits *after* the table because it relies on the reader already having scanned the columns; it tells them what each row *is*, then ties the rows to the independent variable ("Drag Influence Number").
4. **Graph axes with shared abscissa** — placed *after* the caption because the axes can only be labelled once the caption has named the x-quantity (Drag Influence Number / time, scale 0–40).
5. **Curves (cut off here)** — would follow, because the axes without curves leave the reader waiting; the curves will be the visual claim the caption has already framed.

**Why this order:** every move *enables* the next. Headers enable reading the rows; ordered rows enable the caption's claim; the caption names the x-variable the graph axes must use.

A student replicating this for another topic should therefore follow: **define the columns → list the rows in an order that exposes the trend → write a single-sentence caption that names the unit of the row and the independent variable → set up the graph axes with that same independent variable on the abscissa.**

---

## Paragraph Skeletons (replicable templates)

### Skeleton A — The Header Row

1. **Slot 1 — name of the case-identifier column** (symbol, italicised or not, e.g. `N`).
2. **Slot 2 → Slot k — names of the calculated quantities** (each a short symbol such as `f vb`, `f hb`, …, `ftmax`).
   - **How to fill:** pick one independent identifier column on the left; then list every derived quantity as a single symbol that the caption will later gloss.
   - **Original filled version:** "N, f vb, f hb, f∆hc, fhmax, f tc, ftmax"
   - **Demonstration fill (different idea):** "Trial, pH, η₁, η₂, Δη, σ, σ_max" for a chemistry investigation where each trial produces six derived quantities.

### Skeleton B — A Data Row

1. **Slot 1 — independent value** (number, one per row, descending order).
2. **Slot 2 → Slot k — derived quantities for that case** (each number rounded to two decimals).
   - **How to fill:** order rows so the independent variable decreases monotonically; round derived quantities to the same number of decimals as in the original.
   - **Original filled version:** "1490.4   0.86   0.93   0.28   0.33   0.47   0.51"
   - **Demonstration fill (different idea):** "60.0   0.72   0.81   0.34   0.40   0.55   0.61" (first row of the chemistry trial table).

### Skeleton C — The Caption Sentence

1. **Slot 1 — "Table [number]:"** (formal label).
2. **Slot 2 — what was computed, in plural noun form** ("Factors calculated for each [unit]").
3. **Slot 3 — assignment clause linking rows to the independent variable** ("assigned to their corresponding [independent variable]").
   - **How to fill:** make the caption *one sentence*, name the object of one row, then name the column that organises the rows.
   - **Original filled version:** "Table 7: Factors calculated for each rocket assigned to their corresponding Drag Influence Number"
   - **Demonstration fill (different idea):** "Table 3: Yields calculated for each reaction assigned to their corresponding catalyst loading."

### Skeleton D — The Dual-Axis Graph Setup

1. **Slot 1 — left vertical axis: symbol and unit** (e.g. "v (ms⁻¹)").
2. **Slot 2 — left axis scale** (e.g. "0 / 100 / 200 / 300 / 400").
3. **Slot 3 — right vertical axis: symbol and unit** (e.g. "h (m)").
4. **Slot 4 — right axis scale** (e.g. "0 / 2,000 / 4,000 / 6,000 / 8,000").
5. **Slot 5 — shared abscissa tick labels** (e.g. "0  10  20  30  40").
   - **How to fill:** put the *primary* measured quantity on the left axis, the *secondary* on the right, and ensure both share the same x-range so the reader can read two curves off one time-like axis.
   - **Original filled version:** "v (ms⁻¹) … 0–400 … h (m) … 0–8,000 … 0 10 20 30 40"
   - **Demonstration fill (different idea):** "I (A) … 0–5 … V (V) … 0–12 … 0 5 10 15 20" for an electrical circuit characterisation.

---

## Express-Idea Vocabulary

This section is unusual: most "connectives" are **positional** (rows under headers) rather than verbal, but the prose that does exist carries these jobs:

- **Identification / labelling:** "Table 7:" — a one-word tag that frames everything below as belonging to one artefact.
- **Specification of object:** "Factors calculated for each rocket" — narrows the table's contents to *factors*, plural noun, and *one per unit*.
- **Linking / assignment:** "assigned to their corresponding Drag Influence Number" — the only "connective" verb in the section; it ties row to column and *also* ties the table to the x-axis of the graph on the next page.
- **Implicit sequencing (positional):** descending N (1490.4 → 20.9) replaces "firstly … then … finally"; the row order itself does the work of a temporal connectives chain.

No contrast, cause, or concession connectives appear — appropriate, because a data table argues by showing, not by arguing.

---

## How to Explain an Idea (replication steps)

The pattern this section uses to communicate an analytical claim is **define-the-columns → tabulate-in-trend-order → caption-the-table → set-up-the-graph**. It is *not* a definition→unpack→example→implication prose pattern; it is a **data-presentation pattern** in which every move enables reading the next.

To replicate it for a new idea, follow these steps:

1. **Step 1 — Pick one independent variable and one or more dependent quantities.** The independent variable will become the leftmost column and the shared x-axis; the dependent quantities become the other columns and the y-axes.
2. **Step 2 — Write the header row first.** List the independent variable symbol on the left, then every dependent quantity as a compact symbol. Without this, no row can be read.
3. **Step 3 — Generate the data and round uniformly.** Round every derived quantity to the same number of decimals (two here) so columns are visually comparable.
4. **Step 4 — Order the rows so the trend is visible.** Sort descending (or ascending) by the independent variable so the eye reads a pattern without calculation.
5. **Step 5 — Write a single-sentence caption with three parts:** "(a) Table number: (b) what was computed, plural, per unit (c) the independent variable the rows are assigned to." This is the *only* sentence needed to anchor the table.
6. **Step 6 — Set up the graph axes using the same independent variable on the x-axis.** If a second quantity belongs on the same figure, give it a right-hand y-axis; both axes must share the same x-range so the reader can read off two curves.
7. **Step 7 — Plot the curves.** (Cut off in this excerpt; the reader expects them immediately after the axes.)

The logic path is therefore: **key → record → identify → visualise**. Each move hands the reader forward by giving them exactly what they need to interpret the next artefact.
