# Idea Flow Notes: mathematics_7_may2021_AOw6EMLTaLonaPWJ — Desmos

## Paragraph Flow (move by move)

There is effectively one paragraph: a single transitional/setup sentence followed by a data table.

**Paragraph 1** (one setup sentence + tabulated calculation)

**Sentence 1:** "The surface area can now be found by using (36) and the coordinates from Figure 10:"
- **Move:** setup / cross-reference. It does NOT compute anything itself; instead it announces that the reader will see the result and points back to two already-established sources — a numbered equation ("(36)") from earlier in the write-up and a diagram ("Figure 10") that supplies raw inputs.
- **Quoted cue:** "now be found by using (36)"
- **Hand-off to next move:** consequence — the sentence promises a calculation, so the next (and only) move must be the calculation itself, presented as rows of numbers.

**Table (15 rows of x, y, surface-area triples):**
- **Move:** evidence / worked computation. Each row is a discrete application of equation (36) to one pair of coordinates from Figure 10, written as a numeric substitution ("0.5((1.80 ∗ 0.50) − (0.15 ∗ 2.70)) = 0.25" in row 1) that the reader can verify.
- **Hand-off out of the section:** because no verdict, summary, or interpretation sentence is supplied here, the reader is left expecting a follow-up move (graphing, averaging, commenting) that must logically live in the *next* section.

## What This Section Does (content sequence)

For a **calculation-results section** of an IB exploration, the ordered moves are:

1. **Setup sentence that names the quantity to be computed.** Sets the reader up to expect numerical output. (*Why first:* without naming what is being found, the table has no label.)
2. **Cross-reference to the formula used (numbered equation) and the source of inputs (figure).** Tells the reader the table is reproducible. (*Why second:* establishes authority — the numbers come from prior work, not magic.)
3. **Tabulated computation, row by row, each row showing (input₁, input₂ → computed output).** This is the body. (*Why third:* the only move that actually answers the setup sentence.)
4. **(Implicit, not in this excerpt) Interpretation/follow-up in the next section.** The section does not close its own loop — it exists to *feed* a graph, an average, or a comparison that comes next.

Replicable order for any topic: **announce quantity → cite formula + data source → tabulate (input → result) rows → hand off to interpretation.**

## Paragraph Skeletons (replicable templates)

**SKELETON 1 — Setup sentence for a calculation table:**
"[Quantity] can now be found by using ([equation number]) and the [input type] from [Figure/Table number]:"

1. **Slot A — Quantity** (noun phrase naming what will be computed, e.g. "The surface area", "The expected value", "The standard deviation").
2. **Slot B — Equation number** (parenthetical reference to a formula already derived, e.g. "(36)", "(7)", "(ii)").
3. **Slot C — Input type** (a short plural noun describing what the figure supplies, e.g. "coordinates", "data points", "angles").
4. **Slot D — Figure/Table number** (cross-reference to a labelled diagram, e.g. "Figure 10", "Table 2").
   - **How to fill differently:** pick a calculation you have already derived, decide what single number each row will produce, locate the figure that holds the raw inputs, and write one sentence with all four slots in order. Keep the parenthetical equation reference tight against "by using" — this is what tells the reader the table is *verifiable*.
   - **Original fill:** "The surface area can now be found by using (36) and the coordinates from Figure 10:"
   - **Demo fill with a different idea:** "The expected count of arrivals can now be found by using (12) and the time-stamps from Figure 4:"

**SKELETON 2 — Tabular body (implicit, but required by the setup):**
"Row format: [input₁] , [input₂] , [computation expression = result] … repeated for n rows"

1. **Slot A — input₁ column** (the first raw reading, decimal or integer).
2. **Slot B — input₂ column** (the second raw reading).
3. **Slot C — computation cell** (substituted formula with "= result", exactly one worked line so the reader can re-do it).
   - **How to fill differently:** take every relevant data pair from your figure, plug both into the referenced equation, write out the arithmetic in the *first* row only, then leave later rows as bare outputs. This rhythm — one fully shown, the rest inferred — is what makes a calculation table feel like an IB 6/7 rather than a print-out.
   - **Original fill:** first row reads "1.80 , 0.15 , 0.5((1.80 ∗ 0.50) − (0.15 ∗ 2.70)) = 0.25".
   - **Demo fill with a different idea:** first row reads "3 , 5 , (3 · 7 − 5 · 4) = 1".

## Express-Idea Vocabulary

The section is sparse, so the toolbox is small but precise:

- **Sequencing / progress marker:** *"can now be found"* — from "The surface area **can now be found** by using (36)…". Marks "the hard derivation is over; here come the numbers."
- **Method specification (instrumental connective):** *"by using … and …"* — from "by using (36) and the coordinates from Figure 10". Tells the reader *what tools* produce the table.
- **No contrast, no cause-consequence connectives, no concession words.** This is characteristic of a pure-calculation section: connectives would be filler because the table itself does the logical work.
- **Implicit explanation verb (in the worked row):** *"= 0.25"* — the equals sign functions as the verb "equals"; it is the only "explanation" present.

## How to Explain an Idea (replication steps)

The pattern here is **authority-by-reference → repeated worked computation → ready-to-interpret artefact.** It is *not* a definition/unpack/example pattern; it is a *production* pattern. Steps to replicate:

1. **Decide the single number you will produce per row.** This is the "quantity" — write it as a noun phrase at the top of the section. Do not begin the section with anything except this noun phrase and a verb that promises calculation ("can now be found", "can now be computed", "can now be obtained").
2. **Cite the formula.** Put the numbered equation in parentheses immediately after "by using" — no prose gap, no re-derivation. The reader must trust that this equation was justified earlier and need only be pointed to it.
3. **Cite the data source.** Use a "from Figure/Table X" clause so the reader knows where the raw inputs live and can flip back to check.
4. **Stop the prose.** End the sentence with a colon. Do not interpret, do not summarise, do not comment.
5. **Lay down a table whose columns are (input₁, input₂, computed output).** In the very first row, write out the full substituted arithmetic ending in "= result". In every later row, write only the inputs and the bare result. This single fully-shown row is what proves the table is a *worked* calculation rather than a dump.
6. **Resist closing the section.** Do not write "therefore" or "this shows" at the end. Let the table hand itself to the next section, which will graph, average, or interpret it. Closing the loop here would steal the next section's job.
