# Idea Flow Notes: mathematics_7_may2020_uKRa3LH15IKUdk5n — importance, it essentially says that the gradient

## Paragraph Flow (move by move)

**Paragraph 1** — *The integral model is announced.*

- **Move 1 — Claim/definition (continuation):** "of a tension vector at point x is the same as the gradient of the line at point x."
  - *What it does:* Equates two things (tension vector = gradient), setting up the central identity.
  - *Hands to next by — consequence:* The word **"Thus"** in the next sentence forces a logical consequence from this equivalence.

- **Move 2 — Consequence / formal model:** "Thus when the sum of the internal tension vectors in the wire is 0 the following function f(x) should model the shape of the wire:"
  - *What it does:* States the condition (sum = 0) under which the model holds, then points to the upcoming equation.
  - *Hands to next by — equation reference:* The colon introduces the integral; the next paragraph then has to **unpack** what every symbol in that integral means.

- **Move 3 — Mathematical statement:** The integral equation f(x) = ∫T⃗_x dx + c.
  - *What it does:* Encodes the previous claim as a calculus object.
  - *Hands to next by — necessity to define symbols:* Once an equation appears, every symbol demands a definition, so the next paragraph begins with **"Where T⃗_x is…"**.

---

**Paragraph 2** — *The tension vector is decomposed into forces.*

- **Move 1 — Variable definition:** "Where T⃗_x is the tension vector tangential to the wire at point x."
  - *What it does:* Names and locates (tangential to wire) the central symbol.
  - *Hands to next by — justification:* A bare definition needs a reason, so the writer supplies **axiom 1**.

- **Move 2 — Authority / mechanism:** "due to axiom 1 stated above, T⃗_x is equal and opposite to all the vector forces that act on any point below point x:"
  - *What it does:* Invokes a prior axiom to justify why T⃗_x equals a negative sum of forces.
  - *Hands to next by — formalisation:* The colon demands the explicit force balance equation.

- **Move 3 — Mathematical statement:** T⃗_x = −(R⃗ + R⃗_x1)/(p⃗ + F⃗_B + F⃗_g).
  - *What it does:* Writes the equal-and-opposite balance as a fraction, separating numerator (resistive) from denominator (driving).
  - *Hands to next by — defining new symbols:* Each term inside the fraction now needs naming.

---

**Paragraph 3** — *The remaining forces are named, then a forward conjecture is flagged.*

- **Move 1 — Term-by-term definition (resistive forces):** "Where R⃗ is the drag acting on the towfish, and R⃗_x1 is the drag acting on a small segment of wire at which point x is on (drag cannot act on a point),"
  - *What it does:* Defines both numerator symbols, with a parenthetical clarifying a modelling subtlety.
  - *Hands to next by — continuation:* The **"and"** before p⃗ signals more terms follow.

- **Move 2 — Term-by-term definition (driving forces):** "and p⃗ is the distributed force of gravity and buoyancy acting on any point >x, F⃗_B is the buoyant force acting on the towfish, and F⃗_g is the force of gravity acting on the towfish."
  - *What it does:* Defines every denominator symbol, completing the symbol map.
  - *Hands to next by — closure + forward move:* Once every variable is named, the writer can now make a **future-oriented conjecture**.

- **Move 3 — Forward implication / verdict:** "Ideally this vector would be investigated to conjecture a function f(x) modelling the depth of a…"
  - *What it does:* Flags that the investigation is incomplete and points to the next analytical step (conjecture f(x)).
  - *Hands to next by — opening up the topic:* The word **"Ideally"** frames the rest of the coursework as the fulfilment of this conjecture.

---

## What This Section Does (content sequence)

This is an **equation-unpacking section**. The logical order is:

1. **State the central identity** (tension vector = gradient) — sets up why an integral is appropriate.
2. **Announce the model with a condition** ("Thus when… is 0 the following function…") — gives the integral meaning by attaching a physical condition.
3. **Present the first equation** — gives the reader a concrete object to interrogate.
4. **Define the master variable** (T⃗_x) — addresses the first symbol in the equation.
5. **Justify its expression via an axiom** — earns the right to write the second equation.
6. **Present the second equation** — substitutes the force balance into the integral.
7. **Define the resistive terms** (R⃗, R⃗_x1) — handles the numerator.
8. **Define the driving terms** (p⃗, F⃗_B, F⃗_g) — handles the denominator.
9. **Close with a forward conjecture** — signals that the model still needs testing in the next section.

**Why this order:** Each move is *forced* by the previous one — an equation demands its symbols, a symbol demands an authority, an authority demands a formal expression, and a formal expression demands every term be spelled out. A student can replicate this by following the rule: *never write a symbol you have not first named or justified.*

---

## Paragraph Skeletons (replicable templates)

### Skeleton A — Identity leading to a model

**SKELETON:** "[X] is the same as the gradient of [Y] at point x. Thus when [condition] the following function f(x) should model [the quantity of interest]: f(x) = ∫[expression]dx + c."

- **Slot roles / grammar:**
  - Slot 1: equivalence statement between a vector quantity and a gradient — present tense, two noun phrases.
  - Slot 2: conditional introduced by "Thus when" + a physical equilibrium condition, leading to a displayed integral.
- **How to fill with a different idea:** Slot 1 = pick any vector field that is path-derivative of a scalar potential. Slot 2 = pick an equilibrium condition (e.g. "net torque is 0", "mass flow is conserved").
- **Original filled version:** "of a tension vector at point x is the same as the gradient of the line at point x. Thus when the sum of the internal tension vectors in the wire is 0 the following function f(x) should model the shape of the wire."
- **Demo fill (different idea):** "of an electric field vector at point r is the same as the gradient of the potential at point r. Thus when the net charge enclosed by a surface is 0 the following function V(r) should model the potential inside the cavity."

### Skeleton B — Defining a master symbol via an axiom

**SKELETON:** "Where [master variable] is [physical description] at point x. due to [authority] stated above, [master variable] is equal and opposite to [list of forces acting on a region]: [equation]."

- **Slot roles / grammar:**
  - Slot 1: "Where [symbol] is…" definition clause.
  - Slot 2: "due to [named result]" causal justification.
  - Slot 3: explicit equal-and-opposite relation followed by a fraction/vector equation.
- **How to fill with a different idea:** Slot 1 = name the central vector in your model. Slot 2 = cite a law (Newton's third law, Gauss's law, Lenz's law). Slot 3 = write the opposing force sum.
- **Original filled version:** "Where T⃗_x is the tension vector tangential to the wire at point x. due to axiom 1 stated above, T⃗_x is equal and opposite to all the vector forces that act on any point below point x."
- **Demo fill:** "Where F⃗_net is the net force on the fluid element at point y. due to Newton's second law stated above, F⃗_net is equal and opposite to the pressure-gradient and viscous forces that act on the same element."

### Skeleton C — Term-by-term variable glossary

**SKELETON:** "Where [term A] is [definition with location]; [term B] is [definition, often with a parenthetical caveat]; and [term C] is [definition]."

- **Slot roles / grammar:** A coordinated list of "where X is…" clauses, with optional parentheses for modelling subtleties.
- **How to fill with a different idea:** List each symbol that appeared in the previous equation and define it physically; reserve parentheses for any term whose meaning is non-obvious.
- **Original filled version:** "Where R⃗ is the drag acting on the towfish, and R⃗_x1 is the drag acting on a small segment of wire at which point x is on (drag cannot act on a point), and p⃗ is the distributed force of gravity and buoyancy acting on any point >x, F⃗_B is the buoyant force acting on the towfish, and F⃗_g is the force of gravity acting on the towfish."
- **Demo fill:** "Where τ_w is the wall shear stress on the pipe interior; μ is the dynamic viscosity of the fluid (assumed Newtonian throughout); and ΔP is the pressure drop acting across the length of the pipe."

### Skeleton D — Forward conjecture

**SKELETON:** "Ideally [the assembled vector/expression] would be investigated to conjecture a function f(x) modelling [the target quantity] of a [continuation]."

- **Slot roles / grammar:** Single sentence in conditional/modal ("would be") future-perfect framing.
- **How to fill with a different idea:** After defining every symbol, point forward to the next section by naming what still needs to be solved.
- **Original filled version:** "Ideally this vector would be investigated to conjecture a function f(x) modelling the depth of a [towfish trajectory]."
- **Demo fill:** "Ideally this stress tensor would be investigated to conjecture a function ε(t) modelling the strain of a [beam under cyclic loading]."

---

## Express-Idea Vocabulary

**Sequencing / flow**
- **"Thus when"** — "Thus when the sum of the internal tension vectors in the wire is 0…" → marks a derived consequence.
- **"following function"** — "the following function f(x) should model the shape" → signals a transition from idea to formal object.

**Cause / consequence**
- **"Thus"** — "Thus when the sum of the internal tension vectors…" → converts the previous equivalence into a model.
- **"due to"** — "due to axiom 1 stated above, T⃗_x is equal and opposite…" → binds an equation to its justifying authority.

**Authority / evidence handling**
- **"due to axiom 1 stated above"** — "due to axiom 1 stated above, T⃗_x is equal and opposite…" → invokes a previously established result as proof.
- **"stated above"** — same sentence → locates the authority earlier in the paper.

**Specification / definition verbs**
- **"is the same as"** — "of a tension vector at point x is the same as the gradient of the line at point x" → defines via equivalence.
- **"Where"** — "Where T⃗_x is the tension vector tangential to the wire…" → opens every variable definition.
- **"is equal and opposite to"** — "T⃗_x is equal and opposite to all the vector forces…" → specifies a vector relationship.
- **"acting on"** — "drag acting on the towfish…buoyant force acting on the towfish" → repeatedly used to attach a force to a body or region.

**Concession / forward-looking**
- **"Ideally"** — "Ideally this vector would be investigated to conjecture…" → softens the next move as aspirational rather than concluded.
- **"would be investigated"** — same sentence → modal future, marking incompleteness.

---

## How to Explain an Idea (replication steps)

This section uses the **equation-unpacking pattern**: *Identity → Condition → Integral model → Master variable → Authority → Substituted equation → Glossary of remaining symbols → Forward conjecture*.

To explain a NEW idea with the same pattern, follow these steps in order:

1. **State an equivalence claim** — write one sentence that says "[physical quantity A] at point [x] is the same as the gradient of [B] at point [x]." This sentence earns everything that follows.
2. **Add a condition using "Thus when"** — specify the physical equilibrium (sum = 0, closed surface, no net force, etc.) under which your model will hold. End the sentence with a colon.
3. **Display the first (master) equation** — write the integral / differential / function that captures the model. Do not yet explain its parts.
4. **Open the next sentence with "Where"** — define the master symbol physically (its direction, where it acts, what it represents).
5. **Cite an authority with "due to [named result] stated above"** — justify why your definition holds by referencing a law, axiom, or theorem already introduced.
6. **Write the equal-and-opposite (or substitute) equation** — translate the authority into a second equation that decomposes the master symbol into a sum of opposing terms.
7. **Define every remaining term in a coordinated "Where… and… and…" list** — go through numerator then denominator (or one side then the other), one symbol per clause. Use parentheses to flag any non-obvious modelling choice.
8. **Close with a forward-looking sentence beginning "Ideally"** — name what still needs to be investigated to complete the model. This sets up your next section without claiming closure.
