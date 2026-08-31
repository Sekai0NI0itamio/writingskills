# Idea Flow Notes: physics_7_may2021_JJ3xLKguAgY9MH8b — 2.2    Deriving the range equation

## Paragraph Flow (move by move)

**Paragraph 1** (the prose lead-in before the derivation)

1. **Context/authority claim** — "Solving for the range in the xα -direction is the same method" → hands to the reader by invoking a known source (Tsokos) so the next sentence can be treated as a standard procedure rather than a novel idea.
2. **Method step + reason** — "The final time is solved from the yα -equation since when the projectile" → hands forward by isolating one variable (time) and stating the *boundary condition* that justifies it, so the next sentence can act on that variable without re-justifying it.
3. **Procedure connector** — "Then this final time is substituted into the xα -equation" → hands forward by naming the next action explicitly; the word "Then" forces the reader into the substitution move that the equations on the page then execute.
4. **Complication/contrast** — "The math is a bit more complicated compared to projectile motion" → hands forward by warning the reader *why* the upcoming algebra is longer than the textbook version, setting the expectation for the multi-line manipulation that follows.

**Paragraph 2** (the equation block, read as a logic chain)

1. **Setup equation (start state)** — sets the yα expression equal to zero, declaring the landing condition.
2. **Simplification move (extraction)** — factors out *t* so the zero solution is visible; this is the "unpack" step, showing the reader what is being cancelled.
3. **Discard step** — "t initial = 0" removes the trivial root so only the physical solution remains.
4. **Solved variable (verdict of step 1)** — produces t final as an explicit function of u, θ, α, g; this is the answer that the previous prose sentence promised would exist.
5. **Transition header** — "Substituting t final into the xα -equation" names the next move, acting as a hinge between the two equation groups.
6. **Substitution move** — replaces *t* in the xα equation with the expression just found.
7. **Algebraic expansion (unpack)** — splits the product into two numerator terms to expose common structure.
8. **Factor-and-group move** — pulls out the squared-time factor, preparing the trigonometric identity.
9. **Identity substitution (mechanism)** — "cos A cos B − sin A sin B = cos (A + B)" is invoked by name so the reader sees the trig collapse as a named operation, not a trick.
10. **Final cancellation (verdict)** — (α + (θ − α)) collapses to θ, delivering the final neat range equation.

---

## What This Section Does (content sequence)

For a *derivation of a range equation* the logical order is:

1. **Anchor to a known method** — say whose approach you are following and on which page, so the reader does not need the original in front of them.
2. **State the strategy** — name the *two* kinematic equations involved and which variable links them.
3. **Explain the boundary condition** — give the physical reason a particular quantity is set to zero (landing ⇒ y = 0).
4. **Flag the extra difficulty** — tell the reader *why* this derivation will take more lines than the flat-ground one, so the algebra does not look like padding.
5. **Set the first equation to that boundary condition** — write the full y(t) expression equal to zero.
6. **Solve that equation step by step** — show every algebraic move; the IB marker must see the manipulation, not just the result.
7. **Discard the trivial root explicitly** — label t_initial = 0 so the reader sees you chose the correct branch.
8. **Announce the substitution** — a one-line header that hands the reader into the next equation, mirroring the prose hand-off used earlier.
9. **Perform the substitution and expand** — put the expression for t in, then multiply out so the structure is visible.
10. **Group terms to reveal an identity** — rearrange the algebra until a recognisable trig identity sits ready to fire.
11. **Name the identity and apply it** — quote the identity by name (e.g. cosA cosB − sinA sinB = cos(A+B)) so the collapse is justified, not magical.
13. **Simplify to the final form** — collapse brackets and cancel, producing the final boxed-style expression.

The order matters because each move only makes sense once the previous one has produced the symbol/structure it needs: you cannot substitute before you have solved, you cannot fire the identity before you have grouped for it, you cannot simplify before the identity has fired.

---

## Paragraph Skeletons (replicable templates)

**Skeleton A — The "strategy + complication" lead-in paragraph**

SKELETON: "[Overall task] is the same method [Authority] uses to [parallel simpler case] ([Citation: p.x]). [Variable A] is solved from [equation 1] since [physical boundary condition makes a quantity zero]. Then [Variable A] is substituted into [equation 2]. The math is [comparative difficulty] compared to [simpler case] as [equation 2] is a [shape of equation] and not a [simpler shape]."

1. *Slot 1 (Authority + parallel case)* — grammatical shape: a present-tense claim with an in-text citation in parentheses. *Fill with new idea:* pick a published source whose worked example is the *non-tilted* version of your problem, then write "[Your derivation] is the same method [Surname] uses to solve [the standard textbook version of your problem] ([Ref: page])."
2. *Slot 2 (Boundary condition)* — grammatical shape: a "since/because" clause giving a physical reason a quantity is zero. *Fill:* state what physically happens at the moment of interest (hits ground, leaves tube, reaches max height) and identify the coordinate that vanishes.
3. *Slot 3 (Substitution connector)* — grammatical shape: a one-clause "Then…" sentence. *Fill:* name the variable that will move from equation 1 into equation 2.
4. *Slot 4 (Complication flag)* — grammatical shape: a contrastive clause beginning "The math is [adj] compared to…" *Fill:* name one structural difference (quadratic vs linear, coupled vs decoupled, non-conservative vs conservative) that will make the algebra longer.

*Original fill:* "Solving for the range in the xα -direction is the same method Tsokos uses to solve for the range in normal projectile motion on horizontal ground (1: p.49-50). The final time is solved from the yα -equation since when the projectile has landed, its yα -position is zero. Then this final time is substituted into the xα -equation. The math is a bit more complicated compared to projectile motion on flat ground as the xα -equation is a quadratic equation of time and not a linear equation."

*Demonstration fill with a different idea (SHM / pendulum period with damping):* "Deriving the period of a lightly damped pendulum is the same method Marion and Thornton use to derive the period of an undamped simple pendulum (2: p.132). The amplitude ratio is solved from the energy equation since when the bob first returns, the restoring force has done one full cycle of work. Then this amplitude ratio is substituted into the SHM equation. The math is somewhat more involved compared to the undamped case as the SHM equation now contains an exponential-decay factor and not a pure sinusoidal one."

---

**Skeleton B — The "named algebraic move" derivation step**

SKELETON: "[Display of rearranged expression]. Substituting in [identity name] [identity in symbols] [display of collapsed expression]."

1. *Slot 1 (Rearranged display)* — an equation line where the previous messy product has been grouped so one known identity is about to fire.
2. *Slot 2 (Identity header)* — present-tense imperative ("Substituting in…") followed by the identity's verbal name.
3. *Slot 3 (Identity symbols)* — the identity written in standard A/B notation so it is searchable.
4. *Slot 4 (Collapsed display)* — the equation re-displayed one line lower with the identity already applied.

*Original fill:* "Substituting in the cosine rule cos A cos B − sin A sin B = cos (A + B) → xα = 2u² sin(θ−α) / g cos²(α) × cos(α + (θ − α)) = 2u² sin(θ−α) / g cos²(α) × cos(θ)."

*Demonstration fill (relativistic momentum derivation):* "Substituting in the hyperbolic identity cosh²x − sinh²x = 1 → p = γm₀v = m₀v / √(1 − v²/c²); squaring both numerator and denominator to expose 1 − v²/c² gives p² = m₀²v² / (1 − v²/c²), which on rearrangement yields p²c² + m₀²c⁴ = E²."

---

**Skeleton C — The "trivial-root discard" line**

SKELETON: "[Display of factored equation]. [Notation for trivial root] = 0. [Notation for kept root] = [expression]."

1. *Slot 1 (Factored form)* — show that the equation factors into two terms multiplied.
2. *Slot 2 (Discard)* — explicitly set the unphysical root to zero so the marker sees you considered it.
3. *Slot 3 (Kept root)* — write the physically meaningful root on its own line so it can be referenced later.

*Original fill:* "t × [u sin(θ−α) − ½ g cos(α) × t] = 0 → t initial = 0 → t final = 2u sin(θ−α) / g cos(α)."

*Demonstration fill (capacitor discharge voltage):* "V(t) × [V₀ − IR(1 − e^(−t/RC))] = 0 → t initial = 0 (capacitor uncharged) → t threshold = −RC ln(1 − V/I R)."

---

## Express-Idea Vocabulary

**Sequencing / procedure**
- "Then this final time is substituted" — names the next algebraic operation before it appears.
- "Substituting t final into the xα -equation" — re-announces a move at the moment it is executed, acting as a hinge between equation groups.

**Cause / consequence / justification**
- "since when the projectile has landed, its yα -position is zero" — ties the algebraic act of setting an expression to zero to a physical event.
- "as the xα -equation is a quadratic equation of time and not a linear equation" — explains *why* the derivation is longer before the reader wonders.

**Contrast / complication**
- "is the same method Tsokos uses to" — sets up an implicit comparison with a standard, simpler case.
- "is a bit more complicated compared to projectile motion on flat ground" — flags the contrast explicitly.
- "and not a linear equation" — closes the contrast with the specific structural reason.

**Specification / identification**
- "the xα -equation" / "the yα -equation" — labels which of two equations is being acted on at each step.
- "t initial = 0" / "t final = …" — distinguishes the two roots by name, so the reader can track which one is being carried forward.

**Authority / evidence handling**
- "the same method Tsokos uses to solve for the range in normal projectile motion on horizontal ground (1: p.49-50)" — anchors the derivation to a cited source so the reader trusts the strategy.

**Explanation verbs / mechanism names**
- "is solved from" — frames the next equation as yielding one named variable.
- "is substituted into" — names the move of replacing a symbol with its solved expression.
- "Substituting in the cosine rule" — names the trigonometric identity being applied rather than letting it appear as an unexplained trick.

**Equation-text hand-off verbs**
- "Substituting" (twice, once for *t* and once for the trig identity) — used both for algebraic substitution and for invoking an identity, showing that the same verb handles two different kinds of "replace one symbol with another" operations.

---

## How to Explain an Idea (replication steps)

The pattern this section uses is: **authority-anchored strategy → boundary-condition justification → substitution procedure → algebraic manipulation with named identities → neat final form**. To replicate it for a new derivation:

1. **Open by naming a known reference.** State whose method you are following and give the page number; this puts the reader on familiar ground before introducing any new symbols.
2. **Identify the link variable.** Name the single quantity that appears in both of your governing equations and will be carried from one to the other.
3. **Justify the boundary condition.** Give a one-clause physical reason that one quantity equals zero (or a constant) at the moment of interest — "since when X happens, Y is zero."
4. **Announce the substitution.** Write a one-sentence "Then [variable] is substituted into [other equation]" so the reader can predict the next algebraic move.
5. **Flag the complication.** Tell the reader in advance that the algebra will be longer than the textbook version and *why* (quadratic vs linear, coupled vs uncoupled, etc.), so the extra lines do not look like padding.
6. **Display equation 1 set to its boundary condition.** Write the full expression, not just a reference to it.
7. **Show every algebraic step.** Factor, simplify, discard the trivial root explicitly (label it "initial" or "trivial"), and present the kept root on its own line.
8. **Insert a hinge header.** Write "Substituting [result] into [equation 2]" so the transition between the two equation groups is verbal, not silent.
9. **Perform the substitution and expand.** Write out the expanded form so the structure is visible to the reader.
10. **Group terms to expose a named identity.** Rearrange the algebra until a recognisable identity sits ready to fire.
11. **Name the identity in words and in symbols**, then write the collapsed expression one line below.
12. **Cancel and simplify to the final form**, displayed cleanly so the reader sees the journey and the destination.
