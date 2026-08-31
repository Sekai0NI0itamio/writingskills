# Idea Flow Notes: mathematics_7_may2020_2SyPx094JfmxwKa1 — function can then be calculated by replacing the summation in the RMSE formula with a definite integral, integrated from

## Paragraph Flow (move by move)

**Paragraph 1**
1. **Definition/method statement** — "function can then be calculated by replacing the summation in the RMSE formula with a definite integral" → hands to next sentence by *specification*: what exactly does this integral form look like?
2. **Mechanism/justification** — "The absolute value was included in the equation to help us calculate the difference between complex functions" → hands to next paragraph by *establishing purpose* that motivates the worked example to follow.

**Paragraph 2**
1. **Claim of equivalence** — "The MISE of two functions has the same definition in the time domain" → hands to next by *application*: if it holds in the time domain, let us use it there.
2. **Example introduction** — "Let us do a calculation for the MISE for the Fourier series with one term (n = 1)" → hands to next by *specification*: which functions are we comparing?
3. **Definition of f(t)** — "Let f(t) = 2t + 2, −1 < t ≤ 0 and −2t + 2, 0 < t ≤ 1" → hands to next by *pairing*: f needs a counterpart g.
4. **Definition of g(t) + transition signal** — "g(t) = 1 + Σ… cos(nπt), the MISE is then calculated as follows" → hands to next by *consequence*: now that both functions are defined, compute.
5. **Property identification + simplification** — "Since both f(t) and g(t) are both even functions, the integration of the difference… is also equal to two times the integral of either side" → hands to next paragraph by *method requirement*: the simplified integral still needs x-axis intersections to proceed.

**Paragraph 3**
1. **Method requirement** — "In order to calculate this integral, the intersections of the functions with the x-axis should be found" → hands to next by *problem identification*: can this be done analytically?
2. **Obstacle statement** — "Since 2t + 1 − cos(πt) = 0 is a non-linear function, the result is hard to determine using an analytical method" → hands to next by *contrast*: if not analytical, then what tool?
3. **Tool-based solution + evidence** — "Using Wolfram Alpha, an online calculator, the roots that were calculated were t ≈ −0.874, t = −0.5, and t ≈ −1.26" → hands to next paragraph by *enabling condition*: now the roots exist, substitution can proceed.

**Paragraph 4**
1. **Sign verification + transition** — "Since 2(−1) + 1 − cos(−π)/π = −1 + 1/π = −0.189 is negative, substituting the values into the integral gives" → hands to next by *consequence*: the sign determines how the absolute value splits the integral.
2. **Worked calculation (split integral)** — the integration is split at the roots and evaluated → hands to next by *completion*: the antiderivatives are found.
3. **Numerical result** — "= 0.0982" → ends the section by *delivering the verdict*.

---

## What This Section Does (content sequence)

1. **Generalises a formula** from discrete (summation/RMSE) to continuous (definite integral), with a citation anchoring the definition — establishes the mathematical tool before using it.
2. **Asserts domain applicability** — states the formula holds in the time domain, so the reader accepts the upcoming calculation is legitimate.
3. **Sets up a concrete worked example** — defines both the original function f(t) and its Fourier approximation g(t) — gives the calculation something to operate on.
4. **Identifies a simplifying property** — notes both functions are even, halving the work — reduces computational load before the reader sees the algebra.
5. **Identifies a computational obstacle** — the intersection equation is non-linear and resists analytical solution — justifies why an external tool is needed.
6. **Deploys a computational tool** — uses Wolfram Alpha, cites it, reports the roots — resolves the obstacle transparently.
7. **Verifies sign conditions** — checks the sign at a test point to determine how the absolute value splits the integral — ensures the split integral is set up correctly.
8. **Completes the calculation and reports the result** — evaluates the antiderivatives at the bounds and states the numerical MISE value — delivers the payoff the whole section built toward.

**Why this order:** each move creates the *precondition* for the next. You cannot compute MISE without defining the functions; you cannot integrate without finding roots; you cannot split the integral without checking signs. The sequence is *dependency-ordered*, not narrative-ordered.

---

## Paragraph Skeletons (replicable templates)

### Skeleton 1 — Tool Introduction with Justification

**Template:** "[Quantity] can then be calculated by replacing [discrete operation] with [continuous analogue], integrated from [lower bound] to [upper bound] for [condition]. [Feature of the formula] was included in the equation to help us [purpose] ([citation])."

1. **Slot 1 (quantity):** the name of the measure being computed — noun phrase, nominative.
2. **Slot 2 (discrete → continuous):** name the original discrete operation and its continuous replacement — verb phrase with "replacing… with…".
3. **Slot 3 (bounds + condition):** state the integration limits and the condition under which they apply — prepositional phrase.
4. **Slot 4 (feature + purpose):** identify one component of the formula and explain *why* it is there — past passive construction + infinitive of purpose.
5. **Slot 5 (citation):** parenthetical source reference.

**How to fill differently:** Pick any quantity that has both a discrete sum version and a continuous integral version (e.g., centre of mass, expected value). State the replacement, then justify one non-obvious component of your formula with a purpose clause.

**Original filled:** "function can then be calculated by replacing the summation in the RMSE formula with a definite integral, integrated from −L to L for a function with a period of 2L. The absolute value was included in the equation to help us calculate the difference between complex functions (Bevelacqua, n.d.)."

**Demonstration fill (different subject):** "The expected value can then be calculated by replacing the summation in the discrete probability formula with a definite integral, integrated from −∞ to ∞ for a continuous random variable. The probability density function was included in the equation to help us weight the outcomes by their likelihood (Ross, 2014)."

---

### Skeleton 2 — Worked Example Setup with Simplifying Property

**Template:** "[Measure] has the same definition in [context]. Let us do a calculation for [measure] for [specific case] (compared to [reference]). Let [variable A] = [definition A] and [variable B] = [definition B], [measure] is then calculated as follows. Since [shared property of A and B], [simplification of the calculation]."

1. **Slot 1 (equivalence claim):** assert the method transfers to a new context — declarative sentence.
2. **Slot 2 (example announcement):** introduce a specific case with a parameter value — imperative "Let us do a calculation for…".
3. **Slot 3 (variable definitions):** define the two objects being compared — "Let [A] = … and [B] = …".
4. **Slot 4 (transition signal):** announce the calculation begins — "is then calculated as follows".
5. **Slot 5 (property + simplification):** identify a symmetry or property shared by both objects, then state the computational shortcut it enables — "Since [property], [simplification]".

**How to fill differently:** Choose any measure that compares two objects (e.g., variance, distance, error). Define both objects concretely, then spot a shared symmetry that lets you halve or reduce the computation.

**Original filled:** "The MISE of two functions has the same definition in the time domain. Let us do a calculation for the MISE for the Fourier series with one term (n = 1) (compared to the original function). Let f(t) = {2t+2, −1<t≤0 / −2t+2, 0<t≤1} and g(t) = 1 + Σ…cos(nπt), the MISE is then calculated as follows. Since both f(t) and g(t) are both even functions, the integration of the difference… is also equal to two times the integral of either side."

**Demonstration fill (different subject):** "The variance of a dataset has the same definition in the frequency domain. Let us do a calculation for the variance for the first harmonic only (compared to the full signal). Let s(t) = sin(ωt) and h(t) = 0.5sin(ωt), the variance is then calculated as follows. Since both s(t) and h(t) are both odd functions, the integration of the squared difference is also equal to two times the integral over the positive half."

---

### Skeleton 3 — Obstacle Identification and Tool-Based Resolution

**Template:** "In order to [goal], [prerequisite] should be found. Since [equation] is a [type], the result is hard to determine using [method]. Using [tool], [result] was [obtained] ([citation])."

1. **Slot 1 (goal):** state what you need to achieve — infinitive phrase after "In order to".
2. **Slot 2 (prerequisite):** name the intermediate quantity that must be found — passive construction "should be found".
3. **Slot 3 (obstacle):** identify the equation and classify why it resists standard methods — "Since [equation] is a [type], the result is hard to determine using [method]".
4. **Slot 4 (tool + result + citation):** name the external tool, report the output, cite it — "Using [tool], [result] was [obtained] ([citation])".

**How to fill differently:** Pick any calculation that requires solving an equation you cannot solve by hand. Name the obstacle type (transcendental, non-linear, no closed form), then introduce a computational tool and report its output with a citation.

**Original filled:** "In order to calculate this integral, the intersections of the functions with the x-axis should be found. Since 2t + 1 − cos(πt) = 0 is a non-linear function, the result is hard to determine using an analytical method. Using Wolfram Alpha, an online calculator, the roots that were calculated were t ≈ −0.874, t = −0.5, and t ≈ −1.26 (WolframAlpha, 2009)."

**Demonstration fill (different subject):** "In order to calculate this area, the intersections of the curves with each other should be found. Since e^x − x² = 0 is a transcendental equation, the result is hard to determine using an analytical method. Using Desmos, an online graphing calculator, the roots that were calculated were x ≈ −0.703 and x ≈ 1.429 (Desmos, 2023)."

---

## Express-Idea Vocabulary

**Sequencing:**
- "the MISE is then calculated as follows" — signals the calculation begins after definitions are set
- "is also equal to two times the integral" — extends a result to a new case

**Cause/consequence:**
- "Since both f(t) and g(t) are both even functions" — introduces a property that causes a simplification
- "In order to calculate this integral, the intersections… should be found" — goal drives the next step
- "Since 2t + 1 − cos(πt) = 0 is a non-linear function, the result is hard to determine" — property causes a methodological dead-end

**Contrast/concession:**
- "is hard to determine using an analytical method" — concedes a limitation before pivoting to a tool

**Specification:**
- "The MISE of two functions has the same definition in the time domain" — specifies that the definition transfers
- "compared to the original function" — specifies the reference point for the comparison

**Evidence handling:**
- "(Bevelacqua, n.d.)" — anchors the formula definition to a source
- "(WolframAlpha, 2009)" — anchors numerical results to a computational tool

**Explanation verbs:**
- "was included in the equation to help us calculate" — justifies a formula component by purpose
- "can be calculated by replacing the summation… with a definite integral" — defines a method by analogy to a known one
- "is then calculated as follows" — signals a worked calculation is about to begin
- "substituting the values into the integral gives" — bridges from roots to the split integral

---

## How to Explain an Idea (replication steps)

**Pattern: Definition → worked example setup → simplification → obstacle → tool-based resolution → sign check → completed calculation.**

This is a **worked calculation with obstacle resolution** — the section defines a measure, sets up a concrete instance, hits a wall, borrows a tool, verifies, and finishes.

1. **State the general method** and justify one non-obvious component of its formula with a purpose clause and a citation.
2. **Assert the method applies in your working context** (e.g., "has the same definition in [domain]").
3. **Announce a specific worked example** with a parameter value and a reference point for comparison.
4. **Define both objects being compared** — give explicit formulas for each.
5. **Identify a shared symmetry or property** and state the simplification it enables (e.g., halving the integral, exploiting periodicity).
6. **Identify the next computational prerequisite** (e.g., roots, intersections, critical points).
7. **Classify the obstacle** — name the equation type that prevents an analytical solution.
8. **Introduce an external tool**, report its output, and cite it.
9. **Verify a sign or condition** at a test point to justify how the calculation splits or branches.
10. **Execute the calculation** through to a single numerical result, and state it explicitly.
