# Idea Flow Notes: chemistry_6_may2021_wX9nywnRyBVpyNWB — Name                          Equation                                               Terms of the Equation

## Paragraph Flow (move by move)

The section is a table, so each ROW is treated as one paragraph-unit and each CELL ENTRY as a sentence-move. The handoff between cells is positional (schema slot) more than connective.

**Row 0 — Header / schema**
- M1. **Schema declaration** — "Name | Equation | Terms of the Equation" — sets a 3-slot template that every row will then populate. Hands off by *invitation*: the reader now expects a row that fills those three slots.

**Row 1 — Equation 1 (Gibbs free energy definition)**
- M1. **Label** — "Equation 1 - Change in Gibbs free energy*" — names the row, stamping the first schema slot. Hands off by *equation-form specification*: the reader expects the formal statement next.
- M2. **Formal statement** — "ΔG° = ΔH° − TΔS°" — fills the second schema slot. Hands off by *left-to-right unpack*: each symbol in turn invites a corresponding entry in the Terms column.
- M3. **Unpack LHS symbol** — "ΔG° = change in Gibbs free energy at standard conditions" — opens the third schema slot, defining the left-most symbol first. Hands off by *continuation*: the next entry will define the next symbol encountered when reading the equation.
- M4. **Unpack first RHS symbol** — "ΔH° = change in Enthalpy at standard conditions*" — same pattern, next symbol. Hands off the same way.
- M5. **Unpack second RHS symbol** — "ΔS° = change in Entropy at standard conditions*" — same pattern.
- M6. **Unpack third RHS symbol** — "T = Temperature in Kelvin" — closes the equation's terms. Hands off by *new instance*: the reader now expects a fresh row to repeat the 3-slot schema.

**Row 2 — Equation 2 (Nernst equation)**
- M1. **Label** — "Equation 2 - Nernst Equation*" — repeats the schema opener. Hands off by *formal statement*.
- M2. **Formal statement** — "E = E° − (RT/nF) ln Q" — same move as Row 1 M2.
- M3. **Unpack LHS** — "E = Cell potential" — defines the leading symbol.
- M4. **Unpack second symbol** — "E° = Cell potential at standard conditions*" — mirrors Row 1's "at standard conditions" phrasing, signalling *parallel treatment of the standard-state symbol*.
- M5. **Unpack symbol with embedded authority** — "n = Moles of electrons involved in 1 mole of reaction (Brown and Ford)" — same slot, but inserts a parenthetical source citation, the only inline authority in the table.
- M6. **Unpack constant with numeric value** — "F = Faraday's constant = 9.65 × 10⁴ (Cmol⁻¹)**" — same slot, now gives numerical value + unit + double-asterisk marker. Hands off by *parallel form*: the next entry will follow the same "constant = name = value (unit)**" pattern.
- M7. **Unpack constant, parallel form** — "R = Gas constant = 8.31 (JK⁻¹mol⁻¹)**" — exact mirror of M6, proving the pattern is intentional.
- M8. **Unpack derived expression** — "ln Q = the natural log of Qc" — extends the slot to a log term, defining what the symbol's letters stand for.

**Row 3 — Equation 3 (ΔG° = −nFE°)**
- M1. **Label** — "Equation 3 – Standard Gibbs free energy and standard cell potential*" — repeats schema opener, also spans two topics, prefiguring that variables already defined will be reused. Hands off by *formal statement*.
- M2. **Formal statement** — "ΔG° = −nFE°" — fills the equation slot; the third (Terms) slot is intentionally EMPTY because n, F, E° were unpacked in Row 2. Hands off by *reused-instance cue*: reader sees the same symbols and recognises them.

**Row 4 — Equation 4 (ΔG° = −RT ln K)**
- M1. **Label** — "Equation 4 - Standard Gibbs free energy and equilibrium constant*" — schema opener again.
- M2. **Formal statement** — "ΔG° = −RT ln K" — equation slot; R and T already unpacked.
- M3. **Unpack new term only** — "ln K = the natural log of Kc" — fills the Terms slot with just the single new symbol, since the rest are reused. Hands off by *table-end cue*: the pattern of "name → equation → just-the-new-term" signals this is the final row.

**Row 5 — Caption / footnote**
- M1. **Numbering** — "Table 3 -" — anchors the table within the document. Hands off by *purpose statement*.
- M2. **Purpose / function** — "equations to be combined in table 3" — tells the reader what these four rows will do downstream. Hands off by *attribution*.
- M3. **Source attribution** — "Taken from the Chemistry Data Booklet (2014) (International Baccalaureate Organization)" — closes the section, retroactively licensing every starred entry.

## What This Section Does (content sequence)

This is a **reference-table section**. The ordered moves are:

1. **Establish a 3-slot schema** (Name | Equation | Terms of the Equation). *Why first:* every subsequent row is an instance of this template; without the schema the reader has no scaffolding to receive the data.
2. **Lay down rows in a logical dependency chain**: foundational thermodynamic identity (ΔG° = ΔH° − TΔS°) → instrumental equation that uses measured quantities (Nernst) → bridge equations that link ΔG° to the measurable quantities (Eqs 3 and 4). *Why this order:* Equation 1 introduces ΔG° conceptually; Equation 2 introduces the measurable E, n, F, R, Q that the bridge equations then plug in.
3. **Within each row, unpack symbols LEFT-TO-RIGHT as they appear in the equation.** *Why:* the reader meets the equation's symbols in a fixed visual order; the terms must mirror it or the section becomes unusable as a reference.
4. **Differentiate "reused" vs "new" symbols in the Terms column.** *Why:* variables like n, F, R, E°, T appear in multiple rows; the section treats them like a glossary, defining each once and leaving the cell empty or partial in later rows.
5. **Attach numeric values + units to physical constants** (F, R). *Why:* these are the only quantities the student cannot derive; everything else is a relationship.
6. **Embed one inline authority citation** for an ambiguous variable (n → Brown and Ford) rather than a footnote. *Why:* it keeps the definition cell self-contained.
7. **Close with a caption that (a) numbers the table, (b) states its downstream purpose, (c) cites the source booklet.** *Why last:* all definitions must exist before the reader can be told where the data comes from and where it will be used.

Another student replicating this on a different topic should follow: schema → dependency-ordered rows → left-to-right term unpacking → reuse of already-defined symbols → constants with values → single-source citation → numbered caption with purpose + authority.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Section-level skeleton (the whole table)**
- Slot 1: **3-cell column header** — "Name | Equation | Terms of the Equation"
- Slot 2: **Row 1** — "Equation 1 - [topic A]* | [equation A] | [definition of A's symbols, left-to-right]"
- Slot 3: **Row 2** — "Equation 2 - [topic B]* | [equation B] | [definitions of B's NEW symbols, left-to-right, leaving reused ones undefined]"
- Slot 4: **Row N** — same 3-slot row pattern; Terms cell shrinks as variables get re-defined
- Slot 5: **Caption** — "Table [#] - [purpose sentence]. *Taken from [source] ([year]) ([authority])"

  *Slot shapes & fills:*
  - Slot 1: a 3-cell header line naming the categories. Fill by choosing 3 generic category names that every row below will populate.
  - Slots 2–4: each is "label + formal statement + ordered unpacking of any new symbols only". Fill by ordering equations so each later one reuses at least one variable from an earlier one.
  - Slot 5: a one-line caption with three clauses: a number, a purpose, an authority.
  - *Original:* "Name | Equation | Terms of the Equation" → 4 equation rows → "Table 3 - equations to be combined in table 3. *Taken from the Chemistry Data Booklet (2014) (International Baccalaureate Organization)"
  - *Demonstration fill (kinetics):* "Name | Equation | Terms of the Equation" → "Equation 1 - Arrhenius* | k = Ae^(−Ea/RT) | A = pre-exponential factor; Ea = activation energy (J·mol⁻¹); R = Gas constant = 8.31 (JK⁻¹mol⁻¹)**" → "Equation 2 - First-order integrated rate law* | ln[A] = ln[A]₀ − kt | k = rate constant; t = time (s)" → "Table 5 - rate laws to be plotted on the same axes. *Taken from the Chemistry Data Booklet (2014) (International Baccalaureate Organization)"

**SKELETON B — Single equation row (the workhorse unit)**
- Slot 1: **Row label** — "Equation [#] - [name]*"
- Slot 2: **Formal statement** — "[equation]"
- Slot 3: **Term entries, left-to-right** — "[symbol₁] = [definition with units/conditions]; [symbol₂] = [definition]; ..."

  *Slot shapes & fills:*
  - Slot 1: noun phrase naming the equation + asterisk marker for source attribution. Fill by picking the equation's conventional name.
  - Slot 2: the equation exactly as it would be written mathematically. Fill by writing the canonical form.
  - Slot 3: ordered list, one per symbol, each phrased as "[symbol] = [what it stands for, including units or 'at standard conditions' where relevant]".
  - *Original (Row 2):* "Equation 2 - Nernst Equation* | E = E° − (RT/nF) ln Q | E = Cell potential; E° = Cell potential at standard conditions*; n = Moles of electrons involved in 1 mole of reaction (Brown and Ford); F = Faraday's constant = 9.65 × 10⁴ (Cmol⁻¹)**; R = Gas constant = 8.31 (JK⁻¹mol⁻¹)**; ln Q = the natural log of Qc"
  - *Demonstration fill (ideal gas):* "Equation 1 - Combined gas law* | P₁V₁/T₁ = P₂V₂/T₂ | P = Pressure (Pa); V = Volume (m³); T = Temperature (K)" — only one new concept (combined law), so the Terms slot is short; same skeleton works for lengthier rows.

**SKELETON C — Single term-entry micro-skeleton**
- "[Symbol] = [quantity described in words][, 'at standard conditions' if applicable][units in parentheses]*"

  *Slot shape:* a definition clause, optionally with a condition tag and a units tag, optionally flagged with an asterisk.
  *Fill:* for each variable, write the quantity name in plain words, add "at standard conditions" if it has a ° symbol, append "(unit)" only if it's a physical constant or measured quantity.
  *Original:* "ΔH° = change in Enthalpy at standard conditions*"; "R = Gas constant = 8.31 (JK⁻¹mol⁻¹)**"
  *Demonstration fill:* "Ea = minimum energy required to react (J·mol⁻¹)*"; "k = rate constant (s⁻¹ for first-order)*"

## Express-Idea Vocabulary

Because the section is tabular, the connective vocabulary is sparse and structural rather than rhetorical.

- **Sequencing** — implicit through row order and left-to-right symbol order. The only verbal cue is the numeric label itself: "Equation 1 -", "Equation 2 -", "Equation 3 –", "Equation 4 -".
- **Specification / condition tag** — "at standard conditions" (added to ΔG°, ΔH°, ΔS°, E°), "at standard conditions*" (E° definition), "involved in 1 mole of reaction" (n definition). Pattern: append the qualifying phrase at the END of the definition.
- **Definition / unpacking verbs** — equals sign used as the defining verb ("ΔG = change in Gibbs free energy"). No "is defined as" or "refers to"; the = sign carries the load.
- **Authority / evidence handling** — "(Brown and Ford)" (parenthetical, in-line with the n definition); "Taken from the Chemistry Data Booklet (2014) (International Baccalaureate Organization)" (captured at the foot). Asterisk markers (* and **) link cells back to the foot attribution.
- **Function / purpose** — "to be combined in table 3" — one purpose clause in the caption, telling the reader the table's downstream use.
- **Explanation of log terms** — "the natural log of" — used to expand both "ln Q" and "ln K", turning an operator-on-symbol into a verbal phrase.

## How to Explain an Idea (replication steps)

This section relies on a **"reference-card" pattern**: schema setup → formal label → formal statement → ordered left-to-right unpacking → selective numeric values → source attribution → purpose statement.

To explain a NEW set of ideas in the same pattern:

1. **Decide the schema (3 columns):** Name | Equation | Terms (or equivalent). Every row below will fill exactly these slots, so the schema must precede any content.
2. **Order the equations by dependency.** Place the equation that defines foundational concepts first; place equations that consume those concepts later. (Here: ΔG° concept first, measurable E/n/F/R/Q second, bridge equations last.)
3. **For each equation, write the label first** ("Equation [n] - [name]*"). The label is short, noun-phrase, and signals the row's topic.
4. **State the equation exactly in mathematical form** in the centre slot. This is the row's anchor; the Terms cell must mirror it.
5. **Unpack every NEW symbol in the equation, left-to-right.** Read the equation aloud in your head and define each symbol as your eye lands on it. Stop at the equals sign and define the LHS symbol first; continue rightward through the RHS.
6. **Skip already-defined symbols.** If a symbol was unpacked in an earlier row, leave its slot empty or write only the new terms. This signals the table is a glossary, not a fresh list.
7. **Attach units/numeric values only to physical constants and measured quantities** (F = 9.65 × 10⁴, R = 8.31). Do not add units to dimensionless symbols.
8. **Insert one in-line authority citation** where a variable is ambiguous or non-obvious, using parentheses within the cell. Use it sparingly — one per table is enough.
9. **Close the table with a 3-clause caption:** (a) table number, (b) one-clause purpose ("to be combined in / to be plotted against / to be used to calculate…"), (c) source attribution with author/organisation and year.
10. **Flag every cell that draws on an external source with the same asterisk** that the caption defines, so the reader can trace any term back to its origin without leaving the table.
