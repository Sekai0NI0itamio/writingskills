# Idea Flow Notes: mathematics_7_november2016_6jvDzQbdmBzKpwM1 — Substituting this result in,

## Paragraph Flow (move by move)

**Paragraph 1**
- Sentence 1 (the displayed equation pair): "ln |𝐷| + 𝑐1 = − ln ∣𝑣h (cos 𝜃 − 1)(cos 𝜃 + 1)∣ − ∫ d cos 𝜃" — *presents the substituted starting form*. Hands off by **specification**: the integral and log-of-product are the two objects that need immediate unpacking.
- Sentence 2 (second displayed equation): "ln |𝐷| + 𝑐1 = − ln ∣𝑣h ∣|cos 𝜃 − 1||cos 𝜃 + 1| − ∫ d cos 𝜃" — *rewrites the absolute value of a product as separate absolute values*. Hands off by **consequence**: now that the product is split, each log can be expanded individually.

**Paragraph 2**
- Sentence 1 (line 3 equation): "ln |𝐷| + 𝑐1 = − ½ ln ∣𝑣h ∣ − ½ ln |cos 𝜃 − 1| − ½ ln |cos 𝜃 + 1| − (𝑣r)/(2𝑣h) ∫ d cos 𝜃" — *applies log rules to expand the product*. Hands off by **gap recognition**: the absolute value bars and the constant factor now need justifying.

**Paragraph 3**
- Sentence 1 (conditions clause): "Since 𝑣h > 0, 𝐷 ≥ 0 and −1 ≤ cos 𝜃 ≤ 1, we can simplify the absolute value operations" — *states the domain assumptions that license the next line*. Hands off by **authorisation**: given those conditions, the bars can be dropped, so the equation is rewritten.
- Sentence 2 (line 4 equation): "ln 𝐷 + 𝑐1 = − ½ ln 𝑣h − ½ ln (1 − cos 𝜃) − ½ ln (1 + cos 𝜃) − (𝑣r)/(2𝑣h) ln (1 − cos 𝜃) + (𝑣r)/(2𝑣h) ln (1 + cos 𝜃)" — *removes absolute value bars and re-signs the trig terms*. Hands off by **collection**: like terms involving (1 ± cos θ) are now visible and ready to be grouped.

**Paragraph 4**
- Sentence 1 (line 6 equation): "ln 𝐷 + 𝑐2 = (𝑣r/(2𝑣h) − ½) ln (1 + cos 𝜃) − (𝑣r/(2𝑣h) + ½) ln (1 − cos 𝜃) (𝑐2 = 𝑐1 + ln 𝑣h)" — *collects like log terms into two combined coefficients and absorbs a constant into c₂*. Hands off by **termination**: this is the final tidy form — there is no next sentence because the section ends here.

## What This Section Does (content sequence)

This section is a **post-substitution simplification block** in a derivation. The ordered content moves are:

1. **Restate the substituted equation** — what was just produced by the substitution needs to be on the page so the reader sees what is being manipulated.
2. **Apply log-arithmetic identities to split the product** — log of a product becomes a sum; log of a power brings down the exponent. This is *why* it comes next: the next move cannot be done until the single log is decomposed.
3. **State the domain/positivity assumptions that license the next algebraic step** — the conditions justify removing absolute values. They *must* precede the simplification because the rewrite would be unjustified without them.
4. **Drop absolute values, re-sign trig factors, and absorb constants** — the actual simplification step the conditions authorised.
5. **Collect like terms and rename the constant** — the closing aesthetic move, producing the compact final line.

**Why this order works:** each move is the *prerequisite* for the next — you cannot split logs before applying the rule, cannot drop bars before stating the sign assumption, cannot collect terms before they exist as separate logs. This is a linear dependency chain, not a parallel exposition.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Conditions-justified rewriting"** (the conditions paragraph)

> [Quantity A] > 0, [Quantity B] ≥ 0 and [range for variable], we can [simplify the absolute value operations / drop the bars / remove the modulus]. [rewritten equation]

1. **Slot 1** — three independent sign/range facts (two positivity statements + one closed interval), separated by commas. Grammatically: noun phrase + inequality + "and" + inequality + "and" + inequality.
2. **Slot 2** — a one-clause statement of what those facts permit the writer to do. Grammatically: "we can" + bare infinitive verb phrase.
3. **Slot 3** — the rewritten expression that uses the licence from slot 2.

**How to fill it with a different idea:** pick any derivation where modulus/absolute-value notation is currently awkward. Identify the three facts that make the modulus redundant (e.g. "x > 0, y² ≥ 0, 0 ≤ sin φ ≤ 1"). State them in the same order — *positive constant first, then a squared/non-negative term, then a bounded trig range*. Then write the permitted simplification.

**Original filled version:** "Since 𝑣h > 0, 𝐷 ≥ 0 and −1 ≤ cos 𝜃 ≤ 1, we can simplify the absolute value operations."

**Demonstration fill:** "Since *k* > 0, *E²* ≥ 0 and 0 ≤ sin φ ≤ 1, we can drop the absolute value signs." Followed by the rewritten equation without bars.

---

**SKELETON B — "Product-to-sum log expansion"** (the second paragraph)

> ln|[combined product of constants and trig terms]| + c₁ = [distribution of the leading coefficient across each log factor, as separate terms, including any power that came down from the exponent], with the integral term carried along verbatim

1. **Slot 1** — a single logarithm of a product (one constant factor × two or more trig factors), with the original constant c₁.
2. **Slot 2** — the same expression rewritten using ln(ab) = ln a + ln b (and a·ln b = ln bᵃ), distributing any prefactor.

**How to fill it with a different idea:** take any composite expression of the form ln|A · f(x) · g(x)|. Apply the product rule term by term. If there is an overall coefficient on the original log, write it in front of *each* new log term.

**Original filled version:** "ln |𝐷| + 𝑐1 = − ½ ln ∣𝑣h ∣ − ½ ln |cos 𝜃 − 1| − ½ ln |cos 𝜃 + 1| − (𝑣r)/(2𝑣h) ∫ d cos 𝜃"

**Demonstration fill:** Starting from ln|A · sin x · cos x| + c, write it as ln|A| + ln|sin x| + ln|cos x| + c, then distribute a leading ½: "ln P + c₁ = ½ ln|A| + ½ ln|sin x| + ½ ln|cos x| + c₁."

---

**SKELETON C — "Final regrouping with absorbed constant"** (the closing paragraph)

> ln [output] + c₂ = [(combined coefficient of first log) ln (first trig term)] ± [(combined coefficient of second log) ln (second trig term)]  (c₂ = c₁ + [absorbed quantity])

1. **Slot 1** — a log expression on the LHS whose constant has been renamed c₂.
2. **Slot 2** — the LHS log coefficient written as a single combined coefficient times the first log.
3. **Slot 3** — a second combined coefficient times the second log, with the appropriate sign.
4. **Slot 4** — a parenthetical defining the new constant in terms of the old one and the absorbed quantity.

**How to fill it with a different idea:** identify two log terms on the LHS that share the same trig argument and add their coefficients; do the same for the second trig argument. Rename the constant to absorb any pulled-out factors.

**Original filled version:** "ln 𝐷 + 𝑐2 = (𝑣r/(2𝑣h) − ½) ln (1 + cos 𝜃) − (𝑣r/(2𝑣h) + ½) ln (1 − cos 𝜃) (𝑐2 = 𝑐1 + ln 𝑣h)"

**Demonstration fill:** "ln N + c₂ = (a − ½) ln(x + 1) + (b − ½) ln(x − 1)  (c₂ = c₁ + ½ ln k)"

## Express-Idea Vocabulary

- **Sequencing / linear continuation:** none used — the section progresses equation-to-equation without temporal connectives, which is appropriate for algebraic manipulation.
- **Authorisation / licensing:** "Since ... we can simplify" — "Since 𝑣h > 0, 𝐷 ≥ 0 and −1 ≤ cos 𝜃 ≤ 1, we can simplify the absolute value operations." (This is the section's main connective; it carries all the justification load.)
- **Implicit cause (via juxtaposition):** writing the expanded equation directly below the product-form equation — the reader is meant to infer "because the log rules apply, therefore this rewriting is valid." No verbal cause marker; the *vertical layout* does the causal work.
- **Specification / clarification:** the parenthetical "(𝑐2 = 𝑐1 + ln 𝑣h)" — defines a new symbol in terms of an old one.
- **Definition-by-renaming:** "ln |𝐷|" becoming "ln 𝐷" after the conditions clause — the same object, redefined by removing notation.
- **Explanation verbs (implied through structure):** "simplify" — used as the action verb whose justification is the conditions clause. No "defined as", "modelled by", or "explained by" appears; the section is manipulation, not exposition.

## How to Explain an Idea (replication steps)

The pattern this section relies on is **algebraic consequence chain with explicit licence**: each rewrite is licensed by either an identity (log rules) or an assumption (domain/sign), and the licence is named either implicitly (by vertical layout) or explicitly (by a "since" clause).

**Step-by-step instructions to apply this to a NEW derivation:**

1. **Start with a complex single-term expression** (one log, one fraction, one modulus) that contains a product, a power, or an awkward sign. This is the *thing to be unpacked*.
2. **State the identity you are about to apply, by silent demonstration.** Show the original on top, the rewritten form immediately below. The reader infers the rule from the side-by-side. Do not narrate "we now use the product rule" — let the layout speak.
3. **If the next step requires assumptions (sign, domain, positivity), write them explicitly as a "Since … , we can …" clause before the rewrite.** This is the *licence step*. Always place it *between* the expanded form and the simplified form, never after.
4. **Perform the licensed rewrite** (drop bars, absorb constants, factor out). Place it directly beneath the licence clause so the visual chain is: *conditions → rewrite*.
5. **Collect like terms into a compact final form.** If renaming the integration/summation constant is necessary, define the new constant parenthetically at the end of the same line.
6. **Stop.** Do not add a verbal summary; the final tidy equation *is* the summary.

This pattern — *restate → apply identity (silent) → state licence → licensed rewrite → collect → stop* — is the entire logic architecture of the section, and it transfers cleanly to any derivation where each manipulation needs a stated or visible warrant.
