# Idea Flow Notes: chemistry_7_may2020_OOzgzXzKMnCvdlfZ — Uncertainty in time Uncertainty in                  Total y-axis        Total x-axis

## Paragraph Flow (move by move)

**Paragraph 1 (Table of uncertainty values):**
- Sentence 1 (column headers + 5 rows): **Data presentation** — "Uncertainty in uncertainty (%, 1 significant figure) Total y-axis Total x-axis" — hands to §2 by *feeding forward* the raw numbers the prose then interprets.
- Logical hand: the table is a self-contained evidence block; the next paragraph names it ("these uncertainties") as if the reader just absorbed it.

**Paragraph 2 (Error propagation and methodological pivot):**
- Sentence 1: **Consequence/result** — "resulted in the error bars shown on Figure 3" — takes the table's numbers and converts them into a visual artefact, handing to S2 by *raising a procedural problem* ("the error bars exist, but…").
- Sentence 2: **Cause→justification** — "Due to the low level of uncertainty, it was infeasible to draw alternate lines" — explains *why* a new method is needed; hands to S3 by *forcing a method choice*.
- Sentence 3: **Method declaration** — "I thus used Excel's LINEST function" — the "thus" closes the logical gap left by S2 and hands forward by *promising a numerical output*.

**Paragraph 3 (Numerical verdict):**
- Sentence 1: **Evidence with conversion** — "uncertainty of ±1740 out of a gradient of -7043, which amounted to … 24%" — three layered figures (raw, relative, converted to kJ/mol) hand forward by *making the reader feel the scale* before the verdict.
- Sentence 2: **Verdict/evaluation** — "Such a degree of uncertainty definitively compromises the reliability" — the demonstrative "Such a" links back to the numbers just quoted; closes the section.

## What This Section Does (content sequence)

This is an **uncertainty/error-analysis section**. The standard move-sequence is:

1. **Tabulate propagated uncertainties** — sets up all downstream claims with defensible numbers.
2. **State what those numbers produced visually** — translates data into a graph artefact (error bars), orienting them spatially.
3. **Justify the shift from manual to digital analysis** — "Due to [scale of uncertainty], [manual method] was infeasible, so I used [digital method]" — defends why a sophisticated tool is required.
4. **Report the digital tool's raw output** — quote the slope, the uncertainty, the percentage, and the unit-converted value, all stacked so the magnitude is unambiguous.
5. **Deliver a verdict on the original result** — use the percentage to judge whether the earlier claim (here, 59 kJ/mol) still stands.

The order matters because: the table earns the right to make claims; the figure shows the reader where the claims live; the method-justification prevents a "why not by hand?" examiner question; the stacked numbers make the verdict feel earned rather than asserted.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Methodological pivot:**
> "Taking [these propagated values] into account resulted in [the visual artefact] shown on [Figure X]. Due to the [magnitude description] of uncertainty, it was infeasible to [manual alternative] by [method]. I thus used [digital tool] to calculate the [parameter]."

1. *Slot 1* (propagated values): reference noun phrase, plural, that points back to a table.
2. *Slot 2* (visual artefact): a noun like "error bars" + cross-reference to a figure number and page.
3. *Slot 3* (magnitude description): adjective phrase like "low level" — sets up the justification.
4. *Slot 4* (manual alternative): the textbook/mark-scheme method that becomes impractical.
5. *Slot 5* (digital tool + parameter): names the software and what it computed.
6. *Original fill:* "Taking these uncertainties into account resulted in the error bars shown on Figure 3… Due to the low level of uncertainty, it was infeasible to draw alternate lines of best fit by hand. I thus used Excel's LINEST function to calculate the uncertainty of the graph's slope."
7. *Demonstration fill (kinetics of a different reaction):* "Taking these rate-constant uncertainties into account resulted in the shaded confidence band shown on Figure 2. Due to the narrow spread of the data points, it was infeasible to draw alternate tangents by ruler. I thus used Logger Pro's linear-fit tool to calculate the standard error of the initial gradient."

**SKELETON B — Stacked numerical evidence:**
> "This produced [absolute uncertainty] out of [reference value], which amounted to [percentage], or [unit-converted equivalent]."

1. *Slot 1*: raw ± number with units matching the graph.
2. *Slot 2*: the gradient/mean it is compared against.
3. *Slot 3*: percentage conversion (single integer).
4. *Slot 4*: the same uncertainty expressed in the *chemistry-meaningful* unit.
5. *Original fill:* "This produced an uncertainty of ±1740 out of a gradient of -7043, which amounted to a rate of random error of 24%, or ±15kJ/mol."
6. *Demonstration fill (enthalpy experiment):* "This produced an uncertainty of ±0.8°C out of a temperature rise of 6.4°C, which amounted to a rate of random error of 12.5%, or ±2.1 kJ/mol."

**SKELETON C — Verdict sentence:**
> "Such a degree of uncertainty definitively compromises the reliability of the [earlier value] stated earlier."

1. *Slot*: demonstrative ("Such a") + magnitude noun + verb of judgement ("compromises") + the earlier claim being undermined.
2. *Original fill:* "Such a degree of uncertainty definitively compromises the reliability of the 59kJ/mol value of activation energy stated earlier."
3. *Demonstration fill:* "Such a degree of uncertainty definitively compromises the reliability of the -187 kJ/mol enthalpy change stated earlier."

## Express-Idea Vocabulary

- **Sequencing:** "Taking these uncertainties into account" (anchors to prior table); "I thus" (closes the methodological gap).
- **Cause/consequence:** "resulted in" (links data to figure); "Due to the low level" (drives the method choice); "amounted to" (converts raw figure into percentage).
- **Contrast/concession:** implicit — "Due to the low level" frames the manual method as *inadequate*, not wrong.
- **Specification:** "out of a gradient of -7043" (denominator precision); "to ±15kJ/mol" (unit-domain re-expression).
- **Evidence handling:** "This produced an uncertainty of" (introduces tool output); "shown on Figure 3" (cross-reference to visual).
- **Explanation verbs:** "resulted in" (data→artefact); "amounted to" (number→interpreted error rate); "compromises the reliability" (verdict verb).

## How to Explain an Idea (replication steps)

The pattern is **evidence-tabulation → propagation-statement → method-justification → stacked-result → reliability-verdict**.

1. **Tabulate** every source of uncertainty (temperature, volume, moles) with a % column and a total column.
2. **State the visual consequence** of those percentages in one sentence, naming the figure and page.
3. **Justify the tool** with a "Due to …, [manual method] was infeasible" clause — never skip this; it pre-empts examiner pushback.
4. **Name the tool** ("I thus used [software]'s [function]") in a single short sentence.
5. **Stack the result** in three layers: raw ± figure → percentage → chemistry-unit equivalent (e.g. kJ/mol), so the reader feels scale from every angle.
6. **Deliver the verdict** with "Such a degree of uncertainty definitively compromises the reliability of [original claim]" — use "definitively" to lock the conclusion.
