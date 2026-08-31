# Idea Flow Notes: geography_7_may2021_VVsA09PptbIuZ5Kb — Appendices

## Paragraph Flow (move by move)

**Paragraph 1: Appendix 1 – Raw Data Table**
1. [Header/claim] "Appendix 1: Raw Data Table" — names the appendix and claims the space for presenting unprocessed field measurements; hands the reader the foundational dataset every later appendix depends on.
2. [Evidence/table] The 12-row table records site, coordinates, distance downstream, species WQS, dissolved oxygen score, riparian score, nitrate, and phosphate per location — supplies the complete empirical basis that all subsequent calculations reference.

**Paragraph 2: Appendix 2 – Unweighted Composite Index**
1. [Header/claim] "Appendix 2: Unweighted Composite Index Calculations" — signals the first synthesis move, combining individual water-quality parameters into a single score without differential weighting; sets up the simpler synthesis before the weighted version follows.
2. [Context/blank] The page provides calculation space for the unweighted index — establishes the baseline composite method that Appendix 3 then modifies with weights.

**Paragraph 3: Appendix 3 – Weighted Composite Index**
1. [Header/claim] "Appendix 3: Weighted Composite Index Calculations" — names the进阶 synthesis step where parameters carry different importance; contrasts directly with Appendix 2's unweighted approach.
2. [Context/blank] The page provides calculation space for the weighted index — delivers the refined composite that the correlation appendices test against distance downstream.

**Paragraph 4: Appendix 4 – PMCC Calculations**
1. [Header/claim] "Appendix 4: PMCC Calculations (WQS and distance downstream)" — names the parametric correlation test between water quality scores and distance; claims the section as the first formal significance test.
2. [Definition] "PMCC Formula" followed by the formula and "Where: n is the sample size; x̄ and ȳ are the x and y component of the data point; mean(x) and mean(y) are the mean of x components and mean of y components of the data set respectively." — defines each variable so the reader can verify the calculation.
3. [Evidence/citation] "Pearson Correlation Coefficient - Magoosh Statistics Blog." 9 Apr. 2018, https://magoosh.com/statistics/pearson-correlation-coefficient/. Accessed: 3 Jan. 2021." — cites the formula source to establish methodological authority.
4. [Evidence/table] The Table of Critical Values (PMCC) with "degrees of freedom = n - 2" — provides the threshold against which the calculated value is judged.
5. [Verdict] "The critical value for PMCC at α = 0.01 for r = 12 is 0.708. Since 0.90 > 0.708, the result is statistically significant." — compares the calculated PMCC (0.90) against the critical value (0.708) and concludes significance; hands the reader the confirmed linear relationship that the next appendix tests with a different method.

**Paragraph 5: Appendix 5 – SRCC Calculations**
1. [Header/claim] "Appendix 5: SRCC Calculations (Species WQS and Dissolved Oxygen Levels)" — names the non-parametric correlation test between species WQS and dissolved oxygen; positions this as a complementary test to the PMCC in Appendix 4.
2. [Definition] "SRCC Formula" followed by the formula and "Where: dᵢ is the difference in rank of the data point; n is the number of pairs in a sample" — defines the rank-difference variable and sample-pair count for the Spearman test.
3. [Evidence/citation] "Spearman's Rank Correlation Coefficient." 1 Sept. 2020, https://geographyfieldwork.com/SpearmansRank.htm. Accessed: 3 Jan. 2021." — cites the rank-correlation source to establish methodological authority for the alternative test.
4. [Evidence/table] The Table of Critical Values (SRCC) — provides the rank-correlation threshold for significance judgment.
5. [Verdict] "SRCC showed a statistically significant result: rₛ(10) = 0.64, p < 0.05. Since the probability of obtaining this result by chance is less than 0.05, the result is statistically significant." — states the SRCC value (0.64) and p-value (< 0.05), confirms significance through a probability-threshold mechanism; closes the section by independently verifying the relationship PMCC already established.

---

## What This Section Does (content sequence)

1. **Raw data presentation (Appendix 1)** — lists all measured variables across 12 sites; establishes the empirical foundation every subsequent calculation draws from.
2. **Unweighted composite index (Appendix 2)** — combines individual parameters into one score with equal importance; creates the simpler synthesis baseline.
3. **Weighted composite index (Appendix 3)** — re-combines the same parameters with differential weighting; refines the composite score that the correlation tests evaluate.
4. **Parametric correlation test (Appendix 4)** — applies PMCC to test the linear relationship between WQS and distance downstream; provides the first formal significance verdict using a calculated statistic compared to a critical value.
5. **Non-parametric correlation test (Appendix 5)** — applies SRCC to test the monotonic relationship between species WQS and dissolved oxygen; independently verifies the finding using a rank-based method with a different null-hypothesis rejection mechanism.

**Why this order:** Each move builds on the previous one — raw data feeds the composite indices, the composite indices supply the variables for correlation, and the parametric test precedes the non-parametric test as a stricter-to-looser methodological progression. A student replicating this sequence would present: (1) collected measurements, (2) a simple combined score, (3) a refined combined score, (4) a parametric relationship test, and (5) a non-parametric relationship test — each step supplying the variables or justification the next requires.

---

## Paragraph Skeletons (replicable templates)

**SKELETON 1: Statistical test presentation**
"[Test name] Formula [number]: [formula expression]. Where: [variable₁] is the [definition]; [variable₂] is the [definition]; n is the [sample description]."

1. **Slot holdings:** Slot 1 = test name (noun phrase); Slot 2 = formula number (integer); Slot 3 = formula expression (mathematical notation); Slot 4 = variable name (symbol); Slot 5 = its definition (noun phrase); Slot 6 = sample description (noun phrase).
2. **How to fill differently:** Slot 1: pick any statistical test you applied (e.g., "Chi-squared"); Slot 3: write the actual formula you used; Slot 4–5: define each symbol in your formula; Slot 6: state what your sample count represents.
3. **Original filled:** "PMCC Formula: [formula]. Where: n is the sample size; x̄ and ȳ are the x and y component of the data point; mean(x) and mean(y) are the mean of x components and mean of y components of the data set respectively."
4. **Different fill:** "Chi-squared Formula: χ² = Σ(O − E)²/E. Where: O is the observed frequency in each category; E is the expected frequency under the null hypothesis; n is the total number of observations across all categories."

**SKELETON 2: Significance verdict**
"The critical value for [test] at [significance level] for [degrees of freedom] is [value]. Since [calculated statistic] > [critical value], the result is statistically significant."

1. **Slot holdings:** Slot 1 = test name; Slot 2 = significance level (Greek letter expression); Slot 3 = degrees of freedom expression; Slot 4 = critical value (number); Slot 5 = calculated statistic (number); Slot 6 = same or different critical value (number).
2. **How to fill differently:** Slot 1: name your test; Slot 2: state your chosen significance level (e.g., α = 0.05); Slot 3: write the degrees-of-freedom formula you used; Slot 4–5: insert your table-critical and calculated values; Slot 6: repeat the critical value from the table.
3. **Original filled:** "The critical value for PMCC at α = 0.01 for r = 12 is 0.708. Since 0.90 > 0.708, the result is statistically significant."
4. **Different fill:** "The critical value for Chi-squared at α = 0.05 for df = 3 is 7.815. Since 12.4 > 7.815, the result is statistically significant."

**SKELETON 3: Non-parametric significance verdict**
"[Test abbreviation] showed a statistically significant result: [statistic]([df]) = [value], p < [level]. Since the probability of obtaining this result by chance is less than [level], the result is statistically significant."

1. **Slot holdings:** Slot 1 = test abbreviation (noun); Slot 2 = statistic symbol (symbol); Slot 3 = degrees of freedom (number); Slot 4 = calculated statistic value (number); Slot 5 = significance level (number).
2. **How to fill differently:** Slot 1: use your non-parametric test's abbreviation; Slot 2–4: insert your test statistic, its degrees of freedom, and its value; Slot 5: state your p-value threshold.
3. **Original filled:** "SRCC showed a statistically significant result: rₛ(10) = 0.64, p < 0.05. Since the probability of obtaining this result by chance is less than 0.05, the result is statistically significant."
4. **Different fill:** "Chi-squared showed a statistically significant result: χ²(2) = 15.3, p < 0.001. Since the probability of obtaining this result by chance is less than 0.001, the result is statistically significant."

---

## Express-Idea Vocabulary

**Cause/consequence:**
- "Since 0.90 > 0.708, the result is statistically significant." — "Since" introduces the comparison that produces the significance verdict.
- "Since the probability of obtaining this result by chance is less than 0.05, the result is statistically significant." — "Since" introduces the probability threshold that produces the significance verdict.

**Definition:**
- "n is the sample size" — "is" assigns the definition of the sample-size variable.
- "dᵢ is the difference in rank of the data point" — "is" assigns the definition of the rank-difference variable.
- "mean(x) and mean(y) are the mean of x components and mean of y components of the data set respectively" — "are" assigns the definitions of the mean variables.

**Evidence handling:**
- "Pearson Correlation Coefficient - Magoosh Statistics Blog." 9 Apr. 2018, https://magoosh.com/statistics/pearson-correlation-coefficient/. Accessed: 3 Jan. 2021." — citation phrase establishes formula authority.
- "Spearman's Rank Correlation Coefficient." 1 Sept. 2020, https://geographyfieldwork.com/SpearmansRank.htm. Accessed: 3 Jan. 2021." — citation phrase establishes rank-correlation authority.

---

## How to Explain an Idea (replication steps)

**Pattern:** Formula → variable definition → source citation → critical-value table → significance verdict (comparison of calculated vs. critical value, or p-value vs. threshold).

1. **State the test name and display the formula** — write the test's full name, its abbreviation, and the mathematical formula you applied.
2. **Define every symbol in the formula** — list each variable with a one-line definition of what it represents in your investigation; include n and any derived quantities (means, differences, degrees of freedom).
3. **Cite the formula's source** — provide author, title, date, URL, and access date so the reader can verify the formula's correctness.
4. **Present the critical-values table** — include the table showing critical values for your chosen significance levels and degrees of freedom; state how degrees of freedom are calculated in your test.
5. **State the calculated statistic and compare it to the critical value** — report your actual calculated value, identify the corresponding critical value from the table, and use "Since [calculated] > [critical], the result is statistically significant" to deliver the verdict.
6. **Alternatively, report the p-value** — state the test statistic with its degrees of freedom and p-value, then use "Since the probability of obtaining this result by chance is less than [α], the result is statistically significant" to deliver the verdict.
