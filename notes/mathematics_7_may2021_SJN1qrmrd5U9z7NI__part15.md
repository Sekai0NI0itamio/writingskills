# Idea Flow Notes: mathematics_7_may2021_SJN1qrmrd5U9z7NI — 23 Anti-Procrastinat…                91          3.64    The Truth About Magic                         256             3.98          Restore Me                       435          4.18     Diary of a Wire                                  226      3.98

## Paragraph Flow (move by move)

**Paragraph 1 — The raw data table (book list)**

- **Move 1 — Data inventory introduced by formatting.** The block opens with no prose preamble; the table itself is the paragraph. The implicit move is *context-setting by enumeration*: a title appears alongside its two numerical columns. Quote: *"The Worrier's Guide… 112 3.63"*. Hand-off: the reader is now oriented to the unit structure (title + pages + rating) and expects that pattern to repeat.
- **Move 2 — Sequential listing in ascending order.** Each row is ordered by page count within its column — *"112, 120, 132, 144, 152…"*. This is a *sort move*. Hand-off: because ascending page count is the visible signal, the reader infers x = page count is the independent variable being prepared for later analysis.
- **Move 3 — Rating attached as the dependent observation.** A third numerical value is paired with every title — *"3.63"* after *"112"*. This is a *paired-data move*. Hand-off: the reader now has the x,y pairs needed for correlation.
- **Move 4 — Parallel columns to compress horizontal spread.** The data is split into four side-by-side columns of equal rank ordering — *"If I Stay… 261 3.94"*, *"City of Bones 442 4.09"*, *"Holes 233 3.97"*. This is a *layout/economy move*. Hand-off: the reader is shown that the four columns are independent slices of the same dataset, not different groups.
- **Move 5 — Outliers flagged visually.** Two entries carry an asterisk — *"Harry Potter & Order..* 870 4.45"* and *"It * 1116 4.24"*. This is an *annotation move*. Hand-off: the reader is warned that extreme values exist at the top of x and must be handled (or justified) in the next stage.

**Paragraph 2 — Appendix 2: Pearson's Coefficient Calculations**

- **Move 1 — Section label declaring the procedure.** Quote: *"Appendix 2: Pearson's Coefficient Calculations"*. This is a *method-identifier move*. Hand-off: the reader now expects every column to be a defined step of the Pearson formula, not arbitrary numbers.
- **Move 2 — Variables x and y named in the header.** The columns open with the symbols *"x"* and *"y"* — *"720 4.34"*. This is a *variable-definition move*. Hand-off: the reader maps back to Paragraph 1 and now knows pages = x and rating = y.
- **Move 3 — Mean-deviation columns introduced.** Header row reads *"(xᵢ − x̄) (yᵢ − ȳ)"* — *"402.791 0.365"*. This is a *formula-unpack move*. Hand-off: the reader sees that each row first isolates the deviation before any product is taken.
- **Move 4 — Product and squared-deviation columns appended.** Headers *"(xᵢ − x̄)(yᵢ − ȳ)"*, *"(xᵢ − x̄)²"*, *"(yᵢ − ȳ)²"* appear beside each row — *"146.878 162240.346 0.133"*. This is a *working-out move*. Hand-off: the reader can now sum each of these columns to reach r, and the layout invites that summation as the implicit next step.
- **Move 5 — Rows continued across the same calculation template.** The second row repeats the identical six-column pattern — *"672 4.37 354.791 0.395 140.019 125876.439 0.156"*. This is a *repetition-as-validation move*. Hand-off: the reader trusts the method because it is applied uniformly; the next sentence would be the final Σ step that closes the appendix.

## What This Section Does (content sequence)

1. **Raw paired-data inventory first** — so the reader can verify the sample and the variables before any formula is invoked.
2. **Sort the inventory by the independent variable** — so that outliers (longest books) are visually conspicuous and so that x is monotonically ordered, a small clarity gain for the calculation.
3. **Compress into parallel columns** — to keep the dataset one page wide; this is a presentation choice, not a logical one, but it preserves one-to-one pairing.
4. **Flag extreme x-values with an annotation** — to pre-empt the criticism that a 1116-page novel could distort a Pearson r computed on a mostly short-book sample.
5. **Title the calculation appendix explicitly** — so the reader knows the test being applied.
6. **List variables in the column header** — x and y are introduced before numbers, so the reader maps the table back to the dataset in step 1.
7. **Show each formula component as its own column** — deviations, products, squared deviations — so every intermediate quantity is auditable.
8. **Apply the same six-column template to every row** — uniformity is the argument: any row can be checked against the formula.
9. **Leave the summation / final r implicit** — the appendix stops one step before r itself, handing the reader the values needed to complete it. The student replicates this sequence whenever raw data must be defended before a statistical claim is made.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Sorted raw-data inventory"**

> [Row 1: title … pages rating] [Row 2: title … pages rating] [Row 3: title … pages rating] … (presented in N parallel columns, ascending by independent variable).

1. **Slot 1 — title field.** A noun phrase (book / film / song / case name); may be truncated with an ellipsis when long.
2. **Slot 2 — independent variable.** Integer or continuous measure on which rows are sorted ascending.
3. **Slot 3 — dependent variable.** Decimal rating / score paired to slot 2.
4. **Slot 4 — column count.** Chosen so total width fits one page; each column independently sorted.
5. **Slot 5 — outlier marker.** Asterisk attached to any row that is extreme on the independent axis.

**How to fill with a different idea:** slot 1 = any named item from your dataset (podcast episode, experiment trial, country); slot 2 = the quantitative variable you want to correlate (duration, temperature, GDP); slot 3 = the response variable (rating, yield, life expectancy); slot 4 = pick 3–4 columns so the table stays one page; slot 5 = star the row whose x is more than ~3 SD from the mean.

**Original filled version:** *"Hatchet 186 3.74"* / *"Looking for Alaska 350 4.01"* — two adjacent rows from the dataset, pages ascending.

**Demonstration fill (different idea):** *"Episode 12: Mars 47 8.2"* / *"Episode 03: Venus 39 7.8"* — podcast length vs listener rating, same skeleton.

**SKELETON B — "Transparent statistical-working appendix"**

> [Appendix label]: [Test name]. [Variable headers in order: x, y, (xᵢ − x̄), (yᵢ − ȳ), (xᵢ − x̄)(yᵢ − ȳ), (xᵢ − x̄)², (yᵢ − ȳ)²] [Row of numerical values matching header order] [Same template repeated per case].

1. **Slot 1 — appendix tag.** "Appendix N:" followed by the full name of the test.
2. **Slot 2 — variable symbols.** Use italic x and y so the reader instantly recognises the formula.
3. **Slot 3 — deviation columns.** Write the algebraic form with subscripts and a bar over the mean — the reader sees the formula, not just numbers.
4. **Slot 4 — product and squared-deviation columns.** Three more columns whose headers are the literal factor pairs.
5. **Slot 5 — per-case row.** Every case is one row, six numbers in header order; precision to 3 d.p. is conventional.

**How to fill with a different idea:** choose any bivariate test (Spearman, t-test, chi-squared expected-count table); slot 1 = label it "Appendix N: [Test]"; slot 2 = name your two variables; slots 3–4 = put each formula term in its own column header; slot 5 = one row per case, values to 3 d.p.

**Original filled version:** *"Appendix 2: Pearson's Coefficient Calculations"* with header row *"x y (xᵢ − x̄) (yᵢ − ȳ) (xᵢ − x̄)(yᵢ − ȳ) (xᵢ − x̄)² (yᵢ − ȳ)²"*.

**Demonstration fill (different idea):** *"Appendix 3: Spearman's Rank Calculations"* and header *"x y R(x) R(y) R(x)−R(y) (R(x)−R(y))²"* — different test, identical skeleton.

## Express-Idea Vocabulary

This section is almost entirely numeric, so its "connectives" are the column-header symbols and the title phrase. Grouped by job:

- **Sequencing / labelling moves** — *"Appendix 2:"* opens a new computational stage after the data list.
- **Variable identification** — the italicised letters *"x"* and *"y"* in the header row establish which column is which variable.
- **Specification of formula components** — the bracketed headers *"(xᵢ − x̄)"*, *"(yᵢ − ȳ)"*, *"(xᵢ − x̄)(yᵢ − ȳ)"*, *"(xᵢ − x̄)²"*, *"(yᵢ − ȳ)²"* spell the Pearson formula piece by piece.
- **Procedure-naming** — *"Pearson's Coefficient Calculations"* in the appendix title tells the reader the statistical test being performed.
- **Annotation / outlier flag** — the asterisk on *"Harry Potter & Order..*"* and *"It *"* marks extreme values without interrupting the table.
- **Implied summation** — there is no prose verb, but the repetition of the six-column row *"(720, 4.34, 402.791, 0.365, 146.878, 162240.346, 0.133)"* signals that columns are designed to be summed next.

## How to Explain an Idea (replication steps)

The pattern this section uses is **method-naming → variable definition → formula-unpacking via column headers → uniform per-case working → hand-off to summation**. It is a *transparent-calculation* explanation, not a discursive one.

To replicate it for a NEW idea:

1. **Name the method in a heading.** Open with *"Appendix N: [Name of Test]"* so the reader knows which formula is being applied.
2. **Declare the two variables in the first two column headers.** Use symbols (x, y) and never numbers alone.
3. **Transcribe every term of the formula as its own column header**, written in algebraic notation with subscripts and mean bars. The header row *is* the explanation; the reader should be able to read the formula off the top of the page.
4. **Give one row per case, with values in header order**, to a consistent decimal precision (3 d.p. here). Uniformity is the proof of method.
5. **Append a short note on outliers or assumptions** (the asterisk on *"870"* and *"1116"* does this job) before the final computation is implied.
6. **Stop one step short of the final statistic**, leaving the reader to sum the columns — this is how the appendix *hands the calculation* to the result section without duplicating it.
