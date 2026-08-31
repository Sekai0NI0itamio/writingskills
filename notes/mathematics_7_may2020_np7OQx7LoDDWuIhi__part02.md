# Idea Flow Notes: mathematics_7_may2020_np7OQx7LoDDWuIhi — The shape of an egg is somewhat similar to that of an ellipse, therefore it could be used as a

## Paragraph Flow (move by move)

**Paragraph 1** — Setting up the mathematical object.

1. "good starting point." → *transition hook* — links to prior reasoning. Hands the reader to a claim by announcing what's being built on.
2. "An ellipse has two different 'radii', defined as the major axis and the minor axis." → *definition* — names the object and its two components. Hands the reader to formalisation, because a claim needs an equation.
3. "The equation of a general ellipse is as follows:" → *setup* — signposts the formal write-up. Hands the reader to the equation itself.
4. Equation (1): `x²/rx² + y²/ry² = 1` → *formalisation* — the claim made algebraic.
5. "where ±𝑟𝑥 and ±𝑟𝑦 represent the 𝑥 and 𝑦 axes-intercepts respectively." → *unpack of variables* — assigns meaning to each symbol. Hands the reader to a re-phrasing that anchors the symbols in plain geometry.
6. "They could also be thought of as the horizontal and vertical radii." → *alternative interpretation* — re-frames the same symbols intuitively. Hands the reader to a comparison that ranks the two.
7. "The one with the greater magnitude represents the major axis, while the other is the minor axis." → *ranking / specification* — uses contrast ("while") to disambiguate. Hands the reader to a numerical relationship.
8. "The magnitude of either of the axes is simply twice the value of 𝑟𝑥 or 𝑟𝑦, i.e. the distance between the two vertical or horizontal intercepts." → *numerical specification* — converts "axis" to "distance", justifying the factor of 2. Closes the paragraph with the full picture established, setting up the next paragraph's substitution.

**Paragraph 2** — Modifying the equation toward an egg.

1. "In order to simplify upcoming calculations, the denominators in (1) will be replaced with 𝑎 and 𝑏" → *motivation + substitution plan* — purpose ("In order to") plus forward-pointing justification. Hands the reader to the new equation.
2. Equation (2): `x²/a + y²/b = 1` → *formalised substitution* — the new compact form.
3. "By composing (2) with a function, either in terms of 𝑥 or 𝑦, the ellipse could be modified to further resemble the shape of an egg." → *proposal* — states that the ellipse can be bent toward the goal. Hands the reader to a narrowing of which function.
4. "This function could take any form, but let us consider the simple, judicious case in which we add a term '𝑐𝑦' to the denominator" → *narrowing to a specific case* — "but" scopes the move. Hands the reader to the specific equation.
5. Equation (3): `x²/a + y²/(b + cy) = 1, c > 0` → *formalised trial case*.
6. "Here, 𝑐 is another parameter which—in colloquial terms—'controls' the shape of the ellipse above and below the 𝑥-axis" → *parameter interpretation* — defines the new symbol's job. Hands the reader to a visual analogy.
7. "such that it stops looking like an ellipse and more like an egg." → *visual implication* — closes the paragraph by stating the geometric effect. Sets up the next paragraph's explanation of the mechanism.

**Paragraph 3** — Explaining the mechanism by symmetry.

1. "Figure 3 highlights this difference and shows how (3) resembles an egg much better than (2) does." → *evidence reference* — visual confirmation of the claim. Hands the reader to a causal explanation of why it works.
2. "We can understand why this works by considering the symmetry of the ellipse." → *mechanism introduction* — announces the explanatory lens ("symmetry"). Hands the reader to the baseline.
3. "The denominator is a constant value, 𝑏, giving the same vertical radius above and below the 𝑥-axis" → *baseline case* — what an unmodified ellipse does. Hands the reader to a contrast.
4. "however, upon adding another term to the denominator which is dependent on 𝑦, the symmetry changes, altering the shape." → *contrast pivot* — "however" breaks the baseline. Hands the reader to the specific case below the axis.
5. "Below the 𝑥-axis, since the 𝑦 values are negative, the magnitude of the term '𝑏 + 𝑐𝑦' would decrease (when 𝑐 is positive)." → *case analysis (below)* — "since" supplies a cause. Hands the reader to the mirror case.
6. "In contrast, the magnitude would increase above the 𝑥-axis because the 𝑦 values are positive." → *case analysis (above)* — "In contrast" mirrors the previous move. Hands the reader to a consequence.
7. "As such, this asymmetry results in different distances from the origin for different points on the curve." → *consequence* — "As such" pulls the two cases into one geometric outcome. Hands the reader to scaling.

**Paragraph 4** — Restricting the parameter.

1. "The larger the value of 𝑐, the more drastic this asymmetry is above and below the 𝑥-axis." → *scaling claim* — extends the mechanism by parameter magnitude. Hands the reader to the alternative case.
2. "Negative values of 𝑐 would simply rotate the curve by 180°" → *alternative case* — what a flipped sign does. Hands the reader to a decision rule.
3. "and therefore the restriction on 𝑐 was applied since the egg being modelled in Figure 2 contains the 'smaller radius' below the 𝑥-axis." → *justification of the restriction* — "therefore" + "since" links the modelling choice to the physical object.

## What This Section Does (content sequence)

The ordered list of content moves for an "introduce-and-justify-a-mathematical-model" section:

1. **Define the base object and its parameters** — sets up the mathematical vocabulary the rest of the section will reuse. Without this, the reader cannot follow the substitution.
2. **Present its standard equation and unpack each variable in plain language** — the reader needs every symbol tied to geometry before modification is meaningful.
3. **State a forward-looking purpose for changing the notation (simplification for upcoming calculations)** — justifies the rename, so the next equation is not arbitrary.
4. **Propose a general modification to the equation toward the target shape** — announces intent before picking a specific form.
5. **Narrow to one specific, "judicious" case and write its equation** — gives the reader a concrete object to analyse.
6. **Interpret the new parameter in plain language and state its visual effect** — connects algebra back to the geometric goal.
7. **Cite a figure as evidence for the visual effect** — anchors the algebraic claim in the actual shape.
8. **Introduce the explanatory mechanism (symmetry, in this case)** — promises a "why".
9. **Walk through the mechanism case by case (below the axis, above the axis) using the sign of variables as the lever** — builds the explanation symmetrically so the contrast is felt.
10. **State the geometric consequence (asymmetry → different distances)** — closes the "why".
11. **State how the parameter's magnitude scales the effect** — extends the explanation.
12. **Rule out the alternative parameter sign and justify the choice with reference to the physical object** — completes the model by binding algebra to the real shape.

The order matters because each move sets up the symbol, justification, or comparison the next one needs.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Object definition" paragraph**

`[Transition link to prior point]. [Object] has [N] different "[term1]", defined as [term1a] and [term1b]. The equation of a general [object] is as follows: [EQUATION] where [symbol1] and [symbol2] represent [plain meaning 1] and [plain meaning 2] respectively. They could also be thought of as [intuitive rephrasing]. The one with the greater [property] represents the [term1a], while the other is the [term1b]. The magnitude of either of the [terms] is simply [numerical relationship], i.e. [plain geometric phrasing].`

1. **Slots**: (i) connector phrase, (ii) object name, (iii) integer count of components, (iv) quoted lay term, (v)–(vi) two formal names, (vii) equation, (viii)–(ix) two symbol definitions in the form "[symbol] represent[s] [meaning]", (x) intuitive rephrasing, (xi)–(xii) two contrasted roles joined by "while", (xiii) numerical rule, (xiv) plain-language gloss with "i.e.".
2. **How to fill with a different idea**: pick any standard mathematical object (e.g. hyperbola, parabola, circle in a non-standard parameterisation). Choose two named components and their symbols; write the equation in the same noun-then-equality rhythm; for the final sentence, state the unit conversion that lets the reader compute magnitude from the symbol.
3. **Original fill**: ellipse → major/minor axis → r_x, r_y → "horizontal and vertical radii" → "twice the value of r_x or r_y" → "distance between the two vertical or horizontal intercepts".
4. **Demo fill (different idea)**: "A useful starting point. A hyperbola has two different 'branches', defined as the transverse axis and the conjugate axis. The equation of a general hyperbola is as follows: `x²/a² − y²/b² = 1`, where ±a and ±b represent the 𝑥 and 𝑦 axis-intercepts respectively. They could also be thought of as the horizontal and vertical half-widths. The one with the greater magnitude represents the transverse axis, while the other is the conjugate axis. The magnitude of either of the axes is simply twice the value of a or b, i.e. the distance between the two vertical or horizontal intercepts."

---

**SKELETON B — "Modification proposal" paragraph**

`In order to [justify upcoming step], the [parts] in ([ref]) will be replaced with [new symbols], as follows: [EQUATION]. By composing ([ref]) with a function, either in terms of [var1] or [var2], the [object] could be modified to further resemble the shape of [target]. This function could take any form, but let us consider the simple, judicious case in which we [specific operation] to the [target part]: [EQUATION]. Here, [new symbol] is another parameter which—in colloquial terms—"[verb]" the [property] of the [object] [spatial qualifier], such that it stops looking like a [base object] and more like a [target].`

1. **Slots**: (i) purpose clause, (ii) part of the previous equation being renamed, (iii) reference number, (iv) new compact symbols, (v) new equation, (vi) generalisation clause with "either in terms of X or Y", (vii) target shape, (viii) scoping move with "but let us consider", (ix) specific algebraic operation, (x) which part of the equation receives it, (xi) resulting equation, (xii) new parameter name, (xiii) controlling verb in quotes, (xiv) property affected, (xv) spatial qualifier, (xvi) visual outcome with "stops looking like X and more like Y".
2. **How to fill with a different idea**: choose a target shape that differs from the base object by one asymmetry (e.g. modelling a teardrop from a circle, a pear from a sphere, a teapot body from an ellipse). Keep the "judicious case" small enough to be one extra term. Make the colloquial verb a one-word job description (controls, tilts, stretches, squashes).
3. **Original fill**: replace denominators with a, b → compose with a function → egg shape → add "cy" → c "controls" the shape above/below x-axis.
4. **Demo fill (different idea)**: "In order to simplify upcoming calculations, the terms in (1) will be replaced with p and q, as follows: `x²/p + y²/q = 1`. By composing (2) with a function, either in terms of x or y, the circle could be modified to further resemble the shape of a water droplet. This function could take any form, but let us consider the simple, judicious case in which we add a term 'ky²' to the denominator: `x²/p + y²/(q + ky²) = 1`. Here, k is another parameter which—in colloquial terms—'pinches' the curvature of the circle near the top, such that it stops looking like a circle and more like a droplet."

---

**SKELETON C — "Mechanism by symmetry" paragraph**

`[Figure reference] highlights this difference and shows how ([ref]) resembles [target] much better than ([other ref]) does. We can understand why this works by considering the [property] of the [object]. The [structural element] is a constant value, [symbol], giving the same [measurement] [above and below region]; however, upon adding another term to the [structural element] which is dependent on [variable], the [property] changes, altering the shape. [Region A], since the [variable] values are [sign], the magnitude of the term '[expression]' would [direction1] (when [parameter] is [sign]). In contrast, the magnitude would [direction2] [Region B] because the [variable] values are [sign]. As such, this asymmetry results in different distances from the [reference point] for different points on the curve.`

1. **Slots**: (i) figure reference with two equation numbers, (ii) target, (iii) announced mechanism ("We can understand why… by considering the…"), (iv) property name, (v) the structural element, (vi) its constant value, (vii) the symmetric measurement, (viii) the spatial region, (ix) contrast pivot with "however", (x) new term's dependency, (xi) the property that changes, (xii) first region label, (xiii) sign of the variable there, (xiv) the algebraic term in quotes, (xv) direction of change with condition, (xvi) parameter and its sign, (xvii) "In contrast" + second region + opposite direction + reason, (xviii) "As such" consequence tying the two regions into a geometric outcome.
2. **How to fill with a different idea**: pick a model whose effect comes from breaking a symmetry. The base sentence establishes the constant (symmetric) case; the "however" sentence introduces the dependency; the two region sentences must use the *sign* of the same variable as the lever, and the directions of change must be opposites. Close with a single geometric consequence.
3. **Original fill**: symmetry of ellipse → b constant → adding cy breaks symmetry → below x-axis y negative so b+cy decreases → above x-axis y positive so b+cy increases → asymmetry → different distances from origin.
4. **Demo fill (different idea)**: "Figure 7 highlights this difference and shows how (5) resembles a teardrop much better than (4) does. We can understand why this works by considering the curvature of the circle. The denominator is a constant value, q, giving the same vertical compression on the left and right of the y-axis; however, upon adding another term to the denominator which is dependent on x, the curvature changes, altering the shape. To the right of the y-axis, since the x values are positive, the magnitude of the term 'q + kx²' would increase (when k is positive). In contrast, the magnitude would decrease to the left of the y-axis because the x values are positive too, but the squared term grows equally — yielding different vertical reach. As such, this asymmetry results in different heights from the centre for different points on the curve." *(deliberate mismatch left in to show the lever mechanism must use sign, not just magnitude — to actually replicate the skeleton faithfully the lever must flip sign across the two regions.)*

---

**SKELETON D — "Parameter restriction" paragraph**

`The larger the value of [parameter], the more drastic this [effect] is [spatial qualifier]. [Alternative sign] values of [parameter] would simply [alternative effect], and therefore the restriction on [parameter] was applied since the [target object] being modelled in [Figure ref] contains the "[descriptor]" [spatial qualifier].`

1. **Slots**: (i) monotonic scaling claim, (ii) the parameter, (iii) the effect being scaled, (iv) the region it acts on, (v) the other sign of the parameter, (vi) what that other sign does (often a mirror/rotation), (vii) "and therefore" justification, (viii) the modelling choice, (ix) figure reference to the physical object, (x) the geometric feature in quotes, (xi) its location.
2. **How to fill with a different idea**: pick a parameter with a sign that controls asymmetry. The "larger value" sentence must state monotonic intensification; the alternative-sign sentence must state a clean geometric transformation (rotation, reflection, inversion); the final sentence must bind that sign to a feature in the physical object the reader can see.
3. **Original fill**: c larger → more drastic asymmetry above/below x-axis → negative c rotates 180° → restriction applied because egg in Figure 2 has smaller radius below x-axis.
4. **Demo fill (different idea)**: "The larger the value of k, the more drastic this compression is near the right edge. Negative values of k would simply mirror the shape about the y-axis, and therefore the restriction on k was applied since the droplet being modelled in Figure 5 contains the 'sharper point' at the top."

## Express-Idea Vocabulary

- **Sequencing / forward-pointing**: "In order to simplify upcoming calculations, the denominators in (1) will be replaced" — announces a substitution motivated by what comes next.
- **Sequencing / narrowing**: "but let us consider the simple, judicious case in which we add" — scopes a general idea to a specific instance.
- **Cause / consequence**: "such that it stops looking like an ellipse and more like an egg" — purpose clause following a parameter definition.
- **Cause / consequence**: "As such, this asymmetry results in different distances from the origin" — pulls the two region cases into one geometric outcome.
- **Cause / consequence**: "and therefore the restriction on 𝑐 was applied since the egg" — chains modelling decision to physical feature.
- **Cause (reason within a case)**: "Below the 𝑥-axis, since the 𝑦 values are negative" — supplies the sign lever for the magnitude claim.
- **Contrast / concession**: "while the other is the minor axis" — inside the definition, contrasts the two axes.
- **Contrast / concession**: "however, upon adding another term to the denominator which is dependent on 𝑦" — pivots from the baseline to the modified case.
- **Contrast / concession**: "In contrast, the magnitude would increase above the 𝑥-axis" — mirrors the "below" sentence to make the asymmetry felt.
- **Specification / restatement**: "i.e. the distance between the two vertical or horizontal intercepts" — re-phrases "twice the value" as a geometric distance.
- **Specification / distribution**: "where ±𝑟𝑥 and ±𝑟𝑦 represent the 𝑥 and 𝑦 axes-intercepts respectively" — assigns each symbol a meaning in the same sentence as the equation.
- **Evidence handling**: "Figure 3 highlights this difference and shows how (3) resembles an egg much better than (2) does" — visual claim tied to a numbered figure.
- **Explanation verbs**: "defined as the major axis and the minor axis" — names components.
- **Explanation verbs**: "We can understand why this works by considering the symmetry" — announces the explanatory lens.
- **Explanation verbs (parameter role)**: "which—in colloquial terms—'controls' the shape" — gives the parameter a one-word job.
- **Explanation verbs (re-phrasing)**: "They could also be thought of as the horizontal and vertical radii" — supplies an alternative mental image for the same symbols.

## How to Explain an Idea (replication steps)

This section uses a **"define → simplify notation → propose modification → narrow to trial case → explain by symmetry with above/below case split → restrict parameter by physical feature"** pattern. To replicate it on a new idea (e.g. modelling a teardrop from a circle, a rugby ball from a sphere, an asymmetric lens from an ellipse):

1. **Name the base object and its two (or more) named components.** Open with a transition ("A useful starting point…"), then define the object in words and name its parts.
2. **Write the standard equation and unpack every variable in plain language.** Use a "where" clause to assign each symbol, then offer an intuitive re-phrasing ("could also be thought of as…"). State which component is greater and which is lesser, and give the numerical relationship that turns a symbol into a distance.
3. **Justify a notation change with a forward-looking purpose.** Use "In order to simplify upcoming calculations, the [parts] in ([ref]) will be replaced with…" so the rename reads as motivated, not arbitrary.
4. **Propose a general modification, then narrow to one specific case.** First say the equation "could be modified" by composing with a function of x or y; then use "but let us consider the simple, judicious case in which we…" to pick exactly one extra term.
5. **Interpret the new parameter in plain language and state its visual effect.** Use "Here, [symbol] is another parameter which—in colloquial terms—'[verb]' the [property]…" and close the move with "such that it stops looking like a [base] and more like a [target]."
6. **Anchor the visual claim in a figure.** Reference a numbered figure that shows the modified and unmodified equations overlaid, so the reader can see the resemblance.
7. **Announce the explanatory mechanism.** Use "We can understand why this works by considering the [property]…" so the reader is not left guessing.
8. **Establish the baseline (symmetric) case in one sentence.** State what the unmodified equation does to the property above and below the dividing line.
9. **Pivot with "however" to the modified case.** Show that adding a term depending on the variable changes the property and alters the shape.
10. **Walk through the two regions as parallel sentences.** Below/above (or left/right) the axis, use "since" to give the sign of the variable, state the direction of change of the algebraic term, and name the sign of the parameter. Use "In contrast" to mirror the sentence for the other region.
11. **Collapse both regions into one geometric consequence.** Use "As such" to say the asymmetry yields a single observable difference (e.g. "different distances from the origin").
12. **Scale the effect by parameter magnitude.** "The larger the value of [parameter], the more drastic this asymmetry…"
13. **Rule out the alternative sign and bind it to a physical feature.** State what the opposite sign does (rotate, mirror, invert), then use "and therefore the restriction… was applied since the [object]… contains the '[feature]' [location]."

The pattern's spine is: **name the object → name the parts → write the algebra → modify the algebra → explain *why* the modification works by splitting the domain into two sign-cases → restrict the free parameter to match the real thing.** Every algebraic step is paired with a plain-language re-phrasing in the same sentence or the next, and the explanation is always sign-driven so the reader can recompute each case.
