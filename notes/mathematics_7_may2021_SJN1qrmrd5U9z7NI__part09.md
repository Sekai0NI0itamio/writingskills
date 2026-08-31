# Idea Flow Notes: mathematics_7_may2021_SJN1qrmrd5U9z7NI — While this inaccuracy can be seen through visual observation, I decided to calculate the percentage

## Paragraph Flow (move by move)

**Paragraph 1** (the prose block sandwiched between the formula and Table 4)

**Sentence 1:** *"I used this formula to calculate the percentage error for each of my 86 values."*
- **Move:** retrospective method claim — announces in past tense what the author did with the tool introduced above.
- **Hand-off:** the dataset is large (86 values), so the reader cannot see all of it inline; this creates a logical need for the next sentence to address how the evidence is distributed.

**Sentence 2:** *"A portion of the percentage error calculations is seen in Table 4, with the complete calculations found under Appendix 3."*
- **Move:** evidence locator + scope qualifier — names where the visible proof lives and where the full record lives.
- **Hand-off:** because the sentence promises a "portion" of "calculations," the table that follows is the immediate satisfaction of the locator, and the appendix reference satisfies the completeness promise.

**Then the table itself** functions as the visual evidence: each row is one worked instance of the formula, and the column headers ("Actual Rating," "Equation 1 Rating," "Percentage Error") map directly back to the variable definitions (υA, υC, δ) defined two moves earlier — closing the tool → tool-explanation → application → evidence loop.

---

## What This Section Does (content sequence)

This is a **worked-calculation section** with the following ordered moves:

1. **Tool display** — the formula appears as a math object so the reader can see the operation in full.
2. **Tool explanation** — every symbol is decoded in a stacked block (δ = …, υA = …, υC = …).
3. **Application claim** — a single past-tense sentence says the author ran the tool on the full dataset.
4. **Scope qualifier / evidence split** — the author acknowledges the dataset is too large for the body, and splits it into a visible subset and a back-matter copy.
5. **Sampled evidence (table)** — a portion is shown as a table with named columns and concrete rows.
6. **Cross-reference** — the appendix is named by number for completeness.

**Why this order:** the tool must appear before it can be applied; the symbol definitions must appear before the application sentence can be understood (because "percentage error" is the defined term being claimed); the application sentence must precede the scope qualifier because the qualifier is a restriction on the application just claimed; the table must follow the qualifier because the qualifier names the table as its referent. Each move sets up the vocabulary or referent the next move needs.

---

## Paragraph Skeletons (replicable templates)

**SKELETON A — Application claim**
`"I used this formula to calculate [quantity] for each of my [N] values."`

1. **Slots:**
   - `[quantity]` — noun phrase naming the formula's output (e.g., "the percentage error").
   - `[N]` — numeric count of total data points.
2. **How to fill differently:** pick a calculation you actually performed; state its output as a noun phrase; count how many times you ran it.
3. **Original fill:** *"I used this formula to calculate the percentage error for each of my 86 values."*
4. **Demo fill (different idea):** *"I used this equation to compute the damping coefficient for each of my 12 trials."*

---

**SKELETON B — Scope qualifier with split evidence**
`"A portion of the [data-noun] is seen in [Table N], with the complete [data-noun] found under [Appendix M]."`

1. **Slots:**
   - `[data-noun]` — noun matching the type of calculation/result.
   - `[Table N]` — in-text table reference.
   - `[Appendix M]` — back-matter reference.
2. **How to fill differently:** choose a large dataset; name what one row contains; number your visible table and your appendix consistently.
3. **Original fill:** *"A portion of the percentage error calculations is seen in Table 4, with the complete calculations found under Appendix 3."*
4. **Demo fill (different idea):** *"A portion of the reaction-rate calculations is shown in Table 2, with the complete calculations found under Appendix 5."*

---

**SKELETON C — Tool introduction with stacked definitions**
`"[quantity] of each [unit] through the following formula:" + displayed equation + stacked "symbol = plain-English meaning" lines.`

1. **Slots:**
   - Lead-in clause stating what is being computed of each item.
   - Centered/math-displayed equation.
   - One definition line per symbol, each in the form "symbol = definition".
2. **How to fill differently:** state the dependent variable's name; write the equation using standard notation; list every symbol on its own line with a written-out meaning that includes the units or context.
3. **Original fill:** *"error of each point through the following formula:"* followed by `δ = |(υA − υC)/υC| × 100` and the lines `δ = percentage error`, `υA = Actual value (actual Goodreads rating)`, `υC = Calculated Value (rating predicted by Equation 1)`.
4. **Demo fill (different idea):** *"efficiency of each turbine through the following formula:"* followed by `η = (P_out / P_in) × 100` and the lines `η = efficiency`, `P_out = output power (W)`, `P_in = input power (W)`.

---

## Express-Idea Vocabulary

**Tool introduction:**
- *"through the following formula"* — "error of each point through the following formula"

**Definition (mathematical, stacked form):**
- *"= percentage error"* — symbol-decoding line for δ
- *"= Actual value (actual Goodreads rating)"* — symbol-decoding line for υA
- *"= Calculated Value (rating predicted by Equation 1)"* — symbol-decoding line for υC

**Method / application verb:**
- *"I used this formula to calculate"* — "I used this formula to calculate the percentage error"

**Scope / distribution of evidence:**
- *"A portion of"* — "A portion of the percentage error calculations"
- *"is seen in"* — "is seen in Table 4"
- *"with the complete … found under"* — "with the complete calculations found under Appendix 3"

**Note on connectives:** this section is sparse on explicit verbal linkers ("however," "therefore," "in particular" etc.). Its logic moves through **structure** (formula → definitions → claim → table) rather than through connectives — each block is positioned so the previous one has supplied the vocabulary the next one needs.

---

## How to Explain an Idea (replication steps)

**Pattern used here:** *TOOL → TOOL-EXPLAIN → APPLICATION → SCOPE-QUALIFY → SAMPLED-EVIDENCE → FULL-EVIDENCE-LOCATION* (a worked-calculation explanation).

1. **Show the tool.** Display the formula/equation as a math object the reader can read in full — centred, with standard notation.
2. **Explain every part of the tool.** Below the equation, list each symbol on its own line as `symbol = plain-English meaning`, including the units or context where useful.
3. **State that you used it.** Write one past-tense sentence: *"I used this formula to calculate [output] for each of my [N] values."* This is the bridge from tool to evidence.
4. **Split the evidence.** In the next sentence, acknowledge the dataset is too large for the body: *"A portion of the [calculations] is seen in [Table N], with the complete [calculations] found under [Appendix M]."* Name both locations by number.
5. **Show the visible portion as a table.** Build a table whose column headers map directly onto the symbol definitions from step 2 (so the reader can verify each row using the equation from step 1). Include a handful of representative rows — different magnitudes, not just one cluster.
6. **Close the loop.** The table's columns reuse the vocabulary defined in step 2, so the reader can mentally re-run the formula on any row. The appendix reference from step 4 confirms completeness without bloating the body.
