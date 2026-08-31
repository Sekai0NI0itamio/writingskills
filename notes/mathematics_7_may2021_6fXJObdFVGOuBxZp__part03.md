# Idea Flow Notes: mathematics_7_may2021_6fXJObdFVGOuBxZp — Particle

## Paragraph Flow (move by move)

**Paragraph 1**
1. **Claim/definition**: "Let 𝑟 be the displacement of the particle from a point 𝑃 and 𝑝 = 𝑚𝑣 be the linear momentum of the particle, where 𝑚 is the mass of the particle and 𝑣 is its linear velocity" — *sets up the variables and their physical meaning.*
   - **Hand-off**: This hands the reader the quantities needed, so the next sentence can combine them into a new definition.
2. **Definition**: "As angular momentum is defined as 𝐿 = 𝑟×𝑝 (section 2.1) then the angular momentum about point 𝑃 is would be 𝐿 = 𝑟×𝑝 = 𝑚𝑟×𝑣 [8]" — *applies the cross-product definition to the variables just introduced.*
   - **Hand-off**: Having stated the formula, the next paragraph can explore a property of this quantity (its dependence on reference point).

**Paragraph 2**
1. **Specification**: "It is important to note that the magnitude of 𝐿 depends on the choice of reference point 𝑃" — *qualifies the definition just given, flagging a condition the reader must hold.*
   - **Hand-off**: This caveat motivates the next move — introducing a force to see how 𝐿 changes.
2. **Cause/evidence**: "If there is a force 𝐹 acting on the particle, then according to Newton's second law 𝐹 = 𝑑𝑝/𝑑𝑡, there will be a change in momentum, 𝑝. This would result in a torque, τ" — *links force to momentum change and then to torque via Newton's second law.*
   - **Hand-off**: Having introduced torque, the next paragraph can express torque in terms of angular momentum.

**Paragraph 3**
1. **Transition/mechanism**: "As angular momentum, 𝐿 = 𝑟×𝑝 , I can write torque in terms of angular momentum" — *announces the goal: rewriting torque using the angular momentum definition.*
   - **Hand-off**: This sets up the mathematical tool needed to achieve the rewrite.
2. **Mechanism**: "To do so, I used the product rule for cross product, 𝑑(𝑎×𝑏)/𝑑𝑡 = 𝑟×𝑑𝑏/𝑑𝑡 + 𝑑𝑎/𝑑𝑡×𝑏 [9]. Thus 𝑑𝑝/𝑑𝑡 𝑑(𝑟×𝑝) 𝑑𝑟 𝑑(𝑟×𝑝) 𝑑𝐿 τ = 𝑟× = − ×𝑝 = − 𝑣× 𝑚𝑣 = 𝑑𝑡 𝑑𝑡 𝑑𝑡 𝑑𝑡" — *applies the product rule to expand the derivative of the cross product and simplifies.*
   - **Hand-off**: The simplified result leads directly to the physical conclusion.

**Paragraph 4**
1. **Implication**: "Here, I have deduced that torque is proportional to the rate of change of angular momentum" — *states the physical meaning of the derived equation.*
   - **Hand-off**: This proportional relationship sets up the conservation condition.
2. **Contrast/conclusion**: "This shows that without external torque, angular momentum is conserved. However," — *draws the conservation corollary and signals an unresolved point.*
   - **Hand-off**: The trailing "However," opens a contrast or limitation not yet completed.

---

## What This Section Does (content sequence)

1. **Define the quantities** (𝑟, 𝑝, 𝑚, 𝑣) and state the target formula (𝐿 = 𝑟×𝑝) — this gives the reader the symbols and the starting equation so subsequent algebra has a foundation.
2. **Flag a key property** (dependence on reference point) and introduce the external agent (force) — this creates the physical motivation for why the derivation matters.
3. **Apply a mathematical rule** (product rule for cross product) to rewrite torque in terms of angular momentum — this is the core deductive step that transforms the known into the new.
4. **State the physical implication** (torque ∝ 𝑑𝐿/𝑑𝑡) and the conservation corollary — this extracts the conceptual payoff from the algebra.

**Why this order**: Each move supplies exactly what the next needs — symbols before definition, definition before differentiation, differentiation before interpretation. A student replicating this with a different topic would first name the variables, then state a known law, then manipulate it with a mathematical tool, then state what the result means physically.

---

## Paragraph Skeletons (replicable templates)

**SKELETON 1** (Definition paragraph)
"[Variables] are defined as [quantities]; as [target concept] is defined as [formula] (source), then [application]."

1. **Slot shapes**: Slot 1 = noun phrase listing symbols and their meanings; Slot 2 = target concept name; Slot 3 = formal definition formula; Slot 4 = substituted working form.
2. **How to fill differently**: Slot 1: name three symbols with their physical quantities in a single sentence. Slot 2–4: pick a concept you have just defined in your course, quote its formal definition, then substitute to show the working equation.
3. **Original fill**: "Let 𝑟 be the displacement of the particle from a point 𝑃 and 𝑝 = 𝑚𝑣 be the linear momentum of the particle, where 𝑚 is the mass of the particle and 𝑣 is its linear velocity (Figure 6). As angular momentum is defined as 𝐿 = 𝑟×𝑝 (section 2.1) then the angular momentum about point 𝑃 is would be 𝐿 = 𝑟×𝑝 = 𝑚𝑟×𝑣 [8]."
4. **Different fill**: "Let 𝑉 be the volume of the gas and 𝑛 be the number of moles, where 𝑅 is the universal gas constant and 𝑇 is the temperature (Figure 1). As the ideal gas law is defined as 𝑃𝑉 = 𝑛𝑅𝑇 (section 3.2) then the pressure of the gas is 𝑃 = 𝑛𝑅𝑇/𝑉 [5]."

**SKELETON 2** (Derivation paragraph)
"As [target concept] equals [known expression], I can rewrite [new quantity] in terms of [target concept]. To do so, I used [mathematical rule], which [rule statement]. Thus [result]."

1. **Slot shapes**: Slot 1 = target concept with its formula; Slot 2 = new quantity to be expressed; Slot 3 = mathematical rule name; Slot 4 = the rule's formal statement; Slot 5 = the final derived expression.
2. **How to fill differently**: Slot 1: state the concept you are building on with its formula. Slot 2: name the quantity you want to derive. Slot 3–4: name the mathematical rule and quote or state it. Slot 5: write the simplified result.
3. **Original fill**: "As angular momentum, 𝐿 = 𝑟×𝑝 , I can write torque in terms of angular momentum. To do so, I used the product rule for cross product, 𝑑(𝑎×𝑏)/𝑑𝑡 = 𝑟×𝑑𝑏/𝑑𝑡 + 𝑑𝑎/𝑑𝑡×𝑏 [9]. Thus 𝑑𝑝/𝑑𝑡 𝑑(𝑟×𝑝) 𝑑𝑟 𝑑(𝑟×𝑝) 𝑑𝐿 τ = 𝑟× = − ×𝑝 = − 𝑣× 𝑚𝑣 = 𝑑𝑡 𝑑𝑡 𝑑𝑡 𝑑𝑡."
4. **Different fill**: "As work equals 𝑊 = 𝐹𝑑, I can express power in terms of work. To do so, I used the time-derivative rule, 𝑑𝑊/𝑑𝑡 = 𝑑(𝐹𝑑)/𝑑𝑡. Thus 𝑃 = 𝑑𝑊/𝑑𝑡 = 𝐹𝑣."

**SKELETON 3** (Conclusion paragraph)
"Here, I have deduced that [finding]. This shows that [implication]. However,"

1. **Slot shapes**: Slot 1 = a physical relationship discovered from the derivation; Slot 2 = the broader physical principle or condition that follows.
2. **How to fill differently**: Slot 1: state the proportional or equal relationship your algebra revealed. Slot 2: name the conservation law, condition, or physical consequence that follows when a variable is zero or constant.
3. **Original fill**: "Here, I have deduced that torque is proportional to the rate of change of angular momentum. This shows that without external torque, angular momentum is conserved. However,"
4. **Different fill**: "Here, I have deduced that the net heat input equals the change in internal work done. This shows that without heat loss, the internal energy of the system is conserved. However,"

---

## Express-Idea Vocabulary

**Sequencing**:
- "As angular momentum is defined as… then…" — links a prior definition to a new derivation step.
- "To do so, I used…" — signals the method chosen to achieve the stated goal.
- "Thus" — marks the algebraic result that follows from the applied rule.
- "Here, I have deduced that…" — announces the final physical finding after the derivation.

**Cause/consequence**:
- "This would result in a torque, τ" — states the physical consequence of a force acting on the particle.
- "This shows that without external torque, angular momentum is conserved" — draws the conservation implication from the derived proportionality.

**Contrast/concession**:
- "However," — signals an upcoming qualification or limitation (text trails off).
- "It is important to note that…" — foregrounds a caveat about the reference-point dependence.

**Evidence handling**:
- "according to Newton's second law 𝐹 = 𝑑𝑝/𝑑𝑡" — cites an established law as the basis for the next step.
- "[8]", "[9]" — anchors claims to referenced sources.

**Explanation verbs**:
- "is defined as 𝐿 = 𝑟×𝑝" — introduces the formal definition of angular momentum.
- "I used the product rule for cross product" — names the mathematical tool applied.
- "I have deduced that torque is proportional to…" — reports the conclusion drawn from the algebra.

---

## How to Explain an Idea (replication steps)

**Pattern**: Definition → property/condition → derivation (using a mathematical rule) → physical implication.

**Replication steps for a new idea**:

1. **Define every symbol** you will use in one sentence, giving each its physical meaning and unit.
2. **State the known definition or law** that your new idea builds on, citing where it comes from.
3. **Introduce the condition or external factor** (e.g., a force, a constraint) that makes the derivation necessary.
4. **Name the mathematical rule** you will apply and quote or write it out explicitly.
5. **Carry out the algebraic manipulation** step by step, showing how the known expression transforms into the new one.
6. **State the physical finding** in words — what the final equation tells you about the relationship between quantities.
7. **Extract the implication** — what happens when a variable is zero, constant, or at a limit — and signal any unresolved point with a contrast word ("however," "but," "yet").
