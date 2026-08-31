# Idea Flow Notes: mathematics_7_november2016_6jvDzQbdmBzKpwM1 — Raising both sides to base e and rearranging,

## Paragraph Flow (move by move)

**Paragraph 1 — Algebraic simplification to Equation 7**
- S1 [claim/result]: "𝑒ˡⁿ ᴰ⁺ᶜ² = 𝑒^(...)" — re-expresses the integrated form by exponentiating. *Hands reader to:* the next step because exponentiation alone doesn't isolate D yet.
- S2 [unpack]: "𝐷e^𝑐² = 𝑒^((𝑣ᵣ/2𝑣ₕ) ln(1+cos θ)...)" — distributes the exponent across both terms. *Hands reader to:* the next sentence because e^𝑐² is still attached to D.
- S3 [unpack/final form]: "𝐴𝐷 = ((1+cos θ)/...)^(...)" — declares e^𝑐² = 𝐴 and writes the closed-form ratio, labelled "(7)". *Hands reader to:* the next paragraph because this equation is now ready to be evaluated at a specific condition.

**Paragraph 2 — Boundary condition when D = 0**
- S4 [context/motivation]: "Now, as we wish to find the time 𝑡 = 𝑘" — names the *purpose* of the next move. *Hands reader to:* the substitution by defining what D = 0 represents.
- S5 [definition of the condition]: "when 𝐷 = 0, the value of cos 𝜃 at this time, cos 𝜃ₖ" — defines the variable to be solved. *Hands reader to:* the algebra by restating the target symbolically.
- S6 [evidence — substitute]: "can be solved for by substituting 𝐷 = 0 into Equation 7" — names the procedure. *Hands reader to:* the equation on the next line.
- S7 [unpack]: "0 = (1+cos θₖ)/(1−cos θₖ)^(...)" — shows the substituted form. *Hands reader to:* the numerator analysis.
- S8 [deduction]: "0 = 1 + cos θₖ" — collapses the denominator power. *Hands reader to:* the final solve.
- S9 [verdict]: "cos θₖ = −1" — the result. *Hands reader to:* the next paragraph because a second unknown (A) still remains.

**Paragraph 3 — Solving for integration constant A**
- S10 [transition + parallel claim]: "Additionally, the constant of integration 𝐴" — pivots to the other unknown. *Hands reader to:* a parallel procedure to S6.
- S11 [evidence — substitute]: "can be solved for by substituting the initial conditions 𝐷₀ and 𝜃₀" — mirrors the wording of S6, signalling symmetry. *Hands reader to:* the next equation.
- S12 [unpack → algebraic chain]: three successive rearrangements culminating in "𝐴 = ... (8)" — each line cancels a term. *Hands reader to:* the next paragraph because Equation 8 completes the parameter set.

**Paragraph 4 — Re-express Equation 7 for D**
- S13 [transition]: "Now writing Equation 7 in terms of 𝐷" — reopens Equation 7 with the A now known. *Hands reader to:* the isolated D.
- S14 [unpack]: "𝐷 = ((1+cos θ)^(...))/𝐴(...)" — D now stands alone on the LHS. *Hands reader to:* the next paragraph because D is ready to plug back.

**Paragraph 5 — Back-substitution into Equation 5**
- S15 [transition]: "Substituting this into Equation 5" — names the move. *Hands reader to:* the long equation that follows.
- S16 [unpack + classification]: "This is now a first-order separable differential equation" — labels what the mess of algebra has produced. *Hands reader to:* the rearrangement that proves separability.

**Paragraph 6 — Separation rearrangement**
- S17 [claim]: "Rearranging, ... 1 = ((1+cos θ)^(...))/𝐴(1−cos θ)^(...)" — moves D to the LHS via the prior equation. *Hands reader to:* factoring.
- S18 [unpack]: "1 = −((1+cos θ)^(...))/𝐴𝑣ₕ(1−cos θ)^(...) · (1−cos θ)(1+cos θ)/(cos²θ−1)" — multiplies numerator and denominator to expose the separability. *Hands reader to:* the simplified form.
- S19 [unpack → terminal form]: "1 = −((1+cos θ)^(...))/𝐴𝑣ₕ(1−cos θ)^(...) · d cos θ/d𝑡" — collapses the algebraic factor, showing dt on its own side. *Hands reader to:* the integration setup.

**Paragraph 7 — Integration setup**
- S20 [context + boundary limits]: "Integrating with respect to 𝑡 from 𝑡 = 0 to 𝑡 = 𝑘" — names the procedure. *Hands reader to:* the limits in θ.
- S21 [specification of limits]: "from cos 𝜃 = cos 𝜃₀ to cos 𝜃 = cos 𝜃ₖ = −1" — closes the loop by invoking the boundary results of paragraphs 2 and 3. *Hands reader to:* the integral expression (cut off, but clearly the next move is to evaluate).

## What This Section Does (content sequence)

A "manipulate-then-substitute-then-solve-for-constants" derivation block. The order is non-arbitrary because each move unlocks the next:

1. **Simplify the integrated form to a clean equation** — strips exponentials and groups constants; without a tidy equation nothing else can be evaluated.
2. **Define the boundary condition of interest** — name *what* you are solving for (here, the angle when D = 0) so the reader knows why the algebra matters.
3. **Solve for the boundary value** — substitute the condition and extract the symbolic answer.
4. **Solve for the remaining constant of integration using initial conditions** — parallel move; only after both unknowns are pinned is the model fully determined.
5. **Re-express the master equation explicitly for the dependent variable** — needed before re-substitution into a parent equation.
6. **Back-substitute into the parent differential equation** — restores the model to a single variable and one derivative.
7. **Identify the resulting equation's class** (here: separable) — signals to the reader the upcoming technique.
8. **Rearrange into separated form** — perform the algebra that realises the named class.
9. **Write the integration with limits** — close the loop by attaching the boundary and initial values already found.

A student replicating this on any separable ODE follows: tidy → evaluate endpoint → evaluate initial → isolate → substitute → name method → rearrange to method form → integrate.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Tidying after exponentiation"**
"SKELETON: [LHS after raising e to both sides] = [RHS fully expanded]. [distribute the constant over each ln term]. [define named constant A = e^𝑐² and present final tidy equation as (n)]."

1. Slot 1: the equality right after exponentiation; equation block. Slot 2: one-sentence algebra step distributing. Slot 3: a definitional sentence introducing a named constant and a labelled equation number.
2. Fill instructions — pick any separable ODE whose integrated form produces ln terms; slot 1 is mechanical (raise e); slot 2 uses distribution; slot 3 introduces a placeholder symbol and assigns it the leftover exponential.
3. Original: "𝑒ˡⁿ ᴰ⁺ᶜ² = ... → 𝐷e^𝑐² = ... → 𝐴𝐷 = ... (7)".
4. Demo (different idea): ∫(1/(x(1−x))) dx = ln|x| − ln|1−x| + c → e^(ln|x|−ln|1−x|+c) = ... → e^c · x/(1−x) = ... define B = e^c, so Bx/(1−x) = F(x) … (3).

**SKELETON B — "Solving a boundary condition by substitution"**
"SKELETON: [Context sentence naming the moment being solved for]. [Procedure sentence: substitute condition into Equation n]. [Equation block showing substitution]. [One-line collapse]. [Verdict: value equals constant]."

1. Slot 1: a purpose clause introduced by "Now" or "To". Slot 2: a "can be solved by substituting" clause naming the equation and condition. Slot 3: substituted equation. Slot 4: simplified numerator/denominator claim. Slot 5: final symbolic answer.
2. Fill instructions — slot 1 names a physical or geometric event; slot 2 states both the equation number and the condition in symbol form; slot 3 is mechanical; slot 4 drops constant factors; slot 5 gives the numerical or symbolic limit.
3. Original: "Now, as we wish to find the time 𝑡 = 𝑘 ... can be solved for by substituting 𝐷 = 0 ... 0 = 1 + cos θₖ → cos θₖ = −1."
4. Demo: "Now, as we wish to find the height at the apex ... can be solved for by substituting dy/dx = 0 into Equation 4 → 0 = 2x − 6 → x = 3."

**SKELETON C — "Solving an integration constant from initial conditions"**
"SKELETON: [Pivot sentence: 'Additionally, [constant] can be solved for']. [Procedure sentence naming initial conditions]. [Equation block with substituted values]. [Chain of cancellations]. [Labelled final equation]."

1. Slot 1: parallel pivot adverb ("Additionally", "Similarly"). Slot 2: identical grammatical shape as the previous paragraph's procedure sentence. Slot 3: substituted equation. Slot 4: algebra chain. Slot 5: equation number.
2. Fill instructions — slot 1 mirrors the opening word of the previous paragraph; slot 2 mirrors its procedure sentence to signal symmetry; slot 3 is mechanical; slot 4 shows each cancellation explicitly; slot 5 assigns a new equation number one higher than the previous.
3. Original: "Additionally, the constant of integration 𝐴 can be solved for by substituting the initial conditions 𝐷₀ and 𝜃₀ ... 𝐴 = ... (8)."
4. Demo: "Similarly, the constant of integration C can be solved for by substituting the initial conditions (0, 1) ... C = 1 (9)."

**SKELETON D — "Identifying equation class after back-substitution"**
"SKELETON: [Transition sentence: 'Now writing Equation n in terms of [variable]']. [Equation block]. [Transition sentence: 'Substituting this into Equation m']. [Equation block]. [Classification sentence: 'This is now a [type] differential equation']."

1. Slot 1: "Now writing ... in terms of ..." slot 2: variable-isolated equation. Slot 3: "Substituting this into Equation m". Slot 4: large substituted block. Slot 5: "This is now a [type]" naming the technique.
2. Fill instructions — slot 1 reopens the prior tidy equation; slot 2 inverts it; slot 3 names the destination equation; slot 4 is the messy product; slot 5 explicitly labels the form to telegraph the next manipulation.
3. Original: "Now writing Equation 7 in terms of 𝐷 ... Substituting this into Equation 5 ... This is now a first-order separable differential equation."
4. Demo: "Now writing Equation 2 in terms of y' ... Substituting this into Equation 1 ... This is now a first-order linear differential equation."

## Express-Idea Vocabulary

- **Sequencing / transition pivots**: "Now, as we wish to find" (signals a new sub-goal); "Now writing Equation 7 in terms of 𝐷" (re-enters prior work); "Substituting this into Equation 5" (chained substitution); "Additionally" (parallel constant solve); "Rearranging," (algebraic pivot inside a paragraph).
- **Procedure / evidence handling**: "can be solved for by substituting" (used twice — boundary and constant); "Integrating with respect to 𝑡 from 𝑡 = 0 to 𝑡 = 𝑘" (integration with limits).
- **Classification / specification**: "This is now a first-order separable differential equation" — names the technique to set up the next rearrangement; "i.e." — glosses symbols (e.g. "i.e. when 𝐷 = 0", "i.e. from cos 𝜃 = cos 𝜃₀").
- **Definitional / naming moves**: "𝐴 = e^𝑐²" — names a leftover constant; parenthetical equation labels "(7)", "(8)" — anchor for later cross-references.
- **Explanation verbs**: "solved for", "substituting", "Integrating", "Rearranging" — the four operative verbs of the entire section.

## How to Explain an Idea (replication steps)

This section uses the **"tidy → evaluate both anchor points → re-isolate → back-substitute → classify → rearrange to method form → integrate with linked limits"** pattern. To replicate on a new idea:

1. Take the most-recent integrated (or solved) equation and rewrite it in its tidiest equivalent form. Define any leftover constants as named symbols (e.g. 𝐴 = e^𝑐²) and assign it an equation number.
2. State a physical/geometric *moment* you want to find (use "Now, as we wish to find …"). Define it symbolically (e.g. "i.e. when variable = condition").
3. Perform the substitution of that condition into your tidied equation. Display the substituted form, then collapse constant factors on a separate line to reach a clean verdict (e.g. "cos θₖ = −1").
4. Pivot with a parallel adverb ("Additionally" / "Similarly") and solve for the remaining constant using *initial conditions* — mirror the procedure sentence grammar of step 3. Number the new equation one higher.
5. Reopen your tidied equation and isolate the dependent variable on its own (one new line of algebra). Use "Now writing Equation n in terms of [variable]".
6. Announce back-substitution into a parent equation ("Substituting this into Equation m"). Display the resulting expanded form.
7. *Name* what the new equation is in one sentence ("This is now a [type] equation"). This is the only place a reader gets a verbal signpost.
8. Show the algebraic rearrangement that realises the named type, line by line, until the variables are separated.
9. Close by writing the integral with limits, explicitly listing both the *initial* limits and the *boundary* limits you solved in steps 3 and 4 — this binds the whole derivation together.
