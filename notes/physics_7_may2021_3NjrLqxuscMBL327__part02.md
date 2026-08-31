# Idea Flow Notes: physics_7_may2021_3NjrLqxuscMBL327 — dynamic viscosity of a fluid such as blood measures its resistance to flow and is measured in Pascals second

## Paragraph Flow (move by move)

**Paragraph 1** (3 sentences)

- S1 — *Unit derivation / definition*: "(P a · s), otherwise kgm−1 s−1" → rewrites the SI unit of viscosity through dimensional analysis. Hands to S2 by **logical prerequisite**: you must show you understand the unit before you can claim anything about the quantity.
- S2 — *Significance / verdict*: "As a result of this research, I do believe that" → states a personal belief about the stakes of the investigation. Hands to S3 by **consequence**: a claim of importance logically births a question of how to test/measure it.
- S3 — *Question pivot / new frame*: "This results in asking myself 'How does" → turns the belief into a testable research question. Hands to the next paragraph by **specification**: the question names a target (viscosity of glycerol) that the method in P2 must answer.

**Paragraph 2** (1 sentence + figure)

- S1 — *Method announcement / claim*: "To measure the viscosity of glycerol I" → declares the tool (Stokes' Law). Hands forward by **promising** the reader that the next block will justify why Stokes' Law applies.
- Figure caption — *Visual evidence / reference*: "Sphere inside a fluid and its forces" → hands to P3 by giving the reader an image to map the forces onto.

**Paragraph 3** (5 sentences)

- S1 — *Authority / principle*: "From Newton's second law we know" → invokes a law. Hands to S2 by **specialisation**: the law must now be applied to the sphere.
- S2 — *Specialisation / case*: "In this case, our acceleration is g" → applies the law. Hands to S3 by **notation**: a defined variable is introduced.
- S3 — *Notation move*: "We will denote this as Fg" → labels the force. Hands to S4 by **contrast**: a single force is now contrasted with what opposes it.
- S4 — *Contrast / new force*: "However, when the sphere touches the liquid" → introduces the opposing buoyant force. Hands to S5 by **synthesis**: two forces are now available to combine.
- S5 — *Synthesis / setup*: "I can create a new equation for the net" → announces the net force equation that P4 will build.

**Paragraph 4** (algebraic block — treated as one move-chain)

- *Equation statement*: "FD = Fg − Fb" → writes the synthesis.
- *Expansion*: "= ms g − mg g" → unpacks the symbols.
- *Rewrite rule*: "I will rewrite the masses using the fact" → hands to the next line by signalling a substitution strategy.
- *Volume identity*: "the volume of the sphere can be given" → supplies the next substitution.
- *Buoyant volume claim*: "the buoyant force acts against the sphere, its volume" → explains why the sphere's volume also appears in the buoyant term. Hands to the final line by **causal completion**.
- *Final equation*: "Therefore we can write the net downward force as" → delivers the polished FD equation that P5 will analyse.

**Paragraph 5** (4 sentences)

- S1 — *Inference / sign check*: "However, from this we can see that" → notes that the density difference is positive. Hands to S2 by **implication**.
- S2 — *Implication*: "This implies that FD > 0" → concludes the sphere accelerates downward. Hands to S3 by **logical necessity**: if there is downward motion, there must be a drag force balancing it.
- S3 — *Contrast / new force*: "However, by Stokes' Law, there is another" → introduces the drag force as the counter. Hands to S4 by **definition**.
- S4 — *Definition / formula*: "This force is given by Fd" → writes Stokes' drag equation, completing the force triad.

---

## What This Section Does (content sequence)

A "physics setup / theoretical derivation" section. The moves, in order:

1. **Unit verification** — proves dimensional literacy about the quantity. Sets up that the quantity is real and measurable.
2. **Stakes statement** — personal claim about why the quantity matters. Sets up motivation for the work.
3. **Research question** — narrows the broad claim to one testable variable. Sets up what the rest must answer.
4. **Tool announcement** — names the law/method that will do the measurement. Sets up the upcoming derivation.
5. **Visual diagram** — gives a spatial map of the system so the algebraic symbols are anchored to a picture.
6. **Authority invocation** — calls on a known law (Newton's 2nd). Sets up the first force.
7. **Specialisation + notation** — applies the law to the actual sphere and labels the force (Fg). Sets up the first half of the net-force equation.
8. **Contrast/opposing force** — introduces the second force (Fb) via Newton's 3rd. Sets up subtraction.
9. **Net-force synthesis** — declares an equation for the combined downward force. Sets up algebra.
10. **Algebraic rewriting chain** — converts masses to densities × volumes step by step. Sets up a clean sign analysis.
11. **Sign/inference check** — verifies the net force is positive, i.e. the sphere actually falls. Sets up the need for drag.
12. **Final opposing force (drag) by Stokes' Law** — completes the force trio so the derivation can solve for η.

The order is: **dimension → motivation → question → tool → picture → law 1 → label → law 2 (opposite) → combine → algebra → verify sign → law 3 (opposite)**. Each move provides the variable or justification that the next move needs.

---

## Paragraph Skeletons (replicable templates)

### Skeleton A — "Unit → significance → question" opener

`SKELETON: "[Quantity] is measured in [primary unit], otherwise [SI breakdown] as we know that [base unit] is defined as [definition] =⇒ [identity]. As a result of this [context], I do believe that [claim about stakes]. This results in asking myself '[Research question]?'"`

1. **Slot meanings / shapes:**
   - Slot 1 (definition + dimensional proof): noun phrase naming the quantity, then an alternative unit expression; followed by a *that* clause deriving the base unit.
   - Slot 2 (significance): first-person present-tense belief statement with an evaluative adjective ("very dangerous").
   - Slot 3 (question): present-tense "How does X affect Y?" in inverted commas, framed as self-talk.
2. **How to fill with a different idea:** Pick a physical quantity you can dimensionalise (e.g. surface tension). Slot 1: write the unit (N/m) and derive it from N = kg·m·s⁻². Slot 2: claim real-world harm or benefit. Slot 3: turn that harm into a "How does temperature/concentration affect [quantity]?" query.
3. **Original filled version:** "(P a · s), otherwise kgm−1 s−1 as we know that Pascal is pressure defined as force (kgms−2 ) over area (m2 ) =⇒ 1P a = kgm−1 s−2 . As a result of this research, I do believe that a higher viscosity would be very dangerous to a human's well-being. This results in asking myself 'How does the temperature affect the viscosity of glycerol?'"
4. **Demonstration fill (different subject):** "(Nm−1), otherwise kg s−2 as we know that Newton is force defined as mass (kg) times acceleration (m s−2 ) =⇒ 1N = kg m s−2 . As a result of this research, I do believe that a lower surface tension would be very harmful to lung function. This results in asking myself 'How does the surfactant concentration affect the surface tension of distilled water?'"

### Skeleton B — "Tool declaration"

`SKELETON: "To [verb] the [quantity] of [substance] I will be utilising [named law or method]."`

1. **Slot meanings / shapes:** infinitive verb of action + "the [quantity] of [substance]" object + named tool. Single sentence, future-in-present tense ("I will be utilising").
2. **How to fill with a different idea:** Pick a measurement technique tied to a famous equation (e.g. Young's modulus via Hooke's Law). One sentence only, placed between the research question and the figure.
3. **Original filled version:** "To measure the viscosity of glycerol I will be utilising Stokes' Law."
4. **Demonstration fill:** "To determine the Young's modulus of a copper wire I will be utilising Hooke's Law."

### Skeleton C — "Authority → specialisation → notation → contrast → synthesis" force-decomposition paragraph

`SKELETON: "From [authority]'s [law] we know that [principle]. In this case, our [variable] is [value] for our [variable]. We will denote this as [symbol]. However, when [trigger condition], from [authority], there is [opposing force] [symbol]. This way, I can create a new equation for the net [resultant]."`

1. **Slot meanings / shapes:**
   - Authority + law: "From Newton's second law…" / "From [scientist]'s [law]…" (named source + named law).
   - Principle: that-clause stating the textbook fact.
   - Specialisation: "In this case, our [X] is [Y] for our [Z]."
   - Notation: "We will denote this as [symbol]."
   - Contrast: "However, when [physical contact / interaction], from [other authority], there is [opposing force] [symbol]."
   - Synthesis: "This way, I can create a new equation for the net [direction] force."
2. **How to fill with a different idea:** Choose a system with two opposing effects (a mass on a spring with damping, a charged particle in a magnetic field, an object on an inclined plane). Each slot maps cleanly: authority = textbook law; specialisation = your variable; notation = your label; contrast = the resisting force; synthesis = resultant.
3. **Original filled version:** "From Newton's second law we know that when a force is applied to a body of mass m it accelerates. In this case, our acceleration is g for our mass ms of the sphere. We will denote this as Fg. However, when the sphere touches the liquid, from Newton's third law, there is a force opposing the gravitation force of the sphere, the buoyant force Fb. This way, I can create a new equation for the net downward force FD."
4. **Demonstration fill:** "From Coulomb's Law we know that two charges exert a force along the line joining them. In this case, our separation is r for our charge q1. We will denote this as Fe. However, when the charge moves through the magnetic field, from the Lorentz force law, there is a force perpendicular to the velocity, the magnetic force Fm. This way, I can create a new equation for the net transverse force FT."

### Skeleton D — "Algebraic expansion chain leading to a clean form"

`SKELETON: "[Symbol] = [form 1] = [form 2] where [variable is defined]. I will rewrite the [quantities] using the fact that [identity]. [More substitution, one per line]. Therefore we can write [final compact form]."`

1. **Slot meanings / shapes:** equation on each line; "where" defining notation; "I will rewrite…" announcing strategy; successive identities (mass = density × V; V of sphere = 4/3 πr³); final compact equation introduced with "Therefore we can write".
2. **How to fill with a different idea:** Take any derivation where you start with a force, swap masses for densities × volumes, and end with a single bracketed factor. Replace each "mass" with "moles × molar mass", or each density with "concentration", keeping the rewriting rhythm.
3. **Original filled version:** "FD = Fg − Fb = ms g − mg g where mg is the mass of glycerol… I will rewrite the masses using the fact that mass = volume × density. I know that the volume of the sphere can be given as Vs = 4/3 πr³… Therefore we can write the net downward force as FD = Vs ρs g − Vs ρg g = Vs g(ρs − ρg)."
4. **Demonstration fill:** "FT = Fe − Fm = k q1 q2 − qvB… I will rewrite the forces using the fact that force = charge × field. I know that the Coulomb constant can be written as k = 1/(4πϵ0). Therefore we can write the net transverse force as FT = (q1 q2)/(4πϵ0 r²) − qvB."

---

## Express-Idea Vocabulary

**Sequencing / structuring**
- "In this case, our acceleration" — specialisation pivot from a general law to the concrete setup.
- "We will denote this as" — labelling move to fix a symbol.
- "Therefore we can write" — closing a derivation with a clean final form.

**Cause / consequence**
- "As a result of this research, I do believe" — claim of consequence from prior work.
- "This implies that FD > 0" — pure logical consequence marker.
- "This results in asking myself" — consequence-as-question pivot.

**Contrast / concession**
- "However, when the sphere touches the liquid" — introduces a competing force upon contact.
- "However, from this we can see that" — concession that revisits a previous statement to draw a new inference.
- "However, by Stokes' Law, there is another" — concession that the previous force picture is incomplete.

**Specification / precision**
- "respectively" — pairs two symbols with two referents (ρs and ρg).
- "In this case" — narrows the prior general law to one scenario.

**Evidence / authority handling**
- "we know that" — asserts a textbook fact.
- "From Newton's second law we know" — names the source explicitly.
- "from Newton's third law, there is" — names the second source for the opposing force.

**Explanation / definition verbs**
- "is defined as force… over area" — definitional breakdown of a unit.
- "can be given as Vs = 4/3 πr³" — supplies a standard identity.
- "is proportional to its velocity" — qualitative functional claim before the formula.
- "This force is given by Fd = 6πηrv" — formula introduction.

---

## How to Explain an Idea (replication steps)

The pattern this section uses is: **authority → specialisation → notation → contrast (opposing effect) → net synthesis → algebraic expansion → sign/feasibility check → opposing-effect formula**. To replicate it for a NEW idea:

1. **Name the authority and the law.** Open with "From [scientist]'s [law name] we know that [principle in a that-clause]." This borrows credibility and gives the reader a known anchor.
2. **Specialise to your case.** Write "In this case, our [variable A] is [value] for our [variable B]." This collapses the general law onto your specific system.
3. **Fix notation.** Add "We will denote this as [symbol]." Readers need a label to follow the algebra.
4. **Introduce the opposing effect with a contrast.** Use "However, when [trigger condition], from [second authority], there is [opposing force] [second symbol]." The "However" frames the new effect as the necessary counterbalance.
5. **Declare the synthesis.** Write "This way, I can create a new equation for the net [direction] [quantity] [symbol]." Promise an equation, then deliver it on the next line.
6. **Expand algebraically, one substitution at a time.** Convert each symbol into a deeper identity (mass → density × volume; volume of sphere → 4/3 πr³). Use "I will rewrite…" to announce the substitution strategy before you write it.
7. **Verify the sign or feasibility.** Add "However, from this we can see that [inequality]. This implies that [result]." This proves the setup is physically meaningful.
8. **Introduce the second opposing effect by name.** End with "However, by [third law], there is another force… This force is given by [formula]." This completes the force/equation picture and hands the reader to the next stage (solving for the unknown).

The discipline is: **never introduce a symbol without naming it; never add an opposing force without marking it with "However"; never end an algebraic step without "Therefore we can write"; never skip a feasibility check.** This rhythm is what makes the derivation feel logical rather than a dump of equations.
