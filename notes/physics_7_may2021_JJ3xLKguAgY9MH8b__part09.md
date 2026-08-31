# Idea Flow Notes: physics_7_may2021_JJ3xLKguAgY9MH8b — 5.2    Conclusion

## Paragraph Flow (move by move)

**Paragraph 1**
1. **Claim** — "The data points follow some of the same characteristics as the model-line." — Sets the macro-judgment that data ≈ model. This hands the reader into S2 because the vague "some of the same characteristics" demands a concrete instance of which characteristic.
2. **Evidence (general trend)** — "The range in the data points is constantly decreasing" — Specifies *one* shared characteristic (monotonic decrease). Hands to S3 because a general trend without its extremum is incomplete; the reader now expects where the trend bites hardest.
3. **Evidence (extrema) + Comparison** — "The rate of range decrease is largest at the extreme incline angle values α = 0 and α = 65" — Pinpoints the maxima of the rate of decrease. Then closes with comparison: "just like the model does" — parallelises experimental behaviour with theoretical behaviour. This comparison closes the agreement case, which hands the reader into P2 by inviting the counter-question: *where does agreement break?*

**Paragraph 2**
1. **Concession** — "However, the data points do deviate from the model significantly at times." — Pivot move; reverses P1's verdict. Hands to S2 because "at times" is vague and the reader needs a count.
2. **Evidence (quantified)** — "In fact most of the points (11/14) don't touch the line with the error bars." — Provides the proportion the concession implied, sharpening the claim. Hands to S3 because the reader now needs to know *which direction* the deviation goes.
3. **Specification (lower sub-range)** — "The points less than 35 are lower than the model and the deviation seems to increase as the angle approaches 0." — One direction of the deviation, with growth toward an extremum. Hands to S4 because the symmetric case (other half of the data) hasn't been addressed.
4. **Specification (upper sub-range)** — "The data points more than 35 are higher than the model and the deviation seems to increase as the angle approaches 65." — Mirror image of S3; completes the split-specification. Hands to S5 because having described deviation qualitatively, the reader expects a quantitative handle.
5. **Method transition** — "The percentage difference between the data points and the model can be calculated with:" — Shifts from descriptive to numerical. Hands the reader to the formula block and the table.

**Paragraph 3**
1. **Evidence-driven verdict** — "From Table 4 it's clear that the difference gets exceptionally large when the incline angle gets closer to the launch angle." — Reads the table's headline. Hands to S2 because the reader notices the blank α = 65 cell and expects an explanation.
2. **Anomaly explanation** — "There isn't value for α = 65 because the theoretical range is 0 m so there would be division by zero in Equation 1." — Cause-and-effect justification for the missing datum. Hands to S3 because once the anomaly is resolved, the section is ready for its final wrap-up sentence.
3. **Final verdict (abrupt)** — "The model makes physical sense" — Closing judgment that re-anchors the section's overall takeaway.

## What This Section Does (content sequence)

The ordered logic moves are:

1. **Agreement claim first** — establishes a baseline verdict ("the data mostly match the model"). This sets the bar that everything later will qualify or contradict.
2. **Trend evidence for agreement** — substantiates the claim with a single clean monotonic behaviour so the verdict doesn't rest on rhetoric.
3. **Extrema evidence + parallel comparison** — covers the boundary behaviour, then echoes the model so the reader sees the parallel explicitly before the pivot.
4. **Concession / "however" pivot** — the natural next question after agreement is "where does it fail?"; this move opens the deviation case.
5. **Quantified deviation** — turns the concession into a measurable proportion (11/14) so it cannot be dismissed as anecdotal.
6. **Split specification of deviation** — separates the residual into two directional halves (below-launch-angle vs above-launch-angle), each with its own growth rule. The split makes the deviation a structured finding rather than a mess.
7. **Method transition to a metric** — introduces a percentage-difference formula because the deviation now needs a numerical table to be fully communicated.
8. **Table-led verdict** — uses the computed metric to issue a fresh claim about *where* the deviation explodes.
9. **Anomaly explanation** — addresses the conspicuous gap in the table (division by zero / edge case).
10. **One-line closing judgment** — re-asserts the model's validity in a single punchy sentence, leaving the reader with a verdict.

The principle of the order: *establish what works → concede what doesn't → quantify what doesn't → explain the worst case → close on the model's legitimacy.* Each move sets up the question the next move answers.

## Paragraph Skeletons (replicable templates)

**Skeleton A — Agreement-then-evidence paragraph**
> "[General agreement claim between data and model]. [A general trend statement in which the data decreases/increases as a variable changes]. [An extremum observation about where the trend is steepest, followed by a parallel comparison to the model]."

1. *Slots:* (i) Claim — noun phrase + verb of agreement ("data follow some of the same characteristics as the model-line"). (ii) Trend — subject + present-participle decrease/increase + as-clause. (iii) Extremum + comparison — superlative + numerical endpoints + "just like the model does."
2. *How to fill with a different idea:* (i) Pick a phenomenon where experiment and theory should agree (e.g. SHM, exponential decay, Ohm's law) and state the agreement. (ii) Name one monotonic relationship that the data show. (iii) Identify the endpoints of the independent variable and assert the model matches at those ends.
3. *Original fill:* "The data points follow some of the same characteristics as the model-line. The range in the data points is constantly decreasing as the incline angle increases. The rate of range decrease is largest at the extreme incline angle values α = 0 and α = 65 ... just like the model does."
4. *Demonstration fill:* "The measured periods follow the same characteristics as the simple-pendulum model. The period in the data is constantly increasing as the string length increases. The rate of period increase is steepest at the longest string lengths L = 1.0 m and L = 1.2 m, just like the model does."

**Skeleton B — Concession-then-split-specification paragraph**
> "[Concession that data deviate from the model]. [Quantified claim with a ratio or proportion]. [Below-a-threshold specification: data lower than model, deviation growing toward one extreme]. [Above-the-threshold specification: data higher than model, deviation growing toward the other extreme]. [Method-transition sentence introducing the formula that quantifies the deviation]."

1. *Slots:* (i) Concession — "However, the data do deviate..." (ii) Ratio — "In fact most of the points (X/Y)..." (iii) Lower-half — "The points less than [threshold] are lower than the model..." (iv) Upper-half — "The points more than [threshold] are higher than the model..." (v) Method pivot — "The percentage difference ... can be calculated with:".
2. *How to fill:* (i) Open with "However" and name the failure mode. (ii) Count how many points fall outside error bars; express as X/N. (iii) Pick a natural midpoint threshold; describe the lower half's sign and growth direction. (iv) Mirror the lower half for the upper half. (v) Introduce the percentage-error formula.
3. *Original fill:* "However, the data points do deviate from the model significantly at times. In fact most of the points (11/14) don't touch the line with the error bars. The points less than 35 are lower than the model ... The data points more than 35 are higher than the model ... The percentage difference between the data points and the model can be calculated with:".
4. *Demonstration fill:* "However, the measured resistances do deviate from the theoretical values at times. In fact most of the points (8/10) don't fall inside the resistor-tolerance band. The points below 100 Ω are lower than the rated value, and the deviation grows toward the smallest resistance. The points above 100 Ω are higher than the rated value, and the deviation grows toward the largest resistance. The percentage difference between the measured and rated resistance can be calculated with:"

**Skeleton C — Table-verdict paragraph**
> "[Evidence claim that reads the table directly]. [Explanation of a conspicuous missing cell, citing a mathematical or physical edge case]. [Final one-line verdict on the model's physical plausibility]."

1. *Slots:* (i) Table-verdict — "From Table N it's clear that..." (ii) Anomaly cause — "There isn't value for X because Y so there would be ..." (iii) Punchy closing — "The model makes physical sense" / equivalent.
2. *How to fill:* (i) Open with "From Table N" and identify the dependent-variable region where the deviation is worst. (ii) Point at the blank/zero cell; explain the division-by-zero, singularity, or boundary case. (iii) End with a single declarative sentence that re-affirms the model.
3. *Original fill:* "From Table 4 it's clear that the difference gets exceptionally large when the incline angle gets closer to the launch angle. There isn't value for α = 65 because the theoretical range is 0 m so there would be division by zero in Equation 1. The model makes physical sense".
4. *Demonstration fill:* "From Table 7 it's clear that the discrepancy gets exceptionally large when the driving frequency approaches the natural frequency. There isn't a value for f = 50 Hz because the theoretical amplitude is unbounded so there would be division by zero in Equation 2. The resonance model makes physical sense."

## Express-Idea Vocabulary

- **Sequencing / evidence-locating:** "From Table 4 it's clear that" (P3 S1) — frames the next clause as a table-reading. "In fact most of the points" (P2 S2) — upgrades a vague claim with a hard statistic.
- **Cause / consequence:** "There isn't value for α = 65 because the theoretical range is 0 m so there would be division by zero" (P3 S2) — nested cause chain (mathematical cause → computational consequence).
- **Contrast / concession:** "However, the data points do deviate" (P2 S1) — concession marker that reverses P1. "just like the model does" (P1 S3) — comparison closure for agreement.
- **Specification / split:** "The points less than 35 are lower than the model" (P2 S3) and "The data points more than 35 are higher than the model" (P2 S4) — paired directional specifications built around a midpoint threshold.
- **Evidence handling:** "follow some of the same characteristics as the model-line" (P1 S1) — claim-phrase that signals evidence agreement. "In fact most of the points (11/14)" (P2 S2) — quantifier-as-evidence.
- **Explanation / definition verbs:** "can be calculated with:" (P2 S5) — introduces a formula as a definition of the metric. "makes physical sense" (P3 S3) — closing explanatory judgment.

## How to Explain an Idea (replication steps)

The section relies on the pattern **agreement → quantified concession → split specification → table-verdict → anomaly → one-line judgment**. To reproduce it for a new idea:

1. **Open with a one-sentence agreement claim** between your data and your theoretical model. Use a verb of agreement ("follow", "match", "agree with", "reproduce").
2. **State a single monotonic trend** the data share with the model (one independent variable, one dependent variable, one direction).
3. **Identify the extrema** of the independent variable, name where the trend is steepest, and close the sentence with a comparison ("just like the model does") so the reader sees the parallel explicitly.
4. **Pivot with "However"** and concede that agreement is partial — name the failure mode.
5. **Quantify the failure** with a ratio (X/N points outside tolerance, error bars, etc.) so the concession cannot be dismissed as anecdotal.
6. **Split the deviation** into two halves around a natural threshold (a midpoint, a critical value, a launch condition). Describe each half's sign and growth direction in a separate sentence; mirror the phrasing.
7. **Introduce a quantitative metric** in a sentence beginning "The [percentage / absolute / relative] difference ... can be calculated with:" and place the formula directly beneath.
8. **Present a table** of the metric against the independent variable.
9. **Read the table aloud** with "From Table N it's clear that..." and identify the region where the metric explodes.
10. **Explain any conspicuous blank cell** in the table using a nested cause (mathematical singularity → computational consequence, or physical boundary → undefined measurement).
11. **Close on a single declarative verdict** that re-asserts the model's legitimacy ("The model makes physical sense", "The model captures the dominant behaviour", etc.).
