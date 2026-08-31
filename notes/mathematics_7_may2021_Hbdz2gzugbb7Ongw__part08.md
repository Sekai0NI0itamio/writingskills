# Idea Flow Notes: mathematics_7_may2021_Hbdz2gzugbb7Ongw — 3.2      The Euler-Lagrange equations of the system

## Paragraph Flow (move by move)

**Paragraph 1 — Setting up the two Euler–Lagrange equations**

1. **Sentence 1** — *context / method pointer:* "To get the equation of motion, one can simply use the Euler-Lagrange equation (eq. 5)."
   - **Hands to next sentence by *authority → application*:** the reader is told which established formula (eq. 5) is the tool; the next sentence must say how to specialise it.

2. **Sentence 2** — *specification / variable assignment:* "For this system, we can use two Euler-Lagrange equations, where q1 is θ1 and q2 is θ2:"
   - **Hands to the displayed equations by *consequence*:** once the variables are named, the only logical step is to write the two generic formulas in those variables — equations (22) and (23) appear directly below.

3. **Equations (22)–(23)** — *formal instantiation:* display of `d/dt(∂L/∂θ̇ᵢ) = ∂L/∂θᵢ` for i = 1, 2.
   - **Hands to the next paragraph by *specification of the next action*:** the reader now expects someone to actually *perform* the differentiation advertised in the formulas.

---

**Paragraph 2 — Performing the differentiation**

1. **Sentence 1** — *transition / verdict:* "Then, finally, we can derive the equations of motion."
   - "Then, finally" marks the **culmination** of the method set up in paragraph 1; it hands the reader to the procedural sentence by *cause → effect* (we have the template, so now we compute).

2. **Sentence 2** — *mechanism / procedure label:* "Differentiating, we get:"
   - A gerund acting as an instruction tag; hands to the displayed results by *cause* (the verb names the operation that produces the lines below).

3. **Equations (24)–(25)** — *evidence / worked result:* the four partial-derivative expressions after substitution of L.
   - These **hand to the final paragraph by *necessity***: the differentiated system is algebraically messy and explicitly stated as needing further rearrangement.

---

**Paragraph 3 — Rearranging for numerical use**

1. **Sentence 1** — *implication / purpose:* "These equations can then be transformed into a form suitable for numerical solving:"
   - "These equations" anchors back to (24)–(25); "then" marks *consequence*; "suitable for numerical solving" tells the reader *why* the rearrangement matters, setting up the displayed matrix-style rearrangement.

2. **Equations (26)–(27)** — *final worked form:* θ̈₁ and θ̈₂ isolated on the left.
   - The section ends with the form the simulation will consume — a **handoff by purpose**: the next section can now take these as input.

---

## What This Section Does (content sequence)

This is a **derivation bridge** section: it takes a previously defined tool (eq. 5) and turns it into the specific equations the rest of the paper will use. The ordered moves are:

1. **Cite the prior tool** (eq. 5). Sets up authority so the reader trusts the method.
2. **Specialise to the current system** (q1 = θ1, q2 = θ2). Translates abstract formula into concrete variables.
3. **Display the formal apparatus** (eqs. 22–23). Shows what will be differentiated.
4. **Announce the next action** ("derive the equations of motion"). Signals we are moving from template to computation.
5. **Name the operation** ("Differentiating"). Tells the reader exactly what procedure produced the block below.
6. **Show the differentiated result** (eqs. 24–25). Delivers the raw post-differentiation expressions.
7. **Motivate a transformation** ("suitable for numerical solving"). Explains *why* an algebraic rewrite is needed — to feed a computer.
8. **Display the solved-for-accelerations form** (eqs. 26–27). Delivers the input-ready form for the next section.

**Why this order:** each step is a prerequisite for the next — you cannot specialise variables without the formula, cannot differentiate without the substituted form, and cannot numerically integrate without isolating θ̈ on one side. The structure is *method → instantiation → execution → repackaging*.

---

## Paragraph Skeletons (replicable templates)

### Skeleton A — Setup paragraph
> "To get the equation of motion, one can simply use the Euler-Lagrange equation (eq. 5). For this system, we can use two Euler-Lagrange equations, where q1 is θ1 and q2 is θ2:"

**Slots:**
1. Goal phrase (noun phrase: "the equation of motion")
2. Citation to a prior established formula in the paper (parenthetical: "(eq. X)")
3. System noun ("this system")
4. Number of equations to apply
5–6. Two variable assignments ("q1 is θ1" / "q2 is θ2")

**How to fill with a DIFFERENT idea:**
- Slot 1: name the final quantity you want (e.g. "the trajectory", "the energy spectrum").
- Slot 2: cite the equation you already derived earlier (e.g. "eq. 3").
- Slot 3: name your system in one phrase ("the driven RLC circuit").
- Slot 4: count the degrees of freedom you need.
- Slots 5–6: pick the two generalised coordinates of your system and assign them to q1, q2.

**Original filled version:** as quoted above.

**Demonstration fill (different subject):**
> "To get the energy eigenvalues, one can simply use the Schrödinger equation (eq. 2). For the particle-in-a-box, we can use one time-independent Schrödinger equation, where the variable x is constrained to the interval 0 ≤ x ≤ L:"

---

### Skeleton B — Derivation paragraph
> "Then, finally, we can derive the equations of motion. Differentiating, we get:"

**Slots:**
1. Closing transition adverb + "we can derive" + the deliverable noun phrase.
2. Gerund naming the mathematical operation performed, followed by a colon.

**How to fill with a DIFFERENT idea:**
- Slot 1: keep "Then, finally, we can derive" — these are *pure connectors* — and replace only the deliverable noun ("the equations of motion") with what your derivation will produce.
- Slot 2: name the *next* algebraic step you are about to perform ("Integrating", "Substituting", "Expanding", "Applying the chain rule").

**Original filled version:** as quoted above.

**Demonstration fill:**
> "Then, finally, we can derive the dispersion relation. Substituting the trial wavefunction into the time-independent equation, we get:"

---

### Skeleton C — Repackaging paragraph
> "These equations can then be transformed into a form suitable for numerical solving:"

**Slots:**
1. Anaphoric reference to the equations just derived ("These equations").
2. Sequential connector ("can then").
3. The end-purpose that motivates the rewrite ("suitable for numerical solving").

**How to fill with a DIFFERENT idea:**
- Slot 1: keep "These equations" (anaphora is reusable).
- Slot 2: keep "can then".
- Slot 3: replace "numerical solving" with whatever use-case your rearranged form serves ("suitable for matrix diagonalisation", "suitable for comparison with experimental data", "suitable for dimensional analysis").

**Original filled version:** as quoted above.

**Demonstration fill:**
> "These equations can then be transformed into a form suitable for comparison with the experimental decay curve:"

---

## Express-Idea Vocabulary

- **Sequencing / transition:** "Then, finally, we can derive the equations of motion." — uses stacked adverbs to mark culmination.
- **Sequencing / handoff:** "These equations can then be transformed" — anaphoric "These" + "can then" to chain to the next step.
- **Specification / variable assignment:** "where q1 is θ1 and q2 is θ2:" — "where" introduces the mapping clause.
- **Purpose / goal framing:** "To get the equation of motion, one can simply use" — infinitive-of-purpose opens the section.
- **Procedure verbs (gerunds):** "Differentiating, we get:" — labels the operation that produces the displayed result.
- **Method-pointer verbs:** "one can simply use the Euler-Lagrange equation" — "can simply use" frames the tool as readily available from earlier work.
- **Implication / use-cue:** "a form suitable for numerical solving:" — "suitable for" names the downstream consumer of the result.
- **Evidence handling:** none in the connective sense — instead, equations themselves act as evidence, introduced by "we get:".

---

## How to Explain an Idea (replication steps)

The pattern this section relies on is: **tool-citation → specialisation → procedure-label → worked result → repackage-for-use**.

Step-by-step instructions to replicate with a NEW derivation:

1. **Open with an infinitive-of-purpose that names the target output** and the tool that will produce it; cite the tool by equation number from earlier in the paper so the reader does not have to relearn it. ("To get [X], one can simply use [Y] (eq. [N]).")
2. **State how many times the tool must be applied** and assign your system's variables to the tool's generic placeholders, separated by "where". ("For this [system], we can use [k] [tools], where [a] is [α] and [b] is [β]:")
3. **Display the resulting formal equations.** Do not yet compute — show the generic structure with your variables plugged in.
4. **Mark the move to computation** with a closing adverb cluster ("Then, finally, we can derive [X].").
5. **Label the mathematical operation** in a single gerund + colon ("Integrating, we get:", "Differentiating, we get:", "Substituting, we get:") so the reader knows what procedure produced the block beneath.
6. **Show the worked intermediate result.** Let it be algebraically heavy — this is honest about the work done.
7. **Justify the next rewrite** by naming the downstream consumer ("a form suitable for [numerical solving / plotting / comparison]").
8. **Display the final, consumer-ready form.** End the section here so the next section can pick up the equation as its input.
