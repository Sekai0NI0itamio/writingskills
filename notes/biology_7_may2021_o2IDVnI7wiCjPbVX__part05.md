# Idea Flow Notes: biology_7_may2021_o2IDVnI7wiCjPbVX — people

## Paragraph Flow (move by move)

The text contains no prose paragraphs — it is a data table split across two visible blocks (a page break splits rows between "India" and "Indonesia") followed by one sentence-fragment of a note.

**Block 1 — Table rows 1–19 (column header to India)**

- **Move 1: Column header row.** Acts as orientation: "2017 2016 2015 2014 2013". *Function:* defines the temporal axis. *Hand-off:* the first country name must be read against this axis — the header sets the schema every subsequent row instantiates.
- **Move 2: Country rows in alphabetical order (Angola → India).** Acts as evidence inventory: "Angola 12995.69 13155.09 9931.38 …" Each row *replicates the same slot pattern* (name, then six numeric values) so the reader can scan vertically and compare magnitudes. *Hand-off:* alphabetical sequencing means no row "leads to" the next logically — adjacency is taxonomic, not argumentative. The reader is handed from row to row by alphabetical convention, which is itself a methodological choice (standardised ordering = no selection bias in presentation).

**Page break** — the table resumes mid-page with row "Indonesia" as the first line of the second block, signalling continuation rather than a new section.

**Block 2 — Table rows 20–end (Indonesia → Zimbabwe)**

- **Move 3: Country rows continued (Indonesia → Zimbabwe).** Same replicable slot pattern as Block 1: "Indonesia 98.86 83.52 83.99 …". *Hand-off:* continues the alphabetical scan; the reader's hand to the next sentence comes from the residual expectation that more rows will follow.
- **Move 4: Justification note (incomplete).** Acts as caveat/methodological footnote: "Note that data for the cases of malaria for Cameroon in the year 2014 and Nigeria in 2013 were not" — the sentence is cut off but its *job* is clear. It (a) flags missing values (Cameroon shows "n/a" in 2014; Nigeria shows "n/a" in 2013), and (b) attributes those gaps to data unavailability. *Hand-off:* the note is unfinished in the text supplied, but its intended hand-off would be to either a list of further gaps or a statement of how missing data was handled.

## What This Section Does (content sequence)

This is a **raw-data presentation section** for an empirical investigation. The ordered moves are:

1. **Temporal axis (column headers).** Comes first because every number that follows is meaningless without the year it belongs to; the header defines the unit of comparison.
2. **Case-by-case enumeration (country rows).** Comes second because the section's job is to lay the dataset flat before the reader; alphabetical ordering is chosen so the reader can locate any country without the author having privileged some cases over others.
3. **Continuation across page boundary (no caption, no re-statement of header).** Comes third because the author assumes the reader carries the header forward — a deliberate choice to keep the table compact and force the reader to keep the schema active in memory.
4. **Caveat / data-quality note (final).** Comes last because it is a *meta-comment on the table*, not part of the table; it belongs after the reader has seen the "n/a" entries and needs them explained. Placing it first would orphan it; placing it mid-table would interrupt scanning.

Replication principle: **orient the axis → lay every case in a fixed neutral order → interrupt the scan only at the end to flag missing data**. The order is dictated by what each move *enables*: the header enables reading the rows; the rows enable the reader to formulate questions; the note enables the reader to trust the answers.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Tabular Header Row**
```
[dimension 1 label] [dimension 2 label] [dimension 3 label] …
```
1. **What each slot holds:** short noun-phrase or numeral tokens naming the variable being measured for each column. Grammatically parallel bare phrases, no verb.
2. **How to fill with a different idea:** slot 1 = the time/condition dimension (years, trials, sites); slots 2+ = parallel categories of the same type as slot 1 (other years, other trials, other sites). Keep all labels in the same form (all four-digit years, all two-letter site codes, etc.).
3. **Original filled version:** "2017 2016 2015 2014 2013".
4. **Demonstration fill with a different idea:** "Trial 1 Trial 2 Trial 3 Trial 4" (for a lab-experiment dataset measuring reaction time across four trials).

**SKELETON B — Data Row (case instance)**
```
[case label, alphabetically ordered] [numeric value 1] [numeric value 2] [numeric value 3] …
```
1. **What each slot holds:** slot 1 = a proper-noun identifier of the unit being observed (country, participant, specimen); slots 2+ = numeric measurements whose order matches the header row. All values share units with the header's variable.
2. **How to fill with a different idea:** slot 1 = a concrete, named instance from your dataset, in the sort order you have chosen (alphabetical, chronological, by magnitude — state the choice); slots 2+ = the raw numbers for that instance, in the same column order as the header. No prose, no commentary — just the row.
3. **Original filled version:** "Malawi 27737.81 28057.49 21864.27 17835.43 8086.81 20716.37".
4. **Demonstration fill with a different idea:** "Participant 07 4.2 3.9 5.1 4.7 4.4 4.46" (for a psychology study recording anxiety scores across six sessions).

**SKELETON C — Missing-Data Footnote**
```
Note that data for the cases of [phenomenon] for [case A] in [condition X] and [case B] in [condition Y] were not [available / recorded / applicable].
```
1. **What each slot holds:** slot 1 = the variable measured; slots 2 and 3 = the (case, condition) pairs that produced a gap; slot 4 = the verb phrase stating *why* the cell is empty (available, recorded, reported, applicable). Single sentence, often placed beneath the table.
2. **How to fill with a different idea:** scan your completed table for empty/"n/a" cells; list each one as a (case, condition) pair; aggregate them in one sentence using "Note that … were not …". One sentence per gap-cluster.
4. **Original filled version:** "Note that data for the cases of malaria for Cameroon in the year 2014 and Nigeria in 2013 were not".
3. **Demonstration fill with a different idea:** "Note that data for reaction times for Participant 12 in Trial 3 and Participant 18 in Trial 5 were not recorded due to equipment failure."

## Express-Idea Vocabulary

Because this section is tabular, "vocabulary" here is structural rather than connective.

- **Sequencing / ordering tokens:** the year numerals themselves "2017 2016 2015 2014 2013" function as time-ordered labels (descending — recent first). No "firstly/secondly" is used because rows are not argued, they are listed.
- **Caveat / qualification marker:** **"Note that"** — opens the explanatory footnote: "Note that data for the cases of malaria". Job: signals a deviation from the otherwise unannotated table.
- **Absence marker (evidence-handling):** **"n/a"** — used inline in the Cameroon and Nigeria rows to flag missing values without prose. Job: lets the reader see the gap in context, then read the footnote for the reason.
- **Enumeration signal (implicit):** the repeated identical row-slot pattern (name + six numerals, name + six numerals) is itself a *rhetorical device* — it tells the reader "every case is treated with equal weight". No verb is needed; the parallelism does the work.
- **Implicit unit verb:** none. The table relies on the header row to carry all definitional load; no sentence-level verbs are present because no sentence is present.

## How to Explain an Idea (replication steps)

This section does **not** use a prose explanation pattern (no definition → unpack → example → implication chain). It uses a **tabular-evidence pattern**. To replicate:

- **Step 1 (define the axis):** Identify the single variable the reader must hold in mind across all rows. State it as column headers in a fixed order (typically most-recent-first for time series, or largest-magnitude-first for comparisons). Do not yet show data.
- **Step 2 (fix the unit order):** Choose a neutral ordering rule for the rows — alphabetical for named cases, chronological for events, or sorted by a second variable if you are making that variable's variation visible. State the rule implicitly by following it strictly.
- **Step 3 (populate every row identically):** For each case, fill every column with the raw numeric value. Use a consistent decimal-place convention across the whole table. Do not summarise, round to "headline" figures, or omit "uninteresting" cases.
- **Step 4 (mark absences where they exist):** Where a measurement is missing, write "n/a" in the cell — do not leave the cell blank (which reads as a typo) and do not write 0 (which reads as a real value).
- **Step 5 (close with a single caveat sentence):** After the last row, add one sentence beginning "Note that …" that names each (case, condition) pair where data is missing and states the reason (not available, not recorded, not applicable). One sentence per cluster of gaps; never interrupt the row list with mid-table caveats.

The logic the pattern enforces: *let the table speak first, qualify the table second*. The reader is invited to scan, compare, and form their own observations before the author intervenes to explain any anomaly.
