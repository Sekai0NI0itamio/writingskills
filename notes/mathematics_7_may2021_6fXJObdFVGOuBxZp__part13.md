# Idea Flow Notes: mathematics_7_may2021_6fXJObdFVGOuBxZp — Rearranging and simplifying

## Paragraph Flow (move by move)

**Paragraph 1 — The expanded derivative (no sentences, pure equation block).**
This is an equation, not a sentence. It functions as a **state**: it shows the derivative of I(x) already pulled apart into its three summed pieces (the first rational term, the ln H piece, the dk(x)/dx piece). As a state it hands the reader forward by leaving the whole expression "open" — the variables k(x) and dk/dx are still symbolic, signalling that a substitution is coming.

**Paragraph 2 — "Subsituting back into I(x)" + new equation.**
- Move 1 (transition/operation): "Subsituting back into I(x)" — names the act of plugging a previously-derived expression into the current formula. The verb ("Subsituting") tells the reader the symbolic letters are about to be replaced, and the phrase "back into" retroactively anchors the reader: this is a return to a formula seen earlier.
- Move 2 (result/state): the resulting dI/dx equation. It hands the reader forward by the **consequence**: the expression now looks like something one would set equal to zero, because it is set up to find a stationary point.

**Paragraph 3 — "Solving for = 0" + equation.**
- Move 1 (operation/goal): "Solving for !" — names the next step.
- Move 2 (specification): "= 0" — pins what the equation equals, converting the goal into a concrete condition.
- Move 3 (result): the resulting ρπ/2 … = 0 expression. The reader is handed forward by an **unresolved element**: the term dk(x)/dx is still inside, so the next paragraph must explain where that comes from.

**Paragraph 4 — "To proceed further from this point, I found the derivative of k(x) via …"**
- Move 1 (transition): "To proceed further from this point" — bridges from the unsolved "= 0" line to the next act.
- Move 2 (need-identification + tool choice): "I found the derivative of 𝑘 𝑥 via" — names both the missing piece (d/dx of k(x)) and the rule that will supply it. This hands the reader forward by **cause**: because the chain rule was chosen, a chain-rule expression must now appear.

**Paragraph 5 — "Subtituding k(x) =" + equation.**
- Move 1 (operation): "Subtituding 𝑘 𝑥 =" — names the substitution (with the same misspelling as earlier, signalling consistent voice).
- Move 2 (result): the rational expression 2x+1/3 · 1/H. The reader is handed forward by **consequence**: with the substitution done, the next paragraph must show what happens when the substitution enters the derivative.

**Paragraph 6 — Resulting derivative dk/dx (equation only).**
A **state** showing dk/dx after substitution. The expression contains a product of two factors (a rational and 1/H), which sets up the reader to anticipate a product rule. The handoff is by **specification**: the shape of the answer tells the reader what rule must be invoked next.

**Paragraph 7 — "Here, I used the product rule. Let u! be … and v! be …"**
- Move 1 (method declaration): "Here, I used the product rule" — retroactively names the rule that produced the form in Paragraph 6, but more importantly forecasts that the next move is to execute that rule.
- Move 2 (decomposition/definition): "Let 𝑢! be … and 𝑣! be …" — splits the product into two named parts. The hand-off is by **mechanism**: once u and v are named, the product rule formula must follow.

**Paragraph 8 — Product rule formula + chain-rule recall.**
- Move 1 (rule statement): "𝑑/𝑑𝑥 [u·v] = …" — states the formula as d/dx(uv) = u·dv/dx + v·du/dx.
- Move 2 (referenced earlier step): "= 𝑢! · dv!/dx + v! · du!/dx" — unpacks the formula using the u and v just defined. The reader is handed forward by **implication**: now the individual du/dx and dv/dx must be filled in, but the section ends here, so the logic path stops at "formula applied, values pending".

## What This Section Does (content sequence)

A rearrangement-and-simplification section of this kind runs through the following ordered moves:

1. **State the current messy form** (show the derivative as already pulled apart). *Sets up:* reader knows what symbols are floating.
2. **Substitute a previously-derived expression back in** ("Subsituting back into I(x)"). *Sets up:* reader is re-anchored to a formula from an earlier section.
3. **Convert the goal into a concrete equation** ("Solving for … = 0"). *Sets up:* the reason for all subsequent algebra is named.
4. **Surface the unresolved sub-expression** ("To proceed further … I found the derivative of k(x) via"). *Sets up:* the reader is told which symbol still blocks progress and which rule will unblock it.
5. **Execute the named rule** (chain-rule substitution). *Sets up:* the substituted form exposes a product.
6. **Identify the next needed rule from the shape of the result** ("Here, I used the product rule"). *Sets up:* reader expects a decomposition.
7. **Decompose the product into named parts** (Let u = …, v = …). *Sets up:* the rule formula can be plugged in.
8. **Write the rule explicitly with u and v** (d/dx(uv) = u·dv/dx + v·du/dx). *Sets up:* a downstream section will plug in numerical du/dx and dv/dx.

The reason this order works: each move exposes the *exact* obstacle (an unknown derivative, a product, a missing substitution) that the next move is designed to remove. The reader is never asked to hold a piece of algebra that is not immediately being acted on.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Back-substitution transition"**
"Substituting [previous-result] back into [main formula], [new-equation]."

1. Slots: slot 1 is a noun phrase naming a previously-derived quantity; slot 2 is the parent formula being re-entered; slot 3 is the rewritten equation.
2. Fill instructions: slot 1 = take an expression you derived one or two sections ago and name it; slot 2 = name the larger formula that originally contained it; slot 3 = write the equation with the new expression in place.
3. Original fill: *"Subsituting back into I(x)"* — k(x) derived earlier is being re-entered into the moment-of-inertia formula.
4. Demonstration fill with a different idea (compound-interest optimisation): *"Substituting back into A(P), the area formula becomes A = (P/4r) + r·√(P/r) − P²/16r² …"* Same skeleton: take a previously-derived expression for P, drop it back into the area function, write the new equation.

**SKELETON B — "Goal-as-equation"**
"Solving for [variable] = 0: [equation set equal to zero]."

1. Slots: slot 1 is the variable you are solving for (a derivative or unknown); slot 2 is the expression now forced to equal zero.
2. Fill instructions: state the variable you want to isolate (often a derivative), then literally set the whole equation to zero to convert "find optimum" into an algebraic target.
3. Original fill: *"Solving for !" / "= 0"* — setting dI/dx to zero to find the stationary point.
4. Demonstration fill (projectile motion): *"Solving for dv/dt = 0:"* followed by the velocity equation set to zero. The skeleton is identical: name the variable, set it to zero, write the equation.

**SKELETON C — "Need-identification with named tool"**
"To proceed further from this point, I found the [quantity] via [named rule]."

1. Slots: slot 1 is the unresolved derivative/expression blocking progress; slot 2 is the calculus or algebraic rule being applied.
2. Fill instructions: name the single derivative that the previous "= 0" equation still contains, then announce the rule you will use on it. Use "via" to mark the tool explicitly.
3. Original fill: *"To proceed further from this point, I found the derivative of k(x) via [chain rule]"*.
4. Demonstration fill (epidemic SIR model): *"To proceed further from this point, I found the derivative of β(t) via the product rule."* Identical rhetorical move: surface the blocker, name the rule.

**SKELETON D — "Method declaration with decomposition"**
"Here, I used [rule]. Let u = [first factor] and v = [second factor], thus [rule's formula with u and v]."

1. Slots: slot 1 is the named calculus rule; slot 2 and slot 3 are the two factors being split out; slot 4 is the rule restated using those factors.
2. Fill instructions: after announcing the rule, label the two factors u and v in the order they appear in the product, then write the rule with those letters substituted in.
3. Original fill: *"Here, I used the product rule. Let u! be … and v! be …, thus d/dx[u·v] = u·dv/dx + v·du/dx."*
4. Demonstration fill (drag-equation optimisation): *"Here, I used the product rule. Let u = v(t) and v = m(t), thus d/dt(u·v) = u·dv/dt + v·du/dt."* Same skeleton: name rule, name parts, restate rule with parts plugged in.

## Express-Idea Vocabulary

**Sequencing / forward motion:** "To proceed further from this point" (P4) — used to bridge from a stalled "= 0" line to the next unblocking step.

**Operation-announcing verbs (the section's workhorses):**
- "Subsituting" (P2, "Subsituting back into I(x)") — announces a back-substitution.
- "Solving for" (P3, "Solving for … = 0") — announces the conversion of a goal into an equation.
- "found the derivative … via" (P4, "I found the derivative of k(x) via [chain rule]") — announces both the missing piece and the tool.
- "Subtituding" (P5, "Subtituding k(x) =") — announces a fresh substitution, consistent with the misspelling in P2.
- "used the product rule" (P7, "Here, I used the product rule") — retrospectively names the rule that produced the form shown.

**Cause / consequence:** "thus" (P7, "thus … = u!·dv!/dx + v!·du!/dx") — marks the formula as a direct consequence of having defined them.

**Specification / location:** "Here" (P7, "Here, I used the product rule") — points the reader to the exact line they are looking at and names the rule that operates on it.

**Definition verbs:** "Let 𝑢! be … and 𝑣! be" (P7) — the standard IB move of naming parts of a product before applying the rule.

**Evidence handling / method authority:** "via [chain rule]" (P4) — uses the calculus rule itself as the warrant for the next step; the authority is the named theorem, not a citation.

## How to Explain an Idea (replication steps)

This section uses the pattern: **state → re-anchor (substitute back) → goal-as-equation → name the obstacle → name the tool → execute the tool → decompose for a second tool → restate the second tool with the decomposition plugged in.**

Step-by-step to replicate this on a NEW idea:

1. **State.** Write the current equation as a single displayed block. Do not narrate it; just present it. (This shows the reader the messy state of affairs.)
2. **Re-anchor.** Begin the next paragraph with "Substituting [previously-derived expression] back into [main formula]". This is how you tell the reader "we are returning to something from earlier."
3. **Convert goal to equation.** Open the next line with "Solving for [variable] = 0". This makes the algebraic target explicit.
4. **Name the obstacle.** Start the next paragraph with "To proceed further from this point, I found the [unresolved quantity] via [rule]". This surfaces the single thing still blocking the algebra and pre-announces the rule.
5. **Execute the first tool.** Write "Substituting [expression] =" and show the result. Use the same misspelling/voice if you want consistency.
6. **Inspect the result for shape.** Do not narrate yet — show the new equation only. The shape (product, quotient, chain) tells the reader what comes next.
7. **Declare the second tool.** Open the next line with "Here, I used [rule]". This retroactively justifies the shape from step 6 and forecasts a decomposition.
8. **Decompose.** Add "Let u = [factor 1] and v = [factor 2]". These labels feed directly into the next line.
9. **Restate the rule.** Write the rule's formula with u and v plugged in. Stop here — the next section will plug in numerical du/dx and dv/dx.
