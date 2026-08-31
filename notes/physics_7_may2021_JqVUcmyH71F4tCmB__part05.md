# Idea Flow Notes: physics_7_may2021_JqVUcmyH71F4tCmB — Rocket                                             Weight

## Paragraph Flow (move by move)

**Paragraph 1** (introduces the master equation for initial mass)
- Sentence 1: *Source claim* — "The initial mass, was given by the simulator" — names where the data came from; hands forward by ending on "simulator" and letting the next sentence offer a second, independent way to obtain it.
- Sentence 2: *Method pivot* — "It can be calculated through the following" — signals a formula is coming; hands forward by introducing Equation (9).
- (Equation 9: `M0 = Ms + Mc + Mp`) hands forward by leaving three sub-terms undefined.

**Paragraph 2** (zooms into the first sub-term)
- Sentence 1: *Specification / zoom-in* — "Where Ms is the mass of the structure" — picks one term out of Equation (9); hands forward by promising the formula that defines Ms.
- (Equation 10: `Ms = ρs V`) hands forward by introducing two new unknowns (V, ρs) and leaving Mc from (9) untouched.

**Paragraph 3** (inline symbol glossary)
- Sentence 1: *Definition of V* — "V being the rockets volume" — unpacks the first new symbol from (10); hands forward by stacking the next symbols to define.
- Sentence 2: *Definition of ρs and Mc* — "ρs the structural material payload, and Mc is" — finishes the symbol list and ties Mc back to (9); hands forward by closing the unpack of M0, freeing the next paragraph to switch topics.

**Paragraph 4** (switches to final mass)
- Sentence 1: *Topic switch / claim* — "The final mass was calculated with the equation" — moves from initial mass to final mass; hands forward by introducing Equation (11).
- (Equation 11: `Mf = M0 − Mp`) hands forward because M0 is now known and Mp reappears, threading into the next ratio.

**Paragraph 5** (composite ratio built from the two masses)
- Sentence 1: *Definition + method* — "The mass ratio (Λ), which states how much" — names the new quantity and gives its meaning in a relative clause; hands forward by saying "was calculated with the equation", so the formula is the next thing.
- (Equation 12: `Λ = M0/Mf`) hands forward by reusing M0 and Mf, completing the chain of definitions.

**Paragraph 6** (opens the next ratio, then cuts off)
- Sentence 1: *Definition (incomplete)* — "The thrust to weight ratio (Ψ0), indicating" — opens another ratio with the same appositive pattern; hands forward by signalling a definition of thrust-to-weight is coming.

## What This Section Does (content sequence)

This is a **parameter-glossary results subsection**. Its ordered moves are:

1. **Source claim** for a top-level quantity (e.g. M0 came from the simulator).
2. **Master equation** that splits the quantity into named sub-terms.
3. **Sub-term equation** that defines the first sub-quantity.
4. **Symbol glossary** that defines, in plain English, every new variable introduced so far.
5. **Next quantity equation** (e.g. Mf) — written using symbols already on the page.
6. **Composite ratio equation** (e.g. Λ = M0/Mf) — built from two quantities already defined.
7. **Next ratio definition** (Ψ0) — opens with an appositive, leaves room for its equation.

The order matters because each formula reuses symbols that earlier formulas defined. Defining M0 fully before introducing Mf means Mf's equation (`M0 − Mp`) needs no new glossary. Defining both masses before Λ means Λ needs no new glossary either. The section reads as a dependency graph unrolled top-to-bottom.

## Paragraph Skeletons

**SKELETON A — Source + master equation**
`"[Quantity], was [passive verb] by [source]. It can be calculated through the following equation: [equation with 2–3 sub-terms]."`
1. *Slots*: (1) name of quantity + comma + passive source claim; (2) pivot sentence promising an equation; (3) equation whose right-hand side has 2–3 named sub-terms.
2. *How to fill differently*: pick a top-level measured quantity; sentence 1 attributes it to a tool/dataset ("was recorded by", "was returned by"); sentence 2 then offers an independent formula.
3. *Original*: "The initial mass, was given by the simulator when designed. It can be calculated through the following equation: M0 = Ms + Mc + Mp."
4. *Demonstration fill*: "The lift force, was recorded by the load cell during testing. It can be calculated through the following equation: L = ½ ρ v² S C_L."

**SKELETON B — Sub-term equation**
`"Where [symbol] is [plain definition], given by: [equation with new symbols]."`
1. *Slots*: (1) "Where" + one symbol from the master equation + "is" + a short gloss; (2) colon that announces a formula; (3) equation whose right-hand side introduces fresh symbols.
2. *How to fill differently*: take the first sub-term from your master equation and write it as a product or simple function of measurable variables.
3. *Original*: "Where Ms is the mass of the structure, given by: Ms = ρs V."
4. *Demonstration fill*: "Where C_d is the drag coefficient, given by: C_d = f(Re, M)."

**SKELETON C — Inline symbol glossary**
`"[Symbol1] being [short meaning], and [Symbol2] is the [meaning] of [context], being [further specification]."`
1. *Slots*: (1) "being" + plain-English gloss for the first fresh symbol; (2) "and" + next symbol + "is" + longer gloss + optional appositive ("being …").
3. *Original*: "V being the rockets volume. ρs the structural material payload, and Mc is the mass of the payloads carrying, being any other non-structural components."
4. *Demonstration fill*: "v being the free-stream velocity. ρ the air density in the tunnel, and C_d is the dimensionless drag coefficient, being a function of Reynolds number."

**SKELETON D — Ratio definition + equation**
`"The [ratio name] ([symbol]), which [physical interpretation], was calculated with the equation: [ratio of two earlier symbols]."`
1. *Slots*: (1) ratio's plain name; (2) bracketed symbol; (3) relative clause stating what the ratio means in words; (4) "was calculated with the equation:" + formula whose numerator and denominator were both already defined.
2. *How to fill differently*: pick a dimensionless group whose numerator and denominator are already on the page.
3. *Original*: "The mass ratio (Λ), which states how much heavier the rocket is with propellant than without, was calculated with the equation: Λ = M0/Mf."
4. *Demonstration fill*: "The lift-to-drag ratio (L/D), which states how much lift is generated per unit of drag, was calculated with the equation: L/D = L ÷ D."

## Express-Idea Vocabulary

- **Sequencing / method pivots**: "It can be calculated through" (introduces a derivation step); "following equation" (formula marker); "Where" (zooms into one term).
- **Specification / unpacking**: "Where Ms is the mass" (sub-term zoom); "V being the rockets volume" (inline symbol gloss); "being any other non-structural components" (extends the gloss).
- **Definition verbs**: "is the mass of" (Skeleton B); "being" (Skeleton C, twice); "is the mass of the payloads" (Skeleton C).
- **Causation / derivation connectors**: "given by" — used both for a data source ("given by the simulator") and for a formula ("given by: Ms = ρs V"); "was calculated with" (formula introducer, used twice).
- **Appositive / relative-clause definers**: "which states how much heavier" (Skeleton D); "indicating the rockets how much thrust" (same pattern, cut off).
- **Evidence handling**: "given by the simulator when designed" — the simulator is treated as the sole authority; no "according to" or external citation.

## How to Explain an Idea (replication steps)

The pattern is **equation-anchored parameter glossary: define a quantity → give its equation → unpack every new symbol inline → move to the next quantity that reuses already-named symbols.**

1. **Open with a source claim.** State the quantity and where its raw value came from, in a passive clause: "[Quantity] was given by [tool/dataset]."
2. **Pivot to derivation.** Add a second sentence: "It can be calculated through the following equation:" then write the equation with 2–3 named sub-terms the reader will meet later.
3. **Zoom into the first sub-term.** Start with "Where", restate one symbol from step 2 in words, write "given by:" and give its equation, which introduces fresh symbols.
4. **Run a glossary sentence (or two).** Define every new symbol introduced in step 3, using "being" for short ones and "is the [noun] of [context]" for compound ones.
5. **Reuse loop.** Move to the next quantity with "The [next quantity] was calculated with the equation:" and write a formula that uses only symbols already defined.
6. **Build the ratio.** Introduce any dimensionless group as "The [ratio name] ([symbol]), which [physical interpretation], was calculated with the equation:" and write a fraction whose numerator and denominator were both already placed on the page.
7. **Keep going while every new formula reuses old symbols.** That reuse is the section's connective tissue — when a formula needs a symbol the reader has not met, stop and add a glossary pass before continuing.
