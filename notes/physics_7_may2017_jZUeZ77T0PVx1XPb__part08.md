# Idea Flow Notes: physics_7_may2017_jZUeZ77T0PVx1XPb — The final velocities which the cylinders reach at the end of the slope is calculated by averaging

## Paragraph Flow (move by move)

**Paragraph 1** — *Data source and example selection*
- **S1** (context / source anchor): "the final 10 velocity data points recorded by the velocity sensor" — opens by locating WHERE the numbers come from, so the reader knows what is about to be summed.
- **S2** (specification / parameter): "(Note that the velocity sensor records data at a frequency of 20 Hz)" — a parenthetical that specifies the sampling rate, justifying why "10 data points" has meaning; hands on by telling the reader WHICH slice of data is being treated as the worked example.
- **S3** (selection / focus marker): "The data collected when the diameter of the hole of the hollow cylinder is 0 cm is used as an example." — narrows the reader's attention to ONE trial (diameter = 0 cm), which is the prerequisite for the next paragraph's calculation.

→ Hand-off: S3 commits to "this specific trial is the example," so the next block must show the maths FOR that trial.

**Paragraph 2** — *Worked calculation for the chosen trial*
- **M1** (worked mean): `Final velocity (𝑣) = 1/10 × (1.42 + 1.55 + ⋯ + 1.29 + 1.57) = 1.47 m s⁻¹` — unpacks the averaging procedure named in the section title by applying it numerically to the 10 points from S1.
- **M2** (worked uncertainty): `∆𝑣 = 1/2 × (1.57 − 1.35) = 0.11 m s⁻¹` — applies the half-range rule to the same dataset, producing a value that pairs with the mean.

→ Hand-off: the formula has now been DEMONSTRATED once, which licenses the next sentence to say "the same procedure applies elsewhere."

**Paragraph 3** — *Generalisation, result list, aggregate*
- **S1** (generalisation / extension): "Similarly, the final velocities of Trial 2 and Trial 3 can be calculated." — uses "Similarly" to claim the procedure from P2 transfers to the remaining trials without restating it; hands on by promising three finished values.
- **S2** (result list / evidence): "In Trial 1, 𝑣 = (1.47 ± 0.11) m s⁻¹ ; In Trial 2, 𝑣 = (1.48 ± 0.10) m s⁻¹ ; In Trial 3, 𝑣 = (1.45 ± 0.12) m s⁻¹" — delivers the three (mean ± uncertainty) pairs promised, supplying the numbers required for the final aggregation.
- **M3** (worked aggregate mean): `Averaged final velocity (𝑣𝑎𝑣𝑔) = 1/3 × (1.47 + 1.48 + 1.45) = 1.47 m s⁻¹` — applies the same averaging procedure a second level up, across trials rather than within a trial.
- **M4** (worked aggregate uncertainty): `∆𝑣𝑎𝑣𝑔 = 1/2 × (1.58 − 1.33) = 0.13 m s⁻¹` — mirrors M2 at the cross-trial scale, closing the section with the final reported value.

## What This Section Does (content sequence)

1. **Locate the raw dataset** — tell the reader which measurements will be processed (e.g., "the final 10 velocity data points recorded by…").
2. **Quote the instrument parameter** — a parenthetical giving the sampling frequency or resolution, so the count of points is meaningful.
3. **Pick ONE instance to be the worked example** — name the condition (e.g., diameter = 0 cm) that the maths will be applied to.
4. **Show the worked mean for that instance** — write the formula, the substituted values, and the quoted result.
5. **Show the worked uncertainty for that instance** — apply the half-range rule to the same numbers.
6. **Generalise with a "similarly" sentence** — assert, without re-doing the maths, that the other trials are processed the same way.
7. **List the (mean ± uncertainty) results of all trials** — present them in parallel form so they can be compared and aggregated.
8. **Aggregate across trials** — average the trial means and recompute the half-range across the combined dataset.

This order works because each step creates the input the next step needs: the source enables the count, the count enables the mean, the mean enables the generalisation, the generalisation enables the list, and the list enables the final aggregate.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Source-and-example opener**
> "The final *N* [data points] recorded by [instrument] (Note that [instrument] records data at a [rate/resolution]). The data collected when [condition = value] is used as an example."

1. **What each slot holds:** slot 1 is a count + measurement kind + instrument (noun phrase); the parenthetical is a technical aside (present-tense clause); slot 2 is a conditional clause identifying which sub-dataset is exemplified (past-tense passive).
2. **How to fill it with a different idea:** slot 1 — pick a numerical subset of your raw data (e.g., "the last 15 temperature readings") and name the device that logged them; parenthetical — give the sampling frequency, bit-depth, or aperture size so the count has physical meaning; slot 2 — choose the control condition (e.g., "when the filter is absent," "at ambient pressure") that will receive the worked maths.
3. **Original fill:** "the final 10 velocity data points recorded by the velocity sensor (Note that the velocity sensor records data at a frequency of 20 Hz). The data collected when the diameter of the hole of the hollow cylinder is 0 cm is used as an example."
4. **Demo fill (different idea):** "the final 8 voltage readings taken from the multimeter (Note that the multimeter samples at 5 Hz). The data collected when the resistor is rated at 0 Ω is used as an example."

**SKELETON B — Worked-example calculation (mean + uncertainty pair)**
> *[Mean formula = 1/N × (x₁ + x₂ + ⋯ + xₙ) = value (units, 2dp)]*
> *[Uncertainty formula = 1/2 × (x_max − x_min) = value (units, 2dp)]*

1. **What each slot holds:** two equation lines, each with a label, a symbolic formula using the N from Skeleton A, the substituted numerical list, the evaluated value, units, and a precision tag.
2. **How to fill it with a different idea:** line 1 — keep the averaging structure but swap in your variable name and the N from your source opener; line 2 — apply the half-range rule using the smallest and largest of the same N values.
3. **Original fill:** `Final velocity (𝑣) = 1/10 × (1.42 + 1.55 + ⋯ + 1.29 + 1.57) = 1.47 m s⁻¹` and `∆𝑣 = 1/2 × (1.57 − 1.35) = 0.11 m s⁻¹`.
4. **Demo fill (different idea):** `Mean angle (𝜃) = 1/8 × (23.1° + 24.5° + ⋯ + 22.9° + 24.0°) = 23.8° (2dp)` and `∆𝜃 = 1/2 × (24.5° − 22.9°) = 0.8° (2dp)`.

**SKELETON C — "Similarly" generaliser + parallel result list**
> "Similarly, the [quantity] of [Trial/Run 2] and [Trial/Run 3] can be calculated. In [Trial 1], [quantity] = (mean ± uncert); In [Trial 2], [quantity] = (mean ± uncert); In [Trial 3], [quantity] = (mean ± uncert)."

1. **What each slot holds:** a one-clause "similarly" sentence (present-tense modal "can be calculated") followed by a semicolon-separated list of three (value ± value) triples in identical syntax.
2. **How to fill it with a different idea:** first sentence — name the OTHER two runs explicitly; list — copy the (mean ± uncert) format from the worked example into three parallel entries, keeping the units and dp consistent across all three.
3. **Original fill:** "Similarly, the final velocities of Trial 2 and Trial 3 can be calculated. In Trial 1, 𝑣 = (1.47 ± 0.11) m s⁻¹ ; In Trial 2, 𝑣 = (1.48 ± 0.10) m s⁻¹ ; In Trial 3, 𝑣 = (1.45 ± 0.12) m s⁻¹".
4. **Demo fill (different idea):** "Similarly, the mean angles of Trial 2 and Trial 3 can be calculated. In Trial 1, 𝜃 = (23.8 ± 0.8)° ; In Trial 2, 𝜃 = (24.1 ± 0.6)° ; In Trial 3, 𝜃 = (23.6 ± 0.9)°."

**SKELETON D — Aggregate calculation (across-trial mean + uncertainty)**
> *[Aggregate mean = 1/n × (trial₁ + trial₂ + trial₃) = value (units, 2dp)]*
> *[Aggregate uncertainty = 1/2 × (max − min) = value (units, 2dp)]*

1. **What each slot holds:** two equation lines that re-apply the Skeleton B procedure at the higher level (across trials instead of within a trial), pulling inputs from the list in Skeleton C.
2. **How to fill it with a different idea:** line 1 — average the three trial-means from your Skeleton C list; line 2 — apply the half-range to the maximum and minimum of that same three-trial list.
3. **Original fill:** `Averaged final velocity (𝑣𝑎𝑣𝑔) = 1/3 × (1.47 + 1.48 + 1.45) = 1.47 m s⁻¹` and `∆𝑣𝑎𝑣𝑔 = 1/2 × (1.58 − 1.33) = 0.13 m s⁻¹`.
4. **Demo fill (different idea):** `Averaged angle (𝜃𝑎𝑣𝑔) = 1/3 × (23.8 + 24.1 + 23.6) = 23.8° (2dp)` and `∆𝜃𝑎𝑣𝑔 = 1/2 × (24.1 − 23.6) = 0.3° (2dp)`.

## Express-Idea Vocabulary

- **Sequencing / extension:** "Similarly, the final velocities of Trial 2 and Trial 3 can be calculated." — uses "Similarly" as a license to skip the repeated maths.
- **Specification / parameter aside:** "Note that the velocity sensor records data at a frequency of 20 Hz" — parenthetical specification that fixes the meaning of "10 data points."
- **Focus / instance selection:** "The data collected when the diameter of the hole of the hollow cylinder is 0 cm is used as an example." — passive construction that flags ONE subset as the worked instance.
- **Evidence / result delivery:** "In Trial 1, 𝑣 = (1.47 ± 0.11) m s⁻¹ ; In Trial 2, 𝑣 = (1.48 ± 0.10) m s⁻¹" — parallel presentational clauses that deliver the three (mean ± uncert) results.
- **Explanation verbs (mathematical):** the section leans on symbolic-equation verbs rather than prose verbs — `averaged`, `final`, `calculated` appear as equation labels ("Averaged final velocity", "Final velocity"); prose verb `calculated` appears in "the final velocities of Trial 2 and Trial 3 can be calculated."
- **Precision tag:** "(2dp)" — appended to every final value to fix the reporting precision.

## How to Explain an Idea (replication steps)

This section runs a **worked-example → generalisation → aggregation** pattern (a two-level worked calculation). To replicate it for a NEW idea:

1. **Name the raw slice** — state the count and the instrument that produced it (e.g., "the final 10 temperature readings recorded by the thermocouple").
2. **Quote the instrument's resolution** — add a parenthetical specifying the sampling frequency or precision so the count is interpretable.
3. **Designate ONE condition as the worked example** — pick a single value of your independent variable (control or otherwise) that will carry the explicit maths.
4. **Show the within-instance mean** — write the averaging formula using the count from step 1, substitute the values, and quote the result with units and dp.
5. **Show the within-instance uncertainty** — apply the half-range rule to the same list; quote the result alongside the mean.
6. **Generalise with "Similarly"** — one sentence asserting the remaining trials follow the same procedure, without repeating it.
7. **List all trial results in parallel (mean ± uncertainty) syntax** — three identical-shaped entries separated by semicolons so they read as a unit.
8. **Compute the across-trial mean** — average the three trial-means from step 7, using 1/n where n is the number of trials.
9. **Compute the across-trial uncertainty** — apply the half-range rule to the max and min of the three trial-means, completing the section's two-level calculation.
