# Idea Flow Notes: mathematics_7_may2020_uKRa3LH15IKUdk5n — Thus the function for the angle between the tension vector and the x axis that uses relevant sensory data

## Paragraph Flow (move by move)

**Paragraph 1 — Two equivalent angle expressions**

- Move 1: *Present formula (result statement).* Equation "θ = sin⁻¹(−(F_B + F_g)/|T|)" — states the angle as an inverse-sine of a force-sum-over-tension ratio. Hands the reader forward by *leaving the formulation open*, inviting an equivalent form.
- Move 2: *Signal alternative.* "Or:" — names the next expression as an equivalent representation. Hands the reader by *justifying equivalence* before showing it.
- Move 3: *Present alternative formula (restatement).* "θ = cos⁻¹(−R/|T|)" — restates the same angle using a resultant-vector form. Hands the reader forward by *finishing the angle derivation*, so a downstream use of θ is now licensed.

**Paragraph 2 — Substitute θ into the geometry**

- Move 1: *Derive combined function (consequence).* "Thus the function that models the depth of a towfish tethered to an ideal wire is:" — uses "Thus" + a "function that models" framing to *license the substitution* of the previously stated θ into a geometric relation. Hands the reader by *showing the raw combination*, which is still algebraically opaque and so demands simplification.

**Paragraph 3 — Algebraic collapse**

- Move 1: *Simplify (mechanism).* "Which can be simplified to:" — uses "simplified to" as a *signpost that an identity has been applied* (sin(sin⁻¹(x)) = x). Hands the reader forward because *the symbol −(F_B + F_g) is still abstract* and must be unpacked before it can be used.

**Paragraph 4 — Expand abstract vectors into physical quantities**

- Move 1: *Expand (substitution).* "Which in expanded form is:" — uses "expanded form" as a *signpost that abstract vectors will be replaced by measurable physical terms* (gravity, volume, density, drag, area, velocity, mass). Hands the reader forward because *the symbols just introduced carry no meaning until defined*.

**Paragraph 5 — Define every variable in one sweep**

- Move 1: *Define variables (terminology list).* "Where D is the depth of the towfish, l is the length of the wire, g⃗ is gravitational acceleration…" — a single run-on sentence whose "Where" clause performs a *terminal-definition move*, closing the symbol-meaning gap created in Paragraph 4. Hands the reader forward because *the function is now usable and can be plotted*.

**Paragraph 6 — Visualise the function**

- Move 1: *Point to evidence (figure reference).* "The function D(v⃗) is shown plotted in figure 5 with parameters set as realistic values (the exact values chosen are unimportant):" — uses "is shown plotted" to *hand the reader off to a graph* and parenthetically downplays parameter choice so the curve's *qualitative shape* carries the argument. Hands the reader forward by *inviting visual inspection* of the plotted curve.

## What This Section Does (content sequence)

This is a **mathematical derivation section**: it walks the reader from an angle statement to a usable, defined, plotted depth function. The sequence is:

1. **Present the derived angle in two equivalent guises.** Two forms (sin⁻¹ and cos⁻¹) of the same θ establish that the angle is fully determined; this is also where the student demonstrates the relation between the force-sum formulation and the resultant-vector formulation.
2. **Combine θ with geometry to produce the target quantity.** Substituting θ into a geometric depth relation (D = l·sin θ) gives a raw, compound expression — the student *announces* it before tidying.
3. **Collapse the compound expression algebraically.** Apply sin(sin⁻¹(x)) = x to remove the nesting and produce a one-line ratio.
4. **Expand abstract vectors into physical scalars.** Replace F_B, F_g, and T with their physical constituents (gravity, volume, density, drag coefficient, area, velocity, mass).
5. **Define every symbol in a single trailing sentence.** A "Where…" clause removes the symbol-meaning ambiguity that the expansion step just introduced.
6. **Plot the function under stated-but-unimportant parameters.** A figure reference closes the derivation by handing the abstract formula to a visual.

The order is dictated by *information dependency*: each step presupposes the prior. The angle must be stated before it can be substituted; the raw substitution must be shown before it can be simplified; the simplified ratio must be expanded before its symbols can be defined; only after definitions is the function usable enough to plot. A student replicating this sequence with a different topic would: state the auxiliary quantity, derive the target by substitution, simplify algebraically, expand physical symbols, define variables, then visualise.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Equivalent-form pairing"**
"[Result expression 1 using variable set A]. Or: [Result expression 2 using variable set B]."

1. **Slots:** Slot 1 = a single named quantity written as a closed-form expression in one set of symbols (noun phrase containing an equation). Slot 2 = the same quantity written using a different but mathematically equivalent variable set, introduced by the connector "Or:".
2. **How to fill with a different idea:** Slot 1: choose a derived quantity (an angle, a probability, a current) and write it in the cleanest form. Slot 2: rewrite the same quantity in a form that uses a *different intermediate variable* (e.g. a resultant vector, a marginal sum, a complex phasor) — the form should be algebraically equal but conceptually distinct.
3. **Original fill:** "θ = sin⁻¹(−(F_B + F_g)/|T|) … Or: θ = cos⁻¹(−R/|T|)."
4. **Demonstration fill (different idea):** "P(X) = Σᵢ P(X | Eᵢ) P(Eᵢ). Or: P(X) = ∫ P(X | E) f(E) dE." (Same total-probability law, one discrete-sum form and one continuous-integral form.)

---

**SKELETON B — "Substitution → simplify → expand"**
"Thus the function that [verb-phrase describing physical meaning] is: [nested expression]. Which can be simplified to: [collapsed expression]. Which in expanded form is: [fully physical expression]."

1. **Slots:** Slot 1 = "Thus the function that [models / computes / describes] [physical phenomenon] is:" followed by a nested compound expression. Slot 2 = "Which can be simplified to:" followed by the same expression with one identity applied (typically an inverse-function pair cancelling). Slot 3 = "Which in expanded form is:" followed by the expression with abstract symbols replaced by measurable physical terms.
2. **How to fill with a different idea:** Pick a measurable quantity whose expression nests an inverse function inside another function (so a cancellation is available). Write the nested form, then apply the identity to cancel, then expand any remaining abstract symbols into their physical constituents.
3. **Original fill:** "Thus the function that models the depth of a towfish … D = l·sin(sin⁻¹(…)) … simplified to: D = l·(…) … expanded form is: D = l·(−g⃗(Vρ − m) / √(½ρC_D A v⃗²)² + (g⃗(Vρ − m))²)."
4. **Demonstration fill (different idea):** "Thus the function that computes the discharge time of an RC circuit is: t = −RC·ln(1 − V_out/V_in). Which can be simplified by letting x = V_out/V_in to: t = RC·ln(1/(1 − x)). Which in expanded form is: t = (R·C)·ln(V_in/(V_in − V_out))." (Same substitution–simplify–expand rhythm, different physics.)

---

**SKELETON C — "Trailing variable definition"**
"Where [var₁] is [definition₁], [var₂] is [definition₂], …, and [var_n] is [definition_n]."

1. **Slots:** A single long sentence beginning with "Where" that *enumerates* every symbol introduced in the immediately preceding equation, each "is" clause giving a brief physical definition in noun-phrase form.
2. **How to fill with a different idea:** After writing an expanded expression, list every distinct symbol that appears in it and supply a one-clause physical definition for each. Keep the list grammatical by using parallel "is" clauses joined by commas, with "and" before the last.
3. **Original fill:** "Where D is the depth of the towfish, l is the length of the wire, g⃗ is gravitational acceleration, V is the volume of the towfish, ρ is the density of water, C_D is the drag coefficient … and m is the mass of the towfish."
4. **Demonstration fill (different idea):** "Where τ is the RC time constant, R is the resistance of the resistor, C is the capacitance of the capacitor, V_in is the supply voltage, V_out is the output voltage across the capacitor, and t is the elapsed time since the switch closed."

---

**SKELETON D — "Plot reference with parameter disclaimer"**
"The function [Y(x⃗)] is shown plotted in figure [N] with parameters set as [category] (the exact values chosen are unimportant): [caption]."

1. **Slots:** A sentence naming the dependent variable as a function of an input vector, naming a figure, naming the *category* of parameter values used, then a parenthetical disclaimer that the precise numbers do not carry the argument, followed by the figure's caption.
2. **How to fill with a different idea:** Identify the independent variable (often a vector) and dependent variable of the derived function. State that the function has been plotted, name a figure, describe the parameter regime qualitatively, and add the disclaimer that the exact numbers are not the point. End with a short caption.
3. **Original fill:** "The function D(v⃗) is shown plotted in figure 5 with parameters set as realistic values (the exact values chosen are unimportant): Figure 5 shows the function D(v)."
4. **Demonstration fill (different idea):** "The function τ(R, C) is shown plotted in figure 3 with parameters set as typical component values (the exact values chosen are unimportant): Figure 3 shows τ as a function of R for three values of C."

## Express-Idea Vocabulary

- **Sequencing / progression:** "Which can be simplified to:" (signals the next equation is algebraically derived); "Which in expanded form is:" (signals the next equation substitutes physical terms).
- **Consequence / derivation:** "Thus the function that models the depth of a towfish tethered" — "Thus" licenses the next equation as a *direct consequence* of the prior angle statements.
- **Alternative / equivalence:** "Or:" — single-word signpost that the next equation is a *re-expression* of the previous one.
- **Specification / definition connector:** "Where D is the depth of the towfish, l is the length" — "Where" introduces a *terminology-resolving* clause.
- **Evidence handling:** "The function D(v⃗) is shown plotted in figure 5" — "is shown plotted" hands the argument off to a *visual artefact* rather than verbal reasoning.
- **Hedging / downplaying:** "the exact values chosen are unimportant" — parentheses-style disclaimer that *removes a potential objection* before it is raised.
- **Explanation verbs / noun-phrase framings:** "function that models the depth of a towfish" (definition-style framing), "is the depth of the towfish … is the length of the wire … is gravitational acceleration" (parallel "is" definers).

## How to Explain an Idea (replication steps)

The section relies on a **derivation chain pattern: state auxiliary result → combine → simplify → expand → define → visualise.** To replicate it for a new idea, follow these numbered steps:

1. **State the auxiliary result twice in equivalent forms.** Open with the cleanest closed-form expression for a sub-quantity (here, the angle θ), then write "Or:" and give a second, *conceptually distinct* expression for the same sub-quantity (here, a resultant-vector form). Two forms both nail down that the sub-quantity is fully determined.
2. **Substitute the sub-quantity into the target relation.** Use a "Thus … function that … is:" sentence to license the substitution. Present the *raw* combined expression, even though it looks nested and ugly — the ugliness is the point, because it sets up step 3.
3. **Apply a cancellation identity and announce it.** Write "Which can be simplified to:" and show the same expression with the nesting collapsed (sin(sin⁻¹(x)) = x, or its analogue). The reader should be able to verify the cancellation by inspection.
4. **Expand abstract vectors/symbols into physical terms.** Write "Which in expanded form is:" and substitute measurable quantities for every abstract symbol (forces → gravity, volume, density, drag, etc.). Do *not* define the symbols yet — that comes next.
5. **Define every symbol in a single trailing sentence.** Open with "Where" and run a parallel list of "[symbol] is [physical definition]" clauses, ending with "and" before the last clause. This removes all symbol-meaning debt in one move.
7. **Hand off to a figure with a parameter disclaimer.** End with "The function Y(x⃗) is shown plotted in figure N with parameters set as [category] (the exact values chosen are unimportant):" followed by the caption. The disclaimer pre-empts the reader asking "why those numbers?" and signals that the *qualitative* behaviour is the argument.

The pattern's strength is that *each step presupposes only the immediately prior one*, so the reader is never asked to hold two unpinned claims at once.
