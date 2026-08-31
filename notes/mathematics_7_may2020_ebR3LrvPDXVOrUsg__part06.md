# Idea Flow Notes: mathematics_7_may2020_ebR3LrvPDXVOrUsg — As we discussed earlier, matrices are linear transformations that transform the vector

## Paragraph Flow (move by move)

**(Single paragraph — the section is one continuous walk-through.)**

**S1** — *Claim / general rule* — quote: "**transformed off of the vector's original span**"
States the typical behaviour in advance. Hands to S2 by **promising an example** ("For most vectors…" invites "For example…").

**S2** — *Example introducer + setup* — quote: "**For example, the vector ⟨1, 0⟩, being transformed by matrix, N**"
Names a specific vector and the operator. Hands to S3 by **needing the operator written down** before the result can be discussed.

**S3** — *Evidence / visual data* — quote: "**2 0 / 1 1**"
The matrix itself, in display form. Hands to S4 by **supplying the tool** the next sentence uses to locate the result.

**S4** — *Mechanism / unpack of the example* — quote: "**lies on the span of x = 0**"
Reads off where the input and output sit. Hands to S5 by **offering the raw observation** that the generalisation will pull back from.

**S5** — *Generalisation + contrast pivot* — quote: "**but there are a few vectors that stay on their span**"
Zooms back out, then **contrasts** "most" against "a few". Hands to S6 by **flagging the exception** as the next thing to show.

**S6** — *Counter-example / instance of the exception* — quote: "**on the span y = x, transforms to the vector, ⟨2, 2⟩**"
Concretely exhibits the special vector. Hands to S7 by **finishing the demonstration**, so the term can be awarded.

**S7** — *Definition / naming + reason* — quote: "**is known as an Eigenvector for this matrix**"
Labels the phenomenon ("Eigenvector") and **justifies the label with "since…"**. Hands to S8 by **introducing the related companion** ("a related Eigenvalue").

**S8** — *Definition of the companion concept* — quote: "**which is the scalar by which the vector is multiplied**"
Defines Eigenvalue by its mechanism (scaling factor). Hands to S9 by **needing the abstract definition instantiated** in the running example.

**S9** — *Application / verdict on the example* — quote: "**the Eigenvalue of the Eigenvector, ⟨1, 1⟩, is 2**"
Lands the general definition back on ⟨1, 1⟩, closing the loop. **Ends the section** by resolving the value the reader was tracking.

## What This Section Does (content sequence)

The section is an **example-anchored concept introduction**. Its moves, in order:

1. **General behavioural claim** — tells the reader what *usually* happens.
2. **Concrete example of the claim** — picks one specific vector and one specific matrix.
3. **Visual data (the matrix)** — supplies the tool.
4. **Mechanistic reading of the example** — describes where the input and output live.
5. **Generalisation + concession pivot** — restates the rule, then signals the exception ("but there are a few").
6. **Counter-example** — shows the exceptional vector staying put.
7. **Naming** — awards the label (Eigenvector) with a "since" justification.
8. **Companion-concept definition** — introduces the related term (Eigenvalue) and defines it by mechanism.
9. **Instance of the companion concept** — closes the loop on the same vector.

**Why this order:** intuition is built on a worked example *before* terminology arrives; every named term is paired with the justifying reason in the same sentence; the reader sees the *thing*, is told its *name*, then is told its *partner* and the *partner's value* on the same object. Another student replicating this sequence should: claim → instance → observation → restate + flag exception → exhibit exception → name → partner → value on same instance.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "general claim, example, then exceptional instance"**

> [General claim about typical behaviour of subjects]. For example, [one specific subject] being [acted on] by [the operator]: [display of operator]. The original [input] lies on [property A], and the transformed [output] lies on [property B]. This [subject], and most [subjects] get [typical outcome], but there are a few [subjects] that [exceptional outcome]. For [the same operator], it happens to be that [exceptional subject], on [property C], transforms to [result], that also [matches property C]. This [subject] is known as a [term], since [defining reason].

- **Slot 1** (general claim): noun-phrase subject + verb of change + prepositional phrase stating the usual outcome.
- **Slot 2** (concrete example setup): "For example, [subject], being [verbed] by [operator]:" — introduces a named instance.
- **Slot 3** (operator display): a visual block (matrix / formula / diagram).
- **Slot 4** (mechanism): two coordinated clauses locating the input and the output on different properties.
- **Slot 5** (pivot): "This [subject], and most [subjects] get [typical outcome], but there are a few [subjects] that [exceptional outcome]." — restates + concedes an exception.
- **Slot 6** (exceptional instance): "For [the above operator], it happens to be that…" — exhibits one surviving subject.
- **Slot 7** (naming): "This [subject] is known as a [term], since [reason]."

**Original filled version:** "For most vectors, the vector will be transformed off of the vector's original span. For example, the vector ⟨1, 0⟩, being transformed by matrix, N: [2 0; 1 1]. The original vector lies on the span of x = 0, and the transformed vector, ⟨2, 1⟩, lies on the span y = ½x. This vector, and most vectors get thrown off of their span, but there are a few vectors that stay on their span during the transformation. For the above matrix, it happens to be that the vector, ⟨1, 1⟩, on the span y = x, transforms to the vector, ⟨2, 2⟩, that also lies on the span y = x. This vector, ⟨1, 1⟩, is known as an Eigenvector for this matrix, since it stays on its own span."

**Demonstration fill (different idea — phase of a pendulum):** "For most displacements, the pendulum will swing off of the equilibrium's vertical line. For example, the bob at 30°, being released from [diagram of pendulum]: [mass and length labels]. The original bob lies on the displacement arc, and the returned bob lies on a lower arc. This bob, and most bobs get damped below their starting arc, but there are a few bobs that return exactly to their starting arc. For the same pendulum length, it happens to be that the bob released at the small-angle limit, on the arc θ = A, transforms to a position, that also matches θ = A. This bob is known as the *undamped returner*, since it lands on its own arc."

**SKELETON B — "named term plus its scalar companion"**

> [Subject] is known as [term A] for [context], since [defining reason]. This [subject] has a related [term B] which is [mechanistic definition]. In this example, the [term B] of the [term A], [instance], is [value], since [cause].

- **Slot 1** (term + reason): "is known as [A]… since [reason]" — naming clause with a "since" justification.
- **Slot 2** (companion concept): "a related [term B] which is [how it is computed/obtained]" — relative clause definition.
- **Slot 3** (instance value): "In this example, the [term B] of the [term A], [instance], is [value], since [cause]" — applies the definition to the running example.

**Original filled version:** "This vector, ⟨1, 1⟩, is known as an Eigenvector for this matrix, since it stays on its own span. This Eigenvector has a related Eigenvalue which is the scalar by which the vector is multiplied to get the transformed vector. In this example, the Eigenvalue of the Eigenvector, ⟨1, 1⟩, is 2, since the vector is being scaled by 2."

**Demonstration fill (different idea — resonance frequency):** "This mass–spring system is known as a *resonant oscillator* for the driving force, since it amplifies the input signal. This oscillator has a related *quality factor* which is the dimensionless number by which the stored energy exceeds the dissipated energy per cycle. In this example, the quality factor of the resonant oscillator at 1 Hz, is 200, since the damping coefficient is being divided by the critical value."

## Express-Idea Vocabulary

- **Sequencing / example-launchers:** "**For example, the vector ⟨1, 0⟩**" (S2); "**For the above matrix**" (S6); "**In this example**" (S9) — used to **return to the running instance** after abstract talk.
- **Cause / justification:** "**is known as an Eigenvector for this matrix, since**" (S7); "**the Eigenvalue… is 2, since the vector is being scaled by 2**" (S9) — the word *since* is the section's workhorse for making a claim defensible.
- **Contrast / concession:** "**but there are a few vectors that stay**" (S5) — single pivot word that re-routes the whole paragraph.
- **Specification / focus:** "**it happens to be that the vector, ⟨1, 1⟩**" (S6); "**the original vector lies on**" (S4) — narrows from class to instance.
- **Evidence handling:** "**For example, the vector ⟨1, 0⟩, being transformed by matrix, N**" — concrete vector/matrix pair functions as evidence.
- **Explanation verbs:** "**is known as**" (S7, definition by naming); "**is the scalar by which**" (S8, definition by mechanism); "**transforms to**" (S4, S6, mechanism); "**being scaled by**" (S9, cause).

## How to Explain an Idea (replication steps)

**Pattern used:** *worked-example-first concept introduction with a contrast pivot*. The reader sees the **ordinary case** before the **named term** is given, and the term arrives carrying its own *since*-clause justification.

**Replication steps:**

1. **State the ordinary behaviour as a one-sentence rule.** Use the pattern "For most [X], the [X] will be [verbed] [off/away from] the [X]'s [reference property]."
2. **Launch a concrete instance** with "For example, the [specific X], being [verbed] by [operator]:"
3. **Show the operator as a visual block** (matrix / equation / diagram) directly after the colon.
4. **Unpack the example** with a two-clause sentence locating input on property A and output on property B ("The original [X] lies on [A], and the transformed [X] lies on [B].").
5. **Pivot with "but"** to flag the exception: "This [X], and most [X]s get [ordinary outcome], **but** there are a few [X]s that [exceptional outcome]."
6. **Exhibit one exceptional instance**, re-using the same operator: "For the above [operator], it happens to be that [exceptional X]… transforms to [result] that also [matches the original property]."
7. **Award the term** in the form "This [X] is known as a **[Term]**, since [the defining behaviour you just showed]." The *since*-clause is non-optional; it is the proof the label is deserved.
8. **Introduce the companion concept** as "This [Term] has a related [Companion] which is [definition by mechanism, e.g. "the [quantity] by which…"]."
9. **Close the loop** on the running example: "In this example, the [Companion] of the [Term], [instance], is [value], since [arithmetic/cause]."

The rhythm of this section is therefore: **claim → example → mechanism → restate + exception → exhibit exception → name → partner → value.** A 6/7 student keeps every step tied to the *same* running object (here, ⟨1, 1⟩), so the reader never loses what is being talked about.
