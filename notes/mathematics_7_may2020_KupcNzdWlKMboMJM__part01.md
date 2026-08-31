# Idea Flow Notes: mathematics_7_may2020_KupcNzdWlKMboMJM — Because graphics processing units work with two dimensional triangles, the cube needs to be split up

## Paragraph Flow (move by move)

**Paragraph 1** (decomposition reasoning)

1. **Sentence 1** — "into its faces." — *Continuation/elaboration move*: completes a prior sentence about splitting. Hands reader on by introducing the next decomposition step in the same chain.
2. **Sentence 2** — "A cube has six faces, each of which can be split up again" — *Definition + mechanism*: states the object's face count and the recursive splitting rule. Hands reader on by quantifying ("six faces" + "two triangles") so the multiplication can happen next.
3. **Sentence 3** — "a cube consists of 36 individual vertices, duplicates of 8 unique vertices." — *Calculation/consequence move*: produces totals from the prior quantities (6×2×3=36 vs 8 unique). Hands reader on by setting up a contrast between the two numbers.
4. **Sentence 4** — "Only the unique vertices will be calculated for performance reasons, but all 36 need to be specified in OpenGL." — *Implication/tension move*: introduces two opposing requirements that follow from the 36-vs-8 split.

**Paragraph 2** (figure caption — separate move)

5. **Caption** — "Diagram representing the vertices in a 3D OpenGL coordinate system" — *Labelling move*: tells the reader what to look for in the upcoming figure; bridges paragraph 1's numbers to paragraph 3's figure.

**Paragraph 3** (figure-to-equation hand-off)

6. **Sentence 1** — "Figure 3 shows the 8 unique verices A to H graphically." — *Reference/evidence move*: visualises the "8 unique" count from paragraph 1. Hands reader on by naming a specific vertex for anchoring.
7. **Sentence 2** — "The vertex C is located at the origin." — *Specification move*: anchors one vertex to a known reference point, which lets coordinates of the others be understood relative to it. Hands reader on by making the matrices interpretable.
8. **Sentence 3** — "the matrices I defined for the vertices are shown in equations 1 and 2." — *Transition move*: hands the reader from the verbal/visual description into formal mathematical representation.

## What This Section Does (content sequence)

This is a **technical-decomposition setup** section. The ordered moves are:

1. **State the external constraint** (GPUs only render triangles) — sets up *why* decomposition is needed.
2. **Apply the decomposition recursively** (cube → faces → triangles → vertices) — produces a count.
3. **Compute the totals and the unique subset** (36 vs 8) — establishes the working numbers.
4. **Surface a tension between two requirements** (calculate 8 for speed, specify 36 for OpenGL) — frames the engineering compromise.
5. **Introduce a figure that visualises the unique set** — grounds the abstract count.
6. **Anchor one element to a reference** (vertex C at origin) — gives coordinates meaning.
7. **Move to formal notation** (matrices/equations) — shifts from prose to computation.

The order works because each move supplies the *count or label* the next move needs: the constraint justifies the split, the split yields the counts, the counts justify the figure, the figure justifies the matrices, and the origin-anchor makes those matrices readable.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Constraint-driven decomposition with tension"**
> "[Context phrase tying to prior sentence]. A [object] has [N primary parts], each of which can be split up again into [M sub-parts]. As such, a [object] consists of [N×M×K] individual [units], duplicates of [smaller unique count] unique [units]. Only the unique [units] will be [action A] for [reason], but all [total count] need to be [action B] in [system]."

1. **Slot 1 (continuation hook)**: a prepositional phrase finishing a previous sentence; keep it short, present participle or prepositional.
2. **Slot 2 (decomposition rule)**: count primary parts, then state recursive split — past/present tense, declarative.
3. **Slot 3 (tension statement)**: contrast clause introduced by "but"; one clause per competing requirement.
4. **Original filled**: "into its faces. A cube has six faces… split up again into two equal-sized triangles. As such, a cube consists of 36 individual vertices, duplicates of 8 unique vertices. Only the unique vertices will be calculated for performance reasons, but all 36 need to be specified in OpenGL."
5. **Demonstration fill (different idea)**: "into its layers. A Sierpinski tetrahedron has four faces, each of which can be split up again into three smaller triangles. As such, the first iteration consists of 12 individual triangles, duplicates of 6 unique triangles. Only the unique triangles will be cached for render speed, but all 12 need to be submitted to the shader pipeline."

**SKELETON B — "Figure reference with origin-anchor then formal handoff"**
> "Figure [N] shows the [count] [items] [label range] graphically. The [item] [single label] is located at the origin. As such, the [formal structures] I defined for the [items] are shown in equations [range]."

1. **Slot 1 (figure reference)**: present tense, name the figure, state count + label range.
2. **Slot 2 (anchor)**: pick ONE item from the set and locate it at a known reference (origin, axis intersection).
3. **Slot 3 (formal handoff)**: "As such" + "I defined" + equation range; first person to mark ownership of the formalisation.
4. **Original filled**: "Figure 3 shows the 8 unique verices A to H graphically. The vertex C is located at the origin. As such, the matrices I defined for the vertices are shown in equations 1 and 2."
5. **Demonstration fill**: "Figure 5 shows the 6 unique force vectors F₁ to F₆ graphically. The vector F₃ is located at the origin. As such, the coefficient tensors I derived for the vectors are shown in equations 7 and 8."

**SKELETON C — "Figure caption as bridging label"**
> "Figure [N]: [Generic object] representing the [items] in a [system] coordinate system"

1. **Slot 1 (figure number)** + **Slot 2 (what is shown)** + **Slot 3 (the system/frame it sits in)**.
2. **Original filled**: "Figure 3: Diagram representing the vertices in a 3D OpenGL coordinate system."
3. **Demonstration fill**: "Figure 7: Schematic representing the eigenvalues in a 2D Markov state space."

## Express-Idea Vocabulary

**Sequencing / consequence**
- "As such, a cube consists of 36 individual vertices" — marks a derivation step from the prior count.
- "As such, the matrices I defined for the vertices are shown" — marks that the next item follows because of the anchor.

**Specification / narrowing**
- "each of which can be split up again into two equal-sized triangles" — refines the general rule to a concrete number.

**Contrast / concession**
- "but all 36 need to be specified in OpenGL" — sets up the competing requirement against "only the unique vertices will be calculated."

**Evidence handling**
- "Figure 3 shows the 8 unique verices A to H graphically" — invokes the visual as evidence for the verbal claim.

**Explanation verbs / definitional**
- "can be split up again" — recursive decomposition verb.
- "consists of 36 individual vertices, duplicates of 8 unique vertices" — composition + uniqueness claim.

**Reference / hand-off**
- "is located at the origin" — anchors a member to a known point.
- "are shown in equations 1 and 2" — moves the reader into the next representational mode.

## How to Explain an Idea (replication steps)

This section uses a **constraint → decomposition → count → tension → visual → anchor → formal** chain. To replicate:

1. **Name the external constraint** that forces you to break the object into smaller pieces (e.g. "GPUs render triangles").
2. **Decompose hierarchically** — state the primary part count, then state the recursive split rule (faces → triangles → vertices).
3. **Compute two counts**: the total number of raw units AND the number of unique units, and put them in the same sentence.
4. **State the engineering tension**: one requirement wants only the unique set (speed), another wants the full set (correctness/specification).
5. **Reference a figure** that visualises the unique subset, using a label range ("A to H").
6. **Pick one labelled element and anchor it** to a known reference (origin, axis, fixed datum).
7. **Hand off to formal notation** ("As such, the [matrices/equations] I defined… are shown in equations X and Y") so the reader knows the next object is the formal model.

The pattern works because each step supplies the *number, label, or anchor* the next step needs to be readable.
