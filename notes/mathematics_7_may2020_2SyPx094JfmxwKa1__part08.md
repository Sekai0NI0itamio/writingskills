# Idea Flow Notes: mathematics_7_may2020_2SyPx094JfmxwKa1 — Original Function                                        Approximation at the Vertex

## Paragraph Flow (move by move)

**Paragraph 1** (single paragraph, four moves)

**Move 1 — Context + Visual setup:** Sentence 1 introduces the figure and its legend.
- *"Fig. 5 shows the plot of this Fourier series along with its original function, where the purple line is the Fourier series..."*
- Job: anchors the reader to a visual artefact and supplies the colour key so the graph can be read.
- Hand-off → it raises a natural question the reader will ask on seeing the colour list: *why does it jump from 1 term to 3 terms?* This forces Move 2.

**Move 2 — Mechanism / exclusion with cause:** Sentence 2 explains why some lines are missing.
- *"It should be noted that the Fourier series with even number of terms are not plotted because 4 − 4(−1)# cancel to 0..."*
- Job: a flagged caveat ("It should be noted that") that supplies the algebraic reason an entire class of partial sums is omitted.
- Hand-off → the algebra leads to an equivalence (2𝑚 − 1 = 2𝑚), which begs the writer to state the notational convention this implies — exactly Move 3.

**Move 3 — Consequence + Convention (derived notation):** Sentence 3 announces a naming convention.
- *"Therefore, the Fourier series with 𝑛 = 2𝑚 − 1 has 𝑚 terms..."*
- Job: the "Therefore" turn turns the equivalence from Move 2 into a reusable rule for the rest of the example.
- Hand-off → with the convention locked in, the reader is now equipped to interpret the visual verdict that follows in Move 4.

**Move 4 — Verdict / trend observation from the visual:** Sentence 4 states the conclusion drawn from the graph.
- *"As shown in the graph, as the number of terms in the Fourier series increases, the Fourier series approximates the given function better."*
- Job: closes the paragraph by reading off the visible trend and delivering a comparative judgment ("better").
- Hand-off → nothing follows in this section; this is the terminal claim of the figure caption.

## What This Section Does (content sequence)

This is a **figure-caption-with-justification** section. The moves, in order, are:

1. **Visual anchor + legend.** Tell the reader what figure is on the page and what each colour means. *Why first:* the reader must be able to decode the visual before any claim about it can land.
2. **Methodological caveat (what is omitted and why).** Flag a feature of the plot that would otherwise look like a gap — an entire parity of partial sums is skipped — and give the algebraic reason. *Why second:* the legend in step 1 left an unexplained gap; the caveat both fills and justifies it.
3. **Convention derivation.** Turn the caveat into a reusable piece of notation (one index ↔ one term count). *Why third:* without the convention, later sentences using "n terms" would be ambiguous; this step pre-empts that confusion.
4. **Terminal verdict from the visual.** Read off the qualitative trend (more terms → better approximation). *Why last:* only now does the reader have both the legend and the indexing rule needed to accept the verdict at face value.

Replicated generally: any time you present a multi-series plot, the order is **legend → exclusions/caveats → naming convention → overall trend**.

## Paragraph Skeletons (replicable templates)

### Skeleton A — "Visual anchor + colour-coded legend"

**SKELETON:** *"[Figure X] shows the plot of [series A] along with its [baseline B], where [colour 1] is [series variant 1], [colour 2] [variant 2], [colour 3] [variant 3], ... and [colour n] [baseline/ground truth]."*

1. **What each slot holds:** 
   - Figure reference (noun phrase, definite article).
   - Series name (count noun with "this/its" demonstrative).
   - Legend entries (each = colour adjective + "with" + number/category, ending in the ground truth).
   - Grammatical shape: one long declarative sentence with a "where"-clause doing the legend work.
2. **How to fill with a different idea:** Slot 1 = name your figure ("Fig. 7"); slot 2 = name the approximation family you're graphing; slot 3 = pick a baseline (true function, exact solution, data points); slots 4+ = choose 3–5 colours each tied to a parameter value (n, iterations, terms) and end with the colour reserved for the baseline.
3. **Original filled version:** *"Fig. 5 shows the plot of this Fourier series along with its original function, where the purple line is the Fourier series with only the 0th term ..., red with 1 term, blue 3, green 5, and black the original function."*
4. **Demonstration fill (different idea):** *"Fig. 2 shows the plot of the iterated logistic map along with its stable fixed points, where the orange curve is the map after 1 iteration, the green curve after 3, the blue after 7, and the black dashed line the identity y = x."*

### Skeleton B — "Flagged exclusion with algebraic cause"

**SKELETON:** *"It should be noted that [omitted class] are not [shown/plotted/included] because [algebraic reason], which makes [subset A] the same as [set B] where [domain qualifier]."*

1. **What each slot holds:**
   - Opening flag ("It should be noted that").
   - Omitted class (a parity/index/category, plural noun).
   - Algebraic reason (an equation showing cancellation or identity).
   - Resulting equivalence stated in symbolic form with a where-clause defining the domain.
   - Grammatical shape: one sentence, two clauses joined by "because... which makes...".
2. **How to fill with a different idea:** Pick a structural symmetry in your data (odd/even, positive/negative, even multiples, etc.) that causes duplicates; state the duplicate class as the omitted one, write the cancellation as a one-line identity, then express the equivalence symbolically and restrict the index set.
3. **Original filled version:** *"It should be noted that the Fourier series with even number of terms are not plotted because 4 − 4(−1)# cancel to 0, which makes the Fourier series with 2𝑚 − 1 terms the same as that with 2𝑚 terms where 𝑚 𝜖 𝑁."*
4. **Demonstration fill (different idea):** *"It should be noted that the trapezoidal-rule estimates with even sub-intervals are not plotted because the correction terms of order 2𝑘 cancel pairwise, which makes the estimate with 2𝑘 − 1 sub-intervals identical to that with 2𝑘 sub-intervals where 𝑘 ∈ ℕ."*

### Skeleton C — "Convention derived from the caveat"

**SKELETON:** *"Therefore, [symbol/quantity] equals [re-statement], and this convention will be used throughout this [example/section/report]."*

1. **What each slot holds:**
   - "Therefore" as consequence marker.
   - Re-statement of the equivalence in simpler counting language, often with a parenthetical exclusion.
   - Forward-looking sentence committing the rule to the rest of the work.
   - Grammatical shape: a compound sentence linked by "and", second clause in future tense.
2. **How to fill with a different idea:** Take the equivalence from Skeleton B and rewrite it as a count (e.g. "has k nodes", "carries k digits"); add the parenthetical "(not counting [one excluded term])"; close by announcing that this is your standing convention.
3. **Original filled version:** *"Therefore, the Fourier series with 𝑛 = 2𝑚 − 1 has 𝑚 terms (not counting the constant term), and this convention will be used throughout this example."*
4. **Demonstration fill (different idea):** *"Therefore, a B-tree of order 𝑛 = 2𝑚 − 1 contains 𝑚 keys per node (not counting the header pointer), and this convention will be used throughout this implementation."*

### Skeleton D — "Visual verdict / trend claim"

**SKELETON:** *"As shown in the graph, as [independent variable] increases, [dependent quantity] [verb of approach/divergence] [reference quantity] [comparative adverb]."*

1. **What each slot holds:**
   - "As shown in the graph" as anchor.
   - "as X increases" as the trend driver.
   - A transitive verb of approximation or divergence (approximates, converges on, exceeds).
   - A comparative adverb (better, more closely, faster).
   - Grammatical shape: one sentence with a fronted temporal clause and a comparative conclusion.
2. **How to fill with a different idea:** Pick the knob you varied across the colour series in Skeleton A; name what is being matched; choose a comparative verb that captures the direction of the trend.
3. **Original filled version:** *"As shown in the graph, as the number of terms in the Fourier series increases, the Fourier series approximates the given function better."*
4. **Demonstration fill (different idea):** *"As shown in the graph, as the number of Monte Carlo samples increases, the simulated mean approaches the analytical expectation more closely."*

## Express-Idea Vocabulary

**Sequencing / anchoring**
- *"Fig. 5 shows the plot of this Fourier series along with..."* (visual anchor as opener)
- *"As shown in the graph, as the number of terms..."* (re-anchoring at the close)

**Caveat flagging**
- *"It should be noted that the Fourier series with even number of terms..."* (politeness hedge introducing an exception)

**Cause / consequence**
- *"because 4 − 4(−1)# cancel to 0"* (compact algebraic cause)
- *"which makes the Fourier series with 2𝑚 − 1 terms the same..."* (relativised consequence of the cause)
- *"Therefore, the Fourier series with 𝑛 = 2𝑚 − 1 has 𝑚 terms"* (explicit consequence marker carrying the equivalence into a rule)

**Convention / forward scope**
- *"this convention will be used throughout this example"* (commitment clause locking the rule forward in time)

**Comparison / verdict**
- *"approximates the given function better"* (comparative adverb ending the section's claim)

**Specification (implicit)**
- *"not counting the constant term"* (parenthetical narrowing of what the count includes)

## How to Explain an Idea (replication steps)

This section runs on a **visual-evidence-led** explanation pattern with an embedded algebraic caveat. Steps to reproduce it with a new idea:

1. **Open with the visual and its legend.** State the figure number, name what is plotted alongside what baseline, then list each series as `[colour] with [parameter]`, finishing on the ground-truth series.
2. **Flag an omission with "It should be noted that..."** Identify one class of cases that is *missing* from the legend. This anticipates a question the reader will have when they look at the plot.
3. **Give the algebraic / structural cause in one equation.** Write the identity that forces the omission (a cancellation, a symmetry, a duplication). Keep it as compact as possible — one displayed-style fragment inside the running sentence.
4. **State the resulting equivalence as a "which makes..." clause.** Convert the equation into the relationship between two indexed families and restrict the domain (e.g. `where m ∈ ℕ`).
5. **Pivot with "Therefore" and turn the equivalence into a counting convention.** Re-phrase the equivalence in plain counting language, parenthetically exclude the trivially-counted piece, and commit the rule to the rest of the work with "this convention will be used throughout this [example/section]."
6. **Close with a "As shown in the graph, as X increases, Y approximates Z better."** This is the single-sentence verdict that the whole caption has been building toward; it re-anchors to the figure and delivers the comparative claim.
