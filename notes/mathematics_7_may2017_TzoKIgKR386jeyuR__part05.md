# Idea Flow Notes: mathematics_7_may2017_TzoKIgKR386jeyuR — The DSIRM that will be created in this report will simulate the situation when a hypothetical

## Paragraph Flow (move by move)

**Paragraph 1 — Scenario setup with parameters**

1. **Context/Scenario move**: "A non-lethal epidemic is introduced into a school of 1200 students." → Hands to next sentence by specifying the population (a concrete scenario requires a concrete number — the 1200 is the natural next detail).
2. **Specification (parameter)**: "The students in the school are assumed to have 40 interactions" → Hands forward because the reader now needs to know the infection mechanics; "assumed" signals the modelling chain.
3. **Specification (parameter)**: "probability of infection 0.001 and a probability of recovery 0.01" → Hands forward by completing the parameter set; the closing clause gathers the two probabilistic inputs.
4. **Summary/restatement move**: "In other words, N = 1200, α = 40, i = 0.001, r = 0.01." → Hands to the next section (Euler's Method) by compressing the narrative into the symbols that the next paragraphs will operate on.

**Paragraph 2 — Definition of Euler's Method**

1. **Term-introduction move**: "Euler's Method" (header). → Hands to definition by naming the tool that must be explained.
2. **Definition move**: "Euler's Method is a numerical method used to find numerical approximations" → Hands to citation by attributing the definition to a source.
3. **Authority move**: "(Blythe 232)." → Hands to the next paragraph because the reader now knows what the method *is* and wants to see its *core approximation*.

**Paragraph 3 — The fundamental approximation**

1. **Transition/pointer move**: "The fundamental approximation in Euler's Method is as follows." → Hands to the equation by signaling that what follows IS the core idea.
2. **Display of the core relation**: Equation 5 — $\frac{dy}{dx} = f(x,y) \approx \frac{\Delta y}{\Delta x}$. → Hands forward as a definition-as-equation; the reader must next see how this relation produces a step rule.

**Paragraph 4 — Derivation / unpacking of the step**

1. **Conditional setup move**: "If $x_0$ increases by $h$ from $x_0$ to $x_1$" → Hands to algebra by giving the increment condition.
2. **Algebraic unpack (substitution)**: "$f(x_0, y_0) \approx \frac{\Delta y}{h} = \frac{y_1-y_0}{x_1-x_0}$" → Hands forward because the equal sign invites rearrangement.
3. **Rearrangement move**: "$h \times f(x_0, y_0) \approx y_1 - y_0$" → Hands to the final closed-form step.
4. **Final rule (verdict/implication)**: "$y_1 \approx y_0 + h \times f(x_0, y_0)$" → Hands to whatever follows (in the broader report, this becomes the recurrence relation).

## What This Section Does (content sequence)

1. **Scenario framing** — sets the real-world situation so the reader sees *what* is being modelled before *how*. This primes the reader to care about the parameters.
2. **Parameter listing in prose** — translates the situation into verbal assumptions (interactions, infection, recovery). Reasoning move: prose parameters are easier to read than raw symbols, so they appear first.
3. **Symbolic restatement ("In other words")** — compresses the prose parameters into mathematical notation. Reasoning: the next paragraphs need the symbols, and the reader needs to verify the translation.
4. **Method naming** — introduces the tool (Euler's Method) that will be used on those parameters.
5. **Authoritative definition** — defines the tool via a cited source; reasoning: a numerical method needs to be tied to a trusted text before the student is allowed to use it.
6. **Core-relation announcement** — signals "here is the central identity" and displays it. Reasoning: in a derivation, you must show the seed equation so each manipulation is justified.
7. **Conditional framing of the step** — sets up the increment (h, from x₀ to x₁) which justifies why the substitution is valid.
8. **Step-by-step algebraic manipulation** — rewrites the seed into an operational rule. Reasoning: each line must come from the previous one to keep the chain valid.
9. **Closed-form step (verdict)** — produces the recurrence $y_1 \approx y_0 + h f(x_0, y_0)$, the actual reusable tool.

Order logic: **context → parameters → symbols → method definition → core equation → derivation → operational rule.** A student replicating this on a different topic (e.g. predator–prey model, RC circuit) should follow the same scaffold.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Parameter-setting paragraph (real scenario → verbal assumptions → symbolic restatement)**

Slot structure:
- Slot 1: Concrete real-world scenario (one sentence, present/past passive, named population).
- Slot 2: Verbal assumption about the interaction/contact behaviour (past passive "are assumed to have…").
- Slot 3: Verbal assumption about the probabilities/coefficients (listing two or more parameters).
- Slot 4: Symbolic restatement ("In other words, X₁ = …, X₂ = …, …").

How to fill with a DIFFERENT idea:
- Slot 1: Pick a closed system (school, pond, factory, traffic network) and a perturbation reaching it (epidemic, invasive species, contaminant, congestion). State the population size.
- Slot 2: Pick a behavioural/contact rate the model needs (interactions per unit time, collisions per second, intake per day). Use the phrase "assumed to have [number] [behaviour]s per [unit]".
- Slot 3: Pick two probability/rate constants (infection & recovery, birth & death, inflow & outflow). Mirror the phrasing "probability of [process 1] [p₁] and a probability of [process 2] [p₂]".
- Slot 4: Use exactly "In other words, [symbol list]." — list every symbol in order of appearance.

Original filled version: "A non-lethal epidemic is introduced into a school of 1200 students. The students … are assumed to have 40 interactions … per unit time. The epidemic … probability of infection 0.001 and … recovery 0.01. In other words, N = 1200, α = 40, i = 0.001, r = 0.01."

Demonstration fill (different idea — predator–prey):
"A invasive predatory fish is introduced into a closed lake containing 800 native minnows. The minnows are assumed to have 12 encounters with predators per unit time. The system has a predation probability of 0.004 and a prey reproduction probability of 0.02. In other words, N = 800, β = 12, p = 0.004, r = 0.02."

---

**SKELETON B — Method-definition paragraph (named tool → "is a … used to …" → citation)**

Slot structure:
- Slot 1: Header naming the method (centred or bold).
- Slot 2: Definition sentence using "is a [type of method] used to [verb] [object]" pattern.
- Slot 3: Bracketed authority citation.

How to fill:
- Slot 1: Name any numerical/analytical method (Runge–Kutta, Newton's Method, Simpson's Rule, Trapezoidal Rule).
- Slot 2: Begin "X's Method is a numerical method used to find numerical approximations to the solution of [equation class]." Keep the formula generic.
- Slot 3: Cite the textbook page using (Author page).

Original: "Euler's Method … Euler's Method is a numerical method used to find numerical approximations to the solution of the differential equation dy/dx = f(x, y) (Blythe 232)."

Demonstration fill (different idea — Newton's Method):
"Newton's Method. Newton's Method is an iterative numerical method used to find numerical approximations to the roots of a differentiable function g(x) (Stewart 87)."

---

**SKELETON C — Core-equation paragraph (announcement → display → caption)**

Slot structure:
- Slot 1: Pointer — "The fundamental [approximation/relation/identity] in [Method] is as follows."
- Slot 2: Displayed equation.
- Slot 3: Caption labelled "Equation N" plus a noun-phrase restatement of the equation.

How to fill:
- Slot 1: Use "fundamental approximation" for difference-equation methods; swap for "fundamental identity" if the method is algebraic.
- Slot 2: Typeset the relation using standard symbols (Δ for finite difference, d/dx for derivatives).
- Slot 3: Number the equation sequentially and echo the verbal description.

Original: "The fundamental approximation in Euler's Method is as follows. [Equation 5] Equation 5: The fundamental approximation in Euler's method."

Demonstration fill:
"The fundamental identity in Newton's Method is as follows. [Equation 3: x_{n+1} = x_n − g(x_n)/g'(x_n)] Equation 3: The recurrence step in Newton's method."

---

**SKELETON D — Derivation paragraph (conditional → substitution → rearrangement → operational rule)**

Slot structure:
- Slot 1: Conditional clause ("If [variable] increases by [step] from [initial] to [next]").
- Slot 2: Substitution line substituting the discrete Δ's for differences of f.
- Slot 3: Rearrangement line multiplying through by the step.
- Slot 4: Closed-form operational rule (the recursion).

How to fill:
- Slot 1: Pick a generic independent variable and step size (h, k, Δt). Use the pattern "If x₀ increases by h from x₀ to x₁".
- Slot 2: Replace Δx by (x₁−x₀) and Δy by (y₁−y₀) and set f(x₀,y₀) equal to their ratio.
- Slot 3: Multiply both sides by the step.
- Slot 4: Isolate y₁ on the left and present the recurrence as the final line.

Original: "If x₀ increases by h from x₀ to x₁, f(x₀,y₀) ≈ Δy/h = (y₁−y₀)/(x₁−x₀). h × f(x₀,y₀) ≈ y₁ − y₀. y₁ ≈ y₀ + h × f(x₀,y₀)."

Demonstration fill (different idea — trapezoidal step):
"If t increases by k from t₀ to t₁, (F(t₁)+F(t₀))/2 ≈ ΔA/k. k × (F(t₁)+F(t₀))/2 ≈ A₁ − A₀. A₁ ≈ A₀ + k × (F(t₁)+F(t₀))/2."

## Express-Idea Vocabulary

**Sequencing / framing the demonstration**
- "The fundamental approximation in Euler's Method is as follows." (pointer — telling the reader what is about to come)
- "Equation 5" / "Equation N" (caption — labelling display math)

**Specification / parameter translation**
- "In other words, N = 1200, α = 40, i = 0.001, r = 0.01." (compressing prose into symbols)
- "are assumed to have 40 interactions with other students" (declaring a modelling assumption)

**Authority / evidence handling**
- "(Blythe 232)." (parenthetical citation — single-sentence authority hook)
- "is a numerical method used to find numerical approximations" (defining via the textbook's phrasing)

**Explanation verbs / definitional moves**
- "is a numerical method used to find" (definition by category + function)
- "is introduced into" (scenario-anchoring verb)
- "assumed to have" (modelling-assumption verb)
- "can be obtained" / "we can obtain" (implication/derivation verb — implicit here as "From equation 5, we can obtain the following")

**Logical / mathematical connectives**
- "≈" (approximation symbol — repeated, signalling the method's numerical nature)
- "If x₀ increases by h from x₀ to x₁" (conditional — sets up the derivation)
- "From equation 5" (causal/logical pointer — "from this, derive…")

**Implication / verdict verbs**
- "y₁ ≈ y₀ + h × f(x₀, y₀)" (no narrative verb — the rule *is* the verdict; the line itself functions as the conclusion)

## How to Explain an Idea (replication steps)

This section uses the pattern **method-introduction → authoritative definition → display of core relation → algebraic derivation → operational rule**. It is essentially an **authority → definition → worked algebraic derivation** pattern.

Step-by-step replication instructions for a NEW idea (e.g. Runge–Kutta 4th Order):

1. **Name the method as a header.** Place the method's name at the top of its own section so the reader can locate it as a unit. (Slot 1 of Skeleton B.)
2. **Define the method in one sentence using the "is a … used to …" template, followed by an in-text citation in parentheses.** This grounds the method in an external source and signals academic honesty. (Slot 2 + 3 of Skeleton B.)
3. **Announce the core relation with a pointer sentence** — "The fundamental [approximation/identity] in [Method] is as follows." This previews what the reader is about to see and prevents the equation from appearing out of nowhere.
4. **Display the seed equation in a centred, numbered block** with a one-line caption. The caption echoes the verbal label so the reader can cross-reference.
5. **Open the derivation with a conditional clause** ("If x increases by h from x₀ to x₁"). This creates the discrete setting that justifies the substitution.
6. **Substitute the discrete differences** (Δx, Δy) with their expanded forms (x₁−x₀, y₁−y₀). Keep the ≈ symbol to retain the numerical character.
7. **Manipulate line-by-line** — each new line must follow algebraically from the previous. Multiply through by the step size first, then isolate the next-value term.
8. **End on the closed-form recursion** (e.g. $y_1 \approx y_0 + h f(x_0,y_0)$). This final line is the *verdict* of the derivation — the operational tool the rest of the report will reuse. Do not narrate it; let the equation stand as the conclusion.
