# Idea Flow Notes: mathematics_7_may2020_2SyPx094JfmxwKa1 — To calculate the perimeter of the maple leaf Fourier series, I tried doing the computation by plugging in all the

## Paragraph Flow (move by move)

**Paragraph 1** (7 sentences, last one cut off)

1. **Sentence 1** — "terms calculated using the DFT."
   - Move: **context carry-over** (a stranded phrase picking up the previous paragraph's method).
   - Hand-off: because the previous method is being continued, the reader expects a limitation or refinement next.

2. **Sentence 2** — "However, the queries didn't work well since there were so many terms, so I wrote a program using WolframScript..."
   - Move: **contrast + cause + remedy** (However → since → so).
   - Hand-off: states a failed attempt and the replacement tool; the next sentence must give what that tool produced (consequence).

3. **Sentence 3** — "The perimeter of the maple leaf was calculated to be 5404.17 ≈ 5400."
   - Move: **result** of the remedy just announced.
   - Hand-off: bare number is meaningless on its own, so the next sentence must supply a reference frame (specification/justification).

4. **Sentence 4** — "Although this result does not have any units, for a reference, the largest circle in Fig. 11 had a radius of 939.34 ≈ 900 and a circumference of 5902.06 ≈ 5900."
   - Move: **concession + contextual benchmark** (Although → for a reference, here are the comparison numbers).
   - Hand-off: two comparable figures are now on the table; the next sentence must combine them into a derived ratio (mathematical consequence).

5. **Sentence 5** — "This result means that maple leaf has a perimeter with a ratio of ... ≈ 91.6% relative to the largest circle..."
   - Move: **implication** — the ratio computed from the two benchmarks.
   - Hand-off: a 91.6% figure begs a "so what" anchored back to theory, so the next sentence returns to a previously stated principle.

6. **Sentence 6** — "As aforementioned, the more terms that are calculated in the Fourier series, the better the Fourier series represents the original function."
   - Move: **callback to principle** (As aforementioned) — re-anchors the empirical result in theory.
   - Hand-off: a principle is restated, so the next sentence must apply it back to the just-computed result (implication/specification).

7. **Sentence 7** — "Such a result provides a"
   - Move: **incomplete lead-in** — handing the implication forward into the next section.

---

## What This Section Does (content sequence)

This is a **computational-results section** that converts a raw calculation into a defended, comparable finding. The ordered moves are:

1. **Acknowledge the prior tool and its failure** — names what was tried and why it broke (sets up the need for a new tool).
2. **Introduce the substitute method** — new program, software, or procedure, justified by the failure above (so the reader trusts the new number).
3. **State the raw numerical result** — the headline value (this is the "what I got").
4. **Caveat + supply a reference benchmark** — admits the number lacks units/context, then introduces a comparable quantity from a known figure (turns a meaningless number into a meaningful one).
5. **Derive an interpretive ratio** — computes the percentage or ratio between the result and the benchmark (gives the reader something to *understand*).
6. **Re-anchor in a previously stated principle** — pulls back from the number to a theoretical claim already established (validates that the number fits theory).
7. **Open the implication** (cut off here) — begins to say what the validated number proves or supports.

**Why this order?** A raw number is uninterpretable: the writer must (a) earn trust in the method (1→2), (b) deliver the number (3), (c) make it comparable (4→5), and only then (d) tie it back to theory (6) and forward to a claim (7). Skipping any step leaves the reader either unconvinced or lost.

---

## Paragraph Skeletons (replicable templates)

### Skeleton A — "Failed method → substitute tool → headline result"

SKELETON: "[Previous approach] didn't work well since [specific limitation], so I [alternative tool/method] to [target quantity]. The [target quantity] was calculated to be [raw value] ≈ [rounded value]."

1. **Slot 1 (acknowledged failing approach + cause)**: short noun phrase naming the old method, followed by "didn't work well since [concrete reason]" (past tense, one specific bottleneck).
2. **Slot 2 (substitute tool + target)**: "so I [verb] using [tool] to [compute X]" — past tense, names the software/technique and the quantity sought.
3. **Slot 3 (headline numerical result)**: "The [quantity] was calculated to be [precise] ≈ [rounded]" — past passive, exact value plus a rounded companion.

**Original fill**: "queries didn't work well since there were so many terms, so I wrote a program using WolframScript to calculate the perimeter of the maple leaf. The perimeter of the maple leaf was calculated to be 5404.17 ≈ 5400."

**Demonstration fill (different idea — physics, not math)**:
"*Manual integration of the pendulum equation* didn't work well since the ODE is non-elementary, so I switched to a Runge–Kutta 4 script in Python to model the swing angle over time. The maximum angular displacement was computed to be 38.742° ≈ 39°."

---

### Skeleton B — "Unitless result → reference benchmark → derived ratio"

SKELETON: "Although this result does not have [unit/context], for a reference, the [reference object] in [Fig/Table] had a [property] of [value]. This result means that [subject] has a [quantity] with a ratio of [ratio] ≈ [percentage]% relative to the [reference]."

1. **Slot 1 (concession on units)**: "Although this result does not have [units]," — concession connective + admission of absent dimension.
2. **Slot 2 (reference benchmark)**: "for a reference, the [named object] in [Fig X] had a [property] of [precise] ≈ [rounded]" — present-perfect of *had*, single comparable figure.
3. **Slot 3 (derived percentage interpretation)**: "This result means that [subject] has a [quantity] with a ratio of [X/Y] ≈ [%]% relative to the [reference]" — *means that* + ratio + percentage.

**Original fill**: "Although this result does not have any units, for a reference, the largest circle in Fig. 11 had a radius of 939.34 ≈ 900 and a circumference of 5902.06 ≈ 5900. This result means that maple leaf has a perimeter with a ratio of ... ≈ 91.6% relative to the largest circle in its Fourier series."

**Demonstration fill (different idea — biology)**:
"Although this result does not have any time units, for a reference, the untreated control in Fig. 4 had a half-life of 142.6 min ≈ 140 min. This result means that the catalysed reaction has a decay constant with a ratio of 0.347 ≈ 34.7% relative to the untreated control in its decay profile."

---

### Skeleton C — "Callback to principle → forward implication (incomplete)"

SKELETON: "As aforementioned, [principle statement restated in plain words]. Such a result provides a [forward implication]..."

1. **Slot 1 (principle callback)**: "As aforementioned, the more [X] that are [done/varied], the [better/more accurate] the [model/result] [does Y]" — uses *As aforementioned*, restates a monotonic or directional relationship.
2. **Slot 2 (implication lead-in, cut off)**: "Such a result provides a [claim direction]" — incomplete by design, hands to the next paragraph.

**Original fill**: "As aforementioned, the more terms that are calculated in the Fourier series, the better the Fourier series represents the original function. Such a result provides a..."

**Demonstration fill (different idea — statistics)**:
"As aforementioned, the larger the bootstrap sample size, the tighter the confidence interval brackets the true population mean. Such a result provides a..."

---

## Express-Idea Vocabulary

**Sequencing / cause-consequence**
- *However* — "However, the queries didn't work well since there were so many terms..." (signals method switch after failure)
- *so* (consequence) — "...so I wrote a program using WolframScript..." (logical result of the limitation)
- *since* — "...didn't work well since there were so many terms..." (cause clause)

**Concession / specification**
- *Although* — "Although this result does not have any units, for a reference, the largest circle..." (admits weakness before supplying a benchmark)
- *for a reference* — same sentence (introduces comparative anchor)

**Implication / evidence handling**
- *This result means that* — "This result means that maple leaf has a perimeter with a ratio of..." (turns numbers into a claim)
- *Such a result* — "Such a result provides a..." (points the empirical number toward its theoretical payoff)
- *As aforementioned* — "As aforementioned, the more terms that are calculated..." (re-anchors in earlier theory)

**Explanation / computational verbs**
- *was calculated to be* — "The perimeter of the maple leaf was calculated to be 5404.17..." (passive report of a tool's output)
- *had a radius of / had a circumference of* — "the largest circle... had a radius of 939.34..." (reports benchmark property)

---

## How to Explain an Idea (replication steps)

This section relies on the **"computational result with theoretical re-anchoring"** pattern: a raw measurement is earned, contextualized, ratio'd, and then tied to a previously stated principle.

**Steps to reproduce with a new idea:**

1. **Name the previous approach and its bottleneck** — "My [old method] didn't work well since [specific limit], so I switched to [new tool]." One sentence, past tense, one concrete failure reason.
2. **State the headline number** — Passive construction: "The [quantity] was calculated to be [exact] ≈ [rounded]." Always pair an exact value with a rounded companion.
3. **Concede the number's weakness** — "Although this result does not have [units/dimension]..." Use *Although* to acknowledge the limit before defending the number.
4. **Supply one reference benchmark from a labelled figure** — "...for a reference, the [reference object] in [Fig. X] had a [property] of [exact] ≈ [rounded]." One comparable object only.
5. **Derive the ratio/percentage** — "This result means that [subject] has a [quantity] with a ratio of [X/Y] ≈ [%]% relative to the [reference]." Use *means that* + explicit ratio.
6. **Callback to an earlier principle** — "As aforementioned, [direction claim about the phenomenon]." Restate a monotonic relationship already defended upstream.
7. **Open the implication** — "Such a result provides a [forward claim]..." (this is where the next section picks up).
