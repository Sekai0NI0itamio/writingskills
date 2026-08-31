# Idea Flow Notes: mathematics_7_may2020_ebR3LrvPDXVOrUsg — 8.2.1    For λ = ϕ1 

## Paragraph Flow (move by move)

**Paragraph 1**

1. **Sentence 1 — Observation / algebraic shortcut.**
   *Quote:* "Note that 1 − ϕ1 = ϕ2."
   **Move:** flags a substitution the reader should make in the matrix above, collapsing a future coefficient. Hands forward by **specification**: it tells the reader exactly what simplification to apply when they look at the next matrix.

2. **Sentence 2 — Method declaration.**
   *Quote:* "Use Gaussian Elimination to solve:"
   **Move:** announces the technique that will carry the rest of the paragraph. Hands forward by **procedure trigger**: it invites the reader to expect a sequence of transformed matrices next.

3. **Mathematical blocks (20)→(21)→(22)→(23) — Worked procedure.**
   *Quote:* "−ϕ1 ϕ2 −ϕ1 0" etc.
   **Move:** step-by-step row-reduction, building the reader's expectation of a final zero row that signals a free variable. Hands forward by **consequence**: the bottom row of zeros forces the next sentence to declare what was produced.

**Paragraph 2**

1. **Sentence 1 — Result transition.**
   *Quote:* "This produces the system of equations:"
   **Move:** signals that the preceding computation has crystallised into an explicit pair of equations. Hands forward by **delivery**: it commits to showing the clean equations the elimination yielded.

2. **Equations (24)–(25) — Statement of result.**
   *Quote:* "vx − ϕ1 vy = 0" and "vy = vy"
   **Move:** lays down the conclusion of the elimination. Hands forward by **identification of the free variable**: the equation `vy = vy` literally announces a free parameter, which the next paragraph must resolve.

**Paragraph 3**

1. **Sentence 1 — Conditional setup + justification + conclusion.**
   *Quote:* "If vy = 1, which can be plugged in arbitrarily since vy is an independent variable, then, vx = ϕ1 and the Eigenvector, v1 , is:"
   **Move:** combines three sub-moves — (a) **arbitrary instantiation** (`vy = 1`), (b) **justification** ("which can be plugged in arbitrarily since vy is an independent variable"), (c) **computation + naming** ("then, vx = ϕ1 and the Eigenvector, v1 , is:"). Hands forward to the final vector block by **foreshadowing**: the colon at the end tells the reader the eigenvector is written next.

---

## What This Section Does (content sequence)

The section follows a fixed derivation arc that another student could replicate on any eigen-problem:

1. **Algebraic pre-simplification** (state an identity between symbols so the matrix looks cleaner) → sets up that the next matrix reads naturally.
2. **Method declaration** (name the procedure) → licences the block of mechanical work that follows.
3. **Worked computation block** (row-reduce step by step, ending in a zero row) → produces the structural fact (a free variable) the next prose move will exploit.
4. **Result transition** ("This produces the system of equations:") → converts silent matrix manipulation into named equations.
5. **Statement of clean equations** → reveals the free variable.
6. **Justified arbitrary choice + substitution + final answer** → closes the derivation with a named eigenvector.

**Why this order:** each move supplies exactly what the next move needs — the identity is useless without the matrix to apply it to; the method is meaningless without the steps; the steps are unreadable without the "this produces" signpost; the equations are inert without the free-variable observation; the free variable is unfinalised without a justified pick.

---

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Pre-simplify then declare method"**
`Note that [identity]. Use [method] to solve:`

1. **Slot 1 — Algebraic identity.**
   *Grammar:* declarative clause naming two expressions equal, imperative present ("Note that … = …").
   *How to fill differently:* pick a substitution that will visibly appear in the next matrix (e.g. `Note that ω² + 1 = ω`).
   *Original fill:* "Note that 1 − ϕ1 = ϕ2."

2. **Slot 2 — Method imperative.**
   *Grammar:* imperative verb + named procedure + colon.
   *How to fill differently:* swap the technique name for another (e.g. `Use completing the square to solve:`).
   *Original fill:* "Use Gaussian Elimination to solve:"

**Demo fill (different idea):** *"Note that ω² + 1 = ω. Use the quadratic formula to solve:"*

---

**SKELETON B — "Result announcement after a block of work"**
`This produces the [mathematical object]:`

1. **Slot — Result noun phrase.**
   *Grammar:* demonstrative + present-tense verb + definite noun phrase + colon.
   *How to fill differently:* name whatever object the preceding calculation crystallises into (e.g. "the recurrence relation", "the characteristic equation").
   *Original fill:* "This produces the system of equations:"

**Demo fill:** *"This produces the recurrence relation:"*

---

**SKELETON C — "Justified free choice and final answer"**
`If [free variable] = [chosen value], which can be [justification phrase] since [reason it is free], then, [computed partner] and the [named object] is:`

1. **Slot 1 — Arbitrary instantiation.**
   *Grammar:* conditional `if [variable] = [number]`.
   *How to fill differently:* pick whichever variable your system labelled free and assign it `1`.
2. **Slot 2 — Justification clause.**
   *Grammar:* non-restrictive relative beginning "which can be …".
   *How to fill differently:* reuse the verb "plugged in" or substitute "chosen freely", and link to the reason it is free with "since".
3. **Slot 3 — Computed partner and naming.**
   *Grammar:* "then, [expression] and the [Object], [label], is:".
   *How to fill differently:* compute the dependent value, give the final quantity its standard name and label.

*Original fill:* "If vy = 1, which can be plugged in arbitrarily since vy is an independent variable, then, vx = ϕ1 and the Eigenvector, v1 , is:"

**Demo fill (different idea):** *"If k₂ = 1, which can be plugged in arbitrarily since k₂ is a free parameter, then, k₁ = ω² and the solution vector, x₂, is:"*

---

## Express-Idea Vocabulary

- **Signposting / calling attention:** "Note that 1 − ϕ1 = ϕ2" — flags a fact the reader must use.
- **Method declaration:** "Use Gaussian Elimination to solve:" — imperative that launches a procedure.
- **Result transition:** "This produces the system of equations:" — converts silent work into a stated result.
- **Conditional / consequence:** "If vy = 1… then, vx = ϕ1" — sets up a hypothetical and draws its consequence.
- **Justification connective:** "which can be plugged in arbitrarily since vy is an independent variable" — licenses the arbitrary choice with a reason clause.
- **Naming / labelling:** "and the Eigenvector, v1 , is:" — assigns the final quantity its canonical identity.

---

## How to Explain an Idea (replication steps)

The pattern is **algebraic-setup → method → worked steps → result transition → justified free choice → named conclusion.** To reproduce it on a new eigen-problem:

1. **Pre-simplify.** Write one sentence announcing an identity between two of the symbols that appear in your matrix; this primes the reader for the next display.
2. **Declare the method.** One imperative sentence naming the technique you will use, ending with a colon to introduce the worked block.
3. **Show the worked block.** Display each row-reduced matrix (or analogous intermediate state) in order, ending with the form that makes a free variable obvious.
4. **Result-transition.** Write "This produces the [system / equation / recurrence]:" to convert the matrices into a named mathematical object.
5. **Display the clean equations.** Lay out the resulting pair (or tuple) so the reader sees the free variable on its own.
6. **Make the justified arbitrary choice.** One sentence of the shape "If [free variable] = 1, which can be plugged in arbitrarily since [it] is an independent variable, then [partner] = [value] and the [Eigenvector / solution / …], [label], is:" — then present the final vector on a new line.
