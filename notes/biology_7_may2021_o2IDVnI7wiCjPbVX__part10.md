# Idea Flow Notes: biology_7_may2021_o2IDVnI7wiCjPbVX — sensitive to outliers as compared to other forms of statistical testing and is not only restricted to testing

## Paragraph Flow (move by move)

**Paragraph 1**
- **S1 (conclusion from prior discussion / verdict):** "a linear correlation is unlikely to be present between the two variables." *Function:* Closes a previous line of evidence (R²-based reasoning) by delivering a verdict that linear correlation is weak/absent. *Hand-off:* The verdict establishes a *gap* — if linear correlation is unlikely, the writer needs an alternative metric that captures non-linear but monotonic relationships, which is exactly what the next paragraph introduces.

**Paragraph 2**
- **S1 (evidence / data presentation):** "Using Excel, the Spearman's correlation coefficient, rs, calculated is 0.742." *Function:* Announces the new statistical tool and its calculated value, replacing the abandoned linear approach. *Hand-off:* The bare number demands interpretation, which the next clause supplies.
- **S2 (interpretation / magnitude judgment):** "As the value is in the range of 0.500 and 0.750, it shows a moderate positive correlation between average incidence of malaria per 100,000 people and average rate of deforestation." *Function:* Translates the raw coefficient into a labelled strength (using a pre-defined magnitude band). *Hand-off:* Having established *that* a correlation exists, the writer now needs to ask *whether it is trustworthy*, prompting the transition to significance testing.
- **S3 (transition / next-step announcement):** "Furthermore, in order to determine whether this correlation is statistically significant or not, hypothesis testing will be conducted." *Function:* Bridges from magnitude to significance; signals a new analytical procedure. *Hand-off:* Names the procedure (hypothesis testing) without doing it yet, setting up the parameters that the next paragraph supplies.

**Paragraph 3**
- **S1 (procedure / parameter specification):** "The critical value rcrit for 40 data points with a degree of freedom of 38 and testing at a significance level of 5% (α=0.05) is 0.271 (University of York)." *Function:* Sets up the threshold needed for comparison — sample size, df, α, and source. *Hand-off:* Having defined *r_crit*, the writer is now ready to compare it against *r_s*, which is exactly what the next clause performs.
- **S2 (comparison / implication, sentence incomplete):** "Comparing the Spearman's correlation coefficient to the rcrit value, we find that the correlation coefficient is higher (0.742 > 0.271), which means that the null [hypothesis is rejected]." *Function:* Performs the test logic side-by-side with a numerical inequality, and the *which means* clause pre-states the consequence (rejection of H₀). *Hand-off:* The bracketed conclusion (truncated in the excerpt) would normally hand the reader into a verdict sentence — either accepting or rejecting H₀ and stating what this allows the writer to claim.

## What This Section Does (content sequence)

1. **Close the prior method's verdict** — finish a previously chosen test (here, Pearson's R²) with its negative finding, so the reader knows *why* a new test is needed.
2. **Introduce the replacement test and report its output** — name the test, give the calculated statistic in raw form.
3. **Interpret the magnitude of the statistic** — bind the number to a qualitative band (weak/moderate/strong) using a known scale, so the reader understands what the number *means in plain terms*.
4. **Announce the next analytical step (significance testing)** — because magnitude alone doesn't establish reliability.
5. **Specify the test's parameters** — sample size, degrees of freedom, α, and the source/table giving the critical value.
6. **Compare the observed statistic against the critical value** — present the inequality and pre-state its logical consequence (rejection or failure to reject H₀).

*Order rationale:* Each move sets up the next — magnitude interpretation cannot precede the statistic; significance testing cannot precede the announcement that it will happen; the comparison cannot precede the critical value. The sequence moves from **descriptive evidence → labelled interpretation → reliability test → threshold lookup → logical verdict**.

## Paragraph Skeletons (replicable templates)

### Skeleton A — "Verdict on a Prior Test"
**SKELETON:** "[Test X] showed [result], which suggests that [property Y] is [unlikely / likely / absent] between [variable A] and [variable B]."

1. **What each slot holds:** *Test X* = name of the previously applied statistical tool (noun phrase); *result* = a numeric or qualitative outcome from that tool (number + descriptor); *property Y* = the kind of relationship the test can detect (e.g., "a linear correlation", "a normal distribution"); *variable A/B* = the two variables under study.
2. **How to fill with a different idea:** Pick a test you already ran and whose result failed to support a claim. State its output, then name the specific relationship property it tested (linearity, normality, homoscedasticity), and declare it absent/present.
3. **Original fill:** "as shown by the R2 value, a linear correlation is unlikely to be present between the two variables."
4. **Demonstration fill with a different idea:** "As shown by the Shapiro–Wilk test (W = 0.912, p = 0.083), a normal distribution is unlikely to characterise the reaction-time data."

### Skeleton B — "Statistic → Magnitude Band → Direction"
**SKELETON:** "Using [software/tool], the [test statistic name], [symbol], calculated is [value]. As the value is in the range of [low] and [high], it shows a [weak/moderate/strong] [positive/negative] [relationship type] between [var A] and [var B]."

1. **What each slot holds:** *Software* = computing tool (proper noun); *test statistic name* + *symbol* = the metric and its Greek/letter symbol; *value* = the calculated number; *range low/high* = the band's endpoints; *adjective* + *direction* + *relationship type* = the interpreted label.
2. **How to fill with a different idea:** Run any correlation/association test, report the symbol and value, then look up the conventional magnitude bands (e.g., 0–0.2 very weak, 0.2–0.4 weak, etc.) and select the band your value falls into.
3. **Original fill:** "Using Excel, the Spearman's correlation coefficient, rs, calculated is 0.742. As the value is in the range of 0.500 and 0.750, it shows a moderate positive correlation between average incidence of malaria per 100,000 people and average rate of deforestation."
4. **Demonstration fill:** "Using R, Kendall's tau-b, calculated, is 0.61. As the value is in the range of 0.40 and 0.70, it shows a moderate positive monotonic association between years of teaching experience and student satisfaction ratings."

### Skeleton C — "Bridge to Significance Testing"
**SKELETON:** "Furthermore, in order to determine whether this [observed relationship] is statistically significant or not, [procedure] will be conducted."

1. **What each slot holds:** *Observed relationship* = the just-labelled correlation/association; *procedure* = the formal name of the significance test (e.g., "hypothesis testing", "a chi-squared test of independence").
2. **How to fill:** After reporting any non-significance-tested result, add a *Furthermore* connector that explicitly names the unresolved question (significance) and the procedure that will resolve it.
3. **Original fill:** "Furthermore, in order to determine whether this correlation is statistically significant or not, hypothesis testing will be conducted."
4. **Demonstration fill:** "Furthermore, in order to determine whether this difference in mean scores is statistically significant or not, an independent samples t-test will be conducted."

### Skeleton D — "Critical Value Lookup → Comparison"
**SKELETON:** "The [critical-statistic symbol] for [n] data points with a degree of freedom of [df] and testing at a significance level of [X]% (α=0.[Y]) is [value] ([source]). Comparing the [observed statistic] to the [critical-statistic symbol], we find that the [observed statistic] is [higher/lower] ([observed] >/< [critical]), which means that the null [hypothesis will be rejected / cannot be rejected]."

1. **What each slot holds:** Four setup parameters (n, df, α, source), the looked-up critical value, then a parallel comparison sentence with the inequality written out in numerals.
2. **How to fill:** Identify n, compute df (= n − 2 for correlation), state α, cite the table/source, look up the critical value, then write the inequality and pre-state its consequence with *which means*.
3. **Original fill:** "The critical value rcrit for 40 data points with a degree of freedom of 38 and testing at a significance level of 5% (α=0.05) is 0.271 (University of York). Comparing the Spearman's correlation coefficient to the rcrit value, we find that the correlation coefficient is higher (0.742 > 0.271), which means that the null [hypothesis is rejected]."
4. **Demonstration fill:** "The critical value t_crit for 48 data points with a degree of freedom of 47 and testing at a significance level of 1% (α=0.01) is 2.682 (statistics tables). Comparing the t-statistic to the t_crit value, we find that the t-statistic is higher (3.94 > 2.682), which means that the null hypothesis will be rejected."

## Express-Idea Vocabulary

- **Sequencing / transition:** *"Furthermore, in order to determine whether this correlation is statistically significant or not"* — bridges from descriptive interpretation to the significance procedure.
- **Comparison / parallel structure:** *"Comparing the Spearman's correlation coefficient to the rcrit value"* — sets up a side-by-side numerical comparison.
- **Consequence / implication:** *"which means that the null"* — pre-states the logical outcome of the comparison.
- **Specification / parameter setting:** *"for 40 data points with a degree of freedom of 38"* — pins down the exact test conditions.
- **Evidence attribution:** *"(University of York)"* — attaches a source to the critical-value table.
- **Explanation / classification verb:** *"is in the range of 0.500 and 0.750, it shows"* — categorises a numeric value into a labelled magnitude band.
- **Tool attribution:** *"Using Excel, the Spearman's correlation coefficient, rs, calculated is 0.742"* — names the computational tool before the statistic.
- **Inequality signifiers:** *"(0.742 > 0.271)"* — embeds the raw comparison in parentheses after the prose claim.
- **Cause / justification connector:** *"which is important because as shown by the R2 value"* — gives the *because*-clause reason for switching tools.

## How to Explain an Idea (replication steps)

This section uses the **"dismiss prior tool → deploy new tool → label magnitude → test significance"** pattern. To replicate it on a new idea:

1. **Close the previous method with a negative verdict.** State what the earlier test showed and declare that the relationship property it measures is unlikely/insufficient. This creates the *need* for a new tool.
2. **Introduce the replacement test.** Name the tool, the software used, and the calculated statistic with its symbol and raw value in a single sentence.
3. **Translate the raw number into a labelled magnitude.** Use a pre-defined band scale (e.g., 0–0.25 weak, 0.25–0.5 moderate, 0.5–0.75 strong) and write *As the value is in the range of X and Y, it shows a [band] [direction] [relationship]*.
4. **Bridge to significance testing.** Add *Furthermore, in order to determine whether this [relationship] is statistically significant or not, [procedure] will be conducted* — announce the next analytical step explicitly rather than launching into it.
6. **Set the test parameters.** Specify sample size, degrees of freedom, α level (with parenthetical α=0.0X), and cite the source of the critical value in parentheses.
7. **Run the comparison and pre-state the consequence.** Write *Comparing [observed] to [critical], we find that [observed] is [higher/lower] ([observed] >/< [critical]), which means that the null [hypothesis is/is not rejected]* — present the inequality in numerals inside parentheses and use *which means* to attach the verdict.

The underlying logic: every descriptive statistic is suspect until its magnitude is labelled *and* its statistical reliability is tested, so the explanation must perform all three operations in fixed order.
