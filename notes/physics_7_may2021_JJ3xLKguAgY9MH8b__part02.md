# Idea Flow Notes: physics_7_may2021_JJ3xLKguAgY9MH8b — X                                             X

## Paragraph Flow (move by move)

**Paragraph 1 — Acceleration block (xα then yα, displayed)**
1. **Equation move (definition of Newton's 2nd law on the axis):** "Fxα = maxα = Wxα" — declares force along xα equals mass times acceleration equals weight-component along xα. Hands the reader forward by *specifying the right-hand side* (now Wxα must be expanded).
2. **Unpack (geometric substitution):** "= W sin (α)" — replaces Wxα by the sine-component of the weight. Hands forward by *opening a slot for the magnitude of W*.
3. **Substitute (plug in W = mg):** "= −mg sin (α)" — inserts the sign convention. Hands forward by *isolating a (still wrapped in m)* so the reader expects the next line to cancel m.
4. **Consequence (solve for a):** "=⇒ axα = −g sin (α)" — algebraically divides through by m, the *final* form needed. Hands forward by *mirroring the procedure* in y (the y-block is set up by the same pattern).
5–8. **Parallel y-block:** "Fyα = mayα = Wyα" → "= W cos (α)" → "= −mg cos (α)" → "=⇒ ayα = −g cos (α)" — *copy-the-pattern move*; the same three substitutions, just a different trig ratio and a cosine sign.

**Paragraph 2 — Initial velocity components**
1. **Source citation + topic sentence:** "From Figure 2 the components of the initial velocity are:" — invokes the diagram and announces the next two displayed equations. Hands forward by *promising the values* that the reader reads below.

**Paragraph 3 — Initial position and justification of the kinematic equation**
1. **Condition (sets a numerical anchor):** "The initial position of the projectile is (0,0)." — fixes s₀ for the formula. Hands forward by *creating a need* for the s₀ slot of the equation that follows.
2. **Justification (cause → consequence):** "Since the acceleration is constant when looking at the direction separately, the Uniformly Accelerated Motion equations (3) can be used." — *because-condition → permitted tool*. Hands forward by *licensing the displayed equation* s = ut + ½at², which the reader then reads.

**Paragraph 4 — Substitution into the kinematic equation**
1. **Substitution action + announcement:** "Plugging in the accelerations and initial velocities gives the position equations in the xα- and yα-direction:" — verb-of-action plus a promise. Hands forward by *furnishing the slot values* that the two final equations fill in.

## What This Section Does (content sequence)

1. **Resolve the accelerations** (decompose weight along the tilted axes, then divide by mass). *Why first:* every later substitution needs a-component, and a cannot be written until F has been split.
2. **Resolve the initial velocities** (read them from the figure). *Why second:* u is independent of F, but both are needed simultaneously for the kinematic equation.
3. **State the initial position.** *Why third:* provides the integration constant the formula expects.
4. **Justify the kinematic formula** ("since a is constant…"). *Why fourth:* names the equation before it is used, so the substitution reads as derivation, not magic.
5. **Substitute and display the position functions.** *Why last:* this is the output the reader was building toward; everything earlier was setup.

Generalised: any 2-D constant-acceleration derivation follows **decompose accelerations → read initial velocities → fix origin → invoke s = ut + ½at² → substitute**.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Axis-by-axis acceleration derivation**
`For each axis, set the force equal to mass times acceleration and equal to the geometric weight component. Substitute the trig ratio for that component. Insert the sign from the chosen direction convention. Divide by mass to extract the acceleration component.`

1. *Slot shape:* four-line algebraic ladder per axis; second axis mirrors the first.
2. *Fill with a different idea:* pick a 2-D motion on a tilted line (e.g., a bead on a wire inclined at angle β). Replace "sin(α)" with whichever trig ratio projects the weight onto that axis (sin for along-the-slope, cos for perpendicular). Sign stays negative if the axis points away from gravity's pull along it.
3. *Original filled version:* "Fxα = maxα = Wxα / = W sin (α) / = −mg sin (α) / =⇒ axα = −g sin (α)."
4. *Demonstration fill (different idea):* A block sliding down a frictionless ramp at angle β, axis along the slope:
   "Fs = mas = Ws / = mg sin (β) / = +mg sin (β) / =⇒ as = +g sin (β)."
   (Perpendicular axis: "Fn = man = Wn / = mg cos (β) / = +mg cos (β) / =⇒ an = 0.")

**SKELETON B — Justifying and naming the kinematic equation**
`State the initial position. Since [condition that makes the kinematic formula valid], the [named kinematic equation] can be used.`

1. *Slot shape:* two sentences — first a condition (noun phrase), second a "Since… can be used" clause ending with the equation's number or name.
2. *Fill with a different idea:* pick any constant-acceleration 1-D motion. Slot 1 names s₀ (e.g., "The initial height of the drop is 0 m"). Slot 2 names the condition (constant a) and tags the equation ("equations (4)").
3. *Demonstration fill:* "The initial height of the ball is 0 m. Since the acceleration is constant and vertical, the Uniformly Accelerated Motion equations (4) can be used."

**SKELETON C — Substitution announcement**
`Plugging in [list of substituted quantities] gives the [output expressions] in each direction:`

1. *Slot shape:* one sentence, gerund verb, colon, then two parallel displayed equations.
2. *Fill with a different idea:* list every quantity just derived (initial speed component, acceleration component); name the output ("position equations", "velocity equations", etc.).
3. *Original:* "Plugging in the accelerations and initial velocities gives the position equations in the xα- and yα-direction:"
4. *Demonstration fill (different idea — horizontal projectile):* "Plugging in the accelerations and the initial velocity components gives the position equations in the x- and y-direction:"

## Express-Idea Vocabulary

- **Source citation:** "**From Figure 2** the components of the initial velocity are" — moves a quantity from diagram to algebra.
- **Conditional justification (cause → consequence):** "**Since** the acceleration is constant when looking at the direction separately, the Uniformly Accelerated Motion equations (3) **can be used**" — licenses the next equation.
- **Substitution verb:** "**Plugging in** the accelerations and initial velocities **gives**" — announces the algebra operation.
- **Mathematical implication arrow:** "**=⇒** axα = −g sin (α)" — marks the algebraic consequence step.
- **Specification of an output:** "the position equations **in the** xα- and yα-direction" — scopes the result.
- **Reference to a previously-tagged equation:** "Uniformly Accelerated Motion equations (3)" — back-link to the formula box.

## How to Explain an Idea (replication steps)

This section uses a **decomposition → condition → substitution** derivation pattern. To explain a new idea the same way:

1. **Decompose the forcing** along each independent axis, writing F = ma on each axis separately.
2. **Resolve the acceleration** on each axis by substituting the geometric component of the driving force and dividing by the mass.
3. **Read the initial kinematic quantities** (velocity components, starting position) from the problem's diagram or setup.
4. **Justify the formula** you will use — state the single physical condition that makes it valid (e.g., constant acceleration) and name the equation.
5. **Substitute** the resolved accelerations and initial velocities into the named equation, one axis at a time.
6. **Display the resulting functions** as a pair of parallel equations, labelling which axis each belongs to.
