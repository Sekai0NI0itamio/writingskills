# Idea Flow Notes: mathematics_7_may2021_VRK57n2hZhnse7iX — 2.3.1     Identity & Inverse

## Paragraph Flow (move by move)

**Paragraph 1**
- S1 — **Definition**: "ε is the identity permutation." Establishes the symbol and names it.
- S2 — **Implication / behaviour claim**: "It has no impact on a permutation when applied in composition." States the property that makes identity worth naming.
- (Displayed matrix) — **Notation display**: shows ε in two-row permutation form; the *why-it-matters* of S2 is now visualised.
- **Handoff to P2**: S2's "no impact" quietly invites the reader to ask what the *opposite* operation would be — P2 answers exactly that ("opposite permutation").

**Paragraph 2**
- S1 — **Definition by contrast**: "An inverse is essentially an opposite permutation." Opens with "essentially" to compress a definition into one phrase, mirroring the structure of P1's opener.
- S2 — **Back-reference / recall of prior definition**: "Earlier, the permutation was defined as a bijective function…" Reminds the reader of the prerequisite so the next claim can build on it.
- S3 — **Specification / mechanism**: "The inverse of a permutation maps the elements of the codomain to the elements of the domain." Unpacks the abstract "opposite" claim into a precise mapping direction — the consequence of the recalled definition.
- S4 — **Transition to example**: "This is a numerical example:" Signals that the abstract machinery will now be shown concretely.
- (Displayed three-permutation chain) — **Worked instance**: B → its rearranged form → B⁻¹; the reader can trace the "reverse mapping" claim.

## What This Section Does (content sequence)
For a "define-and-contrast" concept pair section, the working order is: name concept A → state A's single key property → display A's notation → open concept B by direct contrast with A → recall the prerequisite definition → specify B's property mechanically → signal and run a worked example. A must arrive first because B is defined *as a contrast to A*; the prerequisite definition must appear *between* the contrast word and the mechanism, because the mechanism is meaningless without it; the example arrives last because it is the moment the reader verifies the whole chain.

## Paragraph Skeletons (replicable templates)

**SKELETON A — short concept paragraph**: "[Symbol] is the [concept]. It [single behavioural property under some operation]."
- Slot 1: symbol + "is the" + concept name, declarative present-tense.
- Slot 2: "It" + verb phrase giving one defining behaviour.
- Fill with: any mathematical object with one defining behaviour (e.g. null matrix, absorbing element, idempotent).
- Original: "ε is the identity permutation. It has no impact on a permutation when applied in composition."
- Demo fill: "Z is the zero matrix. It annihilates any conformable matrix under multiplication."

**SKELETON B — contrast-then-mechanism paragraph**: "[Concept B] is essentially [contrast word] [concept A]. Earlier, [concept A] was defined as [prerequisite definition]. The [specific case] of [B] [performs reverse/dual action]. This is a numerical example:"
- Slot 1: "B is essentially" + contrast adjective + "A"; "essentially" signposts definition.
- Slot 2: "Earlier, A was defined as …"; past-tense back-reference.
- Slot 3: directional verb phrase stating B's action.
- Slot 4: "This is a numerical example:" — fixed transition.
- Fill with: any (A, B) pair where B is the algebraic dual of A (inverse/direct, transpose/original, additive inverse/element).
- Original: "An inverse is essentially an opposite permutation. Earlier, the permutation was defined as a bijective function which maps elements of a set to itself. The inverse of a permutation maps the elements of the codomain to the elements of the domain. This is a numerical example:"
- Demo fill: "A transpose is essentially a flipped matrix. Earlier, a matrix was defined as a rectangular array of entries arranged in rows and columns. The transpose of a matrix swaps the entries along its main diagonal into columns. This is a numerical example:"

## Express-Idea Vocabulary
- Definition / naming: "ε is the identity permutation"; "is essentially an opposite permutation".
- Behaviour / implication: "It has no impact".
- Back-reference / sequencing: "Earlier, the permutation was defined as".
- Specification / mechanism: "maps the elements of the codomain to the elements of the domain".
- Transition to example: "This is a numerical example:".
- Contrast cue: "essentially an opposite".

## How to Explain an Idea (replication steps)
The pattern is **paired-concept introduction with contrast-led mechanism**: define A by its property, define B by contrast with A, recover the prerequisite definition, then state B's action mechanically and verify numerically.
1. Name concept A in one sentence using the copula ("X is the Y").
2. State A's single defining behaviour in one short clause — phrased negatively if the contrast will be negative, positively if positive.
3. Display A's notation so the reader has a visual anchor.
4. Open concept B with "is essentially" + contrast word + reference to A — forces A to stay in mind.
5. Use "Earlier, … was defined as …" to retrieve a prior definition; mandatory, because step 6 depends on it.
6. State B's specific action with a directional verb phrase ("maps … to …", "swaps … into …") — one sentence, one verb.
7. End with "This is a numerical example:" and immediately give a worked instance that traces the action.
