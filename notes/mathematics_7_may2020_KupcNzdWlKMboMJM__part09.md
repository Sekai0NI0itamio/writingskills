# Idea Flow Notes: mathematics_7_may2020_KupcNzdWlKMboMJM — Finally, all the vertices can be transformed by multiplying the position matrices by the rotation matrix

## Paragraph Flow (move by move)

**Paragraph 1** (notation → matrices)

- **Move 1 — Purpose fragment (carry-over).** *"in order to form the new vertex positions."* This is the tail of the prior sentence; it names the *purpose* of the multiplication. It hands the reader to the next sentence by stating *what is being produced*, so the next sentence must specify *what that product looks like*.
- **Move 2 — Notation declaration + evidence pointer.** *"The new position matrix will again be denoted as *, and are shown in equations 13 and 14."* This sentence does two jobs in one breath: it re-introduces the symbol convention (recalling an earlier use) and points the reader to the visual proof that follows. It hands the reader to the matrices by promising "here is what the symbols actually contain."
- **Move 3 — Evidence (visual worked calculation).** The eight 4×1 column matrices labelled *A\* = R × A*, *B\* = R × B*, ..., *H\* = R × H* displayed as equations 13 and 14. Each one *shows the mechanism*: original vertex multiplied by rotation matrix equals new position. The hand-off is *demonstration → reader can now accept the result as established fact*.

**Paragraph 2** (verdict → next step)

- **Move 4 — Verdict / completion statement.** *"Now that the vertices of a scaled and rotated cube have been found, the mesh is complete."* This is a *consequence sentence*: it takes the eight computed matrices as sufficient evidence and closes off the sub-task. It hands the reader forward by declaring *nothing more is owed on the vertex side*, which licences a pivot to a new sub-task.
- **Move 5 — Transition to next procedure.** *"The final step is to group vertices together to form 12 equal area triangles."* This is a *next-step declaration*. It hands the reader to the next section by naming exactly what must now be done, with the count (12) specifying the scope so the next writer knows the target quantity.

## What This Section Does (content sequence)

This is a **worked-calculation section within a procedure**. The ordered moves are:

1. **Purpose fragment** (what the upcoming calculation is for) — sets up the reader's expectation so they read the matrices as an *answer*, not a puzzle.
2. **Notation + reference pointer** — names the symbol the matrices will use and tells the reader where to look (equations 13/14); this prevents the equations from looking orphaned.
3. **Worked calculation laid out visually** — shows the mechanism *input × transformation = output* one vertex at a time, so the reader can verify the method without the writer narrating every multiplication.
4. **Completion verdict** ("the mesh is complete") — collapses eight repeated calculations into a single accepted fact, closing the sub-task.
5. **Forward declaration** ("the final step is to ...") — names the *next* sub-task with its target quantity, handing the reader to the next section cleanly.

**Why this order works:** the purpose justifies the calculation → the notation frames the calculation → the equations are the calculation → the verdict confirms the calculation → the forward declaration pivots. Removing or reordering any move either leaves the matrices unmotivated (drop the purpose) or leaves the reader with no idea what comes next (drop the forward declaration).

## Paragraph Skeletons (replicable templates)

### Skeleton A — Notation-then-Worked-Calculation Paragraph

**SKELETON:** "[Carry-over purpose phrase]. The [output object] will again be denoted as [symbol], and are shown in [reference label]. [Series of equations showing original × transformation = result]."

1. **Slot roles:**
   - Slot 1: tail fragment stating *why* the next sentence exists (no full verb needed — purpose infinitive).
   - Slot 2: naming convention + explicit reference to where the evidence lives. Grammatical shape: *The [noun] will again be denoted as [symbol], and are shown in [reference].*
   - Slot 3: visual worked evidence — a list of equations pairing each input with its transformed output.
2. **How to fill with a different idea:** pick a procedure that produces a new named object from an existing one via a fixed operation (e.g. "rotate," "scale," "translate," "differentiate"). Decide on the symbol convention (asterisk, prime, subscript) and the equation-number range. Then enumerate every instance of the operation and display each as its own one-line equation, keeping the layout symmetric (input | transform | output) so the reader can scan down the column.
3. **Original filled version:** *"in order to form the new vertex positions. The new position matrix will again be denoted as *, and are shown in equations 13 and 14."* + the eight A\*–H\* matrix equations.
4. **Demonstration fill with a different idea:** *"in order to compute the rotated normal vectors. The rotated normal will again be denoted as n′, and are shown in equations 7 and 8. n′₁ = R × n₁ = [...], n′₂ = R × n₂ = [...]..."* (different subject — surface normals of a mesh after rotation — same skeleton.)

### Skeleton B — Verdict-then-Next-Step Paragraph

**SKELETON:** "Now that the [plural artefacts] have been [verb of completion], the [larger construct] is complete. The final step is to [next action] to form [count + description]."

1. **Slot roles:**
   - Slot 1: temporal-causal hinge ("Now that... have been found") plus completion claim. Grammatical shape: *Now that the [X]s have been [verb]-ed, the [Y] is complete.*
   - Slot 2: pointer to the next sub-task with a *count* embedded so scope is explicit. Grammatical shape: *The final step is to [infinitive verb] to form [number] [noun phrase].*
2. **How to fill with a different idea:** after finishing a repeated operation, name the unit that was just finished (vertices, samples, terms, points) and the larger object those units together constitute. Then announce the single remaining action and quantify its output ("form 12 triangles," "produce 6 equations," "draw 4 faces") so the reader knows what success looks like.
3. **Original filled version:** *"Now that the vertices of a scaled and rotated cube have been found, the mesh is complete. The final step is to group vertices together to form 12 equal area triangles."*
4. **Demonstration fill with a different idea:** *"Now that the eigenvalues of the covariance matrix have been computed, the principal components are determined. The final step is to project each data point onto the eigenvectors to form a 2-dimensional scatter plot."* (PCA setup — same skeleton, different domain.)

## Express-Idea Vocabulary

- **Sequencing / hinge:** *"Now that the vertices... have been found"* — opens a closure sentence by treating the prior block as a finished premise.
- **Re-introduction of a symbol:** *"will again be denoted as \*"* — signals to the reader that a convention used earlier is being reused, so the matrices don't feel like new notation.
- **Evidence handling / pointer:** *"are shown in equations 13 and 14"* — delegates the visual proof to a labelled location rather than narrating it inline.
- **Transition to next sub-task:** *"The final step is to"* — names the action about to happen and marks it as the last in the sequence.
- **Specification of scope:** *"to form 12 equal area triangles"* — embeds the target count directly into the verb phrase so the next writer/reader has a measurable goal.
- **Verdict verb:** *"the mesh is complete"* — closes the sub-task with a binary status claim rather than a soft "we now have."

## How to Explain an Idea (replication steps)

The pattern this section relies on is **notation-first worked calculation → completion verdict → forward pointer**. To replicate it for a new idea:

1. **Open with the purpose fragment** — name what the calculation is *for* in one tail clause ("in order to ... "). This tells the reader why the coming symbols matter.
2. **Declare the notation and its home** — choose a symbol convention that already appeared earlier ("will again be denoted as ..."), then point to where the evidence will sit ("are shown in equations X and Y").
3. **Lay out the worked calculation visually, one instance per line** — display *every* application of the operation (input × operator = output) as its own equation, using a consistent left-aligned layout so the reader can scan down the column and confirm the method is uniform.
4. **Collapse the worked set into one verdict sentence** — after the equations, use a *Now that ... have been found, the [larger thing] is complete* sentence. This converts eight equations into a single accepted fact and signals the sub-task is done.
5. **Pivot with a forward declaration** — finish with *The final step is to [infinitive] to form [count] [object]* so the reader knows exactly what the next section must deliver and in what quantity.
