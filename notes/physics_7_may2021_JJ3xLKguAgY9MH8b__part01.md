# Idea Flow Notes: physics_7_may2021_JJ3xLKguAgY9MH8b — 2.1    Angles, forces and motion equations

## Paragraph Flow (move by move)

**Paragraph 1** (definitions of geometry variables)

- **S1 — Deixis/context pointer.** "The variables are represented in Figure 1." Hands off by telling the reader the visual exists, so the next sentence can resolve what each variable *means* without re-introducing the symbols.
- **S2 — Definition (first variable).** "The range is defined as the distance travelled" Hands off by completing variable 1, leaving variable 2 (angle) as the next obvious item in the figure, which the reader will expect to be defined in the same way.
- **S3 — Definition (second variable), parallel to S2.** "the angle between the incline line and" Hands off by finishing the definition cluster; once both geometric terms are fixed, the next paragraph can move to *using* them.

**Paragraph 2** (coordinate-system transformation)

- **S1 — Purpose + setup (problem → tool).** "To solve for the range along the incline" Hands off by announcing a tool (new axes) is being introduced *because* of a goal — so the next sentence must establish the variable that lives in the original frame.
- **S2 — Definition (original-frame variable).** "θ, the launch angle, is the angle between" Hands off by giving the reader a fixed quantity θ; only after θ exists can the next sentence compute how it changes when the frame rotates.
- **S3 — Consequence / derivation.** "Therefore the new launch angle is θ" Hands off because the geometry change (rotate by α) demands a single visual confirmation, which the next sentence supplies.
- **S4 — Deixis (figure consolidates the transform).** "Figure 2 illustrates the coordinate system, all" Hands off by closing the geometric setup; the next paragraph now switches topic from *angles* to *forces*, the only remaining input to the motion.

**Paragraph 3** (force identification + assumption)

- **S1 — Deixis/context pointer.** "Figure 3 shows the forces acting on the" Hands off by signalling that the figure carries information; the next sentence names exactly which force the figure depicts.
- **S2 — Identification (the only force, with general caveat).** "The only force acting on the projectile is" Hands off because the general phrase "all other forces are negligible" requires the reader to be told which specific other force was the relevant one to ignore — supplied next.
- **S3 — Specification of the key assumption, with forward reference.** "In this context, the assumption is that air" Hands off by closing the forces block with a deferred justification, leaving the reader pointed forward to Section 6.

## What This Section Does (content sequence)

This is a **setup-and-definitions section** that prepares every quantity needed before any kinematic equation is written. The move-order is:

1. **Acknowledge the visual (figure reference).** Sets up the symbols before the reader meets them in text.
2. **Define geometric variables one by one.** Order chosen by visual prominence — the quantity on the figure that the reader will see first (range) gets defined first.
3. **State the problem-solving goal.** ("To solve for the range…") Motivates the coordinate transformation that follows.
4. **Introduce the new framework (rotated axes).** Cannot precede step 3 — the reader has no reason to accept a new frame without a stated purpose.
5. **Define the variable in the *original* frame (θ).** Must come *before* the derivation, because the derivation subtracts from θ.
6. **Derive the variable in the *new* frame (θ − α).** Strict consequence of step 5; "Therefore" marks this as logical, not optional.
7. **Re-anchor with a figure.** Confirms visually what steps 4–6 produced.
8. **Switch domain: from angles to forces.** New figure introduces a new physical input (weight).
9. **Identify the single operative force.** Pinned down so the equation of motion in the next section has only one term.
10. **Specify and justify the assumption (negligible air resistance), with cross-reference.** The only non-trivial assumption made in the section is named, restricted in scope ("In this context"), and validated elsewhere.

A student replicating this for any projectile/particle-on-incline problem should: *define geometry → transform coordinates → derive new angle → consolidate with figure → identify forces → justify assumption*.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Definition cluster (Paragraph 1 type)**

> "The variables are represented in Figure X. [Term 1] is defined as [definition]. [Term 2] is defined as [definition]."

1. Slot 1 — *Figure reference*: short sentence, present tense, names "Figure X" as the home of the symbols.
   Slot 2 — *Definition 1*: "is defined as" + noun phrase giving a measurable, geometric meaning.
   Slot 3 — *Definition 2*: identical grammatical shape to Slot 2, defining the second geometric quantity.
2. **How to fill differently:** Slot 1: pick the figure that carries your variables. Slot 2: pick the most visually prominent variable and define it as a measurable quantity in your scenario. Slot 3: pick the second-most prominent and define it as a geometric angle/distance relative to a reference line.
3. **Original fill:** "The variables are represented in Figure 1. The range is defined as the distance travelled on the incline line after the projectile has landed. The angle of incline is defined as the angle between the incline line and the horizontal line."
4. **Demonstration fill (pendulum releasing from a tilted support):** "The variables are represented in Figure 1. The swing radius is defined as the distance from the pivot to the bob at maximum displacement. The release angle is defined as the angle between the string at release and the vertical line."

**SKELETON B — Coordinate transformation with consequence (Paragraph 2 type)**

> "To solve for [target quantity], [new reference] is defined based on [angle]. [Original variable], is [definition]. Therefore the [new derived variable] is [expression]. Figure Y illustrates [elements]."

1. Slot 1 — *Purpose + framework*: "To solve for…" infinitive phrase stating the goal, followed by a passive construction naming the new reference (axes, basis, frame).
   Slot 2 — *Original-frame definition*: symbol + comma + "is" + definition, anchored to the *old* reference (e.g. horizontal).
   Slot 3 — *Consequence derivation*: starts with "Therefore", gives the algebraic form of the variable in the *new* frame.
   Slot 4 — *Figure consolidation*: "Figure Y illustrates" + a list of every element just derived.
2. **How to fill differently:** Slot 1: name what you actually want to compute. Slot 2: define the original variable using the *untransformed* reference (always horizontal or ground-fixed in mechanics problems). Slot 3: write the new value as (old value) − (rotation angle), or the equivalent subtraction/translation your transform produces. Slot 4: enumerate every piece of geometry the reader must see.
3. **Original fill:** "To solve for the range along the incline line, new axes are defined based on the angle α. θ, the launch angle, is the angle between the initial velocity vector and horizontal. Therefore the new launch angle is θ − α. Figure 2 illustrates the coordinate system, all relevant angles and the initial velocity and its components."
4. **Demonstration fill (block on slope, applied push):** "To solve for the acceleration along the slope, new axes are defined based on the angle β. φ, the applied angle, is the angle between the applied force and the horizontal. Therefore the new applied angle is φ − β. Figure 2 illustrates the coordinate system, all relevant angles and the applied force and its components."

**SKELETON C — Force identification with justified assumption (Paragraph 3 type)**

> "Figure X shows the forces acting on the [object] while [condition]. The only force acting on the [object] is [force] assuming that all other forces are negligible. In this context, the assumption is that [specific assumption] (evaluated in Section Y)."

1. Slot 1 — *Figure pointer + scenario condition*: "Figure X shows the forces acting on the [object] while [verb-ing]…"
   Slot 2 — *Identification*: "The only force… is [force]" + "assuming that all other forces are negligible" (a general flag, not a specific one).
   Slot 3 — *Specific assumption with forward reference*: starts "In this context", names *which* negligible force is being ignored, and points to a later section for validation.
2. **How to fill differently:** Slot 1: state the figure and the motion phase. Slot 2: name the single force your analysis will use. Slot 3: name the most important force you are dropping (friction, drag, buoyancy, etc.) and cross-reference where it is justified.
3. **Original fill:** "Figure 3 shows the forces acting on the projectile while its traveling in the air. The only force acting on the projectile is its weight assuming that all other forces are negligible. In this context, the assumption is that air resistance is negligible (evaluated in Section 6)."
4. **Demonstration fill (cylinder rolling):** "Figure 3 shows the forces acting on the cylinder while it rolls down the slope. The only driving force acting on the cylinder is its weight component parallel to the slope assuming that all other forces are negligible. In this context, the assumption is that rolling friction is negligible (validated in Section 5)."

## Express-Idea Vocabulary

- **Purpose / setup markers:** *"To solve for"* — "To solve for the range along the incline" (announces the operation before stating the tool).
- **Definition verbs:** *"is defined as"* — "The range is defined as the distance travelled"; *"is the angle between"* — "θ, the launch angle, is the angle between the initial" (replaces "is defined as" when the term is a symbol rather than a noun-phrase quantity).
- **Cause / consequence:** *"Therefore"* — "Therefore the new launch angle is θ − α" (signals that the next expression is a mechanical consequence of the rotation, not a new claim).
- **Assumption markers:** *"assuming that"* — "assuming that all other forces are negligible" (general flag attached to the operative sentence); *"In this context, the assumption is that"* — "In this context, the assumption is that air resistance" (narrows the scope to one specific ignored force).
- **Visual / deixis handling:** *"is represented in"* / *"shows"* / *"illustrates"* — "The variables are represented in Figure 1"; "Figure 3 shows the forces acting"; "Figure 2 illustrates the coordinate system" (three near-synonyms used to point at the three figures; "represented" for variables, "shows" for forces, "illustrates" for geometry).
- **Scope-restrictor:** *"In this context"* — narrows the assumption so it cannot be misread as a universal claim.

## How to Explain an Idea (replication steps)

The pattern is **define-variables → transform-frame → derive-consequence → consolidate-visual → identify-forces → justify-assumption** — a *geometry-setup-before-equation* pattern.

Step-by-step to replicate with a new idea:

1. **Open by pointing at a figure.** One short sentence telling the reader the symbols live in Figure X.
2. **Define each geometric variable with "is defined as".** Use one sentence per variable, each ending with a measurable description.
3. **State the problem in one "To solve for…" sentence.** Name the quantity you ultimately want.
4. **Introduce the new reference frame in a passive sentence** ("new axes are defined…", "a rotated basis is introduced…") so the reader knows a transformation is happening.
5. **Define the variable in the *old* frame**, anchored to the original reference (usually horizontal/ground).
6. **Derive the variable in the *new* frame**, beginning with "Therefore" and writing it as an algebraic change from the old value.
7. **Re-anchor with a figure** ("Figure Y illustrates…") listing every element introduced in steps 4–6.
8. **Open the forces block with a figure reference** ("Figure Z shows the forces acting on the [object] while…").
9. **Identify the single operative force** using "The only force… is [X] assuming that all other forces are negligible."
10. **Specify the dropped force with "In this context, the assumption is that [Y] is negligible"** and bracket a forward pointer ("(evaluated in Section N)") so the reader knows the assumption is not unbacked.
