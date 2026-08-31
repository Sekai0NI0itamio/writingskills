# Idea Flow Notes: mathematics_7_may2021_6fXJObdFVGOuBxZp — particles would be

## Paragraph Flow (move by move)

**Paragraph 1**
- S1 — *definition of target quantity*: "Where 𝐼! is the moment of inertia of a disc." Hands reader forward by naming the quantity the whole paragraph is operating on — the reader now knows *what* the obstacle applies to.
- S2 — *narrative pivot / obstacle statement*: "At this point, I encountered complications in integrating ∆𝑚!." Hands reader forward by flagging a problem — the reader expects the next sentence to explain *why*.
- S3 — *cause of the obstacle*: "This is because ∆𝑚! is dependent upon the location of the fragment (which makes it a function of 𝑟!)." Hands reader forward by diagnosing the root cause and naming the variable 𝑟! — preparing the reader for a "rewrite in terms of r" move.

**Paragraph 2**
- S1 — *strategy announcement*: "To proceed further, I rewrote ∆𝑚! in terms of 𝑟!." Hands reader forward by stating the rescue move — the reader now expects a tool that makes this rewrite possible.
- S2 — *tool introduction / definition*: "I first defined the density of the material as 𝜌 = ! = !!" — definition with citation [13]. Hands reader forward by supplying the bridge variable; "Rearranging and substituting for ∆𝑚!" then hands the reader to the displayed equation as a worked result.

**Paragraph 3**
- S1 — *geometric justification (authority → insight)*: "Then from Figure 7, I realised that the area of a fragment, ∆𝐴! can be obtained through multiplying its sides." Hands reader forward by sourcing one specific sub-step from a figure — the reader expects the equation form of that insight.
- S2 — *sub-result, derived*: "thus ∆𝐴! = ∆𝑟 ∙ 𝑟! ∆𝜃." Hands reader forward by handing the reader a clean plug-in piece for the final substitution.
- S3 — *consequence / applied move*: "With this, I can rewrite the equation as" — the equation that follows. Hands reader forward (and to the next section) by completing the reformulation the obstacle demanded.

## What This Section Does (content sequence)

This is a **derivation-by-reformulation** section. The order is:

1. **Name the target expression** (what the working is aiming at) — so the reader knows what the obstacle is interrupting.
2. **State the obstacle** ("encountered complications") — so the reader understands why the current form is stuck.
3. **Diagnose the cause** (the troublesome term depends on a coordinate) — so the reader sees *what kind* of rewrite is needed.
4. **Announce the strategy** (rewrite the troublesome term in terms of the right variable) — so the reader knows the shape of the coming moves.
5. **Introduce a tool** (density, with citation) — gives the reader a bridging quantity.
6. **Substitute into the target** to express the troublesome term in product form — produces an intermediate result.
7. **Justify a sub-piece geometrically** via a figure — gives the reader the shape of one factor.
8. **Back-substitute to produce the final usable form** — closes the obstacle and hands the reader to the next integration step.

The order matters because: naming first anchors the reader, diagnosing the cause tells them *what* must change, announcing the strategy tells them *how*, the tool enables the algebra, the geometric sub-piece provides the missing factor, and only then can the final form be assembled.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Obstacle diagnosis**
`"[Target variable] is [brief definition]. At this point, I encountered complications in [operation on a term]. This is because [that term] is dependent upon [coordinate] (which makes it a function of [the coordinate])."`

1. **What each slot holds:** S1 = a one-clause definition of the quantity you are deriving. S2 = a first-person retrospective statement of the operational snag. S3 = a cause clause parenthetically clarifying the dependency.
2. **How to fill with a different idea:** Slot 1 — pick the symbol you want to arrive at, give a one-line definition. Slot 2 — pick the integration / summation step where the integrand resists, name it concretely. Slot 3 — name the spatial coordinate the troublesome term secretly depends on.
3. **Original filled version:** "Where 𝐼! is the moment of inertia of a disc. At this point, I encountered complications in integrating ∆𝑚!. This is because ∆𝑚! is dependent upon the location of the fragment (which makes it a function of 𝑟!)."
4. **Demonstration fill (different subject):** "Where 𝑄 is the heat conducted through the rod. At this point, I encountered complications in integrating 𝑑𝐴!. This is because 𝑑𝐴! is dependent upon the radial position of the ring (which makes it a function of 𝑟)."

**SKELETON B — Tool introduction + substitution**
`"To proceed further, I rewrote [problem term] in terms of [coordinate]. To do so, I first defined [tool] as [definition] [citation]. Rearranging and substituting for [problem term], [worked equation]."`

1. **What each slot holds:** S1 = strategy + target coordinate (infinitive clause). S2 = tool definition with reference. S3 = gerund pair signalling algebraic manipulation, leading to a displayed result.
2. **How to fill with a different idea:** Slot 1 — pick a troublesome term, name the variable you want it in. Slot 2 — pick a measurable property (density, permittivity, resistance per unit length…), define it formally with a citation. Slot 3 — chain the rearrangement verb + the substitution verb, then show the chain of equalities.
3. **Original filled version:** "To proceed further, I rewrote ∆𝑚! in terms of 𝑟!. To do so, I first defined the density of the material as 𝜌 = ! = !! [13]. Rearranging and substituting for ∆𝑚!, ∆𝑚! = 𝜌∆𝑉! = 𝜌 ∆ℎ ∆𝐴! = 𝜌∆ℎ ∙ ∆𝑟 ∙ 𝑟! ∆𝜃."
4. **Demonstration fill (different subject):** "To proceed further, I rewrote 𝑑𝐴! in terms of 𝑟. To do so, I first defined the surface charge density as 𝜎 = 𝑄/𝐴 [4]. Rearranging and substituting for 𝑑𝐴!, 𝑑𝐴! = 𝜎𝑑𝐴/𝑞 = 𝜎 ∙ 2𝜋𝑟𝑑𝑟."

**SKELETON C — Geometric justification + final substitution**
`"Then from [Figure X], I realised that [sub-quantity] can be obtained through [geometric reasoning], thus [sub-result]. With this, I can rewrite the equation as [final equation]."`

1. **What each slot holds:** S1 = a retrospective realisation sentence citing a figure. S2 = a one-line derivation of the sub-quantity. S3 = a "with this" bridge sentence that sets up the final displayed substitution.
2. **How to fill with a different idea:** Slot 1 — pick a sub-quantity inside your integrand, justify its form by pointing to a diagram. Slot 2 — name the geometric operation (multiplying sides, dividing by arc length, etc.) and write the resulting product. Slot 3 — perform the final substitution by re-stating the integrand in its new form.
3. **Original filled version:** "Then from Figure 7, I realised that the area of a fragment, ∆𝐴! can be obtained through multiplying its sides, thus ∆𝐴! = ∆𝑟 ∙ 𝑟! ∆𝜃. With this, I can rewrite the equation as ∆𝑚! = 𝜌 ∆ℎ ∆𝐴! = 𝜌∆ℎ ∙ ∆𝑟 ∙ 𝑟! ∆𝜃."
4. **Demonstration fill (different subject):** "Then from Figure 3, I realised that the arc length, 𝑑𝑠 can be obtained through multiplying a small angular displacement by the radius, thus 𝑑𝑠 = 𝑟𝑑𝜃. With this, I can rewrite the integral as 𝑊 = ∫ 𝐹 ∙ 𝑟𝑑𝜃."

## Express-Idea Vocabulary

- **Strategy / sequencing:** "To proceed further" (To proceed further, I rewrote ∆𝑚!); "first" (I first defined the density); "Then from Figure 7" (Then from Figure 7, I realised…).
- **Cause / consequence:** "This is because" (This is because ∆𝑚! is dependent); "thus" (thus ∆𝐴! = ∆𝑟 ∙ 𝑟! ∆𝜃).
- **Specification / definition:** "defined…as 𝜌 = ! = !!" (I first defined the density of the material as); parenthetical clarification "(which makes it a function of 𝑟!)" (which makes it a function of 𝑟!).
- **Evidence / sourcing:** "[13]" citation flag attached to a tool definition; "from Figure 7" anchoring a geometric claim to a diagram.
- **Procedure verbs:** "rewrote…in terms of" (I rewrote ∆𝑚! in terms of 𝑟!); "Rearranging and substituting" (Rearranging and substituting for ∆𝑚!); "can be obtained through multiplying" (∆𝐴! can be obtained through multiplying its sides); "can rewrite" (I can rewrite the equation as).
- **Obstacle language:** "I encountered complications" (I encountered complications in integrating); "dependent upon" (∆𝑚! is dependent upon the location).

## How to Explain an Idea (replication steps)

This section uses a **derivation-by-reformulation** pattern: obstacle → diagnosis → strategy → tool → substitution → geometric sub-justification → final assembly.

Steps to apply to a NEW idea:

1. **State the target expression in one clause** (what you are ultimately computing).
2. **Announce the obstacle** in first person past — name the specific algebraic operation that has stalled (e.g., "I encountered complications integrating…").
3. **Diagnose the cause** with "This is because…" — identify the hidden coordinate dependency inside the troublesome term, and parenthetically announce it is a function of that coordinate.
4. **Announce the rewrite strategy** with "To proceed further, I rewrote [term] in terms of [coordinate]."
5. **Introduce one bridging tool** with "To do so, I first defined [tool] as [definition] [citation]." The tool must convert an awkward quantity into the desired coordinate.
6. **Perform the substitution in a single displayed chain of equalities**, each link signposted by a verb (rearranging → substituting → expressing).
7. **Justify any remaining sub-piece geometrically** with "Then from Figure X, I realised that [sub-quantity] can be obtained through [geometric reasoning]."
8. **Close with "With this, I can rewrite the equation as…"** and show the final assembled expression, which now contains only the desired coordinate and is ready for the next step (integration, summation, etc.).
