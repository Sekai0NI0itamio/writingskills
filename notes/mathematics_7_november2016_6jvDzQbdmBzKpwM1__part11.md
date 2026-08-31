# Idea Flow Notes: mathematics_7_november2016_6jvDzQbdmBzKpwM1 — 1                       (1 + cos 𝜃) 2𝑣h

## Paragraph Flow (move by move)

**Paragraph 1**
1. **Sentence 1** — VERDICT: "Thus we have derived an expression for 𝑘 as required." Closes off a previous derivation and signals the work that follows is the evaluation of what was just derived.
2. **Sentence 2** — MECHANISM/CALCULATION: "Evaluating the integral, 𝑘 = −∫ … d cos 𝜃" — Hands to next sentence because the integral is set up but not yet solved; the reader needs to see how the integrand is manipulated.
3. **Sentence 3** — MECHANISM (algebraic reorganisation): the integrand is rewritten as a product inside the same integral. Hands to the next paragraph because the substitution that unlocks the integral is the next logical step.

**Paragraph 2**
1. **Sentence 1** — DEFINITION/SUBSTITUTION STATEMENT: "Substituting 𝑢 = 1 − cos 𝜃 so d cos 𝜃 = −1/(1−cos 𝜃)² …" — Hands forward because the reader must see *why* the differentials convert that way; the equivalence justifies the change of variable.
2. **Sentence 2** — MECHANISM (apply substitution): the integral is rewritten entirely in terms of 𝑢. Hands forward because the new integrand still needs algebra before integration is possible.
3. **Sentence 3** — MECHANISM (split/expand): "(2𝑢 − 1) = (2𝑢 − 1 + 1)(2𝑢 − 1)" splits the numerator so that like terms separate. Hands forward by setting up the integrand as a sum of two integrable pieces.
4. **Sentence 4** — MECHANISM (distribute/simplify): the expression becomes a sum of two integrals. Hands forward because each term now has a clear power-of-𝑢 form ready to integrate.

**Paragraph 3**
1. **Sentence 1** — MECHANISM (pull constant + integrate): the leading factor 2/4 is written explicitly and each term is integrated. Hands forward because the antiderivative has been found but not yet bounded.
2. **Sentence 2** — MECHANISM (apply limits): the bracket is evaluated between 1 and 1−cos 𝜃₀, with the condition "(provided 2𝑣h^(+1/2) > 0)" attached. Hands forward because the closed form for 𝑘 exists but is not yet in its usable form.

**Paragraph 4**
1. **Sentence 1** — TRANSITION/REFERENCE: "Substituting in Equation 8," — Hands forward by signalling that the just-derived 𝑘 must now be plugged back into the previously stated master equation.
2. **Sentence 2** — MECHANISM (substitution into Equation 8): the big fraction is constructed with 𝑘's expression substituted. Hands forward because the algebra must collapse before the final answer is reached.
3. **Sentences 3–5** — MECHANISM (algebraic cancellation): repeated equals-signs show common factors being cancelled and terms being collected.
4. **Sentence 6** — VERDICT/FINAL RESULT: "= 𝐷₀ (𝑣r² − 𝑣h² cos² 𝜃₀) / (𝑣r² − 𝑣h²)" labelled (10). Hands backward as closure — the derivation is complete.

## What This Section Does (content sequence)

This is a **worked calculation / algebraic evaluation section**. The ordered moves are:
1. **Closure of prior step** — declare the expression whose evaluation follows.
2. **Set up the integral** — write it explicitly with limits and integrand.
3. **Reorganise the integrand** — factorise/rewrite so a substitution becomes visible.
4. **State the substitution** — name new variable, give the differential identity.
5. **Apply the substitution** — rewrite integral in new variable.
6. **Split / expand** — decompose the integrand into integrable pieces.
7. **Integrate** — write the antiderivative.
8. **Apply bounds** — evaluate at the limits, attaching any domain condition.
9. **Reference the master equation** — link the result back to an earlier equation number.
10. **Algebraic simplification chain** — a sequence of equals-signs showing cancellation.
11. **Final closed form** — the answer, tagged with an equation number.

This order is required because each move produces the expression that the next move needs to act on: a substitution cannot be applied until the integrand is reorganised; integration cannot proceed until pieces are split; the final form cannot be written until simplification has occurred.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Setup the evaluation" paragraph**
   SKELETON: "[Verdict closing the prior derivation]. Evaluating [the expression to be evaluated], [expression] = [rewritten form with same integral but tidied integrand]."

   1. **Slot 1**: A short closing-claim sentence, present-perfect tense ("Thus we have derived…"), declaring a result is in hand and now needs evaluation.
   2. **Slot 2**: A gerund clause naming the operation ("Evaluating the integral,"), followed by an equals-sign chain rewriting the same quantity once.
   3. **HOW to fill with a new idea**: pick the *previous* derived quantity (any boxed/symbolised expression). Slot 1 paraphrases what has just been shown. Slot 2 displays the quantity twice — the second time with its integrand/factor/sum rearranged so the next paragraph's substitution has something to grip.
   4. **Original**: "Thus we have derived an expression for 𝑘 as required. Evaluating the integral, 𝑘 = −∫(1+cos𝜃)/(cos𝜃(1−cos𝜃)³) d cos 𝜃 = −(1/𝐴𝑣h)∫(2−1)(…)/(cos𝜃(1−cos𝜃)·(1−cos𝜃)²) d cos 𝜃."
   5. **Demonstration fill (different idea)**: "Thus we have derived an expression for the displacement Δ as required. Evaluating the sum, Δ = Σ_{i=1}^{n}(F_i · cos α_i) = Σ_{i=1}^{n}(F_i(1+sin α_i − sin α_i)cos α_i)."

**SKELETON B — "Substitution and simplification" paragraph**
   SKELETON: "Substituting [new variable] = [old expression] so [old differential] = [new differential expressed], [integrand in old variable] = [integrand rewritten] = [intermediate expanded form] = [split sum/integrand]."

   1. **Slot 1**: A gerund clause ("Substituting 𝑢 = …") with a "so" clause giving the differential equivalence.
   2. **Slot 2**: A chain of equals-signs (3–4 stages) where each stage rewrites the expression in a slightly simpler form, ending with the integrand split into additive pieces.
   3. **HOW to fill**: name a new variable that removes an awkward factor in the integrand. Each "=" step must be a single algebraic/analytic manipulation (rewrite, factorise, split, rearrange). End with two additive terms that can each be integrated by a standard rule.
   4. **Original**: "Substituting 𝑢 = 1−cos𝜃 so d cos 𝜃 = −1/(1−cos𝜃)², [first 𝑢 integral] = −(1/(2𝐴𝑣h))∫(2𝑢−1+1)(2𝑢−1) … d𝑢 = −(1/(2𝐴𝑣h))∫[(2𝑢−1)(2𝑢−1) + (2𝑢−1)] … d𝑢."
   5. **Demonstration fill (different idea)**: "Substituting 𝑡 = ln 𝑦 so d𝑦 = 𝑒^t d𝑡, I = ∫y² ln y d𝑦 = ∫e^{2t}·t·e^t d𝑡 = ∫t·e^{3t} d𝑡 = (1/3)∫t d(e^{3t})."

**SKELETON C — "Evaluate and bound" paragraph**
   SKELETON: "= [constant times the antiderivative bracketed between limits], [bracketed expression evaluated at upper limit − bracketed expression evaluated at lower limit], with the condition [domain restriction in parentheses]."

   1. **Slot 1**: Equals-sign introducing the antiderivative bracketed by the limits.
   2. **Slot 2**: The bracketed expression written out explicitly: an upper-limit term minus a lower-limit term.
   3. **Slot 3**: A parenthetical "(provided …)" stating any positivity/existence condition needed.
   4. **HOW to fill**: pull the standard antiderivative rule for each split piece; write it in a box-bracket evaluated at both limits; attach any positivity condition on constants introduced by the substitution.
   5. **Original**: "= −(1/(4𝐴𝑣h))[(2𝑢−1)/(2𝑣h^{+1/2}) + (2𝑢−1)/(2𝑣h^{−1/2})] evaluated at 1−cos𝜃₀, … (provided 2𝑣h^{+1/2} > 0) (9)."
   6. **Demonstration fill (different idea)**: "= (1/3)[t·e^{3t} − (1/3)e^{3t}] from 0 to ln 2, = (1/3)[(ln 2)·8 − (1/3)·7 − 0] (provided e^{3t} converges)."

**SKELETON D — "Back-substitute and collapse" paragraph**
   SKELETON: "Substituting in [prior equation number], [big substituted expression] = [simplified form 1] = [simplified form 2] = … = [closed-form final expression labelled (n)]."

   1. **Slot 1**: A clause referencing a previously numbered equation ("Substituting in Equation 8,").
   2. **Slot 2**: A chain of equals-signs (3–6 stages) where each stage cancels one factor or combines two fractions.
   3. **Slot 3**: A boxed/tagged final expression with a new equation number.
   4. **HOW to fill**: identify which prior equation contains the symbol whose explicit form you now have; write the substituted version once fully; perform a sequence of single algebraic manipulations (factor cancellation, combining fractions) one per "=" sign; end with a clean closed form labelled with a fresh equation number.
   5. **Original**: "Substituting in Equation 8, [D₀(1−cos𝜃₀)²/(4(1−cos𝜃₀)^{−1}·2𝑣h^{−1/2})·(…) ] = D₀·[(1−cos𝜃₀)^{−1}/(2𝑣h^{+1/2}) + …] = D₀(1+cos𝜃₀)/(2𝑣r+2𝑣h) + … = D₀(𝑣r² − 𝑣h² cos²𝜃₀)/(𝑣r² − 𝑣h²) (10)."
   6. **Demonstration fill (different idea)**: "Substituting in Equation 4, (1/2)mv²·(m+M/M) = (1/2)m(2v₀/(1+m/M))²·(m+M/M) = … = (m²/(m+M))·v₀² (5)."

## Express-Idea Vocabulary

**Sequencing / closing-prior-step**
- "Thus we have derived an expression" — verdict-verb that announces the next move is evaluation.

**Mechanism verbs (calculation actions)**
- "Evaluating the integral," — names the immediate action.
- "Substituting 𝑢 = 1−cos𝜃" — introduces a change of variable.
- "Substituting in Equation 8," — names a back-substitution referencing a numbered prior result.

**Cause / justification connectives**
- "so d cos 𝜃 = −1/(1−cos𝜃)²" — the "so" clause justifies the differential rewrite that makes the substitution valid.

**Specification / targeting**
- "Evaluating the integral," — specifies *which* operation is about to be performed.

**Condition / domain qualifier**
- "(provided 2𝑣h^{+1/2} > 0)" — attaches a domain constraint as a parenthetical rider to a result.

**Closure / labelling**
- "(9)" and "(10)" — equation tags used to anchor the result for later cross-reference.

## How to Explain an Idea (replication steps)

This section uses the **worked calculation** pattern: *evaluate → substitute → manipulate → bound → back-substitute → simplify*. To replicate:

1. **Close the prior step with a verdict sentence** ("Thus we have derived … as required.") — signals the reader that the boxed expression is now fixed and ready to be processed.
2. **Name the operation** with a gerund ("Evaluating the integral,") — tells the reader what kind of work is on the page.
3. **Display the unevaluated form** with limits and integrand exactly as it stands.
4. **Rewrite the integrand** once with a small algebraic rearrangement so a substitution becomes visible.
5. **State the substitution** ("Substituting 𝑢 = …, so … = …") — define both the new variable *and* the differential equivalence, because the reader needs the chain rule applied.
6. **Apply the substitution** by rewriting the entire integral in the new variable; show the same equals-sign chain step if the new integrand still needs splitting.
7. **Split / factorise** the integrand into additive pieces each integrable by a single rule, so that the next step is obvious.
8. **Integrate term-by-term**, writing the antiderivative in a bracket.
9. **Apply the bounds** by writing the bracket evaluated at upper minus lower, attaching as a rider any positivity/existence condition that the substitution introduced.
10. **Reference an earlier equation** ("Substituting in Equation X,") — signal the reader that the boxed result must be inserted into the master formula.
11. **Show the substituted master formula** in full, then perform a *visible* chain of algebraic cancellations, one per "=" sign, so the reader can audit each cancellation.
12. **Land on the closed-form result** with a fresh equation number — this is the section's verdict.
