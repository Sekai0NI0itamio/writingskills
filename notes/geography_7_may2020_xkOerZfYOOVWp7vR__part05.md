# Idea Flow Notes: geography_7_may2020_xkOerZfYOOVWp7vR — variable (x)                     variable (y)

## Paragraph Flow (move by move)

**Paragraph 1** (the only prose paragraph — the sentences directly after the calculation line).

- **Sentence 1 — composite move: state-result → state-threshold → binary-decision.**
  Quoted chunks: *"the Spearman's Rank Correlation Coefficient… is 0.57"* + *"the critical value for 24 ranks is 0.409"* + *"we can reject the null hypothesis of no correlation"*. The sentence delivers the computed statistic, sets the comparison benchmark, and uses the comparison ("As…is 0.57, and…is 0.409") to land on a yes/no decision. It hands to Sentence 2 because a "reject null" verdict logically requires a follow-up that names what is now accepted — the reader expects the alternative hypothesis to be spelled out.

- **Sentence 2 — implication move: translate-decision-into-substantive-claim.**
  Quoted chunks: *"This means we can accept the alternative hypothesis (H1)"* + *"i.e. there is a positive correlation between distance downstream and the hydraulic radius"*. The "This means" picks up the rejection from Sentence 1 as its cause and converts it into the substantive conclusion (a positive correlation). The "i.e." then re-states that conclusion in plain variable language, which is the natural closing move — no further sentence is needed because the chain is complete.

## What This Section Does (content sequence)

This is a **hypothesis-test conclusion** section, sitting directly under a worked calculation. The ordered moves are:

1. **Lead with the computed statistic value** — sets up the comparison the reader is about to be asked to make; without it the next move has nothing to anchor to.
2. **State the critical-value threshold** — gives the reader the cut-off against which the statistic will be judged; must come before the decision so the comparison is visible.
3. **Make the binary decision** (reject / fail-to-reject null) — this is the verdict the section exists to deliver, and it must follow once both numbers are on the page.
4. **Translate the verdict into the alternative hypothesis** — converts a statistical move into a science claim; logically forced by step 3, and is what the examiner is actually looking for.
5. **Restate the substantive finding in plain variable language** — closes the loop by naming the direction and the two variables involved, so the section ends on a concrete claim rather than on statistics jargon.

The WHY of the order: each move is only legible once the previous one is in place — a threshold without a statistic cannot be compared, a comparison without a threshold is unjustified, a decision without translation is hollow, and a translation without restatement leaves the variables unnamed.

## Paragraph Skeletons (replicable templates)

**Skeleton A — "statistic + threshold → reject → translate → restate" (full single-paragraph hypothesis-test closer).**
SKELETON: *"As the [test name] for [variable A] with respect to [variable B] is [stat value], and the critical value for [n] [units] is [critical value] (see [appendix]), we can reject the null hypothesis of no [relationship] at a [confidence]% confidence level. This means we can accept the alternative hypothesis (H1), i.e. there is [direction] [relationship] between [variable B] and [variable A]."*

1. *Slot contents and shape:* a noun-phrase test name; two variable names; a decimal statistic; an integer *n*; a decimal critical value; a reference label; a relational noun (correlation / association / difference); an integer confidence level; a direction word (positive / negative); a relational noun; two variable names.
2. *How to fill with a different idea:* pick a real dataset you have just ranked or computed; read the test statistic and critical value straight off your table; copy the structure but swap variable names and the relational noun (e.g. "no monotonic trend" instead of "no correlation"). Keep the "As… and…" fronting and the "This means" pivot — they are what makes the paragraph read as one logical chain.
3. *Original filled version:* *"As the Spearman's Rank Correlation Coefficient for the hydraulic radius with respect to distance downstream is 0.57, and the critical value for 24 ranks is 0.409 (see appendix c), we can reject the null hypothesis of no correlation at a 95% confidence level. This means we can accept the alternative hypothesis (H1), i.e. there is a positive correlation between distance downstream and the hydraulic radius."*
4. *Demonstration fill (different subject, same skeleton):* *"As the Spearman's Rank Correlation Coefficient for daily ice-cream sales with respect to maximum air temperature is 0.82, and the critical value for 14 ranks is 0.538 (see appendix B), we can reject the null hypothesis of no monotonic trend at a 95% confidence level. This means we can accept the alternative hypothesis (H1), i.e. there is a positive monotonic relationship between maximum air temperature and daily ice-cream sales."*

**Skeleton B — "two-statistic lead-in" (the fronted comparison clause on its own).**
SKELETON: *"As the [statistic A] for [variable 1] with respect to [variable 2] is [value], and the [statistic B] for [n] [units] is [value] (see [appendix])…"*

1. *Slot contents:* the name of the test just performed; two variables; the computed decimal; the name of the threshold (critical value, table value, *p*-value cut-off); an *n*; a decimal; an appendix tag.
2. *How to fill:* front-load both numbers in the same sentence so the comparison is visible; the clause must use "As…and…" parallelism so the reader reads the two numbers as paired, not as two separate facts. Always attach "(see appendix X)" to the threshold number, not to the computed statistic.
3. *Original filled version:* *"As the Spearman's Rank Correlation Coefficient for the hydraulic radius with respect to distance downstream is 0.57, and the critical value for 24 ranks is 0.409 (see appendix c)…"*
4. *Demonstration fill:* *"As the Mann-Whitney U statistic for the dry-weight of plants grown in shaded versus unshaded conditions is 12, and the critical value for 8 samples per group is 13 (see appendix D)…"*

## Express-Idea Vocabulary

- **Sequencing / pairing within one sentence:** *"As the Spearman's Rank Correlation Coefficient… is 0.57, and the critical value… is 0.409"* — the "As…and…" structure that forces the reader to read two numbers as one comparison.
- **Decision verb (the verdict):** *"we can reject the null hypothesis of no correlation"* — the explicit inferential verb that turns a comparison into a binary outcome.
- **Certainty quantifier attached to the verdict:** *"at a 95% confidence level"* — pinning the rejection to a named confidence figure so the claim is graded, not absolute.
- **Consequence connective (chains decision → interpretation):** *"This means we can accept the alternative hypothesis (H1)"* — the pivot that converts a statistical rejection into a substantive claim.
- **Specification / restatement marker:** *"i.e. there is a positive correlation between"* — re-states the formal hypothesis in plain variable language; functions as the section's closing plain-English line.
- **Relationship noun reused across the section:** *"null hypothesis of no correlation"* → *"positive correlation between distance downstream and the hydraulic radius"* — the same relational word recurs in the formal statement and the restated conclusion, so the reader can see the two are talking about the same claim.

## How to Explain an Idea (replication steps)

This section uses the **"compute → compare → decide → translate → restate"** pattern — a standard hypothesis-test conclusion pipeline. To replicate it on a new idea:

1. **Name the test you actually performed** (Spearman's, Mann-Whitney, chi-squared, *t*-test, etc.) and the two variables it was applied to. Open with *"As the [test name] for [var A] with respect to [var B] is [value]…"*.
2. **Insert the threshold number** in the same opening clause using *"and the critical value for [n] [units] is [value] (see appendix X)"* so the two numbers sit side by side. Do not put them in separate sentences — they must be read as one comparison.
3. **Issue the binary decision** in the same sentence, using the verb pair *"reject / fail to reject the null hypothesis"* and attach *"at a [X]% confidence level"* so the strength of the claim is explicit.
4. **Pivot with *"This means…"*** to begin a new sentence, and immediately state *"we can accept the alternative hypothesis (H1)"* — this is the move that turns a statistic into a science claim.
5. **Restate the substantive finding in plain language** using *"i.e. there is [positive / negative] [relationship word] between [var B] and [var A]"* — name the direction and the two variables one final time so the paragraph closes on a concrete claim rather than on jargon.
6. **Do not add a third sentence.** The chain ends at step 5; any further sentence would dilute the verdict.
