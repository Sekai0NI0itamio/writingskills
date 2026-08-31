# Idea Flow Notes: physics_6_may2021_JHIe4BqHyawhzV8F — UNCERTAINTIES

## Paragraph Flow (move by move)

**Paragraph 1** (intent + variables + starting formula)

- **Move 1 — claim of intent:** "We will calculate the error of μd using the method of propagation of errors" → announces the goal (finding the uncertainty of μd) and names the method. Hands the reader to the next move because **specification** is required — which variables will carry that error.
- **Move 2 — evidence listing:** "m1 = m1 ± Δm… s = s ± Δs" (bullet list) → enumerates each measured quantity and its symbol for uncertainty. Hands the reader to the formula because **only with the symbols defined** can the algebra be read.
- **Move 3 — formula definition:** "a = v² / 2s" → states the working equation for *a*. Hands the reader to the propagation step because this formula is what must now be differentiated.

**Paragraph 2** (partial-derivative expansion of Δa)

- **Move 1 — mechanism (partial derivatives written in long form):** "d/dv (v²/2s) Δv + d/ds (v²/2s) Δs" → applies the propagation rule to *a*. Hands the reader to simplification because the reader cannot yet use the unsimplified expression.
- **Move 2 — repeat / restatement:** the same expression repeated verbatim (likely a transcription artifact) → redundant move that re-anchors the reader before simplification.
- **Move 3 — verdict (simplified form):** "Δa = (v/s) Δv + (v²/2s²) Δs" → collapses the partial derivatives into a usable form. Hands the reader to μd because the same operation must now be applied to a more complex quotient.

**Paragraph 3** (μd and its error)

- **Move 1 — formula definition:** "μd = (m2·g − a(m1+m2)) / (m1·g)" → states the quotient that must now be propagated. Hands the reader to the next move because the formula alone does not give its uncertainty.
- **Move 2 — mechanism (full partial-derivative expansion):** "d/da (…) Δa + d/dm1 (…) Δm1 + d/dm2 (…) Δm2" → sets out three terms, one per variable. Hands the reader to simplification because the expression is too unwieldy to compute directly.
- **Move 3 — verdict (simplified form):** "Δμd = ((m1+m2)/(m1·g)) Δa + …" → collapses each term. Hands the reader to the **Example** because abstract symbols must be replaced by numbers for the calculation to mean anything.

**Paragraph 4** (numerical example — header)

- **Move 1 — transition header:** "Example:" → signals a switch from symbolic to numerical working. Hands the reader to substitution because a specific value must now be chosen.
- **Move 2 — specification:** "For the value of v = 1.73 m/s" → fixes one variable and gives its unit. Hands the reader to substitution into the *a* formula because all symbols must be quantified.
- **Move 3 — example calculation of *a*:** "a = 1.73²/(2×0.65) = 2.30" → demonstrates the formula numerically. Hands the reader to the Δa line because once *a* is known, its uncertainty can be computed.

**Paragraph 5** (numerical Δa)

- **Move 1 — substitution into simplified Δa:** "Δa = (1.73/0.65)×0.005 + (1.73²/(2×0.65²))×0.005" → plugs values into the previously simplified expression. Hands the reader to arithmetic because the symbols must collapse into numbers.
- **Move 2 — verdict (numerical Δa):** "Δa = 0.01330 + 0.017709" → "Δa = 0.03101" → arrives at a single number. Hands the reader to Δμd because this Δa is the input the next propagation needs.

**Paragraph 6** (numerical Δμd, truncated)

- **Move 1 — substitution into Δμd:** "Δμd = ((m1+m2)/(m1·g)) Δa + ((g−a)/(m1·g)) Δm2 + (a·m1/(m1²·g)) Δm1" → plugs every term with the numbers carried over from Paragraph 5. The section **ends mid-calculation**, leaving the final verdict to be continued; the hand-off to a final sum is implicit.

## What This Section Does (content sequence)

This Uncertainties section makes the following ordered content moves:

1. **State intent and method** — declares that propagation of errors will be used, and names the target quantity (μd). Sets up why every symbol that follows matters.
2. **Catalogue measured variables with uncertainties** — lists each symbol and its Δ-symbol. Sets up which letters the algebra will manipulate.
3. **State the algebraic formulas that will be propagated** (in order of dependency: *a* first, then μd). Sets up the chain in which each derived quantity feeds the next.
4. **Apply propagation by writing out all partial-derivative terms** — long form, one per independent variable. Sets up simplification by making every contribution explicit.
5. **Simplify each partial-derivative expression into a single line** — converts calculus notation into algebra the reader can substitute numbers into. Sets up the worked example.
6. **Introduce "Example:"** — signals the switch from symbols to numbers.
7. **Pick one numerical value (here v = 1.73 m/s) and work forward through every formula** — computes *a*, then Δa, then begins Δμd. The order is forced by data dependencies: each result is the input of the next.

Why that order: **dependency chain**. Each propagated quantity (Δa) requires the previous formula's result (*a*), which itself requires the numerical inputs. So the section flows intent → symbols → formulas → calculus → simplification → numerical cascade.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Intent + variable catalogue + anchor formula"** (Paragraph 1)

   SKELETON: "We will calculate the error of [Y] using the method of propagation of errors. [bullet list of Xᵢ = Xᵢ ± ΔXᵢ]. [anchor formula relating Y to one variable]."

1. **What each slot holds (grammatical shape):**
   - Slot 1: future-tense clause naming the target quantity Y.
   - Slot 2: bulleted list; each line is *symbol = symbol ± Δsymbol*.
   - Slot 3: displayed equation defining Y in terms of a small subset of the variables.
2. **HOW to fill with a different idea:** slot 1 — name the final quantity whose uncertainty you want (e.g. period of a pendulum T); slot 2 — list every measured variable in the experiment with its uncertainty symbol; slot 3 — write the simplest sub-formula (e.g. T = 2π√(L/g)) that will be propagated first.
3. **Original filled version:** "We will calculate the error of μd using the method of propagation of errors. m1 = m1 ± Δm … s = s ± Δs. a = v²/2s."
4. **Demonstration fill (different idea):** "We will calculate the error of T using the method of propagation of errors. L = L ± ΔL; g = g ± Δg; π = π ± 0 (constant). T = 2π√(L/g)."

**SKELETON B — "Long-form partial derivatives → simplified line"** (Paragraphs 2 and 3)

   SKELETON: "ΔY = d/dX₁ (formula) ΔX₁ + d/dX₂ (formula) ΔX₂ [repeat for n variables]. [same expression repeated for clarity]. ΔY = [simplified algebraic form]."

1. **What each slot holds:** first line is the chain rule applied term-by-term; second line is a restatement (often identical, signalling an unpacking pause); third line is the result of carrying out each derivative.
2. **HOW to fill with a different idea:** slot 1 — write the propagation rule sum, one partial derivative per variable appearing in the formula; slot 2 — restate to anchor; slot 3 — compute each derivative symbolically and write the simplified expression on one line.
3. **Original filled version:** "Δa = d/dv (v²/2s) Δv + d/ds (v²/2s) Δs. Δa = (v/s) Δv + (v²/2s²) Δs."
4. **Demonstration fill:** "ΔT = d/dL (2π√(L/g)) ΔL + d/dg (2π√(L/g)) Δg. ΔT = (π/√(Lg)) ΔL + (−π√L / g√g) Δg."

**SKELETON C — "Header + pick a value + substitute"** (Paragraph 4)

   SKELETON: "Example: For the value of X₁ = [number] [unit], formula = [substituted expression] = [numerical result]."

1. **What each slot holds:** label word ("Example:"), a "For the value of" clause fixing one variable, then a displayed equation showing the substitution and the computed number.
2. **HOW to fill with a different idea:** slot 1 — write "Example:"; slot 2 — pick one numerical measurement from your data table; slot 3 — substitute every symbol with its number and show the arithmetic.
3. **Original filled version:** "Example: For the value of v = 1.73 m/s, a = 1.73²/(2×0.65) = 2.30."
4. **Demonstration fill:** "Example: For the value of L = 0.85 m, T = 2π√(0.85/9.81) = 1.85 s."

## Express-Idea Vocabulary

- **Sequencing / forward motion:** "as shown in the following" — opens the section and points the reader to the work ahead.
- **Causation / consequence:** "using the method of propagation of errors" — names the technique whose mechanics will produce the answer.
- **Specification / narrowing:** "For the value of v = 1.73 m/s" — pins one variable to one number so the algebra becomes arithmetic.
- **Definition verbs:** no explicit "defined as" appears; quantities are introduced by display equation alone (e.g. "a = v²/2s" acts as an implicit definition).
- **Mechanism verbs (calculus):** "d/dv (v²/2s) Δv + d/ds (v²/2s) Δs" — performs the partial-derivative step that *is* the propagation of errors.
- **Verdict / collapse verbs:** the equals sign is the only such marker; "Δa = 0.01330 + 0.017709" → "Δa = 0.03101" is the final collapse of a sum into a single number.
- **Transition / section markers:** "Example:" — the single explicit signal that switches from symbolic to numerical work.

## How to Explain an Idea (replication steps)

The pattern this section relies on is **formula chain → calculus expansion → algebraic simplification → numerical substitution → numerical verdict** (a worked calculation pattern, with dependency chaining between quantities).

Step-by-step to explain a NEW idea the same way:

1. **Open with intent + method.** State the final quantity whose uncertainty you want and name propagation of errors as the tool (e.g. "We will calculate the error of T…").
2. **Catalogue every measured variable** as *symbol = symbol ± Δsymbol* in a bullet list, so the reader sees the inputs.
3. **Write the anchor formula** for the simplest sub-quantity that the final quantity depends on (here *a* before μd).
4. **Apply the propagation rule in long form** — write one partial derivative per independent variable, each multiplied by the corresponding Δ. Do **not** simplify yet.
5. **Simplify** the long expression into a single line of algebra so it is ready to take numbers.
6. **Move to the next, more complex formula** in the dependency chain (here μd) and repeat steps 3–5 for it.
7. **Label an "Example:" section** and pick one numerical measurement (the variable whose value will anchor the worked calculation).
8. **Substitute numbers into the simplest formula** and compute its value.
9. **Substitute numbers into the corresponding Δ-formula**, then **collapse each term into a single number**, and finally **sum the terms** to a verdict (Δa = 0.03101, etc.).
10. **Feed that verdict into the next Δ-formula** in the chain (Δμd), repeating step 9 until the final uncertainty is reached.
