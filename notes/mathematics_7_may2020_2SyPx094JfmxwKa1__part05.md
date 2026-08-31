# Idea Flow Notes: mathematics_7_may2020_2SyPx094JfmxwKa1 — Example of a Calculation for the Fourier Series

## Paragraph Flow (move by move)

**Paragraph 1**
1. "Let us take these concepts and apply it to a real-life example." — **transition/framing claim** (shift from theory to application). Hands the reader to the next sentence by *announcing* that a concrete instance will be supplied.
2. "Below (Fig. 2) is an image of a maple leaf, which is a suitable image for Fourier epicycles to trace out as the figure has a clear outline." — **example + justification move** (picks the object and gives the reason). Hands the reader by *supplying* the promised example and a qualifier, so the next sentence can act on it.
3. "Before plotting the whole leaf, let us zoom into a corner of the figure (as shown in Fig. 3) and derive the trigonometric Fourier series of the curve." — **scope-narrowing / procedure announcement**. Hands the reader by *restricting* the task to a sub-portion, setting up the geometric description that follows.

**Paragraph 2**
1. "The zoomed in portion of the figure is a triangle with a height-to-width ratio of roughly 1:1." — **specification** (geometric description of the sub-portion). Hands the reader by *characterising* the shape, so a coordinate placement becomes meaningful.
2. "The outline of the triangle is then plotted onto a plane with an arbitrary unit axis, as shown in Fig. 4." — **procedural step / coordinate-setup move**. Hands the reader by *placing* the shape on axes, so the geometric object can now be converted to algebra.

**Paragraph 3**
1. "This curve represents a piecewise function with the formula 𝑓(𝑡) = {2𝑡+2, −2𝑡+2}." — **definition / formalisation move** (geometry → formula). Hands the reader by *converting* the picture into a mathematical object that can be reasoned about.
2. "The Fourier series would trace out a similar function that is repeated periodically and infinitely along the x-axis." — **implication move** (states what the Fourier series does). Hands the reader by *forecasting* the outcome so a property check can be applied next.
3. "Since the function 𝑓(𝑡) is an even function, the Fourier series is a Fourier cosine series, in which the terms 𝑏ₙ are all equal to 0, and a proof will be shown in the next section." — **mechanism / cause→consequence move**. Hands the reader by *flagging deferral* ("proof… next section") so the present paragraph only carries the consequence, not the working.
4. "𝑓(𝑡) is piecewise continuous as both 𝑓(𝑡) = 2𝑡 + 2 and 𝑓(𝑡) = −2𝑡 + 2 are continuous, and" — **evidence / prerequisite-check move**. Hands the reader by *justifying* a precondition required for the Fourier series to apply.

---

## What This Section Does (content sequence)

This is a **worked-example introduction** sitting between theory and a derivation. Its content moves in this order:

1. **Theory → practice pivot** — signals "we now apply what was defined."
2. **Object choice + visual justification** — picks a concrete figure (maple leaf) and gives a *reason* (clear outline).
3. **Scope narrowing** — reduces the figure to a tractable sub-portion (corner/triangle).
4. **Geometric description** — names the shape and its proportions.
5. **Coordinate placement** — moves from picture to axes so algebra can follow.
6. **Mathematical definition** — writes the curve as a piecewise function.
7. **Implication statement** — describes what the Fourier series will produce (periodic repetition).
8. **Symmetry → simplification mechanism** — uses "even" to deduce cosine series and zero bn terms.
9. **Forward signposting** — defers proof to next section so this section stays clean.
10. **Prerequisite verification** — confirms piecewise continuity to licence the Fourier series.

**Why this order:** each move sets up the *thing* the next move needs. The example needs an object; the object needs a reason; the reason needs a tractable slice; the slice needs geometric description; the description needs axes; the axes need a formula; the formula needs a property check (symmetry); the property check needs its proof deferred; and finally a continuity check *closes the loop* on whether Fourier analysis is even valid here.

---

## Paragraph Skeletons (replicable templates)

### Skeleton A — "Pivot + object choice + scope narrow"

**SKELETON:** "Let us take these concepts and apply [it] to a real-life example. Below ([Fig. X]) is an image of a [object], which is a suitable image for [method] to trace out as the figure has a [qualifier]. Before [whole task], let us [narrowed sub-task] (as shown in [Fig. Y]) and [derive the X] of the [curve]."

1. **Slots:**
   - Slot 1: pivot sentence ("let us take…") — imperative, addresses the reader.
   - Slot 2: object + figure pointer + reason clause ("which is a suitable…") — noun + non-restrictive relative.
   - Slot 3: scope-narrowing sentence ("Before…, let us…") — uses "Before" + "let us" to shrink the task.
2. **How to fill with a different idea:** Pick a concrete, visually-clearly-outlined object; justify it with a one-word visual property; then state *which sub-part* you will analyse and *what* you will derive from it.
3. **Original:** "Let us take these concepts… maple leaf… Fourier epicycles… clear outline. Before plotting the whole leaf, let us zoom into a corner… derive the trigonometric Fourier series of the curve."
4. **Demo fill (different idea):** "Let us take these concepts and apply them to a real-life example. Below (Fig. 2) is an ECG trace, which is a suitable signal for Fourier analysis as the trace has a repeating waveform. Before analysing the full heartbeat, let us isolate one P-QRS segment (as shown in Fig. 3) and derive the trigonometric Fourier series of the pulse."

---

### Skeleton B — "Geometric description + coordinate placement"

**SKELETON:** "The zoomed in portion of the figure is a [shape] with a [property]-to-[property] ratio of roughly [X:Y]. The outline of the [shape] is then plotted onto a plane with an arbitrary unit axis, as shown in [Fig. Z]."

1. **Slots:**
   - Slot 1: shape-naming clause ("is a triangle…") — copula + shape noun + ratio phrase.
   - Slot 2: coordinate-placement clause ("is then plotted onto…") — passive + "then" sequencing marker + figure pointer.
2. **How to fill with a different idea:** Name the sub-shape you extracted, give one numeric proportion to anchor it, then announce that it has been placed on (x,y) axes with an arbitrary unit so the reader can map shape → formula.
3. **Original:** "The zoomed in portion of the figure is a triangle with a height-to-width ratio of roughly 1:1. The outline of the triangle is then plotted onto a plane with an arbitrary unit axis, as shown in Fig. 4."
4. **Demo fill (different idea):** "The zoomed in portion of the trace is a single sine pulse with a peak-to-trough ratio of roughly 1:1. The outline of the pulse is then plotted onto a plane with an arbitrary unit axis, as shown in Fig. 4."

---

### Skeleton C — "Definition + implication + symmetry-mechanism + deferral"

**SKELETON:** "This curve represents a [type] with the formula [f(t)=…]. The Fourier series would trace out a [property] that is repeated [adverb] along the [axis]. Since the function [property], the Fourier series is a [special series], in which [terms] are all equal to [0], and [deferral]."

1. **Slots:**
   - Slot 1: formal definition ("represents a piecewise function") — present tense, demonstrative "this."
   - Slot 2: behavioural claim ("would trace out a similar function…") — modal "would" + repetition descriptor.
   - Slot 3: mechanism ("Since …, the Fourier series is a cosine series…") — "Since" + symmetry property → consequence.
   - Slot 4: zeroing of terms ("in which bₙ = 0") — parenthetical clarification.
   - Slot 5: deferral ("a proof will be shown in the next section") — forward signposting.
2. **How to fill with a different idea:** After defining your piecewise/segmented function, predict what the Fourier series does, then identify *one* symmetry or property (even, odd, periodic, bounded) that simplifies the series, name which coefficients vanish, and explicitly defer the proof.
3. **Original:** "This curve represents a piecewise function… The Fourier series would trace out a similar function that is repeated periodically and infinitely along the x-axis. Since the function 𝑓(𝑡) is an even function, the Fourier series is a Fourier cosine series, in which the terms 𝑏ₙ are all equal to 0, and a proof will be shown in the next section."
4. **Demo fill (different idea):** "This curve represents a square-wave function with the formula 𝑔(𝑡) = sgn(sin 𝑡). The Fourier series would trace out a stepped function that is repeated periodically and symmetrically along the t-axis. Since the function 𝑔(𝑡) is an odd function, the Fourier series is a Fourier sine series, in which the terms aₙ are all equal to 0, and a proof will be shown in the next section."

---

## Express-Idea Vocabulary

**Sequencing / procedural ordering**
- "Before plotting the whole leaf, let us zoom" — narrows task order.
- "The outline of the triangle is then plotted" — "then" marks the next step.

**Cause / consequence**
- "Since the function 𝑓(𝑡) is an even function" — launches a cause→consequence chain.

**Specification / qualifier**
- "which is a suitable image for Fourier epicycles" — relative-clause qualifier on the chosen object.
- "with a height-to-width ratio of roughly 1:1" — numeric specification of the shape.

**Evidence handling**
- "The zoomed in portion of the figure is a triangle" — descriptive evidence anchored to a figure.
- "as shown in Fig. 3" / "as shown in Fig. 4" — figure-as-evidence pointers.

**Definition / formalisation verbs**
- "This curve represents a piecewise function" — *represents* as definition verb.
- "is defined as / is modelled by" — pattern not used verbatim but *represents* plays the same role.

**Explanation / mechanism verbs**
- "would trace out a similar function" — *would trace out* = behaviour-describing verb.
- "are all equal to 0" — result-state verb for vanishing terms.

**Transition / frame-shift**
- "Let us take these concepts and apply" — reader-direct pivot verb.

**Deferral / forward signposting**
- "a proof will be shown in the next section" — explicit forward pointer.

---

## How to Explain an Idea (replication steps)

**Pattern used: *Theory → Pivoting Example → Scope-Narrowing → Geometry-to-Algebra Bridge → Symmetry-Mechanism with Deferral*.**

To replicate with a new idea, follow these steps in order:

1. **Open with a pivot.** Write one sentence that signals a shift from the abstract definition just given to a concrete instance ("Let us take these concepts and apply it to a real-life example.").
2. **Pick a visually defensible object.** Name a specific, real-world figure or shape and immediately justify it with one short visual property ("a maple leaf… clear outline").
3. **Narrow the scope.** State explicitly that you will analyse only a sub-portion, so the problem becomes tractable ("Before plotting the whole leaf, let us zoom into a corner").
4. **Describe the sub-portion geometrically.** Name it, give one numeric proportion, and place it on a coordinate plane with an arbitrary unit.
5. **Formalise mathematically.** Convert the shape into a formula, naming the *type* of function (piecewise, periodic, etc.).
6. **State the implication.** Say what the tool/series/method will *do* to this function, using a modal verb ("would trace out a similar function that is repeated periodically").
7. **Apply a symmetry-mechanism.** Identify one property (even, odd, bounded) and use "Since…" to derive a consequence (which coefficients vanish, which form the series takes).
8. **Defer the proof.** Explicitly forward-point: "a proof will be shown in the next section," so the current section stays declarative, not computational.
9. **Verify prerequisites.** End by checking the conditions (continuity, boundedness) that make the method valid, using "as both… are…" to justify each.
