# Idea Flow Notes: mathematics_6_may2020_DURQzgCYVOHZ14jv — Now we can use nCr in order to find the binomial coefficient of the expansion terms for every

## Paragraph Flow (move by move)

**Paragraph 1** (the binomial expansion formula)
1. **Move — Formula display.** "(x+y)n = xn + nxn-1y + ... +nCr xn-r yr + ... +nxyn-1 + yn". *Hands to next sentence by:* handing the reader an un-annotated symbol `nCr` that needs explaining — the parenthetical that follows fills that gap.
2. **Move — Forward reference / roadmap.** "The Pascal's triangle is going to be used later in the proof." *Hands to next sentence by:* closing the formula block, so the reader is ready for a topic pivot to the actual proof.

**Paragraph 2** ("PROVING FERMAT'S LITTLE THEOREM")
1. **Move — Section header / transition.** "PROVING FERMAT'S LITTLE THEOREM". *Hands to next sentence by:* signaling a new argumentative phase, which forces a restatement of what is being proved.
2. **Move — Restatement cue.** "Lets restate what Fermat's little theorem says again". *Hands to next sentence by:* explicitly announcing that what follows is a definition/re-statement, not new content.
3. **Move — Formal definition.** "Fermat's little theorem states: Let p be a prime number, and a be and integer." *Hands to next sentence by:* setting up the two free variables (p, a) so the next move can state what the theorem claims about them.
4. **Move — Statement of the claim.** "Then ap-a is always divisible by p." *Hands to next sentence by:* giving the claim in words; the next move compresses it into modular notation for manipulation.
5. **Move — Translation into working notation.** "ap ≡a mod p". *Hands to next paragraph by:* giving the formal target that the cases below will be checked against.

**Paragraph 3** (Step 1, the trivial case a = 0)
1. **Move — Numbered step + scope.** "1) First we are going to deal with {0}". *Hands to next sentence by:* naming the case category in set notation, requiring a plain-language unpacking.
2. **Move — Unpack / specification.** "or in other words when a=0". *Hands to next sentence by:* fixing a concrete value of `a`, which makes the claim directly evaluable.
3. **Move — Worked evaluation.** "a=0 => 0p mod p = (0 × 0 × … × 0) mod p". *Hands to next sentence by:* showing the substitution; the next move converts this into the modular conclusion.
4. **Move — Consequence / verdict.** "Thus 0p mod ≡ 0". *Hands to next sentence by:* closing the case with a tick (□) so the next paragraph can pick up the next case.

**Paragraph 4** (Step 2, opening the general case)
1. **Move — Numbered step + transition.** "2) Now we are going to prove the theorem". *Hands to next sentence by:* announcing a shift from a special case to a general class; the next move narrows that class.
2. **Move — Scope specification.** "for a∈Z+". *Hands off:* terminates mid-statement (the section ends), signalling the scope under which the general proof will run.

## What This Section Does (content sequence)

This section is a **transitional proof-opening block** — it links a previously-displayed identity to the case-based proof that follows. The ordered content moves are:

1. **Display the key identity** (the binomial expansion) so its coefficient term `nCr` is on the page.
2. **Forward-reference the supporting tool** (Pascal's triangle) so the reader expects it later.
3. **Section header** announcing the proof phase.
4. **Restate the theorem to be proved**, first in words ("ap-a is always divisible by p"), then in modular notation ("ap ≡ a mod p") — the words fix the meaning, the notation fixes the form to be manipulated.
5. **Numbered case-by-case structure**, starting at case 1 = 0.
6. **Solve the base/trivial case** with a one-line substitution (a = 0 ⇒ 0 mod p = 0).
7. **Open the general case** (a ∈ ℤ⁺) so the next paragraph can continue the induction/argument.

The order matters because each move sets up the next: the identity must be on the page before the proof can use it; the theorem must be stated in both words and modular form before a substitution can be checked; the trivial case must be dispatched before the general case can be opened cleanly.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Identity display + roadmap note**
"[Display a general formula]. [Tool/method] is going to be used later in the proof."

1. **Slot 1 (formula display):** an algebraic identity written in one line with a general term highlighted (e.g. `… + nCr x^(n-r) y^r + …`). *Shape:* symbolic, unpunctuated block.
2. **Slot 2 (forward reference):** a parenthetical or short sentence naming the auxiliary tool that will reappear. *Shape:* present continuous ("…is going to be used later in the proof").
3. **How to fill with a different idea:** choose an identity that contains a coefficient/combinatorial term you want to highlight; write it out in full; add a parenthetical naming the diagram/lemma/algorithm that justifies the coefficient later.
4. **Original fill:** "(x+y)n = xn + nxn-1y + ... +nCr xn-r yr + ... +nxyn-1 + yn (The Pascal's triangle is going to be used later in the proof.)"
5. **Demonstration fill (Euler's totient identity):** "ϕ(mn) = ϕ(m)ϕ(n) when gcd(m,n)=1 (The Chinese Remainder Theorem is going to be used later in the proof.)"

---

**SKELETON B — Restate theorem in words, then in working notation**
"Lets restate what [Theorem] says again: [Theorem] states: [hypotheses]. Then [claim in words]. [claim in formal notation]"

1. **Slot 1 (restate cue):** imperative plural ("Lets restate … again"). *Shape:* colon-ending clause.
2. **Slot 2 (hypotheses):** "Let [variable] be [class]". *Shape:* two-clause quantifier sentence.
3. **Slot 3 (verbal claim):** "Then [expression] is always [property]". *Shape:* declarative in plain English.
4. **Slot 4 (formal claim):** the same claim re-expressed in the notation that will be manipulated downstream. *Shape:* one short equivalence/congruence line.
5. **How to fill with a different idea:** pick a theorem; write its hypotheses as "Let X be Y"; write its conclusion first in plain words; then rewrite it in the algebraic/modular/functional notation you will use in the proof.
6. **Original fill:** "Lets restate what Fermat's little theorem says again: Fermat's little theorem states: Let p be a prime number, and a be and integer. Then ap-a is always divisible by p. ap ≡a mod p"
7. **Demonstration fill (Wilson's theorem):** "Lets restate what Wilson's theorem says again: Wilson's theorem states: Let p be a prime number. Then (p-1)! + 1 is always divisible by p. (p-1)! ≡ -1 mod p"

---

**SKELETON C — Numbered base case: dispatch the trivial substitution**
"[N]) First we are going to deal with {[special value]} or in other words when [variable]=[value]. [substitution] ⇒ [evaluated expression] ≡ [result]. Thus [claim]."

1. **Slot 1 (step number + scope):** "1) First we are going to deal with {…}". *Shape:* numeral, parenthetical, future-tense framing.
2. **Slot 2 (unpack the special value):** "or in other words when a=0". *Shape:* disjunction clause.
3. **Slot 3 (worked substitution):** the expression with `a` replaced, showing the multiplication/expansion. *Shape:* symbolic chain.
4. **Slot 4 (modular collapse):** "≡ [result]". *Shape:* short congruence.
5. **Slot 5 (verdict):** "Thus [re-statement of result]" + tick/box. *Shape:* "Thus" + one-line restatement.
6. **How to fill with a different idea:** identify the trivial case in your theorem; state it in set notation; unpack it in words; substitute; reduce modulo whatever the theorem uses; restate with "Thus" + □.
7. **Original fill:** "1) First we are going to deal with {0} or in other words when a=0. a=0 => 0p mod p = (0 × 0 × … × 0) mod p ≡ 0 mod p × … × 0 mod p = 0. Thus 0p mod ≡ 0 □"
8. **Demonstration fill:** "1) First we are going to deal with {1} or in other words when a=1. a=1 => 1p mod p = (1 × 1 × … × 1) mod p ≡ 1 mod p × … × 1 mod p = 1. Thus 1p mod p ≡ 1 □"

---

**SKELETON D — Numbered general-case opening**
"[N]) Now we are going to prove the theorem to be [verb] for [scope]."

1. **Slot 1:** numbered label. *Shape:* "2)".
2. **Slot 2:** transition word. *Shape:* "Now".
3. **Slot 3:** scope quantifier. *Shape:* "for a∈Z+" / "for all prime p" / etc.
4. **How to fill with a different idea:** after dispatching the base case, announce the general scope with a numeral, a "Now", and a set-membership condition that defines the remainder of the proof.
5. **Original fill:** "2) Now we are going to prove the theorem to be prove for a∈Z+"
6. **Demonstration fill:** "2) Now we are going to prove the theorem for all odd primes p"

## Express-Idea Vocabulary

- **Sequencing / numbering:** "1) First we are going to deal with", "2) Now we are going to prove the theorem" — explicit case-labels that tell the reader this is a case-split proof.
- **Restatement / framing:** "Lets restate what Fermat's little theorem says again" — cues the reader that an already-known claim is being re-set on the page.
- **Definition:** "Fermat's little theorem states: Let p be a prime number" — colon-led "Let …" sentence that fixes variables.
- **Specification / unpacking:** "or in other words when a=0" — rephrases a set-membership phrase in substitution-ready form.
- **Cause / consequence / deduction:** "Thus 0p mod ≡ 0" — closes a case by derivation; "Then ap-a is always divisible by p" — verbal conclusion of a "Let … Then …" definition.
- **Forward reference:** "The Pascal's triangle is going to be used later in the proof." — explicit roadmap to a tool not yet invoked.
- **Translation between registers:** "ap-a is always divisible by p." → "ap ≡a mod p" — same idea re-stated in working notation.
- **Explanatory connective verbs:** "states:" (definition), "is going to be used" (forward reference), "is always divisible by" (property), "deal with" (case-handling).

## How to Explain an Idea (replication steps)

This section uses the pattern: **restate-the-target → dispatch-trivial-case → open-general-case**. It is a *proof-opening by case-split*, not a definition→example pattern.

Steps to replicate with a NEW idea:

1. **Open with the working identity** the proof will rely on (here: the binomial expansion). Display it in full so its key term (nCr) is visible.
2. **Drop a one-line forward reference** naming the auxiliary tool (here: Pascal's triangle) that justifies the key term.
3. **Insert a section header** ("PROVING …") so the reader sees a phase change from identity-display to proof.
4. **Cue a restatement** ("Lets restate what … says again") before restating — this primes the reader that nothing new is being introduced.
5. **State the theorem twice**: first in words ("ap-a is always divisible by p"), then in the modular/algebraic notation the proof will actually use ("ap ≡ a mod p"). Both forms must be on the page.
6. **Begin the case-split with the trivial case** (here: a = 0). Mark it with a numeral and a "First" so the reader knows it is base-case work.
7. **Unpack the special value in plain words** ("or in other words when a=0") before substituting — set-membership notation must be translated.
8. **Show the substitution as a written-out chain**, not a single jump ("(0 × 0 × … × 0) mod p"), so the reader can see why the result holds.
9. **Close the case with "Thus …" + a tick** (□), giving a verdict-style signal that this case is done.
10. **Open the next case with "Now" + numeral + scope quantifier** ("2) Now we are going to prove … for a∈Z+"), so the reader sees the proof continuing but with a broader class of inputs.
