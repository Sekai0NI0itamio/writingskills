# Idea Flow Notes: mathematics_7_may2021_SJN1qrmrd5U9z7NI — 5 of 18

## Paragraph Flow (move by move)

**Paragraph 1 — Median recap (carry-over from previous section)**

- Move 1: **Continuation of prior result.** "320 + 322 / 2 = 321" → states the median already obtained, with no connecting sentence. It hands the reader forward only by numerical availability: the value 321 is *not* used downstream, but the symbol "median" is, so the chain depends on it implicitly as scaffolding.

**Paragraph 2 — Quartile setup and calculation**

- Move 1: **Sequencing transition + goal statement.** "Now the data can be split evenly in half and the upper and lower quartile can be found:" — the "Now" signals "we have the median; the next move is quartiles," which hands the reader to the definition that follows by announcing exactly what the next four lines will produce.
- Move 2: **Definition (verbal).** "lower quartile = median of lower half of data" — names the operation in words; hands forward by *requiring* a calculation that turns "lower half" into a single number.
- Move 3: **Application (symbolic → numerical).** "lower quartile = (46/2)th term = 23rd term = 212" — substitutes the dataset size, collapses to a rank, and lands on a value; hands forward by symmetry (an upper analogue is now demanded for balance).
- Move 4: **Parallel definition.** "upper quartile = median of upper half of data" — mirrors Move 2; hands forward by structural symmetry.
- Move 5: **Parallel application.** "upper quartile = (46/2)th term = 23rd term = 452" — mirrors Move 3; hands forward because *both* quartile values are now available, which is exactly what the next sentence needs.

**Paragraph 3 — IQR transition and calculation**

- Move 1: **Causal transition.** "Through these values, the Interquartile Range (IQR) can be found as seen below." — "Through these values" explicitly names Q1 and Q3 (just calculated) as inputs; hands forward by introducing a new quantity that *requires* those inputs.
- Move 2: **Formula statement.** "IQR = Q3 − Q1" — names the operation abstractly; hands forward because the symbols Q1 and Q3 now need concrete substitution.
- Move 3: **Substitution and result.** "IQR = 452 − 212 = 240" — feeds the two previously obtained quartile values in; hands forward because 240 is now the unique new quantity the boundary formulas require.

**Paragraph 4 — Boundary transition, formulas, and table reference**

- Move 1: **Sequencing transition ("finally").** "And finally the upper and lower boundary can be found:" — "finally" closes the calculation chain; hands forward by promising the *last* pair of derived values.
- Move 2: **Parallel formula statements.** "upper boundary = upper quartile + 1.5 × IQR" paired with "lower boundary = lower quartile − 1.5 × IQR" — both formulas appear together; hands forward because both now demand numerical substitution.
- Move 3: **Parallel substitutions.** "lower boundary = 212 − (1.5 × 240) = − 148" and "upper boundary = 452 + (1.5 × 240) = 812" — plug in the stored values; hands forward because the *purpose* of these numbers is stated in the table caption that follows.
- Move 4: **Result reference.** "Table 2: The Outliers Removed" — names what the entire chain has produced and points the reader to the visual that uses it.

## What This Section Does (content sequence)

1. **Carry-forward of prior result** (median) — *sets up* the implicit "data now sorted" assumption the rest depends on.
2. **Verbal transition with "Now"** announcing the next sub-task — *sets up* the reader to expect two paired calculations.
3. **Word-definition of operation** (lower quartile as median of lower half) — *sets up* a symbolic translation.
4. **Symbolic → numerical application** — *produces* a value needed downstream.
5. **Parallel word-definition** (upper quartile) — *sets up* the matching application.
6. **Parallel symbolic → numerical application** — *completes* the pair.
7. **Causal transition "Through these values…"** — *names* what the just-produced pair feeds into.
8. **Abstract formula** (IQR = Q3 − Q1) — *sets up* substitution.
9. **Substitution and result** — *produces* the IQR value, the key multiplier used twice later.
10. **Sequencing transition "And finally…"** — *marks* end of chain.
11. **Paired formulas** (upper and lower boundaries) — *set up* paired substitutions.
12. **Paired substitutions** — *produce* the final pair of values.
13. **Result reference** ("Table 2: The Outliers Removed") — *closes* the chain by showing what the values were *for*.

The order is dictated by strict data dependency: each calculated value is the *input* the next formula needs, so the chain can only run forward, never backward.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Verbal transition announcing a paired operation:**
"Now the data can be split evenly in half and the upper and lower [X] can be found:"
- *Slot grammar:* adverbial sequencing word ("Now"), then declarative sentence ending in a colon.
- *Slot 1:* sequencing marker — "Now", "Next", "Following this" — pick a continuation word that fits position in the chain.
- *Slot 2:* the *single operation* you are about to perform on *two related sub-sets*; pick any quantity whose definition naturally comes in a "lower / upper" or "inner / outer" pair.
- *Original:* "Now the data can be split evenly in half and the upper and lower quartile can be found:"
- *Demo fill (different idea):* "Now the motion can be resolved into components and the horizontal and vertical velocities can be found:"

**SKELETON B — Paired definition + application (lower analogue):**
"[lower X] = [verbal definition]; [lower X] = ([n]/2)th term = [rank]th term = [value]"
- *Slot grammar:* short noun-phrase identity, then an equals-chain.
- *Slot 1:* first quantity name (e.g. "lower quartile") + "= median of lower half of data" — must be *one short clause*.
- *Slot 2:* same symbol + arithmetic/positioning collapse + final number — the equals-chain is the structural fingerprint.
- *Original:* "lower quartile = median of lower half of data" followed by "lower quartile = (46/2)th term = 23rd term = 212"
- *Demo fill:* "lower fence = smallest value above lower hinge" → "lower fence = (25+1)/2 = 13th rank = 87"

**SKELETON C — Causal transition into a derived quantity:**
"Through these values, the [Derived Quantity] ([ABBR]) can be found as seen below."
- *Slot grammar:* prepositional phrase ("Through these values") + declarative + directional phrase ("as seen below").
- *Slot 1:* preposition phrase naming the *just-computed* values — "Through these values", "Using these results", "From the figure above".
- *Slot 2:* the new quantity, optionally introduced by an acronym in brackets on first appearance.
- *Original:* "Through these values, the Interquartile Range (IQR) can be found as seen below."
- *Demo fill:* "Through these velocities, the Resultant Magnitude (R) can be found as seen below."

**SKELETON D — Paired formulas in parallel columns, then paired substitutions:**
"[upper X] = [upper component] + [constant] × [shared Y]"  /  "[lower X] = [lower component] − [constant] × [shared Y]" — then the same pair substituted numerically.
- *Slot grammar:* two symbolic identities laid out side by side, followed by two numeric identities laid out side by side.
- *Slot 1:* the *two* formulas must share the same multiplier so the visual symmetry reads instantly.
- *Slot 2:* the two substitutions should also be visually paired.
- *Original:* "upper boundary = upper quartile + 1.5 × IQR" / "lower boundary = lower quartile − 1.5 × IQR" → "upper boundary = 452 + (1.5 × 240) = 812" / "lower boundary = 212 − (1.5 × 240) = − 148"
- *Demo fill:* "upper control limit = mean + 3 × std dev" / "lower control limit = mean − 3 × std dev" → "upper control limit = 50 + 3(2.1) = 56.3" / "lower control limit = 50 − 3(2.1) = 43.7"

## Express-Idea Vocabulary

**Sequencing (move forward in the chain):**
- "Now the data can be split evenly" — "Now", reopening the chain after the median.
- "And finally the upper and lower boundary" — "And finally", closing the chain.

**Cause / consequence (input → derived quantity):**
- "Through these values, the Interquartile Range (IQR) can be found" — names the upstream values as the *cause* of the next calculation.

**Reference / location (where to look):**
- "can be found as seen below" — directional pointer to the formula that follows.
- "Table 2: The Outliers Removed" — caption-style reference closing the section.

**Explanation verbs (defining operations):**
- "lower quartile = median of lower half" — uses "= … of …" to define operationally.
- "upper quartile = median of upper half" — mirrors the definition verb pattern.

## How to Explain an Idea (replication steps)

This section uses the **chained-derivation pattern**: each new quantity is defined verbally, given a symbolic formula, then evaluated numerically, before the next quantity is unlocked. To replicate:

1. **Open with a sequencing transition** that explicitly links backward ("Now…") to the just-computed value and announces the next sub-task ending with a colon.
2. **State the operation in plain words first**, using an equals sign and a one-clause definition (e.g. "[quantity] = [verbal definition]"). This is your reader's anchor.
3. **Translate the verbal definition into a symbolic equals-chain** that collapses intermediate steps into one line ("= ([n]/2)th term = [rank]th term = [value]"). Three equals signs is the rhythm.
4. **Immediately mirror the previous three steps for the parallel quantity** (lower / upper, x / y, left / right). Same three moves, same layout.
5. **Insert a causal transition** ("Through these values, the [Derived Quantity] can be found…") that *names* the pair just produced as the input to the next formula.
6. **State the new formula abstractly** on its own line ("[New] = [A] − [B]"). One symbol, one rule.
7. **Substitute and evaluate** on the next line, plugging the *exact* numbers produced in step 3–4.
8. **Mark closure with "And finally…"** when you are writing the last derived pair.
9. **Lay out the final two formulas in parallel columns**, then lay out their two substitutions in parallel columns — visual symmetry tells the reader "these are a pair".
10. **End with a result reference** (table caption, figure label) that names what the whole chain was *for*.
