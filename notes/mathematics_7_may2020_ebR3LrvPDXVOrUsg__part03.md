# Idea Flow Notes: mathematics_7_may2020_ebR3LrvPDXVOrUsg — Noticing that repeatedly applying this matrix to a vector would provide me with the

## Paragraph Flow (move by move)

**Paragraph 1** (conjecture-setup, 4 sentences)

1. **Move: motivation / method declaration.** *"I first attempted to find a pattern within the actual matrix."* — declares the student's investigative move (find a pattern, not prove a formula). Hands the reader into **Sentence 2** by *naming the object whose pattern is wanted* — you can't look for a pattern until you have named the thing being patterned.
2. **Move: definition + mechanism.** *"If the vector with the n-th and (n + 1)th term is V, then applying M V once, produces the next term"* — defines the input vector *and* the operation that advances the sequence. Hands the reader into **Sentence 3** by *exposing verbosity*: the writer just wrote out "applying M V once / applying M again" in full, so a compact symbol is the natural next step.
3. **Move: notation shorthand.** *"For simplicity, we denote applying a matrix n times as M n"* — introduces the compact algebraic symbol. Hands the reader into **Sentence 4** by *unblocking the claim*: now that the repetition has a name, the general claim becomes writable in one line.
4. **Move: base-case assumption + synthesis claim.** *"Assuming F0 = 0 and F1 = 1, applying M n to the vector h1, 0i would provide the output vector"* — fixes starting values and states the general formula the section is advancing. Hands the reader into **Paragraph 2** by *consequence*: a claim about every n is now on the table, so the next job is to *test it on small cases*.

**Paragraph 2** (evidence display, 1 sentence + display)

1. **Move: procedural step (announce the test).** *"First, I calculated the matrix multiplications to get an idea of what M n might look like:"* — explicitly labels the next move as exploratory calculation, *not* a proof. Hands the reader into **the displayed matrices** by *promising the evidence*: the colon + display is the fulfillment of "to get an idea."
2. **Move: displayed computation (M¹, M², M³, M⁴).** *"M ⇒ M² ⇒ M³ ⇒ M⁴"* — visual chain showing that each new matrix's top-left entry is the next Fibonacci number. Hands the reader (implicitly, beyond this section) toward *generalising* the visible regularity into the closed-form matrix that comes later.

---

## What This Section Does (content sequence)

This is a **"conjecture-setup before general proof"** section. The ordered content moves are:

1. **Name what you are looking for** (a pattern inside the matrix). — sets the section's purpose.
2. **Define the input object and the recurrence operation** (V holds two consecutive Fibonacci terms; M V shifts forward one step). — without this, the reader cannot parse any later claim.
3. **Introduce compact notation for repeated application** (M^n). — makes the general claim possible in one line.
4. **State base-case assumptions and the general claim** (F0=0, F1=1; M^n·[1,0]ᵀ gives the (n+1)th and (n+2)th term). — delivers the section's takeaway sentence.
5. **Announce that small cases will be computed** ("First, I calculated…"). — pivots from symbolic claim to numerical evidence.
6. **Display the small-case calculations** (M¹ through M⁴). — delivers the promised evidence so the reader can see the pattern before the closed-form derivation arrives later.

The order matters because each move is a *prerequisite for the next*: you cannot write the compact claim (4) without the symbol (3), the symbol (3) is useless without the defined operation (2), and the operation (2) is ungraspable until the reader knows what pattern you are hunting (1). The calculation block (5–6) is placed *after* the claim so the claim can frame what the calculation is supposed to show.

---

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Conjecture-with-notation paragraph"**
`"[Topic], I first attempted to find a pattern within [object]. If [input] is [symbol], then [operation] produces [result]; [operation] again produces [result] and so forth. For simplicity, we denote [repeated operation n times] as [symbol]. Assuming [base case 1] and [base case 2], [operation on input] would provide [output]."`

1. **What each slot holds:**
   - Slot 1 ("[Topic], I first attempted to find a pattern within [object]") — present-perfect/infinitive clause naming the problem and the searched-for pattern; grammatical shape: noun phrase + past-tense verb phrase.
   - Slot 2 ("If [input] is [symbol], then…") — conditional defining the input object; grammatical shape: "if … then …" with a symbol defined *on the right* of "is".
   - Slot 3 ("[operation] produces [result]; [operation] produces [result] and so forth") — mechanism shown twice with the repetition phrase tail; grammatical shape: parallel "produces" clauses joined by a semicolon.
   - Slot 4 ("For simplicity, we denote… as [symbol]") — notation declaration; grammatical shape: fronted prepositional phrase ("For simplicity") + present-tense "we denote".
   - Slot 5 ("Assuming [base case 1] and [base case 2]") — assumption clause; grammatical shape: participial ("Assuming…") fronted before the main clause.
   - Slot 6 ("…would provide [output]") — synthetic claim; grammatical shape: conditional modal "would provide" + precise output description.
2. **How to fill with a DIFFERENT idea:** Pick any recurrence defined by a single linear operation (geometric growth, loan amortisation, population model). Pick two consecutive terms of the recurrence as your input vector. Name one transformation that advances the sequence by one step. Pick two concrete base values. Pick a symbol (a letter with a superscript) for repeating the transformation n times.
3. **Original filled version:** *"Fibonacci sequence, I first attempted to find a pattern within the actual matrix. If the vector with the n-th and (n + 1)th term is V, then applying M V once, produces the next term; applying M again produces the next term and so forth. For simplicity, we denote applying a matrix n times as M n . Assuming F0 = 0 and F1 = 1 , applying M n to the vector h1, 0i would provide the output vector with the (n + 1)th and (n + 2)th term of the Fibonacci sequence."*
4. **Demonstration fill (different idea, same skeleton):** *"Geometric growth, I first attempted to find a pattern within the multiplier itself. If the amount after k periods is A, then multiplying A by r once produces the next period's amount; multiplying again produces the period after and so forth. For simplicity, we denote multiplying r a total of n times as r^n. Assuming A0 = P and r is fixed, multiplying r^n by P would provide the value at period n+1."*

---

**SKELETON B — "Announce-then-display computation paragraph"**
`"First, I [past-tense verb] the [operations] to get an idea of what [symbol] might look like: [displayed computations]."`

1. **What each slot holds:**
   - Slot 1 ("First, I [verb] the [operations]") — sequencing adverb + first-person past tense; signals the section is about to *show evidence*, not derive.
   - Slot 2 ("to get an idea of what [symbol] might look like") — purpose clause with hedged modal "might"; grammatical shape: infinitive of purpose + "of what" + noun phrase.
   - Slot 3 ("[displayed computations]") — visual/numerical block; the colon *earns* this block.
2. **How to fill with a DIFFERENT idea:** Pick a quantity whose general form you have just symbolised. Compute 3–5 small cases by hand. Lead with "First,"; choose a verb that names the arithmetic done (compute, calculate, tabulate). Add "to get an idea" to signal the exploration is provisional. End with a colon and line up the results so the pattern is visible at a glance.
3. **Original filled version:** *"First, I calculated the matrix multiplications to get an idea of what M n might look like:"* followed by the chain M¹ → M² → M³ → M⁴ with each Fibonacci pair visible in the top row.
4. **Demonstration fill (different idea, same skeleton):** *"First, I tabulated the compounded amounts to get an idea of what r^n might look like: 1.05¹ = 1.0500, 1.05² = 1.1025, 1.05³ = 1.1576, 1.05⁴ = 1.2155."*

---

## Express-Idea Vocabulary

**Sequencing / shorthand-introduction**
- *"For simplicity, we denote applying a matrix"* — fronted purpose phrase used to license introducing a new symbol.
- *"First, I calculated the matrix multiplications"* — ordinal adverb that signals the *first* of multiple investigative steps.

**Specification / precision**
- *"the (n + 1)th and (n + 2)th term of the Fibonacci sequence"* — exact, parenthetical indexing that pins down what the output vector contains.

**Assumption-handling**
- *"Assuming F0 = 0 and F1 = 1"* — participial "Assuming" fronting two parallel base values, separating "given" from "to show".

**Hedged evidence-handling**
- *"to get an idea of what M n might look like"* — infinitive of purpose with epistemic modal "might"; signals the calculation is illustrative, not a proof.

**Explanation verbs (definition / mechanism / synthesis)**
- *"the vector … is V"* — defining "is" used to name an input object.
- *"applying M V once, produces the next term"* — "produces" used as the mechanism verb for a recurrence step.
- *"applying M n … would provide the output vector"* — "would provide" used as the synthesis verb for the general claim.

---

## How to Explain an Idea (replication steps)

**The pattern:** **Define the input → state the advancing operation → compress repetition into a symbol → fix base cases → state the general claim → test on small cases.** (A "conjecture-before-proof" exposition pattern.)

Numbered replication steps for a NEW idea:

1. **Pick a recurrence that is driven by one repeatable operation** (e.g. multiplication by a constant, rotation by an angle, application of a transformation). If the recurrence is not driven by *one* operation, stop — this pattern will not carry it.
2. **Define the input as an object that holds the state needed to advance the sequence** (a vector of two consecutive terms, an angle + step, a position + velocity). Use a single letter for it.
3. **Write the operation in plain English twice with the word "and so forth"**, so the reader sees the repetition explicitly before you compress it.
4. **Introduce a compact symbol for "do it n times"** using the format "[operation]^n" or equivalent. Lead the sentence with "For simplicity, we denote …".
5. **State base cases explicitly** ("Assuming initial value = X, second value = Y"). Put this in a participial clause at the front of the sentence.
6. **Write the general claim** in the form "[symbol] applied to [base input] would provide [output]", using the modal "would" — it is a conjecture, not yet a theorem.
7. **Pivot to small cases** with "First, I [past tense verb] the [operations] to get an idea of what [symbol] might look like:" and display 3–5 hand-computed instances whose pattern is *visible by eye*. The pattern you display must visibly match the general claim from step 6, otherwise the reader will distrust the coming derivation.
