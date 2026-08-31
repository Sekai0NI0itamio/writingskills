# Idea Flow Notes: biology_6_may2021_jqeZkGx0EglqCQ4V — The process should be repeated for the next four groups and all total values should be

## Paragraph Flow (move by move)

**Paragraph 1 (calculation line — functions as a continuation of the prior calculation):**
1. Sentence 1 — **Continuation of a worked calculation**, quoting "added together": picks up from the previous clause (elliptical) so the reader is forced to treat this as the next step in the same arithmetic chain. *Hand-off: cause* — the previous line left sums unresolved, so this sentence provides the products that must be summed.
2. Sentence 2 (formula line "CPm = ∑ … = 187.1137149") — **Generalization + verdict**, quoting "CPm= ∑ nk(xgroup DV1-xDV1)": takes the long string of products just shown and folds them into a named symbolic form, giving the reader a label and a final numerical answer (187.1137149). *Hand-off: consequence* — having produced a value, the next paragraph must explain where that value is used, which requires introducing the next term.

**Paragraph 2 (introducing the error cross product):**
1. Sentence 1 — **Transition + identification of next requirement**, quoting "The next element that is needed": names the next logical ingredient the formula needs and frames it as a dependency on the prior value. *Hand-off: specification* — the word "needed" tells the reader the following sentences will specify what that element is.
2. Sentence 2 — **Definition by formula**, quoting "CPE= ∑ (xi -xDV1)(xi -xDV2)": supplies the symbolic definition so the term introduced in sentence 1 has a concrete shape. *Hand-off: procedure trigger* — once the formula is shown, the reader expects the sentence to say how to compute it.
3. Sentence 3 — **Procedure instruction**, quoting "must have the group means subtracted": tells the reader the operational rule for plugging numbers in (subtract group means, then multiply). *Hand-off: repetition trigger* — the instruction is stated in general terms, so the next sentence extends it across the dataset.
4. Sentence 4 — **Scope extension**, quoting "repeated for all data points and groups": generalizes the instruction from one specimen to the whole dataset. *Hand-off: demonstration* — having told the reader to repeat the process, the writer now has to show one instance.
5. Sentence 5 (worked example line ending "= 17.32775511") — **Worked example + numerical verdict**, quoting "(4.1- 4.82857143)(25.3 - 27.942857142857)": demonstrates one or two concrete substitutions following the rule just stated and closes with a final value. *Hand-off: stop* — the section ends on the closed numeric verdict, since the next step would use this value in a ratio.

## What This Section Does (content sequence)

This is a **worked-calculation bridge** between a named formula's main term and the next ingredient that formula needs. The ordered content moves are:

1. **Close out the prior sum.** (carry-forward of arithmetic already started above the section) — sets up that a value is about to be named.
2. **Name and box the result of that sum into a symbolic form** (CPm = … = 187.11…) — turns loose numbers into a labelled quantity the formula can refer back to.
3. **Flag the next ingredient as needed** ("The next element that is needed is…") — tells the reader the logic requires another term before the formula can be completed.
4. **Define that next ingredient with its own formula** (CPE = ∑ …) — gives the new term a symbolic identity parallel to the first.
5. **State the operational rule for that formula** ("subtracted from them and then multiplied") — turns the symbol into a procedure.
6. **Generalize the procedure across the dataset** ("repeated for all data points and groups") — scales the rule.
7. **Demonstrate one substitution and close with a verdict** (worked numbers = 17.3277…) — proves the procedure works and produces the next boxed value.

**Why this order works:** each move hands the reader exactly one job. You cannot name the next element (3) until the prior sum is boxed (2); you cannot define it (4) until it is flagged (3); you cannot demonstrate it (7) until the rule is generalized (5–6). The pattern is *box prior result → flag next dependency → define next term → state rule → generalize → demonstrate → box new result*, which is how any multi-part formula should be walked through in a report.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Carry the prior line into a closed symbolic verdict":**
- `[continued arithmetic] = [boxed value]`, immediately followed by a labelled general formula `[Symbol] = ∑ [components] = [boxed value]`.

   1. *Slot 1 (continued arithmetic)*: a chain of products/sums written in inline numerical form, no prose. *Slot 2 (boxed value)*: a single rounded number that closes slot 1. *Slot 3 (symbolic label)*: a capital-letter abbreviation equal to the formula being computed. *Slot 4 (general formula)*: a summation notation referencing the components of slot 1. *Slot 5 (final value)*: the same number as slot 2, repeated as the verdict.
   2. **How to fill with a different idea**: pick the last un-named sub-calculation in your worked solution; write out its numeric expansion as one inline expression; round to a value; introduce a 2–4 letter symbol for that sub-calculation; restate it as a summation; restate the same rounded value after the equals sign.
   3. **Original fill**: "added together. … CPm = ∑ nk(xgroup DV1−xDV1)(xgroup DV2−xDV2) = 187.1137149".
   4. **Demonstration fill (different idea — titration equivalence-point check)**: "summed together. 0.5(8.4 − 7.2)(12.1 − 10.8) + 0.5(7.9 − 7.2)(11.6 − 10.8) + … = 3.42. SE = ∑ wk(Vi − V̄acid)(Ti − T̄acid) = 3.42."

**SKELETON B — "Flag the next ingredient, define it, and give the procedure for it":**
- `The next [element/quantity] that is needed is the [name]. The [name] is [abbreviation] = ∑ [formula]. [Operational rule stated about each data point]. The process should be repeated for [scope].`

   1. *Slot 1 (flag)*: starts with "The next element that is needed is the…" in present tense, simple declar­ative. *Slot 2 (definition)*: a one-line symbolic equality introducing the abbreviation. *Slot 3 (operational rule)*: a sentence telling the reader which value to subtract from which, in passive voice ("must have X subtracted from them and then multiplied"). *Slot 4 (scope)*: a short instruction to extend the rule across all groups/points.
   2. **How to fill with a different idea**: after finishing one sub-formula, name the very next term your overall equation needs; give it an abbreviation and write its summation form; then write one sentence telling the reader, in plain procedural English, what arithmetic to perform on each raw data point; then close with a sentence saying the procedure must be repeated across every group/case.
   3. **Original fill**: "The next element that is needed is the cross product of the error. The cross product of the error is CPE = ∑(xi − x̄DV1)(xi − x̄DV2). The first data points for the two dependent variables… must have the group means subtracted from them and then multiplied. The process should be repeated for all data points and groups."
   4. **Demonstration fill (different idea — standard error of a calibration curve)**: "The next element that is needed is the residual sum of squares. The residual sum of squares is RSS = ∑(yi − ŷi)². Each measured absorbance must have its predicted absorbance from the regression line subtracted from it, and the result squared. The process should be repeated for all standard concentrations."

**SKELETON C — "Demonstrate one substitution and close with a boxed number":**
- `([first input − its mean])([second input − its mean]) + ([second input − its mean])([…]) + … = [verdict number]`

   1. *Slot 1 (first bracketed pair)*: one raw data point minus its group mean, then a second bracketed pair with another variable's mean, all multiplied. *Slot 2 (continuation)*: same structure repeated for several more data points, joined by "+". *Slot 3 (verdict)*: a single equals sign and a rounded number.
   2. **How to fill with a different idea**: take the formula defined in Skeleton B; pick the first 2–4 raw data rows; for each row, write (raw − mean of variable 1)(raw − mean of variable 2); join with plus signs; show an ellipsis if you are not writing every term; close with the rounded total.
   3. **Original fill**: "(4.1−4.82857143)(25.3−27.942857142857) + (4.4−4.82857143)(25.6−27.942857142857) + … = 17.32775511".
   4. **Demonstration fill (different idea — RSS demonstration)**: "(0.182−0.174)(0.41−0.39) + (0.176−0.174)(0.38−0.39) + (0.169−0.174)(0.36−0.39) + … = 0.00174".

## Express-Idea Vocabulary

**Sequencing / procedural flow**
- "The next element that is needed is…" (flags that one procedure has finished and the next must begin)
- "must have the group means subtracted from them and then multiplied" (orders two actions: subtract, then multiply)
- "The process should be repeated for all data points and groups" (closes a single-case demonstration and scales it)

**Generalization / definition verbs**
- "is CPE =" / "CPE= ∑…" (introduces a symbol by equating it to a formula)
- "CPm= ∑…" (same pattern, used to name the previously-computed quantity)

**Specification / scope**
- "in particular" is not used here; instead scope is marked by **"for all data points and groups"** and by **"The first data points for the two dependent variables"**

**Evidence handling**
- No explicit connectives; raw numbers themselves act as evidence, introduced by the equals sign and closed by a rounded verdict (e.g. "= 187.1137149", "= 17.32775511")

**Causal / consequence connectives**
- None — the section relies on positional logic (one line after another) rather than words like "therefore" or "hence"

**Contrast / concession connectives**
- None used in this excerpt

## How to Explain an Idea (replication steps)

This section uses the **worked-calculation bridge pattern**: *name and box what you already computed → *flag the next ingredient the overall formula needs → *define that ingredient symbolically → *state the procedure in plain English → *generalize the procedure → *demonstrate one substitution → *box the new value. Steps to replicate on a new idea:

1. **Finish the previous line of arithmetic** in inline numerical form, ending with an equals sign and a rounded number, so the reader sees a closed result before you move on.
2. **Box that result under a symbol** by writing a labelled summation formula that restates the components you just summed, and repeat the same rounded number after a second equals sign — this gives the reader something to refer back to.
3. **Open the next move with "The next [thing] that is needed is…"** so the reader is explicitly told a new ingredient is required and why (the overall equation is incomplete).
4. **Define the new ingredient with a parallel symbolic equality** — abbreviation = ∑(components) — keeping the visual rhythm identical to step 2 so the reader recognizes the pattern.
5. **Translate the symbol into a one-sentence operational rule** in passive voice, telling the reader exactly which raw values to subtract from which means and what to do with them (e.g. "subtracted from them and then multiplied").
6. **Generalize the rule across the dataset** with a short sentence ("repeated for all data points and groups") so the reader knows the demonstration is not the whole procedure.
7. **Demonstrate one or two substitutions in bracket notation**, using ellipsis ("…") to indicate the remaining terms are not all written out, and close with an equals sign and a rounded verdict number.
8. **Stop.** Do not explain what the new value will be used for; leave that for the next section, so the bridge stays one bridge.
