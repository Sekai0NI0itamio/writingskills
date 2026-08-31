# Idea Flow Notes: mathematics_7_may2018_INu6ipizvRpfgvBI — number of ways which the remaining telephone can be connected (as not all telephones

## Paragraph Flow (move by move)

**Paragraph 1 — Extending the n − 1 formula**
- **S1 — Bridge / method statement.** *"Taking the formula for n − 1, this will simply require the multiplication of the formula by n:"*
  - Hand-off: it explicitly invokes the prior result, so the reader expects to see one algebraic operation applied to it next.
- **S2 — Worked calculation / result for a sub-case.** *"[…(n − 1)!…] · n = […] ways for an odd number of telephones."*
  - Hand-off: the calculation lands on a formula that is still labelled "for an odd number of telephones", which signals that the even case is still missing and must be addressed next.

**Paragraph 2 — Stating and justifying the unified formula**
- **S1 — General claim with consolidated formula.** *"In general, the maximum number of connections which can be made with n telephones, where n is odd or even, is: ⌊n/2⌋ · n! / (2^⌊n/2⌋ · ⌊n/2⌋!)."*
  - Hand-off: the word "In general" widens the scope, and the formula contains ⌊n/2⌋ — a piece of notation the reader hasn't seen explained, so a justification sentence must follow.
- **S2 — Mechanism / justification of the notation.** *"By flooring (rounding down) n/2, there is no need to have to write two formulae for the odd and even cases of n."*
  - Hand-off: it explains why the formula looks the way it does, closing the derivation and pointing the reader outward to "see" the formula in action.

**Paragraph 3 — Presenting computed values**
- **S1 — Transition to data.** *"The values of ⌊n/2⌋ · n! / (2^⌊n/2⌋ · ⌊n/2⌋!) for values of n from 0-20 are shown below:"*
  - Hand-off: announces that the abstract formula is about to be instantiated numerically, so the next sentence must introduce the table.
- **S2 — Reference / label.** *"Table 3: Number of telephones (n) with maximum connection combinations"*
  - Hand-off: closes the section by handing the reader to the visual evidence that confirms the derived expression.

## What This Section Does (content sequence)

This is a **derivation → generalisation → justification → empirical check** sequence. The order matters:

1. **Extend the known (n − 1) case** — because the new case has to be built from something already proven; the reader needs the bridge first.
2. **Compute the resulting expression for one sub-case** — so the reader sees the algebra working out before being asked to trust a unified form.
3. **State the unified general formula** — now that the algebra is plausible, the reader can absorb the "in general" claim.
4. **Justify the structure of that formula (floor function)** — because the notation is unfamiliar and the whole point of choosing it is to collapse two formulae into one; without the justification the formula looks arbitrary.
5. **Display a table of values** — empirical confirmation that the formula produces concrete numbers the reader can sanity-check.

Replicating the sequence with any other topic: (a) state the n − 1 result you already proved, (b) show one algebraic step that yields the n result for one sub-case, (c) announce the unified formula in one line, (d) defend the notation choice in one sentence, (e) show a small table of computed values.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Method-extension paragraph (prior case → one new sub-case)**
> "[Reference to prior result]. This will simply require [operation] of the formula by [factor]: [worked calculation] [result] for [specific sub-case]."

1. **Slots:** (1) past work re-stated as a noun phrase, (2) light hedge "simply require", (3) verbal name of an algebraic operation, (4) a multiplier, (5) displayed equation, (6) explicit restriction to one case ("for odd n", "for n = k", "for the lower bound", etc.).
2. **How to fill differently:** Slot 1 picks a previously proven step from your exploration and names it as "the formula for [previous parameter]". Slot 3 is the single algebraic action that turns the previous formula into the next one. Slot 6 narrows the claim to the easier sub-case so the harder case can be unified later.
3. **Original fill:** *"Taking the formula for n − 1, this will simply require the multiplication of the formula by n: [(n − 1)! · n] = […] ways for an odd number of telephones."*
4. **Demonstration fill (different idea):** *"Taking the sum for the first (k − 1) terms, this will simply require the addition of the k-th term to the running total: S_(k−1) + a_k = S_k for an arithmetic progression."*

**SKELETON B — Unified-formula paragraph (general claim → justification of structure)**
> "In general, [general claim about the system], is: [unified formula containing a consolidating notation]. By [technique that consolidates the cases], there is no need to [problem that the technique removes]."

1. **Slots:** (1) "In general," + universal claim with place, (2) compact formula, (3) named technique, (4) the duplication the technique removes.
2. **How to fill differently:** Slot 1 names what is being maximised / minimised / counted across *all* parameter values. Slot 2 places the new notation (floor, ceiling, max, min, mod, etc.) at the *position* where the odd/even cases used to split. Slot 3 names that notation as an ordinary arithmetic verb ("flooring", "taking the max", "reducing modulo"). Slot 4 states the duplication the reader would otherwise face.
3. **Original fill:** *"In general, the maximum number of connections which can be made with n telephones, where n is odd or even, is: ⌊n/2⌋ · n! / (2^⌊n/2⌋ · ⌊n/2⌋!). By flooring (rounding down) n/2, there is no need to have to write two formulae for the odd and even cases of n."*
4. **Demonstration fill (different idea):** *"In general, the smallest number of moves needed to solve an n-disk Tower of Hanoi puzzle is: 2^n − 1. By using the closed-form exponential, there is no need to have to write a separate formula for even and odd numbers of disks."*

**SKELETON C — Evidence paragraph (announce table → label it)**
> "The values of [formula] for values of [variable] from [low]–[high] are shown below: [Table caption naming what is being tabulated]."

1. **Slots:** (1) "The values of" + the formula just derived, (2) range expressed as "from a–b", (3) table label with the counted quantity.
2. **How to fill differently:** Slot 1 repeats the unified formula verbatim so the reader maps every number in the table back to the abstract expression. Slot 2 picks a small integer range (0–20, 1–15) that gives enough data to spot a pattern without becoming unreadable. Slot 3 names the dependent variable, not the formula.
3. **Original fill:** *"The values of ⌊n/2⌋ · n! / (2^⌊n/2⌋ · ⌊n/2⌋!) for values of n from 0-20 are shown below: Table 3: Number of telephones (n) with maximum connection combinations."*
4. **Demonstration fill (different idea):** *"The values of 2^n − 1 for values of n from 1–15 are shown below: Table 2: Number of disks (n) with minimum moves to solve the Tower of Hanoi puzzle."*

## Express-Idea Vocabulary

- **Sequencing / scope-widening:** "**In general**, the maximum number of connections which can be made…" — lifts the claim from one sub-case to all n.
- **Bridging / referencing prior work:** "**Taking the formula for n − 1**, this will simply require…" — signals that the next move is built on what came before.
- **Justifying a choice of notation:** "**By flooring (rounding down) n/2**, there is no need to have to write two formulae…" — explains *why* the formula takes the shape it does.
- **Exclusion / no-longer-needed phrasing:** "**there is no need to have to** write two formulae for the odd and even cases of n" — names the redundancy the new notation removes.
- **Defining / restricting the domain:** "**where n is odd or even**, is: [formula]" — embeds the domain of validity inside the claim.
- **Presentation / handing to a figure:** "**are shown below**: Table 3…" — hands the reader off to a visual artefact.
- **Light-hedge verb (calculus of effort):** "**will simply require the multiplication** of the formula by n" — minimises the work implied by the next step.

## How to Explain an Idea (replication steps)

The pattern is **derive-by-extension → unify via a single generalising function → justify that function → display computed data**. To apply it to a new idea, follow these steps in order:

1. **Name the previously proven case** in one phrase ("the formula for n − 1", "the sum of the first k − 1 terms"). Do not re-derive it.
2. **State the single operation** that turns the previous case into the next one, using a hedge verb ("this will simply require the addition / multiplication / subtraction of …").
3. **Display the worked step** so the reader sees the algebra, and label the result for the *easier* sub-case ("for odd n", "for the lower bound", "for a single row").
4. **Open with "In general,"** and write the consolidated formula in one line. Make sure the new generalising notation (floor, ceiling, max, mod, exponent) sits exactly at the position where the sub-cases used to diverge.
5. **Justify the notation in one sentence** beginning "By [technique], there is no need to [previous duplication]." This is what converts a clever-looking formula into a defensible one.
6. **Announce a table** with "The values of [formula] for values of [variable] from a–b are shown below:" and caption it with the counted quantity, not the formula.
7. **Stop.** Do not interpret the table; let the numbers speak.
