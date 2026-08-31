# Idea Flow Notes: biology_6_may2021_jqeZkGx0EglqCQ4V — be calculating the sum of squares of the model, which is represented by the equation

## Paragraph Flow (move by move)

**Paragraph 1** (the formula at the top, with the gloss below it)

- **Sentence 1 — formula presentation:** Displays `SSm = ∑(xk − x̄)²` as a centred equation. It hands off because the reader now needs to know *what the symbols mean* before the equation can mean anything.
- **Sentence 2 — definition/context (x̄):** "The mean of the different factors, or group intervals, must be calculated." This answers the implicit "what is x̄?" raised by the equation, and hands off by narrowing the definition to a *specific* set of means that must be named.
- **Sentence 3 — variable unpacking:** "x̄k represents the mean of the different factors where DV1 represents the root growth and DV2 represents the shoot growth." It picks up "different factors" from sentence 2 and specifies them, listing DV1 and DV2. It hands off by finally giving the reader enough labels to attempt a concrete calculation.

**Paragraph 2**

- **Sentence 1 — worked example, first instance:** "Factor 1's (the control group) mean of the first dependent variable is equal to (4.1 + 4.4 + 4.6 + 5 + 5.1 + 5.2 + 5.4) / 7 = 4.82857143." This *applies* the mean definition just given, on a specific case. It hands off because the model "(sum)/n" only has authority if it can be repeated for the other factors.
- **Sentence 2 — repetition across factors (DV1):** "The same steps can be repeated to give 1F2 = 5.75714286, DV1F3 = 6.7, DV1F4 = 5.07142857, and DV1F5 = 3.91428571." It *extends* sentence 1 via the "same steps can be repeated" hinge, and hands off by signalling that the same repetition must now be done for the *second* dependent variable.
- **Sentence 3 — repetition across factors (DV2):** "These steps can be repeated with the second dependent variable to give DV2F1 = 27.942857142857…" It mirrors the previous move and closes the paragraph by exhausting the per-factor means, handing off because the next step (the SSm calculation) needs a *total* mean to subtract from.

**Paragraph 3**

- **Sentence 1 — next prerequisite:** "The total means for both dependent variables are needed." It transitions from the per-factor means (now complete) to the next quantity the formula requires — a *global* mean per DV. The word "needed" hands off by signalling what's coming next is the values.
- **Sentence 2 — values delivered:** "For DV1, this is 5.2542857142857, and for DV2 it is 25.908571428571." It answers sentence 1 with the two numbers, and hands off because the reader has all per-factor means AND both total means — they can now *do* the SSm.
- **Sentence 3 — procedure instruction:** "Proceed to subtract the total means from each of the factor's means and then square it." It moves from data to *method*, telling the reader the operation sequence (subtract, square), and hands off by promising the reader a worked execution.
- **Sentence 4 — executed calculation (DV1):** "(4.82857143 − 5.75714286)² + … = 5.870416359." It *fulfils* the procedure of sentence 3 on DV1, and hands off by symmetry — DV2 still needs the same treatment.
- **Sentence 5 — result delivered (DV2):** "The second independent variable's SSm = 270.4565714." It mirrors sentence 4, closing the SSm block. The word "Then" at the top of the next paragraph is the explicit transition — the SSM is done, so the next required quantity (SSE) must be introduced.

**Paragraph 4**

- **Sentence 1 — next equation introduced:** "Then the squares of the error must be calculated, using the equation SSE = ∑ sk²(nk − 1)." It is a *transition + new definition*: SSM is done, so the next variance component (SSE) is named with its formula. The text cuts off mid-flow, so the paragraph's job is to *open* the next calculation block the same way paragraph 1 opened SSM.

## What This Section Does (content sequence)

1. **Equation first, definition second.** Show the formula, *then* explain its symbols. Order matters because the symbols ("xk", "x̄") carry no meaning until the reader sees them in situ; naming them after the formula turns the equation from a picture into an instruction.
2. **Worked example for ONE case.** Pick a single factor (Factor 1, DV1) and compute the prerequisite value (the group mean) explicitly. This is what the student can *verify*; one concrete pass builds the model the rest of the section reuses.
3. **Extension by "same steps can be repeated."** Use a single verbal hinge ("The same steps can be repeated", "These steps can be repeated with the second dependent variable") to roll the procedure across the remaining cells of the data matrix. Why this order: one worked case proves the method; repetition *states* the rest without re-deriving it, which is how a long calculation stays readable.
4. **Introduce the NEXT prerequisite for the formula.** State in plain words what is now "needed" (e.g. "The total means for both dependent variables are needed"), then deliver the values. The plain-English statement acts as a signpost so the reader isn't ambushed by another number.
5. **Procedure sentence, then worked execution.** Tell the reader the *operation* ("Proceed to subtract … then square it") in one sentence, then perform it across the cases in the next sentence(s). This split is what separates a calculation section from a list of numbers — the reader is told the rule, then watches it run.
6. **Move to the next formula with a temporal hinge.** Close the current quantity (SSM) and open the next (SSE) with a sequencing word ("Then"). The sequence SSM → SSE → SS total mirrors the order of the ANOVA decomposition itself, so the writing follows the *mathematical* order of operations.

A student replicating this with any other topic should follow: **formula → symbol definitions → one worked instance → "same steps repeated" sweep → name next prerequisite → deliver values → state the operation → execute it → hinge to the next formula.**

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Equation + Symbol Glossary" opener**

`[Equation in display form]. [Plain-language statement of what must be found/calculated first]. [Variable] represents [definition]; in [the investigated context] it [narrower application or instance].`

1. Slot 1 (equation): a centred, single-line statistical formula with subscripts — grammatically a noun phrase, no verb. Slot 2 (what's needed): one sentence using "must be calculated/needed" to flag the *next* quantity the formula requires. Slot 3 (variable gloss): a sentence using "[symbol] represents [general meaning] where [subscript] = [instance 1] and [subscript] = [instance 2]" — two parallel clauses joined by "and".
2. To refill: slot 1 = pull the most "official-looking" formula from your analysis (ANOVA F-statistic, chi-square, R², etc.) and typeset it centred. Slot 2 = name the very first sub-quantity the formula needs. Slot 3 = list the two or three variable names from the equation and tie each to a concrete measured thing in your IA.
3. Original fill: `SSm = ∑(xk − x̄)². The mean of the different factors, or group intervals, must be calculated. x̄k represents the mean of the different factors where DV1 represents the root growth and DV2 represents the shoot growth.`
4. Demo fill (different idea — a chi-square test of independence on a plant-fertiliser trial): `χ² = ∑((O − E)² / E). The expected counts for each cell must be calculated. Eij represents the expected count for cell (i, j) where row 1 = fertiliser A and row 2 = fertiliser B applied, and column 1 = seedlings germinated.`

**SKELETON B — "One worked case, then sweep"**

`[Specific case]'s ([role in study], e.g. control group) [quantity being computed] is equal to ([explicit list of raw values]) / [n] = [decimal result]. The same steps can be repeated to give [result for case 2], [result for case 3], ..., and [result for last case]. These steps can be repeated with the [second/parallel variable] to give [parallel results list].`

1. Slot 1: a fully written-out arithmetic expression with raw numbers, divided by n, equalling a long decimal — present tense, "is equal to". Slot 2: a "same steps can be repeated" hinge, then a comma-separated list of `[label] = [value]` for the remaining cases in the *same* variable. Slot 3: a "These steps can be repeated with the [parallel variable]" hinge and a parallel list.
2. To refill: slot 1 = pick the *first* row/column of your data table and write every value out; show the division. Slot 2 = mechanically compute the other rows, label each with the same naming convention (e.g. `F2`, `F3`…) and list them. Slot 3 = re-run the slot-1 procedure on your second measured variable using a parallel naming scheme (e.g. switch the prefix from `DV1` to `DV2`).
3. Original fill: `Factor 1's (the control group) mean of the first dependent variable is equal to (4.1 + 4.4 + 4.6 + 5 + 5.1 + 5.2 + 5.4) / 7 = 4.82857143. The same steps can be repeated to give 1F2 = 5.75714286, DV1F3 = 6.7, DV1F4 = 5.07142857, and DV1F5 = 3.91428571. These steps can be repeated with the second dependent variable to give DV2F1 = 27.942857142857, DV2F2 = 35.028571428571, DV2F3 = 31.785714285714, DV2F4 = 18.728571428571, and DV2F5 = 16.057142857143.`
4. Demo fill (different idea — reaction rates at five temperatures, measured as time-to-finish *and* colour intensity): `Temperature 1's (room temperature, the control) mean time-to-finish is equal to (3.2 + 3.5 + 3.1 + 3.4 + 3.3) / 5 = 3.30 s. The same steps can be repeated to give T2 = 2.74 s, T3 = 2.20 s, T4 = 1.88 s, and T5 = 1.62 s. These steps can be repeated with the second dependent variable (colour intensity) to give C1 = 0.41, C2 = 0.58, C3 = 0.69, C4 = 0.77, and C5 = 0.83.`

**SKELETON C — "Name the next prerequisite, then state the procedure, then execute"**

`The [next quantity, e.g. total means / overall variance] for [variable(s)] [is/are] needed. For [variable 1], this is [value], and for [variable 2] it is [value]. [Imperative: "Proceed to"/"Next,"] [operation 1] and then [operation 2] [each of the factor's values / across the cases]. Then [worked execution with bracketed arithmetic] = [final result].`

1. Slot 1: a one-sentence "what is needed" statement using "needed" or "must be found". Slot 2: parallel construction "For [A], this is X, and for [B] it is Y." Slot 3: an imperative or "Proceed to …" sentence stating the *sequence of operations* (subtract, square, sum). Slot 4: the calculation written out, case by case, ending in a single numeric result.
2. To refill: slot 1 = identify the next number the formula demands. Slot 2 = compute it for each variable and present in parallel clauses. Slot 3 = write one sentence that names the algebraic steps in plain English, in the *order* the formula prescribes. Slot 4 = execute step 3 inside a single long equation, using parentheses and superscripts, and close with `= [number]`.
3. Original fill: `The total means for both dependent variables are needed. For DV1, this is 5.2542857142857, and for DV2 it is 25.908571428571. Proceed to subtract the total means from each of the factor's means and then square it. Then add all of the values together to get the sum. The first dependent variable's SSm = … = 5.870416359.`
4. Demo fill (different idea — computing sum of squares between groups for the reaction-rate data above): `The grand means for both dependent variables are needed. For time-to-finish, this is 2.348 s, and for colour intensity it is 0.656. Proceed to subtract the grand mean from each temperature's mean and then square the result. Then multiply each squared deviation by the number of trials at that temperature and sum. The time-to-finish SSb = (5·(3.30 − 2.348)² + 5·(2.74 − 2.348)² + 5·(2.20 − 2.348)² + 5·(1.88 − 2.348)² + 5·(1.62 − 2.348)²) = 6.93.`

**SKELETON D — "Temporal hinge to the next formula"**

`Then the [next variance component / next quantity] must be calculated, using the equation [SSE / next formula] = [formula in display form].`

1. Slot 1: a single sentence opening with "Then" (sequencing), naming the next quantity, and ending with a "using the equation … = …" clause that reintroduces a fresh display formula.
2. To refill: name the very next quantity in the decomposition (SSM → SSE → SS total, or SSB → SSW → F), then write out its equation centred, in the same typographic style as the opener.
3. Original fill: `Then the squares of the error must be calculated, using the equation SSE = ∑ sk²(nk − 1).`
4. Demo fill: `Then the within-group sum of squares must be calculated, using the equation SSW = ∑ sk²(nk − 1).`

## Express-Idea Vocabulary

- **Sequencing (temporal/iterative):** "The same steps can be repeated" (sweeps across the remaining factors); "These steps can be repeated with the second dependent variable" (parallels the sweep onto a second variable); "Then" ("Then the squares of the error must be calculated" — opens the next formula block).
- **Cause/consequence:** "Proceed to subtract the total means … and then square it" (operational cause-effect; each operation is the consequence of needing the next quantity); "Then add all of the values together to get the sum" (purpose clause introduced by "to get").
- **Contrast/concession:** none in this section — the section is monotone-procedural, so this category is empty. (Worth flagging: a 6/7 student could still benefit from a single contrast if any step requires *not* doing something.)
- **Specification / narrowing:** "where DV1 represents the root growth and DV2 represents the shoot growth" (the "where … and …" structure narrows a general variable to two concrete instances).
- **Evidence handling:** "The total means for both dependent variables are needed. For DV1, this is …, and for DV2 it is …" (states a need, then delivers the numerical evidence in parallel clauses).
- **Explanation verbs / definitional patterns:** "represents" ("x̄k represents the mean of the different factors where DV1 represents the root growth and DV2 represents the shoot growth"); "is equal to" ("Factor 1's … mean of the first dependent variable is equal to (4.1 + …) / 7 = 4.82857143"); "must be calculated" ("The mean of the different factors … must be calculated"); "using the equation" ("using the equation SSE = …") — these are the verbs that *frame* a calculation as a defined procedure rather than a number drop.

## How to Explain an Idea (replication steps)

The section uses the **formula → symbol glossary → worked instance → "same steps" sweep → prerequisite → procedural instruction → execution → temporal hinge to next formula** pattern. A student replicating it on a new calculation should:

1. **State the master equation in display form** — centred, no surrounding prose, before any sentence that refers to its parts. The equation is the section's spine.
2. **Gloss the symbols in plain English immediately after** — one sentence for the *what* ("The X must be calculated"), one sentence for the *which* ("[symbol] represents [meaning] where [instance 1] and [instance 2]"). Never let a symbol appear in an equation before it has been named.
3. **Pick ONE concrete case and compute it explicitly** — show the raw values, the division/multiplication, and the decimal result. One case is the proof that the method works.
4. **Sweep the remaining cases with a "same steps can be repeated" hinge** — do *not* rewrite the arithmetic; list the results with consistent labels (`F2 = …, F3 = …`). This keeps the section short and signals that the method, not the arithmetic, is the point.
5. **Mirror the sweep onto any second variable** with the same hinge word ("These steps can be repeated with the second dependent variable"). Parallel structure here is what makes the two-variable analysis legible.
6. **Name the next prerequisite the formula needs** in a one-sentence "needed" statement before delivering any numbers — this is the signpost sentence.
7. **Deliver the prerequisite values in a parallel "For A, this is X, and for B it is Y" construction** — the parallelism makes the two variables comparable at a glance.
8. **Issue a procedural-imperative sentence** ("Proceed to …" / "Next, subtract … and then square it") that names the *operations* in the order the formula prescribes. This sentence is what separates a calculation from a dump of numbers.
9. **Execute the procedure in one long equation** with the arithmetic shown, case by case, ending in a single final number. Brackets and superscripts do the visual work.
10. **Close with a temporal hinge ("Then") that names the NEXT formula** (`SSE`, `SS total`, `F`, etc.), and display it. The section ends mid-procedure; that is the point — the next paragraph will mirror paragraphs 1–3 of this section.
