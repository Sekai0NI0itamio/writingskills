# Idea Flow Notes: mathematics_7_may2020_KupcNzdWlKMboMJM — 5.2.3   Axis and Angle to Quaternion

## Paragraph Flow (move by move)

**Paragraph 1** (1 sentence + equation block)
1. **Context/Claim** — *"The rotation axis (unit vector, v̂) and angle (θ) can be converted"* — introduces the conversion operation and names its two inputs (axis as a unit vector, angle). Hands the reader to the equation block by announcing "the following formulae" — the next move is to display them.

**Paragraph 2** (3 sentences)
1. **Mechanism** — *"This makes sense because quaternions consist of"* — asserts that the formula has an internal reason; hands to the next sentence by naming the two-part structure (scalar + vector).
2. **Specification/Evidence** — *"With a unit vector a²i + b²j + c²k = 1, this can be combined"* — feeds the two preconditions (vector-length-one and Pythagorean identity) into a single move; hands to next by signalling that an existing source exists.
3. **Contrast + Authorial claim** — *"While Wolfram MathWorld introduces this idea, it is not very clear"* — concedes the source exists but flags a clarity gap, then pivots to the student's own contribution; hands to next by promising a "more concrete proof."

**Paragraph 3** (equation chain + 1 sentence)
1. **Worked step (evidence chain)** — three stacked equation blocks start from the Pythagorean identity, substitute the unit-vector condition, then expand into four squared terms. Each equation is the *consequence* of the one above (algebraic implication). Hands to next by producing a recognisable form.
2. **Identification/Verdict** — *"This is a form of w² + a² + b² + c² = 1, a unit quaternion."* — names the final expression and labels it; hands to next by signalling a cross-reference back to the definitions.

**Paragraph 4** (1 sentence)
1. **Specification/Cross-reference** — *"Here, w, a, b and c are the individual components laid out"* — anchors the symbols used in the verdict back to equation 10; closes the proof by tying the conclusion to the original formula.

---

## What This Section Does (content sequence)

This is a **formula → justification → motivation → algebraic verification → identification** proof section.

1. **State the working formulae first** — sets the reader's target: here are the conversions you will end up understanding.
2. **Give a one-line reason it must be true** — appeals to structure (scalar + vector composition) so the proof feels necessary, not arbitrary.
3. **Stack the two preconditions (unit-vector norm and Pythagorean identity)** — supplies the raw material the algebra will consume.
4. **Flag a gap in an external source** — establishes the student as filling a real need, not rehearsing a textbook.
5. **Walk the proof in visible steps** — show every substitution so a reader can follow without re-doing the algebra; each line is a consequence of the previous one.
6. **Name the final expression** — pin it to a known label ("unit quaternion") so the reader recognises the destination.
7. **Cross-reference symbols back to the opening equation** — closes the loop and prevents the reader losing track of which variable is which.

The order matters: (1) gives the destination, (2)–(3) supply the why and the raw facts, (4) earns the right to prove, (5) proves in auditable steps, (6)–(7) confirm the destination was reached.

---

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Justification opener"**
`[The operation] can be performed using the following formulae. This makes sense because [object] consists of [structural feature A] and [structural feature B]. With [precondition 1], this can be combined with [precondition 2].`

1. *Slots:* Slot 1 = "can be converted/performed using the following formulae" (declarative, names two inputs in parentheses). Slot 2 = "This makes sense because … consists of X and Y" (one-clause reason). Slot 3 = "With … this can be combined with …" (two citations, each labelled).
2. *Filling instructions:* Pick a transformation with two given quantities and several outputs. List the outputs in a formula block. Then identify the defining structural split of the target object. Finally pull in one external identity for each structural piece so the proof has somewhere to start.
3. *Original:* "The rotation axis (unit vector, v̂) and angle (θ) can be converted into quaternions using the following formulae. This makes sense because quaternions consist of a scalar and vector component. With a unit vector a²i + b²j + c²k = 1, this can be combined with Pythagorean's identity…"
4. *Demonstration fill:* "The pressure (P) and volume (V) of an ideal gas can be related to its temperature using the following formulae. This makes sense because temperature consists of a kinetic-energy component and a potential-energy component. With the equipartition result ½mv² = ³⁄₂kT, this can be combined with the virial expansion of Z."

**SKELETON B — "Source-gap pivot"**
`While [authority/source] introduces this idea [citation], it is not very [criticism] and I would like to offer a [improvement].`

1. *Slots:* "While [source] introduces this idea [n]" (concession with citation), "it is not very [adjective]" (specific complaint), "I would like to offer a [better-quality noun]" (promise of contribution).
2. *Filling instructions:* Choose one textbook or website actually used. Quote it briefly. Diagnose the exact weakness (unclear, missing steps, no justification). Announce what your version adds — concrete proof, worked example, explicit assumptions.
3. *Original:* "While Wolfram MathWorld introduces this idea [7], it is not very clear and I would like to offer a more concrete proof."
4. *Demonstration fill:* "While Stewart's Calculus introduces this idea [4], it is not very rigorous and I would like to offer a more geometric proof."

**SKELETON C — "Algebraic verification chain"**
`[identity 1]. [identity 2 substituted]. [terms expanded].`

1. *Slots:* Three equation lines, each on its own display. Line 1 = a known identity. Line 2 = the same identity with one symbol replaced by a defined expression. Line 3 = the result of distributing/simplifying into separate squared terms.
2. *Filling instructions:* Pick a known identity. Pick a second identity that defines one of its symbols. Substitute. Distribute. End on a sum of squares that equals 1.
3. *Original:* Pythagorean identity → unit-vector substitution → expansion into cos² + a² + b² + c² = 1.
4. *Demonstration fill:* Euler's identity → Euler's formula substitution → expansion into Re² + Im² = 1.

**SKELETON D — "Result identification + cross-reference"**
`This is a form of [canonical expression], a [name]. Here, [symbols] are the individual components laid out in [earlier equation number].`

1. *Slots:* "This is a form of …" (labels the shape), comma + "a [named object]" (gives it a proper name), "Here, … are … laid out in equation [n]" (reminds the reader where each symbol came from).
2. *Filling instructions:* After a derivation, point to the final expression and match it to a textbook form. Name it. Then list the symbols used and cite the equation where they were first defined.
3. *Original:* "This is a form of w² + a² + b² + c² = 1, a unit quaternion. Here, w, a, b and c are the individual components laid out in equation 10."
4. *Demonstration fill:* "This is a form of P² + Q² = 1, a unit complex number. Here, P and Q are the individual components laid out in equation 6."

---

## Express-Idea Vocabulary

- **Sequencing / progression:** *"the following formulae"* — names what is about to be shown; *"the individual components laid out in equation 10"* — orders reader to look back.
- **Cause / mechanism:** *"This makes sense because"* — explains why a formula is reasonable; *"this can be combined with"* — names how two facts fuse.
- **Contrast / concession:** *"While Wolfram MathWorld introduces this idea, it is not very clear"* — concedes source then rejects its quality.
- **Specification / pinpointing:** *"a unit vector a²i + b²j + c²k = 1"* — instantiates an abstract claim with exact terms; *"individual components laid out in equation 10"* — re-anchors symbols.
- **Evidence handling:** *"using the following formulae [5]"* — authority citation before formula; *"Pythagorean's identity … = 1 [7]"* — authority citation before identity.
- **Explanation verbs:** *"can be converted into"* (operational verb); *"consist of"* (structural verb); *"introduces this idea"* (source-attribution verb); *"is a form of"* (identification verb); *"laid out in"* (cross-reference verb).
- **Authorial positioning:** *"I would like to offer a more concrete proof"* — first-person framing of the contribution.

---

## How to Explain an Idea (replication steps)

The pattern is **formula → reason-it-works → motivation (gap in a source) → algebraic verification → identification of result**.

1. **Open with the working formulae.** State the two inputs in parentheses and the outputs as a labelled equation block. The reader now knows the destination.
2. **Give a one-sentence structural reason.** Use "This makes sense because [object] consists of A and B." Name the two-part structure of whatever the formula produces.
3. **Stack the preconditions.** State each external identity the proof will use, with its citation. Give the reader the raw material.
4. **Flag a gap in an existing source.** Use "While [source] introduces this idea [n], it is not very [criticism] and I would like to offer a [better noun]." Establish why your version is needed.
5. **Show the algebra in three visible steps.** Line 1 = the first identity alone. Line 2 = that identity with one symbol replaced by the second identity. Line 3 = the distributed/simplified sum of squares. Every line must be a direct consequence of the line above.
6. **Identify the final form.** Use "This is a form of [canonical expression], a [named object]." Tell the reader what they have just produced.
7. **Cross-reference back to the opening equation.** Use "Here, [symbols] are the individual components laid out in equation [n]." Close the loop.
