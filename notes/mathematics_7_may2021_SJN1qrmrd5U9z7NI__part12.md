# Idea Flow Notes: mathematics_7_may2021_SJN1qrmrd5U9z7NI — to model the data, is more accurate due to

## Paragraph Flow (move by move)

**Paragraph 1** (3 sentences)

1. **Comparative evidence.** "its average percentage error being under 1 percent with a mere 0.97% while Equation 1's average percentage error was higher by 2.01%, sitting at an average error of 2.99%" — stacks two numerical results side by side so one is visibly lower than the other. → hands to S2 by **cause → consequence**: the gap in numbers makes a verdict inevitable.
2. **Verdict / model selection.** "Therefore, this is the equation I will use to model my data" — names the chosen model as the logical consequence of the comparison. → hands to S3 by **contrast (concession)**: a choice having just been made, the writer pivots to qualify that choice with "however."
3. **Limitation / boundary statement.** "however, since Goodreads allows the highest rating of a book to be 5.00 stars, there will be a limitation to my equation's application, since it will no longer be relevant after the rating reaches 5.00" — concedes the model has a cap and pins the cap to an external domain rule (the 5.00 ceiling). → hands to P2 by **consequence → new instance**: the limitation just named becomes the exact problem the next paragraph sets out to solve.

**Paragraph 2** (2 sentences + worked algebra)

1. **Problem re-statement as a findable quantity.** "I can find when exactly Equation 2 can no longer be used by finding when the page count stops increasing the rating, as it will have reached its maximum" — translates the abstract "limitation" into a specific variable to be solved for (page count *x* at the cap). → hands to S2 by **specification**: the general verb "finding when" is about to be tightened into a concrete algebraic instruction.
2. **Procedure specification.** "I will find this page count (x) by setting my equation equal to 5.00 and solving as follows" — converts the verbal method into an operation (set = 5.00) and signals the worked steps. → hands to the calculation block by **specification → execution**: "as follows" is the explicit promise that the algebra on the next lines is the answer to the question just posed.

---

## What This Section Does (content sequence)

The section performs a **"justify → bound → solve for the bound"** sequence:

1. **Comparative quantitative justification** of two candidate models against the same error metric. *(Sets up why a verdict is even possible — without numbers, no defensible pick.)*
2. **Verdict** naming the chosen model. *(Makes the commitment that the rest of the section is about.)*
3. **Limitation** of the chosen model stated via an external domain rule. *(Identifies the precise flaw so it can be addressed, not just acknowledged.)*
4. **Re-framing the limitation as a solvable question** — "find when…" *(Converts a qualitative worry into a variable the algebra can attack.)*
5. **Method statement** — name the algebraic operation (set equation = cap). *(Bridges verbal reasoning to symbolic working.)*
6. **Worked calculation** laid out step by step. *(Delivers the answer the method promised.)*

The order is forced by dependency: you cannot pick a model before comparing it; you cannot bound a model before choosing it; you cannot solve for a boundary before naming the boundary; you cannot algebraically execute before specifying the operation.

---

## Paragraph Skeletons (replicable templates)

### SKELETON A — "Justification-and-Limitation Paragraph"

> SKELETON: "Its [metric A] being [better number] while [competitor]'s [same metric] was [worse number]. Therefore, this is the [thing] I will use to [purpose], however, since [domain rule], there will be a limitation to [its] [scope], since it will no longer be relevant after [boundary condition]."

1. **What each slot holds (grammatical shape):**
   - Slot 1: a comparative numerical result, two clauses joined by "while" — one value low, one value high.
   - Slot 2: a decision sentence fronted by "Therefore," committing to the better-performing item.
   - Slot 3: a concession clause starting "however, since…", naming an external cap and stating that the chosen item stops working past it.
   - All three slots are declarative; verbs are mostly present tense with one future ("will use", "will no longer be relevant").
2. **How to fill with a different idea:**
   - Slot 1: pick two competing models/functions/specimens and quote their performance on the same percentage-error (or accuracy, R², RMSE) metric; put the chosen one first and the loser second.
   - Slot 2: write a one-clause commitment sentence; reuse "Therefore, this is the X I will use to model…" verbatim, swapping the noun.
   - Slot 3: name a real-world maximum (speed limit, solubility ceiling, age limit, rating cap, bandgap ceiling…) and state that the model loses meaning past it.
3. **Original filled version:**
   "its average percentage error being under 1 percent with a mere 0.97% while Equation 1's average percentage error was higher by 2.01%, sitting at an average error of 2.99%. Therefore, this is the equation I will use to model my data, however, since Goodreads allows the highest rating of a book to be 5.00 stars, there will be a limitation to my equation's application, since it will no longer be relevant after the rating reaches 5.00."
4. **Demonstration fill (different idea):**
   "its root-mean-square error sitting at just 0.34 kg while Model B's RMSE was 1.12 kg. Therefore, this is the model I will use to predict crop yield, however, since the fertiliser label states the recommended dose cannot exceed 80 kg/ha, there will be a limitation to my model's application, since it will no longer be relevant after the dose reaches 80."

---

### SKELETON B — "Find-the-Boundary Paragraph"

> SKELETON: "I can find when exactly [chosen equation] can no longer be used by finding when [independent variable] stops increasing [dependent variable], as it will have reached its maximum. I will find this [variable] (x) by setting my equation equal to [cap value] and solving as follows."

1. **What each slot holds:**
   - S1: a problem-identification sentence; structure is "I can find [thing] by finding when [cause], as [reason]." Uses "exactly" to sharpen scope.
   - S2: a procedure sentence; structure is "I will find this [variable] (x) by [operation] and solving as follows." Closes with the promise "as follows" that hands off to the algebra.
2. **How to fill with a different idea:**
   - S1: name your chosen equation/formula and the two variables in it; state the condition under which the formula stops being valid (one variable saturates).
   - S2: name the variable you are solving for (in parentheses as *x*); state the cap value as a number; end with "and solving as follows" to set up the worked block.
3. **Original filled version:**
   "I can find when exactly Equation 2 can no longer be used by finding when the page count stops increasing the rating, as it will have reached its maximum. I will find this page count (x) by setting my equation equal to 5.00 and solving as follows."
4. **Demonstration fill (different idea):**
   "I can find when exactly my dose-response curve can no longer be used by finding when yield stops increasing with dose, as it will have reached its plateau. I will find this dose (x) by setting my equation equal to 80 and solving as follows."

---

## Express-Idea Vocabulary

- **Cause / consequence:** "Therefore, this is the equation I will use to model my data" — verdict driven by prior numbers.
- **Contrast / concession:** "this is the equation I will use to model my data, however, since Goodreads allows the highest rating" — pivot from commitment to qualification.
- **Causal justification (inside a concession):** "since Goodreads allows the highest rating of a book to be 5.00 stars" — external rule invoked to ground the limitation.
- **Specification / sharpening:** "find when exactly Equation 2 can no longer be used" — "exactly" narrows a vague "find when" into a precise target.
- **Operational specification:** "by setting my equation equal to 5.00 and solving" — converts a verbal method into an algebraic instruction.
- **Forward-pointing transition (promise of working):** "and solving as follows" — explicitly announces that the calculation block answers what was just stated.
- **Evidence handling — direct quantitative contrast:** "while Equation 1's average percentage error was higher by 2.01%, sitting at an average error of 2.99%" — pairs two values from two candidates against one benchmark.
- **Reinforcement of magnitude (rhetorical amplification, not logic):** "with a mere 0.97%" — "mere" is a tone-marker nudging the reader toward the verdict.

---

## How to Explain an Idea (replication steps)

This section uses the **"compare-and-pick, then bound-the-pick"** pattern. The logical spine is: *two candidates → verdict → external cap → algebraic boundary-finder.*

Numbered replication steps:

1. **Stage two competing models on the same metric.** Write one sentence that names both candidates and gives their numerical results on a single comparable measure (percentage error, RMSE, etc.), placing the better one first and the worse one second, joined by "while." This is the load-bearing evidence — without it, no defensible choice exists.
2. **Issue the verdict with a consequence marker.** Open with "Therefore," and commit in one clause to the better performer ("this is the [equation/model] I will use to [purpose]"). Do not hedge here — the comparison has already done the work.
3. **Pivot to a limitation with a contrast marker.** Start the next clause with "however," then name an *external* domain rule (a ceiling, cap, maximum, or cut-off point) that lies outside the model. State that past this value the chosen model "will no longer be relevant." This sentence must end on a concrete boundary value so the algebra has a target.
4. **Re-cast the limitation as a solvable problem.** Reframe "the model stops working past X" as "I can find when exactly [model] can no longer be used by finding when [independent variable] stops increasing [dependent variable], as it will have reached its maximum." This step turns a complaint into a variable.
5. **Specify the algebraic operation.** State the variable you will solve for, in parentheses as *x*, and name the operation: "by setting my equation equal to [cap value]." End the sentence with "and solving as follows" — this phrase is mandatory because it licenses the worked block.
6. **Execute the worked algebra.** Lay out each rearrangement of the equation on its own line, in the order the reader needs to follow, ending where the next sub-question begins. Do not skip steps; do not annotate the algebra narratively inside the block — the verbal scaffolding already did that.
