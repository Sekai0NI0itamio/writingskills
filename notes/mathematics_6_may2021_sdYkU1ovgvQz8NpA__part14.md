# Idea Flow Notes: mathematics_6_may2021_sdYkU1ovgvQz8NpA — equation holds true

## Paragraph Flow (move by move)

**Paragraph 1**
1. *"Now reducing the equation to only α and C, I can begin analysing…"* → **Setup move**: announces a simplification step (reducing variables) and immediately states the method (graphing) used to interrogate it. Hands the reader to the next paragraph via the figure that follows — the graph is the visual evidence the setup promised.

**Paragraph 2**
1. *"This shows me all the possible value of α…"* → **Evidence move**: points the reader at the graph and surfaces the first observation. Hands forward by naming the puzzle that observation creates.
2. *"…we do not have solutions for all α ∈ R and I have a maximum attainable α value…"* → **Problem-framing move**: identifies the gap (not all α give solutions) and states the target (find the maximum α). Hands forward because the target now needs a name.
4. *"I first denote that for any ri its corresponding α maximum coordinates to be (αi , Cαi)."* → **Notation move**: introduces symbols for the maximum point. Hands forward by inviting application of those symbols to the visible case.
5. *"Thus, in the figure above, Cα1 was denoted to be the corresponding C value…"* → **Specification move**: pins the general notation to the specific point α1. Hands forward because the reader now knows the target symbol but not yet where the curve misbehaves.
6. *"Notice that from the definition of the equation, at C = 0 the graph becomes discontinuous, as C 6= 0."* → **Edge-case move**: explains why a boundary matters (C cannot be zero). Hands forward by extending the boundary idea from "C = 0" to "α = α1".
7. *"Moreover, the above figure shows me that for |α| < α1 I have 2 solutions, and for |α| > α1 I have no solutions, therefore finding the value of α1 may be crucial…"* → **Regional-analysis + consequence move**: maps the graph into zones (two solutions, zero solutions) and converts that map into a "therefore" justifying why α1 is critical. Hands forward because the importance is now established — what comes next must be a tool to extract α1.
8. *"To find this value, I will implicitly differentiate with respect to α as the gradient of the tangent is undefined at α1."* → **Method-selection move with rationale**: chooses the tool (implicit differentiation) and gives the reason (undefined tangent at the maximum). Hands forward into the algebraic setup.
9. *"Let u = C and v = cosh(Cα), then…"* → **Substitution setup move**: prepares variables u, v so the derivative can be computed cleanly. Hands forward into the derivative expressions that close the section.

## What This Section Does (content sequence)
1. **Reduction / setup** — strip the equation to the two variables of interest so the problem is now two-dimensional. Sets up the method that follows.
2. **Visual evidence** — present the graph (figure) that will do the analytical work. Sets up the observations.
3. **First-pass observation** — state what jumps out of the graph (not all α yield solutions; a maximum α exists). Sets up the question.
4. **Notation** — name the maximum point so it can be referenced. Sets up precise discussion.
5. **Pin notation to figure** — apply the symbol to the specific case. Sets up edge-case reasoning.
6. **Edge/discontinuity check** — defend the boundary by appealing to the equation's domain. Sets up the regional claim.
7. **Regional analysis + consequence** — split the graph into "two solutions / zero solutions" zones and convert that into a "therefore" about importance. Sets up the need for a tool.
8. **Method selection with reason** — name the technique (implicit differentiation) and justify it (undefined gradient at α1). Sets up the algebra.
9. **Substitution launch** — introduce u, v and write the derivatives. Sets up the calculation in the next section.

The order is: **simplify → visualise → observe → name → specialise → justify boundaries → zone the graph → justify method → launch calculation.** Each move converts the previous one's output into the next move's input.

## Paragraph Skeletons (replicable templates)

**SKELETON A — the setup paragraph:**
*"Now [reducing the equation to X and Y], I can begin analysing for what values of X and Y [yield the target] by [method] so I can effectively [solve/predict] for [output] for any [input]."*

1. **Slot 1** — past-progressive action ("Now reducing…"): names what is being stripped away. Grammatically: gerund clause with "Now" frame.
2. **Slot 2** — method verb ("by graphing"): the technique used to interrogate the reduced equation.
3. **Slot 3** — purpose clause ("so I can effectively solve for…"): states the deliverable.
4. **Original:** *"Now reducing the equation to only α and C, I can begin analysing for what values of α and C I can obtain an answer of 1.35 by graphing equation 20 so I can effectively solve for my C for any α value."*
5. **Demo fill (different idea):** *"Now reducing the projectile's path equation to only v₀ and θ, I can begin analysing for what values of v₀ and θ yield a range of 50 m by graphing the trajectory so I can effectively solve for θ for any launch speed."*

**SKELETON B — the observation + regional + "therefore" paragraph:**
*"[Pointer to figure] shows me [all possibilities], and the first thing I notice is that [limitation]. I first denote that for any [case] its [target] coordinates to be [(symbol)]. Thus, [specific instance]. Notice that from the definition of the equation, at [boundary] the graph becomes discontinuous, as [reason]. Moreover, the above figure shows me that for [region A] I have [count] solutions, and for [region B] I have [count], therefore [importance claim], as [consequence]. To find this value, I will [method] as [rationale]. Let [u] = [expression] and [v] = [expression], then [derivative statements]."*

1. **Slot 1** — figure pointer (sentence-leading demonstrative "This/above shows me").
2. **Slot 2** — limitation clause ("we do not have solutions for all X").
3. **Slot 3** — notation sentence (defines (αi, Cαi)).
4. **Slot 4** — specific application ("Thus… denoted to be").
5. **Slot 5** — discontinuity defence ("Notice that… C ≠ 0").
6. **Slot 6** — regional comparison ("Moreover… for |α| < α1…").
7. **Slot 7** — "therefore" importance claim ("therefore finding X may be crucial").
8. **Slot 8** — method justification ("To find this value, I will…").
9. **Slot 9** — substitution launch ("Let u =… v =…").
10. **Original:** as quoted in paragraph 2 above.
11. **Demo fill (different idea):** *"The figure above shows me every (v₀, θ) combination that yields a 50 m range, and the first thing I notice is that not every launch speed allows a real launch angle. I first denote that for any speed vᵢ its maximum-range angle coordinates to be (θᵢ, Rθᵢ). Thus, Rθ₁ is the range achieved at θ₁. Notice that from the definition of the trajectory, at θ = 90° the range equation degenerates, as sin(2θ) collapses. Moreover, the figure shows me that for θ below θ₁ I have two angles, and above θ₁ none, therefore locating θ₁ may be crucial for selecting launch parameters, as no solution exists past it. To find this value, I will differentiate with respect to θ where dR/dθ = 0. Let u = v₀² and v = sin(2θ)/g, then u′ = 2v₀ and v′ = 2cos(2θ)/g."*

**SKELETON C — the consequence-converter micro-move (reusable sentence):**
*"[Zone A] I have [n] solutions, and [Zone B] I have [n], therefore finding [boundary] may be crucial in [real-world goal], as solutions do not exist for [region beyond boundary]."*

1. **Slot 1** — zone A condition (inequality with |·|).
2. **Slot 2** — solution count.
3. **Slot 3** — zone B condition.
4. **Slot 4** — solution count.
5. **Slot 5** — "therefore" + importance claim.
6. **Slot 6** — concrete real-world tie-back.
7. **Original:** *"for |α| < α1 I have 2 solutions, and for |α| > α1 I have no solutions, therefore finding the value of α1 may be crucial in finding the breaking distance for my soap films."*
8. **Demo fill:** *"for concentrations below C₁ I have two equilibrium points, and above C₁ I have none, therefore locating C₁ may be crucial in predicting the saturation threshold for my crystallisation experiment."*

## Express-Idea Vocabulary

**Sequencing / progression**
- *"Now reducing the equation"* — frames the move as a continuation of prior work.
- *"The first thing I notice"* — front-orders the observation among many possible ones.
- *"Moreover, the above figure shows me"* — adds a further observation from the same source.

**Specification / notation**
- *"I first denote that for any ri its corresponding α maximum coordinates to be (αi , Cαi)"* — introduces symbols for repeated reference.
- *"in the figure above, Cα1 was denoted to be"* — pins the general symbol to a specific point.

**Contrast / edge-case**
- *"Notice that from the definition of the equation, at C = 0 the graph becomes discontinuous, as C 6= 0"* — defends the boundary by definition.
- *"for |α| < α1 I have 2 solutions, and for |α| > α1 I have no solutions"* — explicit zone contrast.

**Cause / consequence**
- *"therefore finding the value of α1 may be crucial in finding the breaking distance"* — converts a graph feature into a real-world importance claim.
- *"as solutions do not exist for the radius after the distance |α| > α1"* — supplies the causal reason for the importance claim.

**Evidence handling**
- *"This shows me all the possible value of α"* — points at figure as evidence.
- *"the above figure shows me that for |α| < α1 I have 2 solutions"* — reads a claim directly off the graph.

**Method-selection language**
- *"To find this value, I will implicitly differentiate with respect to α"* — names the tool.
- *"as the gradient of the tangent is undefined at α1"* — justifies the tool.

**Explanation verbs**
- *"from the definition of the equation"* — appeals to a definitional source.
- *"denoted to be"* — sets symbol-to-thing correspondence.
- *"can obtain an answer of 1.35"* — describes what extraction looks like.

## How to Explain an Idea (replication steps)

The section uses the pattern: **observe from a visual → name the target → defend boundary → zone the picture → justify importance → choose tool → launch substitution.**

Steps to replicate with a new idea:

1. **State the reduction.** Open with "Now reducing [the model] to only [var 1] and [var 2], I can begin analysing for what values of [var 1] and [var 2] [produce the target] by [method]…" This sets a two-variable analytical frame.
2. **Insert the visual.** Place a graph/figure that will do the explanatory work; do not argue from the equation alone.
3. **Surface the first observation.** Point at the figure ("This shows me…") and immediately flag the limitation ("we do not have solutions for all [input]").
4. **Name the target.** Introduce a symbol for the boundary value you want to find (e.g., (αi, Cαi)) — make it plural-indexed so a family is implied.
5. **Pin one instance.** Use "Thus" or "in the figure above" to bind the notation to one visible point.
6. **Defend the boundary.** Use "Notice that from the definition…" to explain why the graph behaves at the boundary (domain restriction, denominator, etc.).
7. **Zone the picture.** Split into regions (|x| < boundary gives n solutions; |x| > boundary gives 0) using "Moreover…".
8. **Convert to importance.** Write "therefore finding [boundary] may be crucial in [real application], as [region beyond] yields no solutions."
9. **Justify the tool.** State "To find this value, I will [technique] as [reason involving the boundary]."
10. **Launch the algebra.** Substitute u = …, v = … and write derivative expressions so the next section picks up the calculation cleanly.
