# Idea Flow Notes: mathematics_7_november2016_6jvDzQbdmBzKpwM1 — Just as decreasing the step size in the Euler method increases the accuracy of the result, we will take the

## Paragraph Flow (move by move)

**Paragraph 1** (assumption justification — picking up from "take the limit")

1. **Move: Continuation / concluding-limit.** *"limit as Δ𝑡 → 0 to yield equations relating 𝐷 and 𝜃"* — restates the analytic procedure already introduced (the Euler-method analogy set up the take-the-limit move). Hands to next sentence by **specifying** what those equations will need to satisfy.
2. **Move: Assumption + justification.** *"we may intuitively expect 𝐷(𝑡) and cos 𝜃(𝑡) to be continuous and differentiable"* — installs the smoothness assumption. The "intuitively expect" framing (real-world physics) is what licenses the next clause: because we expect it, we *may assume* it. Hands to next sentence by **asserting the assumption is safe**.

**Paragraph 2** (geometric setup hand-off)

1. **Move: Scene-setting / transition to diagram.** *"Consider the situation at a time 𝑡, as shown in Figure 5."* — pivots from continuous assumption back to a discrete instant. Hands to next sentence by **fixing the moment** the reader must now inspect (the triangle on the left in the figure).

**Paragraph 3** (worked law application)

1. **Move: Method declaration.** *"Applying the cosine rule to the triangle on the left"* — names the tool. The reader is handed over by **naming which geometric object** the law will be applied to.
2. **Move: Object specification.** *"with sides 𝐷(𝑡), 𝑣_h Δ𝑡 and 𝑣_r Δ𝑡 + 𝐷(𝑡 + Δ𝑡)"* — lists the three side lengths in the exact order required by the cosine rule. Hands to next sentence by **finishing the inputs** so only the angle is left.
3. **Move: Final input + equation.** *"using the angle 𝜃(𝑡),"* — supplies the angle, then the equation follows deterministically. The handoff is **mechanical**: every input named, so the formula writes itself.

---

## What This Section Does (content sequence)

This is a **model-setup → assumption → diagram → law application** section. The order is:

1. **Close the limiting process** (so the reader knows the continuous model is in hand).
2. **State and justify the smoothness assumption** (so differentiation later is legal).
3. **Anchor the reader visually at one instant** ("Consider the situation at a time 𝑡").
4. **Name the geometric law** to be used.
5. **List the law's inputs in the order the law requires them.**
6. **Close with the angle** so the equation is fully determined.

WHY this order: each move hands the reader exactly the next prerequisite. The continuity assumption (2) is meaningless without knowing what functions are being smoothed (1). The diagram (3) cannot be analysed until a moment is fixed. The cosine rule (4) cannot be applied until the triangle and its sides are identified (5), and the angle must be the last ingredient (6) because it is what closes the formula. A student replicating this on a different topic should keep: *limit/assumption first, freeze one moment, pick a geometric law, then name its ingredients in the law's own order.*

---

## Paragraph Skeletons (replicable templates)

**SKELETON A — "smoothness assumption" paragraph**

SKELETON: *"Taking the [limiting process] yields [relations among the variables]. As the product of [real-world domain], we may intuitively expect [functions] to be [regularity property 1] and [regularity property 2], so we will assume this is the case."*

1. **Slot 1** — the closing of the analytic step (gerund phrase, present-tense, names the limit operation and what it relates). **Slot 2** — the justifying clause: "real-world physical kinematics" (a noun phrase naming the modelled domain). **Slot 3** — the pair of functions being smoothed (two mathematical objects, named with their argument). **Slot 4 + 5** — the regularity properties (adjective pair, e.g. continuous and differentiable). **Slot 6** — the assertion of the assumption (closing clause beginning "so we will assume").
2. **How to fill with a different idea:** Slot 1 — write the limit you are taking and the quantities it will relate (e.g. "Taking Δx → 0 yields a relation between frequency and wavelength"). Slot 2 — name the physical domain that licenses the expectation (e.g. "wave mechanics in a lossless medium"). Slot 3 — name the two time-dependent quantities (e.g. "the amplitude A(t) and phase φ(t)"). Slot 4/5 — pick the two regularity properties you need (continuous, differentiable, monotonic, bounded). Slot 6 — close with the assumption declaration.
3. **Original fill:** *"limit as Δ𝑡 → 0 to yield equations relating 𝐷 and 𝜃 (in fact cos 𝜃) over time. As the product of real-world physical kinematics, we may intuitively expect 𝐷(𝑡) and cos 𝜃(𝑡) to be continuous and differentiable, so we will assume this is the case."*
4. **Demonstration fill (different idea):** *"Taking Δx → 0 yields a relation between the wave's amplitude and wavelength. As the product of idealised wave propagation in a lossless medium, we may intuitively expect the displacement y(t) and velocity v(t) to be continuous and twice-differentiable, so we will assume this is the case."*

---

**SKELETON B — "freeze one moment" pivot sentence**

SKELETON: *"Consider the situation at [a specific instant/point], as shown in [Figure/ Diagram X]."*

1. **Slot 1** — the time or spatial slice (a noun phrase, e.g. "a time 𝑡"). **Slot 2** — the visual reference (e.g. "Figure 5").
2. **How to fill with a different idea:** Slot 1 — name the parameter value you want the reader to focus on (a single 𝑡, a single angle, a single cross-section). Slot 2 — point to the labelled diagram that depicts it.
3. **Original fill:** *"Consider the situation at a time 𝑡, as shown in Figure 5."*
4. **Demonstration fill:** *"Consider the configuration at an angle θ = π/6, as shown in Figure 2."*

---

**SKELETON C — "law application" paragraph**

SKELETON: *"Applying the [named law] to the [geometric object] [locator], with sides [side A], [side B] and [side C], using the angle [angle name], [equation]."*

1. **Slot 1** — the law (gerund "Applying the X"). **Slot 2** — the geometric object and its location ("triangle on the left", "sector in the upper half"). **Slot 3–5** — the three inputs the law needs, listed in the order the law requires them. **Slot 6** — the angle, as the closing input. **Slot 7** — the resulting displayed equation.
2. **How to fill with a different idea:** Slot 1 — pick a law with a fixed input order (cosine rule, sine rule, Pythagoras, vector dot product). Slot 2 — locate the object in the figure. Slot 3–5 — write the three quantities the law consumes, in the order its formula expects (longest side, adjacent, opposite — or whatever the rule dictates). Slot 6 — name the angle last. Slot 7 — write the formula with that exact ordering.
3. **Original fill:** *"Applying the cosine rule to the triangle on the left with sides 𝐷(𝑡), 𝑣_h Δ𝑡 and 𝑣_r Δ𝑡 + 𝐷(𝑡 + Δ𝑡), using the angle 𝜃(𝑡),"* followed by the equation.
4. **Demonstration fill:** *"Applying the sine rule to the upper triangle with sides R, r₁ and r₂, using the included angle φ, r₁ / sin α = R / sin β."*

---

## Express-Idea Vocabulary

- **Sequencing / process closing:** *"limit as Δ𝑡 → 0 to yield equations relating 𝐷"* — closes a limiting procedure.
- **Cause / consequence:** *"so we will assume this is the case"* — turns expectation into a working hypothesis (consequence-of-belief).
- **Authority / domain justification:** *"As the product of real-world physical kinematics"* — invokes the modelled domain as warrant.
- **Hedged claim:** *"we may intuitively expect"* — soft-modal claim that licenses a downstream assumption.
- **Transition / scene-setting:** *"Consider the situation at a time 𝑡"* — pivotal move to a frozen instant.
- **Tool / method verb:** *"Applying the cosine rule to the triangle"* — names the operative law.
- **Specification (parenthetic):** *"(in fact cos 𝜃)"* — narrows a previously loose variable to the form actually used.
- **Geometry vocabulary:** *"sides … using the angle"* — fixed positional phrasing for cosine-rule setup.
- **Implicit reference:** *"as shown in Figure 5"* — hands the visual load to the diagram rather than re-describing it.

---

## How to Explain an Idea (replication steps)

This section uses the pattern: **LIMIT → ASSUMPTION → FREEZE-INSTANT → NAMED-LAW → LISTED-INPUTS → EQUATION.**

Step-by-step replication for a new idea:

1. **Close the limiting/approximation process** in one phrase; state the limit parameter and what the equations it produces will relate. (E.g. "Taking Δx → 0 yields relations between A and B.")
2. **Insert a justifying clause beginning "As the product of [real-world domain]…"** — invoke the modelled physics to license the next step.
3. **State the regularity assumption on the functions involved**, using a soft modal ("we may intuitively expect") followed by the assumption declaration ("so we will assume this is the case"). This is what makes later calculus legal.
4. **Pivot with "Consider the situation at [single instant]"** — freeze the continuous motion at one parameter value so the reader can see geometry.
5. **Point to the diagram** ("as shown in Figure X") so the visual carries the descriptive load.
6. **Begin the worked step with "Applying the [named law]"** — never begin a law application without naming the law first.
7. **List the law's inputs in the exact order the formula expects them** (the cosine rule needs two sides then the included angle). Do not reorder.
8. **Close the paragraph with the displayed equation**, which falls out automatically once the inputs are named.

The rhythm is: *justify the maths, freeze the picture, pick the tool, feed the tool in order.*
