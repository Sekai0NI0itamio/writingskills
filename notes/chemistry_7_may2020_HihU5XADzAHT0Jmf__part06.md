# Idea Flow Notes: chemistry_7_may2020_HihU5XADzAHT0Jmf — Volume required to reach endpoint                              Inverse

## Paragraph Flow (move by move)

**Paragraph 1** (Table 2 introduction + legend)
- S1: "Table 2 shows data for the first" — **claim/pointer**. Hands off by immediately specifying the experimental condition the table belongs to.
- S2: "The data in red represents processed" — **definition/legend**. Hands off by closing the legend, priming the reader to scan the table.

**Paragraph 2** (Time uncertainty rationale)
- S1: "The time uncertainty was recorded as" — **claim**. Hands off by inviting the *why* of that number.
- S2: "since time was needed while transferring" — **cause**. Hands off by giving a process step that demands a time-window specification.
- S3: "This required approximately 30 seconds" — **specification**. Hands off by giving a total duration that must be split.
- S4: "therefore the sample was withdrawn 15" — **unpack/mechanism**. Hands off by stating one half of the split.
- S5: "and finishing 15 seconds after, hence" — **completion/verdict**. Hands off by closing the mechanism, shifting to a new variable next.

**Paragraph 3** (Volume uncertainty derivation)
- S1: "Although the uncertainty of the burette" — **concession**. Hands off by setting up a contradiction demanding a *cause*.
- S2: "the uncertainty in the volume column" — **claim**. Hands off by flagging the header needs derivation.
- S3: "because the volume was calculated as" — **cause**. Hands off by exposing the formula requiring worked algebra.
- S4: "It therefore follows that: ∆VNaOH" — **implication/worked line**. Hands off by completing algebra; next shifts to demonstration.

**Paragraph 4** (Transition to worked calculations)
- S1: "Calculation examples are demonstrated below" — **transition/promise**. Hands off by announcing an exemplar using a specific row.

**Paragraph 5** (Neglected-uncertainty disclosure + rounding + opening concession)
- S1: "Note that in calculating ∆(1/c), the uncertainties" — **concession/qualifier**. Hands off by demanding a *cause* for the omission.
- S2: "as the solutions were prepared by the technician" — **cause/authority**. Hands off by giving the trust justification, parallel to next sentence's justification.
- S3: "The values of the mean volume were formatted" — **implication**. Hands off by stating a rounding choice needing a reason.
- S4: "as the precision of the burette allowed" — **cause**. Hands off by closing the rounding argument; trailing clause sets up an unshown concession.

## What This Section Does (content sequence)

A "data table + uncertainty justification + worked example + rounding convention" section moves in this fixed order:

1. **Anchor the table to the experimental condition** — name which run / which temperature. Sets up everything downstream as belonging to *one slice*.
2. **Decode the table visually** — explain colour-coding (raw vs. processed). Sets up justification of the numbers that follows.
3. **Justify each uncertainty header variable-by-variable** — for every ± value, explain where it came from in procedural order. Each justification must show the *cause*.
4. **Provide a worked example using the first row** — demonstrate the formula on concrete numbers.
5. **Declare neglected uncertainties and rounding conventions** — justify what was left out (and why) and how values were rounded (and why). Closes all methodological threads.

Order works because the reader must (a) locate, (b) read, (c) trust the table, (d) see the math once, (e) understand all editorial choices before any graph/plot that follows.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Header uncertainty justification"**
SKELETON: "The [variable] uncertainty was recorded as ±[value] [unit], since [procedural reason]. This required [quantity], therefore [action 1] and [action 2], hence the uncertainty."

- **Slot 1** (recorded uncertainty): noun phrase naming variable + numeric uncertainty + unit.
- **Slot 2** (procedural cause): because-clause naming the interrupting step.
- **Slot 3** (operational split): two parallel actions symmetrically around the nominal reading.

*Original*: "The time uncertainty was recorded as ±0.25 minutes (±15 seconds), since time was needed while transferring the mixture from the test tube to the pipette. This required approximately 30 seconds, therefore the sample was withdrawn 15 seconds before the time of the interval, and finishing 15 seconds after, hence the uncertainty."

*Demonstration fill (thermometer lag)*: "The temperature uncertainty was recorded as ±0.4 °C, since the digital probe required equilibration after immersion. This took roughly 20 seconds, therefore the reading was taken 10 seconds before the nominal time and confirmed 10 seconds after, hence the uncertainty."

---

**SKELETON B — "Concessive derivation of a derived uncertainty"**
SKELETON: "Although [base instrument uncertainty], the [derived quantity] is recorded as ±[doubled value] because [derived quantity] was calculated as [formula]. It therefore follows that: ∆[derived] = [expression] = [sum]."

- **Slot 1** (concession): "Although X has uncertainty Y…"
- **Slot 2** (recorded-header claim): state the larger recorded value.
- **Slot 3** (cause as formula): "because [quantity] was calculated as [sum/difference of two readings]."
- **Slot 4** (worked derivation): "It therefore follows that ∆ = ∆A + ∆B = Y + Y = 2Y."

*Original*: "Although the uncertainty of the burette is ±0.05, the uncertainty in the volume column header is recorded as ±0.10 because the volume was calculated as VNaOH = Vfinal − Vinitial. It therefore follows that: ∆VNaOH = ∆Vfinal + ∆Vinitial = 0.05 + 0.05 = 0.10."

*Demonstration fill (resistance)*: "Although the voltmeter has a quoted uncertainty of ±0.02 V, the resistance column is recorded as ±0.04 Ω because R was calculated as V_supply − V_resistor. It therefore follows that: ∆V = ∆V_supply + ∆V_resistor = 0.02 + 0.02 = 0.04."

---

**SKELETON C — "Neglected-uncertainty disclaimer with authority"**
SKELETON: "Note that in calculating ∆([derived quantity]), the uncertainties of [input 1] and [input 2] were not accounted for as [authority figure] prepared [input] and as such, it had to be assumed that these uncertainties were negligible."

- **Slot 1** (flag omission): name the calculation, admit two inputs skipped.
- **Slot 2** (authority justification): name *who* prepared the inputs.
- **Slot 3** (assumption declaration): explicitly declare negligence is justified.

*Original*: "Note that in calculating ∆(1/c), the uncertainties of cNaOH and cHCl were not accounted for as the solutions were prepared by the technician and as such, it had to be assumed that these uncertainties were negligible."

*Demonstration fill (pH from buffer tablets)*: "Note that in calculating ∆pH, the uncertainties of the buffer concentration and the indicator concentration were not accounted for as the solutions were prepared by the lab technician and as such, it had to be assumed that these uncertainties were negligible."

---

**SKELETON D — "Rounding justification by instrument precision"**
SKELETON: "The values of the [quantity] were formatted to [N] significant figures as the precision of the [instrument] allowed for such."

- **Slot 1** (rounding claim): state sig-fig count.
- **Slot 2** (precision justification): name limiting instrument.

*Original*: "The values of the mean volume were formatted to three significant figures as the precision of the burette allowed for such."

*Demonstration fill (length with vernier)*: "The values of the mean length were formatted to two decimal places as the precision of the vernier caliper allowed for such."

## Express-Idea Vocabulary

**Sequencing / transition**
- "Calculation examples are demonstrated below" — shifts from justification to exemplar.
- "The data in red represents processed data while the rest is raw" — pairs parallel categories to define a legend.

**Cause / consequence**
- "since time was needed while transferring the mixture" — procedural cause.
- "therefore the sample was withdrawn 15 seconds before" — consequence of duration estimate.
- "It therefore follows that:" — derives algebraic consequence.
- "as the precision of the burette allowed for such" — justifies rounding.

**Contrast / concession**
- "Although the uncertainty of the burette is ±0.05" — header appears larger than instrument spec.
- "While it would have" — opens an alternative not taken.

**Specification / definition**
- "the volume was calculated as VNaOH = Vfinal − Vinitial" — defines a quantity via formula.
- "represents processed data" — defines the colour code.

**Evidence handling**
- "using values from the first row of the table" — pins the worked example.
- "Table 2 shows data for the first condition" — anchors evidence to source.

**Explanation verbs**
- "was recorded as" — declares a measurement.
- "was calculated as" — introduces a formula.
- "it therefore follows that" — derives a consequence.
- "had to be assumed that these uncertainties were negligible" — declares an assumption.
- "allowed for such" — justifies a formatting choice.

## How to Explain an Idea (replication steps)

This section uses the **"justified-header + worked exemplar + assumption disclosure"** pattern. To explain a *new* idea the same way:

1. **Anchor the data block to a single experimental condition.** Open with "[Table/Figure X] shows data for the first condition ([variable] = [value])."
2. **Decode any visual convention.** Explain colour-coding, bolding, or symbols so the reader reads the table correctly.
3. **Justify each ± header one variable at a time, in the order the experiment produced them.** For each: (a) state the recorded ±, (b) explain the procedural cause, (c) if from adding two instrument uncertainties, write the formula and worked sum.
4. **State a worked example using one row.** Announce the transition ("Calculation examples are demonstrated below using values from the first row"), then run mean → mean uncertainty → derived quantity → derived uncertainty in that order with each step's arithmetic.
5. **Disclose neglected uncertainties with an authority justification.** Open with "Note that…", name which inputs were ignored, name who prepared them, state the assumption.
6. **Justify the rounding convention.** Link the chosen sig-fig count to the precision of the limiting instrument.
7. **Close with a concession about what *would have* been possible but was not chosen.** Previews editorial restraint and primes the next section.

Mechanism: reader sees numbers → is told where each came from → sees one calculation in full → is told what was left out and why → is told how values were trimmed and why. Order is non-negotiable: trust precedes arithmetic precedes admission precedes editing.
