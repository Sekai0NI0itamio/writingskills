# Idea Flow Notes: chemistry_7_may2021_yg0Qxh5BeN1ukDx4 — A     Raw titration data

## Paragraph Flow (move by move)

**Paragraph 1 — Annotation convention note**

1. **Sentence 1 — claim (annotation rule).** Quote: *"overshoot titrations are indicated in red."* Hands to next sentence by raising the implicit question "what is done with these flagged values?" — so the reader expects a rule about treatment.
2. **Sentence 2 — specification (exclusion rule).** Quote: *"These are not accounted in calculations,"* Hands to next sentence by trailing a comma that leaves the corrective action unstated, forcing a consequence clause.
3. **Sentence 3 — implication (corrective action).** Quote: *"an additional titration will be done."* Hands to the next block (the first condition) because once data-handling is settled, the reader expects the actual measurements to begin.

**Paragraph 2 — "2g of salt, 10 min of electrolysis" block**

1. **Sentence 1 — context / parameter specification.** Quote: *"2g of salt, 10 min of electrolysis"*. Hands to next sentence by naming the independent-variable conditions that the following rows will report on.
2. **Sentence 2 — evidence (Sample 1 row).** Quote: *"Volume 9.8 9.7 9.5 9"*. Hands to next by completing one of three replicates, so the reader expects the next replicate.
3. **Sentence 3 — evidence (Sample 2 row).** Quote: *"Volume 9.2 8.6 8.9 8.9"*. Hands to next by being the second of three parallel replicates.
4. **Sentence 4 — evidence (Sample 3 row).** Quote: *"Volume 9.3 9.2 9.3 8.8"*. Hands to the next paragraph because the triplet is complete and a new condition label will reset the cycle.

**Paragraph 3 — "5g of salt, 3 min of electrolysis" block**

1. **Sentence 1 — parameter shift (new condition).** Quote: *"5g of salt, 3 min of electrolysis"*. Hands to next by changing only the electrolysis time, signalling a controlled-variable shift.
2. **S2 — evidence Sample 1:** *"Volume 12.2 11.9 12.3 12.1"*. → next replicate (cause: triplet pattern).
3. **S3 — evidence Sample 2:** *"Volume 10.1 10.3 10.1 10.2"*. → next replicate.
4. **S4 — evidence Sample 3:** *"Volume 11.7 11.6 11.7 11.5 11.6"*. → next block (a fourth trial appears, signalling an overshoot replacement per the opening rule).

**Paragraphs 4–11 — Remaining condition blocks ("5g of salt, 5/7/9/10/12/15/17/20 min of electrolysis")**

Each follows the identical four-move cycle:
1. **Parameter specification** ("5g of salt, *N* min of electrolysis") → hands off by signalling the single changed variable.
2. **Sample 1 evidence row** → hands off by completing one of three replicates.
3. **Sample 2 evidence row** → hands off by completing two of three.
4. **Sample 3 evidence row** → hands off either by completing the triplet (most blocks) or, when a fourth trial is present (e.g. Paragraph 5 Sample 1: *"23.8"* with trial 4 *"24.2 23.8"*; Paragraph 7 Sample 2 *"21.3 21.5 21.6"*; Paragraph 10 Sample 1 *"33.4 33.4 33.1"*), it visibly instantiates the "additional titration" rule from Paragraph 1 — consequence hand-off back to the annotation convention.

**Page markers (ii, iii, iv)** — transition devices: they signal consequence (running out of room) and reset the reader's eye to the top of the next condition.

---

## What This Section Does (content sequence)

The ordered moves a *raw data* section makes:

1. **Annotation convention first.** State any colour/flag convention and the treatment rule attached to it. *Why first:* every number on the page is read through this lens, so the reader must know how to interpret flagged values before meeting them.
2. **Independent-variable condition label.** Give mass + time (or whatever pair is varied). *Why next:* it fixes the context for the rows that follow, so numbers become comparable across blocks.
3. **Replicate set, in fixed order (1 → 2 → 3).** *Why this order:* it mirrors how the experiment was performed (sample-by-sample) and lets the reader visually scan a triplet before moving on.
4. **Loop the condition→triplet pattern across every independent-variable level.** *Why loop:* it builds a parallel structure so trends are visible at a glance.
5. **Page breaks between major groups.** *Why:* physical separation prevents mixing of conditions and gives the reader a "rest" point.

Generalisable sequence: **convention → parameter → replicate → next parameter → replicate …**

---

## Paragraph Skeletons (replicable templates)

### SKELETON A — Annotation convention opener

`SKELETON: "For all data, [flagged subset] are indicated in [marker]. [Subset] are not [excluded action], and [compensating step] will be done."`

1. **Slot 1 — "For all data,"**: scope word setting universal applicability. Grammatically a fronted prepositional phrase.
2. **Slot 2 — flagged subset**: name the type of result that warrants flagging (e.g. "overshoot titrations," "anomalous trials," "out-of-range absorbances").
3. **Slot 3 — marker**: a visual signal (e.g. "red," "an asterisk," "highlighted").
4. **Slot 4 — excluded action**: the calculation rule (e.g. "not accounted in calculations," "omitted from the mean").
5. **Slot 5 — compensating step**: the procedural fix (e.g. "an additional titration will be done," "the trial was repeated").

**Original fill (this text):** *"For all data, overshoot titrations are indicated in red. These are not accounted in calculations, and an additional titration will be done."*

**Demonstration fill (different idea — calorimetry):** *"For all data, anomalous temperature readings are indicated in red. These are not accounted in calculations, and an additional trial will be run to confirm the suspected value."*

---

### SKELETON B — Condition-label + replicate block

`SKELETON: "[Mass/volume] of [substance], [duration] of [process] / Titrations Trial 1 2 [3] / Volume [n₁] [n₂] [n₃] / [Sample 2] / [Sample 3]"`

1. **Slot 1 — condition label**: "[quantity] of [substance], [quantity] of [process]." Grammatically a noun phrase, no verb.
2. **Slot 2 — replicate table header**: a fixed "Titrations Trial 1 2 3" row.
3. **Slot 3 — replicate volume row**: a list of numerals separated by whitespace, one per trial.
4. **Slot 4 — sample label**: "Sample 1," "Sample 2," "Sample 3."
5. **Slot 5 — repetition**: slots 2–4 recur three times per block in fixed order.

**Original fill:** *"2g of salt, 10 min of electrolysis / Volume 9.8 9.7 9.5 9 / Volume 9.2 8.6 8.9 8.9 / Volume 9.3 9.2 9.3 8.8"*

**Demonstration fill (different idea — enzyme assay):** *"3 mL of substrate, 4 min of incubation / Volume 1.2 1.3 1.1 1.2 / Volume 1.0 1.1 0.9 1.0 / Volume 1.4 1.3 1.5 1.4"* — same fixed-vocabulary grid, different subject.

---

### SKELETON C — Page-transition marker

`SKELETON: "[lowercase Roman numeral], centred, alone on its line."`

1. **Slot 1 — Roman numeral**: indicates continuation ordering.

**Original fill:** *"ii," "iii," "iv"*

**Demonstration fill:** *"v, vi, vii"* — or any continued lowercase sequence; structure is the same.

---

## Express-Idea Vocabulary

The connectives/verbs this section actually uses, grouped by job:

- **Scope specification:** *"For all data,"* — universalises the rule before it is stated.
- **Treatment specification:** *"not accounted in calculations,"* — declares the exclusion rule for flagged values.
- **Compensating action (future tense):** *"an additional titration will be done."* — names the procedural fix that follows the exclusion.
- **Parameter-naming (no verb, bare noun phrase):** *"2g of salt,"* *"10 min of electrolysis"* — uses slash/comma pairing to encode two independent variables in one line.
- **Replication label (fixed string):** *"Titrations Trial 1 2 3"* — repeated verbatim to signal parallel structure.
- **Sample label (fixed string):** *"Sample 1,"* *"Sample 2,"* *"Sample 3"* — anchors which replicate set follows.

There are **no** contrast, cause/consequence, or specification connectives in this section — its logic is carried by **parallelism of layout**, not by prose glue words.

---

## How to Explain an Idea (replication steps)

This section is **data presentation, not idea explanation**, but it does run a tight four-step pattern. Replicating it:

1. **Open with the convention** — name the visual marker for non-standard results, declare the exclusion rule, name the compensatory action. (Pattern: flag → exclude → replace.)
2. **State the independent-variable condition as a bare noun phrase** — no verb, two quantities joined by a comma (mass + time, concentration + temperature, etc.). This fixes what the following numbers refer to.
3. **Replicate in fixed order** — repeat the same table skeleton three times (Sample 1, Sample 2, Sample 3). Do not reformat between replicates; consistency is the logic.
4. **Loop the condition→replicate pattern across every level of the independent variable**, varying only one quantity at a time. Insert a page break when a logical subgroup is complete.

The "explanation" the reader receives is **implicit**: by seeing the same layout repeated with one parameter shifted, the reader infers the dependent variable's response. The writer never states the trend — the layout does the work.
