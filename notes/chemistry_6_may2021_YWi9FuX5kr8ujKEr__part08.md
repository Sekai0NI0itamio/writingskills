# Idea Flow Notes: chemistry_6_may2021_YWi9FuX5kr8ujKEr — 4 mol of S2O32- → 1 mol of O2                               titration = 0.352 + 4.85 = ±5.20%

## Paragraph Flow (move by move)

This section is not paragraphed prose; it is structured calculation work, so I will treat each logical block as a "paragraph" (numbered block).

**Block 1 — Stoichiometric calculation of moles of O₂**
- **Sentence 1 (calculation step):** "Number of moles of O2 in water sample = number of moles of thiosulfate ion / 4 = 8.10 × 10⁻⁵ / 4 = 2.02 × 10⁻⁵"
  - **Move:** worked calculation applying a stated mole ratio. The ratio "4 mol of S2O3²⁻ → 1 mol of O2" (quoted from the header strip) is the *specification* that justifies the division by 4.
  - **Hand-off:** the calculated moles value becomes the *input* for the next line, so the next sentence must convert moles → mass.
- **Sentence 2 (calculation step):** "Mass of O2 in water sample = Number of moles × Molar Mass = 2.02 × 10⁻⁵ × 32 = 6.48 × 10⁻⁴ g = 0.648 mg"
  - **Move:** dimension conversion (mol → g → mg), using the *definition* "Mass = moles × molar mass."
  - **Hand-off:** mass and volume are now both known, so the next sentence must divide them.
- **Sentence 3 (calculation step):** "Volume of water sample = 250 cm³ = 0.25 dm³"
  - **Move:** unit conversion of a given parameter, listed *separately* so it can be plugged into the next formula.
  - **Hand-off:** both inputs for concentration (mass, volume) are now in compatible units, so a concentration follows.
- **Sentence 4 (calculation step):** "Concentration of dissolved O2 = mass of Oxygen / volume of water = 0.648 / 0.25 = 2.59 mg/dm³ = 2.59 ppm"
  - **Move:** formula application + unit equivalence ("mg/dm³ = ppm" acts as *definition*), producing the headline number.
  - **Hand-off:** a final "∴" conclusion sentence summarises the value WITH its uncertainty.

**Block 2 — Uncertainty cascade (right-hand column)**
- **Sentence 1 (evidence handling):** "Number of moles of O2 in water sample = ±5.20%"
  - **Move:** declares a propagated uncertainty, *referring back* to the moles calculation in Block 1.
  - **Hand-off:** the reader must see how 5.20% was built — so the next sentence breaks it down.
- **Sentence 2 (mechanism/unpack):** "titration = 0.352 + 4.85 = ±5.20%"
  - **Move:** shows the *components* of the 5.20% (two pipette/volumetric uncertainties added) — this is the *cause* of the percentage above.
  - **Hand-off:** same logic must now apply to the mass step → next sentence carries that down.
- **Sentence 3 (cascade step):** "Mass of O2 in water sample = ±5.20%"
  - **Move:** *consequence* — uncertainty is unchanged because multiplying by molar mass is exact (no new apparatus).
  - **Hand-off:** now the volume uncertainty (a new measured quantity) must be added.
- **Sentence 4 (cascade step):** "Volume of water sample = 250 × 100 … = ±4.00%" (i.e. 4.00% from the 250 cm³ volumetric flask)
  - **Move:** *specification* of the second uncertainty source.
  - **Hand-off:** two independent uncertainty percentages are now in hand → they must be combined for concentration.
- **Sentence 5 (combine):** "Concentration of dissolved O2 = 4.00 + 5.20 = ±9.20%"
  - **Move:** *addition* of the two percentage uncertainties (because concentration = mass/volume, a quotient, so absolute uncertainties add when expressed as %).
  - **Hand-off:** the reader needs the conclusion line carrying both value and uncertainty together — final ∴ sentence closes the block.

**Block 3 — Headline conclusion for Flask A1**
- **Sentence 1 (verdict):** "∴ Concentration of dissolved O2 in Flask A1 at day 5 = 2.59 ppm (±9.20%)"
  - **Move:** final summary restating value + uncertainty with a "therefore" symbol.
  - **Hand-off:** this concentration is now a *variable* needed in the next block — the BOD calculation.

**Block 4 — BOD calculation**
- **Sentence 1 (definition/formula):** "BOD = Day 1 dissolved O2 conc. in Flask A − Day 5 dissolved O2 conc. in Flask A1"
  - **Move:** states the *definition* of BOD as a difference of two concentrations, naming both inputs explicitly.
  - **Hand-off:** inputs are named, so the next sentence performs the subtraction.
- **Sentence 2 (worked calculation):** "∴ BOD = 3.92 − 2.59 = 1.33 ppm"
  - **Move:** substitution + arithmetic, producing the numerical answer.
  - **Hand-off:** uncertainty is missing → next block must add it.

**Block 5 — Uncertainty for BOD (right column)**
- **Sentence 1 (source 1):** "Day 1 dissolved O2 conc. in Flask A = (7.56/… × 3.92) = ±0.296 ppm"
  - **Move:** uncertainty on input #1, converted from % to absolute ppm.
  - **Hand-off:** next sentence must do the same for input #2 so they can be summed.
- **Sentence 2 (source 2):** "Day 5 dissolved O2 conc. in Flask A1 = (9.20/100 × 2.59) = ±0.238 ppm"
  - **Move:** uncertainty on input #2 in absolute ppm.
  - **Hand-off:** two absolute uncertainties are now available → sum them.
- **Sentence 3 (combine):** "BOD = 0.296 + 0.238 = ±0.534 ppm"
  - **Move:** *addition* of absolute uncertainties (because BOD is a difference, absolute uncertainties add).

**Block 6 — Headline conclusion for BOD + generalisation**
- **Sentence 1 (verdict):** "∴ BOD for water sample in Flask A at pH 7.10 = 1.33 ppm (±0.534 ppm)"
  - **Move:** final restated result with uncertainty, framed by sample identity and pH.
  - **Hand-off:** the reader is told the same procedure was repeated — so the *transition* sentence must signal that.
- **Sentence 2 (transition/generalisation):** "Similar calculations were carried out to determine BOD values for Flasks B and B1, C and C1."
  - **Move:** signals that the whole worked block is a *template*, not a one-off — invites the reader to mentally replicate it.

---

## What This Section Does (content sequence)

This is a **quantitative results + uncertainty analysis** section. The ordered move sequence is:

1. **Stoichiometric / formula conversion chain.** Start from a measured titration quantity → apply a mole ratio → convert moles → mass → concentration. Order matters because *each output is the input of the next formula*; you cannot skip a step.
2. **Parallel uncertainty cascade.** Build the uncertainty *alongside* the calculation, not after. Each step carries its own apparatus uncertainty, and each conversion either keeps it unchanged (× exact constants like molar mass) or adds a new source (volumetric flask %). Order matters because you must identify *where the uncertainties enter* before combining.
3. **Combine uncertainties at the end of the chain.** Add percentage uncertainties for multiplicative steps; add absolute uncertainties for additive/subtractive steps. This must come *last*, after both sources are quantified.
4. **Headline "∴" verdict line.** Restate the final number WITH its uncertainty in one bracketed expression — this is what the marker reads first.
5. **Define the derived quantity (BOD) using the headline values.** State the formula *before* substituting, naming both inputs, so the reader knows what is being differenced.
6. **Substitute and calculate.** Plug values into the formula; state the numerical result.
7. **Uncertainty on the derived quantity.** Convert each input's % uncertainty to an absolute ppm uncertainty, then *add* them (because the operation is subtraction).
8. **Second "∴" verdict.** Restate BOD with uncertainty.
9. **"Similar calculations were carried out…" transition.** Signals that the worked example is a template for the remaining flasks.

**Why this order:** each move produces a value or uncertainty that is a *prerequisite* for the next formula. If you swap steps 1 and 3 you cannot compute concentration; if you combine uncertainties before identifying sources, the number is unjustified.

---

## Paragraph Skeletons (replicable templates)

### Skeleton A — "Concentration calculation paragraph" (Block 1)

**Slot template:**
> [Quantity A] = [raw measured value] ÷ [stoichiometric coefficient from reaction equation] = [numerical result in mol].
> [Quantity B, e.g. mass] = [Quantity A] × [molar mass] = [numerical result, with unit conversion to mg].
> [Volume of sample] = [raw volume] = [volume in dm³].
> [Final concentration] = [Quantity B] / [Volume of sample] = [numerical result in mg/dm³ = ppm].
> ∴ [Headline statement]: [value] ([units]).

**Slot instructions:**
- **Slot 1 (named quantity + stoichiometric step):** name the analyte's moles; divide the titration moles by the stoichiometric ratio from the balanced equation (an integer ≥ 1). Past/present tense, equals-sign format.
- **Slot 2 (mass conversion):** multiply moles by the analyte's molar mass; convert g → mg so the final unit is compatible with the volume unit.
- **Slot 3 (volume parameter, standalone):** state the sample volume and convert cm³ → dm³ (× 1000).
- **Slot 4 (final concentration):** divide mass by volume; explicitly note that mg/dm³ ≡ ppm for dilute aqueous solutions.
- **Slot 5 (∴ verdict):** restate the concentration, naming the flask and time point.

**Original fill (paraphrased):** "Number of moles of O2 … = 8.10 × 10⁻⁵ / 4 = 2.02 × 10⁻⁵ … Mass = 2.02 × 10⁻⁵ × 32 = 0.648 mg … Volume = 250 cm³ = 0.25 dm³ … Concentration = 0.648 / 0.25 = 2.59 mg/dm³ = 2.59 ppm."

**Demonstration fill with a different idea (hardness of water by EDTA titration):**
> Number of moles of Ca²⁺ in water sample = moles of EDTA / 1 = 4.30 × 10⁻⁴ / 1 = 4.30 × 10⁻⁴ mol.
> Mass of CaCO₃ equivalent = 4.30 × 10⁻⁴ × 100 = 4.30 × 10⁻² g = 43.0 mg.
> Volume of water sample = 100 cm³ = 0.100 dm³.
> Concentration of hardness = 43.0 / 0.100 = 430 mg/dm³ = 430 ppm CaCO₃.
> ∴ Total hardness of sample X = 430 ppm CaCO₃.

---

### Skeleton B — "Uncertainty cascade paragraph" (Block 2)

**Slot template:**
> [Final quantity] = ±[X]%.
> [Component 1] + [Component 2] = ±[X]%.
> [Sub-step with no new apparatus] = ±[X]%.
> [Sub-step introducing new apparatus, e.g. volumetric flask] = ±[Y]%.
> [Combined final quantity] = ±[X] + ±[Y] = ±[X+Y]%.

**Slot instructions:**
- **Slot 1 (declare total):** state the propagated uncertainty on the final answer as a percentage.
- **Slot 2 (decompose the dominant source):** show the *two* apparatus uncertainties (e.g. pipette + burette) that sum to the percentage above.
- **Slot 3 (carry-through):** a step that uses an exact constant — uncertainty is unchanged.
- **Slot 4 (new source):** identify the new measured quantity (volumetric flask) and quote its own % uncertainty.
- **Slot 5 (combine):** add the two percentage uncertainties because the operation is division.

**Original fill (paraphrased):** "Number of moles of O2 = ±5.20%. Titration = 0.352 + 4.85 = ±5.20%. Mass of O2 = ±5.20%. Volume = 250 × 100 = ±4.00%. Concentration = 4.00 + 5.20 = ±9.20%."

**Demonstration fill with a different idea (pH measurement uncertainty):**
> pH reading = ±2.0%.
> Buffer calibration + electrode drift = 0.5 + 1.5 = ±2.0%.
> Temperature compensation = ±2.0% (no new apparatus).
> Slope of calibration curve = ±1.0%.
> Combined reading = ±2.0 + ±1.0 = ±3.0%.

---

### Skeleton C — "Derived quantity paragraph" (Block 4 + 5 + 6)

**Slot template:**
> [Derived quantity, e.g. BOD] = [Input 1 name] − [Input 2 name].
> ∴ [Derived quantity] = [value 1] − [value 2] = [numerical result].
> [Uncertainty on Input 1] = ([%] / 100) × [value 1] = ±[absolute].
> [Uncertainty on Input 2] = ([%] / 100) × [value 2] = ±[absolute].
> [Derived quantity] = [abs 1] + [abs 2] = ±[total].
> ∴ [Headline statement naming sample and condition] = [value] (±[total]).

**Slot instructions:**
- **Slot 1 (formula + named inputs):** state the operation *verbally* with both input names spelled out.
- **Slot 2 (substitution):** plug numbers in, present the difference as a single equals-sign chain.
- **Slot 3 & 4 (per-input uncertainties, as absolute values):** convert each input's % uncertainty to absolute units by multiplying by the value.
- **Slot 5 (combine):** *add* absolute uncertainties because the operation is subtraction.
- **Slot 6 (∴ verdict with context):** name the sample, the condition (e.g. pH), and present value ± uncertainty together.

**Original fill (paraphrased):** "BOD = Day 1 dissolved O2 conc. in Flask A − Day 5 dissolved O2 conc. in Flask A1. ∴ BOD = 3.92 − 2.59 = 1.33 ppm. Day 1 … = ±0.296 ppm. Day 5 … = ±0.238 ppm. BOD = 0.296 + 0.238 = ±0.534 ppm. ∴ BOD for water sample in Flask A at pH 7.10 = 1.33 ppm (±0.534 ppm)."

**Demonstration fill with a different idea (rate of reaction from two concentration readings):**
> Rate = [Reactant] at t = 0 s − [Reactant] at t = 60 s.
> ∴ Rate = 0.040 − 0.018 = 0.022 mol/dm³/s.
> [Reactant] at t = 0 = (2.0/100) × 0.040 = ±0.0008 mol/dm³/s.
> [Reactant] at t = 60 = (3.5/100) × 0.018 = ±0.00063 mol/dm³/s.
> Rate = 0.0008 + 0.00063 = ±0.00143 mol/dm³/s.
> ∴ Rate of reaction for trial 2 at 298 K = 0.022 mol/dm³/s (±0.00143).

---

## Express-Idea Vocabulary

**Sequencing / structuring the calculation chain**
- "∴" (three-dot therefore) — used to flag every *conclusion* line: "∴ Concentration of dissolved O2 in Flask A1 at day 5 = 2.59ppm".
- "Number of moles of O2 in water sample = number of moles of thiosulfate ion / 4" — implicit "first, divide by stoichiometric coefficient."
- "Mass of O2 in water sample = Number of moles × Molar Mass" — implicit "next, convert using molar mass."

**Cause / consequence (uncertainty propagation)**
- "= ±5.20%" used as a *consequence marker* after addition: "titration = 0.352 + 4.85 = ±5.20%".
- "4.00 + 5.20 = ±9.20%" — addition expressed as direct consequence.

**Specification (naming sources)**
- "Volume of water sample = 250 × 100" — specifying the apparatus that contributes the second uncertainty.
- "Day 1 dissolved O2 conc. in Flask A" / "Day 5 dissolved O2 conc. in Flask A1" — explicit naming of *which* input is being differenced.

**Evidence handling / quantitative reporting**
- "Number of moles of O2 in water sample = 8.10 × 10⁻⁵ / 4 = 2.02 × 10⁻⁵" — figures quoted in scientific notation with explicit intermediate steps.
- "0.296 + 0.238 = ±0.534ppm" — quoting absolute uncertainties to 3 sig figs.

**Explanation / definition verbs**
- "Mass of O2 in water sample = Number of moles × Molar Mass" — *defined as* relationship.
- "Concentration of dissolved O2 = mass of Oxygen / volume of water" — *defined as* quotient.
- "BOD = Day 1 dissolved O2 conc. in Flask A − Day 5 dissolved O2 conc. in Flask A1" — *defined as* a difference.

**Transition / generalisation**
- "Similar calculations were carried out to determine BOD values for Flasks B and B1, C and C1." — *generalisation cue* telling the reader the worked example is a template.

---

## How to Explain an Idea (replication steps)

This section relies on the **"stacked worked calculation with parallel uncertainty cascade"** pattern. To explain any NEW derived quantitative result:

1. **State the headline formula first, naming every input variable in words** (not symbols). Example: "BOD = Day 1 dissolved O2 conc. in Flask A − Day 5 dissolved O2 conc. in Flask A1."
2. **Substitute numerical values into that formula in one equals-sign line**, showing the arithmetic. Example: "∴ BOD = 3.92 − 2.59 = 1.33 ppm."
3. **For each input variable, quote its own percentage uncertainty in a separate short line**, converting it to an absolute uncertainty in the *same units as the input*. Example: "Day 1 … = ±0.296 ppm."
4. **Combine the absolute uncertainties using the rule for the operation** — *add* for ±/∓ (difference/sum), *add percentages* for ×/÷. Example: "BOD = 0.296 + 0.238 = ±0.534 ppm."
5. **Close with a single "∴" verdict line** that names the *sample identity* and *condition* (e.g. flask, pH, temperature), then states the value and bracketed uncertainty together. Example: "∴ BOD for water sample in Flask A at pH 7.10 = 1.33 ppm (±0.534 ppm)."
6. **End with a transition sentence** that signals the same template was repeated for the remaining cases. Example: "Similar calculations were carried out to determine BOD values for Flasks B and B1, C and C1."

The pattern is: *formula → substitute → per-input uncertainty → combine → ∴ verdict → template-signal*. The reader is never asked to hold an un-named variable; every number is either an input, an intermediate, or a final quoted result.
