# Idea Flow Notes: mathematics_7_may2019_uwHSxRQY5IvK0u4D — function show an exponential growth rather than

## Paragraph Flow (move by move)

**Paragraph 1** (initial attempt display)
  1. *Context / carry-over*: "...function show an exponential growth rather than, exponential decay." — quotes "exponential growth rather than, exponential decay". Hands to next by *specifying the numerical form* of that observation (claim needs evidence).
  2. *Evidence display*: "The equation exported was following:" + figure. Quotes "The equation exported was following". Hands to next by *closing the model output* with the need for a judging metric (you cannot evaluate an equation without stating how it will be evaluated).

**Paragraph 2** (introducing and defining the metric)
  1. *Method statement*: "The accuracy of this model was measured using the R-squared (R2) value." Quotes "was measured using the R-squared". Hands to next by *signalling the reader needs to know what the abbreviation means* (acronym triggers definition).
  2. *Definition*: "R is a statistical measure of how well the trend is being represented in a model, from scale of 0 to 1..." Quotes "statistical measure of how well". Hands to next by *finishing the definition at the high end* ("1 being a perfect model"), which lets the reader interpret a numerical result that is about to appear.

**Paragraph 3** (first numerical result + anomaly explanation)
  1. *Evidence*: "R² for Figure 9 was 0.786." Quotes "R2 for Figure 9 was 0.786". Hands to next by *raising a contradiction*: 0.786 looks "high" given the visible mismatch, so the next sentence must reconcile it.
  2. *Mechanism / cause for anomaly*: "The high R² value despite the discrepancy between real data perhaps arises from..." Quotes "despite the discrepancy between real data perhaps arises". Hands to next by *narrowing the global claim to a specific region* where the failure is worst.
  3. *Specification / verdict*: "The R² for the plots located in between 8.5 < # < 9.5 in particular was 0.396..." Quotes "in between 8.5 < # < 9.5 in particular". Closes the paragraph by *resolving the anomaly into a verdict* ("inaccurate"), which is the launch pad for the "2nd attempt".

**Paragraph 4** ("2nd attempt" — diagnosis + first fix)
  1. *Diagnosis / cause hypothesis*: "I assumed that this error could be because the shape Figure 5 had was mirrored..." Quotes "could be because the shape Figure 5". Hands to next by *naming the cause* — once the cause is named, the logical next move is the operation that removes it.
  2. *Consequence / corrective action*: "Therefore, I performed a horizontal reflection for all the datasets extracted..." Quotes "Therefore, I performed a horizontal reflection". Hands to next by *introducing a new sub-problem created by the fix* ("invaded quadrant 4"), which demands a second correction.

**Paragraph 5** (additional fix with justification)
  1. *Additional corrective action + reason*: "Additionally, the whole data set was moved to quadrant 1, as few of the plots after reflected invaded quadrant 4." Quotes "as few of the plots after reflected invaded". Hands to next by *opening a new sub-task*: the move still requires a *numerical translation value*, which must be justified.

**Paragraph 6** (translation + reasoning + final state)
  1. *Action display*: "Following translation was applied:" + equation. Quotes "Following translation was applied". Hands to next by *prompting justification of the constant* chosen.
  2. *Justification of magnitude*: "-9.322… was the smallest value amongst the data plots, and translation had to be greater than this..." Quotes "translation had to be greater than this". Hands to next by *closing on the resulting state of the anchor point*.
  3. *Result / new state*: "This point now lies at # = 0." Quotes "This point now lies at". Closes by *anchoring the reader* at the new coordinate origin.

## What This Section Does (content sequence)

1. **Display the raw model output first** (equation from the software) — because until the reader sees the equation, no judgment of it is possible.
2. **State the evaluative metric** (R²) — this is the bridge that converts "a number" into "a verdict".
3. **Define the metric in full** (what it is, its 0–1 scale, what the extremes mean) — required so the figure that follows is interpretable without outside lookup.
4. **Report the global metric value** — gives the headline figure.
5. **Flag the contradiction** (high R² but visible mismatch) and *explain* it — the explanation prevents the reader from thinking the writer is ignoring the visual error.
6. **Narrow to a worst-case subset and give its value** — converts a soft observation into a hard verdict ("inaccurate") that justifies a retry.
7. **Open the retry with a labelled attempt marker** ("2nd attempt") — frames the next move as an improvement, not a new topic.
8. **Diagnose the error as a geometric mismatch** (mirrored shape vs. reference shape) — gives the *cause* that the next action will remove.
9. **Apply the corrective transformation** (reflection) and state its purpose — cause → effect in one breath.
10. **Justify a second adjustment** that the first created (move to quadrant 1) — iterative refinement: every fix generates a new constraint.
12. **Apply a numerical translation**, justify *why that magnitude* (smallest data value drives the constant), then *state the resulting anchor point* — closes the iteration with a verifiable outcome.

The reason for this order: each move sets up the *metric of success* or the *constraint* for the next. Without the definition you cannot read the numbers; without the anomaly you cannot justify a second attempt; without the diagnosis the reflection is arbitrary; without the magnitude justification the translation looks pulled from nowhere.

## Paragraph Skeletons (replicable templates)

**SKELETON A — metric introduction + definition**
> "[This model/output]'s accuracy was measured using the [METRIC]. [METRIC] is a [category] measure of [what it measures], from scale of 0 to 1, where 0 being the [low extreme] and 1 being the [high extreme]."

1. *Slot roles & shapes*: Slot 1 = method-stating past passive ("was measured using"). Slot 2 = category noun ("statistical measure"). Slot 3 = purpose gerund ("how well the trend is being represented"). Slot 4 = low-end evaluation noun ("least accurate"). Slot 5 = high-end evaluation noun ("perfect model").
2. *How to fill with a different idea*: Pick any iterative numerical model. Replace METRIC with the standard goodness-of-fit statistic (RMSE, χ², R²). State its purpose in one noun + relative clause. Use the 0–1 scale phrasing only if the metric is bounded; otherwise rephrase as "from [low] to [high]".
3. *Original fill*: "The accuracy of this model was measured using the R-squared (R2) value. R is a statistical measure of how well the trend is being represented in a model, from scale of 0 to 1, where 0 being the least accurate and 1 being a perfect model."
4. *Demo fill (different idea)*: "The fit of the damped oscillator was measured using the chi-squared (χ²) value. χ² is a statistical measure of how far the predicted curve deviates from the observed points, from a scale of 0 upwards, where 0 being the curve passes through every point and large values being a poor fit."

**SKELETON B — global value + anomaly explanation + subset verdict**
> "[METRIC] for [Figure/Label] was [value]. The [adjective] [METRIC] despite the [discrepancy] perhaps arises from [cause]. The [METRIC] for the [subset] in particular was [value], further indicating that the [model] [verdict]."

1. *Slot roles & shapes*: Slot 1 = labelled numerical claim (figure + value). Slot 2 = evaluative adjective ("high/low"). Slot 3 = observed contradiction noun ("discrepancy between real data"). Slot 4 = cause clause ("data plots that are plotted horizontally"). Slot 5 = narrowed range expressed as inequality. Slot 6 = weak value to contrast the strong one. Slot 7 = verdict adjective ("inaccurate").
2. *How to fill with a different idea*: Run the model; read off the headline metric; if it looks healthy but the picture looks bad, propose a *reason why the metric is fooled* (e.g. clustered points, leverage outliers). Find a subset where the metric collapses. Report both with "in particular" as the pivot.
3. *Original fill*: "R² for Figure 9 was 0.786. The high R² value despite the discrepancy between real data perhaps arises from the data plots that are plotted horizontally. The R² for the plots located in between 8.5 < x < 9.5 in particular was 0.396, further indicating that the model generated here is inaccurate."
4. *Demo fill*: "χ² for Run 3 was 0.42. The low χ² despite the visible drift perhaps arises from the dense cluster of points near the turning point. The χ² for the readings between t = 8s and t = 10s in particular was 3.14, further indicating that the model generated here is inaccurate."

**SKELETON C — labelled retry + cause diagnosis + corrective action**
> "[Attempt label]. I assumed that this [problem] could be because the [observed shape] was [mismatch] compared to [reference shape]. Therefore, I performed a [operation] for all the [datasets], and thus would [expected outcome]."

1. *Slot roles & shapes*: Slot 1 = labelled attempt ("2nd attempt"). Slot 2 = first-person epistemic claim ("I assumed that…"). Slot 3 = geometric / structural property ("mirrored"). Slot 4 = reference baseline ("normal shape of logistic function"). Slot 5 = named transformation ("horizontal reflection"). Slot 6 = plural object ("datasets extracted"). Slot 7 = purpose clause ("match the shape seen in…").
2. *How to fill with a different idea*: Identify a visual / geometric defect in the model's output. Name it as a *mismatch against a textbook reference*. Pick the single elementary transformation that removes the mismatch. Use "Therefore" to bind the diagnosis to the operation in one breath.
3. *Original fill*: "2nd attempt. I assumed that this error could be because the shape Figure 5 had was mirrored compared to normal shape of logistic function (Figure 4). Therefore, I performed a horizontal reflection for all the datasets extracted, and thus would match the shape seen in logistic function."
4. *Demo fill*: "3rd iteration. I assumed that this drift could be because the curve I generated was offset vertically compared to the equilibrium line of the standard SIR model. Therefore, I performed a vertical translation for all the series extracted, and thus would align with the steady-state baseline seen in the SIR model."

**SKELETON D — second-order fix + magnitude justification + new anchor**
> "Additionally, the [object] was [operation], as [reason]. Following [operation] was applied: [formula]. [constant] was the [extremum] amongst the [reference set], and [operation] had to be [constraint]. This point now lies at [new coordinate]."

1. *Slot roles & shapes*: Slot 1 = "Additionally" + past passive. Slot 2 = consequence clause introduced by "as". Slot 3 = "Following [operation]" lead-in. Slot 4 = numerical constant. Slot 5 = extremum claim ("smallest value"). Slot 6 = mathematical inequality. Slot 7 = final position statement.
2. *How to fill with a different idea*: After your first fix, identify the *new visible defect* (e.g. negative values where there shouldn't be). Describe the corrective move with "Additionally…as". For any constant chosen, anchor it to an extremum of the dataset and state the inequality that extremum forces. Close by stating the anchor's new coordinate.
3. *Original fill*: "Additionally, the whole data set was moved to quadrant 1, as few of the plots after reflected invaded quadrant 4. Following translation was applied: [-9.322…]. -9.322… was the smallest value amongst the data plots, and translation had to be greater than this to make everything in quadrant 1. This point now lies at x = 0."
4. *Demo fill*: "Additionally, the residual curve was shifted upward by 4 units, as several residuals after subtracting still sat below the x-axis. Following vertical translation was applied: +4.00. -3.84 was the most negative residual amongst the sample, and translation had to exceed this to push every point into the upper half-plane. This minimum now lies at y = 0.16."

## Express-Idea Vocabulary

- **Sequencing / step-marker**: "Following translation was applied" — opens the third action in a chain.
- **Cause / consequence**: "Therefore, I performed a horizontal reflection" — diagnosis → action in one breath. "perhaps arises from the data plots that are plotted horizontally" — *hedged* cause attribution. "as few of the plots after reflected invaded quadrant 4" — cause embedded as subordinate "as"-clause.
- **Contrast / concession**: "The high R² value despite the discrepancy between real data" — pairs an apparently good number with the visible bad picture.
- **Specification / narrowing**: "in particular was 0.396" — collapses the global claim onto one subset.
- **Evidence handling**: "R² for Figure 9 was 0.786" — labelled datum. "from scale of 0 to 1" — calibrated frame for the datum.
- **Explanation verbs / epistemic frames**: "was measured using the R-squared" — introduces metric. "is a statistical measure of how well" — definitional copula. "I assumed that this error could be because" — first-person epistemic claim naming a hypothesis. "further indicating that the model generated here is inaccurate" — verdict via "further indicating".

## How to Explain an Idea (replication steps)

**Pattern name**: *iterative numerical refinement — method→metric→global result→anomaly→worst-case subset→diagnosis→transformation→secondary fix→magnitude justification→new anchor.*

Numbered steps to reproduce this pattern on a NEW idea:

1. **Display the first-pass output** as the numerical object of evaluation (an exported equation, a fitted curve, a calibrated constant).
2. **Name the metric** you will use to judge it ("was measured using the [metric]"). Choose the verb *measured*, not "evaluated" — keeps the metric feeling like an instrument.
3. **Define the metric inline** in one sentence: category + what it measures + scale + extremes. Do not assume the reader knows the acronym.
4. **Report the headline metric value** tied to a labelled figure/figure-number.
5. **Concede the apparent contradiction** between the metric and the visible picture ("The high [metric] despite the discrepancy between real data…").
6. **Hedge a cause** for why the contradiction exists ("perhaps arises from…") — the *perhaps* is non-negotiable, because you are inferring a cause from one plot.
7. **Narrow to a subset** that exposes the failure ("The [metric] for the plots located in between [a] < x < [b] in particular was [weak value]"), and use this subset to issue the **verdict** ("further indicating that the model…is inaccurate").
8. **Open a labelled retry** ("2nd attempt", "Iteration 2", "Revised model") — the label alone signals the logic is *not* abandoning the topic but refining it.
9. **State the diagnosis as a geometric / structural mismatch** against a named reference form ("the shape…was mirrored compared to the normal shape of [reference]").
10. **Apply the corrective elementary transformation** in the same sentence as the diagnosis, using **"Therefore"** as the hinge verb.
11. **Surface a new defect that the first fix created** ("Additionally… as few of the plots… invaded…"). This proves the iteration is *real* and not cosmetic.
12. **Apply a second numerical transformation**, then **justify the constant** by anchoring it to the *extremum of the dataset* and stating the inequality that extremum forces.
13. **Close on the anchor's new coordinate** ("This point now lies at x = 0") — gives the reader one sentence they can verify by eye.
