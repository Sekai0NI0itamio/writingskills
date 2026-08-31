# Idea Flow Notes: physics_7_may2021_3NjrLqxuscMBL327 — Temperature

## Paragraph Flow (move by move)

**Paragraph 1 — Data Table (functions as evidence presentation):**

- **Move: column scaffolding (claim of variables).** The header row names the quantities to be read: "Attempt     Attempt     Attempt                     mavg /kg" — sets up that three repeats feed one mean. *Hands to next:* the reader now knows what columns will populate, so the first data row can land without explanation.
- **Move: uncertainty scaffolding (definition of precision).** "∆T = 0.05" beside "Random Uncertainties are placed in each respective individual values" — tells the reader that ± values will sit inside the cells, not outside them. *Hands to next:* the reader expects every averaged value to carry its own ±.
- **Move: numerical evidence (raw data).** Three repeats per temperature row — "0          0.56121     0.56218     0.56220" — delivers the spread from which the mean will be drawn. *Hands to next:* the spread shown, the averaged column immediately answers it.
- **Move: numerical evidence (processed data).** "0.56186 ± 5.0 × 10−4" — collapses the three attempts above into a single number with uncertainty. *Hands to next:* the next row offers a fresh instance for the reader to verify the pattern.
- **Move: caption (verdict on table's role).** "Table 2: Table of results of measured properties of each measuring cylinder with Glycerol" — labels the table's identity and scope. *Hands to next:* the explanatory paragraph must now justify *how* these numbers were obtained.

**Paragraph 2 — Methodology justification + worked example:**

- **Move: claim of dual computation (context).** "Both of the measurement uncertainty and the random uncertainties were calculated." — announces two uncertainty sources exist in this experiment. *Hands to next:* having named two, the writer must now choose.
- **Move: contrast + decision (implication).** "However, for future calculations, the random error will be used as is a significantly higher value." — discards one source via concession ("However") and selects the other via reason ("as is a significantly higher value"). *Hands to next:* the chosen quantity now demands a formula.
- **Move: mechanism (definition of the chosen method).** "The random uncertainty was calculated by subtracting the smallest Attempt value from the largest, then dividing by 2." — specifies the arithmetic operation step by step. *Hands to next:* an abstract formula invites one concrete instance.
- **Move: specification + transition to worked example.** "For the example calculation, data for T = 0◦ C was used:" — narrows the abstract rule down to one row of the table. *Hands to next:* the displayed equation fulfils the promise just made.
- **Move: worked evidence.** "∆mavg = (0.56220 − 0.56121) / 2 = 5.0 × 10−4 to 1 s.f." — instantiates the formula on numbers already familiar from the table, closing the loop between rule and data.

## What This Section Does (content sequence)

1. **First — present raw repeated measurements** in a grid (three attempts per condition). *Why first:* the reader needs the spread before any averaged number is meaningful; without seeing the repeats, the averaged column looks fabricated.
2. **Second — collapse each row into a mean with an attached uncertainty** in the same table. *Why second:* the averaging step is now auditable against the raw values to its left; the formula can be reverse-checked visually.
3. **Third — announce that two uncertainty types exist.** *Why third:* only after the reader has seen numerical evidence does the question of "which error bar matters" arise.
4. **Fourth — discard one uncertainty and justify the discard by magnitude.** *Why fourth:* the choice must be motivated by something the reader has already seen (the ± column), not asserted by authority.
5. **Fifth — define the surviving uncertainty as an arithmetic recipe.** *Why fifth:* once the choice is locked, the recipe is the next logical gap.
6. **Sixth — instantiate the recipe on one row.** *Why last:* the example closes the abstract-to-concrete arc and lets the reader trust every other row in the table.

Generalised order for any lab section: **raw repeats → averaged+uncertainty table → flag competing error types → pick one and justify → write the recipe → worked one-row example.**

## Paragraph Skeletons (replicable templates)

**Skeleton A — The "evidence + caption" table paragraph**

SKELETON: "[Column headers naming raw repeats and processed quantity]. [Per-row: three repeat values]. [Per-row: mean ± uncertainty]. [Caption: 'Table N: Table of results of [measured property] of [apparatus] with [substance]']."

1. **Slot 1 (column headers)** — noun phrases, one per quantity. *Fill:* list the independent variable, the three repeat columns, the processed column, and any constant mass/calibration column.
2. **Slot 2 (raw repeats per row)** — numerical triplets, same unit as headers. *Fill:* record three readings taken at each step of the independent variable.
3. **Slot 3 (processed mean ± uncertainty per row)** — single number, ±, same unit. *Fill:* compute the mean of the triplet and quote its absolute uncertainty to 1 s.f.
4. **Slot 4 (caption)** — one sentence, formal register. *Fill:* "Table N: Table of results of [property] of [instrument] with [material]."
5. **Original fill (this text):** header → "mavg /kg"; row → "0.56121 0.56218 0.56220"; processed → "0.56186 ± 5.0 × 10−4"; caption → "Table 2: Table of results of measured properties of each measuring cylinder with Glycerol".
6. **Demonstration fill (different idea — resistance of a wire):** headers → "Attempt Attempt Attempt    R /Ω"; row → "2.31 2.34 2.29"; processed → "2.31 ± 2.5 × 10−2"; caption → "Table 4: Table of results of measured resistance of nichrome wire with length".

**Skeleton B — The "two errors, one chosen, recipe, example" paragraph**

SKELETON: "Both of the [error type A] and the [error type B] were calculated. However, for future calculations, the [chosen one] will be used as is a significantly higher value. The [chosen one] was calculated by [operation 1 on quantity], then [operation 2]. For the example calculation, data for [condition] was used: [worked line]."

1. **Slot 1 (announce dual sources)** — full sentence, present perfect passive. *Fill:* name both uncertainty contributions the experiment generated.
2. **Slot 2 (contrast + choice with reason)** — "However, … as is a significantly higher value". *Fill:* pick the larger of the two by magnitude; never assert the choice without the magnitude reason.
3. **Slot 3 (recipe)** — one sentence chaining two operations with "then". *Fill:* write the recipe in the imperative logic of arithmetic (subtract X from Y, then divide by Z).
4. **Slot 4 (worked example anchor)** — "For the example calculation, data for [condition] was used:". *Fill:* pick the row from the table that the reader has already seen, so they can verify the substitution.
5. **Slot 5 (worked line)** — centred display equation, result to 1 s.f. *Fill:* substitute the row's largest and smallest repeats into the recipe.
6. **Original fill (this text):** "Both of the measurement uncertainty and the random uncertainties were calculated. However, for future calculations, the random error will be used as is a significantly higher value. The random uncertainty was calculated by subtracting the smallest Attempt value from the largest, then dividing by 2. For the example calculation, data for T = 0◦ C was used: ∆mavg = (0.56220 − 0.56121)/2 = 5.0 × 10−4 to 1 s.f."
6. **Demonstration fill (different idea — pendulum period):** "Both of the stopwatch reaction-time uncertainty and the random spread in timings were calculated. However, for future calculations, the random spread will be used as is a significantly higher value. The random spread was calculated by subtracting the shortest timing from the longest, then dividing by 2. For the example calculation, data for L = 1.00 m was used: ∆T = (2.18 − 2.05)/2 = 6.5 × 10−2 s to 1 s.f."

## Express-Idea Vocabulary

- **Sequencing / specification of procedure:** "then dividing by 2" — the verb "dividing" chains the second step onto the first arithmetic action; "then" makes the order explicit.
- **Contrast / concession:** "However, for future calculations, the random error" — "However" flips the reader's expectation from "both will be used" to "only one will"; "for future calculations" scopes the concession to later sections.
- **Cause / reason (compressed):** "as is a significantly higher value" — "as" introduces the reason for the discard in the same breath as the decision.
- **Evidence handling / quantity acknowledgement:** "Random Uncertainties are placed in each respective individual values" — passive present tense names where in the layout the reader should look for ± marks.
- **Definition / method naming:** "The random uncertainty was calculated by subtracting" — the verb "calculated by … -ing" announces a recipe rather than a result.
- **Transition to worked instance:** "For the example calculation, data for" — prepositional phrase "for the example calculation" flags that the abstract recipe is about to be instantiated on a single row.
- **Quantifier framing:** "Both of the measurement uncertainty and the random uncertainties" — "Both of … and …" sets up the upcoming binary choice.
- **Existence claim:** "∆T = 0.05" — equal sign + numerical value asserts the precision of the independent variable before any row is read.

## How to Explain an Idea (replication steps)

**Pattern used:** *dual-source acknowledgement → magnitude-based selection → arithmetic recipe → single-instance worked example.* This is the **"pick the bigger error, then show how"** pattern.

1. **Step 1 — Announce the two sources.** Write one sentence in present perfect passive naming both contributions your experiment produced (e.g. "Both of X and Y were calculated"). This sets the reader up to expect a choice.
2. **Step 2 — Make the choice with a magnitude reason.** Open the next sentence with "However," and use "as is a significantly higher value" (or an equivalent magnitude comparator) to justify discarding one source. The reason must be numerical, not authoritative.
3. **Step 3 — Convert the choice into a recipe.** Write one sentence that defines the surviving quantity as a chain of two operations joined by "then" (e.g. "was calculated by [op1], then [op2]"). Avoid prose; write it as a procedure.
4. **Step 4 — Anchor the recipe to one row.** Open the next sentence with "For the example calculation, data for [condition] was used:" — pick a row the reader has already seen in your table so verification is possible.
5. **Step 5 — Display the substitution.** Lay out the worked line as a displayed equation with the result quoted to 1 s.f. and the unit. This closes the abstract-to-concrete arc.
6. **Step 6 (optional, for next paragraph) — Generalise backwards.** The reader can now read every other row of your table and trust that the same recipe was applied; no further justification is needed.
