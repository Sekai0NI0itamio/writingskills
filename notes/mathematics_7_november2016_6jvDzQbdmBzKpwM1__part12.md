# Idea Flow Notes: mathematics_7_november2016_6jvDzQbdmBzKpwM1 — Returning to the situation described in the original question, the initial distances and angles between

## Paragraph Flow (move by move)

**Paragraph 1**
- **Sentence 1:** "the raptors and the human are shown in Figure 6." — *Figure pointer move.* It does not argue, it tells the reader where to look. The hand-off is **contextual**: the figure (captioned "initial distances and angles in the original question") supplies the geometric setup that the next paragraph will quantify, so the reader is being positioned to interpret the algebra immediately after.

**Paragraph 2**
- **Sentence 1:** "The initial distance 𝐷0 for each raptor is the same, cos²30° = …" — *Claim + derivation move.* It asserts symmetry ("the same") and immediately grounds it in a trig identity. The hand-off is **completeness**: because distance has been justified, the only piece of initial data still missing is the angular one, which forces the next sentence.
- **Sentence 2:** "while the initial angles 𝜃0 for raptors 1, 2 and 3 are 𝜑, 𝜑 + 120° and 𝜑 + 240°, respectively." — *Specification move.* "while" marks it as the parallel sibling to the distance clause; together the two clauses close out "initial conditions." The hand-off is **sufficiency**: distance + angle = the full state each raptor needs, so the next paragraph is now licensed to plug values into a formula.

**Paragraph 3**
- **Sentence 1:** "Thus, using Equation 10, given these initial conditions and the speeds of the human and raptors outlined in the original question, 𝑘1, 𝑘2 and 𝑘3 are:" — *Transition + setup move.* "Thus" is the logical hinge from the listed conditions to their use; "using Equation 10" names the earlier result being instantiated. The hand-off is **preparation**: the line stops before the formulas so the displayed equations read as the answer to the setup, not as a new claim.

**Paragraph 4**
- **Sentence 1:** "Figure 7 shows a graph of 𝑘1, 𝑘2 and 𝑘3 against 𝜑, and a graph of the overall time of survival 𝑘min, the lowest of the three functions for any given angle 𝜑." — *Figure introduction + definition move.* It names two plots and, mid-sentence, defines 𝑘min as the minimum of the three previously derived functions. The hand-off is **promotion**: by reducing three curves to one (𝑘min), the reader is steered toward analyzing the worst-case raptor, which is what a survival question requires.

## What This Section Does (content sequence)

This is a **"plug-in" section** — the bridge between a general formula and a graphical analysis. The ordered moves are:

1. **Geometric reference.** Re-point the reader at the setup figure so the algebra below is anchored to a picture. (Sets up: any symbol is interpretable.)
2. **Explicit initial conditions.** State every input the formula will need — distance and angles for each agent — with the trig/algebraic justification inline. (Sets up: the formula has nothing missing.)
3. **Substitution into the prior general result.** Use a "Thus, using Equation X" hinge to substitute the inputs, producing three agent-specific functions. (Sets up: there are now concrete functions of a single variable.)
4. **Figure introduction with a derived aggregate.** Introduce the plot and define a new variable (𝑘min) as a function-of-a-function on top of the previous results. (Sets up: a single curve carrying the final story.)

The order is **inputs → computation → visualization**, because each move's output is exactly what the next move consumes as input.

## Paragraph Skeletons (replicable templates)

**SKELETON 1 — "Initial-conditions paragraph"**
> "The initial [property A] for each [agent] is the same, [inline algebraic/trig justification], while the initial [property B] for agents 1, 2 and 3 are [v₁], [v₁ + Δ] and [v₁ + 2Δ], respectively."

1. **Slots:**
   - Slot 1: *property A* (a scalar, singular noun phrase)
   - Slot 2: *inline justification* (a short equality chain)
   - Slot 3: *property B* (another scalar)
   - Slot 4: *ordered list of three values in arithmetic progression* (numeric, comma-separated, closed by "respectively")
2. **How to fill differently:** Pick a scenario with three identical agents (drones, runners, particles). Slot 1 = the quantity that is symmetric by construction (e.g. starting speed). Slot 2 = a one-line derivation from the geometry ("cos²60° = …"). Slot 3 = the quantity that breaks symmetry and varies by agent (e.g. initial heading offset). Slot 4 = three values equally spaced.
3. **Original fill (verbatim):** "The initial distance 𝐷0 for each raptor is the same, cos²30° = … while the initial angles 𝜃0 for raptors 1, 2 and 3 are 𝜑, 𝜑 + 120° and 𝜑 + 240°, respectively."
4. **Demo fill (different idea):** "The initial speed *v*₀ for each drone is the same, cos²45° = ½ · √2 = √2/2, while the initial headings φ₀ for drones 1, 2 and 3 are ψ, ψ + 120° and ψ + 240°, respectively."

**SKELETON 2 — "Formula-application paragraph"**
> "Thus, using [Equation N], given [these conditions] and [other conditions named elsewhere], [output₁], [output₂] and [output₃] are:" *(followed by a displayed formula block)*

1. **Slots:**
   - Slot 1: *connective "Thus, using"* + *reference back to a previously derived general formula* (number/letter)
   - Slot 2: *conditions just stated in this section* (deictic "these")
   - Slot 3: *conditions deferred to an external source* (e.g. the original question, a data table)
   - Slot 4: *list of three instantiated outputs* followed by aligned equations
2. **How to fill differently:** Slot 1 = cite the general equation you proved earlier. Slot 2 = refer back to the paragraph you just wrote. Slot 3 = cite where the leftover constants live. Slot 4 = three formulas produced by plugging the per-agent data into the general equation.
3. **Original fill (verbatim):** "Thus, using Equation 10, given these initial conditions and the speeds of the human and raptors outlined in the original question, 𝑘₁, 𝑘₂ and 𝑘₃ are:"
4. **Demo fill (different idea):** "Thus, using Equation 4, given these release heights and the gravitational acceleration outlined in the original question, *t*₁, *t*₂ and *t*₃ are:"

**SKELETON 3 — "Figure-introduction paragraph"**
> "Figure N shows a graph of [Q₁] against [independent variable], and a graph of the [aggregate noun] [Q_agg], [definition of Q_agg in terms of the Qᵢ] for any given [independent variable]."

1. **Slots:**
   - Slot 1: *figure label* + *first plot's two axis labels*
   - Slot 2: *aggregate noun* (e.g. "overall time of survival")
   - Slot 3: *symbol for the aggregate*
   - Slot 4: *clause defining the aggregate as a function-of-a-function* ("the lowest of the three functions")
   - Slot 5: *restatement of the independent variable*
2. **How to fill differently:** Slot 1 = the family of curves you just produced. Slot 2 = the human-meaningful summary quantity. Slot 3 = a new symbol. Slot 4 = "the maximum/minimum of the three [Qᵢ]." Slot 5 = the same x-axis as Slot 1.
3. **Original fill (verbatim):** "Figure 7 shows a graph of 𝑘₁, 𝑘₂ and 𝑘₃ against 𝜑, and a graph of the overall time of survival 𝑘min, the lowest of the three functions for any given angle 𝜑."
4. **Demo fill (different idea):** "Figure 3 shows a graph of *t*₁, *t*₂ and *t*₃ against release angle ψ, and a graph of the overall flight duration *t*min, the longest of the three functions for any given release angle ψ."

## Express-Idea Vocabulary

- **Sequencing / consequence:** *"Thus, using Equation 10, given these initial conditions"* — the connectives bundle consequence ("Thus") with back-reference ("using Equation 10") so the substitution reads as the inevitable next step, not a new claim.
- **Deictic reference to external source:** *"the speeds … outlined in the original question"* — a one-noun clause that locates constants without re-stating them, keeping the paragraph short.
- **Specification / list-closure:** *"respectively"* — closes an enumerated triple and tells the reader the order matters.
- **Definition mid-sentence:** *"the lowest of the three functions for any given angle"* — a defining appositive inserted between two commas, so a new symbol (𝑘min) is introduced without a separate sentence.
- **Reference to prior result by number:** *"Equation 10"* — names the formula rather than re-deriving it, which is the hinge that makes this section a plug-in rather than a derivation.
- **Pointer-to-figure verb:** *"Figure 7 shows a graph of"* — the verb "shows" frames the upcoming plot as evidence/illustration of the formulas above.

## How to Explain an Idea (replication steps)

This section relies on the **plug-in / instantiation pattern**: general formula previously derived → restate inputs explicitly → substitute → visualize via graph and define the aggregate. Numbered replication steps:

1. **Re-display the geometry figure (or its number) and re-state the scenario in one short sentence.** Do this so every symbol in the next paragraphs is interpretable. *Do not* re-derive anything here; you are orienting.
2. **List the initial conditions of every agent as a parallel pair of clauses.** First clause: a quantity that is the same for all agents, with a one-line algebraic/trig justification inline. Second clause ("while …"): a quantity that varies per agent, written as an ordered triple closed by "respectively." The two clauses together must supply *every* input the formula needs.
3. **Open a new paragraph with "Thus, using [Equation N],"** then name *this section's* conditions (deictic "these") and the *external* conditions (e.g. "outlined in the original question"), and end the sentence with a colon introducing the substituted formulas.
4. **Display the substituted formulas as a block,** one per agent, kept parallel in shape so the reader can read off the symmetry.
5. **In a final sentence, introduce a figure that plots the per-agent functions against the swept parameter,** and in the same sentence define an aggregate symbol (e.g. 𝑘min) as the min/max of those functions. This single sentence does two jobs at once: presents the visualization and promotes the reader from "three curves" to "the one curve that matters."

The logic path in one line: *picture → inputs → substitution → graph of (functions, then aggregate of those functions).*
