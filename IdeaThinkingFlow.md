# IdeaThinkingFlow — How 6/7-Graded IB Students Express Ideas

> Distilled by AI from 10 section-part analyses of 80 grade-6/7 IB exemplar essays.
> Every skeleton and flow pattern carries verbatim quotes from the corpus. This file is a
> COMPLIANCE SPEC for expressing ideas: paragraphs follow these flow patterns, skeletons are
> filled per their slot instructions, and explanations use these replication steps. Pair with
> writing-rules (sentence structures) — that file governs sentence construction; this file
> governs how ideas move.



## General: How an Idea Moves Through a Paragraph

### Core Logic-Flow Patterns (most fundamental → rarest)

**P1 — Section Label + Claim → Formula → Instance Selection**
Header (caps noun phrase) → claim ("[Subject] has [feature] based on [statistic]") → display formula with "where…" clause defining symbols → "Taking/Using the data of [subset], the [statistic] can be calculated."

**P2 — Stage Label → Formula → Substitution → Algebraic Move**
Ordinal step marker ("first/next/final step is [gerund]") → symbolic formula → same formula with one literal inserted → short definition for remaining symbol → "Squaring both sides…"/"Square rooting both sides means that…" → simplified equation.

**P3 — Full Expansion → Collapse → Reverse Operation**
Fraction with every term expanded inline → "Completing all operations…, the fraction becomes [result]" → name intermediate result (variance, etc.) → inverse operation recovers base quantity.

**P4 — Plug-Back → Numeric Result → Plain-English Interpretation**
"Now the value for [intermediate] can be plugged into the equation [formula]" → symbol-to-value assignment → fully substituted equation → "This means that [percentage/threshold/bound]."

**P5 — Rule → Instance → Expansion → Aggregation (for already-introduced formulas)**
"In order to get [X], the [op] must be [verb-ed]… and added together." → "This will be demonstrated with [case]." → full algebra for that case → "This should be repeated for the other [N−1]…" → "Therefore, [STAT] = r₁ + … = T."

**P6 — Worked Example + Sweep**
One fully worked case with raw values → "The same steps can be repeated to give [label] = [val], …" list → "These steps can be repeated with the [second variable]" parallel list.

**P7 — Prerequisite → Procedure → Execution**
"The [quantity] for [var(s)] [is/are] needed." → "For [A], this is X, and for [B] it is Y." → imperative operations → long equation = result.

**P8 — Temporal Hinge**
"Then the [next quantity] must be calculated, using the equation [formula] = [display form]."

**P9 — Standard-Mechanism → Named-Substitute → Operationalise** *(rarer: hypothesis-building)*
"…[prior mechanism]. [whereas/in contrast clause flipping condition]. [Test substance] is [category] that can act as a substitute for [standard agent] and have similar effects."

**P10 — Instrument-Error Cascade** *(rarer: uncertainty flow)*
"[Carry-over announcing upcoming calculation]. [Instrument A] had a margin of error of ±[value][unit]. [Instrument B] had ±[value][unit]. [Instrument C] had ±[value][unit]."

---

### Replicable Skeletons

**S1 — Definition → Instance Selection → Procedure Announcement**
```
[Section label]. [Subject] has [feature] based on [statistic]. 
[STAT] or [formula] = [formula] where [sym1] represents [def] 
and [sym2] is [def]. Taking the data of [subset], 
the [statistic] can be calculated.
```
- Original: `PROCESSED DATA. The raw data has error bars based on the standard error of the mean (SEM). SEM or s̄x = σ/√n where σ represents a sample's standard deviation and n is the amount of data points. Taking the data of the 40ml shoot length, the SEM can be calculated.`
- Demo: `NORMALISED YIELDS. The reaction output has confidence limits based on the standard error of the proportion (SEP). SEP or p̂ = √(p(1−p)/n) where p is the observed proportion and n is the trial count. Taking the data of the 50 °C trial run, the SEP can be calculated.`

**S2 — Stage Label → Formula with One Substitution**
```
The first step is [gerund]. [formula] = [display]. 
[formula with one literal inserted]. [Remaining sym] 
is equal to [def], [value]. [Algebraic move verb] 
[both sides] [simplifies]. [simplified formula].
```
- Original: `The first step is finding the value of the standard deviation. σ = √(1/(N−1) Σ(xᵢ − x̄)²). The mean can be calculated as x̄ = (3.1+3.7+…)/7 = 3.914… N is equal to the number of specimens, 7. Squaring both sides of the equation simplifies the equation. σ² = Σ(xᵢ − x̄)²/(N−1).`
- Demo: `The first step is finding the value of the variance. Var(X) = (1/(n−1)) Σ(xᵢ − μ)². The mean can be calculated as μ = (12+14+15+16+18)/5 = 15. n is equal to the number of readings, 5. Squaring the deviation for each term gives the squared-error total. Var(X) = Σ(xᵢ − μ)²/(n−1).`

**S3 — Full Expansion → Collapse → Reverse Operation**
```
Σ[…]/(n−1) = (a₁−m)² + (a₂−m)² + … / (n−1). 
Completing all operations…, the fraction becomes [result]. 
The [intermediate name] is [result]. 
[Inverse op] both sides means that [base quantity] = [result].
```
- Original: `Σ(xᵢ − x̄)²/(N−1) = (3.1−3.9…)² + … / (7−1). Completing all operations…, the fraction becomes 0.17476… The variance is 0.17476… Square rooting both sides means that σ = 0.4180…`
- Demo: `Σ(pᵢ − p̄)²/(n−1) = (0.12−0.20)² + (0.18−0.20)² + (0.22−0.20)² + (0.28−0.20)² / (4−1). Completing all operations…, the fraction becomes 0.016. The variance is 0.016. Square rooting both sides means that the standard deviation = 0.1265.`

**S4 — Plug-Back → Numeric Result → Interpretation**
```
Now the value for [intermediate] can be plugged into the equation 
[formula]. [Sym] is [value], so the equation becomes 
[formula with values] = [result]. This means that [plain-English].
```
- Original: `Now the value for the standard deviation can be plugged into the equation s̄x = σ/√n. N is 7, so the equation becomes s̄x = 0.418…/√7 = 0.158… This means that the standard amount of error for that group sample is 15%.`
- Demo: `Now the value for the standard deviation can be plugged into the equation CI = 1.96·σ/√n. n is 30, so the equation becomes CI = 1.96·0.42/√30 = 0.150. This means that the 95% confidence interval half-width for that group sample is 0.15 units.`

**S5 — One Worked Case + Sweep**
```
[Case]'s ([role]) [quantity] = (raw values) / n = decimal. 
The same steps can be repeated to give [label₁] = [val], …, 
and [labelₙ] = [val]. These steps can be repeated with the 
[second var] to give [parallel labels] = [values].
```
- Original: `Factor 1's (control) mean of DV1 = (4.1+4.4+4.6+5+5.1+5.2+5.4)/7 = 4.82857143. The same steps can be repeated to give 1F2 = 5.75714286, DV1F3 = 6.7, DV1F4 = 5.07142857, and DV1F5 = 3.91428571. These steps can be repeated with the second dependent variable to give DV2F1 = 27.94…, DV2F2 = 35.03…, …, DV2F5 = 16.06….`
- Demo: `Temp 1's (control) mean time = (3.2+3.5+3.1+3.4+3.3)/5 = 3.30 s. The same steps can be repeated to give T2 = 2.74 s, T3 = 2.20 s, T4 = 1.88 s, and T5 = 1.62 s. These steps can be repeated with colour intensity to give C1 = 0.41, C2 = 0.58, C3 = 0.69, C4 = 0.77, and C5 = 0.83.`

**S6 — Rule → Instance → Expansion → Aggregation**
```
In order to get [X], the [op] must be [verb-ed] from the [ref] 
of their respective [items] and added together. This will be 
demonstrated with [case]. (algebra for case) = R₁. 
This should be repeated for the other [N−1] [cases]. 
Therefore, [STAT] = r₁ + … + r_N = T.
```
- Original: `In order to get this, the mean of the different factors (Fk) must be subtracted from the data points of their respective factors squared and added together. This will be demonstrated with the control group of the first dependent variable. (4.1−4.83)² + … = 1.334. This should be repeated for the other 4 groups. Therefore, SSE = 1.334 + 0.637 + 1.02 + 0.594 + 1.049 = 4.634.`
- Demo: `In order to get the kinetic energy, the mass of the object must be multiplied by the square of its velocity and divided by two. This will be demonstrated with the 2 kg cart on the frictionless track. (½·2·v²) = R₁. This should be repeated for the other 2 cart masses. Therefore, KE = 5.6 + 11.2 + 18.4 = 35.2 J.`

**S7 — Prerequisite → Procedure → Execution**
```
The [quantity] for [var(s)] [is/are] needed. For [A], this is X, 
and for [B] it is Y. [Imperative] [op 1] and then [op 2]. 
Then [worked arithmetic across cases] = [result].
```
- Original: `The total means for both dependent variables are needed. For DV1, this is 5.254…, and for DV2 it is 25.909…. Proceed to subtract the total means from each of the factor's means and then square it. Then add all of the values together. The first dependent variable's SSm = … = 5.870.`
- Demo: `The grand means for both dependent variables are needed. For time-to-finish, this is 2.348 s, and for colour intensity it is 0.656. Proceed to subtract the grand mean from each temperature's mean and then square the result. Then multiply each squared deviation by n and sum. The time-to-finish SSb = (5·(3.30−2.348)² + …) = 6.93.`

**S8 — Temporal Hinge**
```
Then the [next quantity] must be calculated, using the equation 
[formula] = [display form].
```
- Original: `Then the squares of the error must be calculated, using the equation SSE = ∑ sk²(nk − 1).`
- Demo: `Then the within-group sum of squares must be calculated, using the equation SSW = ∑ sk²(nk − 1).`

**S9 — Uncertainty Cascade**
```
[Carry-over announcing upcoming calculation]. [Instrument A] 
[noun phrase] had a margin of error of ±[value][unit]. 
[Instrument B] [noun phrase] had a margin of error of ±[value][unit]. 
[Instrument C] [noun phrase] had a margin of error of ±[value][unit].
```
- Original: `equipment utilized will be calculated. Margin of error in the mass balance: ±0.001 g. Margin of error in the 250 ml graduated cylinder: ±0.5 ml. Margin of error in the 50 ml graduated cylinder: ±0.4 ml.`
- Demo: `The tolerances of the calorimetry apparatus used will now be stated. Margin of error in the digital thermometer: ±0.1 °C. Margin of error in the 100 ml beaker: ±1.0 ml. Margin of error in the top-loading balance: ±0.01 g.`

---

### Express-Idea Vocabulary

| Phrase | Job |
|---|---|
| "whereas the inverse will…" | Contrast / flip condition |
| "give rise to" | Cause / consequence |
| "Like [X], [Y] can…" | Specification / equivalence |
| "can act as a substitute for" | Functional equivalence |
| "can react alongside" | Mechanism interaction |
| "It also…" | Stacking / addition |
| "The variable that is being adjusted and tested is" | IV definition formula |
| "from [anatomical landmark]" | DV measurement protocol |
| "The first/next/final step is [gerund]" | Announces next operation |
| "Now the value for…" | Plug-back signal |
| "Taking/Using the data of [subset]" | Selects single column |
| "where [symbol] represents [def]" | Symbol glossary |
| "Squaring both sides… simplifies" / "Square rooting both sides means that" | Names algebraic move |
| "Completing all operations…, the fraction becomes" | Condenses expansion |
| "This means that…" | Translates abstract → percentage/threshold/bound |
| "The same steps can be repeated" / "These steps can be repeated with the second…" | Sequencing / scaling |
| "Proceed to … and then …" | Imperative operation chain |
| "Therefore, [STAT] = r₁ + … = T" | Aggregation verdict |
| "In order to get X, the Y must be [verb-ed]…" | Rule statement |
| "This should be repeated for the other [N−1]…" | Replication sweep |
| "compared to those in the [bracket] groups" | Contrast / dose-band |
| "showed signs of" / "appeared to" / "showing" | Hedged observation |
| "must be calculated, using the equation" | Formula hinge |
| "had a margin of error of ±[value][unit]" | Uncertainty stamp |

**Evidence handling:** Raw numbers act as evidence, introduced by `=`, closed by rounded verdict (e.g. "= 187.1137149"). No explicit connectives — **positional logic carries the flow** in computational paragraphs.

---

### Replication Steps (dependency-chain model)

**For a new formula's paragraph:**
1. Label section with single capitalised phrase.
2. State claim in one sentence (what feature is quantified).
3. Display headline formula; define every symbol in "where…" clause.
4. Select data subset for worked example.
5. Signpost stages: "The first step is…", "The next step is…".
6. Restate formula with one new number substituted per stage.
7. Expand every term individually before collapsing; announce collapse with "Completing all operations…".
8. Name intermediate result by technical term (variance, etc.).
9. Name inverse operation ("Square rooting both sides means that…") to recover base quantity.
10. Plug recovered quantity into headline formula; give final number.
11. Interpret with "This means that…" converting to percentage, threshold, or bound.

**For a subsequent calculation in the same paragraph chain:**
1. State verbal rule: "In order to get X, the Y must be Z-ed… and added together."
2. Name the demonstration case.
3. Lay out full algebra for that case.
4. Extend: "This should be repeated for the other [N−1]…"
5. Aggregate: "Therefore, [STAT] = r₁ + … = T."
6. Hinge to next formula with "Then… using the equation…".

**Rule:** Each step unlocks the next via dependency chain; no computation appears before its prerequisites are shown. Positional logic, not connectives, signals flow in computational paragraphs.

Background & Definitions

Background & Definitions

### Core Express-Idea Vocabulary (compact groups)

| Connective / phrase | Job in the paragraph |
|---|---|
| "The next element that is needed is the…" | Flag the upcoming ingredient so the reader knows a new sub-formula is being introduced. |
| "X is … = ∑(…)" (one-line symbolic equality) | Define the new term and lock its abbreviation in one breath. |
| "Each/Every … must have … subtracted/multiplied from it, and then …" | Give the operational rule in passive voice, telling the reader which value acts on which. |
| "The process should be repeated for all …" | Close with a scope sentence extending the rule across every group, point, or trial. |

These four jobs recur together whenever an IB 6/7 student transitions from one computational ingredient to the next inside a methods section.

---

### Skeleton B — Flag the next ingredient, define it, give the procedure, scope it

Use this skeleton immediately after finishing one sub-formula, when the next term required for the working must be introduced before the calculation can continue. This is the most common "ingredient hand-off" pattern in IB Chemistry / Biology / Maths IA methods paragraphs.

**Structure (4 slots, in order):**

- **Slot 1 (flag):** "The next element that is needed is the …" — present tense, declarative, names the new ingredient.
- **Slot 2 (definition):** one-line symbolic equality introducing the abbreviation, e.g. "The X is X = ∑(…)."
- **Slot 3 (operational rule):** one sentence in passive voice telling the reader which value must be subtracted from which (or multiplied with which), and in what order.
- **Slot 4 (scope):** short instruction to extend the rule across all groups / data points / trials.

**Fill instructions:**
1. After closing the prior sub-formula, name the next term the working requires.
2. Give its abbreviation and summation (or product) form in a single equality.
3. Write one procedural sentence in passive voice specifying the order of subtraction/multiplication.
4. Close with a scope sentence that tells the reader to repeat the operation across every relevant unit.

**Original fill (cross-product of error in a MANOVA-style working):**
> "The next element that is needed is the cross product of the error. The cross product of the error is CPE = ∑(xi − x̄DV1)(xi − x̄DV2). The first data points for the two dependent variables must have the group means subtracted from them and then multiplied. The process should be repeated for all data points and groups."

**Demo fill (different idea — residual sum of squares for a calibration curve):**
> "The next element that is needed is the residual sum of squares. The residual sum of squares is RSS = ∑(yi − ŷi)². Each measured absorbance must have its predicted absorbance from the regression line subtracted from it, and the result squared. The process should be repeated for all standard concentrations."

The skeleton transfers unchanged across subjects because the four jobs (flag → define → operate → scope) are the same: introduce the next term, anchor it symbolically, tell the reader what to do with each datum, then close the loop.

Methods & Procedures

# Methods & Procedures

## Section Type Tag
Append `[method]`, `[data]`, or `[analysis]` to the section heading to signal the type of content (procedural, raw results, or interpretive).

## Logic‑Flow Patterns

### Flow A – Mechanism → Comparator → Transition
1. **Context‑anchor** – carry‑over from the preceding paragraph.  
2. **Inverse contrast** – “whereas the inverse …” flips the condition.  
3. **Claim + source tag** – introduces the substitute as a new actor.

### Flow B – Property → Mechanism → Implication
1. **Physical property** – raises a handling question.  
2. **Definition + source** – specifies the category.  
3. **Source‑of‑occurrence** – bridges back to the mechanism.  
4. **Functional parallel** – mirrors an earlier pairing.  
5. **Added benefit** – stacks a second effect.

### Flow C – Hypothesis → Variables
1. **Predictive claim** – declares IV/DV relationship.  
2. **IV defined by role**.  
3. **DV defined by measurement + anatomical landmark**.

### Uncertainty Calculation Pattern
**Moves:** catalogue of instrument tolerances → per‑instrument % uncertainty (procedure + calculation, with justification when needed) → sum of uncertainties → final maximum %‑uncertainty verdict.

---

## Paragraph Skeletons (Slot Templates)

### Skeleton A – Finish Prior Mechanism + Name Substitute
```
After [prior mechanism] (see previous paragraph), we introduced [substitute] as a [role] in the [process].
```
**Fill instructions**  
- `[prior mechanism]`: concise summary of the mechanism finished in the preceding paragraph.  
- `[substitute]`: name of the new variable, reagent, or component.  
- `[role]`: functional role (e.g., oxidant, catalyst, buffer).  
- `[process]`: name of the reaction or step where the substitute is used.  

**Original:** “After the reduction of Cu²⁺ by Zn, we introduced CuCl₂ as a source of Cu²⁺ ions in the precipitation step.”  
**Demo:** “After the enzyme cleaved the peptide bond, we introduced trypsin as a proteolytic catalyst in the hydrolysis reaction.”

---

### Skeleton B – Single‑Instrument % Uncertainty
```
The [instrument] used to [measure/adjust] the [quantity] had a margin of error of ±[absolute tolerance][unit]. 
Given the measured value of [value][unit], the percentage uncertainty was calculated as (absolute tolerance / measured value) × 100 = [percentage] %.
```
**Fill instructions**  
- `[instrument]`: name of the measuring device.  
- `[measure/adjust]`: verb describing the action (e.g., weigh, measure).  
- `[quantity]`: variable being measured (e.g., mass of NiCl₂).  
- `[absolute tolerance][unit]`: instrument’s tolerance (e.g., ±0.001 g).  
- `[value][unit]`: actual measured value used in the calculation.  
- `[percentage]`: result to two decimal places.  

**Original:** “The mass balance used to weigh the NiCl₂ had a margin of error of ±0.001 g. Given the measured mass of 0.030 g, the percentage uncertainty was calculated as 0.001 / 0.030 × 100 = 3.33 %.”  
**Demo:** “The 250 ml graduated cylinder used to measure the solution volume had a margin of error of ±0.5 ml. Given the measured volume of 250 ml, the percentage uncertainty was calculated as 0.5 / 250 × 100 = 0.20 %.”

---

### Skeleton C – Multi‑Instrument Uncertainty (repeat Skeleton B for each instrument, then aggregate)
*Use Skeleton B for every instrument, then follow with Skeleton D.*

---

### Skeleton D – Aggregation and Maximum
```
Adding together all the uncertainties, we get the maximum percentage uncertainty (%) of [sum] %.
```
**Fill instructions**  
- `[sum]`: sum of % uncertainties from all instruments, quoted to 2 dp.  

**Original:** “Adding together all the uncertainties, we get the maximum percentage uncertainty (%) of 5.12 %.”  
**Demo:** “Adding together all the uncertainties, we get the maximum percentage uncertainty (%) of 2.45 %.”

---

### Skeleton E – Property → Mechanism → Implication
```
[Physical property] of [system] raises the question of [handling]. 
[Definition] (source) categorises [entity] as a [category]. 
[Source‑of‑occurrence] links this property back to the [mechanism]. 
[Functional parallel] mirrors the earlier [pairing], while [added benefit] provides an additional effect.
```
**Fill instructions**  
- `[Physical property]`: observed property (e.g., low solubility).  
- `[system]`: material or solution described.  
- `[handling]`: procedural challenge posed by the property.  
- `[Definition] (source)`: formal definition with citation.  
- `[entity]`: component being defined.  
- `[category]`: class or type (e.g., hydrophobic polymer).  
- `[Source‑of‑occurrence]`: origin of the property (e.g., manufacturer data).  
- `[mechanism]`: process under discussion.  
- `[Functional parallel]`: analogous function in another component.  
- `[pairing]`: earlier pairing being mirrored.  
- `[added benefit]`: secondary advantage.  

**Original:** “The low solubility of polyvinyl alcohol in organic solvents raises the question of how it can be dispersed in the reaction mixture. The manufacturer’s datasheet defines it as a water‑soluble polymer (source), categorising it as a hydrophilic matrix. This solubility data links the polymer’s behaviour back to the emulsion polymerisation mechanism. The hydrophilic nature mirrors the earlier pairing of the surfactant, while the film‑forming ability provides an additional benefit of improved adhesion.”  
**Demo:** “The high viscosity of the glycerol solution poses a mixing challenge. The standard reference defines glycerol as a viscous polyol (source), classifying it as a humectant. This viscosity data ties back to the heat‑transfer mechanism. The high viscosity parallels the earlier use of PEG, while the moisture‑retaining property offers an extra advantage.”

---

### Skeleton F – Hypothesis → Variables
```
We hypothesised that [IV] would [direction] [DV] as measured by [measurement] at [anatomical landmark].
```
**Fill instructions**  
- `[IV]`: independent variable.  
- `[direction]`: expected effect (increase/decrease).  
- `[DV]`: dependent variable.  
- `[measurement]`: method of measurement.  
- `[anatomical landmark]`: location or time point of measurement.  

**Original:** “We hypothesised that increasing the concentration of HCl would decrease the rate of CO₂ release as measured by gas chromatography at the outlet valve.”  
**Demo:** “We hypothesised that lowering the temperature would increase the viscosity of the solution as measured by rotational viscometry at the mid‑stream point.”

---

## Express‑Idea Vocabulary (Connective + Job)

| Connective / Phrase | Job |
|---------------------|-----|
| “the percentage uncertainty for the same would be the following:” | Primes a calculation |
| “Substituting … into the same we get the following:” | Echoes formula, primes calculation |
| “The [instrument] used to [measure/adjust] the [quantity]” | Assigns instrument to variable |
| “Margin of error in the [instrument]: ±[value][unit]” | Catalogs instrument tolerance |
| “[margin] / [value] × 100 = [result] %” | Displays uncertainty calculation |
| “The smaller the measured value, the higher the uncertainty.” | States conservative‑value rule |
| “Adding together all the uncertainties, we get” | Announces aggregation |
| “After [prior mechanism] … we introduced [substitute] as a [role]” | Finishes mechanism & names substitute |
| “Whereas the inverse …” | Provides inverse contrast |
| “We hypothesised that …” | Introduces hypothesis |
| “Given the measured value of …” | Introduces measured value for calculation |
| “The [property] of [system] raises the question of …” | Opens property‑mechanism paragraph |
| “[Definition] (source) categorises [entity] as a [category]” | Provides definition & classification |
| “[Functional parallel] mirrors the earlier [pairing]” | Draws parallel |
| “[Added benefit] provides an additional effect” | Adds secondary advantage |

---

## Explanation Pattern – Maximum % Uncertainty (Step‑by‑Step)

1. **Announce** the calculation with a carry‑over line (e.g., “The tolerances of the apparatus used will now be calculated.”).  
2. **Catalogue** every instrument’s absolute margin of error in one block using the pattern “[Apparatus]: ±[number][unit]”.  
3. **Procedure sentence** for each instrument: past‑tense, naming quantity, sample, and instrument.  
4. **Justify value** (if needed) with a rule sentence: “The smaller the measured value, the higher the uncertainty.”  
5. **Show substitution** as “margin / value × 100 = result %”, using the margin from step 2 and the chosen measured value; give result to 2 dp.  
6. **Repeat** steps 3‑5 for every instrument in procedural order.  
7. **Aggregate** with one sentence: “Adding together all the uncertainties, we get the maximum percentage uncertainty (%) of [sum] %.”

---

*All skeletons are to be filled verbatim; only the bracketed placeholders may be replaced. The vocabulary list is a quick reference for linking ideas and performing calculations.*

Data, Calculations & Results

Data, Calculations & Results

## Paragraph Logic-Flow: Raw Data Description

1. Categorise data type first (qualitative vs quantitative) — tells reader what evidence to expect.
2. Open with header label naming data type ("Qualitative Data:" / "Quantitative Data:") — noun phrase + colon.
3. Lead with independent variable's most obvious sensory property (colour, smell, texture) — gives concrete anchor for cause.
4. Report earliest positive sign in control and lowest‑treatment group, naming exact day — anchors time‑point 1.
5. Report sustained positive outcome in control at later time point — anchors normal trajectory.
6. Group observations by growth stage (germination → steady growth → morphological irregularities → uptake) — follows biological timeline.
7. Report deviation in highest one or two treatment groups, using phrase "compared to those in the [control] groups" for explicit contrast.
8. Close with visible physical link between IV and subjects — something reader can see — naming the day. Supplies mechanism retroactively.
9. Switch to quantitative block with same two‑word header style, and caption table first, naming dependent variable and trial denominator, before any numbers appear.

## Skeleton A: Qualitative Observations List (Bulleted)

- Slot 1 (header): "Qualitative Data:" — noun phrase + colon.
- Slot 2 (IV physical property): one observation about what IV looked/smelt/tasted/felt like, present‑perfect or past, ending period.
- Slot 3 (early/low‑concentration result): observation about control or low group at early time point, naming day.
- Slot 4 (sustained control result): observation about same control at later time point, past tense, steady continuation.
- Slot 5 (high‑concentration deviation): observation about high group showing morphological/behavioural difference, past tense, "compared to those in the [control] groups".
- Slot 6 (mechanism observation): observation linking high group to IV's visible property, past tense, naming day.

*Fill instructions (slot‑by‑slot)*:
- Slot 1: keep header exact.
- Slot 2: state most obvious IV property ("The [IV] with higher [concentration] had a [sensory description]").
- Slot 3: name control and lowest‑treatment groups; early positive sign on specific day.
- Slot 4: same control; steady process "by the end of the [time unit]".
- Slot 5: name highest two treatment groups; describe irregularity linked with "compared to those in the [control] groups".
- Slot 6: state treated subjects took on IV's sensory property by specific day.

*Original filled version*: as quoted in Chunk 2 Paragraph 1 (adapted to 6 slots).

*Demo fill (different idea — copper sulphate qualitative)*: "The solutions with a higher concentration of copper (II) sulphate had a faint turquoise tint. The leaf surfaces of plants in the 0 and 10 mg/L solutions showing signs of new bud formation as soon as the third day. The plants in the 0 mg/L solution were already showing steady leaf expansion by the end of the fortnight. The leaves of the plants in the 40 and 60 mg/L groups showed minor curling at the margins compared to those in the 0 mg/L groups. The plants in the higher concentration groups appeared to take on the turquoise tint of the copper (II) sulphate solutions by day 6."

## Skeleton B: Quantitative Data Header with Table Caption

- Slot 1 (header): "Quantitative Data:" — noun phrase + colon.
- Slot 2 (table label + description): "Data Table [n]: [a raw data table containing the dependent variable] in each trial" — numbered caption, defines what reader will count.

*Fill instructions*:
- Slot 1: verbatim.
- Slot 2: number table sequentially; name dependent variable; specify "in each trial"; optionally include denominator in parentheses (e.g., "/20").

*Original filled version*: "Data Table 1: A raw data table containing the number of seeds germinated in each trial".

*Demo fill*: "Data Table 1: A raw data table containing the mass of precipitate (g) formed in each trial".

## Express‑Idea Vocabulary

- **Connective**: "compared to those in the [control] groups" — explicit contrast phrase for deviation reporting.
- **Job**: sensory‑property lead — open with IV's visible trait before any biological result.
- **Job**: day‑anchor — name exact day when reporting any time‑point observation.
- **Job**: caption‑first — label table before presenting numbers; name DV and trial denominator.

Analysis & Explanation of Ideas

Analysis & Explanation of Ideas

### Paragraph Logic-Flow: Calculation Bridge
1. Close prior sum inline ending with = rounded value.  
2. Box result under symbolic label: **[Symbol] = ∑ [components] = [same value]**.  
3. Flag next ingredient: *"The next [element] that is needed is…"*  
4. Define new ingredient symbolically: **[Abbreviation] = ∑ [formula]** (parallel visual rhythm to step 2).  
5. State operational rule in one passive-voice sentence: tell exactly which raw values to subtract from which means and what to do (e.g. *"must have X subtracted from them and then multiplied"*).  
6. Generalize across dataset: *"repeated for all data points and groups"* — demonstration is not the whole procedure.  
7. Demonstrate 1–2 substitutions in bracket notation with *"…"*, close with = rounded verdict.  
8. Stop; do not explain next use.

---

### Skeleton A — Carry the prior line into a closed symbolic verdict
| Slot | Role | Fill Instruction |
|------|------|------------------|
| 1 | continued arithmetic | Inline products/sums, no prose. |
| 2 | boxed value | Single rounded number closing slot 1. |
| 3 | symbolic label | 2–4 letter capital abbreviation = the formula just computed. |
| 4 | general formula | Summation notation referencing slot 1 components. |
| 5 | final value | Same number as slot 2, repeated after second =. |

**Fill instructions**: Write last un‑named sub‑calculation as inline expression; round to value; introduce 2–4 letter symbol; restate as summation; repeat value after second =.  
**Original fill**: `added together. … CPm = ∑ nk(xgroup DV1−xDV1)(xgroup DV2−xDV2) = 187.1137149`  
**Demo fill (titration equivalence‑point check)**: `summed together. 0.5(8.4 − 7.2)(12.1 − 10.8) + 0.5(7.9 − 7.2)(11.6 − 10.8) + … = 3.42. SE = ∑ wk(Vi − V̄acid)(Ti − T̄acid) = 3.42`

---

### Skeleton C — Demonstrate one substitution and close with a boxed number
| Slot | Role | Fill Instruction |
|------|------|------------------|
| 1 | first bracketed pair | `(raw1 − mean1)(raw2 − mean2)` |
| 2 | continuation | Same structure repeated, joined by `+`. |
| 3 | verdict | `= rounded number` |

**Fill instructions**: Take defined formula from Skeleton B; pick first 2–4 raw data rows; for each, write `(raw − mean of var1)(raw − mean of var2)`; join with plus signs; use `…` if not writing all terms; close with rounded total.  
**Original fill**: `(4.1−4.82857143)(25.3−27.942857142857) + (4.4−4.82857143)(25.6−27.942857142857) + … = 17.32775511`  
**Demo fill (RSS demonstration)**: `(0.182−0.174)(0.41−0.39) + (0.176−0.174)(0.38−0.39) + (0.169−0.174)(0.36−0.39) + … = 0.00174`

---

### Express-Idea Vocabulary (connective + job)
- **Inline closure**: `… = [value].` — finishes arithmetic without prose.  
- **Symbolic boxing**: `[SYM] = ∑ [parts] = [value].` — names and freezes result.  
- **Forward flag**: `The next [X] that is needed is…` — signals new ingredient.  
- **Parallel definition**: `[ABBR] = ∑ [formula]` — mirrors boxing rhythm.  
- **Passive rule**: `[raw] must have [mean] subtracted from them and then multiplied` — operational, no agency.  
- **Scope line**: `repeated for all data points and groups` — generalizes without enumerating.  
- **Bracket demo**: `(a−ā)(b−b̄) + (c−c̄)(d−d̄) + … = [total]` — shows substitution pattern, not full expansion.  
- **Hard stop**: *No forward reference* — next section picks up the boxed symbol.
