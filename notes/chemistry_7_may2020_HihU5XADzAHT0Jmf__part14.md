# Idea Flow Notes: chemistry_7_may2020_HihU5XADzAHT0Jmf — Time                                                             Time

## Paragraph Flow (move by move)

**Paragraph 1 — Header block (variables → units → uncertainties → trial structure)**

- **Move 1 (variable declaration, left column header):** "𝑉_𝑁𝑎𝑂𝐻 / 𝑐𝑚³" — names the dependent variable and fixes its unit (cm³) directly inside the header via slash notation.
- *Hand-off:* declaring what is measured forces the reader to expect *what changes it* → next column introduces the independent variable.
- **Move 2 (variable declaration, second column header):** "𝑡 / 𝑚𝑖𝑛𝑢𝑡𝑒𝑠" — names the independent variable and its unit, completing the column meaning before any number appears.
- *Hand-off:* once both variables are named, the next logical question is "how precise are these readings?" → move to uncertainty row.
- **Move 3 (uncertainty for DV):** "∆𝑉_𝑁𝑎𝑂𝐻 = ±0. 10𝑐𝑚³" — states the absolute uncertainty of the burette reading, justifying later significant figures.
- *Hand-off:* precision of DV is set; the IV's precision still needs declaring → next cell.
- **Move 4 (uncertainty for IV):** "∆𝑡 = ±0. 25" — states the absolute uncertainty of the time reading, completing the precision framework.
- *Hand-off:* with variable and precision established, the table must now show *how the readings were obtained* (replication) → trial columns.
- **Move 5 (replication + aggregation header):** "Trial 1 Trial 2 Trial 3 Mean" — promises three repeats and a single representative value, signalling reproducibility is built into the design.

**Paragraph 2 — Table 5 body (T = 323 K data)**

- **Move 1 (first data point):** "5.00 … 2.93 ± 0.03" — opens at the earliest time, presenting three trials and a mean; sets the *starting* volume the reader will track upward.
- *Hand-off:* the first reading establishes a baseline; every next row is implicitly compared to it.
- **Move 2–6 (subsequent data points):** "10.0 … 3.20 ± 0.08", "15.0 … 3.83 ± 0.05", "20.0 … 4.33 ± 0.10", "25.0 … 4.83 ± 0.05", "30.0 … 5.20 ± 0.05" — each row *specifies* the next time-step (Δt = 5 min) and shows the corresponding mean volume, building a monotonically rising dataset.
- *Hand-off:* the rising trend in Table 5 creates an expectation that the parallel Table 6 will be *compared* against it.
- **Move 7 (caption):** "Table 5: Relationship between time and volume of NaOH used in titration for 𝑇 = 323K" — names the experiment, fixes the controlled variable (temperature), and frames the table as "relationship" data, preparing the reader for the comparison block.

**Paragraph 3 — Table 6 body (T = 333 K data) + comparative framing**

- **Move 1 (first data point, parallel to Table 5):** "5.00 … 3.12 ± 0.08" — repeats the same time grid; the higher volume (3.12 vs 2.93) immediately signals the temperature effect.
- *Hand-off:* structural parallelism invites row-by-row comparison; the eye tracks each row downward.
- **Move 2–6 (parallel data rows):** "10.0 … 3.50 ± 0.10", "15.0 … 4.03 ± 0.08", "20.0 … 4.70 ± 0.05", "25.0 … 5.27 ± 0.10", "30.0 … 5.58 ± 0.10" — every mean is higher than its Table 5 counterpart at the same time, supplying the *evidence* the caption promises.
- *Hand-off:* data is complete; the parallel caption closes the section by labelling what was just shown.
- **Move 7 (caption):** "Table 6: Relationship between time and volume of NaOH used in titration for 𝑇 = 333K" — mirrors the Table 5 caption exactly except for the temperature value, locking the comparison into the reader's mind through identical phrasing.

## What This Section Does (content sequence)

This is a **raw-data presentation block**. The ordered moves are:

1. **Declare variables + units** (slash notation in column headers) — sets up what every later number means.
2. **Declare absolute uncertainties** (∆ symbol row) — establishes how many figures are justified downstream.
3. **Declare replication structure** (Trial 1 / 2 / 3 / Mean columns) — promises statistical reliability.
4. **List trials + mean for condition A** (Table 5) — provides the first dataset.
5. **Caption condition A** ("for T = 323K") — locks the controlled variable so the reader cannot misinterpret the data.
6. **List trials + mean for condition B** (Table 6) — provides the *comparable* dataset using identical time intervals.
7. **Caption condition B** ("for T = 333K") — mirrors caption A so the *only* visual difference between the tables is the data, forcing the temperature effect to be the inferred conclusion.

**Why this order:** variables must be defined before numbers can be read; precision must be declared before means are trusted; replication must be advertised before raw trials appear; condition A must be anchored before condition B can be meaningfully compared; the captions are deferred until *after* the data so the reader sees the numbers first and the label second (this prevents the label from biasing how the data is read).

## Paragraph Skeletons

**SKELETON A — Header + uncertainty + replication strip**

```
[Var₁]/[unit₁]   [Var₂]/[unit₂]
∆[Var₁] = ±[unc₁]   ∆[Var₂] = ±[unc₂]
Trial 1   Trial 2   Trial 3   Mean
```

- **Slot 1** ("[Var₁]/[unit₁]"): dependent variable name with its SI or apparatus unit, written as a fraction-style header.
- **Slot 2** ("[Var₂]/[unit₂]"): independent variable name with its unit, in the same notation.
- **Slot 3** ("∆[Var₁] = ±[unc₁]"): absolute uncertainty for the DV, matching its unit.
- **Slot 4** ("∆[Var₂] = ±[unc₂]"): absolute uncertainty for the IV, matching its unit.
- **Slot 5** ("Trial 1 Trial 2 Trial 3 Mean"): column labels signalling replication and aggregation.

**How to fill with a different idea:** slot 1 = pick your measured quantity (mass, absorbance, pH…); slot 2 = pick the quantity you varied (concentration, distance, wavelength…); slots 3–4 = read precisions from your instrument and write them in the matching unit; slot 5 = keep the four labels verbatim — they are the convention.

- **Original filled version:** "𝑉_𝑁𝑎𝑂𝐻 / 𝑐𝑚³", "𝑡 / 𝑚𝑖𝑛𝑢𝑡𝑒𝑠", "∆𝑉_𝑁𝑎𝑂𝐻 = ±0. 10𝑐𝑚³", "∆𝑡 = ±0. 25", "Trial 1 Trial 2 Trial 3 Mean".
- **Demonstration fill with a different idea (e.g. cooling experiment):**
  `𝑇 / °C    𝑡 / 𝑠`
  `∆𝑇 = ±0. 5°C    ∆𝑡 = ±0. 5𝑠`
  `Trial 1   Trial 2   Trial 3   Mean`

---

**SKELETON B — Data row**

```
[IV value]   [Trial 1]   [Trial 2]   [Trial 3]   [Mean ± SD/unc]
```

- **Slot 1:** fixed independent-variable value for the row, written to the precision of ∆IV.
- **Slots 2–4:** three raw readings, written to the precision of ∆DV.
- **Slot 5:** mean of slots 2–4, followed by the propagated or sample standard deviation, in DV units.

**How to fill:** slot 1 = the next value of the independent variable on your chosen grid (use evenly spaced values that span the range); slots 2–4 = the three measurements you recorded at that grid value; slot 5 = arithmetic mean with uncertainty.

- **Original filled version:** "10.0 3.30 3.15 3.15 3.20 ± 0.08".
- **Demonstration fill:** `60  18.2  18.5  18.3  18.33 ± 0.15`.

---

**SKELETON C — Caption**

```
Table [N]: Relationship between [IV] and [DV] [used in / of] [apparatus / process] for [controlled condition]
```

- **Slot 1:** table number.
- **Slot 2:** "Relationship between" — fixed phrasing.
- **Slot 3:** IV name.
- **Slot 4:** DV name.
- **Slot 5:** experimental context naming apparatus or process.
- **Slot 6:** the controlled variable (the one that differs across tables).

**How to fill:** keep slots 2 and the connecting wording verbatim; vary slots 1, 3, 4, 5, 6. Slot 6 should be the single thing you changed between parallel tables.

- **Original filled version:** "Table 5: Relationship between time and volume of NaOH used in titration for 𝑇 = 323K".
- **Demonstration fill:** `Table 2: Relationship between wavelength and absorbance of CuSO₄ solution for 𝑐 = 0.10 mol dm⁻³`.

## Express-Idea Vocabulary

Because this section is tabular, *almost no prose connectives appear*. The "vocabulary" is **notation-driven** rather than connective-driven:

- **Variable-with-unit construction (slash notation):** "𝑉_𝑁𝑎𝑂𝐻 / 𝑐𝑚³", "𝑡 / 𝑚𝑖𝑛𝑢𝑡𝑒𝑠" — collapses "variable X measured in unit Y" into one symbol.
- **Uncertainty construction (delta-equals-plus-minus):** "∆𝑉_𝑁𝑎𝑂𝐻 = ±0. 10𝑐𝑚³", "∆𝑡 = ±0. 25" — declares precision in the same row as the variable, signalling that the uncertainty belongs *to that column only*.
- **Replication labels:** "Trial 1 Trial 2 Trial 3" — three repetitions to justify the aggregated value.
- **Aggregation label:** "Mean" — promises a central tendency and an associated spread in the next column.
- **Caption "Relationship between":** "Relationship between time and volume of NaOH" — frames raw numbers as a *trend to be interpreted*, not isolated readings.
- **Controlled-variable tag:** "for 𝑇 = 323K", "for 𝑇 = 333K" — the only piece that changes between the two parallel captions, forcing the reader's attention onto the temperature.

There are **no sequencing, cause, contrast, or specification connectives** in this section — those belong to the prose discussion that surrounds the tables.

## How to Explain an Idea (replication steps)

This section uses a **define-variables → declare-precision → replicate → aggregate → tag-condition** pattern. To replicate it for any new dataset:

1. **Identify the two variables.** Decide which is the independent variable (the one you set) and which is the dependent variable (the one you measure). Write them as `[IV]/[unit]` and `[DV]/[unit]` in the top header row.
2. **Read the instrument precision for each variable.** Write `∆[IV] = ±[value][unit]` and `∆[DV] = ±[value][unit]` in the row directly below the variable headers, matching each uncertainty to its variable's column.
3. **Add a replication + aggregation row.** Write the labels `Trial 1`, `Trial 2`, `Trial 3`, `Mean` across the data columns. This row declares *how many times* each reading was repeated and that a summary statistic will follow.
4. **Build the body row by row.** For each fixed IV value, record the three trials in the three Trial columns and compute the mean with its standard deviation (or propagated uncertainty) in the Mean column. Use evenly spaced IV values so the trend is visible.
5. **Caption the table.** Use the fixed phrase `Table N: Relationship between [IV] and [DV] [used in/for] [process] for [controlled condition = value]`. The controlled-condition slot is the variable that is *constant within this table but differs between parallel tables*.
6. **If you have a comparison table, repeat steps 1–5 with the same IV grid and the same column structure.** Keep the caption phrasing identical except for the controlled-condition value — this visual and verbal parallelism is what makes the comparison readable.
