# Idea Flow Notes: mathematics_7_may2019_uwHSxRQY5IvK0u4D — graphical representation was created by adjusting the circle, semi-circle, the maximum height (y-axis) of this line

## Paragraph Flow (move by move)

**Paragraph 1** (parameter assignment)
- S1: "would provide us the radius." — **claim** (continuation fragment from prior line); declares what the preceding work yields.
- S2: "(θ = 2.968 (given)" — **evidence/specification**; pins the radius to a number.
- Hand to next: by landing on a numerical value, the next paragraph can *assign* this same value to a new variable.

**Paragraph 2** (variable set-up with reason)
- S1: "The value of θA is also same as radius" — **claim/definition**; equates a fresh parameter to the just-stated radius.
- S2: "as we want the circumference of the circle to lie on (0,0)" — **justification** (purpose clause); gives the geometric reason.
- S3: "not anywhere negative." — **specification/contrast**; sharpens the constraint.
- Hand to next: once the parameter is fixed *and* justified, the writer is licensed to **substitute** it back into the master equation.

**Paragraph 3** (equation display + worked derivation)
- S1: "Overall, following is the equation of the head" — **signposting/transition**; announces a consolidated result.
- S2: "after substituting the values back in." — **process marker**; explains where the equation came from.
- Equation line: "(x − 2.968)² + y² = 2.968²" — **evidence (substituted form)**; shows the populated model.
- "Rearranging:" — **transition**; cues the next algebraic move.
- Working: "y² = 2.968² − (x − 2.968)² = 2.968² − (x² − 5.936x + 8.809024) = 5.936x − x²" — **mechanism (derivation chain)**; step-by-step simplification.
- Hand to next: an explicit, checkable model now invites **empirical comparison** with what the software actually measured.

**Paragraph 4** (empirical check + discrepancy)
- S1: "As previously mentioned, the software provides dimensions for the shape created." — **callback/transition**; recycles a prior point.
- S2: "From this data, I am also come to aware that the ellipse is not a complete circle" — **discovery/claim**; new finding.
- S3: "and it is transformed slightly to match the outline." — **mechanism**; explains why the shape deviates.
- S4: "According to the software, width of the circle is 5.764cm, and height is 2.968cm." — **evidence (numerical data)**; supplies the dimensions.
- Hand to next: with discrepancy flagged *and* width known, the next paragraph can launch the **fix-up calculation**.

**Paragraph 5** (next-step announcement)
- S1: "Dividing the width by 2 will give enough information to find out the scale factor." — **procedure claim**; commits to the follow-up move.
- (Section ends — no further hand-off.)

## What This Section Does (content sequence)

This is a **mathematical modelling + verification** micro-section. The ordered moves are:

1. **State the given parameter** (radius = 2.968). *Why first:* every later substitution needs this anchor.
2. **Assign that parameter to a set-up variable, justifying with a geometric constraint.** *Why:* locks down the model before algebra begins.
3. **Substitute into the general equation.** *Why:* produces a concrete, testable form.
4. **Rearrange algebraically to explicit (solved) form.** *Why:* makes the curve directly comparable to data.
5. **Recall the software's measured dimensions.** *Why:* provides the empirical benchmark.
6. **Recognise the deviation** (ellipse, not circle). *Why:* names the gap between model and reality.
7. **Announce the next calculation** (scale factor via width ÷ 2). *Why:* sets up the section that resolves the deviation.

The order is **strictly downstream**: each output is the prerequisite input of the next. A student replicating this with a different shape (e.g. a parabola for projectile motion) would follow the same seven-move chain.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Variable justification paragraph**
"The value of [PARAM] is also same as [SOURCE], as we want [GEOMETRIC CONDITION]. [CONSTRAINT DETAIL]."

1. **Slot 1** `[PARAM]` — a single-letter or short-named variable; noun phrase.
   *Fill with a different idea:* pick a fresh variable from your own equation (e.g. *k*, *h₀*) that must inherit a previously given value.
2. **Slot 2** `[SOURCE]` — the original measured/given quantity.
   *Fill:* state the numerical value or expression already established (e.g. *the maximum height, 4.2 m*).
3. **Slot 3** `[GEOMETRIC CONDITION]` — purpose clause starting "as we want…".
   *Fill:* name where on the diagram the relevant feature must sit (e.g. *the vertex to lie on the x-axis*).
4. **Slot 4** `[CONSTRAINT DETAIL]` — a negation or sharpening clause.
   *Fill:* add a negative bound or extra precision (e.g. *not below the launch point*).

**Original fill:** "The value of θA is also same as radius, as we want the circumference of the circle to lie on (0,0), not anywhere negative."

**Demonstration fill (different subject, same skeleton):** "The value of *k* is also the same as the launch height, as we want the parabola's vertex to lie on the x-axis, not below the ground."

---

**SKELETON B — Equation display + rearrangement paragraph**
"Overall, following is the equation of [OBJECT] after [PROCESS]. [SUBSTITUTED EQUATION]. Rearranging: [STEP 1] = [STEP 2] = [STEP 3]."

1. **Slot 1** `[OBJECT]` — the named curve/shape; noun.
2. **Slot 2** `[PROCESS]` — gerund phrase explaining what was done (e.g. *substituting the values back in*).
3. **Slot 3** `[SUBSTITUTED EQUATION]` — the equation with numbers plugged in, displayed on its own line.
4. **Slot 4** `[STEP 1 = STEP 2 = STEP 3]` — a chained algebraic simplification written with `=` signs.

**Original fill:** "Overall, following is the equation of the head after substituting the values back in. (x − 2.968)² + y² = 2.968². Rearranging: y² = 2.968² − (x − 2.968)² = 2.968² − (x² − 5.936x + 8.809024) = 5.936x − x²."

**Demonstration fill:** "Overall, following is the equation of the trajectory after substituting the launch height back in. y = −0.05(x − 4)² + 3. Rearranging: y = −0.05(x² − 8x + 16) + 3 = −0.05x² + 0.4x − 0.8 + 3 = −0.05x² + 0.4x + 2.2."

---

**SKELETON C — Empirical comparison + discrepancy paragraph**
"As previously mentioned, the [TOOL] provides [DATA TYPE] for the shape created. From this data, I am also come to aware that [DISCOVERY], and [REASON]. According to the [TOOL], [MEASUREMENT 1], and [MEASUREMENT 2]."

1. **Slot 1** `[TOOL]` — software/instrument name; proper noun.
2. **Slot 2** `[DATA TYPE]` — what the tool outputs (e.g. *dimensions*).
3. **Slot 3** `[DISCOVERY]` — a surprise about the modelled shape.
4. **Slot 4** `[REASON]` — why the shape isn't exactly what was modelled.
5. **Slots 5–6** `[MEASUREMENT 1]`, `[MEASUREMENT 2]` — paired numerical values.

**Original fill:** "As previously mentioned, the software provides dimensions for the shape created. From this data, I am also come to aware that the ellipse is not a complete circle, and it is transformed slightly to match the outline. According to the software, width of the circle is 5.764cm, and height is 2.968cm."

**Demonstration fill:** "As previously mentioned, the tracker provides coordinates for the path plotted. From this data, I am also come to aware that the arc is not a true parabola, and it is stretched slightly by air resistance. According to the tracker, horizontal range is 7.2 m, and peak height is 2.8 m."

---

**SKELETON D — Forward-pointing procedure sentence**
"[OPERATION] will give enough information to find out [TARGET QUANTITY]."

1. **Slot 1** `[OPERATION]` — a gerund arithmetic move (dividing, subtracting, halving).
2. **Slot 2** `[TARGET QUANTITY]` — the unknown to be resolved next.

**Original fill:** "Dividing the width by 2 will give enough information to find out the scale factor."

**Demonstration fill:** "Subtracting the theoretical range from the measured range will give enough information to find out the drag coefficient."

## Express-Idea Vocabulary

**Sequencing / signposting**
- "Overall, following is" — "Overall, following is the equation of the head"
- "Rearranging:" — "Rearranging:" (own-line cue)

**Transition / callback**
- "As previously mentioned" — "As previously mentioned, the software provides dimensions"
- "after substituting the values back in" — "Overall, following is the equation of the head after substituting the values back in"

**Cause / justification**
- "as we want" — "as we want the circumference of the circle to lie on (0,0)"

**Constraint specification**
- "not anywhere negative" — "not anywhere negative."

**Evidence handling**
- "(θ = 2.968 (given)" — "(θ = 2.968 (given)"
- "According to the software" — "According to the software, width of the circle is 5.764cm"

**Discovery / finding verbs**
- "I am also come to aware that" — "I am also come to aware that the ellipse is not a complete circle"

**Procedure verbs**
- "Dividing the width by 2" — "Dividing the width by 2 will give enough information"
- "substituting the values back in" — "after substituting the values back in"

## How to Explain an Idea (replication steps)

**Pattern name:** *Parameter-anchored substitution → algebraic simplification → empirical check → discrepancy → forward step.*

This is a **worked derivation chained to a sanity-check**, then pointed forward. To reproduce it on a NEW idea (any curve fit: parabola, sine wave, exponential decay):

1. **Lock in the anchor number** — state the single given measurement (e.g. *max height = 4.2 m*) in one short clause.
2. **Bind a fresh variable to that number** using a *purpose clause* ("as we want the vertex to…"); add one sharpening detail ("not below the origin").
3. **Substitute** the numerical value into the general equation and display the populated equation on its own line.
4. **Rearrange** with the word "Rearranging:" and chain three `=` signs showing expansion → simplification → final explicit form.
5. **Recall** the empirical tool's output ("As previously mentioned, the [tool] provides…") and **report two paired measurements** ("width is X, and height is Y").
6. **Name the deviation** ("I am also come to aware that the curve is not a perfect [shape]") and **give the mechanism** for it.
7. **Forward-point** the next calculation ("[Operation] will give enough information to find out [next quantity]") so the reader sees what resolves the deviation.
