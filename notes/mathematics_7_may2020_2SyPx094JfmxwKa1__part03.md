# Idea Flow Notes: mathematics_7_may2020_2SyPx094JfmxwKa1 — Generalizing to Different Periods

## Paragraph Flow (move by move)

**Paragraph 1**
- **S1 — Claim of generality:** "The orthogonality relation could be expanded to any arbitrary period." Names the move (generalization) and stakes the section's purpose. Hand-off: the claim needs justification, so the next sentence supplies a *special-case framing* to motivate why the expansion is plausible.
- **S2 — Special-case framing:** "as 𝑓(𝑥) with period 2𝜋… could be viewed as a special case of a function with period 2𝐿." Anchors the familiar case inside a broader container. Hand-off: the reader now has the general variable (2L) primed, so the next paragraph can open by *defining* that variable explicitly.

**Paragraph 2**
- **S1 — Setup / definition:** "Let the period of a periodic function be 2𝐿." Picks up the 2L just introduced and formalises it as the working parameter. Hand-off: with 2L fixed, the next sentence must specify *what* the new trig terms stand for.
- **S2 — Specification of correspondence:** "cos (…) and sin (…) represent cos(𝑛𝑡) and sin(𝑛𝑡) when 2𝐿 = 2𝜋." Pins the new notation to the familiar one via an equating condition. Hand-off: the two notations are now interchangeable, so the next sentence can perform the *parallel substitution* into the full series.
- **S3 — Generalization move (parallel display):** "Thus, the Fourier series 𝑓(𝑡) = … with a period of 2𝜋 can then be generalized as 𝑓(𝑡) = … with a period of 2𝐿." Stages the specific formula beside the general formula so the substitution is visible. Hand-off: having shown the series generalises, the next sentence begins to draw the *implication for the orthogonality relation itself*.
- **S4 — Implication (incomplete):** "Since the orthogonality relation for the…" Starts a consequence clause tying the series generalisation back to the section's opening claim. Hand-off (intended): would have delivered the rewritten orthogonality statement that the opening sentence promised.

---

## What This Section Does (content sequence)

A "generalising a previously-derived result" section executes this ordered move-set:

1. **State the generalisation claim** — name what is being broadened (here: orthogonality to arbitrary period). This sets the destination the rest of the paragraph travels toward.
2. **Frame the known case as a special instance** — present the already-proved result as a *sub-case* of the general one. This justifies the move by showing the new result contains the old.
3. **Define the new parameter** ("Let the period … be 2L") — turn the general container into a working variable so concrete symbols can be used.
4. **Specify the term-by-term correspondence** — state the equality condition (2L = 2π) that lets new symbols be read as old ones. This is the bridge between the two cases.
5. **Display the two formulas in parallel** (specific | general) — show the substitution happening visibly, so the reader can verify the swap.
6. **Draw the implication for the original object** — extend the same logic back to the relation the section opened with (orthogonality). This closes the loop promised by move 1.

The order matters: you cannot specialise-to-generalise (move 2) before you have a specific result to specialise; you cannot do the parallel display (move 5) without first defining the parameter (3) and the correspondence (4); and the implication (6) must come last because it depends on moves 3–5 having been shown.

---

## Paragraph Skeletons (replicable templates)

### Skeleton A — "Generalise-by-special-case" opener

> SKELETON: "The **[previous result]** could be expanded to **[broader scope]**, as **[specific case]** could be viewed as a special case of **[general case]**, where **[variable]** 𝜖 **[domain]**."

1. **Slots:** [previous result] = noun phrase naming what you already proved (the orthogonality relation). [broader scope] = a phrase quantifying the wider class ("any arbitrary period", "all real-valued inputs"). [specific case] = the known formula with concrete constants. [general case] = the same formula with a symbolic parameter. [variable] = the parameter symbol. [domain] = the set the parameter ranges over.
2. **How to fill with a different idea:** Pick a theorem/result you proved for one fixed quantity. Decide which quantity you want to free up (frequency, dimension, sample size). State the theorem once with the original constant, then restate it with the variable replacing that constant; let the domain be the natural range (ℝ, ℕ, (0, ∞)).
3. **Original filled version:** "The orthogonality relation could be expanded to any arbitrary period, as 𝑓(𝑥) with period 2𝜋… could be viewed as a special case of a function with period 2𝐿, where L 𝜖 𝑅."
4. **Demonstration fill (different idea):** "The power-reduction identity could be expanded to any integer exponent, as cos²(𝑥) could be viewed as a special case of cosⁿ(𝑥) where n 𝜖 ℕ." (Same skeleton, completely different mathematical content.)

### Skeleton B — "Define parameter, specify correspondence, parallel display"

> SKELETON: "Let the **[parameter]** be **[new value]**, where **[new term A]** and **[new term B]** represent **[old term A]** and **[old term B]** when **[equating condition]**. Thus, the **[specific formula]** with **[old period/value]** can then be generalized as **[general formula]** with **[new period/value]** for **[domain]**."

1. **Slots:** [parameter] = noun naming what you are generalising (period, exponent, dimension). [new value] = a symbolic expression containing the parameter (2L, 𝑛). [new term A/B] = the rewritten trigonometric/expression terms. [old term A/B] = the originals they map to. [equating condition] = the equality that makes the substitution valid (2L = 2π). [specific formula] = the formula with concrete numbers. [general formula] = the same formula with the symbolic parameter substituted throughout.
2. **How to fill with a different idea:** Choose the parameter to free up. Write "Let X be Y" to declare the parameter. Decide which two terms/symbols in your formula need rewriting when Y takes its old numeric value; state the "represent … when" bridge clause. Then write the formula twice in one sentence joined by "can then be generalized as," copying structure but swapping constants for symbols.
3. **Original filled version:** "Let the period of a periodic function be 2𝐿, where cos (…) and sin (…) represent cos(𝑛𝑡) and sin(𝑛𝑡) when 2𝐿 = 2𝜋. Thus, the Fourier series 𝑓(𝑡) = … with a period of 2𝜋 can then be generalized as 𝑓(𝑡) = … with a period of 2𝐿 for L 𝜖 𝑅."
4. **Demonstration fill (different idea):** "Let the side length of a regular polygon be 𝑠, where the interior angle formula (𝑛−2)·180°/𝑛 represents the triangle's angle when 𝑠 replaces the side. Thus, the angle sum for a quadrilateral 360° with fixed vertices can then be generalized as the angle sum (𝑛−2)·180° for 𝑛 𝜖 ℕ, 𝑛 ≥ 3."

### Skeleton C — "Implication back to the original object"

> SKELETON: "Since the **[relation/identity]** for the **[original context]** **[begins to state the generalised version]**, …"

1. **Slots:** [relation/identity] = the central object named in the opener (orthogonality relation). [original context] = the special case it was proved in. [verb phrase] = the generalisation claim that mirrors Skeleton A's move 1.
2. **How to fill with a different idea:** Open with "Since" to mark consequence. Repeat the name of the result you opened the section with. Then repeat the *form* of the original claim but with the new parameter in place of the old constant. The sentence is meant to flow directly into a display of the generalised identity.
3. **Original filled version:** "Since the orthogonality relation for the [period 2𝜋 case can be rewritten for the 2𝐿 case], …" (sentence cut off in source).
4. **Demonstration fill (different idea):** "Since the power-reduction identity for cos²(𝑥) [extends to cosⁿ(𝑥) for any 𝑛 𝜖 ℕ], the same reduction can be applied to the higher-order integrals." (Same skeleton, different mathematical content.)

---

## Express-Idea Vocabulary

**Sequencing / structural connectives**
- "Thus" — "Thus, the Fourier series … can then be generalized as …" (introduces the parallel substitution after the correspondence has been fixed.)
- "can then be generalized as" — same sentence (marks the transition from known case to broadened formula.)

**Claim / assertion verbs**
- "could be expanded to" — "The orthogonality relation could be expanded to any arbitrary period." (announces the generalisation move at the section's head.)
- "could be viewed as a special case of" — same sentence as above (frames the known result as a sub-instance.)

**Setup / definition language**
- "Let the … be" — "Let the period of a periodic function be 2𝐿." (introduces the working parameter.)
- "represent … when" — "cos (…) and sin (…) represent cos(𝑛𝑡) and sin(𝑛𝑡) when 2𝐿 = 2𝜋." (states the term-by-term correspondence rule.)
- "where L 𝜖 𝑅" — closes both opening sentences (specifies the parameter's domain.)

**Cause / consequence connectors**
- "Since" — "Since the orthogonality relation for the …" (opens the implication clause that ties the generalised series back to the opener.)

---

## How to Explain an Idea (replication steps)

This section uses a **claim → contain-as-special-case → parameterise → bridge-equality → parallel-display → consequence** pattern. To replicate it on a new idea:

1. **Open with the generalisation claim.** One sentence announcing that a previously proved result extends to a wider class. Name both the result and the dimension you are freeing up.
2. **Motivate by containment.** In the same opening sentence (using "as" or "since"), show that the *old* result sits inside the *new* one as a special case when the new parameter takes the old value.
3. **Define the new parameter explicitly.** Start a new sentence with "Let the [quantity] be [symbolic expression]." State the domain of the parameter at the end of the sentence ("where X ∈ D").
4. **Write a "bridge" clause.** In the same or next sentence, declare the term-by-term correspondence between old notation and new notation, using the form "where [new symbol] represents [old symbol] when [equating condition]."
5. **Display the two formulas in parallel.** Use "Thus" + "can then be generalized as" to put the specific formula and the generalised formula side by side so the reader can see the substitution happen. Keep the structure identical; swap only constants for symbols.
6. **Close with "Since…"** to begin drawing the implication back to the original object (the relation named in step 1). This is the sentence that proves you have actually delivered on the opening claim.
