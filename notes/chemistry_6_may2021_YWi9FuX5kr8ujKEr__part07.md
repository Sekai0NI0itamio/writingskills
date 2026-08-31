# Idea Flow Notes: chemistry_6_may2021_YWi9FuX5kr8ujKEr — 4 mol of S2O32- → 1 mol of O2

## Paragraph Flow (move by move)

The text is not organised in conventional prose paragraphs but in **calculation blocks** arranged in two side-by-side columns: a main calculation on the left, an uncertainty calculation on the right. Each logical "paragraph" is a short worked-step, and each sentence-line is a single move. I will track the LEFT column as the logical spine (it is the one the reader is led through), noting where the right column echoes it.

**Calculation block 1 — deriving moles of O₂**

1. **Quote:** "Number of moles of O2 in water"
   *Move:* Header / claim-frame (defines what is about to be solved).
   *Hand-off:* the proportionality constant in the next line makes the claim solvable.

2. **Quote:** "4 mol of S2O32- → 1 mol of O2"
   *Move:* Stoichiometric specification — the ratio that converts between substances.
   *Hand-off:* supplies the conversion factor for the substitution below.

3. **Quote:** "∴ number of moles of thiosulfate ion / 4 = 1.23 × 10−4 / 4"
   *Move:* Worked substitution into the stoichiometric ratio.
   *Hand-off:* the result of the division is the bridge to the next-line quantity.

4. **Quote:** "= 3.07 × 10-5"
   *Move:* Numerical result of the division.
   *Hand-off:* because the reader has just been given moles of O₂, the next move is to convert moles into mass.

**Calculation block 2 — converting moles to mass**

5. **Quote:** "Mass of O2 in water sample = Number of moles × Molar Mass"
   *Move:* Definition of the formula to be applied (what mass equals).
   *Hand-off:* the formula demands a numeric substitute, which appears immediately after.

6. **Quote:** "= 3.07 × 10-5 × 32 = 9.81 × 10-4g = 0.981mg"
   *Move:* Worked substitution and chained unit conversion (g → mg).
   *Hand-off:* with mass secured, the next block can pivot to volume.

**Calculation block 3 — preparing volume**

7. **Quote:** "Volume of water sample = 250cm³ = 0.25dm³"
   *Move:* Definition + unit conversion of the divisor quantity.
   *Hand-off:* the reader now has both numerator (mass in mg) and denominator (volume in dm³), so a concentration can be written.

**Calculation block 4 — assembling concentration**

8. **Quote:** "Concentration of dissolved O2 = mass of Oxygen / volume of water = 0.981 / 0.25"
   *Move:* Definition of concentration formula + numerical substitution.
   *Hand-off:* the substitution demands a quotient and a unit label.

9. **Quote:** "= 3.92mg/dm3 = 3.92ppm"
   *Move:* Quotient + unit equivalence statement (mg/dm³ ≡ ppm in dilute aqueous solution).
   *Hand-off:* the result is the *headline quantity*; the next line frames it as the conclusion.

10. **Quote:** "∴ Concentration of dissolved O2 in Flask A at day 1 = 3.92ppm"
    *Move:* Verdict / context-tagged conclusion tying the number back to the specific flask and day.
    *Hand-off:* the verdict invites uncertainty to be evaluated; the right column then begins in parallel.

**Right column — uncertainty propagation (parallel moves)**

11. **Quote:** "sample = ±3.56%"
    *Move:* Header stating the propagated uncertainty for the moles-of-O₂ quantity (echoing block 1).
    *Hand-off:* the reader's eye then moves down to the mass block.

12. **Quote:** "Mass of O2 in water sample = ±3.56%"
    *Move:* Re-statement of the same percentage for the mass, with explicit justification shown: "10".
    *Hand-off:* this is the cause for the concentration block's added percentage.

13. **Quote:** "Volume of water sample = 250 × 10 / 100 = ±4.00%"
    *Move:* Derivation of the volume's percentage uncertainty from absolute ±10 on 250.
    *Hand-off:* the volume uncertainty combines with the mass uncertainty to give the final combined value.

14. **Quote:** "Concentration of dissolved O2 = 4.00 + 3.56 = ±7.56%"
    *Move:* Addition of the two independent percentage uncertainties — the final propagated verdict.
    *Hand-off:* the column is then re-opened with "Flask A1, Day 5", hand-off by time/specimen change.

## What This Section Does (content sequence)

This is a **worked-calculation section** running two parallel streams (calculation + uncertainty). The ordered logic is:

1. **Anchor the conversion factor first.** State the stoichiometric or definitional ratio before substituting any number — because every later quantity depends on it.
2. **Substitute and compute in vertical steps.** Each line carries one operation; equals signs line up so the reader can scan top-to-bottom.
3. **Convert units at the moment of definition, not at the end.** cm³ → dm³ and g → mg appear inline with the quantity they belong to, so the final unit is already correct when written.
4. **Build toward a headline ratio.** Mass and volume are prepared separately so that concentration = mass/volume can be assembled in one display line.
5. **State the formula before the substitution.** Each new quantity (mass, volume, concentration) is introduced as "X = formula" *then* "= numbers". This separates principle from arithmetic.
6. **Attach the result to the specific context last.** Only at the end does "Flask A at day 1" appear, because the value is meaningless until tagged.
7. **Run uncertainty in a parallel column.** Each main line acquires a matching uncertainty line on the right, propagating top-to-bottom, ending with the combined sum of percentage uncertainties.

The order exists because every quantity is *consumed* by the next: ratio consumes the species names, moles consume the ratio, mass consumes moles, concentration consumes mass and volume, and verdict consumes concentration. Removing any earlier step would break the substitution chain of the next.

## Paragraph Skeletons (replicable templates)

**SKELETON A — the stoichiometric / formula block**

```
HEADER (quantity to be found)
∴ SUBSTITUTION FORMULA: [symbol]/[coefficient] = [given value]/[coefficient]
= RESULT
```

- **Slot 1 — header:** a noun-phrase stating what is being solved for ("Number of moles of O2 in water"). Grammatically a noun phrase; can be lifted directly.
- **Slot 2 — substitution line:** a stoichiometric ratio (e.g. "4 mol of A → 1 mol of B") combined with a fraction in which the given value is divided by the stoichiometric coefficient. Grammatically a divided expression.
- **Slot 3 — result line:** the quotient of slot 2, alone on its line, prefixed by `=`.

**How to fill with a different idea:** Choose any chemistry problem with a stoichiometric step. Pick a 2:1 or 1:2 ratio (e.g. "2 mol of H₂ → 1 mol of O₂"). Slot 1 names your target substance. Slot 2 lays out the ratio arrow then substitutes a given experimental number divided by the coefficient. Slot 3 is the calculator output.

**Original fill:** "Number of moles of O2 in water / ∴ 4 mol of S2O32- → 1 mol of O2 / number of moles of thiosulfate ion / 4 = 1.23 × 10−4 / 4 / = 3.07 × 10-5"

**Demonstration fill (different idea — acid–base titration):**
```
Number of moles of HCl neutralised
∴ 1 mol of NaOH → 1 mol of HCl
number of moles of NaOH / 1 = 4.20 × 10⁻³ / 1
= 4.20 × 10⁻³
```

**SKELETON B — the formula-then-substitute block**

```
QUANTITY = FORMULA WORDS
= SUBSTITUTED NUMBERS = CONVERTED UNIT
```

- **Slot 1 — formula words:** a plain-English statement of what the quantity equals ("Mass of O2 in water sample = Number of moles × Molar Mass"). Noun-phrase equated with a verbal formula.
- **Slot 2 — substituted numbers + unit conversion:** the same equals-sign continued with numeric substitution, immediately followed by a unit conversion in the same line. Grammatically a chain of `= … = …` segments.

**How to fill with a different idea:** Identify the quantity you need (mass, energy, moles). Slot 1 writes the defining equation in words. Slot 2 plugs the previous-block's answer and the constant, then converts to the headline unit on the same line.

**Original fill:** "Mass of O2 in water sample = Number of moles × Molar Mass / = 3.07 × 10-5 × 32 = 9.81 × 10-4g = 0.981mg"

**Demonstration fill (different idea — energy released):**
```
Energy released by reaction = mass × specific heat capacity × ΔT
= 0.250 × 4.18 × 12.5 = 13.06 J = 0.01306 kJ
```

**SKELETON C — the parallel uncertainty block**

```
MATCHING QUANTITY NAME = ±X.XX%
```

- **Slot 1:** the exact quantity name from the main calculation, copied verbatim.
- **Slot 2:** an equals sign, then the propagated percentage uncertainty, then `%`.

Each main calculation line that introduces a *new* quantity gets a sibling uncertainty line in the right column carrying the same name. Final lines combine via addition.

**How to fill with a different idea:** Walk down the main column after you finish; for each quantity whose uncertainty has now propagated, write a one-line echo with `= ±value%`. For the final combined quantity, add the two independent percentages: `= ±(a + b)%`.

**Original fill:** "Mass of O2 in water sample = ±3.56%" → "Volume of water sample = 250 × 10 / 100 = ±4.00%" → "Concentration of dissolved O2 = 4.00 + 3.56 = ±7.56%"

**Demonstration fill (different idea — projectile experiment):**
```
Range of projectile = ±2.5%
Time of flight = 1.20 × 0.01 / 1.20 = ±0.83%
Horizontal range = 2.5 + 0.83 = ±3.33%
```

**SKELETON D — the verdict line**

```
∴ [Context-tagged quantity name] = [headline number] [(combined %)]
```

- **Slot 1 — therefore marker:** the `∴` symbol signalling a derived conclusion.
- **Slot 2 — context-tagged name:** the headline quantity with the specific specimen, day, or sample appended ("in Flask A at day 1").
- **Slot 3 — number + uncertainty in parentheses:** the final value followed by the propagated uncertainty in brackets.

**How to fill with a different idea:** After all uncertainty lines are done, drop a `∴`, restate the headline quantity with its specific tag, give the final number, and append the combined uncertainty.

**Original fill:** "∴ Concentration of dissolved O2 in Flask A at day 1 = 3.92ppm (±7.56%)"

**Demonstration fill (different idea — buffer pH):**
```
∴ pH of acetate buffer in Trial 2 = 4.74 (±1.2%)
```

## Express-Idea Vocabulary

**Sequencing / chain markers**
- "∴" — verdict marker, used to open a derived conclusion. Quote: "∴ Concentration of dissolved O2 in Flask A at day 1".

**Specification (formula-then-substitute verbs)**
- "Number of moles = Concentration × Volume" — explicit equals-definition linking principle to arithmetic. Quote: "Number of moles = Concentration × Volume = 0.0393× 2.06/1000".

**Cause / chain-equality**
- "= … = … = …" — chained equals signs that march through unit conversions in a single line. Quote: "= 3.07 × 10-5 × 32 = 9.81 × 10-4g = 0.981mg".

**Definition / identification verbs**
- (implicit) "Mass of O2 in water sample = …" — defining a quantity before computing it; the noun phrase itself acts as the definitional verb.

**Evidence / value handling**
- "Average Titre/Volume of Na2S2O3 = 2.06cm3" — a measured value stated with units inline, acting as the evidentiary anchor for the next calculation.

**Uncertainty-specific verbs / markers**
- "= ±3.56%" / "= ±4.00%" / "= ±7.56%" — propagation markers; the final line uses "+" as the combining operator: "Concentration of dissolved O2 = 4.00 + 3.56 = ±7.56%".

**Unit-conversion verbs (implicit)**
- "= 0.25dm3" / "= 0.981mg" / "= 3.92ppm" — the equals sign carries an implicit "converted to" meaning, signalling unit transformation rather than arithmetic change.

**Connectives between blocks**
- Vertical stacking with shared equals-sign columns; no prose connectives — visual alignment replaces "next", "then", "therefore".

## How to Explain an Idea (replication steps)

This section uses the **worked-calculation + parallel-uncertainty** pattern. To replicate it for a NEW idea, follow these numbered steps:

1. **Choose the headline quantity** you want the reader to arrive at (e.g. concentration, energy, pH, yield). Write it as a noun-phrase header at the top.
2. **List every intermediate quantity in dependency order.** If quantity B needs A, A's line comes first.
4. **For the first step that uses a conversion ratio, write the ratio as an arrow** ("4 mol of A → 1 mol of B") *before* the substitution — readers need the relationship to interpret the division.
5. **Substitute on the next line:** write the given value divided by the relevant coefficient. The quotient appears on the line beneath, alone, prefixed by `=`.
6. **For every subsequent derived quantity, write the defining equation in words first** ("Mass of X = Number of moles × Molar Mass"). This is the *principle* step.
7. **Continue the same line with the numeric substitution**, and chain an equals-sign unit conversion in the same line ("= 3.07 × 10-5 × 32 = 9.81 × 10-4g = 0.981mg"). Each `=` is one operation.
8. **Convert each input unit inline** as soon as the quantity is introduced, not at the end ("= 250cm³ = 0.25dm³"). This means the final headline carries the right unit automatically.
9. **Assemble the headline as a ratio in one display line:** "Concentration = mass / volume = numbers / numbers = result unit = equivalent unit". Use an explicit equivalence ("mg/dm³ = ppm") when one exists.
10. **Open a verdict line beginning with `∴`**, restating the headline quantity *with its context tag* (flask, day, trial) attached. This is where the number becomes meaningful.
11. **In a parallel right column, copy each main quantity's name verbatim** and assign it a `= ±X%` line. For quantities derived from an instrument with an absolute reading uncertainty, compute percentage uncertainty using `(absolute / value) × 100` on the same line.
12. **For the headline, add the independent percentage uncertainties** ("= a + b = ±c%"). This is the final propagated uncertainty.
13. **Stop.** Do not narrate; do not explain "therefore"; do not repeat what the arithmetic already shows. The vertical chain of equals-signs *is* the explanation.
