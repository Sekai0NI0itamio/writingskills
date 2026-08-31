# Idea Flow Notes: biology_7_may2021_o2IDVnI7wiCjPbVX — Republic

## Paragraph Flow (move by move)

This text is not prose with sentences; it is a **data table fragment** spanning two pages. Treating it as a section, the "paragraphs" are the two row-blocks separated by the page number "5". Each "sentence" is a row (a country record).

**Block 1 (rows: Ecuador → Malaysia, before page break):**

Row 1 — **Ecuador**: *Data entry / specimen instance.* "Ecuador 1275 1191 618…" — ten numeric fields presented sequentially. Hands to next row by **continuation**: the reader expects the same column shape repeated for the next country.
Row 2 — **Ethiopia**: *Data entry / larger-scale instance.* "Ethiopia 1530739 1718504…" — hands forward by **same schema, contrast in magnitude** (values jump two orders of magnitude vs. Ecuador, silently inviting comparison).
Row 3 — **Guatemala**: *Data entry.* "Guatemala 3743 4853…" — hands forward by **schema repetition**.
Row 4 — **Guinea**: *Data entry.* "Guinea 1335323 992146…" — hands forward by **schema repetition; a downward trend in column 1 implicitly begins to emerge, which the next rows accumulate**.
Row 5 — **Haiti**: *Data entry / small first-column value contrast.* "Haiti 19135 21430…" — hands forward by **schema repetition; the abrupt drop after Guinea sets up the next row's spike**.
Row 6 — **Honduras**: *Data entry.* "Honduras 1277 4094…" — hands forward by **schema repetition**.
Row 7 — **India**: *Data entry / population-scale anchor.* "India 844558 1087285… 1338658830…" — hands forward by **schema repetition; the population column dwarfs all prior rows, calibrating the reader's sense of scale**.
Row 8 — **Indonesia**: *Data entry.* "Indonesia 261617 218450…" — hands forward by **schema repetition**.
Row 9 — **Laos**: *Data entry / mid-scale instance.* "Laos 9333 11223…" — hands forward by **schema repetition**.
Row 10 — **Madagascar**: *Data entry.* "Madagascar 800661 475333…" — hands forward by **schema repetition**.
Row 11 — **Malawi**: *Data entry / large first-column outlier.* "Malawi 4901344 4827373…" — hands forward by **schema repetition; this row's column-1 magnitude rivals Ethiopia's, priming the eye for the next row's drop**.
Row 12 — **Malaysia**: *Data entry / minimum first-column value.* "Malaysia 85 266…" — hands to the page break by **schema closure**: the smallest values in the block, ending on a low point before the next page.

**Page break marker:** "5" — *navigation artifact*, not a logical move; resets the reader to a new block.

**Block 2 (rows: Myanmar → Papua New Guinea):**

Row 13 — **Myanmar**: *Data entry / restart of schema after break.* "Myanmar 19619 110146…" — hands forward by **explicit schema re-establishment** (the reader must re-confirm column order).
Row 14 — **Nepal**: *Data entry.* "Nepal 623 507…" — hands forward by **schema repetition**.
Row 15 — **Niger**: *Data entry / large first-column values.* "Niger 2638580 4148167…" — hands forward by **schema repetition**.
Row 16 — **Nigeria**: *Data entry / schema violation marker.* "Nigeria 11571958 9234387… n/a …" — hands forward by **schema-with-anomaly**: the literal "n/a" in the fifth numeric column breaks the otherwise uniform pattern, signalling missing data rather than zero.
Row 17 — **Papua New**: *Data entry / closing row.* "Papua New 478340 478497…" — hands off the section by **schema closure**: the final row, the table simply stops.

---

## What This Section Does (content sequence)

This is a **raw-data table**, not an argumentative section. Its move-sequence is:

1. **Schema establishment (first row).** A country name followed by a fixed number of numeric columns. The reader must infer the column meaning from position and from the population-sized final columns.
2. **Repetition with implicit ordering.** Subsequent rows repeat the schema in alphabetical order (Ecuador, Ethiopia, Guatemala…). Each row *implicitly compares* to the last by column position.
3. **Magnitude variation as silent argument.** No commentary accompanies the rows; the variation in column 1 (e.g., Malaysia's 85 vs. Nigeria's 11,571,958) is left to the reader to notice. The table *presents*, it does not *narrate*.
4. **Schema continuation across page break.** A page number (5) interrupts; the next row re-anchors the schema.
5. **Schema-with-anomaly closure.** A missing value ("n/a") appears in the second block, the only verbal token in the table — it is the section's only deviation from pure numeric data.
6. **Abrupt termination.** The table ends mid-alphabet (Papua New Guinea, not Guinea-Bissau); the section is a fragment, not a complete table.

**Why this order:** for a data appendix, ordering is the argument. Alphabetical order makes individual rows retrievable; column order makes cross-row comparison possible; population columns placed last anchor the absolute scale against which the earlier (presumably per-capita or count) columns should be read. The page break is handled by re-issuing the schema immediately.

---

## Paragraph Skeletons (replicable templates)

**SKELETON 1 — Single data row (the atomic unit):**
`[CountryName] [num1] [num2] [num3] [num4] [num5] [pop1] [pop2] [pop3] [pop4] [pop5]`

- **Slot 1 (`CountryName`):** a proper noun, title-cased, no article; identifies the unit of observation.
- **Slots 2–6 (numeric series A):** five integers, no commas, no units, separated by whitespace; presumably a time series of one variable.
- **Slots 7–11 (numeric series B):** five integers, sometimes comma-grouped (e.g., "16,785,360"), two-to-three orders of magnitude larger than series A; presumably population at the same time points.
- **Filling instructions:** slot 1 = pick a country alphabetically adjacent to your neighbour rows; slots 2–6 = a 5-period time series of your measured variable; slots 7–11 = matching population estimates; keep the comma convention consistent *within* the row.
- **Original filled version:** "Ethiopia 1530739 1718504 1867059 2118815 2645454 106400020 103603500 100835460 98,094,250 95,385,790"
- **Demonstration fill (different idea — language data):** "Finland 8421 9012 9587 10203 10876 5548090 5523000 5498200 5473000 5451000"

**SKELETON 2 — Interruption / page-break marker:**
`[isolated page number, centered or right-aligned]`

- **Slot:** a single integer, no surrounding text.
- **Filling instructions:** use the actual page number of your document; do not label it.
- **Original filled version:** "5"
- **Demonstration fill (different idea):** "12"

**SKELETON 3 — Schema-violation row:**
`[CountryName] [num1] [num2] [num3] [num4] n/a [pop1] [pop2] [pop3] [pop4] [pop5]`

- **Slot 5:** the literal string "n/a", lowercase, used exactly once in the table.
- **Filling instructions:** reserve this row for a country whose series-A value is genuinely unavailable; do not use 0 or a blank — the explicit marker is what carries the information.
- **Original filled version:** "Nigeria 11571958 9234387 6850782 7826954 n/a 190873310 185960290 181137450 176,404,900 171765770"
- **Demonstration fill:** "Somalia 4123000 3890000 n/a 2950000 2780000 16320000 16100000 15890000 15685000 15499000"

**SKELETON 4 — Magnitude-contrast row pair (no template, but a pattern):**
A small-series-A row (e.g., "Malaysia 85 266…") followed at some distance by a large-series-A row (e.g., "India 844558…"). Adjacency is not required; the *range* across the table is the rhetorical device.

- **Filling instructions:** when assembling such a table, ensure the smallest and largest series-A values are both present so the reader can self-locate; do not annotate the contrast in prose.
- **Original pattern (paraphrased):** "Malaysia" begins with 85; "Nigeria" begins with 11,571,958 — a 5-order-of-magnitude spread with no commentary.
- **Demonstration fill:** rows beginning with "Iceland 12 18…" and "China 1842000 1925000…" in the same table.

---

## Express-Idea Vocabulary

Because this is a data table, the usual connectives ("however", "therefore") are **absent**. The vocabulary of idea-expression here is structural, not lexical:

- **Sequencing / ordering (implicit):** alphabetical sort by country name — "Ecuador, Ethiopia, Guatemala, Guinea, Haiti, Honduras, India, Indonesia, Laos, Madagascar, Malawi, Malaysia…"
- **Specification / marking a gap:** the literal token "n/a" — "Nigeria 11571958 9234387 … n/a 190873310" (handles the only case where the schema cannot be filled).
- **Magnitude signalling (via digit grouping):** comma insertion at the thousand mark in larger numbers — "16,785,360" vs. "1275" — silently distinguishes small from large values without using words.
- **Schema-anchor repetition:** identical column count (eleven numeric fields) reasserted on every row — "Ecuador 1275 1191 618 242 368 16,785,360 16491120 16,212,020 15,951,840 15,707,470" — the repetition itself is the explanation mechanism.
- **Page-boundary marker:** the numeral "5" alone — no phrase, no connective, the break is purely typographic.

For a *prose* section, the analogous vocabulary would be: sequencing ("firstly", "next"), cause ("therefore", "thus"), contrast ("however", "whereas"), specification ("in particular", "that is"), evidence ("according to", "this suggests"), definition ("defined as", "is measured by"). None of these appear here because the section delegates logical work to **column position and row ordering** rather than to connectives.

---

## How to Explain an Idea (replication steps)

The pattern this section uses is **schema-and-instances** (also called "tabular presentation"): state a fixed column structure once, then let repetition of the structure do the explanatory work.

To reproduce this pattern for a new idea:

1. **Decide the columns.** Choose 2–3 *types* of measurement that you want the reader to compare across units. Place the variable that varies most (or that is the focus) in the leftmost data column; place the absolute-scale anchor (e.g., population) last. (Example: per-capita emissions first, total population last.)
2. **Pick the unit of observation.** This becomes the row label — countries here, but it could be species, years, schools, patients. Make sure every unit is comparable on every column.
3. **Order the rows deliberately.** Alphabetical = lookup; chronological = trend; descending by column 1 = ranking. Choose the order that lets the reader see the argument you want without you having to write the argument in prose.
4. **Fill every cell in every row** except where data is genuinely missing. For genuine gaps, use one consistent missing-value token ("n/a", "—", "..") and use it sparingly — one occurrence per table is ideal, because it draws the eye to the only place the schema breaks.
5. **Format numbers to reveal magnitude.** Use comma-grouping for large values; do not mix styles within a column. The *visual* size of the number is information.
6. **Do not annotate.** Resist adding sentences, captions, or footnotes inside the table body. The whole point of the schema-and-instances pattern is that the structure itself carries the explanation.
7. **Anchor after any page break.** The first row on a new page must restate the full schema (all columns, in order) so the reader can resume reading without backtracking.
8. **End on a row that closes the alphabet/sequence cleanly,** or, if the table is a fragment, accept the truncation and let the reader infer that more rows follow.

The section's *explanation* — that some countries have series-A values in the tens of millions while others have series-A values in the dozens, against populations in the tens of millions either way — emerges entirely from the reader scanning columns 2 and 7 against the country name. No verb of explanation is needed.
