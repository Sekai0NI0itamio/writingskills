# Idea Flow Notes: mathematics_7_may2021_AOw6EMLTaLonaPWJ — C                   D                         D

## Paragraph Flow (move by move)

**Paragraph 1 — Theorem display**
- Move: foundational claim (displayed equation). "A = 1/2 ∮_C P dx + Q dy" (equation 32). It states the canonical, unmodified form of Green's theorem — the result the entire section is built upon.
- Handoff: by presenting the *unaltered* version first, the reader is primed for an explicit change; the next paragraph announces that change.

**Paragraph 2 — Modification proposal + discrete substitutions**
- Move 1 (aim/proposal): "We can modify Green's theorem to better model" — names the action (modify), the target theorem, and the comparative purpose ("better model"). The reader is told *why* a change is coming and *what* will improve.
- Move 2 (context anchor): "the borderline of Britain" — locks the abstract theorem onto a concrete geography, justifying why modification is even needed.
- Move 3 (definition): "with the following discrete intervals:" — signals that the upcoming equations (33) and (34) define the discrete replacements.
- Moves 4–5 (sub-definitions, equation 33 and equation 34): "dx = ∆x = xi+1 − xi" and "dy = ∆y = yi+1 − yi" — operationalise "discrete intervals" by giving the algebraic recipe for the replacement.
- Handoff: by handing the reader explicit discrete substitutes of the *dx* and *dy* that appear in the original (32), the next paragraph is logically forced — the only remaining step is to put them together.

**Paragraph 3 — Algebraic derivation**
- Move 1 (procedural transition): "By substituting (33) and (34) into (32)" — names the algebraic operation and references the prior equations by number, removing any ambiguity about what is being done.
- Move 2 (result flag): "the following can be determined:" — tells the reader the displayed block is the *consequence* of the substitution, not a new claim.
- Moves 3–4 (result equations 35 and 36): "A = 1/2 Σ (xi(yi+1 − yi) − yi(xi+1 − xi))" and its expanded summation form — the discrete area formula now stands ready to be used.
- Handoff: having produced a discrete formula, the next paragraph is forced to provide the *data* that will be plugged into it — anything else would be a derivation with no application.

**Paragraph 4 — Application instantiation + resolution disclosure**
- Move 1 (purpose clause + action): "To use Green's theorem to determine the surface area of Britain, an outline containing the coordinates of Figure 3 was created." — restates the goal in operational terms ("an outline… was created") and introduces the data source.
- Move 2 (cross-reference): "of Figure 3" — anchors the abstract outline to an external figure, handing the reader off to a visual.
- Move 3 (parameter/specification): "Note that the outline between any two coordinates in Figure 10 is approximately 100 km long:" — flags a single salient fact about the data, the *resolution* of the discretisation (here it is a caveat about precision).
- Handoff: with both the formula and the data declared, the section closes; the next section presumably plugs the coordinates into equation (36).

## What This Section Does (content sequence)

A *derivation-from-continuous-to-discrete-and-instantiation* sequence. In order:

1. **State the general theorem** (the unmodified Green's theorem, eq. 32). This must come first because every subsequent move refers back to it.
2. **Announce the modification and its motivation** ("We can modify Green's theorem to better model…"). This frames *why* the reader should expect a change.
3. **Define the replacement components** (eqs. 33, 34). Until the discrete building blocks exist, no substitution is possible.
4. **Perform the substitution explicitly** ("By substituting (33) and (34) into (32)…"). This is the single algebraic act that yields the working tool.
5. **Display the derived formula** (eqs. 35, 36). The reader now holds a tool ready for use.
6. **Instantiate the tool on real data** ("an outline… was created"). Without data, the formula is inert.
7. **Disclose the resolution/scale** ("approximately 100 km long"). This qualifies the precision of the discretisation and pre-empts objections about accuracy.

The order is rigid: a reader cannot follow a derivation backwards (you cannot derive before defining), and cannot apply before deriving, and cannot disclose resolution before instantiating. A student replicating this on any continuous-to-discrete method (trapezoidal rule, Simpson's rule, arc-length summation) should keep the same seven beats.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Modification announcement:**
"We can modify [GENERAL TOOL] to better model [CONTEXT] with the following [REPLACEMENT COMPONENTS]:"

- Slots:
  1. *GENERAL TOOL* — name of theorem/rule/principle (noun phrase).
  2. *CONTEXT* — concrete object being modelled (noun phrase).
  3. *REPLACEMENT COMPONENTS* — plural noun for the discrete pieces (e.g. "discrete intervals", "piecewise segments").
- How to fill: pick a continuous method that fails on the irregular boundary of some real shape; state it in the present tense with a comparative purpose ("better model"); name the shape concretely.
- Original fill: "We can modify Green's theorem to better model the borderline of Britain with the following discrete intervals:"
- Demonstration fill (different idea): "We can modify the trapezoidal rule to better model the irregular coastline of Madagascar with the following piecewise segments:"

**SKELETON B — Algebraic substitution + derived result:**
"By substituting [(a)] and [(b)] into [(c)], the following can be determined: [DERIVED FORMULA]"

- Slots:
  1. *(a), (b), (c)* — equation numbers (integer labels).
  2. *DERIVED FORMULA* — the rewritten expression in displayed form.
- How to fill: state the substitution explicitly by referring to prior equation numbers; use the verb "substituting" and the flag phrase "the following can be determined" so the reader knows the next block is the consequence, not a fresh claim.
- Original fill: "By substituting (33) and (34) into (32), the following can be determined: A = ½ Σ (xi yi+1 − yi xi+1)"
- Demonstration fill: "By substituting (5) and (6) into (3), the following can be determined: L = Σ √((xi+1 − xi)² + (yi+1 − yi)²)"

**SKELETON C — Application instantiation + resolution note:**
"To use [METHOD] to determine [QUANTITY], a [DATA STRUCTURE] containing the coordinates of [FIGURE] was created. Note that the [ELEMENT] between any two coordinates in [FIGURE] is approximately [VALUE] [UNITS]:"

- Slots:
  1. *METHOD* / *QUANTITY* — the derived tool and the physical quantity.
  2. *DATA STRUCTURE* — what was built (outline, polyline, sample list).
  3. *FIGURE* — cross-reference to a numbered figure.
  4. *ELEMENT* / *VALUE* / *UNITS* — what one segment represents, its length, and its units.
- How to fill: pair the method with a real-world quantity you want it to compute; describe a finite data source; quantify the resolution of one piece; flag it with "Note that" so it reads as a caveat.
- Original fill: "To use Green's theorem to determine the surface area of Britain, an outline containing the coordinates of Figure 3 was created. Note that the outline between any two coordinates in Figure 10 is approximately 100 km long:"
- Demonstration fill: "To use the trapezoidal rule to determine the distance travelled by a hiker, a polyline containing the coordinates of Figure 7 was created. Note that the segment between any two coordinates in Figure 7 is approximately 200 m long:"

## Express-Idea Vocabulary

- **Procedural / sequencing verbs:** "modify" ("We can modify Green's theorem to better model…"); "substituting" ("By substituting (33) and (34) into (32)…"); "created" ("an outline… was created").
- **Result / consequence flags:** "the following can be determined" — primes the reader that the next block is the *consequence* of the named operation.
- **Purpose / infinitive markers:** "To use Green's theorem to determine" — opens a purpose clause that names both the method and the goal.
- **Specification / scale:** "approximately" ("approximately 100 km long"); "Note that" ("Note that the outline…") — both flag that what follows is a precision caveat, not a new argument.
- **Comparison / motivation:** "better model" — a compact comparative purpose that justifies the entire modification.
- **Cross-reference / evidence handling:** "of Figure 3", "in Figure 10" — referring to external figures by number to anchor data to an image.
- **Mereology / count frame:** "any two coordinates" — frames the discretisation as a sequence of pairwise segments.

## How to Explain an Idea (replication steps)

This section uses a **continuous-to-discrete derivation pattern**. To replicate on a NEW idea:

1. **Display the unmodified tool.** Write out the canonical continuous formula (theorem, rule, principle) so the reader has the baseline. (Paragraph 1.)
2. **Announce the modification with comparative purpose.** Open with "We can modify [tool] to better model [context]…" — the comparative phrase is essential, because it justifies the work to come.
3. **Define the discrete replacement components.** Give each replacement its own numbered equation; keep them simple (here, dx and dy became differences of consecutive coordinates). (Paragraph 2, eqs. 33–34.)
4. **Signal the algebraic act.** Use the phrase "By substituting [(a)] and [(b)] into [(c)]" — naming prior equations by number forces a linear, checkable derivation.
5. **Flag the result, then display it.** Always precede the derived formula with "the following can be determined:" so the reader treats the next equation as a consequence rather than a claim.
6. **Instantiate on real data.** Restate the goal with "To use [tool] to determine [quantity]…" and describe what concrete data structure you built (outline, polyline, sample list).
7. **Disclose the resolution.** End with a "Note that…" sentence quantifying the size of one piece of the discretisation; this pre-empts accuracy objections and sets the scale for interpretation.
