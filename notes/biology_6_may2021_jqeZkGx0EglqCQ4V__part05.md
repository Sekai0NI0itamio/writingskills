# Idea Flow Notes: biology_6_may2021_jqeZkGx0EglqCQ4V — 0 (control) 10ml         20ml        30ml        40ml

## Paragraph Flow (move by move)

**Paragraph 1** (table — header line "0 (control) 10ml 20ml 30ml 40ml")
- Move 1: header — establishes column variables ("0 (control) 10ml 20ml 30ml 40ml"). Hands forward by *enumerating* the categories the data rows will populate.
- Move 2: numbered data row — presents a single trial as raw measurement ("25.3± .159 31.8± .159 …"). Hands forward by *iteration* — the reader expects the next numbered row to repeat the same shape.

**Paragraph 2** (rows 2–7 of the table)
- Repeats the same row move seven times, each handing forward by *parallel iteration*; the form itself (not content) accumulates evidence.

**Paragraph 3** ("PROCESSED DATA" header — "The raw data has error bars based on the standard error of the mean (SEM).")
- Move 1: section label — signals a new stage ("PROCESSED DATA").
- Move 2: claim about data treatment ("The raw data has error bars based on"). Hands forward by *specification* — the next sentence must name what SEM is.
- Move 3: definition anchor with formula ("SEM or s̄x = σ / √n where σ…"). Hands forward by *naming a worked instance* — the next sentence picks one column to demonstrate.
- Move 4: chosen instance ("Taking the data of the 40ml shoot length, the SEM can be calculated"). Hands forward by *procedure announcement* — the reader expects the steps that follow.

**Paragraph 4** ("The first step is finding the value of the standard deviation.")
- Move 1: stage label / procedure pointer ("The first step is finding"). Hands forward by *signposting the order* of upcoming operations.
- Move 2: formula restated ("σ = √(1/(N−1) Σ(xᵢ − x̄)²)"). Hands forward by *substituting components* — next line supplies the mean.
- Move 3: worked substitution of the mean ("x̄ = (3.1 + 3.7 + …)/7 = 3.9142857142857"). Hands forward by *completion of sub-step* — the next sentence can now square deviations.

**Paragraph 5** ("σ = √(1/(N−1) Σ(xᵢ − 3.9142857142857)²). N is equal to …")
- Move 1: formula with numerical plug-in ("σ = √(1/(N−1) Σ(xᵢ − 3.9142857142857)²)"). Hands forward by *next algebraic move* — squaring both sides.
- Move 2: variable definition ("N is equal to the number of specimens"). Hands forward by *parameter clarification* needed for the next operation.
- Move 3: algebraic simplification announcement ("Squaring both sides of the equation simplifies"). Hands forward by *revealing the simplified form*.
- Move 4: simplified form restated ("σ² = Σ(xᵢ − x̄)²/(N−1)"). Hands forward by *naming the next quantity to compute*.

**Paragraph 6** ("Σ(xᵢ − x̄)²/(N−1) = (3.1−3.9…)² + … / (7−1)")
- Move 1: expansion of the numerator/denominator with each datum shown ("(3.1−3.9…)² + (3.7−3.9…)² + …"). Hands forward by *computational execution* — the result must be stated.
- Move 2: result of computation ("variance is 0.1747619047619"). Hands forward by *reverse operation* — square-root to recover σ.
- Move 3: recovered σ ("σ = 0.4180453381655"). Hands forward by *plug-back* — σ is now ready to enter the SEM equation.

**Paragraph 7** ("Now the value for the standard deviation can be plugged…")
- Move 1: transition + plug-in ("Now the value for the standard deviation can be plugged"). Hands forward by *substitution announcement*.
- Move 2: numerical result ("s̄x = 0.4180453381655/√7 = 0.15800628593369"). Hands forward by *interpretation*.
- Move 3: interpretation as a percentage ("the standard amount of error for that group sample is 15%"). Hands forward by *implication* — the text cuts off mid-thought, but the next move would be comparison or judgement.

## What This Section Does (content sequence)
This is a **processed-data + worked-example** section, and the sequence is:
1. **Raw data table** (column variables first, then iterated rows) — sets up *what* will be processed.
2. **Transition label** ("PROCESSED DATA") — marks the shift from observation to analysis.
3. **Claim about the treatment** ("error bars based on SEM") — states *why* the numbers exist.
4. **Definition + formula of the statistic** — gives the reader the *tool* being applied.
5. **Choice of a single column to demonstrate** — narrows scope so the procedure is tractable.
6. **Stage 1 of the procedure** ("first step is finding the standard deviation") — signposts the sub-task.
7. **Substitution of mean** — supplies a quantity the next formula needs.
8. **Squaring / simplification step** — converts formula into a computable shape.
9. **Full numeric expansion** — shows every term, then collapses to variance.
10. **Recovery of σ via square root** — completes the intermediate quantity.
11. **Plug σ into SEM equation** — returns to the statistic named in step 4.
12. **Interpretation as a percentage** — translates abstract number into a meaningful bound ("15%").

The order matters because each move **unlocks the next computation**: the formula needs values, values need a chosen column, the column needs a mean, the mean needs deviation, the deviation needs squaring, and only then can σ be plugged into the headline statistic. The reader is walked along the dependency chain.

## Paragraph Skeletons (replicable templates)

**Skeleton A — "Definition → instance selection → procedure announcement"** (paragraph 3 pattern)
- SKELETON: "[SECTION LABEL]. [The data / sample / result] has [treatment / property] based on [named statistic] ([abbreviation]). [Statistic full name] is defined as [formula or quote of formula]; where [symbols explained]. [Taking / Using] the data of [specific subset], the [statistic] can be calculated."

  1. Slot 1 — section label (single noun phrase, capitals).
  2. Slot 2 — claim sentence: "[Subject] has [feature] based on [statistic name]" — past/present tense, one clause.
  3. Slot 3 — formula display (equation block) + "where" clause defining each symbol.
  4. Slot 4 — instance sentence: "[Taking/Using] the data of [subset], the [statistic] can be calculated" — sets up the worked example.

  - **Original fill:** "PROCESSED DATA. The raw data has error bars based on the standard error of the mean (SEM). SEM or s̄x = σ/√n where σ represents a sample's standard deviation and n is the amount of data points. Taking the data of the 40ml shoot length, the SEM can be calculated."
  - **Demonstration fill (different idea):** "NORMALISED YIELDS. The reaction output has confidence limits based on the standard error of the proportion (SEP). SEP or p̂ = √(p(1−p)/n) where p is the observed proportion and n is the trial count. Taking the data of the 50 °C trial run, the SEP can be calculated."

**Skeleton B — "Stage label → formula restated with one symbol plugged"** (paragraph 4–5 pattern)
- SKELETON: "[The first / next / final] step is [gerund phrase]. [Formula] = [formula with one numeric substitution]. [Variable] is equal to [its definition]. [Algebraic move verb]-ing both sides of the equation [simplifies / rearranges] the equation. [Simplified formula]."

  1. Slot 1 — ordinal step marker ("first step", "next step").
  2. Slot 2 — formula in symbolic form.
  3. Slot 3 — same formula with one literal number inserted.
  4. Slot 4 — short definitional clause for the remaining symbol.
  5. Slot 5 — algebraic move sentence ("Squaring both sides…", "Dividing both sides…").
  6. Slot 6 — the simplified equation restated.

  - **Original fill:** "The first step is finding the value of the standard deviation. σ = √(1/(N−1) Σ(xᵢ − x̄)²). The mean can be calculated as x̄ = (3.1 + 3.7 + 3.9 + 4 + 4.1 + 4.3 + 4.3)/7 = 3.9142857142857. N is equal to the number of specimens in each group, 7. Squaring both sides of the equation simplifies the equation. σ² = Σ(xᵢ − x̄)²/(N−1)."
  - **Demonstration fill (different idea):** "The first step is finding the value of the variance. Var(X) = (1/(n−1)) Σ(xᵢ − μ)². The mean can be calculated as μ = (12 + 14 + 15 + 16 + 18)/5 = 15. n is equal to the number of readings, 5. Squaring the deviation for each term gives the squared-error total. Var(X) = Σ(xᵢ − μ)²/(n−1)."

**Skeleton C — "Full expansion → collapse to one number → reverse operation"** (paragraph 6 pattern)
- SKELETON: "[Numerator/denominator expression] = ([each term shown explicitly]) / ([constant]). Completing all of the operations on the top and bottom, the fraction becomes [result]. [Square-rooting / Inverting / Re-arranging] both sides means that [recovered quantity] = [number]."

  1. Slot 1 — fraction written with every term expanded inline.
  2. Slot 2 — execution sentence announcing collapse to one number.
  3. Slot 3 — final numeric value (named as variance / probability / total, etc.).
  4. Slot 4 — inverse operation sentence recovering the un-squared (or un-summarised) quantity.

  - **Original fill:** "Σ(xᵢ − x̄)²/(N−1) = (3.1−3.9…)² + (3.7−3.9…)² + … / (7−1). Completing all of the operations on the top and bottom, the fraction becomes [result]. The standard deviation squared or the variance is 0.1747619047619. Square rooting both sides means that σ = 0.4180453381655."
  - **Demonstration fill (different idea):** "Σ(pᵢ − p̄)² / (n−1) = (0.12−0.20)² + (0.18−0.20)² + (0.22−0.20)² + (0.28−0.20)² / (4−1). Completing all of the operations on the top and bottom, the fraction becomes 0.016. The variance is 0.016. Square rooting both sides means that the standard deviation = 0.1265."

**Skeleton D — "Plug-back → numeric result → interpretation"** (paragraph 7 pattern)
- SKELETON: "Now the value for [intermediate quantity] can be plugged into the equation [formula] = [formula]. [Symbol] is [value], so the equation becomes [formula with substitution] = [final number]. This means that [plain-English interpretation of the number]."

  1. Slot 1 — "Now" transition opening the plug-back.
  2. Slot 2 — original headline formula restated.
  3. Slot 3 — symbol-to-value assignment sentence.
  4. Slot 4 — fully substituted equation giving final number.
  5. Slot 5 — "This means that…" interpretation in everyday terms (often as a percentage or bounded quantity).

  - **Original fill:** "Now the value for the standard deviation can be plugged into the equation s̄x = σ/√n. N is 7, so the equation becomes s̄x = 0.4180453381655/√7 = 0.15800628593369. This means that the standard amount of error for that group sample is 15%."
  - **Demonstration fill (different idea):** "Now the value for the standard deviation can be plugged into the equation CI = 1.96·σ/√n. n is 30, so the equation becomes CI = 1.96·0.42/√30 = 0.150. This means that the 95% confidence interval half-width for that group sample is 0.15 units."

## Express-Idea Vocabulary
- **Sequencing / stage-marking:** "The first step is finding" — announces the next operation. "Now the value for" — signals the plug-back stage.
- **Specification / narrowing:** "Taking the data of the 40ml shoot length" — selects one column for the worked example.
- **Definition / formula handling:** "is defined as" (implicit via equation), "where σ represents", "N is equal to the number of specimens".
- **Algebraic-move verbs (explanation mechanism):** "Squaring both sides of the equation simplifies the equation" — names the algebraic operation as an action. "Square rooting both sides means that σ=" — converts an inverse operation into a conclusion.
- **Completion / collapse:** "Completing all of the operations on the top and bottom, the fraction becomes" — condenses expanded terms into a single result.
- **Interpretation / meaning:** "This means that the standard amount of error" — translates the number into plain-English meaning, here as a percentage.
- **Authority / epistemic neutral:** no appeals to sources in this section; the equations themselves carry authority.

## How to Explain an Idea (replication steps)
The section uses a **formula → symbol-by-symbol worked calculation → plug-back → interpretation** pattern.

1. **Name the section** with a single capitalised label (e.g. "PROCESSED DATA").
2. **State the claim** in one sentence: what feature of the data is being quantified.
3. **Display the headline formula** and define every symbol in a "where…" sentence.
4. **Select the subset** of data the worked example will use, in one sentence.
5. **Signpost stages** with "The first step is…", "The next step is…" — turn the procedure into a numbered tour.
6. **Restate each formula with one new number substituted** as the tour proceeds, so the reader sees the formula evolving.
7. **Show every term expanded** before collapsing — write each (xᵢ − x̄)² individually, then announce the collapse with "Completing all of the operations…".
8. **State the intermediate result** (e.g. variance) by its technical name, not just its number.
9. **Name the inverse operation** ("Square rooting both sides means that…") to recover the un-squared quantity.
10. **Plug the recovered quantity back into the headline formula**, then rewrite the headline equation in fully substituted form to give the final number.
11. **Interpret the number in plain English** with a "This means that…" sentence, converting the abstract value into a percentage, threshold, or bound that the reader can use.

The pattern forces the reader along the **dependency chain** of the calculation: nothing is computed before its prerequisites are shown, and every algebraic step is named as an action rather than skipped.
