# Idea Flow Notes: mathematics_7_may2021_IRV8BRXWKji6u0XU — Trial (T)   Hits

## Paragraph Flow (move by move)

**Paragraph 1** (2 sentences — bridge from table to error metric)

1. **Transition + count + claim-proposal:** "we have conducted a total of 6 trials" — names the scope just demonstrated in the table; hands the reader forward by suggesting a *use* for that scope.
2. **Specification + setup-for-calculation:** "the average squared error, e, is:" — introduces the symbol `e` and the formula by name; hands the reader to the worked calculation by literally prompting them to expect a value next.

**Paragraph 2** (formula display — no prose moves; the displayed arithmetic *is* the move: sum-of-six concrete squared-errors → divided by 6 → single number `1.33·10⁻²`. The paragraph hands the reader forward by *finishing* — the calculation is terminal and only invites a "so what?", which the next paragraph supplies.)

**Paragraph 3** (2 sentences — pivot from n = 6 to arbitrary m)

1. **Transition + generalization move:** "Attempting to generalize, we could survey an m number of trials" — explicit leap from the fixed n = 6 to a variable m; hands the reader forward by replacing concrete instances with placeholders, demanding a new formula shape.
2. **Consequence + term-definition + setup:** "Thus the mth squared error being (p̂m − p)²" — names the per-trial quantity, then "and hence the mth average square error as such:" announces the final aggregate; hands the reader to a displayed general formula.

**Paragraph 4** (formula display — closes the pattern: a generic `e(p, m)` in summation form, which hands the reader out of the section by giving them a reusable formula rather than a verdict.)

## What This Section Does (content sequence)

The ordered sequence is:

1. **Recap the sample size** — anchor the reader in what was just done in the table.
2. **Propose a goodness metric** — give the reader a reason the upcoming arithmetic matters.
3. **Compute the metric for the fixed n** — show the concrete sum and resulting number.
4. **Pivot to generalization** — replace 6 with m, replace concrete errors with placeholder terms.
5. **Define the per-trial term symbolically** — so the summation is unambiguous.
6. **Display the general formula** — leave the reader with a reusable expression.

**Why this order:** the section moves *outward* from a specific small-n case to a general formula. The recap grounds the reader, the proposed metric tells them what to look at next, the concrete calculation gives a worked instance, and only then does the writer earn the right to generalize. A reader needs the worked number before the symbol `e(p, m)` carries meaning. Replicating this on a different topic: always finish the concrete calculation first, *then* signal "generalizing" before introducing new variables.

## Paragraph Skeletons (replicable templates)

**SKELETON A** (the "recap → propose metric → setup calculation" paragraph)
   `SKELETON: "[Transition], we have conducted a total of [N] [units], and hence we could think of taking [metric name] as a way of seeing how good [estimator] is as a means of approximating [target]! Doing this process, we get namely that [metric symbol], [name], is:"`

1. **Slots:**
   - *Transition* — short contrastive conjunction ("But then again", "Having done so", "Looking back").
   - *[N] [units]* — integer + noun naming what was just produced (trials, samples, runs).
   - *[metric name]* — a goodness-of-fit phrase in plain English (average squared error, mean absolute deviation).
   - *[estimator]* — the symbol with hat (p̂, β̂, μ̂) that the metric evaluates.
   - *[target]* — the true value being approximated (π, the regression coefficient, the population mean).
   - *[metric symbol]* — short letter, introduced in this sentence (e, MAD, RMSE).
2. **How to fill with a different idea:** Pick the dataset you actually ran (e.g. 8 simulation runs of a coin-flip estimator). State N and the noun; name a metric that compares estimator to truth; define the symbol here, do not assume the reader knows it.
3. **Original filled version:** "But then again, we have conducted a total of 6 trials, and hence we could think of taking the average squared error as a way of seeing how good the parameter p̂ is as a means of approximating π!"
4. **Demonstration fill with a new idea:** "Having collected a total of 8 simulations, we could think of taking the mean absolute deviation as a way of seeing how good the estimator θ̂ is as a means of approximating θ! Doing this process, we get namely that the mean absolute deviation, D, is:"

---

**SKELETON B** (the "generalize → define per-trial term → setup general formula" paragraph)
   `SKELETON: "Attempting to generalize, we could survey an m number of [units] each giving some [parameter with hat] from a true [parameter]. Thus the mth [per-unit error] being ([hat-var] − [true-var])² , and hence the mth [aggregate metric] as such:"`

1. **Slots:**
   - *"Attempting to generalize"* — fixed cue phrase signaling movement from specific to general.
   - *[units]* — noun that varies with the study (trials, samples, observations).
   - *[parameter with hat]* / *[parameter]* — estimator / truth pair.
   - *[per-unit error]* — name for the squared (or absolute) deviation.
   - *[aggregate metric]* — name for the averaged quantity.
2. **How to fill with a different idea:** Replace "6" with a generic `m`; explicitly pair each estimator with a truth value; define the per-trial symbol immediately before the formula display so the reader never meets an undefined term.
3. **Original filled version:** "Attempting to generalize, we could survey an m number of trials each giving some parameter p̂m from a true p. Thus the mth squared error being (p̂m − p)², and hence the mth average square error as such:"
4. **Demonstration fill with a new idea:** "Attempting to generalize, we could survey an m number of simulations each giving some estimator μ̂m from a true μ. Thus the mth squared error being (μ̂m − μ)², and hence the mth mean squared error as such:"

---

**SKELETON C** (the worked concrete calculation, formula-display paragraph)
   `SKELETON: "[Sum of N explicit per-unit terms]   e = —————————————————   e = [single decimal in s.f.]`

1. **Slots:**
   - *Numerator* — N previously-listed error values, written in scientific notation, added.
   - *Denominator* — the integer N from Skeleton A.
   - *Final value* — a single number in matching s.f. as the inputs.
2. **How to fill:** Write each error with the same number of significant figures; align vertically so the reader can re-add them; divide by N; present the quotient to the same precision.
3. **Original filled version:** `e = (7.09·10⁻³ + 4.03·10⁻³ + 2.73·10⁻² + 4.01·10⁻² + 2.75·10⁻⁴ + 1.29·10⁻³) / 6`, with `e = 1.33·10⁻²`.
4. **Demonstration fill with a new idea:** `MAD = (0.043 + 0.029 + 0.061 + 0.018 + 0.055 + 0.037 + 0.044 + 0.022) / 8`, with `MAD = 3.86·10⁻²`.

---

**SKELETON D** (the general formula paragraph)
   `SKELETON: [displayed summation: (Σ from i=1 to m of (estimator_i − truth)²) / m]`

1. **Slots:** summation index, per-trial squared deviation, denominator m.
2. **How to fill:** Mirror Skeleton B's terminology exactly; never introduce new symbols inside the display.
3. **Original filled version:** `e(p, m) = [(p̂₁ − p)² + (p̂₂ − p)² + … + (p̂_m − p)²] / m`.
4. **Demonstration fill:** `MSE(μ, m) = [(μ̂₁ − μ)² + … + (μ̂_m − μ)²] / m`.

## Express-Idea Vocabulary

- **Sequencing / forward motion:** "Doing this process" ("Doing this process, we get namely that the average squared error"); "we get namely" (introduces the *named* result the reader should now look at).
- **Cause / consequence:** "and hence" used twice — first to justify the *choice* of metric ("hence we could think of taking the average squared error"), then to justify the *formula* ("and hence the mth average square error as such"). "Thus" to chain the per-trial definition to the aggregate ("Thus the mth squared error being").
- **Contrast / concession (transition into the new move):** "But then again" ("But then again, we have conducted a total of 6 trials") — concedes the table was just seen and pivots to a new use of it.
- **Generalization cue:** "Attempting to generalize" ("Attempting to generalize, we could survey an m number of trials") — fixed signpost that the writer is leaving the specific n = 6 behind.
- **Explanation verbs:** "defined as" / "is" used to introduce `e` ("the average squared error, e, is:"); "being" used to define the per-trial term in shorthand ("the mth squared error being (p̂m − p)²").
- **Evidence handling:** implicit — the displayed sum itself is the evidence; the section never says "according to" or "this suggests", because the arithmetic *is* the argument.

## How to Explain an Idea (replication steps)

The pattern is **specific-instance-with-worked-number → generalize → symbolic general formula**, i.e. a *concrete-to-general* explanation. To replicate:

1. **State the sample size you actually produced** (an integer count tied to what the reader just saw). This anchors the next move.
2. **Propose the goodness metric in plain English** and give it a short symbol in the same sentence — so the reader is not ambushed by the symbol later.
3. **Display the concrete calculation** as numerator-over-denominator with every per-unit value written out, then state the single quotient in matching significant figures.
4. **Use a fixed generalization cue** ("Attempting to generalize", "To extend this…") to mark the leap from fixed N to a generic `m`. Do not start generalizing silently.
5. **Define every new symbol inline** the moment it appears (e.g. "the mth squared error being (p̂m − p)²"), so the next formula is read off already-defined pieces.
6. **Display the general formula** using only symbols already defined, with the summation laid out so each piece maps back to the concrete calculation in step 3.
7. **Stop without verdict.** The section's job is to *hand the reader a reusable expression*, not to judge it — leave evaluation for the section that follows.
