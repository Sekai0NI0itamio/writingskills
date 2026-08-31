# Idea Flow Notes: chemistry_6_may2021_wX9nywnRyBVpyNWB — Temperature Average                    Average Ecell       Average Ecell          Percentage

## Paragraph Flow (move by move)

This section is not written in prose paragraphs — it is a **data-presentation block** composed of two numbered tables followed by a transitional sentence stub. I'll treat each table + its surrounding scaffolding as one "paragraph-unit" and map sentence by sentence (or row by row where no sentences exist).

**Unit 1 — Table 10 (header + 5 data rows):**

1. **Sentence/Row 1 — Header context:** "Temperature Average Average Ecell Average Ecell Percentage" — *context/definition move*: declares what columns the table tracks. Hands reader to the next row by establishing **what variable will appear under which heading** (a definitional handoff — you read the column meaning, then the value drops into it).
2. **Row 1 (298.15 K):** "298.15 0.429 — ±1.00 × 10 −3 2.31 × 10−1" — *evidence move*: first data instance. Hands forward by **establishing the lowest-temperature baseline** the next four rows will be read against.
3. **Row 2 (303.15 K):** "303.15 0.407 ±1.50 × 10 −3 ±2.50 × 10 −3 6.14 × 10−1" — *evidence move + implicit contrast*: value drops relative to row 1. Hands forward by **showing the largest percentage uncertainty so far**, inviting scrutiny of the next row.
4. **Row 3 (308.15 K):** "308.15 0.398 ±5.00 × 10 −4 ±1.50 × 10 −3 3.77 × 10−1" — *evidence move*: continued decrease in Ecell, smallest Ecell-side uncertainty. Hands forward by **normalising the uncertainty pattern** the reader should now expect.
5. **Row 4 (313.15 K):** "313.15 0.393 - ±1.00 × 10 −3 2.54 × 10−1" — *evidence move*: a dash replaces the Ecell-uncertainty cell (a missing-value signal). Hands forward as a **consequence/specification move**: the reader must infer that some trials lacked a recorded Ecell spread.
6. **Row 5 (318.15 K):** "318.15 0.389 ±5.00 × 10 −4 ±1.50 × 10 −3 3.85 × 10−1" — *evidence/verdict move*: lowest Ecell, lowest total uncertainty %. Hands forward by **closing the dataset**, which cues the caption.
7. **Caption:** "Table 10 – Processed data for Ecell" — *label move*: retroactively binds the whole block. Hands forward by **naming what was just seen**, so the reader enters Table 11 already primed to compare.

**Unit 2 — Table 11 (header + 5 data rows):**

8. **Header:** "Temperature Average 𝐾𝑐 Absolute uncertainty (Maximum – Recorded Value) Percentage uncertainty (%)" — *context/definition move*: same skeleton as Unit 1, but with a **substituted dependent variable (Kc instead of Ecell)** — a deliberate parallel that hands the reader into a **comparison move**: "same structure, different quantity."
9. **Row 1 (298.15 K):** "298.15 4.51 × 10 0 6.30 × 10 −2 1.41 × 10 0" — *evidence move*: anchors Kc near 4.5 at low T. Hands forward by giving the **baseline against which the four higher-T rows will be judged.**
10. **Row 2 (303.15 K):** "303.15 4.43 × 10 0 6.68 × 10 −2 2.01 × 10 0" — *evidence move + trend continuation*: Kc falls, % uncertainty rises to the table's maximum. Hands forward by **flagging the worst-case uncertainty point** for the reader to remember.
11. **Row 3 (308.15 K):** "308.15 4.40 × 10 0 6.43 × 10 −2 1.46 × 10 0" — *evidence move*: steady decline, uncertainty re-tightens. Hands forward by **reinforcing monotonicity** so the next two rows feel like a verification.
12. **Row 4 (313.15 K):** "313.15 4.37 × 10 0 6.31 × 10 −2 1.44 × 10 0" — *evidence move*. Hands forward by **continuation**.
13. **Row 5 (318.15 K):** "318.15 4.35 × 10 0 6.44 × 10 −2 1.48 × 10 0" — *evidence/verdict move*: lowest Kc, uncertainty ticks up marginally. Hands forward to the caption.
14. **Caption:** "Table 11 - Processed data for Kc" — *label move*: mirrors Caption 7 exactly in form, handing reader forward by **inviting a side-by-side read** of the two tables' trends.

**Unit 3 — Section opener stub:**

15. **"10. Data Presentation:"** — *transition/heading move*: signals the start of a new numbered section. Hands forward to "Graph 1 – line of best fit of Average 𝐾𝑐 results in table 10" — the next artefact — by **promising that the tables will now be visualised** (cause: data has been tabulated → therefore a graph follows).

## What This Section Does (content sequence)

This is a **processed-data presentation section**. The sequence it enforces, and why:

1. **Quantity #1 raw table** — establishes the first measured/produced quantity (here Ecell) with columns for independent variable, average, instrument uncertainty, propagated total uncertainty, percentage uncertainty. *Sets up:* a known, fully-quantified dataset.
2. **Caption binding Quantity #1** — locks the table to its variable. *Sets up:* parallel structure.
3. **Quantity #2 raw table (derived)** — reuses the identical column skeleton for a derived quantity (here Kc). *Sets up:* a comparison between primary and secondary trends under identical formatting.
4. **Caption binding Quantity #2** — closes the parallel. *Sets up:* a "Graph of Quantity #2 follows" cue.
5. **Numbered section heading ("10. Data Presentation:")** — announces the deliverable category. *Sets up:* the visual artefact (graph) that the next section will produce from these tables.

The order is **primary measurement → derived quantity → visual representation** because the reader must see both numbers (and their uncertainties) before a line of best fit can be defended as trustworthy.

## Paragraph Skeletons (replicable templates)

**Skeleton A — Parallel processed-data table block (the unit the whole section repeats)**

```
SKELETON: "[HEADING: Independent-variable column | Quantity-1 column | Quantity-1 uncertainty | Propagated total uncertainty | Percentage uncertainty]. [Row N at lowest independent-variable value, giving all five cells]. [Row N+1 ...]. ... [Caption: Table X – Processed data for <Quantity>]"
```

1. *Slots:* (i) a 5-column header where slot 1 names the controlled variable, slot 2 the average of the response, slot 3 its instrument spread, slot 4 the propagated total, slot 5 the percentage; (ii) N data rows in ascending order of the independent variable; (iii) a caption "Table N – Processed data for [Quantity]".
2. *How to fill with a DIFFERENT idea:* Slot 1 — pick the experimental variable you controlled (e.g. "Concentration", "Time", "pH") in bold with units. Slot 2 — put your measured response quantity and unit. Slot 3 — record raw instrument uncertainty (or a dash if no spread was captured). Slot 4 — write the propagated absolute uncertainty. Slot 5 — write (slot 4 / slot 2) × 100. Rows — five trials at evenly-spaced independent-variable settings, ascending. Caption — "Table X – Processed data for [Quantity]."
3. *Original filled version:* "Temperature Average Average Ecell Average Ecell Percentage ... Table 10 – Processed data for Ecell."
4. *Demonstration fill with a different idea:* "pH (±0.01) Average reaction rate (mol dm⁻³ s⁻¹) Rate uncertainty (±0.002) Propagated total uncertainty Percentage uncertainty (%) ... Table 10 – Processed data for reaction rate." Rows at pH 2, 4, 6, 8, 10.

**Skeleton B — Derived-quantity echo table (mirrors Skeleton A with one column swap)**

```
SKELETON: "[Same 5-column header as Skeleton A, but with the response quantity replaced by a value derived from the previous table]. [Identical independent-variable column]. [Rows]. [Caption: Table N+1 – Processed data for <Derived Quantity>]"
```

1. *Slots:* (i) the same column structure as A; (ii) the **same** independent-variable values (so columns line up across both tables); (iii) a new response quantity computed from Quantity 1.
2. *How to fill:* keep the independent-variable column numerically identical to Table 10's; replace the response column with a derived value (here Kc; elsewhere: equilibrium constant, rate constant, activation energy, etc.); re-propagate uncertainty for the **derived** operation; caption as "Table N – Processed data for [Derived quantity]."
3. *Original filled version:* "Temperature Average 𝐾𝑐 Absolute uncertainty (Maximum – Recorded Value) Percentage uncertainty (%) ... Table 11 - Processed data for Kc."
4. *Demonstration fill:* "pH (±0.01) Average Ka (dimensionless) Propagated Ka uncertainty Percentage uncertainty (%) ... Table 11 – Processed data for Ka."

**Skeleton C — Section-opening transition stub**

```
SKELETON: "[Number]. Data Presentation: [Lead-in to next visual artefact: 'Graph X – line of best fit of <Derived Quantity> results in table <N>, with ...']"
```

1. *Slots:* (i) section number; (ii) section title "Data Presentation:"; (iii) a labelled pointer to the next figure that **names the quantity** and **references the prior table**.
2. *How to fill:* advance the section number from whatever precedes; keep the title "Data Presentation:" if you are visualising; name the figure ("Graph 1"); name the dependent variable; cite the table the graph is built from.
3. *Original filled version:* "10. Data Presentation: Graph 1 – line of best fit of Average 𝐾𝑐 results in table 10, with".
4. *Demonstration fill:* "11. Data Presentation: Graph 2 – line of best fit of Average rate results in table 10, with error bars representing the propagated uncertainty."

## Express-Idea Vocabulary

**Sequencing / structural connectives**
- "Table 10 – Processed data" — caption-level sequencing (orders artefacts by number, not by a connective word).
- "Table 11 - Processed data" — caption-level sequencing, parallel to the above.
- "10. Data Presentation:" — numbered section marker, functions as a forward pointer.

**Specification / labelling**
- "(±0.5K)" — units + instrument precision baked into the column header; signals that the **next number is bounded by this uncertainty**.
- "(±0.001V)" — same move for voltage.
- "Maximum – Recorded Value" — specification of how the absolute uncertainty was *computed*, not just stated.

**Evidence handling (silent — through column order)**
- A dash "—" — used in the uncertainty cell to mean "no spread recorded," i.e. **evidence-absence marker**, not a missing entry.
- Bold for the dependent variable ("Average 𝑲𝒄") and italics for the constant ("Temperature") — typographic specification that the **bolded quantity is the response**, the unbolded is the control.

**Explanation verbs (sparse — this section is data, not prose)**
- "Processed data for" — caption verb that frames the entire table as a **result of a calculation chain**, not raw measurement.

## How to Explain an Idea (replication steps)

This section does **not** explain a concept — it **presents processed evidence in parallel-table form**. The replication pattern is therefore a **"parallel-tabled evidence"** move, not a definition→example chain. To reproduce it:

1. **Decide the controlled variable.** State it with its unit and instrument precision in parentheses; this becomes Column 1.
2. **Decide the first response quantity** (a directly measured value). Name it, unit it, and create three columns: average, instrument uncertainty, propagated total uncertainty. Add a fifth column for percentage uncertainty = (propagated / average) × 100.
3. **Fill the rows in ascending order of the controlled variable** (typically 5 rows). For each row, decide whether instrument uncertainty was captured — if not, place a dash, do **not** leave the cell blank. Compute propagated and percentage values.
4. **Caption with a number and the phrase "Processed data for [Quantity]."** The word "Processed" is the signal that a calculation chain has been applied.
5. **Repeat the skeleton verbatim** for a second, derived quantity, keeping Column 1 numerically identical so the two tables can be read side-by-side.
6. **Open the next section with a numbered "Data Presentation:" heading that names the forthcoming figure and explicitly cites the table it will plot.** This converts the tables into inputs for the visual analysis that follows.

The logic chain the section enforces on the reader is: *controlled variable is fixed → response was measured → uncertainty was propagated → a derived quantity was computed from it → next step is visualisation.* Every sentence/row in the section either populates one slot of that chain or labels it.
