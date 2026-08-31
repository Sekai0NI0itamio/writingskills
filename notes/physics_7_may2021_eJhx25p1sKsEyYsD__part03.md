# Idea Flow Notes: physics_7_may2021_eJhx25p1sKsEyYsD — This uncertainty is derived from half of the resolution of the grids on the oscilloscope display,

## Paragraph Flow (move by move)

**Paragraph 1 — Framing the calculation set**

- **Move 1 (continuation fragment / contextualising clause):** "as is standard for analogue equipment." — A trailing qualifier that retroactively justifies whatever uncertainty convention was just stated. It hands the reader to the next sentence because the reader now expects a *derivation* from that convention: what do you actually compute?
- **Move 2 (transition / result-announcement):** "From these, the following can be calculated:" — Promises a chain of derived quantities. The colon signals the equations that follow, so the reader is handed directly into the calculation block.

**Paragraph 2 — Displaying the calculation chain**

- **Move 3 (claim / opening equivalence):** "%𝑢𝑡𝑒𝑛𝑠𝑖𝑜𝑛 = %𝑢𝑚𝑎𝑠𝑠" — States that percentage uncertainty passes through unchanged. Hands forward because the reader needs to see *how* each individual %𝑢 is built before the chain is summed.
- **Move 4 (definition / first sub-formula):** "%𝑢𝑓,𝑠𝑖𝑔𝑛𝑎𝑙 𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟 = 𝑢𝑓,𝑠𝑖𝑔𝑛𝑎𝑙 𝑔𝑒ε𝑛𝑒𝑟𝑎𝑡𝑜𝑟 ⁄ 𝑓𝑠𝑖𝑔𝑛𝑎𝑙 𝑔𝑒𝑛𝑒𝑟𝑎τ₀𝑟 ∗ 100" — Defines the first uncertainty ratio. Hands to the next by introducing the doubling rule.
- **Move 5 (specification / consequence):** "%𝑢𝑓2 ,ℒ𝑠𝑖𝑔𝑛𝑎𝑙 𝑔𝑒𝑛𝑒𝑟𝑎τ₀𝑟 = 2 ∗ %𝑢𝑓,ℒ𝑠𝑖𝑔𝑛𝑎𝑙 𝑔𝑒𝑛𝑒𝑟𝑎τ₀𝑟" — Applies the squared-uncertainty rule to the first instrument. Hands forward by mirroring the structure with the second instrument.
- **Move 6 (parallel definition):** "%𝑢𝑓,𝑜𝑠𝑐𝑖𝑙𝑙𝑜𝑠𝑐𝑜𝑝𝑒 = 𝑢𝑛 𝑜𝑓 𝑔𝑟𝑖𝑑𝑠,𝑜𝑠𝑐𝑖𝑙𝑙𝑜𝑠𝑐𝑜𝑝𝑒 ⁄ 𝑛𝑔𝑟𝑖𝑑𝑠 ∗ 100" — Defines the second instrument's uncertainty by parallel construction. Hands to the closing doubling rule.
- **Move 7 (closing specification):** "%𝑢𝑓2 ,𝑜𝑠𝑐𝑖𝑙𝑙𝑜𝑠𝑐𝑜𝑝𝑒 = 2 ∗ %𝑢𝑓,𝑜𝑠𝑐𝑖𝑙𝑙𝑜𝑠𝑐𝑜𝑝𝑒" — Squares the second instrument's uncertainty, completing the symmetry.

**Paragraph 3 — Defining the variables**

- **Move 8 (explanation / variable key):** "Where 𝑢𝑡𝑒𝑛𝑠𝑖𝑜𝑛 = uncertainty of tension, … 𝑓𝑠𝑖𝑔𝑛𝑎𝑙 𝑔𝑒𝑛𝑒𝑟𝑎τ₀𝑟 = uncertainty of the frequency displayed" — Unpacks the symbols used above so the reader can interpret them. Hands forward by making the values themselves the next thing to expect.

**Paragraph 4 — Stating the result and locating it**

- **Move 9 (verdict / consequence):** "Therefore, the uncertainties are as follows." — Announces that numerical values are next. Hands to the table reference.
- **Move 10 (reference / pointer):** "See Table 2 in the Appendix for the full table of data." — Directs the reader to the stored results. Hands to the ordering note so the table can be cross-read.
- **Move 11 (specification / cross-reference):** "Note that the order is the same as in the previous table (i.e. row 1 corresponds to 500g, row 2 corresponds to 520g, etc.)." — Anchors the new table to the old one with a concrete example pair, so the reader can match rows.

---

## What This Section Does (content sequence)

This is an **uncertainty-propagation derivation block**. The ordered content moves are:

1. **Justify the chosen uncertainty convention** (1st) — so the reader accepts the rule that powers every formula.
2. **Transition into the calculation set** (2nd) — names what is about to be derived, priming them to read formulas as outputs of a stated method.
3. **State the parent equivalence** (3rd) — establishes the top-line identity (%𝑢𝑡𝑒𝑛𝑠𝑖𝑜𝑛 = %𝑢𝑚𝑎𝑠𝑠) which every line below must serve.
4. **Define the per-instrument %𝑢** (4th, 6th) — gives the raw ratio first for each device, mirroring each other.
5. **Apply the squared-uncertainty propagation rule** (5th, 7th) — turns each %𝑢 into %𝑢², because the final form is frequency-squared.
6. **Define every symbol used** (8th) — only after the reader has seen the structure, so the definitions feel like labels rather than prerequisites.
7. **Announce numerical results** (9th) — "therefore" links the algebra to a concrete outcome.
8. **Locate the full results in an appendix table** (10th) — keeps the prose body uncluttered.
9. **Anchor the new table to a prior one** (11th) — protects the reader's ability to cross-reference rows.

The *why* of this order: convention → transition → parent claim → component formulas → propagation rule → symbol key → verdict → evidence location → cross-reference. Each move depends on the one before; skipping ahead (e.g. defining symbols before showing the equations) would invert the cognitive load.

---

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Equation block with symbol key"**

```
"[Trailing contextual clause that justifies the convention]. From these,
the following can be calculated: [PARENT EQUATION]. [SUB-FORMULA 1].
[TRANSFORMATION OF SUB-FORMULA 1]. [SUB-FORMULA 2]. [TRANSFORMATION OF
SUB-FORMULA 2]. Where [var 1] = [gloss 1], [var 2] = [gloss 2],
[var 3] = [gloss 3], and [var 4] = [gloss 4]."
```

- **Slot 1** (contextual clause): adverbial phrase naming the convention's source domain (e.g. "as is standard for [equipment class]"). Shape: prepositional phrase, past/present tense.
- **Slot 2** (parent equation): the top-line identity the section proves.
- **Slots 3 + 4** (sub-formula + transformation): a raw ratio followed by its propagated (squared, doubled, summed) form. Shape: two aligned equations.
- **Slots 5 + 6** (second sub-formula + transformation): mirror of slots 3–4 for a second quantity.
- **Slot 7** (symbol key): comma-separated "X = gloss of X" chain.
- **How to fill with a different idea**: pick two measurements whose uncertainties combine (e.g. resistance from voltmeter + ammeter). Slot 1 cites the convention (e.g. "as is standard for digital multimeters"). Slot 2 is the top identity (e.g. %𝑅 = %𝑉 + %𝐼). Slots 3–6 build each side. Slot 7 defines every symbol used.
- **Original fill**: uncertainty-of-tension derivation using signal generator + oscilloscope (see text).
- **Demonstration fill with different idea**:
  "as is standard for digital multimeters. From these, the following can be calculated: %𝑢𝑅 = %𝑢𝑉 + %𝑢𝐼. %𝑢𝑉,𝑚𝑢𝑙𝑡𝑖𝑚𝑒𝑡𝑒𝑟 = (Δ𝑉𝑚𝑢𝑙𝑡𝑖𝑚𝑒𝑡𝑒𝑟 / 𝑉𝑚𝑢𝑙
