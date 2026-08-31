# Idea Flow Notes: geography_7_may2020_xkOerZfYOOVWp7vR — Site   Downstream   Width   Depth     Velocity

## Paragraph Flow (move by move)

**Paragraph 1 — Tabular Data Block (Site 1–3 raw measurements)**

- Move 1: **Column-header definition.** "(mm)         (mm)         (mm)       Shape Index / (km)       (m)     (m)       (m/s)" — declares the units each variable carries. *Hand-off:* the unit line immediately below a labelled column forces the reader to read the data rows as instantiations of those defined quantities, so the next move is the raw instances.
- Move 2: **Raw instances, Site 1.** "1       1.89       2.51     0.05      0.13" — delivers Site-1 measurements (rows 1–8). *Hand-off:* because every Site-1 row begins with the same identifier "1", the reader expects a switch when that digit changes; this primes the next move.
- Move 3: **Raw instances, Site 2.** "2       2.00       4.42     0.03      0.16" — delivers Site-2 measurements (rows 9–16). *Hand-off:* the change in leading digit (1 → 2) signals a grouping boundary; the reader anticipates another boundary, so the next move is a second switch.
- Move 4: **Raw instances, Site 3.** "3       2.37       6.65     0.10      0.48" — delivers Site-3 measurements (rows 17–23). *Hand-off:* closure of the dataset invites the reader to ask "what is done with these numbers?", which the formula statement must answer.

**Paragraph 2 — Statistical Formula Statement**

- Move 1: **Section title / topic announcement.** "B. SPEARMAN'S RANK CORRELATION COEFFICIENT" — names the technique the data will be subjected to. *Hand-off:* having named the technique, the reader expects the operational form of it; the next move must therefore display the formula.
- Move 2: **Formula presentation.** "𝑅𝑠 = 1 − (6∑𝐷2)/(𝑛3−𝑛)" — gives the working equation in symbolic form. *Hand-off:* an equation alone is opaque, so the reader requires a symbol key; this is answered next.
- Move 3: **Symbol unpacking.** "Rs is the correlation coefficient, D the difference between the ranks and n the number of ranks" — defines each symbol by stating *what it represents*. *Hand-off:* with both the equation and the legend supplied, the next move must point to where this technique will be applied (the critical-values table that follows).

**Paragraph 3 — Forward Pointer**

- Move 1: **Section label.** "C. CRITICAL VALUES" — signals the next appendix block. *Hand-off:* the heading functions as a transition device, telling the reader the formula is about to be benchmarked against a significance threshold.

---

## What This Section Does (content sequence)

This is an **appendix / supporting-evidence block**, not an argument. The ordered moves it makes are:

1. **Units header first.** Sets the measurement system so the numbers below are interpretable on first read.
2. **Grouped raw data.** Numbers are clustered by *Site* (the first column acts as a grouping key), so the reader can see within-site variation before any averaging or ranking.
3. **Technique name.** Names the statistical test the data will be put through (Spearman's rank), so the reader knows what comes next is method, not more data.
4. **Formula display.** Presents the exact symbolic form so the reader can replicate the calculation.
5. **Symbol legend.** Each symbol in the formula is defined inline in one clause, preserving brevity.
6. **Forward pointer.** A new section heading ("Critical Values") hands the reader to the significance table, completing the inferential arc (data → test → benchmark).

The *why* of the order: units before numbers (so numbers are readable), grouped data before test (so the reader has seen the raw evidence the test will act on), test name before formula (so the formula is anticipated), formula before legend (so the legend explains symbols already encountered), and finally a heading that bridges to the threshold check.

A student replicating this sequence for a different investigation would: (i) declare units, (ii) present raw data grouped by sample/location, (iii) name the statistical technique, (iv) write the formula, (v) define each variable in one sentence, (vi) pointer to the critical-values table.

---

## Paragraph Skeletons (replicable templates)

### SKELETON A — Grouped Raw Data Block

"[Column header row giving units]. [Group-A label column heading]. [Group A: n rows of values]. [Group B label column heading]. [Group B: n rows of values]. [Group C label column heading]. [Group C: n rows of values]."

1. **What each slot holds.** Slot 1 = a header line with parenthetical units; Slots 2/4/6 = a short label that names the grouping (e.g. "Site 1"); Slots 3/5/7 = parallel rows of numerical measurements in the same column order.
2. **How to fill with a different idea.** Slot 1: pick the variables you measured and write their units in a single header line. Slots 2, 4, 6: choose a categorical grouping that divides your sample (site, time, condition). Slots 3, 5, 7: list the measurements for each group with consistent column alignment.
3. **Original filled version.** "(mm)         (mm)         (mm)       Shape Index / 1       1.89       2.51     0.05      0.13" — Site-tagged rows of stream-measurement data.
4. **Demonstration fill (different idea).** "(°C)        (kPa)        (rpm)        Yield / Trial 1     22.5     101.3      1500        0.87" — chemistry-yield data grouped by trial number instead of by site.

### SKELETON B — Formula Statement with Inline Legend

"[LETTER. NAME OF TECHNIQUE]. [Equation written symbolically]. [Legend clause: each symbol defined as what it represents], [second symbol defined] and [third symbol defined]."

1. **What each slot holds.** Slot 1 = a section letter + the technique's full name (title case). Slot 2 = the working equation. Slot 3 = one running sentence beginning "Where …" that defines every symbol used in the formula.
2. **How to fill with a different idea.** Slot 1: pick a statistical test. Slot 2: write its standard form. Slot 3: list each variable in the order they appeared in the formula and define each with "the [quantity] it measures".
3. **Original filled version.** "B. SPEARMAN'S RANK CORRELATION COEFFICIENT / 𝑅𝑠 = 1 − (6∑𝐷2)/(𝑛3−𝑛) / Where Rs is the correlation coefficient, D the difference between the ranks and n the number of ranks."
4. **Demonstration fill (different idea).** "D. PEARSON'S PRODUCT-MOMENT CORRELATION / r = (Σ(xᵢ − x̄)(yᵢ − ȳ)) / √(Σ(xᵢ − x̄)² · Σ(yᵢ − ȳ)²) / Where xᵢ, yᵢ are the paired observations, x̄ and ȳ their sample means, and Σ denotes summation across all pairs."

### SKELETON C — Forward-Pointer Heading

"[LETTER. NEXT-TABLE LABEL]"

1. **What each slot holds.** A capital letter continuing the appendix sequence, followed by a 2–3-word label naming the next lookup table.
2. **How to fill with a different idea.** Continue lettering from the previous block; choose a label that names the *function* of the next table (critical values, conversion factors, constants).
3. **Original filled version.** "C. CRITICAL VALUES"
4. **Demonstration fill (different idea).** "E. PHYSICAL CONSTANTS" — same skeletal role, different content.

---

## Express-Idea Vocabulary

**Sequencing / grouping**
- "(km)       (m)     (m)       (m/s)" — header row enforces reading order on the numerical columns that follow.
- "1       1.89       2.51" — leading integer "1" repeats to mark Site 1 as a contiguous group, then changes to "2" and "3" to mark new groups.

**Symbol-handling (definition-style)**
- "Where Rs is the correlation coefficient" — assigns meaning to a symbol by stating what it *is*.
- "D the difference between the ranks" — compact "symbol + verbal definition" pattern, no verb.
- "n the number of ranks" — same "symbol + definition" pattern.

**Technique-naming (context-setting)**
- "B. SPEARMAN'S RANK CORRELATION COEFFICIENT" — names the apparatus the data will be subjected to.

**Forward-pointer (transition)**
- "C. CRITICAL VALUES" — signals the next block without explanation.

---

## How to Explain an Idea (replication steps)

The pattern this section relies on is **labelled-data → named-technique → symbolic-form → inline-legend → threshold-pointer**. To replicate it for a NEW statistical / computational technique:

1. **Present the raw data first**, grouped by a single categorical key (site / trial / condition). Declare units in a header line so the numbers below are instantly legible.
2. **Cluster the data** by that key (e.g. all Site 1 rows together, then Site 2, then Site 3) so within-group variability is visible before any aggregation.
3. **Name the technique** as a section heading ("B. [TEST NAME]") so the reader knows the dataset is about to be processed.
4. **Display the formula** in standard symbolic form on a single line.
5. **Add a single "Where …" clause** that defines each symbol in the order it appeared in the formula, using the compressed pattern "Symbol is the [meaning], Symbol the [meaning] and Symbol the [meaning]".
6. **Close with a forward-pointing heading** ("C. CRITICAL VALUES" or equivalent) that announces the significance threshold or lookup table the formula will be checked against, completing the inferential chain data → test → benchmark.
