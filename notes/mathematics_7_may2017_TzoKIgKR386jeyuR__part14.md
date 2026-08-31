# Idea Flow Notes: mathematics_7_may2017_TzoKIgKR386jeyuR — Equations

## Paragraph Flow (move by move)

**Paragraph 1** (Equations 1–6):

**Move 1** — *Definition.* "The Binomial Probability Distribution Function" — establishes the foundational probability model. It hands the reader the statistical basis that the later stochastic equations depend on (cause).

**Move 2** — *Definition/mechanism.* "The rate of change of the number of people in the S population group over time in a DSIRM" — defines the susceptible compartment's dynamics. It hands the reader the first piece of the epidemiological system (specification).

**Move 3** — *Definition/mechanism.* "The rate of change of the number of people in the I population group over time in a DSIRM" — defines the infected compartment's dynamics. It hands the reader the infection flow that the S equation feeds into (cause).

**Move 4** — *Definition/mechanism.* "The rate of change of the number of people in the R population group over time in a DSIRM" — defines the recovered compartment's dynamics. It hands the reader the final compartment completing the trio (completion).

**Move 5** — *Definition/transition.* "The fundamental approximation in Euler's method" — introduces the numerical discretisation tool. It hands the reader the method required to convert the continuous rates into computable steps (cause).

**Move 6** — *Mechanism/synthesis.* "Equation for the DSIRM" — combines Equations 2–4 with Equation 5 into one discrete iterative form. It hands the reader the working deterministic model ready for calculation (consequence).

**Paragraph 2** (Equations 7–10):

**Move 1** — *Definition.* "The ICBPDF" — introduces the inverse cumulative binomial sampling function. It hands the reader the stochastic tool that replaces deterministic rates with random draws (cause).

**Move 2** — *Mechanism.* "The change of the number of people in the S population group over time in a PSIRM" — applies the ICBPDF to the S compartment. It hands the reader the first stochastic update equation (specification).

**Move 3** — *Mechanism.* "The change of the number of people in the I population group over time in a PSIRM" — applies the ICBPDF to the I compartment with a recovery subtraction term. It hands the reader the infection dynamics in the stochastic model (specification).

**Move 4** — *Mechanism.* "The change of the number of people in the R population group over time in a PSIRM" — applies the ICBPDF to the R compartment. It hands the reader the complete stochastic model (completion).

---

## What This Section Does (content sequence)

1. **Foundational distribution** (Equation 1): Establishes the binomial probability model as the statistical backbone. This sets up the ICBPDF that appears later.
2. **Continuous compartmental rates** (Equations 2–4): Defines the deterministic DSIRM model by specifying how each population (S, I, R) changes continuously. This sets up the system that needs a numerical solution.
3. **Numerical approximation method** (Equation 5): Introduces Euler's method as the tool to convert continuous derivatives into discrete steps. This sets up the discretisation of Equations 2–4.
4. **Discrete DSIRM equation** (Equation 6): Combines the continuous rates with Euler's method into one iterative equation. This sets up the deterministic computational model.
5. **Stochastic sampling function** (Equation 7): Defines the ICBPDF as the inverse function for random parameter sampling. This sets up the stochastic extension of the model.
6. **Stochastic PSIRM equations** (Equations 8–10): Applies the ICBPDF to each compartment, replacing deterministic rates with stochastic draws. This produces the final probabilistic model.

The order moves from **statistical foundation → deterministic continuous model → numerical method → deterministic discrete model → stochastic function → stochastic model**, so each step supplies the tool or theory the next requires. A student replicating this would present any new idea by first establishing its mathematical basis, then its continuous form, then the solution method, then the discrete version, and finally the stochastic extension.

---

## Paragraph Skeletons (replicable templates)

**Skeleton 1:**
"`[mathematical expression]` is identified as `[term label]`; it represents `[what the expression describes]`."

1. **Slot shapes:** Slot 1 — a formula in notation (noun phrase); Slot 2 — a standardised name (noun phrase); Slot 3 — a relative clause stating the phenomenon captured.
2. **How to fill differently:** Pick any formula you encounter; label it with its conventional name; state in one clause what physical or mathematical phenomenon it quantifies.
3. **Original filled:** "`𝑃(𝑋 = 𝑥) = (𝑛𝑥)𝑝ˣ(1−𝑝)ⁿ⁻ˣ, 𝑥 = 0, 1, 2, … 𝑛`" is identified as "The Binomial Probability Distribution Function"; it represents the probability of x successes in n independent trials.
4. **Demonstration fill:** "`𝑓(𝑥) = (𝜆ˣ𝑒^(−𝜆))/𝑥!`" is identified as "The Poisson Probability Mass Function"; it represents the probability of x events occurring in a fixed interval.

**Skeleton 2:**
"`The rate of change of [quantity] in [population group] over time in [model type]` is given by `[derivative expression]`."

1. **Slot shapes:** Slot 1 — the dependent variable being modelled (noun phrase); Slot 2 — the compartment label (noun phrase); Slot 3 — the model/system name (noun phrase); Slot 4 — a differential expression (noun phrase with derivative notation).
2. **How to fill differently:** Choose any system with flowing quantities; name the variable; name the compartment; name the system; write its derivative expression using standard notation.
3. **Original filled:** "The rate of change of the number of people in the S population group over time in a DSIRM" is given by "𝑑𝑆(𝑡)/𝑑𝑡 = −𝑆(𝑡)/𝑁 × 𝐼(𝑡)/𝑁 × 𝑖 × 𝑁 × 𝛼".
4. **Demonstration fill:** "The rate of change of the concentration of reactant A in a batch reactor over time" is given by "𝑑[A]/𝑑𝑡 = −𝑘[A][B]".

**Skeleton 3:**
"`[Discrete equation label]` combines `[source continuous equations]` with `[numerical method]` to produce `[iterative computational form]`."

1. **Slot shapes:** Slot 1 — the equation number and label (noun phrase); Slot 2 — the equations being synthesised (noun phrase); Slot 3 — the bridging method (noun phrase); Slot 4 — the resulting discrete form (noun phrase).
2. **How to fill differently:** Identify which continuous equations you are discretising; name the numerical method that bridges them; state the resulting iterative equation's purpose.
3. **Original filled:** "Equation for the DSIRM" combines Equations 2–4 with "Euler's method" to produce the iterative form "𝑆₁ = 𝑆₀ + Δ𝑡 × 𝑑𝑆(𝑡)/𝑑𝑡".
4. **Demonstration fill:** "The discrete logistic growth equation" combines the continuous rate equation with "Euler's forward step" to produce "𝑥ₙ₊₁ = 𝑥ₙ + 𝑟𝑥ₙ(1 − 𝑥ₙ/𝐾)".

**Skeleton 4:**
"`The change of [quantity] in [population group] over time in [model type]` uses `[sampling function]` with `[parameters]`."

1. **Slot shapes:** Slot 1 — the type of change (noun phrase); Slot 2 — the compartment (noun phrase); Slot 3 — the model variant (noun phrase); Slot 4 — the inverse sampling function (noun phrase); Slot 5 — the parameters passed (noun phrase).
2. **How to fill differently:** Choose a compartment in a stochastic model; name the change type; name the model; identify the inverse cumulative sampling function and its parameters.
3. **Original filled:** "The change of the number of people in the S population group over time in a PSIRM" uses "InvBi(𝑆(𝑡)/𝑁 × 𝐼(𝑡)/𝑁 × 𝑁 × 𝛼, 𝑖, 𝑋)".
4. **Demonstration fill:** "The change of the number of infected individuals over time in a stochastic SEIR model" uses "InvBi(𝛽𝑆𝐸/𝑁, 𝜎, 𝑌)".

---

## Express-Idea Vocabulary

**Definition / labeling:**
- "The [X] is [term]" — assigns a standard mathematical identity to each expression. Example: "The Binomial Probability Distribution Function" (Equation 1 label).
- "The ICBPDF" — introduces the abbreviation for the inverse cumulative binomial function (Equation 7 label).

**Specification:**
- "The rate of change of the number of people in the" — pinpoints which compartment and which model variant each differential equation addresses. Example: "The rate of change of the number of people in the S population group over time in a DSIRM" (Equation 2).
- "The change of the number of people in the" — pinpoints which compartment's stochastic update each equation defines. Example: "The change of the number of people in the I population group over time in a PSIRM" (Equation 9).
- "The fundamental approximation in" — specifies the mathematical role of Equation 5 within Euler's method. Example: "The fundamental approximation in Euler's method" (Equation 5).

**Synthesis / equivalence:**
- "Equation for the" — labels a composite equation that merges prior components. Example: "Equation for the DSIRM" (Equation 6 label).

**Authority / citation:**
- "(Fabio 530)" — attributes the binomial formula to a source immediately after its expression. Example: "(Fabio 530)" following Equation 1.

---

## How to Explain an Idea (replication steps)

The pattern this section relies on is **Label → Formula → Contextual specification** (with citation where the formula is borrowed).

Step 1: Assign the equation a number and a descriptive label that names the mathematical concept in plain terms (e.g., "The Binomial Probability Distribution Function").
Step 2: Write the formal mathematical expression using standard notation, including all variables and their domains or ranges.
Step 3: If the formula is sourced from a reference, append a parenthetical citation immediately after the expression.
Step 4: For each new equation, specify its contextual role — which population compartment, which model type (deterministic vs. stochastic), and which mathematical operation it performs (rate of change, numerical approximation, discrete update).
Step 5: When presenting a composite equation, explicitly reference the component equations it synthesises and name the method that bridges them into a single form.
Step 6: Group related equations under a common model heading, presenting the deterministic version before its stochastic extension, so the reader sees the foundation before the extension.
