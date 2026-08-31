# Idea Flow Notes: mathematics_7_may2017_TzoKIgKR386jeyuR — Procedures of creating the Deterministic SIR Model in Microsoft Excel

## Paragraph Flow (move by move)

**Paragraph 1** (tool declaration + figure caption)
- **Sentence 1 — claim/context:** "The spreadsheet software Microsoft Excel is used to create the DSIRM." States the software used to build the model. Hands the reader forward by *announcing what tool*, so a visual of that tool's layout can follow as evidence.
- **Sentence 2 — visual evidence/reference:** "Figure 1 Microsoft Excel layout of creating the DSIRM." Provides the layout to orient the reader before procedures begin. Hands the reader forward by *demonstrating the workspace*, so the procedural steps that use specific boxes/cells can now make sense.

**Paragraph 2** (single transition sentence)
- **Sentence 1 — transition/announcement:** "The procedures for creating this DSIRM is as follows." Signals a switch from orientation to procedure. Hands the reader forward by *promising a list*, so the numbered procedural block immediately follows.

**Paragraph 3** (numbered procedural list — items 1–16)
- **Item 1 — setup (constants):** "Enter the constants and their corresponding values in columns Q and R" — establishes fixed parameters. Hands forward by *placing parameter values first*, so later formulas that reference them ($R$3, $R$4…) have something to draw from.
- **Item 2 — setup (headers):** "Enter the column headers as shown in boxes A1, B1, C1…" — labels every column. Hands forward by *naming the column roles*, so subsequent steps can refer to specific cells unambiguously.
- **Item 3 — initial conditions:** "Assuming that the total number of students is 1200, in which 1197, 3 and 0 are initially (t = 0)" — seeds the first row with starting values. Hands forward by *populating t = 0*, so differential-equation cells can be computed from these values.
- **Item 4 — input equation (dS):** "Enter Equation 2 into Box G2 in Excel code" — encodes the first derivative. Hands forward by *computing dS*, so other rates can reference or build on it.
- **Item 5 — input equation (dI):** "Enter Equation 3 into Box H2 in Excel code" — encodes the second derivative, defined in terms of G2. Hands forward by *using the previous cell*, so a causal chain of derivative terms forms.
- **Item 6 — input equation (dR):** "Enter Equation 4 into Box I2 in Excel code" — encodes the third derivative, completing the rate set. Hands forward by *completing the rate triplet*, so all three deltas can now be computed in parallel.
- **Item 7 — delta calculation (∆S):** "Obtain ∆S for t = 0 through multiplying dS(t)/dt with Time step" — applies the Euler step to S. Hands forward by *using the same operation pattern* (rate × Δt), so the next two deltas can mirror it.
- **Item 8 — delta calculation (∆I):** "Obtain ∆I for t = 0 through multiplying dI(t)/dt with Time step" — parallel of item 7 for I. Hands forward by *repeating the operation* on a new variable, establishing the pattern.
- **Item 9 — delta calculation (∆R):** "Obtain ∆R for t = 0 through multiplying dR(t)/dt with Time step" — parallel of items 7–8 for R. Hands forward by *finishing the delta triplet*, so the next time step's S, I, R can be assembled.
- **Item 10 — advance time:** "For t = 1, enter '1' into Box A3." — sets the next time index. Hands forward by *opening row 3*, so output cells (B3, D3, E3) can be placed in it.
- **Item 11 — diagnostic check:** "To monitor the total population, enter '=C2+D2+E2' into Box B2." — sanity-checks conservation. Hands forward by *ensuring S+I+R stays constant*, so the next three computations are justified.
- **Item 12 — output (S at t=1):** "To see the value of S(t) at t = 1, enter '=C2+K2' into Box C3." — applies Euler update to S. Hands forward by *mirroring the formula structure*, so I and R updates follow the same logic.
- **Item 13 — output (I at t=1):** "To see the value of I(t) at t = 1, enter '=D2+L2' into Box D3." — applies Euler update to I. Hands forward by *repeating the addition pattern*, so the final variable follows.
- **Item 14 — output (R at t=1):** "To see the value of R(t) at t = 1, enter '=E2+M2' into Box E3." — applies Euler update to R. Hands forward by *completing one full step*, so the formulas can now be propagated.
- **Item 15 — propagate derivatives/deltas:** "Highlight Boxes horizontally from Box G2 to Box M2 and drag it down to Row 3." — copies rate and delta cells to row 3. Hands forward by *extending one row*, so the entire row can then be dragged.
- **Item 16 — propagate full table:** "Highlight Boxes horizontally from Box A3 to Box M3 and drag it down to Row 1000." — fills all subsequent time steps. Hands forward by *finishing the model*, ending the procedure.

## What This Section Does (content sequence)

This is a **procedures/methodology** section. The ordered content moves are:

1. **Tool declaration** — names the software, setting up the environment the reader expects.
2. **Figure of the workspace** — visually grounds the reader before any text instructions.
3. **Transition sentence ("procedures … as follows")** — signposts the shift to a numbered list.
4. **Constants entry (parameters in named columns)** — must come first because every formula references them.
5. **Header entry (column labels)** — must come next so subsequent cell references are unambiguous.
6. **Initial-condition entry (t = 0 values)** — must precede any rate calculation; derivatives need a starting state.
7. **Differential-equation entry (rates in G, H, I)** — rates are computed before deltas because deltas multiply them.
8. **Delta calculations (rates × Δt)** — come immediately after rates because of the Euler step's structure.
9. **Time advancement (set t = 1)** — opens the next row so update cells have a destination.
10. **Population-conservation diagnostic** — placed after the first update to verify the model is behaving.
11. **State updates (S, I, R at t = 1)** — assemble the next time step from prior values + deltas.
12. **Formula propagation (drag down)** — must come last because it replicates everything already built.

The **why** for this order: parameters → headers → initial state → rates → deltas → time step → state update → propagation. Each move produces a value or cell that the next move references.

## Paragraph Skeletons (replicable templates)

**Skeleton A — Tool-Opening Paragraph**
> "The [software/tool] is used to create the [model]. [Figure X: visual layout of the workspace]."

- **Slot 1** (`[software/tool]`): noun phrase naming the platform.
- **Slot 2** (`[model]`): noun phrase naming the artefact being built.
- **Slot 3**: figure caption with "layout of creating the [model]".
- **HOW to fill with a different idea**: pick the exact program used (R, GeoGebra, Python notebook…), name the artefact produced, and caption a screenshot of its interface.
- **Original fill**: "The spreadsheet software Microsoft Excel is used to create the DSIRM. Figure 1 Microsoft Excel layout of creating the DSIRM."
- **Demo fill (different idea)**: "The programming language Python is used to construct the Monte Carlo simulation. Figure 1 Jupyter notebook layout of constructing the Monte Carlo simulation."

**Skeleton B — Transition-to-List Sentence**
> "The procedures for creating this [model] is as follows."

- **Slot**: noun phrase naming the model.
- **HOW to fill**: state the artefact in the same noun phrase used in the opening; declare the section is moving to a numbered procedure.
- **Original fill**: "The procedures for creating this DSIRM is as follows."
- **Demo fill**: "The steps for constructing this predator–prey model are presented below."

**Skeleton C — Parameter / Header / Initial-Condition Setup Step**
> "[Verb] the [data type] [as shown / assuming that …] in [cell range]."

- **Slot 1** (`[Verb]`): imperative ("Enter", "Type").
- **Slot 2** (`[data type]`): noun phrase ("the constants", "the column headers", "the initial values").
- **Slot 3** (`[cell range]`): comma-separated cell list.
- **HOW to fill**: state the input category, then give explicit cell coordinates already labelled in the figure.
- **Original fill**: "Enter the constants and their corresponding values in columns Q and R as shown in Figure 2."
- **Demo fill**: "Enter the parameter values and initial conditions in cells B2 through F2 as shown in Figure 2."

**Skeleton D — Equation-Input Step (with Excel code)**
> "Enter Equation [n] into Box [cell] in Excel code ('=[formula]')."

- **Slot 1** (`[n]`): equation number.
- **Slot 2** (`[cell]`): target cell.
- **Slot 3** (`[formula]`): the literal Excel expression, enclosed in single quotes.
- **HOW to fill**: pick the equation, pick the cell that already hosts that rate/delta/output, and paste the literal formula.
- **Original fill**: "Enter Equation 2 into Box G2 in Excel code ('=-C2/B2*D2/B2*$R$3*$R$2*B2')."
- **Demo fill**: "Enter Equation 5 into Box F4 in Excel code ('=B4*$D$1*EXP(-0.05*F4)')."

**Skeleton E — Euler-Delta / Output / Propagation Step**
> "Obtain ∆[X] for t = 0 through multiplying [rate] with Time step (∆t) by entering '[formula]' into Box [cell]."
> OR
> "To [verb] the [quantity], enter '[formula]' into Box [cell]."
> OR
> "Highlight Boxes [horizontally/vertically] from Box [start] to Box [end] and drag it down to Row [n]."

- **Slot 1** (`[X]`, `[quantity]`): variable name.
- **Slot 2** (`[formula]`): exact Excel string.
- **Slot 3** (`[cell]` or row range): cell/row coordinates.
- **HOW to fill**: name the variable being computed, paste the formula you already tested, target the correct cell/row, and use either "Obtain … through multiplying …" (for delta steps), "To monitor / to see the value of" (for outputs), or "Highlight … and drag it down" (for propagation).
- **Original fill**: "Obtain ∆S for t = 0 through multiplying dS(t)/dt with Time step (∆t) by entering '=G2*$R$5' into Box K2."
- **Demo fill**: "Obtain ∆P for t = 0 through multiplying dP/dt with Time step (∆t) by entering '=G2*$F$1' into Box L2."

## Express-Idea Vocabulary

**Sequencing / list-launching**
- "The procedures for creating this DSIRM is **as follows**." — announces the numbered list.

**Specification / condition-setting**
- "**Assuming that** the total number of students is 1200" — frames the initial-state rule.
- "…susceptible, infected and recovered **respectively**" — distributes values across categories.
- "**For t = 1**, enter '1' into Box A3." — advances the time index explicitly.

**Explanation / method verbs**
- "is **used to create** the DSIRM" — defines the tool's role.
- "**Enter** Equation 2 into Box G2" — direct command verb for inputs.
- "**Obtain** ∆S … through multiplying dS(t)/dt with Time step" — names the operation being performed (numerical Euler step).
- "**monitor** the total population" — purpose verb for a diagnostic cell.
- "**see the value of** S(t) at t = 1" — purpose verb for an output cell.
- "**Highlight** Boxes … and **drag** it down" — drag-down propagation verbs.

**Purpose / function cues**
- "**To monitor** the total population" — signals a check cell.
- "**To see the value of** I(t) at t = 1" — signals a state-output cell.

**Evidence handling**
- "as shown **in Figure 2**" — grounds every step in the visual evidence already supplied.

**Comparison / parallel structure**
- The three "Obtain ∆X … through multiplying … by entering '=X2*$R$5' into Box Y2" items repeat the same syntactic frame, paralleling the three ODEs.

## How to Explain an Idea (replication steps)

This section uses a **worked-procedure / numerical-recipe** pattern: parameter declaration → header setup → initial state → rate computation → discrete update → propagation.

Step-by-step instructions to replicate the pattern for a NEW idea (e.g. a logistic-growth model in a spreadsheet):

1. **State the tool.** One sentence declaring the software used to build the artefact ("The spreadsheet … is used to construct the [model].").
2. **Insert a figure of the workspace** with a caption so every later cell reference is visually anchored.
3. **Add a one-sentence transition** ("The procedures for constructing this [model] is as follows.") that immediately precedes the numbered list.
4. **Enter constants/parameters first** (imperative: "Enter the constants … in cells [range] as shown in Figure 2"), so formulas later can use absolute references.
5. **Enter column headers next**, naming each output column in row 1.
6. **Specify initial conditions** with an "Assuming that …" sentence that fixes the value at t = 0 in the appropriate cells.
7. **Input the rate equations** one per cell using "Enter Equation [n] into Box [cell] in Excel code ('=[formula]')."
8. **Compute discrete updates** using the same parallel sentence ("Obtain ∆[X] for t = 0 through multiplying [rate] with Time step (∆t) by entering '[formula]' into Box [cell].") repeated for each variable.
9. **Advance the time index** ("For t = 1, enter '1' into Box ….").
10. **Optionally add a diagnostic** ("To monitor the total/invariant quantity, enter '[formula]' into Box ….").
11. **Compute next-step state variables** with parallel "To see the value of [X](t) at t = 1, enter '[formula]' into Box …." sentences.
12. **Propagate the model** with two "Highlight … and drag it down to Row …." sentences — first for the rate/delta row, then for the full table.

The pattern hinges on **inputs before formulas, rates before deltas, deltas before state updates, and a single drag-down at the end**; every step's output is the next step's input.
