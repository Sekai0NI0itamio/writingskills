# Idea Flow Notes: mathematics_7_may2020_KupcNzdWlKMboMJM — Euler angles can be specified in different orders, and this order will change the final orientation of

## Paragraph Flow (move by move)

**Paragraph 1**

1. **Claim/reference** — "the mesh [8]." — Hands forward by anchoring the discussion to a concrete object (the mesh) that the previous section established; the citation [8] signals that the following explanation draws on a source.
2. **Mechanism** — "This is because each successive rotation contains all the previous rotations." — Answers *why* the mesh context matters by stating the cumulative property of successive rotations; this cause makes the next sentence about relevance follow.
3. **Transition/implication** — "This will be relevant later on." — Signals forward utility, creating suspense that primes the reader to accept the classification coming next.
4. **Claim/definition-introduction** — "Different orders of angles are given separate names." — Introduces the concept that rotation sequences have designated terminology, setting up the two categories to follow.
5. **Definition/evidence** — "Proper euler angles describe z-x-z, x-y-x, y-z-y, z-y-z, x-z-x, y-x-y orientations [8]." — Provides the first named category with its specific sequences; the citation and exhaustive list give the reader a complete, verifiable set.
6. **Definition/evidence** — "Tait-Bryan angles describe x-y-z, y-z-x, z-x-y, x-z-y, z-y-x, y-x-z orientations [8]." — Provides the second named category, completing the contrast established in sentence 5; the parallel structure makes the distinction immediately graspable.
7. **Specification/example** — "Within graphics processing, the order of angles is generally specified as y-z-x, which are Tait-Bryan angles." — Narrows from the general taxonomy to the specific domain convention, answering *which* type the reader should focus on.
8. **Contrast/concession** — "However, it should be noted that these are nonetheless referred to as Euler angles in graphics jargon." — Introduces a terminology conflict that complicates the clean distinction just drawn; this tension sets up the need for careful notation in the next paragraph.

**Paragraph 2**

1. **Claim** — "Every one of the three components of Euler angles can be expressed as matrices." — States the central proposition that each rotational component has a matrix form; this claim makes the forthcoming formulae a logical expectation rather than an arbitrary display.
2. **Context/setup** — "Assuming a, b and c are the angles for X, Y and Z respectively, the following formulae can be used [7]:" — Assigns variable names and signals the arrival of formal expressions; the citation establishes authority.
3. **Evidence** — The three matrix displays (X, Y, Z with their trigonometric entries and domain restrictions). — Provides the actual mathematical artefacts; the visual arrangement of three parallel matrices lets the reader compare the structure of each component side-by-side.
4. **Explanation/unpack** — "Again, the fourth column is included to allow the multiplication with the position matrix." — Explains the purpose of a structural element (the fourth column) that may seem arbitrary; the word "again" connects back to the cumulative-rotation logic of paragraph 1.
5. **Mechanism** — "The final rotation matrix can then be found by multiplying these components." — States the operation that combines the individual matrices; "then" marks this as the next logical step after understanding each component.
6. **Specification/example** — "For a y-z-x order, R = Y × Z × X, where R is the final rotation matrix that can be applied to all vertices." — Instantiates the general mechanism with the specific order established in paragraph 1, closing the loop between naming convention and mathematical realisation.

**Paragraph 3**

1. **Claim/transition** — "However, Euler (or Tait-Bryan) angles can be problematic as they can create a gimbal lock." — Introduces a limitation using "However" to contrast with the constructive tone of the previous paragraph; the problem name ("gimbal lock") is presented before it is explained.
2. **Mechanism/analogue-introduction** — "These can be explained using an object, such as a plane, in a gimbal." — Offers a physical model as the explanatory vehicle for the abstract problem; this choice of analogy sets up the concrete description to follow.
3. **Reference back** — "As aforementioned, each rotation also includes the previous rotations." — Recalls the cumulative-rotation principle from paragraph 1, making the failure mechanism a direct consequence of a property already accepted by the reader.
4. **Evidence/unpack** — "It some cases, this can lead to two "gimbals" aligning with each other, often when angles approach π2 radians." — Specifies the precise condition under which the failure occurs; the threshold (π/2) gives the reader a quantitative boundary.
5. **Evidence reference** — "This is shown in figure 5." — Points to visual proof; this sentence makes the figure a required piece of the argument rather than an illustration.
6. **Label** — "Figure 5: A gimbal lock on an aeroplane [4]." — Identifies the visual artefact and its source; the aeroplane confirms the analogy introduced in sentence 2.

**Paragraph 4**

1. **Evidence/description** — "Here, two gimbals are aligned horizontally." — Describes what the reader should see in the figure; "here" anchors the sentence to the visual just referenced.
2. **Unpack/implication** — "As such, one gimbal is "lost", they are "stuck together", and rather than being able to move three gimbals, only two can be used." — Explains the practical consequence of the alignment; the quotation marks around "lost" and "stuck together" convey the functional meaning of the failure.
3. **Explanation/implication** — "Mathematically speaking, this means that in this scenario one dimension is lost." — Translates the physical observation into an abstract mathematical consequence; "mathematically speaking" signals a shift from the analogue to the formal domain.
4. **Evaluation** — "This is undesireable, as rotations often need to be three dimensional." — States the normative judgment that motivates the search for an alternative; the justification (3D requirement) makes the problem concrete.
5. **Verdict/decision** — "While it is possible to solve my problem with Euler angles, I will be using quaternions instead, as these are guaranteed to work for anyting without creating gimbal locks." — Announces the chosen solution and its justification; "while" concedes Euler angles are not universally broken, but the guarantee of quaternions overrides that partial adequacy.

---

## What This Section Does (content sequence)

1. **Names and distinguishes the types of rotation orders** (proper Euler vs. Tait-Bryan) and specifies which one graphics uses — this establishes the *vocabulary* the reader needs before any mathematics appears.
2. **Expresses each component as a matrix and shows how to compose them** — this converts the named conventions into *operational tools*, answering "how do I actually compute with these angles?"
3. **Introduces the failure mode (gimbal lock) and explains it through a physical analogue** — this reveals *why the tools from step 2 are insufficient*, creating a problem that demands a solution.
4. **Translates the physical failure into a mathematical consequence and decides on an alternative method** — this closes the section by *resolving the problem* the reader now understands, justifying the shift to quaternions.

**Why this order:** Step 1 must come first because the matrices in step 2 reference named rotation orders (y-z-x) that the reader must already recognise. Step 2 must precede step 3 because the gimbal lock explanation depends on the cumulative-rotation property that the matrix section formalises. Step 3 must precede step 4 because the decision to use quaternions is only motivated once the reader has accepted that Euler angles can lose a degree of freedom. A student replicating this sequence with a different topic should follow: *name the items → show how they work mechanically → expose a failure condition → choose an alternative*.

---

## Paragraph Skeletons (replicable templates)

**Skeleton 1 — Taxonomy-and-convention paragraph**

```
"[Prior-context fragment]. This is because [cumulative/general principle]. This will be [forward-relevance signal]. [Category-distinction claim]: [Type A] describes [list A]; [Type B] describes [list B]. Within [specific domain], [specific instance] is generally used, which are [Type B]. However, [concession about terminology confusion]."
```

1. **Slot shapes:** Slot 1 — noun phrase fragment acting as a topic carry-over; Slot 2 — "because"-clause stating a general property; Slot 3 — future-tense relevance statement; Slot 4 — plural-noun subject introducing a distinction; Slot 5 — two parallel "[noun] describe [list]" clauses joined by a semicolon; Slot 6 — prepositional phrase narrowing to a domain, followed by a relative clause identifying the type; Slot 7 — concessive "however" clause about naming.
2. **How to fill differently:** Slot 1: pick a carry-over noun phrase from your prior section (e.g., "the dataset [3]"). Slot 2: state a general property that justifies the carry-over (e.g., "This is because each variable depends on all previous transformations."). Slot 3: signal forward relevance (e.g., "This will be essential for the analysis below."). Slot 4: introduce your classification (e.g., "Different scaling methods are given separate names."). Slot 5: list the two categories with their members (e.g., "Linear scaling describes min-max and z-score normalisation; logarithmic scaling describes log-transform and power-transform."). Slot 6: specify your domain's convention (e.g., "Within machine learning, the min-max approach is generally preferred, which are linear scaling methods."). Slot 7: add a naming caveat (e.g., "However, it should be noted that these are nonetheless referred to as normalization in some frameworks.").
3. **Original filled version:** "the mesh [8]. This is because each successive rotation contains all the previous rotations. This will be relevant later on. Different orders of angles are given separate names. Proper euler angles describe z-x-z, x-y-x, y-z-y, z-y-z, x-z-x, y-x-y orientations [8]. Tait-Bryan angles describe x-y-z, y-z-x, z-x-y, x-z-y, z-y-x, y-x-z orientations [8]. Within graphics processing, the order of angles is generally specified as y-z-x, which are Tait-Bryan angles. However, it should be noted that these are nonetheless referred to as Euler angles in graphics jargon."
4. **Different-fill demonstration:** "the dataset [3]. This is because each variable depends on all previous transformations. This will be essential for the analysis below. Different scaling methods are given separate names. Linear scaling describes min-max and z-score normalisation; logarithmic scaling describes log-transform and power-transform. Within machine learning, the min-max approach is generally preferred, which are linear scaling methods. However, it should be noted that these are nonetheless referred to as normalization in some frameworks."

---

**Skeleton 2 — Formalisation-and-composition paragraph**

```
"[Universal claim about representability]. Assuming [variables] are [quantities], the following [artefacts] can be used [citation]. [Explanation of a structural component's purpose]. The [composite result] can then be found by [operation]. For [specific instance], [formula], where [result] is [application]."
```

1. **Slot shapes:** Slot 1 — universal claim using "every/none/all" + noun phrase + modal "can be" verb; Slot 2 — "assuming" clause defining variables, followed by a colon introducing artefacts; Slot 3 — "again"/"additionally" + explanation of a structural element; Slot 4 — composite-result sentence using "can then be found by"; Slot 5 — "For [order], [equation], where [symbol] is [description]" specification.
2. **How to fill differently:** Slot 1: state that every element of your subject has a formal representation (e.g., "Every one of the three forces can be resolved into components."). Slot 2: define your variables and introduce the equations (e.g., Assuming Fx, Fy and Fz are the magnitudes along the three axes, the following equations can be used [1]:). Slot 3: explain a structural feature (e.g., "Again, the negative signs account for directional opposition."). Slot 4: state the combination rule (e.g., "The resultant force can then be found by vector addition."). Slot 5: give the specific case (e.g., "For a horizontal surface, R = Fx + Fy, where R is the resultant that can be applied to the free-body diagram.").
3. **Original filled version:** "Every one of the three components of Euler angles can be expressed as matrices. Assuming a, b and c are the angles for X, Y and Z respectively, the following formulae can be used [7]: [matrix display]. Again, the fourth column is included to allow the multiplication with the position matrix. The final rotation matrix can then be found by multiplying these components. For a y-z-x order, R = Y × Z × X, where R is the final rotation matrix that can be applied to all vertices."
4. **Different-fill demonstration:** "Every one of the three forces can be resolved into components. Assuming Fx, Fy and Fz are the magnitudes along the three axes, the following equations can be used [1]: [equation display]. Again, the negative signs account for directional opposition. The resultant force can then be found by vector addition. For a horizontal surface, R = Fx + Fy, where R is the resultant that can be applied to the free-body diagram."

---

**Skeleton 3 — Problem-exposure-and-decision paragraph**

```
"However, [technique] can be problematic as they can [failure mode]. These can be explained using [analogue], in [context]. [Cumulative-principle reference]. In [condition], this can lead to [failure state], often when [threshold]. [Visual evidence reference]. Here, [description of failure in the analogue]. As such, [practical consequence]. Mathematically speaking, this means [abstract consequence]. This is undesirable, as [requirement]. While [partial-solution], I will use [alternative], as these [guaranteed benefit]."
```

1. **Slot shapes:** Slot 1 — concessive "however" clause naming the technique and its failure mode; Slot 2 — "explained using" clause introducing the physical analogue; Slot 3 — "as aforementioned" clause recalling a prior principle; Slot 4 — "in some cases" clause describing the failure with a quantitative threshold; Slot 5 — figure-reference sentence; Slot 6 — "here" sentence describing the visual; Slot 7 — "as such" sentence stating the practical loss; Slot 8 — "mathematically speaking" sentence stating the abstract loss; Slot 9 — "this is undesirable" sentence with a justification; Slot 10 — "while...I will" decision sentence with a guarantee.
2. **How to fill differently:** Slot 1: name your technique and its key failure (e.g., "However, linear regression can be problematic as it can produce overfitting."). Slot 2: introduce an analogy (e.g., "These can be explained using a curve, such as a high-degree polynomial, fitted to data points."). Slot 3: recall a prior principle (e.g., "As aforementioned, each additional term increases the model's complexity."). Slot 4: specify the failure condition (e.g., "In some cases, this can lead to the curve passing through every point, often when the degree approaches the number of data points."). Slot 5: figure reference (e.g., "This is shown in figure 3."). Slot 6: describe the visual (e.g., "Here, the curve oscillates wildly between points."). Slot 7: practical consequence (e.g., "As such, the model captures noise rather than signal."). Slot 8: abstract consequence (e.g., "Mathematically speaking, this means the variance of predictions becomes arbitrarily large."). Slot 9: why it matters (e.g., "This is undesirable, as predictions often need to generalise to new data."). Slot 10: decision (e.g., "While it is possible to solve my problem with linear regression, I will use regularisation instead, as these are guaranteed to reduce overfitting without eliminating the linear relationship.").
3. **Original filled version:** "However, Euler (or Tait-Bryan) angles can be problematic as they can create a gimbal lock. These can be explained using an object, such as a plane, in a gimbal. As aforementioned, each rotation also includes the previous rotations. It some cases, this can lead to two "gimbals" aligning with each other, often when angles approach π2 radians. This is shown in figure 5. Here, two gimbals are aligned horizontally. As such, one gimbal is "lost", they are "stuck together", and rather than being able to move three gimbals, only two can be used. Mathematically speaking, this means that in this scenario one dimension is lost. This is undesireable, as rotations often need to be three dimensional. While it is possible to solve my problem with Euler angles, I will be using quaternions instead, as these are guaranteed to work for anyting without creating gimbal locks."
4. **Different-fill demonstration:** "However, linear regression can be problematic as it can produce overfitting. These can be explained using a curve, such as a high-degree polynomial, fitted to data points. As aforementioned, each additional term increases the model's complexity. In some cases, this can lead to the curve passing through every point, often when the degree approaches the number of data points. This is shown in figure 3. Here, the curve oscillates wildly between points. As such, the model captures noise rather than signal. Mathematically speaking, this means the variance of predictions becomes arbitrarily large. This is undesirable, as predictions often need to generalise to new data. While it is possible to solve my problem with linear regression, I will use regularisation instead, as these are guaranteed to reduce overfitting without eliminating the linear relationship."

---

## Express-Idea Vocabulary

**Sequencing:**
- "This will be relevant later on." — signals that a property carries forward importance, making the next classification feel purposeful.
- "Again, the fourth column is included to allow the multiplication with the position matrix." — "Again" marks this as a repeated or reinforcing point, sequencing it after the matrix display.

**Cause/consequence:**
- "This is because each successive rotation contains all the previous rotations." — "because" establishes a causal explanation for the mesh reference.
- "The final rotation matrix can then be found by multiplying these components." — "can then be found by" marks composition as the direct consequence of understanding the individual matrices.
- "this can lead to two "gimbals" aligning with each other" — "can lead to" expresses the consequence of cumulative rotations under threshold conditions.
- "this means that in this scenario one dimension is lost" — "means that" translates the physical observation into a mathematical consequence.

**Contrast/concession:**
- "However, it should be noted that these are nonetheless referred to as Euler angles in graphics jargon." — "However...nonetheless" concedes that the clean Tait-Bryan classification is complicated by graphics terminology.
- "However, Euler (or Tait-Bryan) angles can be problematic as they can create a gimbal lock." — "However" pivots from the constructive matrix section to a limitation.
- "While it is possible to solve my problem with Euler angles, I will be using quaternions instead" — "While" concedes partial adequacy of Euler angles before rejecting them.

**Specification:**
- "Within graphics processing, the order of angles is generally specified as y-z-x, which are Tait-Bryan angles." — "Within...generally specified as" narrows the general taxonomy to a domain-specific convention.
- "For a y-z-x order, R = Y × Z × X" — "For...order" instantiates the general matrix-composition rule with a specific sequence.

**Evidence handling:**
- "These can be explained using an object, such as a plane, in a gimbal." — "can be explained using" introduces a physical model as explanatory evidence for an abstract problem.
- "This is shown in figure 5." — "is shown in" directs the reader to visual evidence.
- "Figure 5: A gimbal lock on an aeroplane [4]." — figure label with citation anchors the visual to a source.

**Explanation verbs:**
- "can be expressed as matrices" — "expressed as" frames the translation from angles to matrix form.
- "is included to allow the multiplication" — "is included to allow" explains the functional purpose of a structural element (the fourth column).
- "can be problematic as they can create" — "can be problematic" introduces a failure mode as an explanation of limitation.

---

## How to Explain an Idea (replication steps)

**The pattern this section relies on:** *Convention → Formalisation → Failure exposure → Analogical unpacking → Mathematical translation → Decision.* This is a "establish what it is → show how it works → reveal how it breaks → translate the break → decide what replaces it" pattern.

**Step-by-step instructions to explain a NEW idea with the same pattern:**

1. **Name and classify the items** you are explaining: state what the things are called and distinguish the subtypes, then specify which subtype your domain uses and acknowledge any naming confusion that exists.
2. **State that each component can be represented formally** and define your variables; present the formal artefacts (equations, matrices, diagrams) with a citation, then explain the purpose of any structural element that might seem arbitrary.
3. **State the composite operation** that combines the individual formal artefacts into a single result, and instantiate it with the specific case relevant to your domain.
4. **Pivot with "however"** to introduce the failure mode of the technique you just formalised, and offer a physical or visual analogue that makes the failure intuitively graspable.
5. **Recall the cumulative or structural principle** from step 2 that causes the failure, then specify the precise condition (often a numerical threshold) under which the failure occurs and reference a figure that demonstrates it.
6. **Describe what the failure looks like** in the analogue, state the practical consequence, then translate that consequence into an abstract mathematical loss.
7. **State why the loss is undesirable** by referencing the requirement the technique was supposed to satisfy, then announce your chosen alternative and the guarantee it provides that the original technique could not.
