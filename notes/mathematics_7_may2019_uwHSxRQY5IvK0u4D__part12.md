# Idea Flow Notes: mathematics_7_may2019_uwHSxRQY5IvK0u4D — Although visually the model looks accurate, it remains unclear whether if it is faithful to the initial graphical

## Paragraph Flow (move by move)

**Paragraph 1 (4 sentences — method setup)**
- S1. **Carry-forward context** — "(continuation of the previous paragraph describing the) model created (Figure 3)." Hands to S2 by *anchoring the artifact* that the next sentence will operate on.
- S2. **Method claim (authority by precedent)** — "I would be able to find this through applying the method". Hands to S3 by *naming the tool that will perform the method*.
- S3. **Tool application** — "Using WebPlotDigitier, I extracted points". Hands to S4 by *handing over the extracted artefact to a comparison step*.
- S4. **Comparison mechanism + metric** — "compared the extracted dataset with the plots … using R2 value". Hands to the table by *announcing the metric whose numbers will follow*.
- S5. **Result signpost** — "The result is following:" — pure transition; hands to Paragraph 2 by *deferring the answer*.

**Paragraph 2 (1 sentence — evidence block)**
- The table itself is the **evidence dump**: four R² readings + an average column. It hands forward by *supplying the numbers Paragraph 3 will interpret*.

**Paragraph 3 (5 sentences — interpretation)**
- S1. **Verdict (dual confirmation)** — "As much as it looked accurate, the R2 value also show that it is also faithful". Hands to S2 by *stacking visual + numerical agreement* so a counter-point can be raised.
- S2. **Contrast pivot → limitation** — "However, as seen in the actual 3D figure in Figure 17, although Doraemon does resemble circular shape, it is never a transformed circle". Hands to S3 by *introducing an admitted flaw that needs re-framing*.
- S3. **Reframe as strength (concession→revaluation)** — "While this is a source of error, it can also be seen as a strength". Hands to S4 by *adding another independent supportive argument*.
- S4. **Additional evidence-based claim (reliability)** — "high R2 value also proves that the steps I took are reliable". Hands to S5 by *generalising the result into a future-oriented claim*.
- S5. **Implication for the future** — "which comes in significant in future purposes." Closes the paragraph.

## What This Section Does (content sequence)
This is an **evaluation/verification section**. The ordered moves are:
1. **Recall the artifact just produced** (so the reader knows what is being checked).
2. **Name the verification procedure + the tool used** (legitimises the check by invoking a method that worked earlier).
3. **State the metric** that will quantify faithfulness (R²).
4. **Present the numeric evidence** in a compact table with a summary statistic (average).
5. **Issue a dual-mode verdict** (visual + numerical agree).
6. **Admit a limitation** with a "however" pivot grounded in a concrete figure.
7. **Reframe the limitation as a strength** (concession → revaluation).
8. **Add a second independent argument** (reliability of the procedure itself).
9. **Project forward** to future use.

The order matters because: you cannot judge numbers before you run the procedure (1→4); you cannot honestly claim success without admitting a visible flaw (5→6); and a single claim of success needs an independent supporting argument plus a future-use justification before the section can close (7→9).

## Paragraph Skeletons (replicable templates)

**SKELETON A — Method recap + verification set-up**
   "[Recap of artefact just produced, e.g. 'the model created (Figure 3)']. I would be able to find this through applying the method [reference to earlier work, e.g. 'I discovered while I investigated …']. Using [TOOL], I extracted [input] and then compared [extracted data] with [what the formula gives], using [METRIC]. The result is following:"

- **Slot 1 (carry-forward noun phrase):** the model/output from the prior paragraph + figure number in parentheses; parenthetical.
- **Slot 2 (method-by-precedent clause):** "I would be able to find this through applying the method I discovered while I investigated X"; first-person, past-tense reference to a previous sub-task.
- **Slot 3 (tool action):** "Using [software], I extracted [data type] from the [source]"; fronted gerund with software name + past-tense verb.
- **Slot 4 (comparison + metric):** "and then compared … using [metric]"; coordinated verb + metric noun.
- **Slot 5 (signpost):** "The result is following:" — short declarative that defers to a table/figure.

*Filled (original):* "model created (Figure 3). I would be able to find this through applying the method I discovered while I investigated 'Body' and 'Feet' section. Using WebPlotDigitier, I extracted points from the graphical model and then compared the extracted dataset with the plots the equation will give, using R2 value. The result is following:"

*Demo fill (different topic — logistic growth fit):* "trend line plotted (Figure 4). I would be able to check this through applying the procedure I trialled on the yeast dataset. Using Tracker, I extracted coordinates from the scatter plot and then compared the extracted series with the values the logistic equation predicts, using χ² test. The result is following:"

---

**SKELETON B — Evidence table + dual-mode verdict**
   "[Numeric table with one metric per row and a summary column]. As much as it looked [visual impression], the [metric] also show that it is also faithful to the [source]."

- **Slot 1:** tidy table; first column = categories, second column = values, optional third column = aggregate.
- **Slot 2 (verdict):** "As much as it looked [adjective], the [metric] also show[s] that it is also [adjective] to the [reference artefact]"; double confirmation ("as much as … also … also").

*Filled (original):* the table of R² values followed by "As much as it looked accurate, the R2 value also show that it is also faithful to the graphical model I initially created."

*Demo fill (different topic — colour vs. pH calibration):* a table of absorbance readings followed by "As much as it looked linear, the r² value also shows that it is also consistent with the calibration curve I plotted initially."

---

**SKELETON C — Concession → revaluation + forward projection**
   "However, as seen in the actual [figure] in [Figure X], although [subject] does resemble [idealised shape], it is never [idealisation], but [realistic shape]. While this is a source of error, it can also be seen as a strength as it [upside]. Additionally, high [metric] also proves that the steps I took are reliable and able to yield consistent results; which comes in significant in future purposes."

- **Slot 1 (however pivot):** "However, as seen in the actual [figure] in [Figure X]"; concessive connective + concrete figure reference.
- **Slot 2 (concession clause):** "although [X] does resemble [ideal]"; embedded although.
- **Slot 3 (realistic description):** "it is never [ideal], but [real-shape]"; negated ideal + corrected reality.
- **Slot 4 (revaluation):** "While this is a source of error, it can also be seen as a strength as it [upside]"; paired adversative + positive spin.
- **Slot 5 (independent supporting claim):** "Additionally, high [metric] also proves that the steps I took are reliable"; additive connective + metric noun.
- **Slot 6 (future projection):** "which comes in significant in future purposes"; relative-clause forward look.

*Filled (original):* "However, as seen in the actual 3D figure in Figure 17, although Doraemon does resemble circular shape, it is never a transformed circle, but a circle that is a bit inflated. While this is a source of error, it can also be seen as a strength as it fully used the current mathematics knowledge to everywhere applicable. Additionally, high R2 value also proves that the steps I took are reliable and able to yield consistent results; which comes in significant in future purposes."

*Demo fill (different topic — projectile fit):* "However, as seen in the high-speed footage in Video 2, although the ball does resemble a parabola, it is never a textbook parabola, but a parabola distorted by air drag. While this is a source of error, it can also be seen as a strength as it forced me to use the full drag equation instead of cherry-picking. Additionally, low χ² also proves that the steps I took are reliable and able to yield consistent results; which comes in significant in future purposes."

## Express-Idea Vocabulary

- **Sequencing / signposting:** "The result is following:" (hands to table).
- **Concession / contrast:** "However, as seen in the actual 3D figure" (introduces limitation).
- **Embedded concession:** "although Doraemon does resemble circular shape" (softens the contrast).
- **Reframing / revaluation:** "While this is a source of error, it can also be seen as a strength" (turns flaw into merit).
- **Additive support:** "Additionally, high R2 value also proves" (layers a second argument).
- **Dual-mode verdict:** "As much as it looked accurate, the R2 value also show that" (visual + numerical agreement).
- **Method-by-precedent verbs:** "I would be able to find this through applying the method" (legitimises procedure).
- **Evidence-handling verbs:** "extracted points from the graphical model", "compared the extracted dataset with the plots" (technical verbs for data pipeline).
- **Explanation verbs:** "can also be seen as a strength as it fully used the current mathematics" (re-characterisation).
- **Future-projection connective:** "which comes in significant in future purposes" (closes with use-value).

## How to Explain an Idea (replication steps)

The dominant pattern is **verification + honest-limitation + revaluation + future use**. Replicate it with these moves:

1. **Recap** the artefact you are about to verify (name it, cite its figure).
2. **Borrow credibility** by saying the procedure mirrors an earlier sub-task that worked.
3. **Run the check**: name the software/tool, the action ("extracted"), the comparison target, and the metric (R², χ², %error, etc.).
4. **Present the evidence compactly** — a table with a summary column (average, max, min) so the reader does not have to compute.
5. **Issue a double verdict** ("as much as it looked X, the metric also shows X") so two independent lines of evidence agree.
6. **Pivot with "however"** to a *visible, concrete* flaw (point at a specific figure), and phrase the flaw as "although it resembles [ideal], it is never [ideal], but [real-shape]" — a clean ideal-vs-reality split.
7. **Reframe the flaw as a strength** using "While this is a source of error, it can also be seen as a strength as it …" — pair the negative with a positive re-reading.
8. **Add an additive, independent claim** ("Additionally, …") that defends the *procedure itself*, not just the outcome.
9. **Close with a forward-looking relative clause** ("which comes in significant in future purposes") that lifts the result beyond this one task.
