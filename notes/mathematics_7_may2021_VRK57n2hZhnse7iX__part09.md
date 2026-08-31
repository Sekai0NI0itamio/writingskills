# Idea Flow Notes: mathematics_7_may2021_VRK57n2hZhnse7iX — key to showing this result is to formalise a permutation based on its Vandermonde polynomial

## Paragraph Flow (move by move)

**Paragraph 1**

1. **Sentence 1** — Transition/verdict: "These definitions of the permutation allow for a more rigorous proof." Hands to next sentence by **promising a proof mechanism**, which the following definition will supply.
2. **Sentence 2** — Definition opener with citation: "The Vandermonde polynomial is defined as [Dun08]:" Hands to next sentence by **introducing a formal object that needs a domain** (i.e., what it applies to).
3. **Sentence 3** — Specification of domain: "for a permutation on a set with n unique elements." Hands to next sentence by **naming a general action (transposition)** that the reader should now inspect.
4. **Sentence 4** — Mechanism claim: "Any transposition of elements, u and v, ... will swap every instance of xu and xv in the polynomial." Hands to next sentence by **asserting a rule without numbers** — the reader expects the rule made concrete.
5. **Sentence 5** — Example marker + base instance: "For example:" followed by P(x₁,x₂,x₃) = (x₁−x₂)(x₂−x₃)(x₁−x₃). Hands to next sentence by **showing the un-permuted baseline**, so the next move can apply a concrete permutation to it.
6. **Sentence 6** — Worked example setup: "If a relatively simple permutation were applied, such as σ=(1 2), which swaps 1 and 2 [Bas+08]:" Hands to next display by **introducing a named σ and an action**, so the formula now shows what swapping does.

## What This Section Does (content sequence)
1. **Bridge from prior definition** — first sentence confirms the prior definition has now armed a proof (sets up *why* the reader should keep reading).
2. **Cite and define the central polynomial** — gives the formal object with authority.
3. **Restrict the domain** — "for a permutation on a set with n unique elements" so the formula's inputs are unambiguous.
4. **State the general behavioural rule** — what a transposition *does* to the polynomial (swaps every instance).
5. **Show the untouched polynomial** — concrete 3-variable instance as a baseline.
6. **Apply a minimal named permutation** — simplest non-trivial σ, then display the new polynomial to make the rule visible.

This order works because each move narrows the reader's uncertainty: existence → form → scope → behaviour → concrete case → worked case.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "definition-then-applicability" mini-frame**
"These definitions of [object] allow for a more [rigorous/proof-based/precise] [outcome]. The [object] is defined as [citation]: [formula] for a [context] with [condition]. Any [basic operation], [example], for example, will [effect] every [instance] in the [object]."

1. **Slot 1** (clause, past/present verb): a verdict on prior definitions, predicate "allow for …".
2. **Slot 2** (noun phrase + citation): names the new formal object.
3. **Slot 3** (display formula): the object itself.
4. **Slot 4** (prepositional phrase): "for a [context] with [condition]" — narrows inputs.
5. **Slot 5** (general rule clause): what a basic operation does to every variable in the object.
6. **Fill with a different idea** — replace "permutation" with "symmetric group" and "Vandermonde polynomial" with "cycle index polynomial"; swap "transposition" with "conjugation"; same skeleton produces a parallel paragraph.
7. **Original filled**: "These definitions of the permutation allow for a more rigorous proof. The Vandermonde polynomial is defined as [Dun08]: P(x₁,…,xₙ)=∏(xᵢ−xⱼ) for a permutation on a set with n unique elements. Any transposition of elements, u and v, for example, will swap every instance of xᵤ and xᵥ in the polynomial."
8. **Demonstration fill (different idea)**: "These definitions of the matrix allow for a more efficient determinant. The characteristic polynomial is defined as [Axl11]: p(λ)=det(λI−A) for a square matrix of order n with real entries. Any row swap, rows i and j, for example, will change the sign of every cofactor in the polynomial."

**SKELETON B — "baseline-then-applied-permutation" display pair**
"For example: [untouched formula]. If a relatively simple [operation] were applied, such as [σ]=([action]), which [plain-English description] [citation]: [transformed formula]."

1. **Slot 1** ("For example:" + display): the object in its default state.
2. **Slot 2** (conditional clause, present/future passive): introduces σ in cycle notation.
3. **Slot 3** (display): the object after σ acts on it.
4. **Fill with a different idea** — swap "Vandermonde / permutation σ=(1 2)" for "determinant of a 3×3 / row swap"; same shape works.
5. **Original filled**: "For example: P(x₁,x₂,x₃) = (x₁−x₂)(x₂−x₃)(x₁−x₃). If a relatively simple permutation were applied, such as σ=(1 2), which swaps 1 and 2 [Bas+08]: P(xσ(1),xσ(2),xσ(3)) = (x₂−x₁)(x₁−x₃)(x₂−x₃)."
6. **Demonstration fill (different idea)**: "For example: det(A) = a₁₁(a₂₂a₃₃−a₂₃a₃₂) − a₁₂(a₂₁a₃₃−a₂₃a₃₁) + a₁₃(a₂₁a₃₂−a₂₂a₃₁). If a relatively simple row swap were applied, such as R₁↔R₂, which exchanges rows 1 and 2 [Str16]: det(A') = −a₁₁(a₂₂a₃₃−a₂₃a₃₂) + a₁₂(a₂₁a₃₃−a₂₃a₃₁) − a₁₃(a₂₁a₃₂−a₂₂a₃₁)."

## Express-Idea Vocabulary

- **Sequencing / transition**: "These definitions … allow for" (bridge from prior paragraph).
- **Authority/definition**: "is defined as [Dun08]" (formal object + source).
- **Specification / scoping**: "for a permutation on a set with n unique elements" (input domain).
- **Generalisation + example**: "Any transposition of elements, u and v, for example," (universal claim via canonical instance).
- **Mechanism verbs**: "will swap every instance of xᵤ and xᵥ" (states the rule's action).
- **Example markers**: "For example:" (signals a concrete instance follows).
- **Conditional worked case**: "If a relatively simple permutation were applied, such as σ=(1 2)" (sets up a minimal worked example).
- **Plain-English unpacking**: "which swaps 1 and 2" (translates notation for the reader).
- **Citation inline**: "[Bas+08]", "[Dun08]" (sources attached to the formal move, not separated).

## How to Explain an Idea (replication steps)
The pattern is: **definition → domain → general behaviour rule → baseline instance → minimal worked instance**. Replicate with these numbered steps:

1. **Open with a bridging sentence** that tells the reader what the prior material now enables (here: "more rigorous proof"). Frame the new section's payoff in one clause.
2. **Name and cite the central object** in the form "The X is defined as [source]:" — the colon signals a display formula will follow.
3. **Display the formula**, then immediately add a prepositional phrase restricting its inputs ("for a … with …").
4. **State the universal behaviour** of the simplest non-trivial operation on the object ("Any … will … every instance of …"). Keep it abstract (variables u, v, not numbers).
5. **Insert the marker "For example:"** and show the formula with the smallest non-trivial number of inputs (here n=3). This is the untouched baseline.
6. **Introduce the worked case via a conditional** ("If a relatively simple … were applied, such as σ=(…), which … [citation]:") and display the transformed formula, making the behaviour from step 4 numerically visible.
