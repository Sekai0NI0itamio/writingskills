# Idea Flow Notes: mathematics_7_may2021_IRV8BRXWKji6u0XU — Y   n xi

## Paragraph Flow (move by move)

**Paragraph 1** — Equation block only.
- Move 1 (formal display): the binomial probability is written out as P(Y = k) = … (Equation 4). Quote: "P (Y = k)". Function: presents the discrete probability model the rest of the section will re-package. Hands the reader to Paragraph 2 by handing over the *new* object built from this one — namely the product over independent trials.

**Paragraph 2** — one short orienting sentence plus a display equation.
- Move 1 (definition / notation): "For sake of clarity, the new function in Equation (2) will be denoted a function of p and x such that". Function: renames the product-of-trials object as L(p, x) so it can be talked about as a single entity. Hands the reader to Paragraph 3 by depositing an *analysable* function — now the writer can ask what to *do* with it.
- Move 2 (display): L(p, x) = ∏ p^{x_i}(1−p)^{n−x_i}. Function: the formal definition just announced, filled in. Hands the reader forward by giving the raw algebraic object the next paragraph will manipulate.

**Paragraph 3** — the working paragraph.
- Move 1 (claim + authority): "this function must have some local maxima on the interval p ∈ (0, 1) the proof of which follows from the mean value theorem specifically." Function: asserts that the maximum-likelihood *problem exists* (a peak is guaranteed), and pins the guarantee on the MVT. Hands forward by naming the target (a maximum) so the next sentence can name the tool (a derivative).
- Move 2 (mechanism): "So we can now take the derivative of this function with respect to the parameter p." Function: selects the calculus operation that matches the claim just made ("So" = consequence of MVT implying differentiability). Hands forward by inviting the reader to ask *why*.
- Move 3 (implication / purpose): "This is important to find the p which allow for maximum probability of a number of successes occurring." Function: justifies the derivative move in probabilistic terms — the peak *means* something. Hands forward by acknowledging the algebra is about to get heavy.
- Move 4 (specification / strategy): "In order to make this process simpler, we may take the logarithm of L, log(L(p, x))." Function: introduces the log-trick, motivating it as a simplification. Hands forward by raising the question of what the log *is*.
- Move 5 (rhetorical pivot → transition): "But what is log(L(p, x))? Expanding L we get". Function: turns the abstract symbol into a concrete expansion. Hands forward by launching the displayed calculation that ends the section.
- Move 6 (display / worked step): the expansion of L as a product of binomial terms. Function: the answer to the rhetorical question — log is being computed term-by-term. Ends the section by handing the reader a fully expanded product ready to be summed.

## What This Section Does (content sequence)

This is a **transitional method section** that converts a probability formula into an analysable likelihood expression. The standard order is:

1. **Display the probability object** (Equation 4) — the writer needs the reader to see the building block before it is multiplied together.
2. **Rename and isolate it as a function** L(p, x) — a notational step that lets the writer speak about "maximising" without re-writing the product each time.
3. **Guarantee that a maximum exists** (MVT appeal) — establishes that the optimisation problem is well-posed *before* doing calculus on it.
4. **Declare the calculus tool** (derivative w.r.t. p) — the operation that follows from the guarantee.
5. **Justify the tool probabilistically** (find the p with maximum probability of successes) — gives the algebra a *meaning*.
6. **Introduce the log simplification** — anticipates algebraic pain and offers a remedy.
7. **Expand the product** so the log can actually be applied — closes the gap between the new symbol log(L(p, x)) and something computable.

Why this order: each move hands the reader the object the next move needs to act on. You cannot rename something the reader has not yet seen (steps 1→2); you cannot differentiate a function whose existence as a maximum is unverified (steps 2→3→4); you cannot log a product you have not yet written out (steps 5→6→7).

## Paragraph Skeletons (replicable templates)

**Skeleton A — "Notation hand-off paragraph"**
```
SKELETON: "For [reason], the [new object] will be denoted [symbol]([variables]) such that [displayed definition]."
```
1. *Slots:* (a) reason phrase in noun form ("sake of clarity", "ease of reference"); (b) reference to a previously-defined object ("the new function in Equation (2)"); (c) a compact two-argument symbol; (d) a displayed equation in formal notation.
2. *How to fill with a different idea:* pick the moment in your derivation where you keep re-writing the same expression; give it a single-letter name with the variables that actually vary; write the named form on its own line as a numbered equation.
3. *Original fill:* "For sake of clarity, the new function in Equation (2) will be denoted a function of p and x such that" + L(p, x) = ∏ p^{x_i}(1−p)^{n−x_i}.
4. *Demonstration fill (different idea — signal processing):* "For ease of reference, the impulse response derived in Equation (3) will be denoted as a function of t and ω such that" + H(t, ω) = ∫₀ᵗ h(τ) e^{−iωτ} dτ.

**Skeleton B — "Existence-then-tool paragraph"**
```
SKELETON: "[Callback to earlier case]. This function must have [property] on the interval [domain], the proof of which follows from [theorem] specifically. [So/Therefore], we can now [operation] with respect to [parameter]. This is important to [goal in the modelled context]."
```
1. *Slots:* (a) anaphoric reference ("As we also saw…"); (b) an extremal claim ("must have local maxima"); (c) an interval/domain of the parameter; (d) a named theorem (MVT, Rolle's, fixed-point…); (e) the calculus operation; (f) the parameter letter; (g) a substantive interpretation of what the operation achieves.
2. *How to fill:* start by pointing back to a special case already solved; lift the structural property to the general function; cite the theorem that *guarantees* the property (not the property itself); immediately deploy the operation that theorem licenses; finish by translating the operation into the language of the original problem so it is not "math for math's sake."
3. *Original fill:* "As we also saw in the specific case, this function must have some local maxima on the interval p ∈ (0, 1) the proof of which follows from the mean value theorem specifically. So we can now take the derivative of this function with respect to the parameter p. This is important to find the p which allow for maximum probability of a number of successes occurring."
4. *Demonstration fill (different idea — economics / utility maximisation):* "As we also saw in the two-good case, the utility surface must attain a maximum on the interior of the budget set, the existence of which follows from the extreme value theorem specifically. Hence, we can now take the partial derivatives of U(x, y) with respect to x and y. This is important to identify the bundle that yields the consumer's highest attainable satisfaction."

**Skeleton C — "Simplification-then-rhetorical-pivot paragraph"**
```
SKELETON: "In order to make this process [adjective], we may [operation] of [object], [new symbol]. But what is [new symbol]? [Action] we get [displayed expansion]."
```
1. *Slots:* (a) a justification word ("simpler", "tractable", "manageable"); (b) a transform (log, Laplace, Fourier, completing the square); (c) the function being transformed; (d) the transformed symbol; (e) a "what is it?" rhetorical question; (f) an imperative ("expanding", "applying", "multiplying out"); (g) the displayed worked form.
2. *How to fill:* name the algebraic pain point ("simpler"); propose a standard fix; write the fix as a symbol; immediately question the symbol out loud; turn the question into an imperative verb and display the first concrete step of working it out.
3. *Original fill:* "In order to make this process simpler, we may take the logarithm of L, log(L(p, x)). But what is log(L(p, x))? Expanding L we get" + the term-by-term product.
4. *Demonstration fill (different idea — differential equations):* "In order to make this process tractable, we may take the Laplace transform of y″(t), denoted Y(s). But what is Y(s)? Applying the transform we get" + s²Y(s) − sy(0) − y′(0) = … .

## Express-Idea Vocabulary

**Sequencing / progression**
- "So we can now take the derivative" — announces the next operational step as a consequence.
- "In order to make this process simpler" — frames the next move as a simplification of the previous one.

**Anaphoric / transition**
- "As we also saw in the specific case" — connects the general analysis back to an earlier worked example.
- "But what is log(L(p, x))?" — rhetorical pivot from abstract symbol to concrete expansion.

**Specification / precision**
- "on the interval p ∈ (0, 1)" — narrows the domain of the claim.
- "specifically" — pins the guarantee to one named tool rather than a vague appeal.

**Mathematical / explanation verbs**
- "will be denoted a function of" — name-introduction verb that converts prose into a callable symbol.
- "take the derivative … with respect to" — names the calculus operation and its parameter.
- "the proof of which follows from" — authority-handling verb that attributes the guarantee to a theorem.
- "Expanding … we get" — working-verb that signals a term-by-term rewrite is coming.

## How to Explain an Idea (replication steps)

The dominant pattern here is **display object → rename → existence guarantee → operation → justification → simplification transform → expansion**. To explain any new optimisable quantity the same way:

1. **Display the raw object.** Show the formula or expression the reader must have on screen before anything else. Put it on its own numbered line.
2. **Rename it as a function of its parameters.** Write one short orienting sentence ("For [reason], the [object] will be denoted as a function of [param 1] and [param 2] such that") and then display the renamed form. This converts prose into a callable symbol.
3. **Guarantee a solution exists.** In one sentence, claim the extremal property you need (max, min, fixed point, root), state the interval/domain, and name the theorem that *guarantees* it (MVT, EVT, Rolle's, Brouwer, IVT). Use the phrase "the proof of which follows from [theorem] specifically."
4. **Declare the tool the guarantee licenses.** Begin with a consequence marker ("So", "Hence") and state the operation: derivative, partial derivative, gradient, fixed-point iteration. Be explicit about which parameter you are operating on.
5. **Translate the tool back into the original problem.** Add one sentence that explains what finding the operation *means* in the modelled context (the p with maximum probability, the bundle with highest utility, etc.). This stops the algebra feeling decorative.
6. **Introduce a standard simplification.** Use "In order to make this process [simpler/tractable], we may [transform]" — log, Laplace, completing the square, change of variable — and write the transformed symbol.
7. **Pivot rhetorically and expand.** Ask "But what is [new symbol]?" out loud, then answer with an imperative verb ("Expanding", "Applying") followed by the displayed worked form. End the section here; the next section takes the expanded form and solves it.
