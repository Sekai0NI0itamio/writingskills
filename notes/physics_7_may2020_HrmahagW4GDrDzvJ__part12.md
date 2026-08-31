# Idea Flow Notes: physics_7_may2020_HrmahagW4GDrDzvJ — Density                     Concentration

## Paragraph Flow (move by move)

**Paragraph 1 (interpretation of Table 6)**

- **S1 — Claim with evidence handle:** "Table 6 suggests that the there is a positive correlation" → opens by naming the source (Table 6) and stating the headline trend. Hands the reader to S2 by flagging the finding as **expected**, which licences a "but..." next.
- **S2 — Contrast (concession):** "however, the viscosity values between the two balls differ" → directly negates the "expected" framing in S1. Hands the reader to S3 because the writer now owes a *cause/explanation* for the unexpected gap (theoretical similarity has been violated).
- **S3 — Mechanism + authority reference:** "since we know that the true value of water's viscosity is" → supplies the *reason* the gap matters: an external reference value exists. Hands the reader to S4 because once an error is named, the only logical next move is to declare what will be done about it.
- **S4 — Implication / forward link:** "These errors will need to be taken into consideration during further analysis." → closes the paragraph by punting the resolution downstream.

**Paragraph 2 (uncertainty note + transition to worked example)**

- **S1 — Summary claim with numeric range:** "The viscosity uncertainties have been formatted to three decimal places" → characterises the precision of the data in a single sweep. Hands the reader to S2 because precision has just been justified, so the natural next move is to *show* how one uncertainty was obtained.
- **S2 — Transition to worked example:** "As for the uncertainty calculations, using the second row for the large ball:" → pivots from summary to demonstration, explicitly selecting the worked instance.

**Figure 4 caption**

- **S1 — Definition + visual inventory:** "A graph (created using Desmos) showing a linear relationship" → names what the figure is and asserts the relationship type. Hands the reader to S2 by promising that the lines themselves are colour-coded with meaning.
- **S2 — Specification of legend / what to read:** "The lines of best fit … indicated with the red line, while the blue and green lines represent" → tells the reader how to decode the visual. Hands reader off the figure (caption ends).

---

## What This Section Does (content sequence)

This is a **results + initial analysis** section. The move order is:

1. **Raw data table first** — so the reader can audit every claim that follows.
2. **Headline pattern (correlation claim)** — sets up the "expected" half of an expected/unexpected pair.
3. **Anomaly against theory (contrast)** — creates the puzzle that motivates the rest.
4. **Systematic error identification with reference value** — provides the *mechanism* explaining the anomaly and legitimises the magnitude.
5. **Forward statement ("will be taken into account…")** — explicitly defers resolution so the reader doesn't expect a fix here.
6. **Uncertainty summary in % range** — quickly characterises data quality.
7. **Worked uncertainty calculation on a chosen row** — demonstrates the method behind the % figures rather than just asserting them.
8. **Figure + caption** — visualises the headline trend from move 2 with fitted lines and uncertainty bounds.

**Replication logic:** 1 sets up 2 by giving numbers; 2 hands 3 a baseline to contradict; 3 forces 4 (you must explain the anomaly); 4 forces 5 (you must declare what you'll do); 5 makes 6 natural (if errors matter, how precise is the data?); 6 hands 7 the chance to *show* the work; 7 hands 8 a justified plot to display. The rhythm is *show → claim → contrast → explain → defer → quantify → demonstrate → visualise*.

---

## Paragraph Skeletons (replicable templates)

### SKELETON A — "Table suggests expected finding, but anomaly, caused by X, deferred to later"

`SKELETON: "[Source] suggests that there is a [trend] between [var A] and [var B] for [cases], which was expected; however, [cases] differ [metric] by [value], which was not expected, as they should, theoretically, be similar. Furthermore, there seems to be a [error type] of [magnitude] for all the values, since we know that the true value of [reference] is [number], whereas the values obtained are significantly [direction]. These [errors] will need to be taken into consideration during further analysis."`

1. **What each slot holds:**
   - Slot 1: source label + verb of evidence ("Table N suggests") — noun phrase + reporting verb.
   - Slot 2: general trend ("positive correlation") — adjective + noun phrase.
   - Slot 3: contrast pivot ("however") + comparison metric ("differ by ~X").
   - Slot 4: mechanism ("since we know that the true value…") — causal clause with authority.
   - Slot 5: forward implication ("These… will need to be taken into consideration…") — declarative with modal.
2. **How to fill with a DIFFERENT idea:** Pick a dataset with two cases (e.g., two sensors, two temperatures, two materials). Slot 1 names the table. Slot 2 states the expected trend. Slot 3 quantifies the gap between cases. Slot 4 names an external reference (textbook value, manufacturer's spec). Slot 5 promises downstream correction.
3. **Original filled version:** "Table 6 suggests that the there is a positive correlation between concentration and the viscosity of the solution for both balls, which was expected; however, the viscosity values between the two balls differ significantly by about 0.3 Pas, which was not expected, as they should, theoretically, be similar. Furthermore, there seems to be a systematic error of ~103 for all the values, since we know that the true value of water's viscosity is 0.89 mPas, whereas the values obtained are significantly higher. These errors will need to be taken into consideration during further analysis."
4. **Demonstration fill (different subject):** "Table 2 suggests that there is a positive correlation between applied voltage and current through both LEDs, which was expected; however, the LED currents differ significantly by about 4 mA at 3.0 V, which was not expected, as they should, theoretically, share the same I–V curve. Furthermore, there seems to be a systematic offset of ~0.2 V for all the values, since we know that the true forward voltage of a red LED at 20 mA is 1.95 V, whereas the values obtained are significantly higher. These offsets will need to be taken into consideration during further analysis."

### SKELETON B — "Uncertainties are low (range), so here is one worked example"

`SKELETON: "The [quantity] uncertainties have been formatted to [precision] and are relatively [adjective], ranging from [min]%–[max]%. As for the uncertainty calculations, using the [Nth] row for the [case]:"`

1. **What each slot holds:**
   - Slot 1: summary claim with precision specifier and percentage range — noun phrase + range phrase.
   - Slot 2: pivot ("As for…") + explicit selection of a worked instance (row, object) — prepositional phrase.
2. **How to fill with a DIFFERENT idea:** Pick any propagated uncertainty in your data. State the precision convention (e.g., "two significant figures"). Give a min–max percentage range across all rows. Then pivot and name one specific row + object that you will unpack.
3. **Original filled version:** "The viscosity uncertainties have been formatted to three decimal places and are relatively low, ranging from 1.0%–2.3%. As for the uncertainty calculations, using the second row for the large ball:"
4. **Demonstration fill (different subject):** "The resistance uncertainties have been formatted to two significant figures and are relatively modest, ranging from 0.8%–3.1%. As for the uncertainty calculations, using the fourth row for the nichrome wire:"

### SKELETON C — Figure caption: relationship claim → legend decode → key statistics

`SKELETON: "A graph (created using [tool]) showing a [relationship type] between [x], [symbol], and [y], [symbol], using [case A] and [case B]. The lines of best fit ([form]) are indicated with the [colour] line, while the [other colours] represent the [boundary] slopes respectively. The equations, gradients, [y]-intercepts and [r² / R²] values are given."`

1. **What each slot holds:** tool name (parenthetical) → relationship type → variables with symbols → cases → colour legend → statistic inventory. Each is a noun phrase stacking outward from the figure.
2. **How to fill with a DIFFERENT idea:** Name your software, the trend ("linear", "exponential decay"), the two variables with their symbols, your two cases, your colour scheme for best fit and bounding slopes, and the four statistics you report.
3. **Original filled version:** "A graph (created using Desmos) showing a linear relationship between salt concentration, c, and viscosity, η, using a small steel ball and a larger one. The lines of best fit (𝑦 = 𝑚𝑥 + 𝑐) are indicated with the red line, while the blue and green lines represent the maximum and minimum slopes respectively."
4. **Demonstration fill:** "A graph (created using LoggerPro) showing a logarithmic relationship between frequency, f, and reactance, X_L, using the 100 Ω and 220 Ω inductors. The curves of best fit (𝑦 = 𝑎 ln(𝑥) + 𝑏) are indicated with the red line, while the blue and green curves represent the maximum and minimum gradients respectively."

---

## Express-Idea Vocabulary

- **Sequencing / adding evidence:** "Furthermore, there seems to be a systematic error" — stacks a second, independent observation onto the first.
- **Contrast / concession:** "however, the viscosity values between the two balls differ" — flips expectation set up one clause earlier.
- **Specification of magnitude:** "differ significantly by about 0.3 Pas" — turns a vague "differ" into a defensible number.
- **Authority / external reference:** "since we know that the true value of water's viscosity is" — grounds the anomaly in a known reference.
- **Comparison (paired against reference):** "whereas the values obtained are significantly higher" — explicit side-by-side with the reference.
- **Forward implication / deferral:** "These errors will need to be taken into consideration during further analysis" — closes a paragraph by punting downstream.
- **Topic pivot / transition:** "As for the uncertainty calculations, using the second row" — switches from summary to demonstration in one move.
- **Evidence-handling verb:** "Table 6 suggests that the there is a positive correlation" — frames a data table as a soft claim ("suggests") rather than proof.
- **Numeric-range summariser:** "ranging from 1.0%–2.3%" — compresses many rows into a single bounded statement.
- **Figure caption verbs:** "showing a linear relationship between … and …, using" — one verb carries the whole relationship claim.

---

## How to Explain an Idea (replication steps)

This section uses a **"data → claim → expected-but-anomaly → mechanism with reference → deferral → quantification → demonstration → visualisation"** chain. Replicate with a NEW idea:

1. **Lay out the raw numbers first** (table or list). Without them, no later claim is auditable.
2. **State the headline pattern in one clause**, naming the source ("Table X suggests…"). Soft-modal verbs ("suggests", "appears to") let you stay honest.
3. **Flag the pattern as expected** ("which was expected") so the next move can break it.
4. **Use "however" to introduce the anomaly**, quantifying it ("differ by ~X units"). Do not let the anomaly be vague.
5. **Explain the anomaly via an external reference** ("since we know the true value is Y"), using "whereas" to set your data against the reference. This converts "unexpected" into "explainable".
6. **Defer the fix in one sentence** ("These will need to be taken into consideration…") so the reader doesn't expect a solution here.
7. **Quantify data quality in a percentage range** ("ranging from A%–B%") — one sentence, no math.
8. **Pivot to a worked calculation** ("As for the uncertainty calculations, using row N for [case]:") and unpack one instance in full so the reader sees the method.
9. **Visualise the headline claim** with a graph whose caption (i) names the tool, (ii) names the relationship, (iii) decodes the colour legend, (iv) lists the reported statistics.
