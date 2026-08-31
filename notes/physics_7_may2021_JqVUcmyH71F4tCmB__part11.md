# Idea Flow Notes: physics_7_may2021_JqVUcmyH71F4tCmB — 0.5                                                                                                     ftmax

## Paragraph Flow (move by move)

**Paragraph 1 — the figure caption (single sentence, six moves)**

| # | Move | Quote | What it does |
|---|------|-------|--------------|
| 1 | Label/identifier | "Figure 11:" | Names the visual so the reader can locate it. Hands off by colon-introduction — whatever follows is what the label *points at*. |
| 2 | Plot type + subject | "Scatter plot of reduction factors" | Declares visualisation type and what is plotted; sets up the need for a data source. Hands off because the subject ("reduction factors") is generic until sourced. |
| 3 | Source cross-reference | "(Table 7)" | Anchors the plotted points to previously tabulated data. Hands off because, with the data grounded, the caption can now add *analytic layers* on top. |
| 4 | Analytic layer 1 — trend | "with their lines of best fit" | Adds the fitted curves; logically follows because trend lines require raw points (move 2) and refer to the same factors. Hands off by the connector "and" — another layer is being stacked. |
| 5 | Analytic layer 2 — model | "and the equations for the lines of best fit" | Adds the quantitative descriptor for those curves; follows because equations are the *mathematical form* of the just-mentioned lines. |
| 6 | Scope qualifier | "of each respective factor" | Locks the equation-to-curve pairing; follows because without it, "equations" is ambiguous (one? many?). Closes the caption with the cardinality rule that governs the six equations (18)–(23). |

**The implicit "paragraph" of equations (18)→(23)** — no prose connects them, but the ordering itself carries logic:

The six equations are stacked in an **ascending complexity / paired-variable order** (vertical/horizontal/heave factors, then crest/maximum force factors). The handoff between them is *not* argumentative but **cataloguing**: each new line broadens the catalogue so that "each respective factor" in the caption is fulfilled. The reader is handed from (18) to (19) by **parallel form** — same `f(N) = a + b·r^N − c` template, new subscript.

## What This Section Does (content sequence)

This is a **figure-with-embedded-equations** results block. The canonical move order is:

1. **Display the equations in numbered sequence** — they are the *quantitative payoff* of the analysis; placing them visible makes the figure self-contained.
2. **Anchor with figure label** ("Figure 11:") — fixes position in the document's figure series.
3. **Name the plot genre** ("Scatter plot") — tells the reader how to read the visual.
4. **Identify the data subject** ("of reduction factors") — narrows the plot to the variables in play.
5. **Cross-reference the source** ("(Table 7)") — links the figure back to a prior data block; this is the hand-off *backwards* in the report.
6. **Stack analytic layer 1** ("with their lines of best fit") — moves from raw points to fitted trend.
7. **Stack analytic layer 2** ("and the equations for the lines") — moves from visual fit to mathematical model.
8. **Close with scope rule** ("of each respective factor") — guarantees one equation per factor, matching the six displayed.

**Why this order:** the caption moves *outside-in* — from a flat label, to the data, to the analytic superstructure built on the data. Each move presupposes the one before: you cannot name trend lines (move 6) until you have named the points (move 4); you cannot name the equations (move 7) until you have named the lines (move 6). A student replicating this must keep each later move *contingent* on an earlier one.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Caption sentence**

`FIGURE [N]: [plot-genre] of [subject variables] ([source reference]) with their [first analytic layer] and the [second analytic layer] of each respective [unit/class].`

1. *Slot shape and contents:*
   - Slot 1 `FIGURE [N]:` — proper-noun label + ordinal + colon (functions as title).
   - Slot 2 `[plot-genre] of [subject variables]` — noun phrase: visualisation type + "of" + the data being plotted (plural noun group).
   - Slot 3 `([source reference])` — bracketed citation: a prior Table or Equation number.
   - Slot 4 `with their [first analytic layer]` — prepositional phrase: "with" + possessive + analytic noun (e.g. "lines of best fit").
   - Slot 5 `and the [second analytic layer]` — coordinated noun phrase, parallel to slot 4 but mathematically/computationally heavier (e.g. "equations for the lines").
   - Slot 6 `of each respective [unit/class].` — closing prepositional phrase that fixes a one-to-one mapping between layer 1/2 items and the unit class.
2. *How to fill with a different idea:* Pick a scatter-style plot you have already tabulated. Slot 2 = name the plot type ("Bar chart", "Scatter plot", "Residual plot") then the variables. Slot 3 = cite the table/equation that holds the raw numbers. Slot 4 = name a graphical overlay ("error bars", "confidence band", "running mean"). Slot 5 = name the numerical descriptor of that overlay. Slot 6 = name the categorical axis (e.g. "of each respective trial", "of each material tested").
3. *Original filled version:* "Figure 11: Scatter plot of reduction factors (Table 7) with their lines of best fit and the equations for the lines of best fit of each respective factor."
4. *Demonstration fill (different idea):* "Figure 4: Scatter plot of measured Young's moduli (Table 3) with their lines of best fit and the equations for the lines of best fit of each respective specimen."

**SKELETON B — Equation list item**

`f[subscript](N) = [constant] + [coefficient] × [base]^N − [small correction]`

1. *Slot shape and contents:*
   - Slot 1 `f[subscript](N)` — function notation; subscript names the factor, `(N)` names the independent variable.
   - Slot 2 `[constant]` — leading intercept (positive real).
   - Slot 3 `[coefficient]` — positive multiplier.
   - Slot 4 `[base]^N` — base strictly between 0 and 1 raised to independent variable (signals decay form).
   - Slot 5 `− [small correction]` — subtractive term, one or two orders of magnitude smaller than the other coefficients (signals fine-tuning/curvature).
2. *How to fill with a different idea:* Choose a quantity that depends on a non-negative integer (iteration count, time index, cycle number). Pick a base in (0,1) that captures the dominant decay. Treat the intercept, coefficient, and correction as the three least-squares parameters you would recover from `cftool`/Excel. Always display with a unit in the LHS, e.g. `(mm)`, `(s)`.
3. *Original filled version:* "fvb(N) = 0.8899 + 0.1992 × 0.9976^N − 2.261 × 10^−5 N" — vertical force factor.
4. *Demonstration fill (different idea):* "fcyc(N) = 1.024 + 0.183 × 0.9983^N − 3.71 × 10^−5 N" — fatigue-cycle retention factor for a polymer coupon.

## Express-Idea Vocabulary

Because this is a figure-caption/results block, the connective vocabulary is minimal but precisely loaded:

- **Labeling/identification:** "Figure 11:" — figure-number prefix used as section opener.
- **Specification/relationship:** "of reduction factors", "of each respective factor" — "of" chains a noun to its class; "respective" enforces one-to-one pairing.
- **Addition/stacking:** "with their lines of best fit", "and the equations for the lines of best fit" — "with" attaches the first overlay; "and" coordinates the second, heavier overlay.
- **Cross-reference (parenthetical):** "(Table 7)" — bracketed citation that points backwards to the raw data.
- **Mathematical-equality verbs (implicit):** "=" in `fvb(N) = …` — the equation sign itself does the work of "is modelled by" / "is given by".

There are **no** sequencing connectives ("firstly", "next"), no cause/consequence ("therefore", "hence"), and no contrast ("however") because the section makes no argument — it *presents*.

## How to Explain an Idea (replication steps)

The pattern here is **layered-visual-to-mathematical description** (also called *outside-in captioning*). It explains a figure by stacking analytic layers from raw visual to symbolic model.

Steps to replicate on a NEW idea (e.g. a graph of temperature vs. reaction rate with fitted curves):

1. **Gather the regression equations first.** Decide whether each curve deserves its own numbered equation. Write them in a vertical list, matching subscripts to the categorical labels on the plot.
2. **Open with the figure label.** Use the format `Figure [N]:` — the number comes from your running figure count; the colon signals that what follows describes the labelled object.
3. **Name the plot genre in three words or fewer.** "Scatter plot", "Bar chart", "Residual plot" — never "a graph showing", which is vague.
4. **State the plotted subject.** Use "of [plural noun phrase]" — e.g. "of reaction rates", "of stress values".
5. **Bracket the data source.** A parenthetical Table/Equation reference grounds the points in earlier text.
6. **Stack the first analytic layer with "with their".** This must be a *visual* overlay of the raw points (line, band, bar).
7. **Stack the second analytic layer with "and the".** This must be a *symbolic/mathematical* descriptor of that overlay (equation, formula).
8. **Close with the scope qualifier "of each respective [unit]".** This is the sentence's load-bearing clause — without it, the equation count is ambiguous.

The mechanism in one line: **label → visual subject → source → visual overlay → symbolic overlay → one-to-one pairing rule.** Each step presupposes the previous; collapse any step and the caption becomes either unfalsifiable or ambiguous.
