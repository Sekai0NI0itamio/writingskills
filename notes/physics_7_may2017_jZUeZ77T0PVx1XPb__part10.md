# Idea Flow Notes: physics_7_may2017_jZUeZ77T0PVx1XPb — To see if the data obtained from the experiment fits with the theoretical model of this

## Paragraph Flow (move by move)

**Paragraph 1**
- S1 ("experiment, the data obtained will be plot against the Ratio Factor"): states the next procedural move — the graph-to-variable pairing that will be tested. Hands to S2 by setting up a *condition* the reader needs the criterion for.
- S2 ("If the data produces a linear relationship with the Ratio Factor, it means that the data obtained fits the model"): states the *criterion/verdict rule* — the conditional that defines "fit." Hands to Paragraph 2 because the criterion can't be applied until the Ratio Factor itself is numerically defined.

**Paragraph 2**
- S1 ("The Ratio Factor of the hollow cylinders have to be calculated"): states the *necessary next step* — caused by the criterion in P1. Hands to S2 by announcing a calculation that needs a concrete instance.
- S2 ("The hollow cylinder with a hole with a diameter of 9 cm is used as an example"): *specification* — picks one cylinder as the worked example. Hands to the formula by supplying the numbers (9, 10) the formula needs.

**Paragraph 3 (formula + uncertainty block)**
- Move 1 ("∆𝑃/𝑃 = 1/2 × [2 × (∆𝑅/𝑅 + ∆𝑅′/𝑅′)]"): states the *propagation rule* — extends the example from value to uncertainty. Hands forward by requiring a numerical result.
- Move 2 ("∆𝑃 = 0.005"): states the *computed uncertainty result* — completes the worked example.

**Paragraph 4**
- S1 ("Similarly, the Ratio Factors of all the other cylinders can be calculated"): *generalization* using "Similarly" — lifts the worked example to the whole data set. Hands to S2 by promising where the bulk results live.
- S2 ("The results are shown in Table 1 in Appendix 2"): *evidence hand-off* — directs reader to the tabulated data. Hands to Paragraph 5 by making the graph the natural next destination.

**Paragraph 5**
- S1 ("The average final velocity is then graphed against the Ratio Factor"): states the *plotting action* — "then" ties it to the completed table. Hands to S2 because the graph now needs to be located.
- S2 ("The relationship is shown in Figure 5"): *evidence reference* — points to the visual where the linear test from P1 will be read.

## What This Section Does (content sequence)

This is a **"test-the-model" section**. The required order is:

1. **State the test procedure and its pass criterion** — what will be plotted against what, and what shape counts as "fit." *Why first:* it tells the reader the entire section is a decision, not a description.
2. **Define/operationalise the model variable** — calculate the abstract quantity (here Ratio Factor) using a formula. *Why second:* the test in step 1 cannot run until this variable has a numerical meaning.
3. **Work one example by hand** — plug concrete numbers into the formula. *Why third:* demonstrates the calculation transparently and lets the reader see the rule.
4. **Propagate uncertainty on the worked example** — add error analysis to the same instance. *Why fourth:* matches the rigour standard of the criterion (a "fit" claim needs uncertainty).
5. **Generalise to all cases via "Similarly"** — extend the worked example to the full data set and refer to a table. *Why fifth:* collapses repetition so the prose doesn't enumerate.
6. **Execute the test (plot) and reference the figure** — do the actual graphing step promised in step 1 and point to it. *Why last:* the section ends exactly at the point where the reader can now look at the figure and judge the criterion for themselves.

A student replicating this with a different topic keeps steps 1, 2, 3, 5, 6 invariant and only swaps step 4 if their variable has a simpler error model.

## Paragraph Skeletons (replicable templates)

**Skeleton A — "Set the test and its criterion" (Paragraph 1)**
SKELETON: "…, the data obtained will be plot against the [MODEL VARIABLE]. If the data produces a [EXPECTED SHAPE] with the [MODEL VARIABLE], it means that the data obtained fits the model."

1. *Slot 1* — verb in future tense ("will be plot against"); declares the plotting pair. *Fill:* name your two variables.
2. *Slot 2* — conditional clause naming the expected pattern (linear, exponential, inverse…). *Fill:* state the shape your theory predicts.
3. *Slot 3* — verdict clause ("it means… fits the model"). *Fill:* name what a positive outcome confirms.
4. **Original:** "experiment, the data obtained will be plot against the Ratio Factor of the cylinders. If the data produces a linear relationship with the Ratio Factor, it means that the data obtained fits the model."
5. **Demo fill (pendulum vs. small-angle theory):** "the period data obtained will be plot against the square root of the pendulum length. If the data produces a linear relationship with the square root of the length, it means that the data obtained fits the small-angle period model."

**Skeleton B — "Operationalise one example" (Paragraph 2 + formula)**
SKELETON: "The [MODEL VARIABLE] of the [SAMPLE SET] have to be calculated. The [SAMPLE] with a [PROPERTY = value] is used as an example." [followed by the formula and numerical result]

1. *Slot 1* — present-tense necessity statement; introduces the operation. *Fill:* replace with your variable name and dataset.
2. *Slot 2* — singular specification of one member with one numerical property. *Fill:* pick a representative item and give one distinguishing number.
3. *Slot 3* — formula expression and result. *Fill:* insert your working equation and three-sig-fig answer.
4. **Original:** "The Ratio Factor of the hollow cylinders have to be calculated. The hollow cylinder with a hole with a diameter of 9 cm is used as an example." P = 1/√(3+(10/9)²) = 0.512 (3sf).
5. **Demo fill (spring constant via SHM):** "The spring constant of the trial springs has to be calculated. The spring stretched by 0.18 m under a 2.0 N load is used as an example." k = F/Δx = 11.1 N/m (3sf).

**Skeleton C — "Generalise and point to the table" (Paragraph 4)**
SKELETON: "Similarly, the [MODEL VARIABLE] of all the other [UNITS] can be calculated. The results are shown in Table [#] in Appendix [#]."

1. *Slot 1* — adverb "Similarly" + light verb ("can be calculated"); mirrors the worked example. *Fill:* keep the verb passive/light; only swap the variable and the unit noun.
2. *Slot 2* — "The results are shown in Table X in Appendix Y." *Fill:* name your table and appendix.
3. **Original:** "Similarly, the Ratio Factors of all the other cylinders can be calculated. The results are shown in Table 1 in Appendix 2."
4. **Demo fill (resistances in a circuit IA):** "Similarly, the resistances of all the other resistors can be calculated. The results are shown in Table 2 in Appendix 1."

**Skeleton D — "Execute the plot and reference the figure" (Paragraph 5)**
SKELETON: "The [DEPENDENT VARIABLE] is then graphed against the [MODEL VARIABLE] of each of the [UNITS]. The relationship is shown in Figure [#]."

1. *Slot 1* — "The [X] is then graphed against the [Y]" with "then" tying back to the prior step. *Fill:* state the y-axis variable first, then the x-axis variable.
2. *Slot 2* — one-sentence pointer to the figure. *Fill:* give the figure number.
3. **Original:** "The average final velocity is then graphed against the Ratio Factor of each of the cylinders. The relationship is shown in Figure 5."
4. **Demo fill (cooling experiment):** "The temperature drop is then graphed against the elapsed time of each of the trials. The relationship is shown in Figure 3."

## Express-Idea Vocabulary

**Sequencing**
- "is then graphed against" — connects the calculation step to the plotting step (Paragraph 5, S1).
- "have to be calculated" — marks the next procedural move as obligatory (Paragraph 2, S1).

**Cause / consequence**
- "it means that the data obtained fits the model" — names the consequence of meeting the conditional (Paragraph 1, S2).

**Conditional / criterion-setting**
- "If the data produces a linear relationship" — sets up the pass condition for the test (Paragraph 1, S2).

**Generalisation**
- "Similarly, the Ratio Factors of all the other cylinders can be calculated" — lifts one worked example to the whole set (Paragraph 4, S1).
- "is used as an example" — flags the single instance as illustrative rather than exhaustive (Paragraph 2, S2).

**Specification / instance-picking**
- "with a hole with a diameter of 9 cm" — narrows the dataset to one concrete member (Paragraph 2, S2).

**Evidence handling**
- "The results are shown in Table 1" — delegates bulk data to an appendix (Paragraph 4, S2).
- "The relationship is shown in Figure 5" — delegates the visual to a figure (Paragraph 5, S2).

**Explanation verbs (mathematical)**
- "will be plot against" — modelling verb pairing two quantities (Paragraph 1, S1).
- "have to be calculated" — operationalising verb (Paragraph 2, S1).

## How to Explain an Idea (replication steps)

The section uses a **"criterion-then-operationalise-then-execute" pattern**: define what counts as success *before* the maths is shown, prove you can compute the model variable with one worked example (value + uncertainty), then run the test.

Step-by-step to explain a NEW idea with the same pattern:

1. **Open with the test, not the data.** One sentence naming the two quantities you will plot against each other.
2. **State the pass criterion immediately after** in a conditional ("If the data shows [shape], it means it fits [model]"). This sentence is the section's *thesis* — everything below it serves it.
3. **Announce that the model variable must be computed** ("The [X] of the [samples] have to be calculated").
4. **Pick one specimen** with one distinguishing number ("The [unit] with [property = value] is used as an example")
5. **Show the formula and substitute** the chosen numbers; give the answer to 3 sig figs.
6. **Add the uncertainty** on the same worked example using a propagation expression; state the numerical ∆.
7. **Generalise with "Similarly"** and redirect the reader to a table in an appendix ("Similarly, the [X] of all the other [units] can be calculated. The results are shown in Table [#] in Appendix [#]")
8. **Execute the plot** with a "then" tie-back ("The [dependent variable] is then graphed against the [model variable] of each of the [units]")
9. **End with a figure pointer** ("The relationship is shown in Figure [#]"). Do not interpret the figure — that is the next section's job.
