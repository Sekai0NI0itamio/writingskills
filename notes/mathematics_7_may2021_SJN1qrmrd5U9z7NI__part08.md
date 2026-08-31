# Idea Flow Notes: mathematics_7_may2021_SJN1qrmrd5U9z7NI — While the r value is known, further calculations will be done to find the standard deviations for both

## Paragraph Flow (move by move)

**Paragraph 1**

1. **Move: fragment-continuation (context pickup)** — "the y and x values" — picks up from a prior page so the reader knows the target data series. Hands the reader to the next sentence by **naming the objects** that the method will now operate on.
2. **Move: purpose + method introduction** — "To find the standard deviations, the following formula was used" — states *what is being calculated* and *how* (by formula). Hands the reader forward by **pointing** ("following") so the formula is expected next.
3. **Move: scope clarification (concession/contrast pivot)** — "While the formula indicates the values used for the x data points, the same formula will be used for the y points" — concedes the formula as written is x-only, then **swaps** to y. Hands the reader forward by **mirroring** (one formula, two datasets), setting up a parallel calculation later.

**Paragraph 2 (formula + variable key)**

4. **Move: formula presentation + definition list** — the boxed equation and the four-line key ("σx= standard deviation…", "x = values…", "x̄ = mean…", "N = total number…"). The formula is given first, then each symbol is **defined in turn**. Each definition hands to the next by **same-symbol → next-symbol** order, so the reader can decode the equation symbol-by-symbol.

**Paragraph 3 (transition)**

5. **Move: forward-pointing transition** — "The working for both σx and σy are seen below" — signals a shift from *general formula* to *specific substitution*. Hands the reader forward by **pointing** ("below") to a worked demonstration.

**Paragraph 4 (worked calculation)**

6. **Move: intermediate-sum statement (evidence)**, right column triggers parallel statement for y — "∑(x − x̄)² = 2142682.233" / "∑(y − ȳ)² = 5.073". Hands the reader forward by **producing the numerator** that the next division needs.
7. **Move: divisor statement (evidence)** — "Nx = 86" / "Ny = 86". Hands forward by **supplying the denominator**.
8. **Move: substitution into formula (mechanism)** — "2142682.233 / 86" / "5.073 / 86". Hands forward by **executing the operation** that the formula requires.
10. **Move: verdict (final numeric result)** — "σx ≈ 157.845" / "σy ≈ 0.243". Hands forward (or closes) by **approximating** ("≈") — the calculation is now finished and reusable.

## What This Section Does (content sequence)

This is a **worked-calculation section**. The required order is:

1. **State the target quantity** (e.g., "to find the standard deviations"). This sets up *why* a formula is needed.
2. **Present the formula** in symbolic form. This sets up the reader to look up unfamiliar symbols.
3. **Define every symbol** in the formula. This sets up the reader to substitute numbers correctly later.
4. **Signal the working** ("seen below"). This sets up the transition from general → specific.
5. **Show the parallel worked steps** side by side: intermediate sum → divisor → fraction → final value, applied to **both** data series. This sets up the reader to **verify** the calculation by mirror reading.

Why this order: the reader cannot decode the working without the formula; cannot decode the formula without the key; cannot trust the working without the parallel repetition confirming the method was applied identically to both sets.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Method-justification paragraph"**
`[Object of calculation]. To find [quantity], [procedure] was used. While [procedure as stated] applies to [first dataset], the same [procedure] will be used for [second dataset].`

1. **Slots:**
   - Slot 1: a noun phrase naming the data series being worked on (e.g., "the y and x values").
   - Slot 2: the target quantity (noun phrase, e.g., "the standard deviations").
   - Slot 3: the named method (past tense, e.g., "the following formula").
   - Slot 4: the first dataset the formula explicitly references.
   - Slot 5: the second dataset that will use the same procedure.
2. **How to fill with a different idea:** slot 1 = state the two variables you're treating the same way; slot 2 = name the statistic or quantity being computed; slot 3 = name the formula or test in past passive ("was applied"); slots 4–5 = label your two groups (x/y, control/experimental, before/after).
3. **Original fill:** "the y and x values. To find the standard deviations, the following formula was used. While the formula indicates the values used for the x data points, the same formula will be used for the y points."
4. **Demonstration fill (different idea — t-test comparison):** "the reaction-time and accuracy scores. To find whether the difference is significant, an independent-samples t-test was used. While the formula as written treats the experimental group's data, the same test will be applied to the control group."

**SKELETON B — "Formula-plus-key block"**
`[Display formula]. [Symbol 1] = [definition]. [Symbol 2] = [definition]. [Symbol 3] = [definition]. [Symbol 4] = [definition].`

1. **Slots:**
   - Slot 0: an equation in symbolic form.
   - Slots 1–4: each symbol that appears in the equation, defined as `symbol = definition`, where the definition names the variable in plain English and (optionally) restates its context (e.g., "x = values of the x-variable in the set of data (page count)").
2. **How to fill with a different idea:** write the formula first; list every symbol in the order they appear left-to-right in the equation; for each, write `symbol = full-sentence definition that includes the variable's role in your context`.
3. **Original fill:** σ_x formula followed by σx = standard deviation…, x = values of the x-variable…, x̄ = mean of the x values, N = total number of points.
4. **Demonstration fill (different idea — chi-squared):** "χ² = Σ((O−E)²/E). O = observed count in each category. E = expected count under the null hypothesis. Σ = sum taken across all categories."

**SKELETON C — "Parallel worked-calculation paragraph"**
`The working for [quantity 1] and [quantity 2] are seen below: ∑(component 1) = [number 1]   ∑(component 2) = [number 2]. N₁ = [n]. Fraction 1 = [numerator 1]/[n]. Fraction 2 = [numerator 2]/[n]. Quantity 1 ≈ [result 1]. Quantity 2 ≈ [result 2].`

1. **Slots:**
   - Slot opener: a forward-pointing sentence ("seen below").
   - Intermediate-sums pair: two bracketed sums placed side-by-side.
   - Divisor pair: two equal sample sizes stated once each.
   - Fraction pair: numerator / denominator, repeated for the second quantity.
   - Verdict pair: two final values preceded by "≈".
2. **How to fill with a different idea:** pick a calculation that has identical structure for two datasets (e.g., two means, two variances); compute the numerator expression for both, place them in two columns, share the divisor, then write the two rounded answers side-by-side.
3. **Original fill:** Σ(x − x̄)² = 2142682.233 and Σ(y − ȳ)² = 5.073; N_x = N_y = 86; 2142682.233/86 and 5.073/86; σx ≈ 157.845, σy ≈ 0.243.
4. **Demonstration fill (different idea — two sample standard deviations of reaction times):** "The working for σ_concert and σ_silence are seen below: Σ(t − t̄)² = 142.8 and Σ(t − t̄)² = 98.4. N = 30 each. 142.8/29 and 98.4/29. σ_concert ≈ 2.22 s, σ_silence ≈ 1.84 s."

## Express-Idea Vocabulary

- **Sequencing / forward-pointing:** "the following formula was used" — anchors the formula as the *next* thing to look at.
- **Forward-pointing transition:** "seen below" — hands reader from setup to working.
- **Concession pivot ("while…"/"same… will"):** "While the formula indicates the values used for the x data points, the same formula will be used for the y points" — concedes the formula's wording, then mirrors it.
- **Specification / scope-narrowing:** "for the x data points" / "for the y points" — restricts each instance to one dataset.
- **Evidence handling (computed quantities as facts):** "∑(x − x̄)² = 2142682.233" — presents the sum as a stated number.
- **Approximation marker:** "σx ≈ 157.845" — signals the final numeric verdict.
- **Explanation verbs / definition format:** "σx = standard deviation of x data points" / "x̄ = mean of the x values" / "N = total number of points in data set" — verb of definition is implied "is" written as "="; the equation-sign acts as "is defined as".

## How to Explain an Idea (replication steps)

The pattern is **worked-calculation: formula → variable key → parallel substitution → parallel verdict**. To explain any new quantity the same way:

1. **Name the target quantity** in a purpose sentence ("To find X, …").
2. **State the formula** in its symbolic form, displayed so it stands alone.
3. **Define every symbol** in the formula, one per line, in the order the reader will meet them.
4. **Insert a forward-pointing sentence** that hands the reader to the next block ("…seen below:").
5. **Compute the intermediate expression** (sum, product, etc.) for both datasets and place the two values **side-by-side** so the reader can compare.
6. **State the shared divisor** (sample size, N) for each dataset, also side-by-side.
7. **Write the two fractions** (numerator ÷ divisor) explicitly — do not skip the substitution step.
8. **Give the two final answers** with an approximation sign ("≈"), side-by-side, so the reader sees that the same method produced two parallel results.
