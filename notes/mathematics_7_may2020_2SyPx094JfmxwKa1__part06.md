# Idea Flow Notes: mathematics_7_may2020_2SyPx094JfmxwKa1 — Using integration by parts,

## Paragraph Flow (move by move)

**Paragraph 1 — Derivation of aₙ via integration by parts**

1. **Claim/mechanism** — The integration by parts formula is applied to `2t ∙ cos(nπt) dt`, producing the split `2t ∙ [sin(nπt)/nπ] − ∫ sin(nπt) ∙ 2 dt`. *Handoff:* this establishes the antiderivative form, so the next move can evaluate it at specific bounds.
2. **Mechanism** — The second integral `∫ sin(nπt) ∙ 2 dt` is resolved to `(1/nπ) cos(nπt)`, completing the indefinite result. *Handoff:* having the full antiderivative enables the next sentence to convert it into a definite integral.
3. **Transition** — "aₙ can then be calculated by substituting the integral with a definite integral as shown below." *Handoff:* this explicitly signals the shift from indefinite derivation to bounded evaluation.
4. **Evidence** — The bounds 0 and 2 are substituted into `(πnt ∙ sin(nπt) + cos(nπt))/nπ`, yielding two evaluated terms. *Handoff:* the evaluated expression sets up the next move to simplify the trigonometric values at those bounds.
5. **Unpack** — The trigonometric terms are simplified using `sin(0)=0`, `cos(0)=1`, `sin(2πn)=0`, `cos(2πn)=1` and `cos(-2πn)=1`, producing `{[1 − (−1)ⁿ] − [(−1)ⁿ − 1]}/(nπ)`. *Handoff:* this simplified form leads directly to the final arithmetic reduction.
6. **Consequence** — The expression reduces to `2[1 − (−1)ⁿ]/(nπ)`, giving the final closed form for aₙ. *Handoff:* this result is now available for the next paragraph's verification.

**Paragraph 2 — Verification that cₙ = aₙ**

1. **Transition/claim** — "Verifying that cₙ = aₙ using the equation of aₙ:" *Handoff:* this positions the paragraph as a cross-check, so the next sentence must carry out that verification.
2. **Evidence** — The integral `∫ 2t ∙ cos(0) dt` is split into three parts and evaluated as `t²|₀² − t²|₀² + 2t|₀² = −1 − 1 + 2 − (−2) = 2`. *Handoff:* the numerical result feeds the final ratio step.
3. **Verdict** — "∴ cₙ/2 = aₙ/2 = 1 = cₙ" confirms the equality. *Handoff:* the confirmed identity closes this verification thread and sets up the final proof section.

**Paragraph 3 — Proof that bₙ = 0 for even functions**

1. **Claim/heading** — "Proof that the Fourier Series is a Cosine Series (bₙ = 0)" *Handoff:* the heading announces the claim, so the next sentence must establish the starting assumption.
2. **Assumption** — "Assuming that bₙ ≠ 0 for a Fourier series of f(t), where f(t) is an even function in the real-number domain," *Handoff:* the assumption sets up the contradiction that follows.
3. **Evidence** — The Fourier expansion `aₙ cos[nπt/L] + bₙ sin[nπt/L]` is rewritten using `f(t) = f(-t)` to show `bₙ sin[nπt/L]` must equal `bₙ sin[-nπt/L]`. *Handoff:* this equality creates the logical tension resolved in the next sentence.
4. **Unpack** — "This creates a contradiction as bₙ sin[-nπt/L] should equal bₙ sin[nπt/L] = −bₙ sin[-nπt/L] unless nt = L so that sin(-nπt/L) = 0." *Handoff:* the contradiction narrows the solution space, leading to the universal conclusion.
5. **Implication** — "Since n changes as the Fourier coefficients are summed up and t changes with the function, the only way for the Fourier series to satisfy all terms for any given t is for bₙ = 0." *Handoff:* this universal claim is then offered for numerical verification.
6. **Transition** — "A quick calculation helps us to verify this statement." *Handoff:* signals that a computational check follows (though the calculation itself is not shown in this section).

---

## What This Section Does (content sequence)

1. **Apply a method to obtain an indefinite result** — Integration by parts is used to split `2t ∙ cos(nπt)` into an antiderivative. *Why first:* you need the general antiderivative before any bounds can be applied.
2. **Convert to a definite integral and evaluate** — The antiderivative is placed between bounds 0 and 2 and the trigonometric values are substituted. *Why second:* bounds turn the abstract antiderivative into a concrete number.
3. **Simplify to a closed-form expression** — The evaluated terms are reduced using known trigonometric identities to `2[1 − (−1)ⁿ]/(nπ)`. *Why third:* simplification makes the result usable for comparison in later steps.
4. **Cross-verify with an independent calculation** — A direct computation confirms `cₙ = aₙ`. *Why fourth:* verifying through a separate route strengthens confidence in the derived formula before moving to the next proof.
5. **Prove a property by contradiction** — Assume `bₙ ≠ 0`, expand using the even-function property, and show the resulting equality can only hold trivially. *Why last:* once `aₙ` is established, the complementary coefficient `bₙ` is addressed to complete the characterization of the series.

*Generalization:* Any student can replicate this sequence for a different integral or series by (1) deriving the general antiderivative, (2) substituting bounds, (3) simplifying, (4) verifying via an alternative route, and (5) proving a related property by contradiction if the topic requires it.

---

## Paragraph Skeletons (replicable templates)

**SKELETON 1 — Worked integration skeleton**
`"[Method] is applied to [expression], yielding [intermediate split]. The remaining integral [simplified term] is resolved, giving the full antiderivative [result]. [Variable] can then be calculated by substituting [bounds], which evaluates to [evaluated expression] and simplifies to [final closed form]."`

- **Slot shapes:** Slot 1 = noun phrase naming a calculus method; Slot 2 = mathematical expression; Slot 3 = noun phrase describing a split term; Slot 4 = noun phrase; Slot 5 = mathematical expression; Slot 6 = variable name; Slot 7 = bound values; Slot 8 = evaluated expression; Slot 9 = final simplified expression.
- **How to fill differently:** Slot 1: pick any integration technique (e.g., "trigonometric substitution"); Slot 2: write the integrand you are working with; Slot 6: rename the coefficient you are solving for; Slot 7: insert your own bounds.
- **Original fill:** "Integration by parts is applied to `2t ∙ cos(nπt) dt`, yielding `2t ∙ [sin(nπt)/nπ] − ∫ sin(nπt) ∙ 2 dt`. The remaining integral `∫ sin(nπt) ∙ 2 dt` is resolved to `(1/nπ) cos(nπt)`, giving the full antiderivative `[sin(nπt)/nπ] − (1/nπ) cos(nπt)`. aₙ can then be calculated by substituting the definite integral with bounds 0 and 2, which evaluates to `[πnt ∙ sin(nπt) + cos(nπt)]/nπ` evaluated at those bounds and simplifies to `2[1 − (−1)ⁿ]/(nπ)`."
- **Different fill:** "Substitution is applied to `x ∙ e^(2x) dx`, yielding `u = 2x` and `du = 2 dx`, giving the restructured integral `(1/4) ∫ u ∙ e^u du`. The remaining integral is resolved by parts to `(1/4)(u − 1)e^u`, giving the full antiderivative `(1/4)(2x − 1)e^(2x)`. Aₙ can then be calculated by substituting bounds 1 and 3, which evaluates to `(1/4)(2x − 1)e^(2x)|₁³` and simplifies to `(1/2)(e⁶ − e²)`."

**SKELETON 2 — Verification skeleton**
`"Verifying that [relationship] using [source equation]: [calculation split into parts] = [intermediate total], therefore [conclusion]."`

- **Slot shapes:** Slot 1 = equation asserting equality of two quantities; Slot 2 = the equation or formula being used; Slot 3 = arithmetic or algebraic steps broken into additive parts; Slot 4 = computed total; Slot 5 = final confirmed relationship.
- **How to fill differently:** Slot 1: state any two expressions you want to prove equal; Slot 2: name the formula you are using as the basis; Slot 5: restate the confirmed equality.
- **Original fill:** "Verifying that cₙ = aₙ using the equation of aₙ: `t²|₀² − t²|₀² + 2t|₀² = −1 − 1 + 2 − (−2) = 2`, therefore `cₙ/2 = aₙ/2 = 1 = cₙ`."
- **Different fill:** "Verifying that g′(x) = 2x + 3 using the power rule: `d/dx(x²) + d/dx(3x) = 2x + 3`, therefore `g′(x) = 2x + 3` is confirmed."

**SKELETON 3 — Proof by contradiction skeleton**
`"Assuming that [negated claim], where [condition], [expansion showing the assumption leads to conflicting terms]. This creates a contradiction as [term A] should equal [term B] = −[term A] unless [trivial case]. Since [variable reason], the only way for [system] to satisfy [requirement] for any [parameter] is for [negated claim to be false, i.e., original claim]."`

- **Slot shapes:** Slot 1 = the negation of what you want to prove; Slot 2 = the domain or property condition; Slot 3 = the algebraic or logical expansion; Slot 4 = one side of the conflicting equality; Slot 5 = the other side; Slot 6 = the trivial case that would resolve it; Slot 7 = explanation of why the variable cannot be fixed; Slot 8 = the system being analyzed; Slot 9 = the requirement it must meet; Slot 10 = the original (positive) claim.
- **How to fill differently:** Slot 1: negate the theorem you want to prove; Slot 2: state the domain condition; Slot 4–5: derive the conflicting expressions; Slot 10: state your theorem positively.
- **Original fill:** "Assuming that bₙ ≠ 0, where f(t) is an even function in the real-number domain, `aₙ cos[nπt/L] + bₙ sin[nπt/L]` is rewritten using `f(t) = f(-t)` to show `bₙ sin[nπt/L]` must equal `bₙ sin[-nπt/L]`. This creates a contradiction as `bₙ sin[-nπt/L]` should equal `bₙ sin[nπt/L]` = `−bₙ sin[-nπt/L]` unless `nt = L` so that `sin(-nπt/L) = 0`. Since n changes as the Fourier coefficients are summed up and t changes with the function, the only way for the Fourier series to satisfy all terms for any given t is for bₙ = 0."
- **Different fill:** "Assuming that the sequence {aₙ} diverges, where aₙ = 1/n² for all natural n, the partial sums `S_N = Σ 1/n²` are bounded above by `π²/6` by the Basel result. This creates a contradiction as {aₙ} should be unbounded if it diverges = the partial sums converge to a finite limit unless the terms do not tend to zero. Since each term `1/n² → 0` and the series is monotonically increasing and bounded, the only way for the sequence of partial sums to remain finite for any N is for {aₙ} to converge, contradicting the assumption."

---

## Express-Idea Vocabulary

**Sequencing:**
- "can then be calculated by substituting" — "aₙ can then be calculated by substituting the integral with a definite integral"
- "as shown below" — "substituting the integral with a definite integral as shown below"

**Cause/consequence:**
- "This creates a contradiction as" — "This creates a contradiction as bₙ sin[-nπt/L] should equal"
- "the only way… is for" — "the only way for the Fourier series to satisfy all terms for any given t is for bₙ = 0"

**Contrast/concession:**
- "unless" — "unless nt = L so that sin(-nπt/L) = 0"
- "= −" (sign flip) — "bₙ sin[nπt/L] = −bₙ sin[-nπt/L]"

**Specification:**
- "for any given t" — "the only way for the Fourier series to satisfy all terms for any given t"
- "in the real-number domain" — "f(t) is an even function in the real-number domain"

**Evidence handling:**
- "helps us to verify" — "A quick calculation helps us to verify this statement"
- "Verifying that" — "Verifying that cₙ = aₙ using the equation of aₙ"

**Explanation verbs:**
- "defined as" / "is an even function" — "f(t) is an even function in the real-number domain"
- "creates a contradiction as… should equal" — "This creates a contradiction as bₙ sin[-nπt/L] should equal bₙ sin[nπt/L]"

---

## How to Explain an Idea (replication steps)

**Pattern used:** Derivation → Evaluation → Verification → Proof by contradiction (a four-stage mathematical explanation pattern).

**Steps to explain a new idea with the same pattern:**

1. **State the method and apply it** — Name the technique (e.g., integration by parts, substitution, differentiation) and show its application to the target expression, writing out the intermediate split or transformation.
2. **Convert to a definite/evaluated form** — Introduce bounds, initial conditions, or specific values, and substitute them into the general result to produce a concrete numerical or simplified expression.
3. **Simplify and state the closed form** — Reduce the evaluated expression using known identities, arithmetic, or algebraic rules, and present the final compact result clearly.
4. **Cross-verify independently** — Recompute the result through a different route or direct substitution, split the calculation into visible parts, and confirm the two results match with a therefore/conclusion statement.
5. **Prove a related property by contradiction** — Assume the negation of the property you want to establish, expand using the given conditions, show that the assumption leads to a logical conflict (e.g., a term equalling its own negative), identify the trivial exception, and conclude that the original property must hold for all relevant parameters.
