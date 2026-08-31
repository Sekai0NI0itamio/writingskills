# Idea Flow Notes: mathematics_7_november2016_6jvDzQbdmBzKpwM1 — 3 Application of mathematics

## Paragraph Flow (move by move)

**Paragraph 1**

1. **Sentence 1** — *Transition/narrowing* — "Let us firstly consider the motion of a single raptor"
   *Move:* hand the reader from whatever came before by isolating ONE case ("a single raptor") out of the broader problem, signalling that generalisation was the setup for this move.
2. **Sentence 2** — *Claim + method introduction* — "can be approximated numerically using a geometric method"
   *Move:* hand the reader forward by answering "how?" — the word "approximated" forces the next sentence to define the units/interval, and "as shown in Figure 3" defers the visual mechanism to the next beat.

**Paragraph 2**

1. **Sentence 1** — *Mechanism unpack (step-by-step)* — "modelled as the human travelling 𝑣h Δ𝑡 m … followed by the raptor moving"
   *Move:* hand the reader forward by sequencing two actions inside one interval; the word "followed by" makes the reader expect either what happens next interval, or what the *consequence* of repeating the rule is.
2. **Sentence 2** — *Concession + redirect* — "It is possible to solve for the equation … but as"
   *Move:* hand the reader forward by contrast — "possible … but" sets up a reason why this route is rejected in favour of something else (text cuts off at "as"), so the reader expects the student's chosen alternative.

## What This Section Does (content sequence)

This is an **Application of mathematics** section that follows the canonical "model → discretise → iterate" sequence:
1. **Anchor the variable** — name and symbolise the quantity being tracked (position of raptor, 𝑣r).
2. **Declare the method** — state the numerical approximation technique (Euler-style geometric step), and defer details to a figure.
3. **Show the figure as evidence** — present positions at discrete time steps so the reader sees the iteration visually.
4. **Unpack one step of the iteration** — describe what happens inside one Δ𝑡 (human moves first, raptor moves to new human position), turning the visual into a verbal rule.
5. **Acknowledge the analytic alternative, then redirect** — cite literature for a closed-form solution, but the "but" signposts why the numerical path is preferred for this coursework.

The order matters because (1) the reader cannot understand the figure without the symbol definitions; (2) the figure cannot ground the rule without being placed first; (3) the rule cannot be evaluated without one explicit worked step; (4) the concession pre-empts the examiner's objection that a calculus solution exists.

## Paragraph Skeletons (replicable templates)

**SKELETON A** — "Method declaration paragraph"
"Let us firstly consider [single instance] at [symbol] [units]. The [quantity A] and [quantity B] over time, [symA] and [symB] respectively, can be approximated numerically using a [method type] as shown in Figure [n]."

- **Slot 1**: opening transitional clause — past or present tense, names ONE simplified case.
- **Slot 2**: two variables of the system, symbolised in the same notation style as the rest of the paper.
- **Slot 3**: name of the numerical/approximate technique ("Euler", "Riemann sum", "Verlet", "forward difference").
- **Original**: "Let us firstly consider the motion of a single raptor travelling at 𝑣r m s−1 . The positions of the human and raptor over time, 𝒔h and 𝒔r respectively, can be approximated numerically using a geometric method similar to the Euler method as shown in Figure 3."
- **Demonstration fill (different idea — cooling coffee)**: "Let us firstly consider the temperature of a single cup cooling at rate k min⁻¹. The temperatures of the cup and surroundings over time, T_c and T_s respectively, can be approximated numerically using a step-by-step Newton-cooling method as shown in Figure 2."

**SKELETON B** — "One-step mechanism paragraph"
"In each [interval] of [Δsymbol] [units] (in Figure [n], [concrete value] [unit]), the situation can be modelled as [actor 1] moving [distance 1] in [its direction], followed by [actor 2] moving [distance 2] towards [actor 1]'s new position."

- **Slot 1**: a discrete interval variable with units (Δt s, Δx m, Δθ rad).
- **Slot 2**: the concrete worked value shown in the figure, so the reader can map rule to diagram.
- **Slot 3**: a two-stage action sequence inside the interval, using "followed by" to enforce temporal order.
- **Original**: "In each time interval of Δ𝑡 s (in Figure 3, 1 s), the situation can be modelled as the human travelling 𝑣h Δ𝑡 m in its direction of motion, followed by the raptor moving 𝑣r Δ𝑡 m towards the human's new position."
- **Demonstration fill (different idea — predator–prey)**: "In each spatial step of Δx m (in Figure 4, 0.5 m), the situation can be modelled as the prey moving v_p Δx m along its escape bearing, followed by the predator moving v_q Δx m towards the prey's new position."

**SKELETON C** — "Alternative-then-redirect paragraph"
"It is possible to solve for the [quantity]'s motion (see [Author1] [ref] and [Author2] [ref]), but as…"

- **Slot 1**: a hedged concession that an analytic/closed-form route exists.
- **Slot 2**: two literature citations in standard IB bracketed form.
- **Slot 3**: the "but as…" clause that has not yet been completed — the writer commits to justifying the numerical choice.
- **Original**: "It is possible to solve for the equation of the raptor's motion (see Lloyd [4] and Mungan [5]), but as" *(cuts off)*
- **Demonstration fill (different idea — logistic growth)**: "It is possible to solve for the equation of the population's growth analytically (see Verhulst [2] and May [3]), but as the carrying capacity varies with season, a discrete numerical model is more appropriate here."

## Express-Idea Vocabulary

**Sequencing / ordering**
- "Let us firstly consider" — opens the section and orders it first in a sequence.

**Method introduction / evidence handling**
- "can be approximated numerically" — frames the chosen route as an approximation supported by the figure.
- "as shown in Figure 3" — defers visual verification to a labelled diagram.
- "(see Lloyd [4] and Mungan [5])" — bracketed dual citation, classic IB evidence move.

**Mechanism / explanation verbs**
- "can be modelled as" — converts a verbal rule into a mathematical statement.
- "travelling 𝑣h Δ𝑡 m in its direction of motion, followed by the raptor moving" — the "followed by" inside a single sentence sequences two half-steps of the iteration.

**Concession / contrast**
- "It is possible to … but as" — the "possible … but" construction signals an analytic alternative is being set aside.

**Specification**
- "In each time interval of Δ𝑡 s (in Figure 3, 1 s)" — gives the abstract symbol and then the concrete numerical value, a definition-then-specification pair.

## How to Explain an Idea (replication steps)

The pattern this section relies on is: **anchor the variable → declare the numerical method → defer to a diagram → unpack one iteration step → acknowledge the analytic alternative**.

To explain a NEW idea with the same pattern:

1. **Open with a narrowing clause.** Write "Let us firstly consider…" and isolate one simple instance of the system. Name its speed/rate with a symbol and units.
2. **Name the two (or more) quantities being tracked.** Give them paired subscripts in the same notation family (e.g. 𝒔_h and 𝒔_r).
3. **Declare the approximation method by name.** Use a phrase like "can be approximated numerically using a … method" and reference a labelled figure.
4. **Insert the figure with discrete snapshots.** Place step-numbered positions so the reader sees the iteration visually.
5. **Verbalise one iteration step.** Use "In each interval of Δ[symbol] … the situation can be modelled as [actor 1] moving [distance], followed by [actor 2] moving [distance] towards [actor 1]'s new position." This is the core mechanism line.
6. **Acknowledge the analytic route.** End with "It is possible to solve for [equation] (see [Author A] [ref] and [Author B] [ref]), but as…" — then complete with the justification (e.g. variable parameters, pedagogical clarity, or computational convenience).
