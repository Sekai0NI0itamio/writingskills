# Idea Flow Notes: mathematics_7_may2020_np7OQx7LoDDWuIhi — finding polynomial equations that can model one half of the egg, and then reflecting them in

## Paragraph Flow (move by move)

The section is effectively one paragraph with an embedded display formula. Treating it sentence-by-sentence:

**Paragraph 1 (continued from above)**

- **Move 1 — Method assumption / geometric condition:** "to obtain the equations for the other half, assuming that the egg is symmetrical" — States the structural property (symmetry) that legitimises the reflection approach. Hands forward by establishing that *polynomial equations for one half* must already exist — which the next move immediately supplies a method for.
- **Move 2 — Tool introduction + governing principle:** "These polynomial functions can be found using the Lagrange interpolation formula, which states that for a unique polynomial of degree 𝑛" — Names the specific tool and embeds its core principle (uniqueness tied to degree). Hands forward by raising the implicit question *how many points does that require?* — answered in the next move.
- **Move 3 — Specification of data requirement:** "(𝑛+1) data points are required to find a 'best' fit" — Quantifies the input condition implied by the uniqueness claim. Hands forward by justifying why the formula display is necessary (the reader now has the principle and input count, but needs the operation itself).
- **Move 4 — Verbal signpost to display:** "The formula is given as follows for a polynomial 𝑃(𝑥):" — Verbal cue preparing the reader for a non-prose element. Hands forward by handing the floor to the displayed equation.
- **Move 5 — Display of the formula:** the Lagrange sum equation — The operational definition. Hands forward because the symbols introduce variables whose allowed ranges and meaning must be pinned down.
- **Move 6 — Conditions + citation:** "where 1 ≤ 𝑖 ≤ 𝑛 + 1 𝑎𝑛𝑑 𝑃(𝑥𝑖) = 𝑦𝑖 (Brilliant, 2019)" — Closes the definition with index range and interpolation property, and anchors the source. Hands forward to the next section (which presumably applies the formula) by leaving the reader with a fully specified, sourced tool.

## What This Section Does (content sequence)

This is a **method-introduction / tool-definition** sequence. The ordered moves are:

1. **State the geometric/methodological assumption** that justifies the procedure (symmetry).
2. **Name the specific tool** that will perform the procedure (Lagrange interpolation).
3. **State the principle the tool embodies** and the input it requires (uniqueness + (𝑛+1) points).
4. **Verbal signpost** announcing a display ("The formula is given as follows…").
5. **Display the formula** as the operational definition.
6. **Define the symbols' conditions** and cite the source.

**WHY this order:** The assumption (1) is the *why* — it tells the reader the approach is valid. The tool name (2) is the *what*. The principle + data count (3) is the *why this tool* — it shows the tool is appropriate, not arbitrary. The signpost (4) and display (5) deliver the *how*. The conditions + citation (6) close the definition with rigour (variable domains, source). Removing or rearranging any move breaks the chain: without (1) the method floats; without (3) the reader can't tell why this tool fits; without (6) the definition is incomplete and unsourced.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Assumption + tool-introduction clause**
`"[continuation of prior method], assuming that [structural property of the object]. [The required mathematical object] can be found using the [named formula/method], which states that for [output property], [input requirement] [items] are required to find a '[adjective]' fit."`

1. *Slot roles:* first clause is a dangling participle/continuation giving geometric context; the "assuming that…" is a present-participle condition; the second sentence has a subject ("these … functions"), a modal-passive verb ("can be found using"), the tool in apposition, and a relative clause ("which states that…").
2. *How to fill with a different idea:* slot 1 — pick the structural property that lets you derive one half/portion from another (e.g. a curve's periodicity, a shape's rotational symmetry, a process's reversibility); slot 2 — pick a tool whose output is defined by a unique polynomial/interpolation/regression (Lagrange, Newton's divided differences, cubic spline); slot 3 — state the degree-to-data-points rule with the same (𝑛+1) logic, or the equivalent input rule for your chosen tool.
3. *Original filled version:* "to obtain the equations for the other half, assuming that the egg is symmetrical… These polynomial functions can be found using the Lagrange interpolation formula, which states that for a unique polynomial of degree 𝑛, (𝑛+1) data points are required to find a 'best' fit."
4. *Demonstration fill (different idea — modelling one period of a periodic temperature dataset):* "to obtain the equations for each subsequent day, assuming that the readings are periodic. These sinusoidal functions can be found using the discrete Fourier transform, which states that for a unique spectrum of 𝑁 components, (𝑁) frequency samples are required to find a 'reconstructable' signal."

**SKELETON B — Signpost + display + conditions**
`"The formula is given as follows for a [function name]([variable]): [DISPLAY]. where [index range] and [interpolation/evaluation property] ([Source, year])."`

1. *Slot roles:* sentence 1 is a third-person present-passive signpost naming the function being defined; the display is a centred equation block; the "where" clause is a fragment specifying domain of the summation index and the defining property of the function, followed by an in-text citation.
2. *How to fill with a different idea:* pick any named formula with an index/dummy variable (Newton–Cotes quadrature, finite-difference stencil, recursive sequence closed form); display it as an equation block; then give the index range and the condition linking input to output; cite one source.
3. *Original filled version:* "The formula is given as follows for a polynomial 𝑃(𝑥): [Lagrange sum]. where 1 ≤ 𝑖 ≤ 𝑛 + 1 𝑎𝑛𝑑 𝑃(𝑥𝑖) = 𝑦𝑖 (Brilliant, 2019)."
4. *Demonstration fill (Simpson's rule for numerical integration):* "The formula is given as follows for an integral 𝐼(𝑥): [displayed Simpson's 1/3-rule sum]. where 0 ≤ 𝑖 ≤ 𝑛 and 𝐼(𝑥𝑖) = 𝑓(𝑥𝑖) (Press et al., 2007)."

## Express-Idea Vocabulary

- **Sequencing / handing to next move:** "The formula is given as follows" — verbal cue that a display is coming.
- **Specification / defining clauses:** "which states that for a unique polynomial of degree 𝑛" — relative clause that pins down the governing property of the tool.
- **Explanation verbs:** "can be found using" (tool introduction), "states that" (principle attribution), "is given as follows for" (display signpost).
- **Evidence handling:** "(Brilliant, 2019)" — parenthetical author-date citation anchoring the formula to a source.
- **Conditional / domain-setting:** "where 1 ≤ 𝑖 ≤ 𝑛 + 1 𝑎𝑛𝑑 𝑃(𝑥𝑖) = 𝑦𝑖" — "where" + range + defining property closing the definition.

(No explicit cause/consequence or contrast/concession connectives appear in this short section — its logic is definitional rather than argumentative.)

## How to Explain an Idea (replication steps)

This section relies on the pattern **Assumption → Named tool + governing principle → Signposted display → Conditions + citation**.

To replicate the pattern on a new idea, take these steps in order:

1. **Open with the structural assumption** that lets the reader see *why* a derivation is even possible — state it in a participle clause attached to a preceding method (e.g. "assuming the object is symmetrical / periodic / monotonic").
2. **Name the tool** that will produce the required mathematical object. Place it in apposition immediately after the verb "can be found using" so the tool is grammatically inseparable from its purpose.
3. **Embed the tool's governing principle** in a "which states that…" relative clause, including the precise input requirement (number of points, order, components) so the reader can judge fit.
4. **Signpost the formula** with a short third-person present-passive sentence ending in a colon — e.g. "The formula is given as follows for [function]([variable]):" — so the reader is prepared for a display, not prose.
5. **Display the formula** as a centred equation block; do not embed it inline, because its complexity needs vertical space.
6. **Close with a "where" fragment** that gives (a) the index range and (b) the defining property linking input values to output values, then append a parenthetical citation. This is what converts the display from a picture into a working definition.
