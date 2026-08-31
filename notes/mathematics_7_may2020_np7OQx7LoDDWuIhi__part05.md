# Idea Flow Notes: mathematics_7_may2020_np7OQx7LoDDWuIhi — that would result in complicated polynomials that are unnecessarily long and would be time

## Paragraph Flow (move by move)

### Paragraph 1

**Sentence 1** — *Problem/limitation (tail of prior sentence)*: "...consuming to expand and simplify."
*Move:* states a downside of the approach used just before. *Hand-off:* the dangling "as such" implied in the missing sentence stem signals that the reader should expect a remedy; the very next sentence delivers it.

**Sentence 2** — *Consequence/proposal*: "As such, it could be helpful to divide the egg into three sections: left, middle and right, where each section can be modelled using a separate polynomial."
*Move:* structural solution that follows the recognised problem; defines the three sub-units of analysis. *Hand-off:* the promise "can be modelled using a separate polynomial" forces the next sentence to specify WHICH polynomial degree is being chosen.

**Sentence 3** — *Specification with rationale*: "I have chosen to simply use quadratic equations; in which case I will need three data points for each section."
*Move:* pins down the degree (quadratic) and the data requirement (3 points) that makes the next formula valid. *Hand-off:* "in which case" turns the degree choice into a data-count condition, which directly justifies why the Lagrange formula that follows takes three terms.

**Sentence 4** — *Definition / general formula set-up*: "The Lagrange interpolation formula for a quadratic (n = 2, i = 3) is then written as:"
*Move:* introduces the abstract tool, labelling it with the parameters (n = 2, i = 3) that mirror sentence 3. *Hand-off:* "is then written as" opens an equation slot — the reader now expects the boxed display.

**Display (equation 8)** — *Tool / mechanism*: "𝑄(𝑥) = ... + ... + ..." (the Lagrange quadratic template).
*Move:* shows the generic symbolic machine. *Hand-off:* because the terms carry the symbols x₁, x₂, x₃ and y₁, y₂, y₃, the reader expects these slots to be filled with concrete coordinates next.

### Paragraph 2

**Sentence 1** — *Application / evidence handling*: "Using three randomly chosen co-ordinates from the 'left' section of the egg (given in Table 1), we can therefore find the quadratic equation, 𝑄ₗ(x), to be:"
*Move:* selects concrete data points and promises a specific instance of the general formula. *Hand-off:* "we can therefore find … to be" sets up the substituted expression that follows and the numerical answer that closes the paragraph.

**Display (substituted formula)** — *Worked substitution*: "(𝑥 − 0.25)(𝑥 − 0.512) / ((0 − 0.25)(0 − 0.512)) (0.01) + …"
*Move:* slots the three chosen coordinates into the Lagrange template from paragraph 1. *Hand-off:* because every variable now has a number, the reader expects a closed-form polynomial.

**Final line** — *Verdict / result*: "≈ −3.884244x² + 4.475061x + 0.01 (6 d.p.)"
*Move:* delivers the simplified quadratic that the paragraph promised. *Hand-off:* the "≈" and the stated precision flag the end of the working; any continuation would have to verify, graph, or move to the middle section.

---

## What This Section Does (content sequence)

The section is a **method-justification + first worked example** that follows this fixed sequence:

1. **Acknowledge a limitation** of the prior approach (too much expanding/simplifying) — sets the reader up to want a cleaner route.
2. **Propose a structural decomposition** (divide the egg into left/middle/right sections, each its own polynomial) — this is what makes separate fitting possible.
3. **Pin the polynomial degree and data requirement** (quadratic ⇒ three points per section) — converts the structural idea into a numerical specification.
4. **State the general formula** with its parameters labelled — supplies the tool that the specification makes useable.
5. **Apply the formula to one chosen section** (the 'left' section, coordinates from Table 1) — demonstrates the tool working on real data.
6. **Give the numerical result with precision stated** — closes the example and confirms the method actually produces a usable equation.

The order matters because each move converts the previous move into the *conditions* the next move needs: the limitation creates the need for decomposition; decomposition makes degree choice meaningful; degree choice justifies the three-point Lagrange template; the template makes substitution possible; substitution yields a result.

---

## Paragraph Skeletons (replicable templates)

### Skeleton A — "From limitation to method"

**SKELETON:** "[Short statement of why the previous approach is too costly]. As such, it could be helpful to divide the [object] into three sections: A, B and C, where each section can be modelled using a separate [tool]. I have chosen to simply use [specific choice]; in which case I will need [number] data points for each section. The [named formula] for a [choice] is then written as:"

**Slot instructions:**
- **Slot 1 — Limitation tail** (past participle phrase): name the wasted resource of the earlier method (e.g. "time-consuming to expand", "algebraically unwieldy to simplify").
- **Slot 2 — Decomposition proposal** (full clause with "As such, it could be helpful to"): partition the object into 2–4 named sub-units and assert that each is fitted independently.
- **Slot 3 — Tool choice + data count** (semicolon-joined sentences): declare the lowest-degree family that fits, then specify the point count that degree demands.
- **Slot 4 — Formula introduction** ("The [formula name] … is then written as:"): name the tool and any parameter labels, then present the boxed equation.

**Original fill:** "...consuming to expand and simplify. As such, it could be helpful to divide the egg into three sections: left, middle and right, where each section can be modelled using a separate polynomial. I have chosen to simply use quadratic equations; in which case I will need three data points for each section. The Lagrange interpolation formula for a quadratic (n = 2, i = 3) is then written as:"

**Demonstration fill (different idea):** "...tedious to differentiate by hand. As such, it could be helpful to divide the wing's cross-section into three regions: leading edge, midsection and trailing edge, where each region can be modelled using a separate camber line. I have chosen to simply use cubic polynomials; in which case I will need four data points for each region. The cubic spline interpolation formula (n = 3, i = 4) is then written as:"

### Skeleton B — "From general formula to one worked instance"

**SKELETON:** "Using [number] randomly chosen co-ordinates from the '[section name]' of the [object] (given in Table X), we can therefore find the [output function], to be: [substituted display] ≈ [closed-form numeric result] ([precision])."

**Slot instructions:**
- **Slot 1 — Data selection clause** ("Using N … co-ordinates from the '[section]'"): pick the count that matches your skeleton A choice, name which sub-unit, and cross-reference a table.
- **Slot 2 — Promise of result** ("we can therefore find … to be:"): use "therefore" to mark the deduction from the general formula.
- **Slot 3 — Substituted display**: every symbolic variable from skeleton A's equation must now have a numerical coordinate plugged in.
- **Slot 4 — Closed-form result with precision**: end with "≈", the simplified polynomial/function, and the decimal-place count in parentheses.

**Original fill:** "Using three randomly chosen co-ordinates from the 'left' section of the egg (given in Table 1), we can therefore find the quadratic equation, 𝑄ₗ(x), to be: [Lagrange substitution] ≈ −3.884244x² + 4.475061x + 0.01 (6 d.p.)"

**Demonstration fill (different idea):** "Using four randomly chosen co-ordinates from the 'leading edge' of the wing (given in Table 2), we can therefore find the cubic camber function, 𝑦ₗₑ(x), to be: [cubic-spline substitution] ≈ 0.0021x³ − 0.0417x² + 0.3184x + 0.0275 (4 d.p.)"

---

## Express-Idea Vocabulary

**Sequencing / ordering**
- "is then written as" — *"The Lagrange interpolation formula for a quadratic (n = 2, i = 3) is then written as:"* — marks the move from choice to formal tool.

**Cause / consequence**
- "As such" — *"As such, it could be helpful to divide the egg"* — converts the previous limitation into a justification for the next proposal.
- "in which case" — *"I have chosen to simply use quadratic equations; in which case I will need"* — turns the polynomial-degree decision into a direct data-count consequence.
- "therefore" — *"we can therefore find the quadratic equation"* — draws the result from the substituted formula.

**Evidence handling**
- "Using … co-ordinates … (given in Table 1)" — anchors the working in a previously produced data source.

**Explanation / mechanism verbs**
- "can be modelled using" — *"where each section can be modelled using a separate polynomial"* — names what the tool *does* in this context.
- "chosen to" — *"I have chosen to simply use quadratic equations"* — flags the modelling decision and signals its minimality ("simply").
- "find … to be" — *"we can therefore find the quadratic equation … to be"* — frames the next display as the resolution of the calculation.

---

## How to Explain an Idea (replication steps)

The section runs a **limitation → decomposition → degree choice → general formula → one worked instance → numeric result** pattern. To reproduce it for a new idea:

1. **Open with a limitation of the previous method** (one participial phrase is enough: "time-consuming to …", "algebraically messy to …"). This earns the reader's need for a new approach.
2. **Propose a structural decomposition** using "As such, it could be helpful to divide [object] into [N] sections: A, B, C, where each section can be modelled using a separate [tool]." Each unit must later become its own fit.
3. **Pick the lowest-degree family that can do the job** ("I have chosen to simply use [degree] equations") and immediately state the data count it forces ("in which case I will need [degree+1] data points for each section"). This converts the structural idea into a numerical specification.
4. **Introduce the named general formula** with its parameters labelled ("The [formula name] for a [degree] is then written as:") and display it in a centred equation.
5. **Pick concrete data for one sub-unit only** ("Using [N] … co-ordinates from the '[section name]' of the [object] (given in Table X)") and use "we can therefore find … to be:" to signal that the general formula is about to be instantiated.
6. **Show the substituted display** with every symbol from step 4 replaced by a number.
7. **Close with the simplified closed-form result**, prefaced by "≈" and suffixed with the working precision in parentheses, e.g. "(6 d.p.)". This both validates the method and gives the reader a ready-to-use equation.
