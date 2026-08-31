# Idea Flow Notes: physics_6_may2020_lP9oEIfrx2GJWXJw — Oscillation                              Time in Gate (t)/s

## Paragraph Flow (move by move)

**1. (b. Processed Data — opening prose)**
- S1 (method statement): *"Using equation (11), values of 𝑥N were calculated for all values of N."* — names the equation and the operation performed. Hands to S2 by *justifying the precision* of that calculation (why it was done this way).
- S2 (significance-figures justification): *"3 significant figures are used due to the multiplication of d and √𝑙 involved"* — explains the *cause* (precision of inputs) that dictates the output precision. Hands to S3 by *specifying which input values* were used.
- S3 (input selection): *"Average values of t are used in processing."* — declares the chosen input (the mean). Hands to the equation display by *preparing the reader for the substitution*.

**2. Equation display** — *x_N = 0.0248 × √(0.739) × 1/(9.81 t²) = 0.00681/t²  m*. Operationalises S3's "average t" into a usable expression; hands to Table 3 by *showing the result column* this formula populates.

**3. Table 3 caption** — *"Processing of t to 𝒙𝟎"*. Hands to §c by *completing the conversion step* so the next concern (uncertainty) can begin.

**4. (c. Propagation of Uncertainties — independent variable)**
- S1 (exclusion statement): *"Since the independent variable is discrete, no error results there."* — defines what is *not* being analysed. Sets up §c's next sentence by *narrowing the scope to the dependent variable*.

**5. Dependent variable lead-in**
- S1 (framework invocation): *"In the case of the dependent variable, based on equation (12), fractional uncertainties are added as follows:"* — names the regime (dependent variable) and the rule (fractional addition). Hands to the equation by *promising the formula next*.

**6. Equation (14)** — *Δx_N/x_N = Δt/t + Δd/d + Δl/(2l)*. Materialises the rule. Hands to the next prose by *requiring each fractional term to be evaluated*.

**7. First-term dismissal**
- S1 (cause + verdict): *"Given that t is measured correct to 0.000001s, the values of ∆𝑡/𝑡 are on the order of 10⁻⁵, which is negligible"* — *cause* (precision of timer) → *verdict* (negligible). Frees the formula from the Δt/t term; hands to S2 by *specifying which remaining term is evaluated first*.

**8. Two worked fractional terms** — Δd/d = 0.00005/0.0248 ≈ 0.00202 and Δl/(2l) = 0.0005/0.739 ≈ 0.00077. Hands forward by *leaving Δt/t as the only unquantified term*, prompting the next paragraph to address it.

**9. Δt/t revisited — alternative method**
- S1 (re-statement of cause): *"given that t is measured correct to 0.000001s, the values of ∆𝑡/𝑡 are on the comparatively negligible order of 10⁻⁵"* — repeats the verdict to *justify abandoning* the direct method.
- S2 (method substitution): *"Instead, the method used is taking the standard deviation of values of t from all 5 trials … and finding the average"* — *contrast move* ("Instead") proposing a substitute procedure.
- S3 (lead-in): *"Hence:"* — hands to equation (15) as the *quantification* of that substitute.

**10. Equation (15)** — *Δt = Σ(Standard Deviation)/117 ≈ 0.00905*. Hands to the next line by *flagging that this Δt is still per-row dependent*.

**11. Per-row formula lead-in**
- S1 (consequence statement): *"∆𝑡/𝑡 is then dependent on each value of 𝑡ave. Hence:"* — *consequence* of S2/S3 → formula.

**12. Equation (16)** — per-row fractional uncertainty. Hands to the data table by *populating it*.

**13. Table-introduction sentence**
- S1 (delivery): *"The calculation of ∆𝑥N and ∆𝑥N/𝑥N for N = 0, 10, …, and 58.5 are below:"* — promises the reader the computed values.

**14. Table 4** — delivers the values promised.

**15. (d. Analysis)**
- S1 (pointer): *"The graph of Amplitude (𝑥N /𝑚), derived from 𝑡ave/𝑠, against Oscillation Number (N), … is shown below:"* — *transition* from numerical to graphical; the logic hand-off is *now look at the visual trend*.

## What This Section Does (content sequence)

This is a **data-processing + uncertainty + presentation** section. The ordered moves are:

1. **State the conversion rule** (name the equation, declare which inputs feed it).
2. **Justify the precision choice** (why these sig figs — usually because the inputs constrain them).
3. **Show the processed table** (apply rule → tabulate output).
4. **Eliminate independent-variable uncertainty** (one-line dismissal — frees the analysis).
5. **Invoke the uncertainty framework for the dependent variable** (name the rule, e.g. fractional addition).
6. **Display the master uncertainty equation** (the skeleton to be filled).
7. **Evaluate each term one-by-one, with cause-then-verdict sentences** (measurement precision → magnitude → conclusion of "negligible" or "keep").
8. **Substitute alternative method when a direct term is unusable** (justification → contrast "Instead" → averaged substitute → equation).
9. **Make uncertainty row-dependent** (signal that the final expression varies with each t).
10. **Deliver the final uncertainty table**.
11. **Hand off to the next medium** (graph), by *pointing* rather than re-explaining.

**Why this order**: each move *removes an open variable* before the next is introduced, so the reader never has two unresolved questions at once. The justification-before-formula pattern means the reader accepts the formula before being asked to interpret its numbers.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Precision-justification opener"**
`[Method statement referencing equation (N)]. [Number] significant figures are used due to the [operation] involved, which are of [number] significant figures [each/sourced from X]. [Chosen input type] are used in processing.`

1. *Slots*: (i) method statement + equation tag, (ii) sig-fig count, (iii) cause-clause (operation), (iv) justification of source precision, (v) one-line input-selection.
   *Grammatical shape*: declarative past/passive; clause of cause ("due to …"); short final declarative.
2. *Fill instructions* — slot (i): pick the conversion equation used and name what it produces; slot (ii): count sig figs of the *output*; slot (iii): name the arithmetic operation (multiplication, division) that propagates precision; slot (iv): state the precision of the limiting input; slot (v): state which version of each repeated measurement (mean, median, single trial) was used.
3. *Original fill*: "Using equation (11), values of x_N were calculated for all values of N. 3 significant figures are used due to the multiplication of d and √l involved, which are of 3 significant figures each. Average values of t are used in processing."
4. *Demo fill (different idea)*: "Using equation (3), values of resistance R were calculated for every trial pair. 2 significant figures are retained because the subtraction of two nearly-equal voltages dominates, and each voltage is recorded to 2 significant figures. Mean values of current are used in subsequent processing."

**SKELETON B — "Regime split: independent / dependent"**
`Since the [independent variable] is [property], no error results there.` → `[Transition phrase] the [dependent variable], based on equation (N), [rule] are [applied] as follows:`

1. *Slots*: (i) dismissal of one variable with a cause-clause ("Since … is …, no error results there"), (ii) regime switch with explicit naming of the framework, (iii) lead-in to the master equation.
   *Grammatical shape*: subordinate clause of cause + main clause with "no"; second sentence opens with "In the case of …" and ends with colon introducing display math.
2. *Fill instructions* — slot (i): identify which variable is *defined* (discrete, constant, exact count) so its uncertainty is zero; slot (ii): name the complementary variable and the rule applied (fractional addition, quadrature, etc.); slot (iii): end on a colon.
3. *Original fill*: "Since the independent variable is discrete, no error results there. In the case of the dependent variable, based on equation (12), fractional uncertainties are added as follows:"
4. *Demo fill*: "Since the distance is read from a fixed ruler marking, no error results there. In the case of the period, based on equation (4), fractional uncertainties are combined in quadrature as follows:"

**SKELETON C — "Cause → magnitude → verdict dismissal"**
`Given that [quantity] is measured correct to [precision], the values of [fractional term] are on the order of [10⁻ⁿ], which is [negligible / dominant] compared to [other source].`

1. *Slots*: (i) precision claim of the measurement, (ii) computed order-of-magnitude of the fractional term, (iii) comparative verdict against another uncertainty source.
   *Grammatical shape*: subordinate "Given that …" + main clause with quantitative order + "which is … compared to …".
2. *Fill instructions* — slot (i): name the instrument precision (e.g. 0.000001 s); slot (ii): give the order of magnitude of the ratio numerically; slot (iii): compare against the *largest* other term using "negligible" or "dominant".
3. *Original fill*: "Given that t is measured correct to 0.000001s, the values of ∆𝑡/𝑡 are on the order of 10⁻⁵, which is negligible compared to uncertainty from other measurements."
4. *Demo fill*: "Given that the voltmeter is calibrated to 0.001 V, the values of ∆V/V are on the order of 10⁻⁴, which is negligible compared to uncertainty from the ammeter's 0.01 A resolution."

**SKELETON D — "Method substitution with contrast marker"**
`In the case of [term], [repeat cause statement]. Instead, the method used is [alternative procedure], [scope qualifier]. Hence:`

1. *Slots*: (i) term name, (ii) re-statement of why direct evaluation fails, (iii) contrast marker "Instead", (iv) alternative procedure (averaging, standard deviation, calibration curve…), (v) scope qualifier ("for each N", "across all trials"), (vi) lead-in "Hence:".
   *Grammatical shape*: "In the case of …" + concessive re-statement + "Instead, …" + lead-in colon.
2. *Fill instructions* — slot (i): name the variable whose direct uncertainty cannot be used; slot (ii): restate the precision verdict briefly; slot (iii)–(iv): propose the substitute method concretely (which statistical operation, over which subset); slot (v): delimit the subset; slot (vi): colon introducing the numerical formula.
3. *Original fill*: "In the case of ∆𝑡, given that t is measured correct to 0.000001s, the values of ∆𝑡/𝑡 are on the comparatively negligible order of 10⁻⁵. Instead, the method used is taking the standard deviation of values of t from all 5 trials, for each N to 58.5, and finding the average of all these values. Hence:"
4. *Demo fill*: "In the case of Δθ, given that the angle is recorded to 0.1°, the values of Δθ/θ are on the order of 10⁻³. Instead, the method used is computing the range across the six trials at each setting and averaging those ranges. Hence:"

## Express-Idea Vocabulary

**Sequencing / structural connectives**
- *"for all values of N"* (scope of operation) — "values of 𝑥N were calculated for all values of N."
- *"for each N to 58.5"* (scope of substitution) — "taking the standard deviation … for each N to 58.5."
- *"below:"* (delivery marker) — "are below:" / "is shown below:"
- *"as follows:"* (display lead-in) — "fractional uncertainties are added as follows:"

**Cause / consequence**
- *"due to the multiplication of"* — "due to the multiplication of d and √l involved."
- *"Given that … is measured correct to"* — "Given that t is measured correct to 0.000001s."
- *"which is negligible compared to"* — "which is negligible compared to uncertainty from other measurements."
- *"Hence:"* — "Hence:" (used twice, as a single-word equation lead-in).

**Contrast / concession**
- *"Since … no error results there."* — dismissal via definition.
- *"In the case of"* — regime marker, used twice (once for dependent variable, once for Δt specifically).
- *"Instead, the method used is"* — substitution marker.

**Specification / definition**
- *"based on equation (12)"* — framework citation.
- *"the values of > are on the order of 10⁻⁵"* — magnitude specification.
- *"compared to uncertainty from other measurements"* — comparative specification.

**Evidence / handling**
- *"Average values of t are used"* — input-selection declaration.
- *"taking the standard deviation of values of t from all 5 trials"* — provenance statement for the substituted value.

**Explanation / calculation verbs**
- *"were calculated for"* — "values of 𝑥N were calculated for all values of N."
- *"are added as follows:"* — operation + display lead-in.
- *"is then dependent on"* — "∆𝑡/𝑡 is then dependent on each value of 𝑡ave."
- *"the method used is taking the standard deviation"* — methodology declaration verb.

## How to Explain an Idea (replication steps)

The pattern is **method statement → precision justification → input choice → regime split (independent vs dependent) → framework citation → term-by-term dismissal/substitution → row-dependent formula → table → graph pointer**. Replicate with a new idea as follows:

1. **Name the equation** that converts raw data into the final quantity, and state it is applied to every trial (or row).
2. **Justify the precision** of the output by pointing to the *limiting* input precision and the *operation* (multiplication, division, subtraction) that propagates it.
3. **Declare which input version** (mean, median, single) feeds the calculation.
4. **Dismiss uncertainty in the independent variable** with a one-line "Since it is [discrete/exact/constant], no error results there."
5. **Open the dependent-variable regime** with "In the case of the dependent variable, based on equation (N), [rule] are applied as follows:" and display the master uncertainty equation.
6. **For each term, write a cause-then-verdict sentence**: instrument precision → order of magnitude → "negligible / dominant compared to …".
7. **When a term must be replaced**, restate the cause, mark the substitution with "Instead," describe the substitute method (e.g. standard deviation across trials), scope it, and close with "Hence:" before the equation.
8. **Flag that the surviving term is row-dependent** ("is then dependent on each value of …") and display the per-row expression.
9. **Promise the table**: "The calculation of … for [list of values] are below:" — then deliver it.
10. **Hand off** with a single-sentence pointer to the next medium (graph, comparison, conclusion): "The graph of [y] against [x] … is shown below:" — no re-explanation, just a cue.
