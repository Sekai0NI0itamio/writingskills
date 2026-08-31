# Idea Flow Notes: mathematics_7_may2020_np7OQx7LoDDWuIhi — Note that the equation above was not simplified by expanding the linear expressions and

## Paragraph Flow (move by move)

**Paragraph 1**
1. Method-justification move: "summing them, as that would have been tedious and time consuming" — names the manual alternative and rejects it on effort grounds. Hands to the reader by announcing the chosen shortcut.
2. Tool-action move: "rather, I inputted (8) into WolframAlpha to simplify the equation to a quadratic in the form 𝑎𝑥² + 𝑏𝑥 + 𝑐" — states who did what, with which tool, to produce what structural shape. Hands to the reader by introducing the variable "where:" which obliges the reader to see the definitions.
3. Definition block: the displayed equations for 𝑎, 𝑏, 𝑐 — unpacks the named coefficients piece by piece so the form just announced becomes concrete.

**Paragraph 2**
1. Sequential-action move: "I then simply inputted the expressions above and the co-ordinates' values from the tables to calculate the quadratic coefficients using Desmos" — executes the next stage (calculator tool), and the word "simply" signals the burden has shifted away from the student onto software. Hands to the reader by reaching the end of the left-section derivation, opening the door to "Repeating this procedure…".

**Paragraph 3**
1. Generalisation move: "Repeating this procedure, I obtained the equations for the middle section, 𝑄𝑚(𝑥), and the right section, 𝑄𝑟(𝑥)" — echoes paragraph 2 and extends the same pipeline to two more datasets.
2. Source-specification move: "using the data from Tables 2 and 3 respectively" — ties each new equation to its source table, preventing ambiguity.
3. Precision + delivery move: "To six decimal places, the functions are given as follows:" — announces the rounding convention first, then obliges the reader to inspect the numbers beneath.

**Paragraph 4**
1. Visual-conversion move: "The three functions were then graphed using Desmos, as follows:" — converts the numerical table into a figure and points to it. Hands to the reader by signalling that the assembly stage is next.

**Paragraph 5**
1. Synthesis move: "Finally, we can restrict the domains of each function and reflect them in the 𝑥-axis to obtain a final piecewise relation modelling the egg:" — names the two modifications (domain restriction, axis reflection) and their joint purpose (one piecewise model of the egg). Hands to the reader by announcing "modelling the egg:", which cues the reader to expect the final formula beneath.
2. The piecewise function (9) — unpacks the synthesis promise numerically with three ±-branches keyed to x-intervals.

## What This Section Does (content sequence)

This is a *tool-assisted derivation, repetition, and assembly* section. The moves occur in this fixed order:

1. Justify the tool choice — name the manual alternative (expanding the linear expressions) and dismiss it on grounds of tedium.
2. State the structural output of the tool — declare the canonical shape produced (a quadratic in 𝑎𝑥²+𝑏𝑥+𝑐, "where:").
3. Display the parameter definitions — show 𝑎, 𝑏, 𝑐 explicitly so the shape is not left abstract.
4. Execute the next computational tool — feed definitions and table data into Desmos.
5. Generalise by repetition — "Repeating this procedure…" applies the same pipeline to the remaining datasets.
6. State precision, then deliver numbers — "To six decimal places, the functions are given as follows:" pairs a rounding claim with the coefficients.
7. Visualise — graph all three and refer to the figure.
8. Announce the assembly step — restrict domains, reflect in an axis, build a piecewise relation.
9. Display the final model — the piecewise formula closes the section.

Each move sets up the next: (1) makes (2)–(3) acceptable; (3) makes (4) executable; (4) makes (5) plausible by example; (5)–(6) make (7) sensible because three numerical objects now exist; (7) makes (8) meaningful because the visual confirms continuity breaks; (8) makes (9) deliverable.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Tool-justification + structural definition"**

> [Manual step] was not done by [hand method], as [reason against hand method]; rather, I [verb] [prior equation reference] into [Tool A] to simplify the equation to [target form name], where: [parameter 1 = …], [parameter 2 = …], [parameter 3 = …].

- Slot 1 (manual step + rejection): grammatical shape = a participle phrase ("summing them, as that would have been tedious…"). Fill it with the slow mathematical path the student almost took.
- Slot 2 (tool + target shape): grammatical shape = "rather, I [past tense verb] [reference] into [named software] to simplify… to [canonical form]". Fill it with the software actually used and the textbook-named form it produces.
- Slot 3 (parameter block): grammatical shape = stacked labelled equations. Fill it with three named coefficients each set equal to a closed-form expression.
- Original filled version: "summing them, as that would have been tedious and time consuming; rather, I inputted (8) into WolframAlpha to simplify the equation to a quadratic in the form 𝑎𝑥²+𝑏𝑥+𝑐, where: 𝑎 = … 𝑏 = … 𝑐 = …"
- Demonstration fill with a different idea: "differentiating each term by hand, as that would have been error-prone with four nested products; rather, I uploaded the Lagrangian into SymPy to extract the stationary conditions to a system in the form ∇f = 𝜆∇g, where: ∂f/∂x₁ = …, ∂f/∂x₂ = …, ∂f/∂x₃ = …"

**SKELETON B — "Repetition + precision + numerical delivery"**

> Repeating this procedure, I obtained the equations for the [variant 1] and the [variant 2], using the data from [source A] and [source B] respectively. To [precision statement], the functions are given as follows: [equation 1]; [equation 2].

- Slot 1 (generalisation opener): grammatical shape = present-participle + "I obtained". Fill it with the verb that describes repeating the pipeline.
- Slot 2 (variant naming): grammatical shape = "the [position] section, 𝑄ₓ(𝑥)". Fill with two named sub-models in symbolic notation.
- Slot 3 (source pairing): grammatical shape = "using the data from Tables [n] and [n] respectively". Fill with explicit table references to keep provenance visible.
- Slot 4 (precision + deliver): grammatical shape = prepositional phrase "To [n] decimal places" + "the functions are given as follows:". Fill with the rounding rule before showing numbers.
- Original filled version: "Repeating this procedure, I obtained the equations for the middle section, 𝑄ₘ(𝑥), and the right section, 𝑄𝑟(𝑥), using the data from Tables 2 and 3 respectively. To six decimal places, the functions are given as follows: 𝑄ₘ(𝑥)=…; 𝑄ᵣ(𝑥)=…"
- Demonstration fill with a different idea: "Repeating this procedure, I obtained the coefficients for the weekday model, 𝑀_w(𝑡), and the weekend model, 𝑀_e(𝑡), using the data from Sheets 2 and 3 respectively. To two significant figures, the models are given as follows: 𝑀_w(𝑡)=…; 𝑀_e(𝑡)=…"

**SKELETON C — "Assembly + final deliverable"**

> Finally, we can [modification 1] and [modification 2] to obtain a final [object type] [gerund-phrase purpose]: [piecewise formula with three keyed branches].

- Slot 1 (announcement of synthesis): grammatical shape = "Finally, we can [verb] and [verb] to obtain a final [noun] [purpose]". Fill with two transformation verbs and the purpose phrase.
- Slot 2 (piecewise formula): grammatical shape = a left-brace formula with three rows, each starting with a sign-bracketed expression and ending with an interval constraint.
- Original filled version: "Finally, we can restrict the domains of each function and reflect them in the 𝑥-axis to obtain a final piecewise relation modelling the egg: 𝑓(𝑥)={±(−3.884244𝑥²+…), ±(…), ±(…)}"
- Demonstration fill with a different idea: "Finally, we can clip the noise floor of each channel and normalise the gain to obtain a final composite signal replicating the speech waveform: 𝑠(𝑡)={A₁cos(2πf₁t), A₂cos(2πf₂t), A₃cos(2πf₃t)}"

## Express-Idea Vocabulary

- Sequencing: "then" ("I then simply inputted the expressions above…"); "Repeating this procedure" ("Repeating this procedure, I obtained the equations…"); "Finally" ("Finally, we can restrict the domains…").
- Cause / rejection of alternative: "as that would have been tedious and time consuming" (justifies the tool choice by naming the avoided cost).
- Specification / structural cue: "in the form" ("a quadratic in the form 𝑎𝑥²+𝑏𝑥+𝑐"); "as follows" ("the functions are given as follows:"); "where:" ("…where: 𝑎=…").
- Precision-handling: "To six decimal places" ("To six decimal places, the functions are given…").
- Tool-naming verbs (action): "inputted" ("I inputted (8) into WolframAlpha…"); "calculate" ("…to calculate the quadratic coefficients…"); "obtained" ("I obtained the equations for the middle section…"); "graphed" ("The three functions were then graphed…").
- Synthesis verbs: "restrict" ("restrict the domains of each function…"); "reflect" ("…reflect them in the 𝑥-axis…"); "obtain" ("…to obtain a final piecewise relation…").
- Definition / purpose phrase: "modelling the egg" ("…modelling the egg:").

## How to Explain an Idea (replication steps)

The pattern is: **reject-manual → name-tool-and-canonical-shape → display-parameters → run-tool → generalise-by-repetition → declare-precision-then-show-numbers → visualise → assemble-modifications → deliver-final-formula**.

1. Identify the manual path the reader expects (e.g. summing a long series by hand, differentiating a Lagrangian term-by-term, inverting a matrix on paper). Write one participle phrase naming it and one clause rejecting it on effort/accuracy grounds ("…, as that would have been tedious and error-prone").
2. Name the software and the canonical output shape ("I inputted … into [Tool] to simplify the equation to [form], where:"). The "where:" is mandatory — it obliges the next step.
3. Display the named parameters as labelled equations (𝑎 = …, 𝑏 = …, 𝑐 = …). Keep them stacked so the reader sees the form instantiated.
4. State the execution step with the next tool in one sentence beginning with "I then" — feed the parameter expressions plus the dataset into the second tool.
5. Generalise with "Repeating this procedure, I obtained …" naming each variant and pairing it with its data table ("using the data from Tables n and m respectively").
6. Pair a precision phrase with a delivery phrase ("To [n] decimal places, the functions are given as follows:") and list the numerical equations immediately beneath.
7. Convert to a visual with one short sentence ("The [n] functions were then graphed using [Tool], as follows:") and reference the figure.
8. Announce the assembly ("Finally, we can [modification 1] and [modification 2] to obtain a final [object type] [purpose]:"). The two modifications should be small, distinct, and reversible.
9. Display the final composite object — a piecewise/branched formula keyed by intervals — so the section ends with the deliverable, not commentary.
