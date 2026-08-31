# Idea Flow Notes: mathematics_7_may2021_Hbdz2gzugbb7Ongw — 4.2     Example of solving the DEs using Euler’s Method

## Paragraph Flow (move by move)

**Paragraph 1 — Stating the conditions**
- Move 1: Header/label — *"Conditions:"* — declares that what follows are the parameter values for the example. Hands the reader to the next move by signaling "use these values."
- Move 2: Parameter list — *"m1 = m2 = l1 = l2 = 1"* — fixes the physical parameters. Hands forward by removing all free symbols except the angles and their derivatives.
- Move 3: Initial angles — *"θ1 (0) = 0.25π, θ2 (0) = 0.5π"* — assigns starting positions. Sets up everything the DEs need to be numerically evaluable.
- Move 4: Initial angular velocities and step — *"θ˙1 (0) = θ˙2 (0) = 0 ; dt = 0.001"* — completes the initial state vector and the iteration step. Hands the reader to the first substitution into the DE.

**Paragraph 2 — Evaluating θ̈1(0)**
- Move 1: DE with values plugged in — *"[1 − cos² (0.25π)]θ¨1 (0) = −g sin(0.25π) + …"* — substitutes the conditions from Paragraph 1 into the previously derived equation. Hands forward by reducing the equation to a single unknown, θ̈1(0).
- Move 2: Solved result — *"θ¨1 (0) = −√2⁄3 g"* — delivers the cleaned numerical coefficient. Hands forward by giving the slope (angular acceleration) that Euler's formula needs.

**Paragraph 3 — First Euler step for pendulum 1**
- Move 1: Velocity update — *"θ˙1 (0.001) = θ˙1 (0) + 0.001 × θ¨1 (0)"* — applies the Euler formula. Hands forward by producing θ̇1 at the new time.
- Move 2: Numerical value — *"= −0.001 × √2⁄3 × 9.81 = −4.62 × 10⁻³ s⁻¹"* — converts the symbolic result into a number. Hands forward by making the velocity usable in the next Euler step.
- Move 3: Position update — *"θ1 (0.001) = θ1 (0) + 0.001 × θ˙1 (0)"* — applies the position form of Euler. Note θ̇(0)=0, so this hands the reader to the *second* iteration where the new velocity will actually matter.

**Paragraph 4 — Second Euler step for θ1**
- Move 1: Position update formula — *"θ1 (0.002) = θ1 (0.001) + 0.001 × θ˙1 (0.001)"* — repeats Euler for the next dt. Hands forward by demonstrating that the new velocity now bites.
- Move 2: Numerical value — *"= 0.25π − 4.62 × 10⁻⁶"* — shows the first non-trivial positional change. Hands the reader sideways to the parallel calculation for pendulum 2.

**Paragraph 5 — Evaluating θ̈2(0)**
- Move 1: DE with values plugged in — *"[1 − cos² (0.25π)]θ¨2 (0) = −g sin(0.5π) − cos(0.25π)[…]"* — mirrors Paragraph 2 for the second variable. Hands forward by establishing symmetry of method.
- Move 2: Solved result — *"θ¨2 (0) = −2⁄3 g"* — delivers the cleaned coefficient. Hands forward to the Euler iterations on θ̇2.

**Paragraph 6 — First Euler step for pendulum 2**
- Move 1: Velocity update — *"θ˙2 (0.001) = θ˙2 (0) + 0.001 × θ¨2 (0)"* — same template as Paragraph 3.
- Move 2: Numerical value — *"= −0.001 × 2⁄3 × 9.81 = −6.54 × 10⁻³ s⁻¹"* — specific number, parallels Paragraph 3.
- Move 3: Position update — *"θ2 (0.001) = θ2 (0) + 0.001 × θ˙2 (0)"* — same template, will yield θ2 unchanged this step.

**Paragraph 7 — Second Euler step for θ2**
- Move 1: Position update formula — *"θ2 (0.002) = θ2 (0.001) + 0.001 × θ˙2 (0.001)"* — mirrors Paragraph 4.
- Move 2: Numerical value — *"= 0.5π − 6.54 × 10⁻⁶"* — confirms the new velocity contributes a measurable displacement.

**Paragraph 8 — Justifying the switch to software**
- Move 1: Cause/complication claim — *"As these equations are complicated, and there are many iterations, it is difficult to do by hand."* — names the practical obstacle just demonstrated. Hands forward by raising the need for a tool.
- Move 2: Implication — *"It is better to use computer software."* — the consequence of the preceding claim.
- Move 3: Specific decision — *"I chose to use the programming language Python, with the libraries math, numpy, and matplotlib."* — narrows the general recommendation to the actual tool used.

## What This Section Does (content sequence)

1. **State the initial state vector and the step size** — needed before any numerical solver can run.
2. **Evaluate each differential equation at t = 0** — produces the slopes θ̈1(0), θ̈2(0) that Euler needs.
3. **Apply Euler's update to each velocity** — first use of the iteration rule on θ̇.
4. **Apply Euler's update to each position using the OLD velocity** — shows that at the first step the position barely moves (because initial velocity = 0).
5. **Apply Euler's update again using the NEW velocity** — shows the iteration actually advancing the state.
6. **Repeat the three Euler moves for the second variable** — proves the method generalises, not just one worked case.
7. **Name the bottleneck** — frames the worked example as illustrative, not exhaustive.
8. **Name the replacement tool** — closes the loop between "shown by hand" and "what was actually used."

Order rationale: parameters must precede substitution → substitution must precede iteration → first iteration must precede second (to demonstrate the method actually moves the state) → second variable must follow the first (to generalise) → only then does the case for software follow logically from the bulk already shown.

## Paragraph Skeletons (replicable templates)

**Skeleton A — Conditions block**
- Slot 1: A label/header word (e.g. "Conditions:"). Grammatically a noun.
- Slot 2: A run of equality statements listing physical constants.
- Slot 3: A run of equality statements listing initial positions.
- Slot 4: A run of equality statements listing initial rates and the step size.
- **How to fill differently:** Pick a worked example from your own investigation. Replace the constants with the specific numbers your system uses; replace the initial values with whatever t = 0 starting conditions apply; keep dt small (e.g. 0.001 or 0.01).
- **Original fill:** *"Conditions: m1 = m2 = l1 = l2 = 1 ; θ1 (0) = 0.25π, θ2 (0) = 0.5π ; θ˙1 (0) = θ˙2 (0) = 0 ; dt = 0.001"*
- **Demo fill (different idea — logistic population growth):** *"Conditions: r = 0.4, K = 500 ; P(0) = 10 ; dP/dt (0) = r P(0) (1 − P(0)/K) ; dt = 0.1"*

**Skeleton B — DE-substitution block**
- Slot 1: General DE copied across with the parameter values substituted in (bracket-coefficient form).
- Slot 2: A simplified numerical coefficient for the second derivative.
- **How to fill differently:** Take your previously derived ODE, swap the symbols for the values listed in Skeleton A, simplify the trig/constants, and write the result on the next line with "=" sign.
- **Original fill:** *"[1 − cos²(0.25π)]θ¨1 (0) = −g sin(0.25π) + g cos(0.25π) sin(0.5π) ; θ¨1 (0) = −√2⁄3 g"*
- **Demo fill (different idea — exponential decay):** *"k · m · v˙(0) = −m · g · sin(0) ; v˙(0) = 0"*

**Skeleton C — Euler-step block**
- Slot 1: "θ̇(t+dt) = θ̇(t) + dt × θ̈(t)" written out.
- Slot 2: Numerical substitution yielding a value with units.
- Slot 3: "θ(t+dt) = θ(t) + dt × θ̇(t)" written out.
- Slot 4: Numerical value (often equal to θ(t) on the first step).
- **How to fill differently:** Write the Euler update twice — once for the rate, once for the state — and compute each. Make the units explicit on the rate line.
- **Original fill:** *"θ˙1 (0.001) = θ˙1 (0) + 0.001 × θ¨1 (0) = −4.62 × 10⁻³ s⁻¹ ; θ1 (0.001) = θ1 (0) + 0.001 × θ˙1 (0) = 0.25π"*
- **Demo fill (different idea — cooling coffee):** *"T(1) = T(0) + 1 × −k(T(0) − T_env) = 78 − 1.4 = 76.6 ; T(2) = T(1) + 1 × −k(T(1) − T_env) = 76.6 − 1.32 = 75.28"*

**Skeleton D — Tool-justification paragraph**
- Slot 1: "As these [items] are [adjective], and there are [quantity] [plural noun], it is [adjective] to [verb] by [method]." (cause statement)
- Slot 2: "It is better to [verb] [alternative]." (implication)
- Slot 3: "I chose to use [specific tool], with the [supporting detail]." (decision)
- **How to fill differently:** Identify the actual obstacle (algebra, iteration count, time), propose the family of solution (software, calculator, table), then commit to one specific tool and its libraries/features.
- **Original fill:** *"As these equations are complicated, and there are many iterations, it is difficult to do by hand. It is better to use computer software. I chose to use the programming language Python, with the libraries math, numpy, and matplotlib."*
- **Demo fill (different idea — numerically solving a projectile with air drag):** *"As these integrals have no closed form, and the drag term is evaluated at every step, it is impractical to do by hand. It is better to use numerical integration. I chose to use Python, with the libraries scipy.integrate.odeint and matplotlib for plotting."*

## Express-Idea Vocabulary

**Sequencing / iteration**
- "θ1 (0.002) = θ1 (0.001) + 0.001 × θ˙1 (0.001)" — the repeated "+ 0.001 × θ˙1" frames each block as the next instance of the same template; sequencing is shown by the time argument stepping (0 → 0.001 → 0.002).

**Cause / consequence**
- "As these equations are complicated, and there are many iterations, it is difficult to do by hand." — "As …, it is difficult" names cause → effect.

**Implication**
- "It is better to use computer software." — implicit "therefore" carried by the comparative "better."

**Specification / narrowing**
- "I chose to use the programming language Python, with the libraries math, numpy, and matplotlib." — "with the libraries" narrows the general "computer software" to a concrete stack.

**Explanation verbs (mathematical use)**
- "θ¨1 (0) = −√2⁄3 g" — implicit "is equal to" / "simplifies to" carried by the equals sign.
- "θ˙1 (0.001) = θ˙1 (0) + 0.001 × θ¨1 (0)" — "is updated by" / "is computed from" carried by the Euler formula.

**Contrast handled structurally, not lexically**
- The contrast between "by hand" and "by computer" is built into Skeleton D's slot sequence rather than signalled by "however/whereas."

## How to Explain an Idea (replication steps)

The section uses a **worked-numerical-example pattern**: *fix the parameters → evaluate the analytical equation at t = 0 → apply the iteration rule → show one further iteration → mirror for a second variable → justify switching tool*.

To replicate with a new idea:

1. **Pin the numbers down.** Write a labelled block of conditions: constants, initial values of the state variables, initial values of their rates, and the step size dt. (Skeleton A)
2. **Evaluate the governing equation once, by hand, at t = 0.** Show the substituted form on one line and the cleaned coefficient on the next. (Skeleton B)
3. **Apply the chosen numerical scheme once for each rate.** Write the update formula symbolically, then the numerical value with units. (Skeleton C, slot 1–2)
4. **Apply the scheme once for each state variable using the *old* rate.** Note explicitly if the state does not change (because the rate is zero) — this is itself a teaching beat. (Skeleton C, slot 3–4)
5. **Apply the scheme a *second* time using the *new* rate.** This is where the reader sees the method actually moving the state forward. (Skeleton C applied again)
6. **Mirror the entire evaluation for a second variable.** This proves the method works generally, not just for one lucky case.
7. **Close with a three-sentence justification paragraph** that names the bottleneck, names the class of solution, and names the specific tool. (Skeleton D)
