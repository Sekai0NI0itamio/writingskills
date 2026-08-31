# Idea Flow Notes: mathematics_6_may2021_sdYkU1ovgvQz8NpA — C                 C

## Paragraph Flow (move by move)

**Paragraph 1** (interpretive reflection)

1. **Transition / rhetorical pivot.** *"Well, but what does this mean?"* — Returns the reader to a previous result and signals that an interpretation move is coming. Hands to S2 by demanding a verdict on the just-raised question.
2. **Verdict.** *"This is a very, very interesting result."* — Stamps the result with the writer's evaluation. Hands to S3 because a verdict on "interesting" requires stating *what* is interesting about it.
3. **Claim / recall.** *"I know that the catenoid equation must be equal to the radius ri"* — Re-states the surprising equality. Hands to S4 by setting up the premise that "However" will now qualify.
4. **Concession / unpack.** *"However, radius, which is a constant and the boundary condition of my equation, does not affect the derivative."* — Disrupts the reader's likely assumption (that changing r changes everything). Hands to S5 by leaving a consequence dangling ("does not affect" → "so what follows?").
5. **Implication / specification.** *"This means that the derivative of the catenoid equation must apply to all catenoids with different radii, that is, it must show the solution to all possible maximum distances x = α of different ri."* — Converts the concession into a powerful generalisation. Hands to S6 because an abstract generalisation cries out for a picture.
6. **Evidence directive.** *"Consider Figure 6 with different ri = C cosh(C/α) and equation 21 to visualise this relationship:"* — Points the reader at a figure to make the generalisation tangible.

**Paragraph 2** (procedural / empirical)

1. **Method limitation (cause).** *"Finding the intersections between equation 21 and the catenoid equation is not solvable by hand, as isolating α or C is not possible."* — States why a closed-form path is blocked. Hands to S2 because the block demands a substitute procedure.
2. **Procedure move.** *"Solving for the 2 using technology for all ri grants me the solutions for αi in the table below."* — Adopts technology to obtain αi. Hands to S3 because getting αi alone does not test anything — a comparator is needed.
3. **Comparator procedure.** *"To test whether the hypothesised αi breaking distance is the same, I have recorded the breaking distances of my soap film in real life…"* — Introduces empirical βi so αi can be checked. Hands to S4 because the new symbol βi must be operationalised.
4. **Operational definition.** *"The recorded distance was denoted to be βi (By measuring the distance between two rings and dividing by 2 on the breaking frame. See Appendix A for the recordings)."* — Fixes how βi is measured so the table is reproducible.

**Paragraph 3** (table) — Evidence display; hands to Paragraph 4 because raw numbers invite evaluation.

**Paragraph 4** (handoff + open problem)

1. **Forward pointer.** *"The evaluation of these results can be found in section 4."* — Defers judgement. Hands to S2 by acknowledging that the present section is closed off.
2. **Achievement recap + new puzzle.** *"Whilst I was able to find an equation to solve for all αi and the breaking distance, I have yet to understand why for any distance |α| < αi I have 2 solutions."* — Caps what was done, then flags an unresolved anomaly. The cut-off "Since the" launches the next section.

## What This Section Does (content sequence)

This is an **interpretation → method → evidence → deferred-evaluation → open-question** section. The ordered moves are:

1. **Re-interpret the prior algebraic result** (what does the equality *mean*?). This sets up the need to act on the insight.
2. **Generalise the result** to a family of cases (all ri). This sets up that one figure cannot stand alone — many curves are needed.
3. **Display the generalisation visually** (Figure 6). This makes the abstract consequence concrete so the reader can see the comparison.
4. **Admit analytical intractability** (cannot solve by hand). This *necessitates* the next move.
5. **Adopt a computational substitute** to obtain αi for all ri. This produces numbers that can be tested.
6. **Design an empirical comparator** (βi from real soap film) so αi has something to be checked against. This sets up the table.
7. **Display the comparison** in a table with percentage error. This is the evidence payload.
8. **Defer the verdict** to a later evaluation section, signalling that the present section's job is to *produce* and *gather*, not to judge.
9. **Surface a residual anomaly** (two solutions for |α| < αi) to motivate the next section.

The order is forced: interpretation must come before method (you cannot compute what you haven't understood); the method must come before evidence (you cannot tabulate what you haven't solved); evidence must precede its evaluation; and evaluation must precede the new anomaly (you only notice the anomaly once the work above is closed).

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Re-interpreting a surprising equality"**

> [Rhetorical pivot back to a previous result]. This is a [evaluative adjective] result. I know that [A] must be equal to [B]. However, [B], which is a [qualifier] and the [role] of my equation, does not affect [the derivative/quantifier being discussed]. This means that [the derivative] must apply to all [family] with different [parameter], that is, it must show the solution to all possible [outputs] of different [parameter]. Consider [Figure X] with [parameter] = [formula] to visualise this relationship:

- Slot 1 (rhetorical pivot): a short question, often "Well, but what does this mean?" — rhetorical, end with question mark.
- Slot 2 (verdict): one short evaluative sentence with an intensifier ("very, very", "quite", "indeed").
- Slot 3 (claim): "I know that X must equal Y" — declarative past-present claim with subscripts if needed.
- Slot 4 (concession): "However, Y, which is a [constant/role], does not affect [Z]" — comma-bracketed appositive plus negative verb.
- Slot 5 (implication): "This means that Z must apply to all [family], that is, …" — chained "that is" rephrasing.
- Slot 6 (visual directive): "Consider Figure X with [formula] to visualise this relationship:" — second-person imperative ending in colon.
- **How to fill differently:** pick a derivation that ended with a surprising equality (e.g. period vs. length of pendulum formula). Slot 1 returns to that result; slot 2 labels it; slot 3 restates the equality; slot 4 isolates one term that is *fixed* in the derivation (like g or π); slot 5 declares the equality therefore holds for all values of an independent parameter; slot 6 names a graph.
- **Original fill:** the catenoid equality with ri.
- **Demonstration fill (different idea):** "Well, but what does this mean? This is a genuinely striking result. I know that the small-angle period T of a simple pendulum must be equal to the ratio √(L/g). However, g, which is a constant and the gravitational parameter of my equation, does not affect the dependence on L. This means that the L-only expression must apply to all pendulums with different lengths, that is, it must show the period for every possible rod-length L. Consider Figure 6 with T = 2π√(L/9.81) to visualise this relationship:"

---

**SKELETON B — "From analytical block to computational solution to empirical test"**

> Finding the [intersections/solutions] between [equation A] and [equation B] is not solvable by hand, as isolating [variable] is not possible. Solving for the [variable] using technology for all [parameter values] grants me the solutions for [symbol] in the table below. To test whether the hypothesised [symbol] is the same, I have recorded [the real-world counterpart] using [instrument]. The recorded [quantity] was denoted to be [new symbol] (By [measurement protocol]. See [Appendix] for the recordings).

- Slot 1 (block): "Finding X is not solvable by hand, as isolating Y is not possible" — present-tense diagnosis with cause-clause.
- Slot 2 (computational fix): "Solving … using technology … grants me the solutions" — gerund phrase + result clause.
- Slot 3 (test setup): "To test whether the hypothesised X is the same, I have recorded Y using Z" — purpose clause + past-tense action.
- Slot 4 (operational definition): "The recorded X was denoted to be Y (By …)" — passive + parenthetical method.
- **How to fill differently:** take any system where the closed-form comparison fails (e.g. comparing a hypothesised cooling curve to thermometer readings). Slot 1 states why symbolic comparison fails; slot 2 uses a solver/calculator to tabulate; slot 3 designs a real measurement using named equipment; slot 4 defines the new symbol with a measurement sentence.
- **Original fill:** intersections of eq. 21 and the catenoid, βi from high-res camera.
- **Demonstration fill (different idea):** "Finding the intersections between Newton's cooling equation and the empirical temperature curve is not solvable by hand, as isolating t is not possible. Solving for t using a numerical solver for all initial temperatures T₀ grants me the solutions for tᵢ in the table below. To test whether the hypothesised tᵢ cooling time is the same, I have recorded the real cooling times of copper cylinders using a thermocouple and stopwatch. The recorded time was denoted to be τᵢ (By timing from immersion until the cylinder reached 30 °C. See Appendix B for the readings)."

---

**SKELETON C — "Closing with deferred evaluation + residual puzzle"**

> The evaluation of these results can be found in [section X]. Whilst I was able to [achievement], I have yet to understand why for [condition] I have [anomaly]. Since the…

- Slot 1 (deferral): "The evaluation … can be found in section X" — passive forward pointer.
- Slot 2 (achievement): "Whilst I was able to [find/do X], I have yet to understand why for [Y] I have [Z]" — concessive clause + open anomaly, ending mid-thought.
- **How to fill differently:** pick any completed piece of analysis whose full judgement belongs elsewhere; add an unresolved oddity that the next section will chase.
- **Original fill:** deferral to section 4, plus the two-solution puzzle for |α| < αi.
- **Demonstration fill:** "The evaluation of these results can be found in Section 5. Whilst I was able to derive the cooling constant for each cylinder, I have yet to understand why for any cylinder with mass m < 50 g I obtain two distinct cooling constants. Since the…"

## Express-Idea Vocabulary

**Sequencing / procedural moves**
- "Solving for the 2 using technology for all ri" → gerund-led procedure
- "To test whether the hypothesised αi breaking distance is the same" → purpose-clause opener

**Cause / consequence**
- "as isolating α or C is not possible" → causal "as" inside a limitation claim
- "This means that the derivative of the catenoid equation must apply to all catenoids" → "This means that…" consequence marker
- "grants me the solutions for αi in the table below" → result verb "grants"

**Contrast / concession**
- "However, radius, which is a constant … does not affect the derivative" → "However," interrupting the prior claim
- "Whilst I was able to find an equation to solve for all αi" → "Whilst" concessive before the anomaly
- "I have yet to understand why" → unfinished-problem phrasing

**Specification / restatement**
- "that is, it must show the solution to all possible maximum distances" → "that is," rephrase
- "Consider Figure 6 with different ri = C cosh(C/α) and equation 21" → "Consider" + named figure, narrowing scope

**Evidence handling**
- "to visualise this relationship" → purpose-of-figure phrasing
- "recorded the breaking distances of my soap film in real life" → empirical anchor
- "See Appendix A for the recordings" → external-evidence pointer
- "The recorded distance was denoted to be βi" → symbol-introduction passive

**Explanation / definition verbs**
- "I know that the catenoid equation must be equal to" → epistemic "I know that"
- "The recorded distance was denoted to be βi" → "denoted to be" for new variable
- "is not solvable by hand" → capability verb in negation

**Verdict / evaluation verbs**
- "This is a very, very interesting result" → first-person evaluative verdict
- "Whilst I was able to find an equation" → "able to" achievement verb

## How to Explain an Idea (replication steps)

This section relies on the **surprising-equality → generalisation → intractability → computational+empirical substitute → deferred judgement** pattern. To explain a *new* idea the same way, follow these steps:

1. **Open with a return-to-question pivot.** Begin with a one-sentence rhetorical re-entry ("Well, but what does this mean?") that signals you are about to interpret, not introduce.
2. **Stamp the result with a verdict.** Give a short evaluative sentence ("This is a striking result") so the reader knows the writer treats the finding as significant before unpacking why.
3. **State the equality that surprised you.** Use "I know that X must be equal to Y" — a present-tense epistemic claim — so the reader sees the exact relation being interrogated.
4. **Insert a "However" concession that isolates a fixed parameter.** Use a comma-bracketed appositive ("However, Y, which is a constant and the [role], does not affect [Z]") to disrupt the naive reading.
5. **Convert the concession into a generalisation.** Use "This means that … that is, …" to first state the implication and then re-state it in plainer terms, making the consequence explicit.
6. **Direct the reader to a figure.** Use second-person imperative ("Consider Figure X with [formula]") so the visual does the work of convincing.
7. **Admit analytical intractability.** Use "Finding X is not solvable by hand, as isolating Y is not possible" to legitimise the next move.
8. **Switch to a computational substitute.** Use a gerund clause ("Solving … using technology … grants me the solutions") that names the tool and the resulting symbol.
9. **Design an empirical comparator.** Use "To test whether … I have recorded … using [instrument]" so the hypothesised symbol has something to be checked against.
10. **Operationally define the new symbol in parentheses.** "The recorded X was denoted to be Y (By [protocol]. See Appendix …)" so the table is reproducible.
11. **Defer the verdict.** "The evaluation … can be found in section X" — signal that the present section's job is to *gather*, not to judge.
12. **Surface one residual anomaly.** End with "Whilst I was able to …, I have yet to understand why for [condition] I have [oddity]. Since the…" so the next section has a launching problem.
