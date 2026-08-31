# Idea Flow Notes: mathematics_7_may2017_TzoKIgKR386jeyuR — Procedures of creating the Probabilistic SIR Model

## Paragraph Flow (move by move)

**Paragraph 1 — Opening (3 sentences + figure caption)**

1. **Sentence 1** — *Claim / tool identification*: "The spreadsheet software Microsoft Excel is used to create the PSIRM."
   - Hands the reader forward by **announcing the medium** so the figure caption that follows has a referent.
2. **Sentence 2 (figure caption)** — *Visual evidence reference*: "Figure 1 Microsoft Excel layout of creating the PSIRM."
   - Hands the reader forward by **showing the reader where to look** before announcing the list, priming them for box-letter references.
3. **Sentence 3** — *Transition / signposting*: "The procedures for creating this PSIRM is as follows."
   - Hands the reader forward by **signalling the list pattern** — every numbered step below becomes the "as follows" payoff.

**Paragraph 2 — Numbered procedure (13 step-sentences)**

1. **Step 1** — *Action / constants setup*: "Enter the constants and their corresponding values in columns M and N"
   - Hands forward by **putting fixed parameters in first** so every later formula can reference them.
2. **Step 2** — *Action / scaffold setup*: "Enter the column headers as shown in boxes A1, B1, C1…"
   - Hands forward by **labelling the grid**, which makes every later "into Box X" instruction legible.
3. **Step 3** — *Specification with assumed initial conditions*: "Assuming that the total number of students is 1200, in which 1197, 3 and 0"
   - Hands forward by **seeding the simulation** — once A2–E2 hold values, ΔS in Step 4 has inputs to operate on.
4. **Step 4** — *Calculation with rationale*: "Obtain ∆S for 𝑡 = 0 by entering Equation 8 into Box G2"
   - Hands forward by **performing the first model step**, which Step 5 parallels.
5. **Step 5** — *Parallel calculation*: "Obtain ∆𝐼 for 𝑡 = 0 by entering Equation 9"
   - Hands forward by **completing the infectious delta**, letting Step 6 close the trio.
6. **Step 6** — *Closing parallel calculation*: "Obtain ∆𝑅 for 𝑡 =0 by entering Equation 10"
   - Hands forward by **balancing the bookkeeping** (ΔS + ΔI + ΔR = 0), so Step 7 advances time cleanly.
7. **Step 7** — *Time advance*: "For 𝑡 = 1, enter '1' into Box A3."
   - Hands forward by **incrementing t**, opening a new row for Steps 8–11 to populate.
8. **Step 8** — *Auxiliary check*: "To monitor the total population, enter '=C2+D2+E2'"
   - Hands forward by **adding a diagnostic column** that validates the simulation later.
9. **Step 9** — *State update S*: "To see the value of 𝑆(𝑡) at 𝑡 = 1, enter '=C2+K2'"
   - Hands forward by **applying ΔS to S**, giving the new susceptible count.
10. **Step 10** — *State update I*: "To see the value of 𝐼(𝑡) at 𝑡 = 1, enter '=D2+L2'"
    - Hands forward by **applying ΔI to I**, parallel to Step 9.
11. **Step 11** — *State update R*: "To see the value of 𝑅(𝑡) at 𝑡 = 1, enter '=E2+M2'"
    - Hands forward by **applying ΔR to R**, closing the parallel triple and letting Step 12 extend the row.
12. **Step 12** — *Local extension*: "Highlight Boxes horizontally from Box G2 to Box I2 and drag it down to Row 3."
    - Hands forward by **copying the delta formulas one row down**, after which Step 13 mass-copies.
13. **Step 13** — *Global extension / terminal step*: "Highlight Boxes horizontally from Box A3 to Box I3 and drag it down to Row 1000."
    - Closes the paragraph as the **final verb of the procedure**, terminating the list.

## What This Section Does (content sequence)

The ordered sequence a methods/procedures section of this kind should make:

1. **Tool identification** — name the software/program so every later command has a host.
2. **Visual reference** — point to the layout figure so box references (A1, B2, etc.) are grounded.
3. **Transition + list signposting** — tell the reader "as follows" so the numbered steps read as a contract.
4. **Constants** — set immutable parameters first, because every formula will call on them.
5. **Headers / labels** — populate the spreadsheet skeleton before any values are typed.
6. **Initial-condition assumption** — explicitly state the assumed t = 0 values, because the model depends on them.
7. **First model calculation, with inline rationale** — perform ΔS and justify non-obvious Excel choices (ROUND, RAND) in the same step.
8. **Parallel calculations** — ΔI and ΔR follow the same shape, so they are stated tersely.
9. **Time advance** — increment t so a new row opens.
10. **Diagnostic + parallel state updates** — total population plus S(t), I(t), R(t), in matched triplets.
11. **Local drag-down** — copy formulas one row to populate the next t.
12. **Global drag-down** — copy formulas down many rows to run the simulation.

Why this order works: each move only makes sense once the prior move's output exists (you cannot enter ΔS before S, I, R, and the constants exist; you cannot drag down before the first row's formulas exist). The pattern is **inputs → first tick → update rule → replicate** — replicable with any spreadsheet-based stochastic simulation.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Tool + figure + list signpost"**

SKELETON: "[Tool name] is used to create the [model name]. Figure [#] [Tool name] layout of creating the [model name]. The procedures for creating this [model name] is as follows."

1. **Slots and shapes**:
   - Slot 1: software/program proper noun + "is used to create the [abbreviation]" — declarative simple sentence.
   - Slot 2: figure number + noun phrase describing the layout shown — noun-phrase caption.
   - Slot 3: "The procedures for creating this [abbreviation] is as follows" — present-tense transition that flags a numbered list.
2. **How to fill with a different idea**:
   - Slot 1: pick the actual software (R, Python, GeoGebra). Keep present simple passive ("is used to create").
   - Slot 2: name the figure the same number as in your appendix; describe what the screenshot shows in ≤ 12 words.
   - Slot 3: keep "as follows" verbatim so the numbered list that follows is signposted.
3. **Original fill**: "The spreadsheet software Microsoft Excel is used to create the PSIRM. Figure 1 Microsoft Excel layout of creating the PSIRM. The procedures for creating this PSIRM is as follows."
4. **Demonstration fill (different idea)**: "The statistical language R is used to create the Markov-chain weather model. Figure 1 R console layout of generating the transition matrix. The procedures for building this Markov-chain weather model is as follows."

**SKELETON B — "Initial-value assumption"**

SKELETON: "Assuming that the [population] is [N], in which [a], [b] and [c] are initially (𝑡 = 0) [state 1], [state 2] and [state 3] respectively, enter the respective values into Boxes [L1], [L2], [L3], [L4] and [L5]."

1. **Slots and shapes**:
   - Slot 1: "Assuming that…" participial clause stating the total population (number).
   - Slot 2: comma-separated triple of state counts at t = 0 (numerals).
   - Slot 3: list of cell references (boxes) into which those values go.
2. **How to fill with a different idea**:
   - Slot 1: name the cohort and give one concrete total (e.g. 500 cells).
   - Slot 2: split that total into the model's compartments (e.g. 480 live, 20 apoptotic, 0 necrotic).
   - Slot 3: pick the row 2 cells whose letters match your column headers, listed in order.
3. **Original fill**: "Assuming that the total number of students is 1200, in which 1197, 3 and 0 are initially (𝑡 = 0) susceptible, infected and recovered respectively, enter the respective values into Boxes A2, B2, C2, D2 and E2."
4. **Demonstration fill (different idea)**: "Assuming that the total number of cells is 500, in which 480, 20 and 0 are initially (𝑡 = 0) live, apoptotic and necrotic respectively, enter the respective values into Boxes A2, B2, C2, D2 and E2."

**SKELETON C — "Calculation with inline rationale"**

SKELETON: "Obtain [Δstate] for 𝑡 = 0 by entering Equation [#] into Box [X] in [tool] code ('=[formula]'). Note that a '[function]' function is needed for [reason]."

1. **Slots and shapes**:
   - Slot 1: imperative verb "Obtain" + Δ-state + "for 𝑡 = 0" (sets time index).
   - Slot 2: "by entering Equation [#] into Box [X] in [tool] code" + quoted formula.
   - Slot 3: "Note that…" parenthetical justification explaining a non-obvious Excel function choice.
2. **How to fill with a different idea**:
   - Slot 1: name the increment being computed and pin it to the first time tick.
   - Slot 2: cite the equation number from your own appendix and paste the literal Excel string in quotes.
   - Slot 3: explain any function the reader won't recognise (e.g. POISSON, NORM.INV) by stating what requirement it satisfies.
3. **Original fill**: "Obtain ∆S for 𝑡 = 0 by entering Equation 8 into Box G2 in Excel code ('=-BINOM.INV(ROUND(C2*D2/B2*$N$2,0), $N$3, RAND())'). Note that a 'ROUND(number, num_digits)' function is needed for the first part of Equation 8, as a positive integral number of trials is needed for the ICBPDF."
4. **Demonstration fill (different idea)**: "Obtain ∆L for 𝑡 = 0 by entering Equation 4 into Box G2 in Excel code ('=-POISSON.DIST(RAND(),$N$2,TRUE)'). Note that a 'POISSON.DIST' function is needed here, as the apoptosis trigger is a rare discrete event requiring a Poisson rate parameter."

**SKELETON D — "Drag-down iteration"**

SKELETON: "Highlight Boxes horizontally from Box [X1] to Box [X2] and drag it down to Row [#]."

1. **Slots and shapes**:
   - Slot 1: range of cells on the first filled row (left-to-right).
   - Slot 2: target row number to which the fill handle is dragged.
2. **How to fill with a different idea**:
   - Slot 1: pick the contiguous block of cells on row 2 that contain the delta formulas.
   - Slot 2: choose how long the simulation runs (e.g. 500, 1000). Keep imperative "drag it down".
3. **Original fill**: "Highlight Boxes horizontally from Box G2 to Box I2 and drag it down to Row 3." (and the global version to Row 1000)
4. **Demonstration fill (different idea)**: "Highlight Boxes horizontally from Box G2 to Box K2 and drag it down to Row 500."

## Express-Idea Vocabulary

- **Sequencing / list-marking**: "as follows" ("The procedures for creating this PSIRM is as follows"); implicit step numbers "1. … 2. …" that carry the procedure.
- **Action verbs (procedural)**: "Enter the constants" (Step 1); "Obtain ∆S" (Step 4); "Highlight Boxes … and drag it down" (Step 12).
- **Cause / consequence / requirement**: "as a positive integral number of trials is needed for the ICBPDF" (justifying ROUND); "simulating the underlying random probability of a person being infected" (justifying RAND).
- **Specification / inline note**: "Note that a 'ROUND(number, num_digits)' function is needed" (flagging a non-obvious choice inside a step).
- **Evidence handling / figure reference**: "as shown in Figure 4" (Steps 1, 2, 3); "as shown in boxes A1, B1, C1…" (Step 2).
- **Time / index pinning**: "for 𝑡 = 0" (Steps 4, 5, 6); "For 𝑡 = 1" (Step 7); "at 𝑡 = 1" (Steps 9, 10, 11).
- **Explanation verbs**: "is used to create" (Para 1); "is needed for" (Step 4 rationale); "is used here as" (Step 4 rationale, justifying Monte-Carlo).

## How to Explain an Idea (replication steps)

The pattern this section relies on is **"setup → seed → first rule with rationale → replicate"** — a procedural-explainer pattern in which the *one* non-trivial calculation is unpacked, and every parallel step after it is stated tersely.

Steps to replicate the pattern for a NEW idea:

1. **Name the tool.** Open with "[Software] is used to create the [Model]." (Declarative simple sentence, present passive.)
2. **Anchor the reader visually.** Insert a figure caption that points to the workspace they will see in every subsequent step.
3. **Signpost the list.** End the intro paragraph with "The procedures for creating this [Model] is as follows." so the reader expects a numbered list.
4. **Set constants first.** Step 1: type fixed parameters into the constants area — never inside the working area.
5. **Label headers next.** Step 2: put column names in row 1 so cell references later are meaningful.
6. **State the t = 0 assumption explicitly.** Step 3: "Assuming that the [population] is [N], in which [a], [b], [c] are initially (𝑡 = 0) [state 1], [state 2], [state 3] respectively…"
7. **Perform the first non-trivial calculation AND justify it inline.** Step 4: state the formula in Excel code inside quotes, then add a "Note that…" clause explaining any function a reader would not recognise.
8. **Repeat the parallel calculations tersely.** Steps 5–6: same shape, no new rationale.
9. **Advance time.** Step 7: increment t and open the next row.
10. **Add diagnostics and parallel state updates.** Steps 8–11: matched triplets of formulas.
11. **Local drag-down, then global drag-down.** Steps 12–13: copy the delta row one cell, then copy the full row across the desired horizon — terminating the procedure.
