# Idea Flow Notes: chemistry_7_may2020_OOzgzXzKMnCvdlfZ — Quantitative Observations

## Paragraph Flow (move by move)

This section contains one functional block after the table: a three-sentence note. I treat the table-title line as a pre-block setup.

**Setup line (table title):** "A table displaying the time taken in each experiment to produce 10cm3 of oxygen gas at all investigated temperatures for the catalysed decomposition of hydrogen peroxide."
- Move: **label + scope claim** — names the artefact ("Table 3"), declares the measured variable ("time taken"), the fixed outcome ("10cm3 of oxygen gas"), the swept parameter ("temperatures"), and the system ("catalysed decomposition of hydrogen peroxide").
- Hands the reader to: the actual table, because the line promises exactly the columns and rows the reader is about to inspect; the scope claim primes the reader to verify that the rows/columns match.

**Block — Note paragraph (3 sentences):**

**Sentence 1:** "The result in bold in Table 3 is anomalous, and will not be included in any further calculations."
- Move: **flag + exclusion decision.** Identifies a specific cell (the bold value) and announces it will be dropped from later work.
- Hands the reader to sentence 2 via **cause/reason expectation — the reader now asks *why a row was bold and why it was excluded*; the next sentence supplies the methodological reasoning that frames the exclusion.

**Sentence 2:** "Furthermore, displayed values are shown to one decimal place to align with the uncertainty of the stopwatch and reaction time."
- Move: **precision justification**, signalled by "Furthermore" (additive continuation, not new topic). It explains a *display* convention by tying it to the resolution of two instruments ("the stopwatch and reaction time"). It also implicitly generalises the bold/exclusion point into a broader principle about honest reporting of measured precision.
- Hands the reader to sentence 3 via **tension/contrast —** once rounding is justified, the reader anticipates an apparent conflict (if values are rounded for display, what was actually computed?), which sentence 3 resolves.

**Sentence 3:** "Full values were used in all calculations."
- Move: **disambiguation / calculation-method clarification.** Contrasts with the rounded display values; specifies that the working numbers were the unrounded ones.
- Hands the reader to: the closing "Qualitative Observations:" heading, via **category shift** — the reader has finished audit-trail reasoning for the *quantitative* data, and the next block switches register to descriptive observation.

## What This Section Does (content sequence)

This is a **data-presentation section with a transparency audit-trail.** The ordered moves are:

1. **Artefact label + scope claim** (Table 3: …). Sets up what the reader is looking at and constrains the columns/rows.
2. **The data table itself.** Delivers the raw observations the rest of the report will use.
3. **Anomaly flag + exclusion decision.** Tells the reader which datum is being removed and that downstream calculations will not use it (establishes honesty about a clear outlier).
4. **Display-precision justification** ("Furthermore… to align with the uncertainty of…"). Explains *why* the table looks the way it does — the decimal places match the instrument, not arbitrary.
5. **Internal-calculation clarification** ("Full values were used…"). Closes the loop by disambiguating that the *rounding was only cosmetic* — actual maths used the raw numbers.

Why this order: **label → data → exception → display rationale → internal-method clarification.** Each move sets up a question the next move answers. The label previews the columns; the data creates the need to flag outliers; the flag raises the broader question of how precisely the data should be shown; the rounding raises the apparent conflict with calculation rigour; the final sentence removes that conflict.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Table-title line:**
`[Label]: A table displaying [quantity measured] for [system/process] at [swept parameter] for the [adjective-modifier] [process name].`

1. Slots:
   - Label: ordinal + noun ("Table 3").
   - Quantity measured: a dependent variable in the form "the [noun] [past participle]" ("the time taken").
   - System/process: a defined experimental target ("the catalysed decomposition of hydrogen peroxide").
   - Swept parameter: a plural or range phrase ("all investigated temperatures").
2. How to fill with a different idea: pick a single dependent variable you measured; pick a chemical or physical process; pick the independent variable you varied; combine into one noun phrase with "for" + "at".
3. Original filled: "Table 3: A table displaying the time taken in each experiment to produce 10cm3 of oxygen gas at all investigated temperatures for the catalysed decomposition of hydrogen peroxide."
4. Demonstration fill: *"Table 4: A table displaying the current recorded in milliamps for the discharging nickel-metal hydride cell at all investigated resistances across the 2.0–4.5 Ω range."*

---

**SKELETON B — Anomaly + exclusion note:**
`The result [format marker] in [reference] is anomalous, and will not be included in any further calculations.`

1. Slots:
   - Format marker: a typographic indicator ("in bold", "italicised", "circled").
   - Reference: label back to the artefact ("Table 3", "the graph below").
   - The decision clause is fixed: "will not be included in any further calculations."
2. How to fill: choose one clearly deviating data point you want to discard; mark it visually in the artefact; cite the artefact label.
3. Original filled: "The result in bold in Table 3 is anomalous, and will not be included in any further calculations."
4. Demonstration fill: *"The point circled in Figure 2 is anomalous, and will not be included in any further calculations."*

---

**SKELETON C — Precision-justification note:**
`Furthermore, displayed values are shown to [precision] to align with the uncertainty of the [instrument A] and [instrument/process B].`

1. Slots:
   - Precision: a decimal-place phrase ("one decimal place", "two significant figures").
   - Instrument A: the timing/measurement device ("stopwatch").
   - Instrument/process B: the human or second source of variability ("reaction time", "ruler reading", "operator start delay").
   - Lead-in: "Furthermore" (additive, not contrastive) — pairs naturally with Skeleton B.
2. How to fill: identify the dominant uncertainty in your experiment; name two sources (machine + human, or sensor + procedure); match the precision shown on screen to the worse of those two uncertainties.
3. Original filled: "Furthermore, displayed values are shown to one decimal place to align with the uncertainty of the stopwatch and reaction time."
4. Demonstration fill: *"Furthermore, displayed values are shown to two significant figures to align with the uncertainty of the voltmeter and the contact-resistance variation at the electrodes."*

---

**SKELETON D — Internal-calculation clarification:**
`Full values were used in all calculations.`

1. Slot: a one-sentence correction that contrasts the *displayed* precision with the *worked* precision; fixed imperative-style statement.
2. How to fill: state explicitly that any rounding visible to the reader was not carried into the maths.
3. Original filled: "Full values were used in all calculations."
4. Demonstration fill: *"Raw recorded values were used in all calculations; the two-significant-figure rounding applies only to the table."*

## Express-Idea Vocabulary

**Sequencing / addition**
- "Furthermore" — used to extend the *exclusion* sentence into a *display-precision* rationale; quoted: "Furthermore, displayed values are shown to one decimal place".

**Scope / limitation specifiers**
- "will not be included in any further calculations" — explicit boundary on where the datum flows next; quoted: "will not be included in any further calculations".
- "in all calculations" — universal scope on the calculation method; quoted: "Full values were used in all calculations".

**Causal / justification connectors**
- "to align with the uncertainty of" — anchors a display choice to the instrument's resolution; quoted: "to align with the uncertainty of the stopwatch".

**Description verbs (this section is sparse — mostly nominal/labelling)**
- "displaying" — presentational verb in the table title; quoted: "A table displaying the time taken".
- "is anomalous" — single-word verdict label justifying exclusion; quoted: "is anomalous".

**Evidence-handling phrasing**
- "The result in bold in Table 3" — points the reader to a typographically marked datum; quoted: "The result in bold in Table 3".

## How to Explain an Idea (replication steps)

This section is not an *explanation* of a phenomenon; it is a **transparency / audit-trail pattern for raw data**. The replication steps for any new experiment are:

1. **Name and constrain the artefact** (one sentence). State the label, what is being displayed, what was swept, and what system it describes. *Constraint:* this sentence must name the dependent variable, the independent variable, and the process in one noun phrase.
2. **Show the data** (the table itself). Order rows by the swept parameter; align units in headers.
4. **Flag and exclude the outlier** (one sentence). Pick the single most clearly anomalous cell, mark it visibly in the artefact, then declare it will not be reused. *Constraint:* the sentence must contain both a visual locator ("in bold", "circled", "italicised") and the word "anomalous" or equivalent.
5. **Justify the displayed precision** (one sentence, starting with "Furthermore"). Tie the number of decimal places shown to the resolution of the limiting instrument and one human/process source. *Constraint:* include both a machine and a human/process source of uncertainty.
6. **Clarify the working precision** (one short sentence). State that the rounding applied to the table was *not* carried into calculations. *Constraint:* this sentence must contrast with the previous one, otherwise it has no job.
7. **Hand off** to the next section by category shift (here: from quantitative table to qualitative observation heading).

The pattern's logic: **display the evidence → disclose its warts → defend how it was displayed → confirm the maths was rigorous.** Any student can apply it by, first, listing the dependent variable, the independent variable, and the dominant uncertainties before drafting — the sentences then assemble themselves in this order.
