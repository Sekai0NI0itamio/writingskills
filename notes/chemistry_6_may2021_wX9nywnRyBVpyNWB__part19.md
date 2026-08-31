# Idea Flow Notes: chemistry_6_may2021_wX9nywnRyBVpyNWB — 11.5 Uncertainty in Trendlines: Analysis has shown that increasing temperature decreases both average Ecell and 𝐾𝑐 ; both

## Paragraph Flow (move by move)

**Paragraph 1** (Ecell vs Temperature — first relationship):

1. **Sentence 1** — *continuation claim + data-quality note*: "have negative linear correlations with the equations … respectively, having removed the anomalous data point at 298.15±0.50K."
   Hands to next by **specification** — two equations are named at once, so the reader expects them to be treated one at a time; the next sentence narrows to the first.

2. **Sentence 2** — *evidence → implication*: "The error bars for temperature and average Ecell are small, therefore using maximum and minimum lines are not feasible to obtain error."
   Hands to next by **method-forcing contrast** — "therefore … not feasible" creates a problem that the next sentence must solve.

3. **Sentence 3** — *method substitution*: "Instead, the line estimate function on MS Excel can be employed which uses the uncertainty of the slope itself."
   Hands to next by **result delivery** — having named the tool, the next sentence must report what it produced.

4. **Sentence 4** — *result statement*: "The coefficient of 𝑥 in the average Ecell against temperature is −0.00118 ±1.64 × 10⁻⁴."
   Hands to next by **comparison pivot** — the first relationship is closed off with a number; the reader now waits to see whether the second follows the same path.

**Paragraph 2** (Kc vs Temperature — second relationship):

1. **Sentence 1** — *contrast pivot + evidence + method*: "For 𝐾𝑐 against temperature, since the error bars are larger, maximum and minimum lines (graph 4) can be used to find the uncertainty in gradient."
   Hands to next by **procedure specification** — a method has been chosen, so the next beat must show *how* it is performed.

2. **Sentence 2** — *worked calculation*: "The half range method (table 6) can be used: (Maximum Gradient – Minimum Gradient)/2 = (−0.01408 – 0.00341)/2 = ±0.008745 = ±8.75 × 10⁻³"
   Hands to next by **result packaging** — the raw calculation must now be re-stated as the final quoted coefficient.

3. **Sentence 3** — *result statement*: "The coefficient of 𝑥 in 𝐾𝑐 against temperature is −0.00540 ± 8.75 × 10⁻³."
   Hands to next by **metric escalation** — a raw ± value has been delivered; the natural next move is to convert it into a more comparable percentage.

**Paragraph 3** (Percentage uncertainty — first application):

1. **Sentence 1** — *methodological pivot + dual-announcement*: "Percentage uncertainty is calculated using the formula below for the gradients of average Ecell and temperature, and 𝐾𝑐 and temperature, respectively:"
   Hands to next by **display** — "respectively" pre-packages both calculations; the next block must show the first one in full, mirroring paragraph order.

2. **Worked calculation block** — *numerical demonstration for Ecell*: "Uncertainty/Measured Value × 100 = 1.64 × 10⁻⁴ / −0.001182 × 100 = ±13.9%"
   Hands to next by **implied parallel** — the "respectively" promise still owes the reader the second calculation.

**Paragraph 4** (Percentage uncertainty — second application):

1. **Worked calculation block** — *numerical demonstration for Kc*: "Uncertainty/Measured Value × 100 = 8.75 × 10⁻³ / −0.00540 × 100 = ±162%"
   Terminal — section ends; the dual-promise of "respectively" is now satisfied and no comparison or verdict is offered.

## What This Section Does (content sequence)

An *uncertainty-in-trendlines* section moves through this ordered sequence:

1. **State trendline equation(s)** with any anomalous points removed — sets up what will be quoted as "the value."
2. **Assess error-bar magnitude on the chosen axes** — this single observation decides which uncertainty method is valid.
3. **Branch the method on error-bar size** (small → statistical slope-uncertainty tool; large → graphical max/min lines).
4. **Show the worked calculation for the chosen branch** so the ± number is auditable, not asserted.
5. **Quote the final coefficient with its ± uncertainty** — closes the raw-value beat.
6. **Promote raw ± to percentage uncertainty** because two relationships with different units/scales can only be compared in %.
7. **Apply percentage uncertainty to *both* relationships** in parallel, using "respectively" so the order of appearance is locked to the order of treatment above.

The order is forced by dependency: you cannot pick a method (step 3) until error bars are assessed (step 2); you cannot quote a ± (step 5) until the calculation runs (step 4); you cannot compute a % (step 7) until the ± exists (step 5). Repeating steps 3–7 for the second relationship is what makes the section symmetrical rather than lopsided.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "First relationship, statistical branch"**
Slot template:
"[Equations], having removed the anomalous data point at [point]. The error bars for [var A] and [var B] are [size], therefore [graphical method] [is/are] not feasible to obtain error. Instead, [statistical tool] can be employed which [what it uses]. The coefficient of [x] in [relationship] is [value ± uncertainty]."

1. **Slot grammar**: equations are bare mathematical forms; the removal note is a participial clause; "small/large" is the key adjective; the statistical tool is named generically (software function or formula).
2. **Fill instructions**: slot 1 = the two fitted line equations from your graph (mention data removal if you discarded any); slot 2 = a one-word size judgement on the visible bars; slot 3 = the name of the tool that returns uncertainty directly (e.g. LINEST, a regression function); slot 4 = what that tool mathematically uses (slope standard error); slot 5 = the gradient ± its uncertainty, copied from the tool output.
3. **Original fill**: "have negative linear correlations with the equations 𝑦 = −0.00118𝑥 + 0.76332 and 𝑦 = −0.00540𝑥 + 6.06501 respectively, having removed the anomalous data point at 298.15±0.50K. The error bars for temperature and average Ecell are small, therefore using maximum and minimum lines are not feasible to obtain error. Instead, the line estimate function on MS Excel can be employed which uses the uncertainty of the slope itself. The coefficient of 𝑥 in the average Ecell against temperature is −0.00118 ±1.64 × 10⁻⁴."
4. **Demonstration fill** (different topic — rate vs pH): "have positive linear correlations with the equations 𝑦 = 0.0047𝑥 + 0.011 and 𝑦 = 0.0092𝑥 − 0.083 respectively, having removed the anomalous data point at pH 4.5. The error bars for pH and reaction rate are small, therefore drawing maximum and minimum lines are not feasible to obtain error. Instead, the LINEST function on MS Excel can be employed which uses the standard error of the slope itself. The coefficient of 𝑥 in rate against pH is 0.0047 ± 6.1 × 10⁻⁴."

---

**SKELETON B — "Second relationship, graphical branch"**
Slot template:
"For [second relationship], since the error bars are [size], [graphical method] can be used to find the uncertainty in gradient. The [named sub-method] can be used: (Maximum Gradient − Minimum Gradient)/2 = ([a] − [b])/2 = ±[result]. The coefficient of [x] in [relationship] is [value ± uncertainty]."

1. **Slot grammar**: "For …, since …" sets up a contrast with the first relationship; "can be used" introduces the procedure; the calculation is the half-range formula displayed with substituted numbers.
2. **Fill instructions**: slot 1 = name of the second y-variable and the same x-variable, in the same order as Skeleton A; slot 2 = the opposite size adjective to slot A; slot 3 = the graphical method you would use (max/min lines); slot 4 = the specific procedure label (e.g. half-range method); slot 5 = the two extreme gradient values you read off your graph; slot 6 = the final coefficient with the half-range uncertainty attached.
3. **Original fill**: "For 𝐾𝑐 against temperature, since the error bars are larger, maximum and minimum lines (graph 4) can be used to find the uncertainty in gradient. The half range method (table 6) can be used: (Maximum Gradient – Minimum Gradient)/2 = (−0.01408 – 0.00341)/2 = ±0.008745 = ±8.75 × 10⁻³. The coefficient of 𝑥 in 𝐾𝑐 against temperature is −0.00540 ± 8.75 × 10⁻³."
4. **Demonstration fill** (different topic — absorbance vs concentration): "For absorbance against concentration, since the error bars are larger, maximum and minimum lines (graph 2) can be used to find the uncertainty in gradient. The half range method (table 3) can be used: (Maximum Gradient − Minimum Gradient)/2 = (0.182 − 0.149)/2 = ±0.0165. The coefficient of 𝑥 in absorbance against concentration is 0.165 ± 0.0165."

---

**SKELETON C — "Dual percentage-uncertainty block"**
Slot template:
"Percentage uncertainty is calculated using the formula below for [relationship 1] and [relationship 2], respectively: Uncertainty/Measured Value × 100 = [unc₁]/[val₁] × 100 = ±[pct₁]%. Uncertainty/Measured Value × 100 = [unc₂]/[val₂] × 100 = ±[pct₂]%."

1. **Slot grammar**: introductory clause uses "respectively" to lock ordering; both calculation lines use the identical template so the reader can scan them side by side.
2. **Fill instructions**: keep the "respectively" so the order matches Skeletons A and B; paste the same ± value and coefficient you just reported; only the *meaning* (×100, %) is new — the inputs are recycled from earlier paragraphs.
3. **Original fill**: "Percentage uncertainty is calculated using the formula below for the gradients of average Ecell and temperature, and 𝐾𝑐 and temperature, respectively: Uncertainty/Measured Value × 100 = 1.64 × 10⁻⁴/−0.001182 × 100 = ±13.9%. Uncertainty/Measured Value × 100 = 8.75 × 10⁻³/−0.00540 × 100 = ±162%."
4. **Demonstration fill** (different topic): "Percentage uncertainty is calculated using the formula below for the gradients of rate against pH, and absorbance against concentration, respectively: Uncertainty/Measured Value × 100 = 6.1 × 10⁻⁴/0.0047 × 100 = ±13.0%. Uncertainty/Measured Value × 100 = 0.0165/0.165 × 100 = ±10.0%."

## Express-Idea Vocabulary

- **Sequencing / parallel ordering**: "respectively" — appears in "the equations … respectively, having removed the anomalous data point" and in "for the gradients of average Ecell and temperature, and 𝐾𝑐 and temperature, respectively".
- **Cause / consequence**: "therefore" — "The error bars for temperature and average Ecell are small, therefore using maximum and minimum lines are not feasible to obtain error."
- **Contrast / concession / method-forcing pivot**: "Instead," — "Instead, the line estimate function on MS Excel can be employed which uses the uncertainty of the slope itself."
- **Conditional cause (because-the-data-is-different)**: "since" — "For 𝐾𝑐 against temperature, since the error bars are larger, maximum and minimum lines … can be used".
- **Procedural verbs (method introduction)**: "can be employed", "can be used" — "the line estimate function … can be employed"; "maximum and minimum lines … can be used"; "The half range method … can be used".
- **Specification / relative-clause unpacking**: "which uses the uncertainty of the slope itself" — unpacks *what* the Excel function actually does.
- **Result-introducer**: "The coefficient of 𝑥 in … is …" — appears in both relationship blocks, signposting the final quoted number.

Note: this section deliberately avoids hedging verbs ("suggests", "implies") because the work is numerical, not interpretive — the verbs are all *operational* (employed, used, calculated).

## How to Explain an Idea (replication steps)

The pattern is **conditional-branch uncertainty calculation**:

1. **Announce both relationships together** with their fitted equations, in the same sentence, and flag any data point you removed. This locks the *order* in which you will treat them.
2. **Judge error-bar size for relationship #1** in one clause. Decide the method from this single observation — if bars are small, the graphical method will not work; if bars are large, it will.
3. **Justify the rejected method with "therefore … not feasible"** so the reader sees the choice is forced, not arbitrary.
4. **Name the chosen method in an "Instead," sentence** and unpack, in a relative clause, what it mathematically uses (e.g. "the uncertainty of the slope itself").
5. **Quote the final coefficient with its ± value** in one short sentence. This is the deliverable of branch #1.
6. **Open branch #2 with "For …, since …"** — the "since" clause must give the *opposite* error-bar judgement, which is what makes a second branch necessary rather than redundant.
7. **Show the half-range worked calculation explicitly** (numerator, denominator, intermediate and final values), because a graphical method has no automated output to copy.
8. **Quote branch #2's coefficient with its ± value** in the same one-sentence shape as step 5.
9. **Promote both raw ± values to % uncertainty** in a single paragraph that uses "respectively" to re-invoke the order established in step 1, and displays both calculations with the identical formula template.
10. **Stop.** No verdict is needed — the comparison is done by the numbers themselves; any commentary belongs in the next section (e.g. "Evaluation of Uncertainty").
