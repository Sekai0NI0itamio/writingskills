# Idea Flow Notes: mathematics_7_may2018_INu6ipizvRpfgvBI — Number of telephones (n) Number of combinations

## Paragraph Flow (move by move)

**Paragraph 1 — Data Observation**
- S1: CLAIM from data — *"The first obvious thing which can be seen here is that, for n > 0, numbers of combination"* — surfaces a pattern noticed in the preceding table; flags the reader that an empirical observation is about to be generalized.
- Hand-off (cause): the empirical claim begs verification → next sentence specifies the precise pattern.
- S2: SPECIFICATION of the pattern — *"n and n + 1 have the same number of combinations where n is odd."* — narrows the observation to odd n only; sets up a falsifiable proposition that demands proof.

**Paragraph 2 — Proof Setup**
- S1: TRANSITION + TASK ANNOUNCEMENT — *"To prove this works for all odd n ∈ N, consider:"* — converts the pattern into a universal claim and announces an algebraic proof.
- Hand-off (consequence): the universal claim must be formalised → next paragraph stages the equality.
- S2 (equation): DEFINITION of the two quantities under comparison — `nC(n/2)` and `(n+1)C((n+1)/2)` — pins down what "same number of combinations" means symbolically.

**Paragraph 3 — Equality Statement**
- S1: TASK RECASTING — *"We must show that these two expressions are equal:"* — restates the goal as a pure equality, making the proof target explicit.
- Hand-off (procedure): goal is set → next paragraph executes the first algebraic step.

**Paragraph 4 — First Manipulation**
- S1: PROCEDURE STEP (verb-led) — *"First, multiply both sides by both denominators to give:"* — uses ordinal sequencing; eliminates denominators to clear the fraction.
- Hand-off (chaining): cleared denominators → next step can simplify.

**Paragraph 5 — Second Manipulation**
- S1: PROCEDURE STEP (chained) — *"We can then divide both sides by n!:"* — exploits the previous clearing; reduces the factorial expression.
- Hand-off (need): residual combinatorial terms remain → next paragraph supplies the key identity.

**Paragraph 6 — Justifying Identity**
- S1: JUSTIFICATION via modular arithmetic — *"Since n ≡ 1 (mod 2): [binomial coefficients simplify]"* — supplies the specific number-theoretic fact that unlocks the simplification.
- Hand-off (enabling): the identity makes substitution possible → next paragraph performs it.

**Paragraph 7 — Substitution Step**
- S1: PROCEDURE STEP (consequence-led) — *"Therefore, we can re-write the equation as:"* — causal connective links the prior identity to a new form.
- Hand-off (further reduction): the new form still has factorials → next paragraph proposes a division that uses another identity.

**Paragraph 8 — Division Using Difference-of-Indices Identity**
- S1: PROCEDURE + JUSTIFICATION fused — *"Since the difference of [these indices] is 1, we can divide both side of the equation by"* — combines a number-theoretic fact with a manipulation; collapses a large factorial expression.
- Hand-off (escalation): the equation is now tractable → next paragraph reduces to powers of √2.

**Paragraph 9 — Terminal Algebraic Chain**
- S1: MECHANISM step — *"Multiplying both sides by √2 gives:"*
- S2: MECHANISM step — *"Then dividing both sides by (√2)^n gives:"*
- Each step uses a verb of operation (multiplying, dividing) that mirrors the previous step's inverse; the chain collapses to `C(n+1,2) = n+1`.
- Final line — *"n+1=n+1"* — is the tautological residue, the visual endpoint that proves equality.
- Hand-off (verdict): the chain must now be interpreted → next paragraph delivers the conclusion.

**Paragraph 10 — Verdict**
- S1: VERDICT — *"Both sides are shown to be identical. Hence, the equation holds true for all odd n ∈ N."* — closes the proof, echoing the universal quantifier from paragraph 2 to bookend the argument.

## What This Section Does (content sequence)

This is a **proof section** following an empirical observation. The ordered content moves are:

1. **Empirical claim** extracted from a data table — sets the puzzle to be explained.
2. **Specification** of the claim to a precise case (odd n only) — narrows scope to a falsifiable statement.
3. **Universal restatement** ("for all odd n ∈ N") — converts observation into something requiring proof.
4. **Symbolic restatement** of the two quantities being compared — translates words into algebra.
5. **Goal restatement** ("we must show … equal") — names the equality to be demonstrated.
6. **Sequenced algebraic manipulations** (multiply denominators, divide by n!, substitute binomial identity, divide by factorial using index difference, manipulate roots) — each step is a single arithmetic action labelled by a verb.
7. **Justification injections** at decision points (mod-2 argument, index-difference argument) — supply the number-theoretic fact that licenses the next manipulation.
8. **Tautological residue** (`n+1 = n+1`) — visual proof that the algebra closed.
9. **Verdict restating the original universal claim** — bookends the proof and returns to the language of the opening.

The order matters because each manipulation only becomes *legal* once the previous justification has been supplied; the chain cannot be reordered without breaking the logic.

## Paragraph Skeletons (replicable templates)

### Skeleton A — Observation-to-Proof Opener (1 paragraph)

SKELETON: *"The first obvious thing which can be seen here is that, [empirical pattern from data]. To prove this works for all [quantified domain], consider: [symbolic restatement]."*

1. **Slot 1 (empirical pattern)**: a past-tense observation drawn from immediately preceding data; names two variables and a condition under which they coincide. Grammatically: relative clause introduced by "which".
2. **Slot 2 (proof transition + universal claim)**: infinitive-of-purpose clause ("To prove…") followed by an algebraic display. Sets up the formal target.
3. **HOW to fill differently**: slot 1 — pick two adjacent rows or values from a table you have just shown, name the rule that links them and the restriction (odd/even/positive/etc.). Slot 2 — pick the quantifier that matches the restriction and write the two expressions that must be shown equal.
4. **Original fill**: *"The first obvious thing which can be seen here is that, for n > 0, numbers of combination are in pairs such that n and n + 1 have the same number of combinations where n is odd. To prove this works for all odd n ∈ N, consider: [C(n, n/2) and C(n+1, (n+1)/2)]."*
5. **Demonstration fill (different idea)**: *"The first obvious thing which can be seen here is that, for n ≥ 1, Fibonacci values appear in pairs such that F(n) and F(n+1) sum to F(n+2). To prove this works for all n ∈ N, consider: F(n) + F(n+1) and F(n+2)."*

### Skeleton B — Chained Algebraic Manipulation Block (1 paragraph)

SKELETON: *"First, [first verb-led manipulation] to give: [equation]. [Chaining connective], [second verb-led manipulation]: [equation]. Since [number-theoretic justification], [consequence verb]: [simpler equation]."*

1. **Slot 1 (first action)**: ordinal adverb + verb of arithmetic + "both sides" object + result. Grammatically: imperative mood directed at the reader.
2. **Slot 2 (chaining connective)**: temporal/consecutive phrase such as "we can then" or "next".
3. **Slot 3 (second action)**: same shape as slot 1 but operating on the result.
4. **Slot 4 (justification clause)**: introduces the number-theoretic fact that unlocks the next move.
5. **HOW to fill differently**: pick any equality involving factorials/binomials where one identity (e.g., `C(n,k) = C(n,n-k)`, index difference = 1, or mod-2 parity) licenses a substitution; chain three to five single-action steps, each producing a simpler equation.
6. **Original fill**: *"First, multiply both sides by both denominators to give: … We can then divide both sides by n!: … Since n ≡ 1 (mod 2): C((n+1)/2, …) = …, therefore, we can re-write the equation as: …"*
7. **Demonstration fill**: *"First, multiply both sides by (n−1)! to give: n! = (n+1)·(n−1)!. We can then divide both sides by (n−1)!: n = n+1. Since n ∈ N is undefined here, we cannot proceed further."*

### Skeleton C — Verdict Paragraph (1 paragraph)

SKELETON: *"[Tautological residue displayed]. [Restatement that both sides are identical]. Hence, [the original universal claim restated verbatim]."*

1. **Slot 1 (tautology)**: the displayed equation of the form `X = X` or its algebraic equivalent.
2. **Slot 2 (verdict verb)**: passive reporting verb ("is shown", "is established", "is verified").
3. **Slot 3 (causal conclusion)**: "Hence"/"Therefore" + restatement of the universal claim from the opener.
4. **HOW to fill differently**: display the final algebraic identity in display form, then sentence stating it is identical, then one sentence echoing the original claim with its quantifier.
5. **Original fill**: *"n+1 = n+1. Both sides are shown to be identical. Hence, the equation holds true for all odd n ∈ N."*
6. **Demonstration fill**: *"2 = 2. Both sides are shown to be identical. Hence, the recursion holds for all n ∈ N."*

## Express-Idea Vocabulary

**Sequencing**
- *"First, multiply both sides"* — ordinal adverb initiating the first manipulation.
- *"We can then divide"* — temporal chaining connective for the second step.
- *"Then dividing both sides by"* — third-step chaining, maintains imperative procedural voice.

**Cause / Consequence**
- *"Therefore, we can re-write the equation"* — causal pivot that converts the prior identity into a new form.
- *"Hence, the equation holds true"* — final consequence marking proof completion.

**Specification / Restriction**
- *"where n is odd"* — restricts the empirical claim to a subset.
- *"for all odd n ∈ N"* — quantifier + restriction defining the universal domain.
- *"Since n ≡ 1 (mod 2)"* — equivalent technical restatement of "n is odd".

**Justification / Evidence Handling**
- *"Since the difference of [these indices] is 1"* — supplies the numeric fact licensing the next division.
- *"Both sides are shown to be identical"* — passive verdict reporting the proof outcome.

**Explanation / Manipulation Verbs**
- *"multiply both sides by both denominators"* — clearing-fractions verb cluster.
- *"divide both sides by n!"* — factorial-cancellation verb cluster.
- *"re-write the equation as"* — substitution/rewriting verb.
- *"is shown to be"* — passive proof-completion verb.

**Definition / Framing**
- *"numbers of combination are in pairs"* — informal definition framing the empirical observation.
- *"We must show that these two expressions are equal"* — task-defining verb cluster.

## How to Explain an Idea (replication steps)

This section relies on the pattern: **empirical observation → precise restatement → symbolic translation → goal statement → sequenced algebraic chain with embedded justifications → tautological residue → verdict**.

Step-by-step instructions to replicate:

1. **Display a small table** (or list) of values for two variables; let the reader spot a pattern in adjacent rows.
2. **State the observed pattern in words**, naming the two variables and the condition (parity, sign, range) under which they match. Use a "first obvious thing …" framing to flag it as empirical.
3. **Tighten the pattern into a universal claim** by introducing a quantifier ("for all … ∈ N"). This converts observation into something requiring proof.
4. **Translate the claim into symbols** by writing the two algebraic expressions that must coincide; display them.
5. **Restate the goal as an equality to be shown** ("We must show that … are equal"). This is the proof's target.
6. **Choose a first legal manipulation** (multiply through, divide through, substitute); announce it with an ordinal adverb + verb of arithmetic + "both sides".
7. **Execute and display** the resulting equation.
8. **Insert a justification clause** ("Since [number-theoretic identity]") whenever the next move requires licensing; keep justifications to a single sentence.
9. **Chain three to five single-action manipulations**, each announced by a verb cluster and producing a simpler displayed equation.
10. **Drive the chain until a tautology appears** (e.g., `X = X`); this is the visual proof of equality.
11. **Close with a verdict** in two sentences: passive reporting ("Both sides are shown to be identical") followed by a "Hence/Therefore" sentence that restates the universal claim from step 3, bookending the proof.
