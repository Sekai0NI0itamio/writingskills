# Idea Flow Notes: mathematics_7_may2020_ebR3LrvPDXVOrUsg — n                                            n

## Paragraph Flow (move by move)

**Paragraph 1 — Theorem statement and inductive proof**

1. *Claim (continuation):* "M2,1 provide the n-th term of the sequence." Hands the reader to sentence 2 by **completing an already-stated finding** so the reader now knows the complete claim that needs proving.
2. *Claim (parallel restatement):* "M1,1 provides the (n + 1)th term." Hands the reader to sentence 3 by **mirroring the structure** of the prior sentence, so both matrix entries have now been accounted for and a proof becomes the natural next action.
3. *Transition + method announcement:* "This can be proved by induction:" Hands the reader to sentence 4 by **naming the procedure**, which signals a base case will follow.
4. *Formal statement:* "Theorem 1. [matrix identity] for all n ∈ N" Hands the reader to sentence 5 by **laying down what must be shown**, so a starting case is logically required.
5. *Base-case setup:* "Let n = 1:" Hands the reader to sentence 6 by **anchoring the induction at its lowest value**.
6. *Base-case verification:* matrix showing "M = [[1,1],[1,0]]" Hands the reader to sentence 7 by **closing the base case**, which licenses moving to the inductive hypothesis.
7. *Inductive hypothesis:* "Let k ∈ N be given and suppose M^n is true for n = k. Then:" Hands the reader to sentence 8 by **stipulating the assumption** that the next step will manipulate.
8. *Step transition:* "Inductive step for when n = k + 1:" Hands the reader to sentences 9–15 by **naming the target matrix** so each algebraic line answers it.
9–15. *Mechanism (algebraic chain):* lines (3)→(7) showing "M^{k+1} = M · M^k = ... = [[Fk+2, Fk+1],[Fk+1, Fk]]" Hand the reader to sentence 16 by **producing the exact target matrix**, leaving only the logical closure to do.
16. *Verdict:* "Since n = 1 is true, and when n = k is assumed to be true, n = k + 1 is also true, Theorem 1 holds. QED" Closes the paragraph by **fulfilling the induction contract** (base + step = proved).

**Paragraph 2 — Reflection on the proof**

1. *Verdict on usefulness:* "The information provided by these findings was crucial in my process." Hands the reader to sentence 2 by **asserting value**, which must now be backed by what was actually found.
2. *Evidence / discovery:* "I found that M^n's elements were the Fibonacci sequence itself." Hands the reader to sentence 3 by **delivering the concrete payoff**, which prompts an evaluative reaction.
3. *Concession + cause:* "At first, it seemed like this was a dead end, since I thought I had gone into an inevitable circle." Hands the reader to sentence 4 by **registering doubt**, which is the classic setup for a "but then I…" pivot.
4. *Forward transition:* "In hopes to find a more" — incomplete, hands the reader off-page by **opening a forward-pointing phrase** that the next paragraph resolves.

## What This Section Does (content sequence)

This section performs a two-part content sequence typical of an exploratory IB maths piece after an experimental phase:

1. **Formal closure of a discovered pattern** — first, the writer turns a numerical observation into a stated theorem so the work can be credited as rigorous rather than accidental.
2. **Inductive proof** — then, the writer proves it using the standard base-case + inductive-step + verdict structure, because induction is the conventional tool for sequence identities.
3. **Base case (n=1)** — first sub-move of the proof, because induction logically requires a starting verified value before any step can build on it.
4. **Inductive hypothesis (assume for k)** — second sub-move, because the step needs something to manipulate; without naming the assumption the algebra has no licence.
5. **Inductive step (show for k+1)** — third sub-move, because this is the substantive work that connects hypothesis to conclusion via the recurrence.
6. **Verdict** — final sub-move, because the induction contract must be explicitly closed (base + step ⇒ theorem) before a reader trusts the claim.
7. **Personal reflection on the proof's value** — after the formal block, the writer returns to first person and judges whether the proof advanced the exploration.
8. **Statement of the concrete finding** — gives the reader the specific takeaway so the judgement is anchored.
9. **Concession of initial doubt** — adds intellectual honesty and sets up a pivot toward what the writer will *next* pursue (sentence trails off, signalling continuation).

## Paragraph Skeletons (replicable templates)

**SKELETON A — Proof paragraph (claim → method → base case → hypothesis → step → verdict):**

   "[Continuation claim about object] and [companion claim]. This can be proved by [method]: Theorem 1. [formal statement]. Proof. Let n = [lowest case]: [verified base]. Let k ∈ N be given and suppose [hypothesis]. Then: [assumed matrix]. [Transition]: [target matrix]. [Algebraic chain] = ... = [target]. Since [base] is true, and when [hypothesis] is assumed, [target] is also true, [theorem] holds. QED"

1. **Slot 1 (continuation claims):** two parallel sentences identifying which part of the object equals which term of the sequence; declarative, present tense, mathematical notation.
2. **Slot 2 (method announcement):** a one-clause sentence naming the proof technique; ends with a colon to introduce the theorem.
3. **Slot 3 (theorem statement):** "Theorem 1." + matrix identity + quantifier "for all n ∈ N".
4. **Slot 4 (base case setup):** "Let n = [value]:" — sets lowest natural number.
5. **Slot 5 (base case evidence):** the explicit matrix for that base value.
6. **Slot 6 (inductive hypothesis):** "Let k ∈ N be given and suppose [pattern] is true for n = k."
7. **Slot 7 (assumed object):** the matrix as it looks under the hypothesis.
8. **Slot 8 (step transition):** "Inductive step for when n = k + 1:" + target matrix.
9. **Slot 9 (algebraic chain):** numbered lines (3)–(7) reducing M^{k+1} to the target by factoring, multiplying, and using the recurrence.
10. **Slot 10 (verdict):** single sentence confirming base + step ⇒ theorem, plus "QED".

**How to fill with a different idea:** pick any recursively defined object whose n-th term is given by a matrix power (e.g. Lucas numbers, Pell numbers, a custom linear recurrence). Replace every F with L or P, adjust the base matrix to match the recurrence's first two terms, and the induction still goes through.

**Original filled version:** the Fibonacci-matrix proof above.

**Demonstration fill (different idea — Lucas numbers via matrix):**
"and M2,1 provide the n-th Lucas number. M1,1 provides the (n+1)th. This can be proved by induction: Theorem 1. M^n = [[L_{n+1}, L_n],[L_n, L_{n-1}]] for all n ∈ N. Proof. Let n = 1: M = [[1,1],[1,0]]. Let k ∈ N be given and suppose M^k is [[L_{k+1}, L_k],[L_k, L_{k-1}]]. Inductive step for n = k+1: target [[L_{k+2}, L_{k+1}],[L_{k+1}, L_k]]. M^{k+1} = M·M^k = [[1,1],[1,0]]·[[L_{k+1}, L_k],[L_k, L_{k-1}]] = [[L_{k+1}+L_k, L_k+L_{k-1}],[L_{k+1}, L_k]] = [[L_{k+2}, L_{k+1}],[L_{k+1}, L_k]]. Since n=1 holds and the step transfers the hypothesis, Theorem 1 holds. QED."

**SKELETON B — Reflective tie-back paragraph (verdict → finding → concession → forward pivot):**

   "The information provided by [these findings / this result] was [evaluative adjective] in my process. I found that [specific concrete finding]. At first, it seemed like this was [negative interpretation], since [reason for the doubt]. [Forward-looking phrase setting up next paragraph]…"

1. **Slot 1 (verdict on value):** one sentence judging how much the formal result helped; first person, past tense, evaluative adjective ("crucial", "essential", "limited").
2. **Slot 2 (concrete finding):** a sentence stating what the writer now knows, phrased as a personal discovery with the notation visible.
3. **Slot 3 (concession + cause):** a sentence admitting an earlier wrong reaction, with "since" giving the reason; past tense, contemplative tone.
4. **Slot 4 (forward transition):** a trailing sentence beginning with "In hopes to…" or "Looking to…" that explicitly points to the next paragraph and is left syntactically incomplete so the next paragraph picks up the thread.

**How to fill with a different idea:** keep the structure intact but swap the object (e.g. eigenvalues of M, a closed-form Binet formula, a geometric interpretation) and the doubt (e.g. "I thought the closed form was too messy to use").

**Original filled version:** "The information provided by these findings was crucial in my process. I found that M^n's elements were the Fibonacci sequence itself. At first, it seemed like this was a dead end, since I thought I had gone into an inevitable circle. In hopes to find a more…"

**Demonstration fill (different idea — Binet's formula):** "The information provided by these findings was limited in my process. I found that the eigenvalues of M were the golden ratio φ and its conjugate 1−φ. At first, it seemed like this was overkill, since I thought a closed form added nothing new. In hopes to find a more…"

## Express-Idea Vocabulary

- **Sequencing / method-marking:** "This can be proved by induction:" — announces the proof strategy before the theorem.
- **Case-marking:** "Let n = 1:" — opens the base case.
- **Hypothesis-marking:** "Let k ∈ N be given and suppose" — sets up the inductive assumption.
- **Step-marking:** "Inductive step for when n = k + 1:" — transitions from assumption to consequence.
- **Cause / consequence:** "since I thought I had gone into an inevitable circle" — explains why the finding felt like a dead end.
- **Concession / doubt:** "At first, it seemed like this was a dead end" — admits the initial wrong reading.
- **Verdict / evaluation:** "Theorem 1 holds" — closes the logical contract of the proof.
- **Personal-discovery verbs:** "I found that M^n's elements were the Fibonacci sequence itself" — frames the result as personally discovered evidence.
- **Forward transition:** "In hopes to find a more" — opens a purpose clause that continues into the next paragraph.
- **Utility verdict:** "was crucial in my process" — judges how much the proof contributed to the exploration.

## How to Explain an Idea (replication steps)

This section relies on the **definition → identity-statement → inductive proof → personal-reflection** pattern. Step-by-step to apply it to a new idea:

1. **State the pattern in words.** Say which entries of your object correspond to which terms of the sequence. Two parallel sentences work best.
2. **Announce the method.** Declare "This can be proved by induction:" before introducing any formalism — this previews the proof structure.
3. **Box the claim as a theorem.** Use "Theorem 1." and write a matrix identity with a quantifier ("for all n ∈ N"). This converts an observation into something provable.
4. **Verify the base case.** Write "Let n = 1:" and display the explicit matrix. This is the smallest natural number and is usually trivial.
5. **State the inductive hypothesis.** Write "Let k ∈ N be given and suppose [pattern] is true for n = k. Then:" and display the assumed matrix. You must name what you are allowed to use.
6. **Mark the inductive step.** Write "Inductive step for when n = k + 1:" and display the matrix you are aiming to reach. The reader now knows the target.
7. **Perform algebraic chain.** Number each equality (3), (4), (5)… and reduce M^{k+1} = M·M^k down to the target, using the recurrence as a substitution.
8. **Close with a verdict.** One sentence: "Since n = 1 is true, and when n = k is assumed to be true, n = k + 1 is also true, [theorem] holds. QED." The contract must be visible.
9. **Switch to reflective voice.** Begin the next paragraph with a personal verdict on the proof's usefulness, e.g. "The information provided by these findings was [adjective] in my process."
10. **Name the concrete finding.** Write "I found that [specific mathematical statement]." This anchors the abstract proof to what the writer actually learned.
11. **Concede initial doubt.** Use "At first, it seemed like…" plus "since…" to admit a wrong reaction and give its cause — this makes the reflection credible.
12. **Open a forward clause.** End with "In hopes to find a more…" so the next paragraph visibly continues the thought.
