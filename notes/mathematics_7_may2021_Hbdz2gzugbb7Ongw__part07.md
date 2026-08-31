# Idea Flow Notes: mathematics_7_may2021_Hbdz2gzugbb7Ongw — variables

## Paragraph Flow (move by move)

**Paragraph 1** — *Kinetic energy in Cartesian velocity form*
- Move 1 (tool citation + setup): "Using Pythagoras' Theorem (v² = ẋ² + ẏ²)" — names the tool to be used; sets up that two formulas will follow.
- Hand-off: by naming Pythagoras, the next move must show that formula being applied.
- Move 2 (claim, two displayed equations): "T1 = ½m1(ẋ1² + ẏ1²)" and "T2 = ½m2(ẋ2² + ẏ2²)" — writes down the kinetic energies of the two masses as a direct application of the stated tool.
- Hand-off: the formulas are still in Cartesian velocities, so the next move must convert them into the working coordinate (θ̇) so the reader can recognise the system's generalised coordinates.

**Paragraph 2** — *Substituting θ̇ into the kinetic energies*
- Move 1 (pointer to prior work): "Expanding using equations (9) to (12)" — tells the reader which earlier results will now be substituted in.
- Hand-off: having named the substitutions, the reader expects the substituted, simplified forms next.
- Move 2 (result for T1): "T1 = (m1/2) l1² θ̇1²" — replaces Cartesian velocity with the angular velocity from eq. (9).
- Move 3 (result for T2): "T2 = ½m2 [ l1² θ̇1² + l2² θ̇2² + l1 l2 cos(θ2 − θ1)θ̇1 θ̇2 ]" — does the same for the second mass using eqs. (10–12); contains a cross-term because the second bob is attached to the first.
- Hand-off: kinetic energy is now fully expressed in the working coordinates, so the next paragraph must switch energy type — from kinetic to potential — using a parallel structure.

**Paragraph 3** — *Potential energy in Cartesian height form*
- Move 1 (new sub-topic + tool): "Gravitational potential energies Using equation (8)" — names a new energy quantity and the tool that defines it.
- Hand-off: by naming eq. (8), the reader expects V1 and V2 written in that tool's variables next.
- Move 2 (claim, two displayed equations): "V1 = m1 g y1" and "V2 = m2 g y2" — applies eq. (8) directly to each bob.
- Hand-off: again the variables are Cartesian, so the next move must mirror paragraph 2 and replace them with θ-coordinates.

**Paragraph 4** — *Substituting θ into the potential energies*
- Move 1 (pointer to prior work): "Expanding using equation (10) and (12)" — flags which substitutions will be used.
- Hand-off: the reader expects the simplified θ-forms.
- Move 2 (result for V1): "V1 = −m1 g l1 cos θ1" — the lower mass's height.
- Move 3 (result for V2): "V2 = −m2 g(l1 cos θ1 + l2 cos θ2)" — the upper mass's height relative to the pivot.
- Hand-off: with both T's and V's in θ-coordinates, the next move is the only remaining assembly step — forming the Lagrangian itself.

**Paragraph 5** — *Assembling the Lagrangian*
- Move 1 (operation + tools named): "Using the definition of the Lagrangian (equation 6) and the energies derived above" — names the combining rule and signals that everything already derived will be reused.
- Hand-off: by stating the operation and the ingredients, the next move is the explicit substitution.
- Move 2 (substitution statement): "L = T1 + T2 − V1 − V2" — writes the combining formula in words.
- Move 3 (full assembly, one displayed equation): equation (21) — plugs in equations (15)(16)(19)(20) and collects like terms, producing the final L in θ-coordinates.
- Hand-off (section end): the Lagrangian is now complete and the derivation stops.

## What This Section Does (content sequence)

1. **Open a derived quantity with the generic tool that defines it** — sets up what formula is about to appear (e.g. v² = ẋ² + ẏ² for T; y-coordinates for V).
2. **Write the quantity for each body in the tool's variables** — one equation per mass, in display form.
3. **Announce the substitution source** — point back at specific earlier equation numbers.
4. **Show the substituted, simplified form for each body** — one expanded equation per mass.
5. **Switch energy type using the same two-move pattern** — repeat steps 1–4 for the next energy quantity.
6. **Name the combining rule and the prior ingredients** — one sentence that previews the assembly.
7. **Display the final assembled expression** — one large multi-line equation that absorbs all previous steps.

The order works because the reader always needs the generic form before the substituted form, and needs every energy expressed in the *same* coordinate before they can be combined. The pattern is: **generic per body → specialise per body → switch quantity → combine all**.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Tool citation + per-body generic form"**
*"Using [named tool/equation]: [equation A for body 1]; [equation B for body 2]."*

- **Slots:**
  - Slot 1 — named tool/equation: a previously defined relation, in a present-participle lead-in ("Using …").
  - Slot 2 — equation for body 1: a displayed formula applying that tool to the first mass.
  - Slot 3 — equation for body 2: a parallel displayed formula for the second mass.
- **How to fill with a different idea:** Slot 1: pick any general formula from earlier in the document that defines a quantity. Slot 2: apply it to one component of your system and write the result as a numbered displayed equation. Slot 3: apply the same formula to the second component, matching the layout of Slot 2.
- **Original fill:** *"Using Pythagoras' Theorem (v² = ẋ² + ẏ²) and equation (7): T1 = ½m1(ẋ1² + ẏ1²) … T2 = ½m2(ẋ2² + ẏ2²)."*
- **Demonstration fill (different subject, same skeleton):** *"Using the moment-of-inertia formula (I = Σmr²) and equation (3): I₁ = m₁a₁²; I₂ = m₂(a₁² + a₂²)."*

**SKELETON B — "Announce substitution + expanded per-body form"**
*"Expanding using equations ([refs]): [expanded body 1]; [expanded body 2]."*

- **Slots:**
  - Slot 1 — pointer: present participle "Expanding using" followed by bracketed equation numbers from earlier.
  - Slot 2 — expanded body 1: a displayed equation in the working coordinate.
  - Slot 3 — expanded body 2: a parallel displayed equation, possibly longer if the body has more terms.
- **How to fill with a different idea:** Slot 1: name the specific substitutions that will be made. Slot 2: write body 1's simplified form. Slot 3: write body 2's simplified form — if the body is coupled to body 1, the expansion will contain cross-terms.
- **Original fill:** *"Expanding using equations (9) to (12): T1 = (m1/2) l1² θ̇1²; T2 = ½m₂ [l1² θ̇1² + l2² θ̇2² + l1 l2 cos(θ2 − θ1)θ̇1 θ̇2]."*
- **Demonstration fill (different subject, same skeleton):** *"Expanding using equations (5) to (7): KE₁ = ½m₁l₁²ω₁²; KE₂ = ½m₂[l₁²ω₁² + l₂²ω₂² + 2l₁l₂ω₁ω₂ cos(φ₂ − φ₁)]."*

**SKELETON C — "Combine into the final expression"**
*"[Using the definition of X (equation N)] and the [ingredients] derived above: [symbolic form]; [expanded multi-line equation]."*

- **Slots:**
  - Slot 1 — operation + tool: name the definition being invoked and what it operates on.
  - Slot 2 — ingredient phrase: a noun phrase collecting everything built earlier.
  - Slot 3 — symbolic form: one line stating L = T₁ + T₂ − V₁ − V₂ before expanding.
  - Slot 4 — expanded form: one large displayed equation grouping all terms.
- **How to fill with a different idea:** Slot 1: name the combining rule from earlier work. Slot 2: refer back to all quantities just derived. Slot 3: write the unexpanded combination. Slot 4: substitute each derived expression in, line by line, grouping terms that share a common factor.
- **Original fill:** *"Using the definition of the Lagrangian (equation 6) and the energies derived above: L = T₁ + T₂ − V₁ − V₂ = [full equation (21)]."*
- **Demonstration fill (different subject, same skeleton):** *"Using the definition of the Hamiltonian (equation 4) and the momenta derived above: H = p₁θ̇₁ + p₂θ̇₂ − L; [fully expanded multi-line H in θ-coordinates]."*

## Express-Idea Vocabulary

- **Sequencing / operation announcement:** "Using Pythagoras' Theorem (v² = ẋ² + ẏ²)"; "Expanding using equations (9) to (12)"; "Using equation (8)"; "Using the definition of the Lagrangian".
- **Cause / substitution driver:** "Expanding using equations (9) to (12)" — names what forces the simplification in the next line.
- **Specification / pointer-back:** "and the energies derived above" — locates the source of the inserted terms.
- **Assembly verbs:** "Using the definition of the Lagrangian" — frames the next line as a definition being applied.
- **Connectives in inline math:** "and" joins parallel terms in the displayed equations; "−" signs separate kinetic from potential contributions in L = T₁ + T₂ − V₁ − V₂.

## How to Explain an Idea (replication steps)

This section uses the **"per-body generic → per-body specialised → combine" pattern**. To reproduce it for a new derivation:

1. **Pick the generic defining tool.** Choose one previously derived equation that defines your target quantity in the most natural variables.
2. **Apply it to each component separately.** Write one displayed equation per body so the reader can see the rule being used identically each time.
3. **Name the substitutions that will specialise the result.** Announce in a short lead-in sentence which earlier equation numbers you will now substitute.
4. **Display the specialised form for each body.** Write one expanded equation per body; if a body is coupled to another, expect cross-terms in its expansion.
5. **Repeat steps 1–4 for the next quantity** (here, swap kinetic for potential energy, keeping the structure identical).
6. **State the combining rule in words.** One sentence names the definition that links the pieces.
7. **Write the symbolic combination, then the fully expanded final equation.** The symbolic line teaches the structure (e.g. L = T − V); the expanded line absorbs every result from steps 1–5.
