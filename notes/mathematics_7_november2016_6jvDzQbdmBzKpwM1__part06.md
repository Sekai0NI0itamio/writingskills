# Idea Flow Notes: mathematics_7_november2016_6jvDzQbdmBzKpwM1 — Expanding and rearranging,

## Paragraph Flow (move by move)

**Paragraph 1 — Equation (1) and rearrangement into a useful form**
- Move 1 — *display initial equation*: "𝐷(𝑡 + Δ𝑡))2 − (𝐷(𝑡))2 = 𝑣h 2 (Δ𝑡)2 − 2𝐷(𝑡)𝑣h Δ𝑡 cos 𝜃(𝑡)" (Equation 1). Hands to the next by *stating the rule that will transform it*.
- Move 2 — *claim of rearrangement*: "− 𝑣r 2 (Δ𝑡)2 − 2𝑣r Δ𝑡𝐷(𝑡 + Δ𝑡)" (terms brought to the right-hand side). Hands to the next by *producing a form where Δt² terms sit together and can be cancelled in the next step*.

**Paragraph 2 — First simplification**
- Move 3 — *operation verb*: "Dividing both sides by Δ𝑡". Hands to the next by *committing to a specific algebraic reduction*.
- Move 4 — *display result*: shows each term reduced by one power of Δt. Hands to the next by *setting up a limit, since Δt now appears linearly*.

**Paragraph 3 — Taking the limit**
- Move 5 — *operation verb*: "Taking the limit as Δ𝑡 → 0". Hands to the next by *forcing the Δt terms to vanish, which exposes a derivative*.
- Move 6 — *display limit result*: the surviving terms, with Δt now absent from denominators. Hands to the next by *the surviving left-hand side now visibly matches the form of a derivative*.

**Paragraph 4 — Justify, substitute, simplify, label**
- Move 7 — *definition/assumption*: "Since 𝐷(𝑡) is assumed to be differentiable at 𝑡". Hands to the next by *granting permission to invoke the derivative definition*.
- Move 8 — *identification by definition*: "the left-hand side is simply d𝑡d 𝐷2". Hands to the next by *naming the limit as a derivative so it can be manipulated symbolically*.
- Move 9 — *operation verb + substitution*: "Applying the power rule to the left-hand side" and the resulting line. Hands to the next by *reducing the derivative to first order so D can be divided through*.
- Move 10 — *label and clean form*: "= −𝑣h cos 𝜃 − 𝑣r" (Equation 2). Hands to the next by *signalling one differential equation is complete and another is needed*.

**Paragraph 5 — Second geometric relation with modified angle**
- Move 11 — *callback + modification*: "Returning to Figure 5 and applying the cosine rule again, but using the angle 𝛼 = 180° − 𝜃(𝑡 + Δ𝑡), so cos 𝛼 = − cos 𝜃(𝑡 + Δ𝑡)". Hands to the next by *mirroring the setup of Equation 1 but with a sign-flipped cosine term*.
- Move 12 — *display expanded equation*: Equation (3). Hands to the next by *producing a second equation of the same family, now ready to combine*.

**Paragraph 6 — Combining the two equations**
- Move 13 — *operation verb*: "Adding Equation 1 and Equation 3 together and collecting like terms". Hands to the next by *announcing the strategic reason for the combination*.
- Move 14 — *display simplified sum*: the squared-distance terms cancel, leaving a mixed-product expression. Hands to the next by *revealing a structure that contains a D cos θ term*.

**Paragraph 7 — Divide and rearrange**
- Move 15 — *operation verb*: "Dividing by 2𝑣h Δ𝑡 and rearranging". Hands to the next by *stripping common factors to leave a derivative-ready ratio*.
- Move 16 — *display rearranged form*: "𝐷(𝑡 + Δ𝑡) cos 𝜃(𝑡 + Δ𝑡) − 𝐷(𝑡) cos 𝜃(𝑡) = …". Hands to the next by *mirroring the difference-quotient shape seen earlier*.

**Paragraph 8 — Second limit and recognition**
- Move 17 — *operation verb*: "Dividing by Δ𝑡 and taking the limit as Δ𝑡 → 0". Hands to the next by *promising the same derivative pattern will reappear*.
- Move 18 — *display limit form*. Hands to the next by *making the derivative identification explicit*.
- Move 19 — *identification*: "Once again, the left-hand side corresponds with the first-principles definition of a derivative, d𝑡d 𝐷 cos 𝜃". Hands off by *closing the section on a second named derivative relation, ready for the next derivation step*.

## What This Section Does (content sequence)
The ordered list of moves that an "Expanding and rearranging" section of a mathematical derivation performs:

1. **Display the starting equation** (Equation 1) — sets the algebra to be transformed.
2. **Rearrange terms** so the quantities of interest are grouped — previews which terms will survive a limit.
3. **Divide by the small increment Δt** — lowers the polynomial order so a limit is meaningful.
4. **Take the limit Δt → 0** — kills off vanishing terms, leaving only the structure relevant at the instant.
5. **Invoke a differentiability assumption** — gives permission to identify the limit as a derivative.
6. **Substitute the derivative notation** and **apply standard rules (e.g. power rule)** — cleans the equation into its most usable form.
7. **Label the result** (Equation 2) — checkpoints the first differential relation.
8. **Return to the original geometric figure** with a *modified angle* — produces a structurally similar second equation (Equation 3).
9. **Add the two equations and collect terms** — engineered so squared-distance terms cancel and a new product structure emerges.
10. **Divide by a common factor and rearrange** — pushes the surviving expression into difference-quotient shape.
11. **Divide by Δt and take the limit again** — confirms the same derivative-identification move works a second time.
12. **Name the second derivative** — checkpoints the second differential relation.

The order matters because each move either *creates the form* the next move needs (Δt² must first be reduced to Δt before a limit) or *creates a parallel relation* that combines with the first to produce a new derivative identity.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Single algebraic operation → resulting equation"**
- Slot 1: Operation verb in gerund/imperative, naming the rule applied to the previous equation.
- Slot 2: The new equation displayed in aligned form, showing every term on the right-hand side.
- Original: "Dividing both sides by Δ𝑡" → resulting equation with each term reduced by one power of Δt.
- Fill with new idea: Take the derivation of relativistic kinetic energy. Slot 1: "Multiplying both sides by 2"; Slot 2: "2KE = 2½mv² − 2mc² + 2mc²/γ", producing the clean energy relation.

**SKELETON B — "Operation → limit → identify as derivative"**
- Slot 1: "Taking the limit as Δ𝑡 → 0" or analogous limit statement.
- Slot 2: The limit form with surviving terms displayed.
- Slot 3: A sentence that names the surviving expression as a derivative, citing the first-principles definition.
- Original: "Taking the limit as Δ𝑡 → 0" → limit equation → "the left-hand side is simply d𝑡d 𝐷2".
- Fill with new idea: Deriving the heat equation from Fourier's law. Slot 1: "Taking the limit as Δx → 0"; Slot 2: limit of the flux difference quotient; Slot 3: "the left-hand side is simply ∂Q/∂x, the heat flux gradient".

**SKELETON C — "Callback to original figure + modified angle → second equation"**
- Slot 1: "Returning to [Figure X] and applying [rule] again, but using [modified parameter]".
- Slot 2: Display of the new expanded equation mirroring the first.
- Original: "Returning to Figure 5 and applying the cosine rule again, but using the angle 𝛼 = 180° − 𝜃(𝑡 + Δ𝑡), so cos 𝛼 = − cos 𝜃(𝑡 + Δ𝑡)" → Equation 3.
- Fill with new idea: Resolving forces on a block on two inclines. Slot 1: "Returning to Figure 2 and resolving forces again, but now along the y-axis of the second incline"; Slot 2: the y-component equation.

**SKELETON D — "Combine → cancel → simplify → rearrange → identify"**
- Slot 1: "Adding [Eq A] and [Eq B] together and collecting like terms".
- Slot 2: Combined equation with cancellation noted.
- Slot 3: "Dividing by [common factor] and rearranging".
- Slot 4: Clean expression named as a derivative.
- Original: "Adding Equation 1 and Equation 3 together and collecting like terms" → sum → "Dividing by 2𝑣h Δ𝑡 and rearranging" → "d𝑡d 𝐷 cos 𝜃".
- Fill with new idea: Deriving wave speed from two linearised momentum equations. Slot 1: "Adding the linearised momentum equations for the two media"; Slot 2: sum with the linear terms cancelling; Slot 3: "Dividing by 2ρA and rearranging"; Slot 4: "∂p/∂t = −ρc² ∂u/∂x".

## Express-Idea Vocabulary

**Sequencing / operation verbs** — name what is being done to the equation
- "Dividing both sides by Δ𝑡" — gerund operation statement
- "Taking the limit as Δ𝑡 → 0" — gerund operation statement
- "Applying the power rule to the left-hand side" — gerund + identification of what is operated on
- "Adding Equation 1 and Equation 3 together and collecting like terms" — chained gerund operations
- "Dividing by 2𝑣h Δ𝑡 and rearranging" — chained gerund operations

**Cause / justification / permission moves**
- "Since 𝐷(𝑡) is assumed to be differentiable at 𝑡" — assumption that licenses the next step
- "from the first-principles definition of the derivative" — authority cited for the identification
- "so cos 𝛼 = − cos 𝜃(𝑡 + Δ𝑡)" — direct consequence stated as "so"

**Specification / identity statements**
- "the left-hand side is simply d𝑡d 𝐷2" — naming what the expression *is*
- "Once again, the left-hand side corresponds with" — pattern-match cue
- "Returning to Figure 5 and applying the cosine rule again, but using the angle" — callback + modification

**Contrast / repetition cues**
- "but using the angle 𝛼 = 180° − 𝜃(𝑡 + Δ𝑡)" — *but* marks the deliberate change
- "Once again, the left-hand side corresponds" — *once again* signals a parallel argument is being repeated

## How to Explain an Idea (replication steps)

The explanation pattern this section relies on is **algebraic manipulation engineered to expose a derivative structure, then system-building by combining two geometric relations to extract a second derivative**. To replicate it:

1. **Display the starting equation** obtained from a geometric or physical law (e.g. the cosine rule, Newton's law). State it on its own line, numbered.
2. **Rearrange terms** so the expressions you want to take a limit of sit on one side. Do not yet divide — just rearrange.
3. **Divide by the small increment** (Δt, Δx, etc.) using a gerund sentence ("Dividing both sides by Δt"). Display the reduced equation.
4. **Take the limit** as the increment → 0 in a separate gerund sentence. Display the surviving terms.
5. **Justify** the move with a "since" clause that names an assumption (differentiability, smoothness) — this is what licenses the identification.
6. **Identify** the surviving limit as a derivative using the first-principles definition, citing the definition explicitly.
7. **Apply a standard rule** (power rule, product rule) to simplify the derivative expression.
8. **Label the clean result** as a numbered output (Equation 2).
9. **Return to the original diagram** with a *modified* parameter (a different angle, a different axis), signalled by "Returning to Figure X … but using …". Display the new expanded equation as Equation 3.
10. **Combine** Equation 1 and Equation 3 with a gerund ("Adding Equation 1 and Equation 3 together and collecting like terms"). Display the cancellation explicitly.
12. **Divide by a common factor and rearrange**, again as a gerund sentence, to push the expression into difference-quotient shape.
13. **Take the limit a second time** with "Dividing by Δt and taking the limit as Δt → 0".
14. **Name the second derivative** ("Once again, the left-hand side corresponds with …"), using "once again" to flag the parallel structure.
