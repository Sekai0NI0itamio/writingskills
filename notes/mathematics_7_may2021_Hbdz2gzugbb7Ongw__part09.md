# Idea Flow Notes: mathematics_7_may2021_Hbdz2gzugbb7Ongw — 4.1     Use of Euler’s Method

## Paragraph Flow (move by move)

**Paragraph 1**
1. **S1 — Goal/justification claim:** "To numerically solve for θ1 (t) and θ2 (t), Euler's method must be used." → states the task and the method required. Hands to S2 by announcing a method whose form will now be shown.
2. **S2 — Pointer/setup:** "This is achieved by the equations below:" → transitions from the verbal claim to the displayed equations, signalling that the mechanism follows visually.
3. **Equations 28–30 — Mechanism block:** initial condition (28), angular-velocity definition (29), Euler update step (30). Hands to Paragraph 2 by raising a dependency the reader can see is unresolved (θ˙i still needs solving).

**Paragraph 2**
1. **S1 — Contrast/correction move (uses "However"):** "However, θ˙i (t) must also be solved numerically using Euler's method:" → flags a missing piece from Paragraph 1; the "also" tells the reader this is a second numerical procedure, not a replacement. Hands to the equations by reasserting the same method for a different variable.
2. **Equations 31–33 — Second mechanism block:** initial condition (31), angular-acceleration definition (32), Euler update for θ˙i (33). Hands to Paragraph 3 by leaving one final link (θ¨i values) explicitly unnamed.

**Paragraph 3**
1. **S1 — Source/specification:** "θ¨1 and θ¨2 can be found by using equations (26) and (27)." → closes the gap left at the end of Paragraph 2, naming where the input to (33) comes from. Hands to S2 by feeding the chain forward.
2. **S2 — Chain consequence:** "They are used in equation (33) to solve for θ˙1 and θ˙2, which are then used in equation (30) to find angular displacements." → runs the full cause-chain through both procedures, satisfying the original goal stated in Paragraph 1.

## What This Section Does (content sequence)

This is a **method-presentation section** with a nested-dependency structure. The ordered moves are:
1. **State the computational goal** (what must be solved) and **name the method** that will do it. Sets up why the equations that follow exist.
2. **Display the first procedure block** (initial conditions → derivative definition → update rule). Establishes the visual template the reader will look for twice.
3. **Pivot with a contrast move ("However")** to reveal that a variable appearing in the first block is itself a solution of a parallel procedure. Justifies a second block.
4. **Display the second, parallel procedure block** in the same visual order. Reinforces the pattern and creates symmetry.
5. **Close the dependency loop** by sourcing the missing input from earlier equations, then run a single chained sentence that walks the reader through the full computation: source → first block → second block → final answer.

The order works because each move opens exactly one unresolved question that the next move answers; the final sentence resolves them all in sequence.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Goal + method claim, then visual block":**
   1. Slot 1: a one-sentence claim naming the quantities to be solved and the chosen numerical method. Grammatical shape: infinitive purpose clause + "must be used." Slot 2: a one-clause pointer ("This is achieved by …") introducing a display block. The block holds, in order: an initial-condition line, a derivative-definition line, an update-rule line.
   2. **How to fill differently:** Pick two state variables in your problem, name a numerical method you are applying, and write one sentence stating that the variables must be found using it. Then format three equations in the same order: (a) initial values, (b) the derivative defined as a function of the other variables, (c) the iterative step with `+ … × dt`.
   3. **Original fill:** "To numerically solve for θ1 (t) and θ2 (t), Euler's method must be used" followed by eqs. (28)–(30).
   4. **Demo fill:** "To numerically solve for x(t) and v(t) for the falling parachutist, Euler's method must be used." Then x(0)=x0; v'(t)=g−(c/m)v; x(t+dt)=x(t)+v(t)·dt.

**SKELETON B — "However pivot to a parallel procedure":**
   1. Slot 1: a contrast-opening sentence ("However, [a variable from the first block] must also be solved numerically using the same method"). Slot 2: a parallel display block in the same three-line order (initial condition → derivative definition → update rule).
   2. **How to fill differently:** Identify the velocity-like variable in your first block, state that it too requires numerical integration, then present three equations whose left-hand side is the rate of that variable and whose right-hand side is the new acceleration equation.
   3. **Original fill:** "However, θ˙i (t) must also be solved numerically using Euler's method" followed by eqs. (31)–(33).
   4. **Demo fill:** "However, v(t) must also be solved numerically using Euler's method." Then v(0)=v0; v'(t)=(g−(c/m)v); v(t+dt)=v(t)+v'(t)·dt.

**SKELETON C — "Close the loop with a single chained sentence":**
   1. Slot 1: a short sentence sourcing the missing input from a previously numbered equation ("[acceleration quantities] can be found by using equations (X) and (Y)."). Slot 2: a single chained sentence using "which … then …" or "then … which …" to thread the input → first procedure → second procedure → final quantity.
   2. **How to fill differently:** Name the two quantities your second block needs as inputs, point to where in earlier work they were derived, then write one sentence that walks through the substitution chain ending in the variable the section originally promised to find.
   3. **Original fill:** "θ¨1 and θ¨2 can be found by using equations (26) and (27). They are used in equation (33) to solve for θ˙1 and θ˙2, which are then used in equation (30) to find angular displacements."
   4. **Demo fill:** "The drag term c·v/m can be found using equation (4). It is used in the v-update equation (6) to solve for v(t), which is then used in the x-update equation (5) to find the position at each step."

## Express-Idea Vocabulary

- **Goal/method claim verbs:** "must be used" — "Euler's method must be used."
- **Sequencing/pointing:** "This is achieved by" — "This is achieved by the equations below."
- **Contrast/concession:** "However," — "However, θ˙i (t) must also be solved."
- **Parallel procedure markers:** "must also be solved" — mirrors the first block's "must be used."
- **Source/specification:** "can be found by using equations (26) and (27)" — names an external equation pair as the supplier.
- **Chain connectives (consequence):** "which are then used in", "which are then used" — runs the substitution chain forward.
- **Equation-as-sentence verbs:** "defined as" (implicit via "= ωi = θ˙i ="), "solved for" — turns formulas into verbs the reader can follow.
- **Numerical-handling phrase:** "solved numerically using Euler's method" — labels the operation type without re-explaining the algorithm.

## How to Explain an Idea (replication steps)

This section uses a **nested-procedure → dependency closure** pattern: each block contains its own initial condition, derivative, and update rule, and the section closes by linking the blocks through a single chain sentence. To replicate:

1. **State the target quantities** in one sentence and name the numerical method that will compute them.
2. **Display Block 1** as three lines in this order: initial condition for variable X → derivative of X defined as a function of the other variables → Euler update step for X.
3. **Open a "However" sentence** that names one variable appearing inside Block 1 (its derivative) and declares that variable itself needs a parallel numerical treatment.
4. **Display Block 2** in the identical three-line order, but now for that derivative variable, ending with its Euler update step.
5. **Close with a source sentence** that locates the inputs of Block 2 inside an earlier numbered equation pair.
6. **Finish with one chained sentence** using "which … then …" to thread: earlier equation → Block 2 → Block 1 → the quantity named in step 1, so the reader can follow the entire computation in one breath.
