# Idea Flow Notes: mathematics_7_may2020_ebR3LrvPDXVOrUsg — It is possible to redefine any given linear transformation in the bases of its Eigenvec-

## Paragraph Flow (move by move)

**Paragraph 1** (procedure → worked example)

1. *(continuation move — picks up an unfinished thought from the previous page)* **Procedure statement:** "This would mean creating the change of basis matrix, B, for the two Eigenvectors" — hands to next sentence by **promising a benefit**, so the reader expects the *why* of doing it.
2. **Value claim / justification:** "I found that this would change the matrix in a way" — fills the promised benefit; hands to next sentence by saying "I will now demonstrate," so the reader expects a concrete instance.
3. **Transition to instance:** "Let us try doing this for the matrix above, N :" — acts as a **specification bridge** that narrows the general claim down to one worked matrix.
5–8. **Evidence (matrices):** displays N, its eigenvalues λ₁ = 1, λ₂ = 2, eigenvectors v₁, v₂, then B and B⁻¹, and the product B⁻¹NB — these are the **worked example** that fulfils the promise of sentence 3. The block **hands forward by producing an output matrix** whose shape invites comment.

**Paragraph 2** (observation → unpack → name → mechanism → concession-implication)

1. **Observation / verdict on the output:** "The interesting part of this matrix is that it is diagonal." — hands forward by **naming a property that needs explaining**.
2. **Unpack (define the property by its appearance):** "There only exist values in the matrix along the diagonal" — **specifies** what "diagonal" looks like visually; hands forward by signalling that this appearance is *not a coincidence*.
3. **Name / generalise the result:** "This is a special result when the bases are changed" — **labels** the observation as a recognised phenomenon (Eigenbases); hands forward by raising "why does this happen?"
4. **Mechanism (cause):** "This is because the transformation is now defined by a stretching" — **answers** the why raised in sentence 3 by giving a geometric reason; hands forward because a mechanism this neat begs the question "so what?"
5. **Concession → implication pivot:** "At first glance, this isn't very useful, but the useful thing … is the following property:" — **dismisses a naive objection, then escalates** to a payoff the next sentence will deliver.

## What This Section Does (content sequence)

This is a **concept-to-application section** showing how abstract theory (Eigenvector bases) produces a concrete algebraic result.

1. **State the procedure in general terms** ("create the change of basis matrix") — sets up what the reader will see done.
2. **Justify the procedure with a benefit** ("easier to generalise") — gives the reader a reason to keep reading.
3. **Pivot to a concrete worked example** ("Let us try doing this for the matrix above") — moves from theory to a specific instance the reader can verify.
4. **Display the full computation step by step** (matrix → eigenvalues → eigenvectors → B → B⁻¹ → B⁻¹NB) — proves the procedure works on a real object.
5. **Identify the key feature of the result** ("it is diagonal") — gives the reader something to notice.
6. **Define that feature visually** ("only exist … along the diagonal") — ensures the reader has concretely seen what was claimed.
7. **Generalise the result into a named phenomenon** ("Eigenbases") — links the specific case back to the general theory from sentence 1.
8. **Give the underlying mechanism** ("stretching and pulling of the basis vectors") — explains *why* the result is inevitable, not coincidental.
9. **Acknowledge a reader objection, then promise a deeper payoff** ("At first glance … but the useful thing … is the following property") — sets up the next section to deliver the main theorem.

The order is **claim → reason → instance → evidence → observation → definition → naming → cause → concession-implication**. Each move exists to make the next one feel necessary: a promise is made, fulfilled, observed, explained, and then escalated.

## Paragraph Skeletons (replicable templates)

**Skeleton A — General principle promised, then demonstrated on one object**
SKELETON: "[This would mean / We now do] [procedure X] for [the object]. [I found / One finds] that this would [consequence Y]. [Let us try / Consider] doing this for [specific instance]: [worked-out evidence]. [Result] = [output]."

- **Slot 1 — Procedure statement:** declarative present; names an object and the action performed on it.
- **Slot 2 — Justification:** "I found / One can see" + outcome clause; states the payoff.
- **Slot 3 — Concrete instance marker:** "Let us try …" / "Consider …" introducing a named worked example.
- **Slot 4 — Evidence block:** displayable computation.
- **Slot 5 — Final expression:** a closed-form result that the next paragraph will comment on.

*Original fill:* "This would mean creating the change of basis matrix, B, for the two Eigenvectors of the transformation matrix. I found that this would change the matrix in a way that could make it much easier to generalise. Let us try doing this for the matrix above, N…" with B⁻¹NB = diag(1, 2).

*Demonstration fill (different idea):* "This would mean writing the recurrence in closed form. I noticed that doing so would let the nth iterate be read off immediately. Let us try this for the Fibonacci recurrence aₙ = aₙ₋₁ + aₙ₋₂ with a₀ = 0, a₁ = 1…" yielding aₙ = (φⁿ − ψⁿ)/√5.

**Skeleton B — Observation, defined by appearance, then generalised and explained**
SKELETON: "The [interesting / striking] part of this [object] is that it is [property]. There only [exist / appear] [values / elements] [in the position characteristic of property]. This is a [special / general] result when [condition] is met to create [named concept]. This is because [mechanism]."

- **Slot 1 — Verdict:** "The interesting part … is that it is [adjective]"
- **Slot 2 — Visual unpack:** "There only exist … [position phrase]"
- **Slot 3 — Generalisation + name:** "This is a special result when … to create [term]"
- **Slot 4 — Causal mechanism:** "This is because [geometric / physical reason]"

*Original fill:* "The interesting part of this matrix is that it is diagonal. There only exist values in the matrix along the diagonal from the top left to the bottom right. This is a special result when the bases are changed to the Eigenvectors to create Eigenbases. This is because the transformation is now defined by a stretching and pulling of the basis vectors."

*Demonstration fill (different idea):* "The interesting part of this polynomial is that it is reducible. There only exist integer coefficients along two bracketed quadratic factors. This is a useful property when the polynomial is factored over ℤ to obtain rational roots. This is because the rational root theorem restricts possible roots to divisors of the constant."

**Skeleton C — Concession pivot that escalates to a payoff**
SKELETON: "At first glance, this [isn't very useful / seems trivial], but the [useful / important] thing about [phenomenon] is the following property: [formula / theorem statement]."

- **Slot 1 — Dismissal of naive view:** "At first glance, …"
- **Slot 2 — Pivot:** "but the useful thing … is"
- **Slot 3 — Payoff preview:** "the following property:"
- **Slot 4 — The thing itself:** formula or named property, displayed.

*Original fill:* "At first glance, this isn't very useful, but the useful thing about diagonalising the matrix is the following property: [[a,0],[0,b]]ⁿ = [[aⁿ,0],[0,bⁿ]]."

*Demonstration fill (different idea):* "At first glance, this just lists the roots, but the useful thing about the characteristic polynomial is the following identity: det(A − λI) = 0 ⟺ λ is an eigenvalue."

## Express-Idea Vocabulary

- **Sequencing / pivoting to instance:** *"Let us try doing this for"* — moves from theory to a specific case.
- **Causal mechanism:** *"This is because"* — explicitly opens a why-clause after a "special result" claim.
- **Concession / contrast:** *"At first glance, this isn't very useful, but"* — admits the surface reading before pivoting.
- **Escalation marker:** *"the useful thing … is the following property"* — flags that what follows is the payoff.
- **Observation / verdict:** *"The interesting part of this matrix is that"* — frames the next sentences as a noticing.
- **Definition-by-appearance:** *"There only exist values in the matrix along the diagonal"* — defines a property by visual location.
- **Naming / generalising:** *"This is a special result … to create Eigenbases"* — turns a specific result into a named concept.
- **Explanation verb (mechanism):** *"the transformation is now defined by a stretching"* — uses "defined by" to bind geometry to algebra.
- **Justification of effort:** *"this would change the matrix in a way that could make it much easier to generalise"* — "would make … easier to" frames the work as enabling generality.

## How to Explain an Idea (replication steps)

This section uses the **observation-after-worked-example** pattern: do the procedure, *look* at what came out, *name* what you see, then *explain why it had to be so*. Replicate it in 7 steps:

1. **Announce the procedure in general terms** in one declarative sentence that names the operation and the object it acts on (e.g. "forming the change of basis matrix for the eigenvectors").
2. **Attach a payoff clause** to the same procedure so the reader knows why you are about to do work ("would make it easier to generalise").
3. **Bridge to one concrete instance** with "Let us try …" or "Consider …" and name it (e.g. "matrix N").
4. **Display the full worked computation** as a block — matrices, equations, or diagrams — without prose interruption.
5. **Open the next paragraph with a verdict sentence** that singles out one striking feature of the result ("The interesting part … is that it is X").
6. **Define X by where it appears** in the output, not by an abstract gloss ("values only along the diagonal"), then **generalise X into a recognised term** (Eigenbases) and **supply the causal mechanism** ("This is because …").
7. **End with a concession pivot** ("At first glance … but the useful thing … is the following property:") that throws the result forward into the *next* section as the real payoff.

The rhythm is: **promise → demonstrate → notice → name → explain → escalate**.
