# Idea Flow Notes: mathematics_7_may2018_INu6ipizvRpfgvBI — In the above table (apart from the first two rows), let n be the number of telephones and let

## Paragraph Flow (move by move)

**Paragraph 1**

1. **Sentence 1** — *Definition*: "Cn be the number of combinations with n telephones." → hands the reader to S2 by **establishing a variable that needs boundary examples** to feel anchored.
2. **Sentence 2** — *Evidence / base-case example*: "For example, n = 0, C0 = 1 and n = 1, C1 = 1." → hands the reader to S3 by **showing the minimum cases the general formula must leave alone**, so the reader now wants the "apart from" rule.
3. **Sentence 3** — *Claim (formula)* + *definition of terms*: "the combinations of n telephones are given by: Cn = Cn−1 + (n − 1)Cn−2 , where Cn−1 is the row above…" → hands the reader to S4 by **posing an abstract relation that demands a concrete instance**.
4. **Sentence 4** — *Example (substitution into the formula)*: "For example, C5 = C5−1 + (5 − 1)C5−2 = C4 + 4C3." → hands the reader to S5 by **leaving two unknowns (C4, C3) the reader cannot yet resolve**.
5. **Sentence 5** — *Evidence (lookup from table)*: "We can see from the table that C4 = 10 and C3 = 4." → hands the reader to S6 by **supplying the exact numerical inputs the example needs**.
6. **Sentence 6** — *Mechanism / computation* + *verdict*: "Therefore, C5 = 10 + 4(4) = 26, which is, indeed, what is shown…" → hands the reader to S7 by **closing the worked example and leaving the formula itself unnamed**.
7. **Sentence 7** — *Naming / classification* + *transition*: "is known as a Recurrence Relation and it is discussed in the section below." → hands the reader out of the paragraph by **promising a deeper explanation downstream**.

**Paragraph 2**

1. **Sentence 1** — *Observation / transition hand-off*: "The table shows a large increase in combinations as the number of telephones is increased." → hands the reader to the next section by **flagging a behavioural pattern (growth) that the next section will investigate**.

---

## What This Section Does (content sequence)

This is a **"formula-introduction and worked-verification" section**. The move order is:

1. **Define notation first** — gives the reader a symbol to track.
2. **Anchor with base cases** — proves the notation is real and bounded.
3. **State the general relation** — the headlining claim, in symbolic form.
4. **Define each piece of the relation** — prevents the reader mis-reading the symbols.
5. **Pick ONE specific n** — collapses the abstract formula to one numerical instance.
6. **Look up the inner values from the data** — keeps the example honest.
7. **Compute mechanically** — shows the arithmetic follows.
8. **Verify against the original data** — "which is, indeed…" closes the loop.
9. **Name the formula type** — labels the technique used.
10. **Hand off with a behavioural observation** — pivots into the next section.

**Why this order:** the reader must own the notation (1–2) before the formula is meaningful (3–4); the formula must exist (3–4) before it can be tested (5–7); the test must be checked (8) before the reader trusts the labelling (9); and the closing observation (10) seeds the next move so the section never ends in dead air.

---

## Paragraph Skeletons (replicable templates)

**Skeleton A — "Abstract formula then a fully worked numerical check"**

`SKELETON: "[Let X_n be defined as…]. For example, [boundary case 1] and [boundary case 2]. [Apart from those cases], X_n is given by: X_n = [f(X_{n−1}, X_{n−2}, n)], where [first term] is [definition] and [second term] is [definition]. For example, X_k = [expanded form]. We can see from [the data] that [value] and [value]. Therefore, X_k = [arithmetic] = [result], which is, indeed, [matches the data]. The relation … is known as [term] and it is discussed in [the next section]."`

1. **Slots:**
   - Slot 1: define the variable (`Let X_n be the [count] of [items] with n [units]`) — noun phrase introduced with "be".
   - Slot 2: give two concrete boundary values joined by "and" — paired numerals.
   - Slot 3: state the closed-form relation with two defined components — symbolic equation + two "where" clauses.
   - Slot 4: substitute a chosen n to expose the dependent values — single substituted equation.
   - Slot 5: read those values off the data — "We can see from…".
   - Slot 6: compute and verify — "Therefore … which is, indeed…".
   - Slot 7: name the technique and hand forward — "is known as … discussed in…".
2. **How to refill with a new idea:** pick a combinatorial sequence that depends on two previous terms (e.g. derangements, telephone numbers, Bell numbers, or matching brackets). Choose the smallest non-trivial n (≥2) that the reader has not yet computed, and write the substitution in two stages — substitution first, then data lookup — so the verification is visible.
3. **Original filled version (quoted):** "Cn = Cn−1 + (n − 1)Cn−2 … Therefore, C5 = 10 + 4(4) = 26, which is, indeed, what is shown in the row in which n = 5."
4. **Demonstration fill (different idea, same skeleton):** *Let D_n be the number of derangements of n objects. For example, D_0 = 1 and D_1 = 0. Apart from these, D_n is given by: D_n = (n − 1)(D_{n−1} + D_{n−2}), where D_{n−1} is the derangement count for n−1 and D_{n−2} is that for n−2. For example, D_3 = (3−1)(D_2 + D_1) = 2(D_2 + D_1). We can see from the table that D_2 = 1 and D_1 = 0. Therefore, D_3 = 2(1 + 0) = 2, which is, indeed, the value shown in the row where n = 3. The relation D_n = (n − 1)(D_{n−1} + D_{n−2}) is known as a recurrence relation and it is discussed in the section below.*

---

**Skeleton B — "Boundary cases as evidence the notation is grounded"**

`SKELETON: "[Define X_n]. For example, [n = 0, X_0 = a] and [n = 1, X_1 = b]."`

1. **Slots:** slot 1 = a noun-phrase definition opening; slot 2 = a parallel pair of literal substitutions joined by "and".
2. **How to refill:** choose the two smallest n values your sequence actually admits (usually 0 and 1, or 1 and 2) and present them as plain equalities — no prose, just the symbols and their numerical results.
3. **Original filled version (quoted):** "For example, n = 0, C0 = 1 and n = 1, C1 = 1."
4. **Demonstration fill (different idea):** "For example, n = 1, F_1 = 1 and n = 2, F_2 = 1." (boundary cases for the Fibonacci sequence).

---

**Skeleton C — "Closing transition via behavioural observation"**

`SKELETON: "The [data] shows a [qualitative trend] in [the quantity] as [the input] is [changed]."`

1. **Slots:** slot 1 = a single short sentence naming the data source; slot 2 = an adjective describing the pattern (large increase, exponential growth, oscillation…); slot 3 = the variable whose behaviour is being flagged.
2. **How to refill:** look at the table from the largest n back to the smallest and write one sentence capturing the *shape* of the trend (not a number). Use it to foreshadow the analytical section that follows.
3. **Original filled version (quoted):** "The table shows a large increase in combinations as the number of telephones is increased."
4. **Demonstration fill (different idea):** "The table shows rapid exponential growth in derangements as n is increased."

---

## Express-Idea Vocabulary

- **Sequencing / progression:** none in this section (the section is a closed worked example, not a list).
- **Specification / definition of a symbol:** *where Cn−1 is the row above* — used to unpack each piece of the formula; *is known as a Recurrence Relation* — used to label a technique.
- **Evidence handling:** *For example* (×2) — opens both the base-case mini-list and the worked instance; *We can see from the table* — frames a number as data-derived, not assumed; *what is shown in the row in which n = 5* — points the reader back to the original table as the source of truth.
- **Cause / consequence:** *Therefore* — links the substituted numbers to the computed result.
- **Verification:** *which is, indeed* — explicit confirmation marker that the arithmetic matches the data.
- **Transition:** *it is discussed in the section below* — promises the reader the technique will be unpacked later; *The table shows a large increase* — pivots from the closed example to a forward-looking observation.

---

## How to Explain an Idea (replication steps)

The pattern this section relies on is **formula-statement → component definition → single-instance substitution → data lookup → arithmetic → verification → naming → forward hand-off**.

To explain a NEW idea using the same pattern:

1. **Open with a symbol definition.** Write one sentence of the form "[Let X_n be the … with n …]."
2. **Show the minimum cases.** List the two smallest admissible n as paired equalities joined by "and."
3. **State the closed-form rule in symbols.** Write the formula once, on its own line if possible.
4. **Define each symbol inside the rule.** Use a single "where" clause (or two short clauses) so the reader does not mis-read any term.
5. **Choose ONE specific n.** Pick a value that exercises both terms of the formula (e.g. n = 5, not n = 3).
6. **Substitute that n explicitly.** Rewrite the formula with numbers in place of every symbolic reference except the unknown inner terms.
7. **Look up the inner values from the data table.** Frame this with "We can see from the table that …."
8. **Compute the arithmetic step.** Use "Therefore" and show one line of working.
9. **Verify against the table.** Add "which is, indeed, what is shown in the row in which n = [k]" to close the loop.
10. **Name the technique.** Identify the formula type (recurrence relation, closed-form, generating function, …) in one sentence.
11. **Hand off to the next section.** End with a one-sentence behavioural observation about the data ("The table shows a …") that seeds the reader into what follows.
