# Idea Flow Notes: biology_7_may2021_f2EKQVzK41czTZ1f — Results of data analysis and discussion

## Paragraph Flow (move by move)

**Paragraph 1: Height**

- **Sentence 1** — *Evidence pointer*: "Height: according to table 4." → Hands reader forward by **naming the variable AND its evidence source in one beat**; the next sentence must now unpack what that table shows.
- **Sentence 2** — *Evidence unpack (spread claim)*: "The standard deviation and sample variance of the group treated with the treatment 1 (water) and treatment 3 (0.5% microalgae) appears the largest…" → Hands reader forward by **flagging the two extreme groups first**, which forces the next sentence to give the opposite extreme for symmetry.
- **Sentence 3** — *Evidence unpack (opposite extreme)*: "…with treatment 2 (0.1% brown algae) having the lowest standard deviation and sample variance." → Hands reader forward by **a "but" pivot introduced in the next clause**, moving from spread to a graphical mean comparison.
- **Sentence 4** — *Counter-evidence / qualifier*: "with fig. 3 not showing a significant difference between the heights." → Hands reader forward by **ending on a test-statistic hook** that the next sentence will resolve.
- **Sentence 5** — *Verdict via test*: "Based on the ANOVA test results there is no significant difference between the group's means." → Hands reader forward by **closing one variable** (height), which cues the next paragraph to open the next variable in the same format.

**Paragraph 2: Fresh weight**

- **Sentence 1** — *Evidence pointer*: "Fresh weight: according to table 5." → Hands reader forward by **mirroring paragraph 1's opener**, signalling identical structure will follow for a new variable.
- **Sentence 2** — *Evidence unpack (extreme group)*: "The standard deviation and sample variance of the group treated with the treatment 5 (microalgae 0.01%) appeared to be the highest out of the groups…" → Hands reader forward by **inviting a comparison with the remaining groups**, supplied next.
- **Sentence 3** — *Evidence unpack (remainder)*: "with the rest having similar standard deviation and sample variance." → Hands reader forward by **switching evidence type** (variance table → mean figure), exactly as paragraph 1 did.
- **Sentence 4** — *Mean comparison*: "According to fig.5 the mean fresh weight of treatment 3 (0.5% microalgae) appears to be larger than the rest of the groups…" → Hands reader forward by **a "while" concession** that sets up the statistical verdict.
- **Sentence 5** — *Verdict via test*: "While the anova test did not reveal any significance of the data, the" → Sentence cuts off, but its move is a **concessive verdict that hands the reader an unfinished clause** — the text truncates before the consequence.

## What This Section Does (content sequence)

This is a **per-variable results-discussion block**. The replicated order is:

1. **Variable label + data source** — anchors the reader to *which* measurement and *which* table/figure carries it.
2. **Spread evidence (SD/variance)** — names the highest-spread group, then either the lowest or the "rest," because spread must be compared before means make sense.
3. **Mean evidence (figure)** — describes what the bar/plot shows about group means, framed relative to the spread-extreme already named.
4. **Statistical verdict (ANOVA)** — closes the variable with the inferential test result, usually framed as *non-significance* when visuals look suggestive.
5. **(Optional) Bridge / concession** — uses "while/although" to qualify the visual impression against the test result, preparing the next variable.

**Why this order works**: source first → spread second → mean third → test last. Putting spread before means prevents the reader from inferring significance from a figure alone; closing with ANOVA forces the reader to weigh the test above the visual. Repeating the same five-beat block per variable creates a scannable rhythm and makes missing data obvious.

## Paragraph Skeletons (replicable templates)

**Skeleton A — Single-variable results paragraph (with one extreme + opposite + figure + test):**

SKELETON: "[Variable]: according to table [#]. The standard deviation and sample variance of the group treated with [treatment code] appeared [extreme], with [opposite group] having [opposite extreme]. [Figure #] not showing a significant difference between the [variable]. Based on the [test] test results there is no significant difference between the group's means."

1. **Slot 1 — Variable + source**: grammatical shape = "Noun phrase: according to table/figure [#]." Hold = the measured quantity and its evidence container.
   *Fill differently*: pick your dependent variable (e.g. "Leaf width") and the table that holds its raw numbers.

2. **Slot 2 — Spread of named group**: grammatical shape = "The standard deviation and sample variance of the group treated with [code] appeared to be the [highest/lowest]…". Hold = the group with the most extreme dispersion.
   *Fill differently*: choose whichever treatment group in your data shows the widest spread, name its code, choose "highest" or "lowest."

3. **Slot 3 — Spread of contrasting group(s)**: grammatical shape = "with [group] having [opposite adjective]." Hold = the other end of the spread range OR a "similar" remainder.
   *Fill differently*: name the group at the opposite extreme, or write "with the rest having similar standard deviation and sample variance."

4. **Slot 4 — Figure-based mean comparison**: grammatical shape = "[Figure #] [not] showing a significant difference between the [variable]s." Hold = a qualitative read of the visual.
   *Fill differently*: state whether the bars look similar or whether one looks taller, and name the figure.

5. **Slot 5 — Inferential verdict**: grammatical shape = "Based on the [test] test results there is no significant difference between the group's means." Hold = the p-value decision.
   *Fill differently*: name your test (ANOVA, t-test, Kruskal-Wallis) and state "no significant difference" or report p.

**Original fill**: "Height: according to table 4. The standard deviation and sample variance of the group treated with the treatment 1 (water) and treatment 3 (0.5% microalgae) appears the largest out of the rest of the groups with treatment 2 (0.1% brown algae) having the lowest standard deviation and sample variance. with fig. 3 not showing a significant difference between the heights. Based on the ANOVA test results there is no significant difference between the group's means."

**Demonstration fill (different idea)**: "Root length: according to table 7. The standard deviation and sample variance of the group treated with fertilizer B appeared to be the highest out of the groups, with fertilizer A having the lowest standard deviation and sample variance. Fig. 9 not showing a clear difference between the root lengths. Based on the ANOVA test results there is no significant difference between the group's means."

---

**Skeleton B — Single-variable paragraph with "similar remainder" spread + figure-highlighted mean + concessive verdict:**

SKELETON: "[Variable]: according to table [#]. The standard deviation and sample variance of the group treated with [code] appeared to be the highest out of the groups, with the rest having similar standard deviation and sample variance. According to fig.[#] the mean [variable] of [code] appears to be larger than the rest of the groups all of which have similar means. While the [test] test did not reveal any significance of the data, [consequence/qualifier]."

1. **Slot 1 — Variable + source**: shape = "Noun phrase: according to table [#]." Hold = variable + container.
   *Fill differently*: swap "Fresh weight" for any continuous measurement and the table number.

2. **Slot 2 — Single extreme spread group**: shape = "The standard deviation and sample variance of the group treated with [code] appeared to be the highest out of the groups." Hold = one standout group.
   *Fill differently*: pick the treatment whose SD visibly jumps out in your dataset.

3. **Slot 3 — "Similar remainder" spread**: shape = "with the rest having similar standard deviation and sample variance." Hold = collapse the non-extreme groups.
   *Fill differently*: always write this verbatim when 3+ groups share a near-identical spread.

4. **Slot 4 — Figure mean highlight**: shape = "According to fig.[#] the mean [variable] of [code] appears to be larger than the rest of the groups all of which have similar means." Hold = which group's bar towers above the others.
   *Fill differently*: name the figure, the leading group, and assert the others "have similar means."

5. **Slot 5 — Concessive verdict**: shape = "While the [test] test did not reveal any significance of the data, [clause]." Hold = "although the figure looks different, the test says no."
   *Fill differently*: keep "while" + your test name + "did not reveal any significance"; the trailing clause can state the implication or open the next variable.

**Original fill**: "Fresh weight: according to table 5. The standard deviation and sample variance of the group treated with the treatment 5 (microalgae 0.01%) appeared to be the highest out of the groups, with the rest having similar standard deviation and sample variance. According to fig.5 the mean fresh weight of treatment 3 (0.5% microalgae) appears to be larger than the rest of the groups all of which have similar means. While the anova test did not reveal any significance of the data, the"

**Demonstration fill (different idea)**: "Shoot height: according to table 12. The standard deviation and sample variance of the group treated with nitrogen 50 ppm appeared to be the highest out of the groups, with the rest having similar standard deviation and sample variance. According to fig. 14 the mean shoot height of nitrogen 50 ppm appears to be larger than the rest of the groups all of which have similar means. While the ANOVA test did not reveal any significance of the data, the trend visually favours the 50 ppm treatment."

## Express-Idea Vocabulary

**Sequencing / source-pointing** (move from one piece of evidence to the next)
- "according to table 4" — used to launch a variable and bind it to its container.
- "according to table 5" — same move, next variable.
- "According to fig.5" — switches evidence type from numerical table to visual.

**Specification / extreme-naming** (locate the standout within a set)
- "appears the largest out of the rest of the groups" — flags the top-spread group.
- "having the lowest standard deviation" — flags the bottom-spread group.
- "appeared to be the highest out of the groups" — single-extreme variant.
- "with the rest having similar standard deviation" — collapses non-extreme groups.

**Qualification / hedging** (soften a claim before the test)
- "not showing a significant difference" — pre-empts an inferential reading from a figure alone.
- "appears to be larger than the rest" — visual hedge, not a claim of significance.

**Concession / contrast** (bridge visual to test)
- "While the anova test did not reveal any significance" — concedes against the figure's apparent signal.

**Evidence-handling verb** (carry the test result)
- "Based on the ANOVA test results there is no significant difference" — full inferential verdict in one clause.

## How to Explain an Idea (replication steps)

The pattern is **variable-by-variable evidence-stacking: source → spread → mean → test**, with each step pulling the next into focus.

To replicate with a NEW variable:

1. **Name the variable and bind it to one container.** Write "[Variable]: according to table [#]." This forces every later sentence to be evidence-anchored.
2. **State the spread of the most extreme group.** Use "The standard deviation and sample variance of the group treated with [code] appeared to be the [highest/lowest]…" — pick whichever extreme is true in your data.
3. **State the spread of the opposing group OR collapse the rest.** Either mirror with "with [code] having the [opposite]…" OR use "with the rest having similar standard deviation and sample variance." Choosing one keeps the sentence from overloading.
4. **Pivot to the figure for the mean comparison.** Use "According to fig.[#] the mean [variable] of [code] appears to be larger than the rest of the groups all of which have similar means." Frame the mean claim as visual ("appears to be"), never as significant.
5. **Close with the inferential test using a concession opener.** Use "While the [test] test did not reveal any significance of the data, …" OR "Based on the [test] test results there is no significant difference between the group's means." The concession opener is required when the figure looks suggestive; the plain verdict is used when the figure looks flat.
6. **(Optional) Bridge to the next variable.** End with an unfinished clause ("…, the") or a one-word transition so the next paragraph can re-open with the same "Variable: according to table [#]." structure — this is what creates the section's scannable rhythm.
