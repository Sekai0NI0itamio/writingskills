# Idea Flow Notes: chemistry_7_may2021_fLxO5wBwhiXqNACh — Purity

## Paragraph Flow (move by move)

**Paragraph 1 — Raw data block (table of repeated trials)**

Sentence 1 *(table header + 5 rows of values)*: **Evidence / data dump** — quotes "11.238 ... 11.604 ... 11.756 ... 11.858 ... 11.917". This presents the repeated trials for one condition and hands the reader to the calculation block because the table alone cannot answer how much spread there is; the reader needs a numerical average to anchor the spread calculation.

**Paragraph 2 — Anchoring the average**

Sentence 1 *(Avergae Volume for pH 11.238 = 35.65mL)*: **Definition / anchor value** — quotes "Avergae Volume for pH 11.238 = 35.65mL". Hands to the next sentence because once the centre is named, the spread from that centre must now be computed in both directions.

**Paragraph 3 — Upper deviation**

Sentence 1 *(△V = Vmax − Vaverage = 35.95 − 35.65 = 0.3)*: **Mechanism / calculation (upper side)** — quotes "Vma x − Vaverage = 35.95 − 35.65". Hands forward by symmetry: the upper deviation has been computed, so the lower deviation must be computed the same way to allow comparison.

**Paragraph 4 — Lower deviation**

Sentence 1 *(△V = Vaverage − Vmin = 35.65 − 35.45 = 0.2)*: **Mechanism / calculation (lower side)** — quotes "Vaverage − Vmin − = 35.65 − 35.45 = 0.2". Hands to the decision sentence because two candidate uncertainties now exist and a selection rule is required.

**Paragraph 5 — Selection rule**

Sentence 1 *(The larger random uncertainty is taken, in this case ± 0.2mL)*: **Verdict / selection** — quotes "The larger random uncertainty is taken". Hands forward by contrast: a value has been chosen, so the reader now needs to know why the smaller competing source of error (the burette itself) is set aside.

**Paragraph 6 — Justification + action**

Sentence 1 *(In this case the random uncertainty is greater than the burette's uncertainty (± 0.1mL), I will be ignoring the instrumental uncertainty)*: **Justification + decision action** — quotes "the random uncertainty is greater than the burette's uncertainty". Hands to the next section ("Processed Data Representation") because the uncertainty number is fixed and now must be carried forward into a plot.

**Paragraph 7 — Transition to visualisation**

Sentence 1 *(D. Processed Data Representation / Figure 9: mass of pure caffeine vs pH of aqueous brewing solution)*: **Transition / forward pointer** — quotes "mass of pure caffeine vs pH of aqueous brewing solution". Hands forward by setting up the reader for what the uncertainty will be applied to next.

## What This Section Does (content sequence)

A "random uncertainty of an averaged trial" section moves through this fixed sequence:

1. **Raw repeated trials** (a table of the same measurement repeated several times). *Why first:* the reader must see the spread before any spread-statistic can be justified.
2. **Anchor average** (state the mean of those trials). *Why second:* every deviation is measured from this point, so it must exist on the page before any ΔV can be written.
3. **Upper deviation (max − average)**. *Why third:* one side of the spread has to be calculated first to establish the comparison.
4. **Lower deviation (average − min)**. *Why fourth:* the mirror calculation produces a second candidate uncertainty.
5. **Selection verdict** (take the larger of the two). *Why fifth:* a stated rule resolves the comparison; without it the reader cannot know which number to use downstream.
6. **Comparison against instrumental uncertainty** (is my random error bigger than the instrument's resolution?). *Why sixth:* the chosen value is only meaningful if it dominates the alternative error source.
7. **Action statement** (ignore the smaller, instrumental uncertainty). *Why seventh:* explicitly states which error budget is being carried forward.
8. **Forward transition** (heading + figure caption naming the dependent vs. independent variables). *Why eighth:* the uncertainty is now a property of the x-axis and must be applied to a graph.

A student replicating this on any other experiment (e.g. cooling rate, titration of a different acid) keeps this eight‑step skeleton and only swaps the numbers and the variable names.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Two-sided spread calculation"**

> SKELETON: "[Label of averaged quantity] = [value][units]. △[symbol] = [max symbol] − [average symbol] = [max] − [average] = [result]. △[symbol] = [average symbol] − [min symbol] = [average] − [min] = [result]."

1. **What each slot holds** — first line is a noun-phrase definition with an equals sign; each subsequent line is a symbolic equation with three equals separated by minus signs and a numerical result. The grammar is identical in both Δ lines (subject → equals → three terms → result).
2. **How to fill with a different idea** — slot 1: write "[Quantity name] for [condition label] = [mean][units]". slot 2: use the maximum value from your table on the left and the mean in the middle. slot 3: use the mean in the middle and the minimum on the left. Keep the equation shape exactly parallel.
3. **Original fill** — "Avergae Volume for pH 11.238 = 35.65mL. △ V = Vma x − Vaverage = 35.95 − 35.65 = 0.3. △ V = Vaverage − Vmin − = 35.65 − 35.45 = 0.2."
4. **Demonstration fill (different idea)** — "Mean Cooling Time for Trial Set B = 142 s. △T = Tmax − Tmean = 158 − 142 = 16. △T = Tmean − Tmin = 142 − 128 = 14."

**SKELETON B — "Selection rule + comparator + override"**

> SKELETON: "The [direction adjective] [error type] is taken, in this case ± [value][units]. In this case the [error type] is [comparator] than the [instrument]'s uncertainty (± [value][units]), I will be ignoring the [alternative source] uncertainty for the [error type] calculated."

1. **What each slot holds** — sentence 1: passive "is taken" verdict with a numerical signed value; sentence 2: two-clause structure where the first clause runs the comparison and the second clause names the abandoned source. Both use the same error-type word three times in sentence 2 (subject, comparison, object of "for").
2. **How to fill with a different idea** — slot 1: pick whichever of your two Δ values is bigger and prefix with "larger" (or "greater" if comparing absolute). slot 2: state the instrument's rated precision in parentheses, then say you are dropping it because the random error dominates.
3. **Original fill** — "The larger random uncertainty is taken, in this case ± 0.2mL. In this case the random uncertainty is greater than the burette's uncertainty (± 0.1mL), I will be ignoring the instrumental uncertainty for the random uncertainty calculated."
4. **Demonstration fill (different idea)** — "The larger timing uncertainty is taken, in this case ± 7 s. In this case the random uncertainty is greater than the stopwatch's uncertainty (± 0.5 s), I will be ignoring the instrumental uncertainty for the random uncertainty calculated."

## Express-Idea Vocabulary

**Anchoring / definition**
- "**Avergae Volume for pH 11.238 = 35.65mL**" — defines the centre value with an equals-sign noun phrase.

**Calculation verbs (implicit)**
- "**= 35.95 − 35.65 = 0.3**" — arithmetic written as chain-of-equalities, not as "calculate" or "compute".

**Selection / verdict**
- "**The larger random uncertainty is taken**" — passive "is taken" commits to a single number from competing candidates.

**Comparison**
- "**greater than the burette's uncertainty (± 0.1mL)**" — magnitude comparison with bracketed instrument spec immediately after.

**Concession / override**
- "**I will be ignoring the instrumental uncertainty**" — first-person future intent marks the abandoned source explicitly.

**Forward transition**
- "**Processed Data Representation**" / "**mass of pure caffeine vs pH of aqueous brewing solution**" — section heading plus a "vs" axis statement names what the uncertainty will next be applied to.

(No sequencing connectives, no "therefore" / "hence", no "however" appear in this section — its logic is carried entirely by equation shape, the "is taken" verdict, and the "greater than" comparison.)

## How to Explain an Idea (replication steps)

This section uses the **two-sided-spread → take-the-larger → comparator-override** pattern. To replicate it for any new measurement:

1. **Tabulate** at least three repeated trials of the same measurement (one row per trial, identical column structure).
2. **State the mean** of those trials on its own line, in the form "[Quantity] for [condition] = [value][units]".
3. **Compute the upper deviation** by writing the equation exactly as "[Δ symbol] = [max symbol] − [average symbol] = [number] − [number] = [result]". Do not label it "upper" — the equation shape carries that meaning.
4. **Compute the lower deviation** in the mirror form "[Δ symbol] = [average symbol] − [min symbol] = [number] − [number] = [result]". The two Δ lines must be visually parallel so the reader sees they are a matched pair.
5. **Announce the verdict** in one sentence using the passive "is taken": name the adjective ("larger"), name the error type, give the signed value with units.
6. **Compare to the instrument's stated precision** in the same sentence or the next, using "greater than" with the instrument's ±value in parentheses.
7. **State the override** in first person ("I will be ignoring the instrumental uncertainty") so the reader sees which source has just been dropped from the error budget.
8. **Hand forward** by titling the next sub-section ("Processed Data Representation") and writing a "vs" figure caption that names the dependent and independent variables — the uncertainty from step 5 will now ride on the x-axis of that plot.
