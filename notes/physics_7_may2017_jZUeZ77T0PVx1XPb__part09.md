# Idea Flow Notes: physics_7_may2017_jZUeZ77T0PVx1XPb — Diameter of the hole                               Final Velocities                         Average final velocity

## Paragraph Flow (move by move)

This section is a single data table rather than prose paragraphs, but it operates as three logical "moves." I treat each as a paragraph-equivalent.

**Paragraph 1 — Column header row (variable declaration move)**
- Sentence/move 1: **Header declaration** — names the independent variable and its uncertainty. Quote: *"Diameter of the hole (± 0.05 cm)"*. Function: tells the reader *what was varied* and *how precisely*.
- Hand-off: the same row continues with dependent-variable columns — *"Trial 1 (m s-1)    Trial 2 (m s-1)    Trial 3 (m s-1)"* — **specification**: once the manipulated variable is fixed, the measured output must be specified (triplicate trials, SI unit attached).
- Final column header: *"Average final velocity (m s-1)"* — **consequence/implication**: declaring the unit for the computed column that the data rows below must populate.

**Paragraph 2 — Data block (evidence block)**
- Move: **trial-by-trial evidence** — ten rows, each presenting three repeated measurements with propagated uncertainty, e.g. *"1.47 ± 0.11        1.48 ± 0.10        1.45 ± 0.12"*. Function: shows replication; the reader can see internal consistency at each diameter.
- Hand-off: the rightmost cell in the same row, e.g. *"1.47 ± 0.13"*, is the **synthesis** of the three trials just shown — averaging collapses the triplet into one summary value, which is exactly what the header promised.
- Trajectory across rows: diameters increase in **uniform steps of 1.00 cm**, which is **specification** of the sampling interval and hands the reader down to the next datum by **ordered sequence** rather than narrative.

**Paragraph 3 — Caption (labelling move)**
- Move: **table caption** — *"Table 4        Processed raw quantitative data of the experiment."* Function: **naming/context** — assigns the table a reference number and tells the reader the data has already been processed (not raw recordings), which retroactively justifies the averaged column and uncertainties inside the table above.
- Hand-off: by being labelled "processed," the caption transitions the reader to whatever follows (likely analysis/graphs in the next section) — a **cause→next-step** hand-off.

## What This Section Does (content sequence)

For a *processed-results table* section in IB Physics IA, the canonical ordered sequence is:

1. **Independent variable with uncertainty, first column.** Comes first because every other column is read *against* this axis; the reader needs the manipulated quantity before measurements make sense.
2. **Repeated raw trial columns (3 trials is the IA norm).** Comes next because replication is the *evidence* — averaging only works once multiple trials exist.
3. **Averaged dependent-variable column with propagated uncertainty.** Comes after the trials because it is a *computation* on them; presenting it last lets the reader cross-check the arithmetic.
4. **Uniform sampling interval across rows** (here, 1.00 cm increments). Built into row ordering so the table doubles as a trend-readable object.
5. **SI units in every header, with explicit uncertainties.** Comes inside the header row because the reader needs unit consistency before any number is interpreted.
6. **Caption with table number + descriptor ("Processed raw quantitative data…").** Comes last because it names and qualifies the block; it also signals to the reader that any graph that follows is built from this table.

The reason for this order: *axis → evidence → synthesis → naming*. Skip the axis and trials float; skip synthesis and the reader must calculate; skip captioning and the table loses its anchor to the rest of the report.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Header row (variable + unit + uncertainty declaration)**
> [Independent variable name] (± [precision of instrument])   | [Dependent variable, trial 1] ([unit])   | [Dependent variable, trial 2] ([unit])   | [Dependent variable, trial 3] ([unit])   | [Averaged/computed dependent variable] ([unit])

1. *Slot 1*: independent variable + instrument precision in parentheses, centred/header style. Filled with a noun phrase naming the manipulated quantity.
2. *Slot 2–4*: repeated trial columns. Filled with a constant label followed by an SI unit in parentheses.
3. *Slot 5*: computed/average column. Filled with a noun phrase summarising what the rightmost column will hold.
4. **Original fill:** *"Diameter of the hole (± 0.05 cm)               Trial 1 (m s-1)    Trial 2 (m s-1)    Trial 3 (m s-1)              Average final velocity (m s-1)"*.
5. **Demonstration fill (different idea):** *"Length of pendulum (± 0.001 m)               Trial 1 (s)    Trial 2 (s)    Trial 3 (s)              Average period (s)"*.

**SKELETON B — Data row (triplicate evidence → average)**
> [independent value with one decimal]   [trial 1 ± uncertainty]        [trial 2 ± uncertainty]        [trial 3 ± uncertainty]              [average ± uncertainty]

1. *Slot 1*: manipulated value, one decimal place matching instrument precision.
2. *Slot 2–4*: three measurements each with propagated ± to two decimal places, separated by whitespace for column alignment.
3. *Slot 5*: mean of slots 2–4 with its propagated uncertainty, same decimal precision.
4. **Original fill:** *"0.00                   1.47 ± 0.11        1.48 ± 0.10        1.45 ± 0.12              1.47 ± 0.13"*.
5. **Demonstration fill (different idea):** *"0.20                   1.74 ± 0.05        1.71 ± 0.06        1.76 ± 0.04              1.74 ± 0.06"*.

**SKELETON C — Caption (numbered table descriptor)**
> Table [N]        [adjective phrase describing the state of the data] [noun phrase naming what the table contains] of the [investigation scope].

1. *Slot 1*: "Table" + ordinal number for in-text referencing.
2. *Slot 2*: short adjective telling the reader whether data is raw or processed.
3. *Slot 3*: "data of the experiment" — fixed closing phrasing that anchors the table to the IA itself.
4. **Original fill:** *"Table 4        Processed raw quantitative data of the experiment."*
5. **Demonstration fill (different idea):** *"Table 2        Unprocessed qualitative observations of the resonance experiment."*

## Express-Idea Vocabulary

This section is tabular, so connective vocabulary is sparse, but each visible phrase carries a job:

- **Labelling / naming:** *"Processed raw quantitative data"* — verb-substitute "Processed" signals that the numbers have already been averaged and uncertainty-propagated, not transcribed raw. (Quote context: *"Processed raw quantitative data of the experiment."*)
- **Precision signalling:** *"± 0.05 cm"*, *"± 0.11"* — the ± sign is the verb-equivalent here; it asserts measurement uncertainty inline.
- **Synthesis verb (in header):** *"Average final velocity"* — the noun "Average" functions as a verb telling the reader the rightmost column is a computed aggregate.
- **Trial labelling:** *"Trial 1 (m s-1)", "Trial 2 (m s-1)", "Trial 3 (m s-1)"* — the word "Trial" + ordinal is the sequencing device; it replaces "firstly/secondly/thirdly" with positional labels.
- **Reference device:** *"Table 4"* — the numeral is the connective; it lets later sentences say "(see Table 4)" without restating the contents.

## How to Explain an Idea (replication steps)

The explanation pattern this section uses is **axis-declaration → triplicate evidence → statistical synthesis → labelling**. It is a *data-presentation pattern*, not a discursive one. To replicate it for a NEW idea:

1. **Name the manipulated variable and the precision of the instrument controlling it.** Put it in the leftmost header cell with the SI unit and uncertainty in parentheses (e.g., *"Length of wire (± 0.001 m)"*).
2. **Reserve three adjacent header columns for repeated trials of the response variable.** Append the SI unit to each header so the reader never has to infer units from row data.
3. **Reserve one further header column for the averaged/computed response variable** (mean, weighted mean, derived quantity), again with its SI unit.
4. **List the data row by row in uniform increments of the independent variable.** For each row, write the three trial values with their propagated ± uncertainties, then the average with its ± uncertainty, aligned so the reader's eye can run across.
5. **End the table with a numbered caption** whose adjective ("Processed"/"Raw"/"Corrected") tells the reader what transformation has already been applied, and whose noun phrase names the experiment — this is the sentence-equivalent that hands the reader into the next section (analysis, graph, or conclusion).

The pattern works because every column promises something the rows must deliver; the caption then confirms which promise has been fulfilled.
