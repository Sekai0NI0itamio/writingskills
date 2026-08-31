# Idea Flow Notes: mathematics_7_may2020_ebR3LrvPDXVOrUsg — 9     Fibonacci Ratio

## Paragraph Flow (move by move)

**Paragraph 1** (2 sentences)
- S1 — *context + observation*: "The ratios for the first 10 terms are shown in the table below, and a clear pattern is seen." → Hands off by *specification*: the "pattern" is named in the next sentence.
- S2 — *claim / specification of pattern*: "The ratios converge upon a values 1.618, or ϕ1." → Hands off by *extension*: the claim now needs to hold for all n, not just the 10 rows, so the next paragraph generalises.

**Paragraph 2** (2 sentences)
- S1 — *generalised claim / condition*: "As n grows larger, the value of the ratio converges to ϕ1." → Hands off by *promise of proof*: the reader expects the "how".
- S2 — *mechanism (introduces method)*: "This can be proven by computing the limit as n approaches ∞ of the ratio between Fn+1 and Fn." → Hands off by *formalisation*: a verbal proof-idea becomes a boxed theorem.

**Paragraph 3** (Theorem statement + algebraic proof)
- Move 1 — *formal theorem*: "Theorem 2. limx→∞ FFn+1 / n = ϕ1" → Hands off by *invitation to verify*: the reader now watches every algebraic line.
- Moves 2–9 — *worked calculation (chain of equalities)*: equations (26) → (27) → (28) → (29) → (30) → (31) → (32) → (33). Each line is *derived from* the previous one by substitution. → Hands off because the substitution of ϕ2 is non-obvious; the reader needs the justification given in the next paragraph.

**Paragraph 4** (1 sentence)
- *Justification / evidence handling*: "Note that ϕ2 = − ϕ11 since the product of the roots ϕ1 and ϕ2 is -1, derived from the formula for the product of roots in the equation, x2 − x − 1." → Hands off by *return to derivation*: the reader is sent back to equation (28) where the substitution is used.

**Paragraph 5** (equations 28 → 33)
- *Worked calculation (continuation)*: "= lim n→∞ …" lines. → Hands off because the final two terms are bounded; that observation is named in the next paragraph.

**Paragraph 6** (1 sentence, cut off)
- *Setup / specification of what is fixed*: "Note that the terms (−1)n+1 and ϕ1 (−1)n are constant even as n approaches ∞, allowing" → Hands off by *permission* (cut): the reader is told the next step is legal.

## What This Section Does (content sequence)

This is a **proof-with-motivation** section in a mathematical exploration. The ordered moves are:

1. **Empirical evidence first** — show the table of values so the reader *sees* the pattern before being told it.
2. **Name the observed pattern** — give the limit value ϕ1, so the claim is anchored to a number, not a feeling.
3. **Generalise the pattern** — "as n grows larger" shifts from 10 rows to all n.
4. **Announce the method** — "this can be proven by computing the limit", so the reader knows what tool will be used.
5. **Formalise in a theorem box** — convert the verbal claim into a statement with symbols; this is the contract being proved.
6. **Execute the algebraic proof line-by-line** — every line follows the previous by one named identity.
7. **Justify any non-obvious substitution** (e.g. ϕ2 = −1/ϕ1) — never let a step be unmotivated.
8. **Identify the bounded terms** — set up the final cancellation by naming what stays constant.

*Why this order*: a mathematical reader must see (a) what is being claimed, (b) why anyone cares, and (c) why every algebraic move is legitimate. The order moves from concrete (table) → abstract (theorem) → mechanical (calculation) → audited (justifications).

## Paragraph Skeletons (replicable templates)

**Skeleton A — Empirical lead-in to a claim**
```
SKELETON: "The [quantities] for the first [N] terms are shown [in the table/figure], and [a pattern] is seen. The [quantities] converge upon a value [X], or [symbol]."
```

1. Slot 1: numerical evidence — noun phrase naming a list of computed values ("The ratios…").
   Slot 2: verdict clause — short observation ("a clear pattern is seen").
   Slot 3: claim with numerical target and symbolic name.
2. Fill it differently: pick any sequence you've tabulated (e.g. partial sums, ratios of consecutive triangular numbers). State the first 10 rows in a table; then assert they appear to settle on one number and give it a Greek letter or constant name.
3. Original: "The ratios for the first 10 terms are shown in the table below, and a clear pattern is seen. The ratios converge upon a values 1.618, or ϕ1."
4. Demo fill: "The values of (1 + 1/n)^n for the first 10 values of n are shown in the table below, and a clear pattern is seen. The values approach a limit near 2.718, or e."

**Skeleton B — Generalisation + method declaration**
```
SKELETON: "As [variable] grows larger, the [quantity] converges to [value]. This can be proven by [technique applied to limit of ratio/expression]."
```

1. Slot 1: conditional clause with "as X grows larger".
   Slot 2: limit-style claim stating convergence.
   Slot 3: mechanistic sentence beginning "This can be proven by…" naming the operation (limit, sum, derivative).
2. Fill it differently: pick any convergent sequence, take the variable to infinity in the opening clause, name the limit, then announce the tool (limit, induction, integral test).
3. Original: "As n grows larger, the value of the ratio converges to ϕ1. This can be proven by computing the limit as n approaches ∞ of the ratio between Fn+1 and Fn."
4. Demo fill: "As k grows larger, the kth partial sum S_k approaches π²/6. This can be proven by evaluating the limit of S_k as k approaches ∞."

**Skeleton C — Justification of a substitution step**
```
SKELETON: "Note that [expression A] = [expression B] since [principle], derived from [named formula]."
```

1. Slot 1: "Note that" + an equality between two forms of the same quantity.
   Slot 2: "since" + a one-clause reason (product of roots, sum of angles, integration by parts).
   Slot 3: "derived from" + a named identity/theorem.
2. Fill it differently: whenever a calculation uses an apparently magical rewrite, isolate it in its own sentence and back it with a standard result.
3. Original: "Note that ϕ2 = − ϕ11 since the product of the roots ϕ1 and ϕ2 is -1, derived from the formula for the product of roots in the equation, x2 − x − 1."
4. Demo fill: "Note that sin(2θ) = 2 sin θ cos θ since the angle-doubling identity holds, derived from the sine addition formula."

**Skeleton D — Bounded-term announcement**
```
SKELETON: "Note that the terms [A] and [B] are constant even as [variable] approaches ∞, allowing [next simplification]."
```

1. Slot 1: flag word "Note that".
   Slot 2: list two bounded pieces of the expression.
   Slot 3: "even as [variable] approaches ∞" to mark the limit context.
   Slot 4: "allowing" + a one-clause forecast of what is now permitted (cancellation, division, passage to limit).
2. Fill it differently: any time your limit expression contains oscillating or bounded factors, point them out before the final step so the reader can see why the limit exists.
3. Original: "Note that the terms (−1)n+1 and ϕ1 (−1)n are constant even as n approaches ∞, allowing" (text cuts off).
4. Demo fill: "Note that the factors (−1)^n and cos(nπ/2) are bounded between −1 and 1 even as n approaches ∞, allowing the remainder term to vanish in the limit."

## Express-Idea Vocabulary

**Sequencing / flow**
- "and a clear pattern is seen" — observation marker.
- "The ratios for the first 10 terms are shown" — evidence presentation.

**Cause / consequence**
- "This can be proven by computing the limit" — announces consequence of claim.
- "derived from the formula for the product of roots" — explains origin.

**Contrast / concession** — none used; the section is strictly deductive.

**Specification / focus**
- "Note that ϕ2 = − ϕ11" — flags a non-obvious step.
- "in particular" is absent; "Note that" does the same job.

**Evidence handling**
- "shown in the table below" — cites numerical evidence.
- "is derived from the formula for the product of roots" — cites theorem.

**Explanation / definition verbs**
- "converge upon a values 1.618" — defines target.
- "can be proven by computing" — method verb.
- "derived from" — origin verb.
- "allowing" — permission verb (sets up next move).

## How to Explain an Idea (replication steps)

**Pattern name: Observation → Claim → Method → Formal Theorem → Worked Calculation → Justified Substitutions → Bounded-term Audit.**

Use this when you want to convince a reader that a numerical pattern is a true mathematical fact.

1. **Show the data.** Open with a table or figure that tabulates the first ~10 instances and let a sentence announce that a pattern is visible.
2. **Name the pattern in words and symbols.** State the limit/target value and give it a notation (ϕ1, e, L) so the reader can refer back to it.
3. **Generalise the variable.** Move from "the first 10 terms" to "as n grows large" so the claim is about all instances.
4. **Announce the proof technique.** One sentence beginning "This can be proven by…" naming the operation (limit, induction, derivative test).
5. **Box the claim as a theorem.** Rewrite the verbal statement in symbols with a label ("Theorem 2."). This is the contract.
6. **Walk through the algebra one line at a time.** Each line equals the previous by exactly one named identity; number the equations so the reader can track substitutions.
7. **Justify every non-obvious substitution in its own sentence.** Use "Note that X = Z since … derived from …". Never let an unmotivated rewrite appear.
8. **Audit the bounded pieces.** End the proof by pointing out which factors stay constant or bounded as n → ∞, then state what that allows you to conclude.
