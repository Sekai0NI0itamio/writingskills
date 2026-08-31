# Idea Flow Notes: physics_7_may2017_jZUeZ77T0PVx1XPb — can be calculated as the summation of the moments of inertia of infinitely small rings, or the integral

## Paragraph Flow (move by move)

**Unit 1 — Sentence fragment (continuation of prior line):**
- Move: **residue of a prior statement + forward reference to evidence**. It finishes an integral expression ("of r2 by m over the range of R' to R") and then announces two pieces of supporting evidence.
- Quote: "as illustrated in Figure 2 and Equation 4"
- Hand-off: the phrase "as illustrated in" tells the reader that what follows will *show* (not argue) the claim — it points forward to the figure on the next line, so the reader expects a visual rather than further prose.

**Unit 2 — Figure 2 caption:**
- Move: **identification/definition of the physical object**. The caption names the geometry the math will model.
- Quote: "A hollow cylinder with the given conditions"
- Hand-off: by identifying the object as a "hollow cylinder" and freezing the parameters ("with the given conditions"), it sets up the variables (R, R', h, ρ) that the next unit will manipulate. The reader hands off from caption to equation because the caption supplies the *labels* the equation needs.

**Unit 3 — Equation 4 (displayed derivation chain):**
- Move: **worked calculation**, a chain of equalities performing substitution → integration → evaluation → simplification. Each "=" is a logical step.
- Quote: "I = ∫ r² dm = ∫ r² · ρ · dV = ∫ r² · ρ · 2πr · dr · h = ρ2πh [r⁴/4]"
- Hand-off: the chain ends in a closed-form expression (½M(R² + R'²)), which invites the reader to ask "what did I just see?" — that question is answered by the caption on the next line.

**Unit 4 — Equation 4 caption:**
- Move: **label/naming of the result**. It retrospectively identifies what the chain of equalities accomplished.
- Quote: "The derivation of the moment of inertia of a hollow cylinder with the given conditions"
- Hand-off: this is a closing move; it has no successor in the section. It seals the unit by converting a bare mathematical expression into a named, citable result.

---

## What This Section Does (content sequence)

This is a **derivation block**, and its content moves run in this strict order:

1. **Residue + forward reference** — anchors the current line to a prior calculation and promises visual support ("as illustrated in Figure 2 and Equation 4").
2. **Geometric identification via figure** — names the physical object ("A hollow cylinder") and fixes the operating conditions ("with the given conditions"). *Why first among the visuals:* the reader cannot read the integral symbols unless they already know which object is being parameterised.
3. **Worked calculation chain** — rewrites dm as ρ dV, substitutes dV = 2πr dr h, integrates r³, evaluates the limits R'→R, pulls constants out, and replaces ρ with M/V. *Why next:* the figure gave the labels, the equation now uses them; each equals sign is justified by the step that precedes it.
4. **Result-labelling caption** — names the derivation and re-states the object, allowing the closed-form expression to be cited later as "the moment of inertia of a hollow cylinder."

A second student replicating this for a different shape (e.g. solid sphere) must follow the same order: name the object in a figure first, then perform the chain of equalities whose substitutions are visible to the reader, then caption what the chain produced.

---

## Paragraph Skeletons (replicable templates)

**SKELETON A — Object-identification caption (figure caption)**
> SKELETON: "A [geometric object] with the given conditions."

1. **What each slot holds:** a noun phrase naming the shape ("hollow cylinder"), preceded by the determiner "A"; the tail "with the given conditions" is a fixed modifier that defers detail to the body text.
2. **How to fill with a different idea:** slot 1 = name the physical object whose moment of inertia (or analogous derived quantity) you are about to compute. Keep it singular and descriptive ("solid sphere", "thin rod", "rectangular plate"); do not insert dimensions, those belong in the body.
3. **Original fill:** "A hollow cylinder with the given conditions."
4. **Demonstration fill:** "A solid sphere with the given conditions."

---

**SKELETON B — Forward-reference fragment**
> SKELETON: "[residue of prior symbolic expression], as illustrated in [Figure X] and [Equation Y]."

1. **What each slot holds:** a tail-end of a prior calculation (often an unevaluated integral or a limit), then the fixed connective "as illustrated in", then two numbered references (one figure, one equation).
2. **How to fill:** finish the calculation you were mid-way through, then advertise the two supports the reader should consult next. The two references must be a *figure* (the visual) and an *equation* (the math).
3. **Original fill:** "of r2 by m over the range of R' to R, as illustrated in Figure 2 and Equation 4."
4. **Demonstration fill:** "of r² sin θ dθ from 0 to π, as illustrated in Figure 3 and Equation 5."

---

**SKELETON C — Result-labelling caption (equation caption)**
> SKELETON: "The [process-noun] of the [quantity] of a [object] with the given conditions."

1. **What each slot holds:** a gerund-style process noun ("derivation", "calculation", "determination"), then the named quantity ("moment of inertia", "centre of mass"), then the object noun phrase, then the fixed tail "with the given conditions".
2. **How to fill:** pick the *process* you just performed (usually "derivation"), the *quantity* you produced, and the *object* you modelled. Mirror the wording of the figure caption so the pair reads as a unit.
3. **Original fill:** "The derivation of the moment of inertia of a hollow cylinder with the given conditions."
4. **Demonstration fill:** "The derivation of the moment of inertia of a solid sphere with the given conditions."

---

## Express-Idea Vocabulary

**Visual referencing / evidence handling:**
- "as illustrated in" — "as illustrated in Figure 2 and Equation 4" (announces paired visual evidence)

**Specification (pinning context to the working conditions):**
- "with the given conditions" — "A hollow cylinder with the given conditions" (declares that parameters are fixed elsewhere)

**Process-naming / labelling:**
- "The derivation of" — "The derivation of the moment of inertia of a hollow cylinder" (retrospectively converts an equation into a named, citable result)

(No explicit sequencing, causal, contrast, or connective vocabulary appears in this fragment — the section's logic is carried by mathematical symbols and captions, not prose connectives.)

---

## How to Explain an Idea (replication steps)

This section relies on the **figure → worked-derivation chain → labelled-result** pattern. To replicate it on a NEW shape/quantity:

1. **Finish the prior sentence with a forward reference.** End an earlier calculation with a dangling integral or limit, then write "as illustrated in Figure [n] and Equation [n+1]." This tells the reader what is about to do the proving.
2. **Insert a figure and caption it with the object name only.** Caption = "A [shape] with the given conditions." Do not embed dimensions in the caption; the figure should already show them.
3. **Write the derivation as a single chain of equalities.** Each "=" must be justified by a substitution or algebraic move visible on the page: write dm in terms of ρ and dV, substitute the geometry-specific dV, pull constants outside the integral, integrate, evaluate the limits, then re-express any constants in terms of measurable quantities (mass, dimensions).
4. **Caption the equation as a result.** Caption = "The derivation of the [quantity] of a [shape] with the given conditions." This converts the chain into something that can be cited by name later in the report.
5. **Resist the urge to narrate.** The pattern works because the captions carry the *naming* and the equation carries the *showing*; prose connectives would interrupt the visual rhythm the reader is being asked to follow.
