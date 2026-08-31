# Idea Flow Notes: mathematics_7_may2017_TzoKIgKR386jeyuR — From the above equation, the equations for the dependent variable in a PSIRM can be

## Paragraph Flow (move by move)

**Paragraph 1 (explaining Equation 8):**

1. **Sentence 1** — Comparison / analogy move: *"Similar to Equation 2, the first part of the ICBPDF represents…"*. Anchors the unfamiliar Equation 8 onto the already-explained Equation 2 so the reader re-uses a known structure. Hands the reader forward by naming the structural slot ("first part") that the rest of the paragraph will unpack.
2. **Sentence 2** — Specification / parameter definition: *"The probability of success of the infection is i."*. Hands the reader forward by giving the success-rate of the "trials" that sentence 1 just set up, so the next sentence can layer the randomness on top.
3. **Sentence 3** — Definition + unpacking: *"X is a continuous random variable that is uniformly distributed between 0 and 1, simulating the underlying random probability…"*. Hands the reader forward by supplying the randomising ingredient the trial needs to actually run.
4. **Sentence 4** — Mechanism / sign-justification: *"A negative sign is used here as the number of people in the S population group must decrease…"*. Closes the equation by explaining its sign, which forces a contrast in the next paragraph (whatever S loses, I must gain).

**Paragraph 2 (explaining Equation 9):**

1. **Sentence 1** — Comparison / mirror move: *"The first part of this equation is the negative of Equation 8, as the decrease of the number of people in the S population group should be equal to the negative of the increase…"*. Re-uses the conclusion of Paragraph 1 to set up the flow term in Equation 9. Hands the reader forward by closing the mirror half so the next sentence can introduce the new process.
2. **Sentence 2** — Contrast / pivot: *"However, as the people in in the I population group recover, the number of people in the I population group decreases."*. The "However" breaks the mirror and opens a new process (recovery) acting on the same group. Hands the reader forward because the I-population now needs its own trial/probability structure.
3. **Sentence 3** — Specification / trial-count definition: *"The number of trials performed on the people in the I population group is I(t)."*. Hands the reader forward by mirroring sentence 1 of Paragraph 1 (trials defined first), setting up the probability next.
4. **Sentence 4** — Parameter definition: *"The probability of success of the recovery is r."*. Hands the reader forward by closing the recovery process terms, leaving only the random variable to define.
5. **Sentence 5** — Definition (cut off): *"Y is a continuous random variable that is uniformly distributed between 0 and 1,"*. Hands the reader forward by completing the parallel to "X" in Paragraph 1, sentence 3 — the structure is intentionally cloned.

---

## What This Section Does (content sequence)

This section type is a **term-by-term equation walk-through**. The order is:

1. **Caption the equation** (sets the boundary of what is being explained).
2. **Cross-reference a prior equation** (so the reader imports a known scaffold rather than meeting a new one cold).
3. **Translate the first term** from symbol to plain meaning (what it "represents").
4. **Define the probability parameter** controlling that term.
5. **Define the random variable** supplying the stochastic element.
6. **Justify the sign/operator** with a conservation or behavioural reason.
7. **Caption the next equation** in the family.
8. **State the mirror relationship** to the previous equation (negative of Equation 8).
9. **Pivot with "However"** to introduce a second competing process on the same compartment.
10. **Re-run steps 3–5** in the same left-to-right order for the new process.

The order works because each move answers one specific question the reader will have at that moment: "what is this?", "how likely?", "where does the randomness come from?", "why that sign?", "what else acts on this group?" Repeating the same left-to-right order across equations lets the reader pattern-match between them.

---

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Equation-by-analogy" paragraph** (used for Paragraph 1)

> *(Refer to Equation X)* Similar to [prior equation], the [position] part of the [formula name] represents [plain meaning]. [Probability parameter] is [definition]. [Random variable] is a continuous random variable that is uniformly distributed between 0 and 1, [simulating / modelling what]. A [sign/operator] is used here as [conservation/behavioural reason].

1. **Slot 1 — prior equation reference:** a noun-phrase label of an earlier equation. *"Equation 2."*
2. **Slot 2 — position phrase:** an ordinal / locative phrase identifying which term you are unpacking. *"the first part."*
3. **Slot 3 — formula name:** the name of the probability function being used. *"the ICBPDF."*
4. **Slot 4 — plain meaning:** what that term counts in everyday language. *"the number of interactions… per unit time."*
5. **Slot 5 — probability definition:** a single-letter parameter stated in one short clause. *"The probability of success… is i."*
6. **Slot 6 — random variable:** a distribution statement followed by a participle clause stating its purpose. *"X is a continuous random variable… simulating the underlying random probability."*
7. **Slot 7 — sign justification:** a "as" / "because" clause tied to system behaviour. *"as the number of people… must decrease."*

**How to fill with a DIFFERENT idea:** Pick an equation that is built from a binomial-style core. Replace slot 1 with an earlier analogous equation from your work, slot 2 with whichever term you want to unpack (first, second, last…), slot 3 with the name of your probability distribution, slot 4 with the count it represents, slot 5 with the success-probability letter, slot 6 with another uniform random variable, slot 7 with the population-level reason for any negative sign.

**Original filled version (this text):** *"Similar to Equation 2, the first part of the ICBPDF represents the number of interactions… The probability of success of the infection is i. X is a continuous random variable… A negative sign is used here as the number of people in the S population group must decrease as people get infected."*

**Demonstration fill (different subject, same skeleton):** *Similar to Equation 4, the first part of the logit function represents the linear combination of predictor variables. The coefficient of the predictor is β₁. X is a continuous random variable that is uniformly distributed between 0 and 1, simulating the underlying random error of the measurement. A negative sign is used here as a one-unit increase in the predictor must decrease the log-odds of the event.*

**SKELETON B — "Equation-by-mirror-then-pivot" paragraph** (used for Paragraph 2)

> *(Refer to Equation X)* The first part of this equation is the [mirror word: negative/inverse] of [prior equation], as [conservation reason]. However, [new process affecting the same compartment], the [compartment] [decreases/increases]. The number of trials performed on the [compartment] is [size expression]. The probability of success of the [new process] is [parameter]. [Variable] is a continuous random variable that is uniformly distributed between 0 and 1, [role].

1. **Slot 1 — mirror claim:** a single sentence equating the current term to the negative of the prior equation. *"The first part of this equation is the negative of Equation 8."*
2. **Slot 2 — conservation reason:** an "as" clause stating the bookkeeping rule. *"as the decrease… should be equal to the negative of the increase."*
3. **Slot 3 — "However" pivot:** a contrastive conjunction introducing a second process on the same compartment. *"However, as the people in the I population group recover."*
4. **Slot 4 — trial count:** the compartment size used as the number of trials. *"I(t)."*
5. **Slot 5 — success probability of the new process:** a single letter. *"r."*
6. **Slot 6 — random variable for the new process:** distributed uniform on [0,1]. *"Y."*

**How to fill with a DIFFERENT idea:** Pick a system with two linked compartments where one gains what the other loses. Replace slot 1 with the equivalent mirror statement, slot 2 with a conservation sentence, slot 3 with a "However" clause naming the second flow (recover / decay / be removed…), and re-use slots 4–6 for that second flow.

**Original filled version (this text):** *"The first part of this equation is the negative of Equation 8… However, as the people in in the I population group recover, the number of people in the I population group decreases. The number of trials performed… is I(t). The probability of success of the recovery is r."*

**Demonstration fill (different subject, same skeleton):** *The first part of this equation is the negative of Equation 10, as the amount of solvent leaving the beaker should equal the negative of the amount entering the solution. However, as the solute precipitates, the dissolved mass decreases. The number of trials performed on the dissolved mass is C(t). The probability of success of precipitation is p. E is a continuous random variable that is uniformly distributed between 0 and 1, governing whether a given particle nucleates in this step.*

---

## Express-Idea Vocabulary

**Sequencing / cross-referencing**
- *"Similar to Equation 2, the first part…"* — links a new equation to an old one as the entry move.
- *"(Refer to Equation 8)"* / *"(Refer to Equation 9)"* — explicit pointer that signals "now I unpack this".

**Cause / consequence / justification**
- *"as the number of people in the S population group must decrease as people get infected"* — "as … as" stacked clauses tying sign to behaviour.
- *"as the decrease of the number of people… should be equal to the negative of the increase"* — conservation reasoning used to justify a mirror equation.

**Contrast / concession**
- *"However, as the people in in the I population group recover, the number of people in the I population group decreases."* — "However" is the single pivot that opens a second process on the same compartment.

**Specification (defining a term inside the equation)**
- *"The probability of success of the infection is i."*
- *"The number of trials performed on the people in the I population group is I(t)."*
- *"The probability of success of the recovery is r."*

**Evidence handling**
- (None — the section is definitional, not evidentiary; no "according to" / "this suggests" is used.)

**Explanation verbs**
- *"represents the number of interactions between members of the S population group…"* — "represents" used to translate symbol → meaning.
- *"is a continuous random variable that is uniformly distributed between 0 and 1, simulating the underlying random probability…"* — "is" + present-participle ("simulating") defines and then unpacks role.
- *"is used here as the number of people… must decrease"* — "is used here as" justifies an operator.

---

## How to Explain an Idea (replication steps)

The pattern this section relies on is **comparison → left-to-right term definition → sign/operator justification → mirror equation → "However" pivot → left-to-right term definition again**. To explain a NEW idea with the same pattern:

1. **Caption the equation** on its own line with a label such as "Equation N — [what it computes]".
2. **Open with a comparison** to a previously explained equation (*"Similar to Equation X, the … part of the … represents …"*) so the reader imports a known scaffold.
3. **Define the trial / count term first**, in plain language, as a noun phrase.
4. **Define the probability parameter** as a single short clause (*"The probability of success … is [letter]."*).
5. **Define the random variable** with its distribution and its role in one sentence (*"[Letter] is a continuous random variable that is uniformly distributed between 0 and 1, [role]."*).
6. **Justify any sign or operator** with a behavioural clause (*"A negative sign is used here as … must decrease/increase."*).
7. **Caption the next equation** and **state its mirror relationship** to the previous one (*"The first part of this equation is the negative of Equation N …"*).
8. **Pivot with "However"** to introduce the second process acting on the same compartment.
9. **Re-run steps 3–5** in the same left-to-right order for the new process (trials → probability → random variable).
10. **Close** so that the reader ends on the random variable, mirroring the close of the previous paragraph.
