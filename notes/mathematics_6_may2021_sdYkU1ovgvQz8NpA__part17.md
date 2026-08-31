# Idea Flow Notes: mathematics_6_may2021_sdYkU1ovgvQz8NpA — Euler-Lagrange does not show the nature of the extrema, it is possible that one solution is a minima, whilst the other

## Paragraph Flow (move by move)

**Paragraph 1**

1. **Verdict (carried-in fragment).** "is a maxima." — Flags one branch of a previous bifurcation as the wrong type of extremum. Hands to next sentence by demanding: *which branch is the real one?* (problem-set-up).

2. **Method proposal + reason.** "I can test out for which solution of C resembles my soap film" — Proposes a discrimination strategy. Hands forward by stating the criterion that licenses it.

3. **Justifying principle.** "as I know that soap film mimics minimal surfaces" — Supplies the real-world analogy that makes the test valid. Hands forward by giving *why* the test works (cause link).

4. **Implication of that principle.** "which will allow me to negate one of the solutions." — States the pay-off: one value gets eliminated. Hands forward by pivoting from *why* to *how* (transition "To do this").

5. **Procedure specification.** "I will consider a arbitrary distance such as α = 0.5" — Operationalises the test by picking a concrete parameter value. Hands forward by setting up the equation to be tested (specification).

6. **Equation reference.** "and analyse how different C compute the equation y(x) = C cosh Cx (Introduction to the calculus of variations, 2016, p.45-46)." — Names the formula being tested and cites source. Hands forward by promising output (lead-in "Using technology, I find…").

7. **Tool statement + result lead-in.** "Using technology, I find that the following are the possible solutions for C when α = 0.5:" — Announces that the computation has been run. Hands forward by pointing the reader to the data list.

**Paragraph 2**

8. **Numerical results.** "C ≃ 0.187988, 1.24854" — Presents the two candidate constants. Hands forward by raising: *which of these is the surface?* (problem-set-up for visual test).

**Paragraph 3**

9. **Visualisation procedure + purpose.** "I graph the function with these C values… in the domain of [−0.5, 0.5] as I have chosen from α = 0.5, to see how my soap film shape differs with both C" — Describes what is plotted, the domain, and the comparison goal. Hands forward by pointing the reader to the figure (transition into evidence).

**Paragraph 4**

10. **Evidence reading 1.** "It is now possible to see from Figure 7 that for larger C, the function arc length is smaller" — Reports first observable from the graph. Hands forward by stacking a second observation under "Moreover".

11. **Evidence reading 2 (cross-check).** "Moreover, the shape with C = 1.24854 largely corresponds with the shape in my photo" — Matches graph to physical photograph, confirming direction. Hands forward by accumulating enough evidence for a verdict (transition "Thus").

12. **Final deduction.** "Thus, I can deduce that for values of C > Cαi it is a minimal." — Closes with the general claim surviving the test. Hands forward to whatever follows (or ends section).

---

## What This Section Does (content sequence)

A **solution-discrimination** section in a modelling write-up. Ordered moves:

1. **Frame the unresolved question** — the Euler–Lagrange equation has given multiple roots; one must be the real minimum, the other a maximum (or saddle).
2. **Name a real-world discriminator** — soap films exhibit minimal surfaces, so the photo becomes the truth-test.
3. **Operationalise the test numerically** — fix a domain parameter (α = 0.5) and substitute into the candidate equation to enumerate possible constants.
4. **Run the computation and list the candidates** — present the discrete set of solutions for C.
5. **Visualise the candidates** — graph each function over the chosen domain so the shape difference is visible.
6. **Read the graph for a measurable property** (arc length, curvature, etc.) — produce evidence the model alone could not yield.
7. **Cross-check against the physical photograph** — second, qualitative line of support.
8. **Issue a verdict** that generalises beyond the tested α — "for C > Cαi it is a minimal."

The order matters because each step *sets up the next*: the bifurcation only matters once a discriminator exists; the discriminator only works once a specific number is plugged in; the number is meaningless until visualised; the visual is meaningless until matched to the photograph; both lines of evidence are needed before the writer can upgrade a single data-point test into a general claim.

---

## Paragraph Skeletons (replicable templates)

**SKELETON A — Problem-framing + test-proposal paragraph**

`[Carried-in verdict that the previous step is a wrong-type extremum]. I can test [which candidate] [resembles my real-world reference], as [a known physical analogy links the reference to the extremum type], which will allow me to negate [the wrong candidate]. To do this, I will [fix a parameter value], and [plug it into the candidate equation] ([citation]).`

- **Slot 1 (carried-in verdict, fragment):** the previous paragraph's conclusion that a given extremum is a maximum. One short phrase, no verb.
- **Slot 2 (test proposal):** "I can test out for which solution of C resembles my soap film" — first-person, future-tense intention, naming the variable and the comparator.
- **Slot 3 (real-world analogy):** "as I know that soap film mimics minimal surfaces" — single dependent clause giving the physical principle that licences the test.
- **Slot 4 (pay-off):** "which will allow me to negate one of the solutions" — relative clause stating what the test achieves.
- **Slot 5 (operational pivot):** "To do this, I will consider a arbitrary distance such as α = 0.5" — "To do this" transition + first-person future + concrete numerical value.
- **Slot 6 (equation + source):** "and analyse how different C compute the equation y(x) = C cosh Cx (Introduction to the calculus of variations, 2016, p.45-46)" — citation in parentheses at sentence end.

**Filled-in demonstration with a different idea:** "is overestimating the damping. I can test which damping coefficient matches the observed oscillation decay, as a free pendulum in air decays logarithmically with time, which will allow me to discard the unrealistic coefficient. To do this, I will fix an elapsed time of t = 4 s, and compute the candidate amplitudes given by A(t) = A₀ e^(–γ t) (Marion & Thornton, 2004, p.112)."

---

**SKELETON B — Numerical-results + setup-of-visualisation paragraph**

`Using technology, I find that the following are the possible solutions for [variable] when [parameter] = [value]: [list of values]. I graph the function with these [variable] values ([equation list]) in the domain of [[lower], [upper]] as I have chosen from [parameter] = [value], to see how my [real-world reference] differs with both [variable].`

- **Slot 1 (tool + lead-in):** "Using technology, I find that the following are the possible solutions" — present-tense report.
- **Slot 2 (data list):** numerical values separated by commas, no verb.
- **Slot 3 (graphing action):** "I graph the function with these [variable] values" — first-person present.
- **Slot 4 (equations in parentheses):** each candidate function written in LaTeX style, comma-separated.
- **Slot 5 (domain justification):** "in the domain of [a, b] as I have chosen from α = 0.5" — domain tied back to the parameter chosen earlier.
- **Slot 6 (purpose clause):** "to see how my [reference object] differs with both [variable]" — purpose infinitive.

**Filled-in demonstration with a different idea:** "Using technology, I find that the following are the possible decay rates when t = 4 s: γ ≃ 0.043, 0.317. I graph the function with these γ values (A(t) = 5 e^(–0.043 t) and A(t) = 5 e^(–0.317 t)) in the domain of [0, 10] as I have chosen from t = 4, to see how my recorded amplitude trace differs with both γ."

---

**SKELETON C — Evidence-reading + verdict paragraph**

`It is now possible to see from [Figure X] that for [larger/smaller] [variable], the [measurable property] is [comparative] than the other [variable] solution. Moreover, the [candidate] with [chosen value] [qualitatively matches] the [reference photograph/measurement] [if a transformation is applied]! Thus, I can deduce that for [values beyond threshold] it is a [qualifier for the extremum].`

- **Slot 1 (evidence marker):** "It is now possible to see from Figure 7 that" — fixed opening that attributes reading to a figure.
- **Slot 2 (quantitative observation):** "for larger C, the function arc length is smaller than the other C solution function" — comparison between the two plotted curves.
- **Slot 3 (corroboration):** "Moreover, the shape with C = 1.24854 largely corresponds with the shape in my photo if it is rotated 360° around the x axis" — second-line evidence, possibly with a geometric transformation stated.
- **Slot 4 (consequence marker):** "Thus, I can deduce that" — verdict hinge.
- **Slot 5 (general claim):** "for values of C > Cαi it is a minimal" — upgraded general statement that survives the single test.

**Filled-in demonstration with a different idea:** "It is now possible to see from Figure 3 that for larger γ, the oscillation envelope is shallower than the other γ solution. Moreover, the trace with γ = 0.317 largely corresponds with my oscilloscope capture if I align the t = 0 markers! Thus, I can deduce that for values of γ > 0.3 the model is realistic."

---

## Express-Idea Vocabulary

- **Sequencing / procedure pivots:** "To do this" (transitioning from justification to execution); "I graph the function" (next-step action verb); "Using technology, I find" (signalling computational step).
- **Cause / consequence / justification:** "as I know that soap film mimics minimal surfaces" (grounds the test); "which will allow me to negate one of the solutions" (pay-off relative clause); "Thus, I can deduce that" (verdict hinge).
- **Specification / narrowing:** "such as α = 0.5" (concrete instance of a general parameter); "in the domain of [−0.5, 0.5] as I have chosen from α = 0.5" (domain explicitly tied back to earlier parameter).
- **Evidence handling / cross-check:** "It is now possible to see from Figure 7 that" (cites a figure as the source of an observation); "Moreover, the shape with C = 1.24854 largely corresponds with the shape in my photo" (stacks a second, qualitative check).
- **Comparison / qualifying match:** "largely corresponds with the shape in my photo" (acknowledges imperfect fit without abandoning the claim); "if it is rotated 360◦ around the x axis" (states the transformation needed for the comparison).
- **Explanation verbs / framing verbs:** "mimics" (analogy verb); "will allow me to negate" (predictive action); "I can deduce" (epistemic verb upgrading a single observation to a rule); "Using technology, I find" (computational verb hiding the algorithm).
- **Purpose infinitive:** "to see how my soap film shape differs with both C" (states what the visualisation is *for*).

---

## How to Explain an Idea (replication steps)

The pattern this section runs is **principle-anchored numerical discrimination + visual corroboration → generalised verdict**. Replicate it with any new idea as follows:

1. **Carry in a verdict from the previous step.** Open with a fragment ("is a maxima") that flags the *other* branch as the wrong type of extremum, so the reader knows the fork needs resolving.
2. **Name a real-world reference object** that exhibits the property you're testing for (soap film → minimal surface; pendulum → logarithmic decay; lens → focal point). Use *first-person knowledge* ("I know that…") to anchor authority.
3. **State the test's pay-off** in a relative clause ("which will allow me to negate one of the solutions") so the reader sees why the test is being run before they see how.
4. **Pivot with "To do this"** and fix one numerical parameter by *example*, not by general declaration ("such as α = 0.5") — the concreteness lets you compute.
5. **Run the computation through a tool** and present the candidate values as a bare list; the reader does not need the working, only the menu of options.
6. **Plot each candidate over a domain explicitly tied to your earlier parameter** and state the *purpose* with "to see how…" so the figure is read with intent.
7. **Read the figure for a quantitative comparison** between the candidates (arc length, envelope depth, focal sharpness — whatever is measurable).
8. **Stack a second, qualitative cross-check** with "Moreover," — match to a photograph, video, or recorded measurement, stating any geometric transformation needed ("if rotated 360°").
9. **Close with "Thus, I can deduce that…"** and *upgrade* the single numerical test into a general threshold claim ("for values of C > Cαi it is a minimal"). The generalisation is what the section is really for; the test is just the evidence for it.
