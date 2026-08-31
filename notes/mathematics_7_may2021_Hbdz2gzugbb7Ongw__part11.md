# Idea Flow Notes: mathematics_7_may2021_Hbdz2gzugbb7Ongw — A chaotic nature means small changes in initial conditions bring about a significant difference in

## Paragraph Flow (move by move)

**Paragraph 1** (2 sentences)

- **Move 1 — Verdict + Naming (continuation of a prior sentence):** "final results, which is the 'butterfly effect'." Tags the observed outcome with its conceptual label, handing forward by demanding *how one knows* — the verdict is asserted but the proof is not yet shown, so the reader needs a verification move next.
- **Move 2 — Verification claim:** "This can be verified by doing trials with slightly different initial conditions." Promises the method (perturbation trials) that will demonstrate the verdict, handing forward by forcing the reader to ask *with what fixed settings?* — which the next paragraph supplies.

**Paragraph 2** (3 sentences + table)

- **Move 1 — Constant fixation:** "All trials are done with dt = 0.0001 and g = 9.81." Locks the two environmental/numerical constants so every trial is comparable, handing forward because the reader still needs to know the *unit* of the angle variable and the *meaning* of T.
- **Move 2 — Unit specification:** "θ is in radians." Resolves the ambiguity around angle measurement, handing forward by leaving one last symbol (T) undefined.
- **Move 3 — Symbol definition:** "T is the duration of the trial." Closes the definition loop, handing forward by clearing the conceptual ground for the table that immediately follows.
- **Move 4 — Tabulated evidence:** A 9-row table presenting one-at-a-time perturbations (5% increase in θ₁₀, 5% increase in θ₂₀, small initial ω₁₀, etc.). Each row isolates a single input change, operationalising the "slightly different initial conditions" claim from Paragraph 1.

## What This Section Does (content sequence)

This is a **sensitivity-analysis setup** block. The ordered content moves are:

1. **Name the phenomenon** (here: "butterfly effect") — sets the headline so the reader knows what is being tested.
2. **Announce the verification strategy** (perturbation trials) — tells the reader the *type* of evidence that will follow.
3. **Fix the constants** (dt, g) — establishes what is held identical across every row.
4. **Define the symbols and units** (θ in radians, T = duration) — removes ambiguity before data is shown.
5. **Present a one-variable-at-a-time table** — operationalises the strategy concretely.

The order matters because: you cannot verify an unnamed phenomenon; you cannot run trials without fixed constants; you cannot read a table without defined symbols; the table must come *last* because every cell depends on the prior definitions. A student replicating this on a different topic (e.g. predator–prey sensitivity, projectile spread, resistor drift) would: name the headline behaviour → announce a perturbation strategy → list constants → define units → tabulate single-variable changes.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Verdict + Verification" bridge paragraph**

> "[Observed outcome], which is the [named phenomenon]. This can be verified by doing trials with slightly different [input variable]."

- Slot 1: an observed outcome (noun phrase, past/present tense).
- Slot 2: the named phenomenon (a label/term, often in quotes).
- Slot 3: the verification strategy (a perturbation method).
- *How to fill differently:* Slot 1 = the visible behaviour you noticed (e.g. "the spread of the spring's period", "the divergence of the predator curve"); Slot 2 = a named concept (e.g. "nonlinear sensitivity", "drift instability"); Slot 3 = the input you plan to perturb (e.g. "spring constant", "initial population").
- *Original filled version:* "final results, which is the 'butterfly effect'. This can be verified by doing trials with slightly different initial conditions."
- *Demonstration fill (new idea):* "the long-term spread of the spring's period, which is the 'nonlinear sensitivity effect'. This can be verified by doing trials with slightly different release angles."

**SKELETON B — "Constants + Definitions" parameter paragraph**

> "All trials are done with [constant A] = [value] and [constant B] = [value]. [Variable] is in [unit]. [Variable] is the [description]."

- Slot 1: a fixed numerical/numerical-symbol constant with a value.
- Slot 2: a second fixed constant with a value.
- Slot 3: the primary variable, stated in a specific unit.
- Slot 4: a secondary variable defined as a duration/count/extent.
- *How to fill differently:* Slot 1 + 2 = the two environmental/physical constants the experiment holds fixed; Slot 3 = the principal measured quantity in its conventional unit; Slot 4 = a symbol the reader would otherwise misread.
- *Original filled version:* "All trials are done with dt = 0.0001 and g = 9.81. θ is in radians. T is the duration of the trial."
- *Demonstration fill (new idea):* "All trials are done with step size = 0.001 and damping = 0.2. Amplitude is in metres. N is the number of oscillations recorded."

**SKELETON C — "One-variable-at-a-time" perturbation table**

- A column for the variation label, followed by columns of all parameters, with one cell per row changed while every other cell repeats the standard row.
- *How to fill:* keep one row labelled "Standard" with all baseline values; each subsequent row mutates exactly one cell, and the label names that mutation explicitly (e.g. "+5% in l₁", "Small initial ω₂₀").
- *Original filled version:* the 9-row table above, with "Standard" as row 1 and eight single-cell perturbations.
- *Demonstration fill (new idea):* Standard row of spring-mass parameters (k = 1, m = 1, A₀ = 0.25π, T = 20), followed by rows labelled "5% increase in k", "5% increase in m", "Small initial A₀", etc.

## Express-Idea Vocabulary

- **Verification linking:** "This can be verified by doing trials" — bridges an asserted phenomenon to its empirical check (evidence-handling connectives).
- **Constant fixation:** "All trials are done with" — a setup verb that announces which variables are frozen across the section.
- **Unit specification:** "θ is in radians" — definitional `is in` pattern for unit clarification.
- **Variable definition:** "T is the duration of" — definitional `is the [noun] of` pattern for symbol clarification.
- **Perturbation labelling:** "5% increase in θ10", "Small initial ω10" — compact noun-phrase labels that name the *single* parameter changed in each table row (no connective needed; the table label itself is the move).

(Notice the section contains *no* sequencing, contrast, or concession words — every move is either definitional or evidentiary, which is appropriate for a parameter-setup block.)

## How to Explain an Idea (replication steps)

**Pattern: Claim-of-sensitivity → Setup-of-perturbation experiment.** The author asserts a nonlinear-sensitivity phenomenon and then constructs the smallest possible experimental frame that can demonstrate it: lock the environment, define the units, then tabulate one-at-a-time perturbations.

To replicate on a NEW idea:

1. **Name the headline phenomenon** in two clauses — first the observed behaviour, then the conceptual label (e.g. "the spread grows, which is the 'drift effect'").
2. **Announce a verification strategy** in one sentence using the pattern "This can be verified by doing trials with slightly different [variable]."
3. **Fix the constants** in a single sentence listing two environmental/numerical values with `=` (e.g. "All trials are done with X = a and Y = b").
4. **Define the units and remaining symbols** in one or two short sentences using `is in [unit]` and `is the [description] of`.
5. **Build a table** whose first row is the standard case and whose every following row mutates exactly one cell, with each row label explicitly naming that mutation.
6. **Stop** — let the table carry the rest of the argument; the reader will infer sensitivity from comparing rows.
