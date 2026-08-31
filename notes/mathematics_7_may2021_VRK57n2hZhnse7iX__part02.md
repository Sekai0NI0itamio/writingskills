# Idea Flow Notes: mathematics_7_may2021_VRK57n2hZhnse7iX — 2.1    Permutations

## Paragraph Flow (move by move)

**Paragraph 1**
1. S1 — **Claim**: "The appropriate mathematical structure I identified was the permutation of a set." → Hands off by *naming the object* that the rest of the paragraph must define.
2. S2 — **Definition (with citation)**: "A permutation is a bijective function from a set to itself [QHH13]." → Hands off by *introducing an unknown term* ("bijective") that requires unpacking.
3. S3 — **Frame / topic sentence for a list**: "A bijective function has the properties of injectivity and surjectivity:" → Hands off by *announcing a two-part decomposition*, so the reader expects each property next.

**Paragraph 2**
1. S1 — **Synthesis / mechanism**: "A bijective function maps every element of one set to exactly one element of the second set." → Hands off by *collapsing the two listed properties into a single mechanism*, which then feeds the implication about permutations.
2. S2 — **Implication ("Hence")**: "Hence, a permutation, f, maps every element of a set back to an element in the same set." → Hands off by *applying the mechanism to the original object*, which now needs visual/notation form.
3. S3 — **Specification (setup for notation)**: "It uses the following notation for a set of size n, {1, 2, ···, n − 1, n}:" → Hands off by *declaring the domain*, so the matrix that follows is read as defined.

**Paragraph 3**
1. S1 — **Verdict on form**: "The function can be represented as a permutation in this form." → Hands off by *closing the abstract notation* and *pivoting to an instance*.
2. S2 — **Example-introducer**: "For an example, consider p:" → Hands off by *pointing to the concrete matrix below*.

**Paragraph 4**
1. S1 — **Unpack / reading of example**: "This permutation sends 1 to 2, 2 to 3, 3 to 1, 4 to 6, 5 to 5, and 6 to 4." → Hands off by *completing the example* with explicit mappings, then *widening* to a new operation.
2. S2 — **Definition of new operation**: "Permutations can also be applied one after another, known as compositions." → Hands off by *naming a new operation*, whose reading order must be specified.
3. S3 — **Specification (convention)**: "They are read from right to left in a composition." → Hands off by *stating a reading rule* that the next sentence will illustrate.
4. S4 — **Worked example of convention**: "A permutation g = pqr would be evaluated by applying r, then q and then p." → Hands off by *instantiating the rule*, which lets a final property follow.
5. S5 — **Property + consequence ("hence")**: "Compositions of permutations are not commutative, hence these cannot be swapped." → *Closes the section by warning the reader about a constraint.*

## What This Section Does (content sequence)

This is a **concept-anchoring section** for a technical definition. The ordered moves are:

1. **Announce the chosen mathematical object** ("permutation"). Sets up everything that follows.
2. **Give a one-sentence textbook definition with citation.** Anchors authority and terminology.
3. **Decompose a sub-term** ("bijective") into its two component properties and define each on a numbered list. Decomposition is needed before the reader can use the term freely.
4. **Collapse the two properties into one mechanism sentence.** Reinforces the definition without re-listing.
5. **Draw a consequence for the original object** ("Hence, a permutation …"). Re-applies the mechanism to the named object.
6. **Introduce notation** (general matrix form on a set of size n). Gives the reader a symbolic handle.
7. **Instantiate the notation with a concrete example** (the matrix p).
8. **Read the example element-by-element** so the notation is decoded, not just displayed.
9. **Extend to a second operation** (composition), **state its reading convention**, **illustrate it with a worked example**, and **flag a key non-property** (non-commutativity).

The order is deliberate: each move first establishes what the object *is*, then what it *looks like*, then what it *does*, then what *constraint* it carries. A reader can use an object only after they have definition → shape → behaviour → limits.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Define-and-decompose" paragraph**
**Slots:**
- Slot 1: A claim naming the chosen mathematical/tool object in the student's own voice. (*Grammatical shape:* noun phrase + past tense reporting verb.)
- Slot 2: A textbook definition of that object, with a bracketed citation. (*Grammatical shape:* "[Object] is [class] from [domain] to [codomain/range] [citation].")
- Slot 3: A sentence that flags a key sub-term and announces it will be broken into parts. (*Grammatical shape:* "[Object] has the properties of X and Y:")
- Slots 4–5: A numbered list of the two properties, each with a one-sentence gloss in parentheses.

**How to fill it with a different idea:**
- Slot 1: pick the structure you settled on for your exploration; state it as "The appropriate [structure] I identified was …"
- Slot 2: copy the source definition verbatim, append a bracketed reference.
- Slot 3: choose the unfamiliar word inside that definition and say it has two properties.
- Slot 4–5: define each property, then add a parenthetical gloss for the technical vocabulary (domain, range, codomain, etc.).

**Original filled version:** "The appropriate mathematical structure I identified was the permutation of a set. A permutation is a bijective function from a set to itself [QHH13]. A bijective function has the properties of injectivity and surjectivity: 1. Injectivity… 2. Surjectivity…"

**Demonstration fill with a different idea:** "The appropriate mathematical structure I identified was the eigenvalue of a square matrix. An eigenvalue of an n×n matrix A is a scalar λ for which Av = λv for some non-zero vector v [Str16]. The scalar λ satisfies two conditions: 1. Non-triviality: the eigenvector v is not the zero vector. 2. Linear dependence: the columns of (A − λI) become linearly dependent (the null space becomes non-trivial)."

---

**SKELETON B — "From mechanism to notation" paragraph**
**Slots:**
- Slot 1: A synthesis sentence collapsing the previously-listed properties into one mechanism. (*Grammatical shape:* "[Object] [does X] to every element of [set1].")
- Slot 2: An implication sentence applying that mechanism back to the named object, using "Hence" or "Therefore". (*Grammatical shape:* "Hence, a [object], f, [consequence].")
- Slot 3: A setup sentence for a general symbolic template. (*Grammatical shape:* "It uses the following notation for [generalised case]:")
- Slot 4: The symbolic template itself (matrix, equation, or diagram).

**How to fill it with a different idea:**
- Slot 1: re-state the combined effect of the two properties in plain language.
- Slot 2: bridge back to the named object with a consequence connective.
- Slot 3: choose a parameter (n, k, t) and declare its domain explicitly.
- Slot 4: write the general formula/array.

**Original filled version:** "A bijective function maps every element of one set to exactly one element of the second set. Hence, a permutation, f, maps every element of a set back to an element in the same set. It uses the following notation for a set of size n, {1, 2, ···, n − 1, n}: [matrix f]."

**Demonstration fill with a different idea:** "An inner product combines two vectors into a single scalar in a bilinear, symmetric way. Hence, the dot product, ⟨u, v⟩, returns a real number that reflects both vectors' alignment. It uses the following notation for two n-component vectors u = (u₁, …, uₙ) and v = (v₁, …, vₙ): ⟨u, v⟩ = Σ uᵢvᵢ."

---

**SKELETON C — "Decode-the-example" paragraph**
**Slots:**
- Slot 1: A verdict sentence stating that the notation shown represents the operation. (*Grammatical shape:* "[Object] can be represented as a [thing] in this form.")
- Slot 2: An example-introducer pointing at a labelled instance. (*Grammatical shape:* "For an example, consider [label]:")
- Slot 3: The labelled instance (matrix, equation, diagram).
- Slot 4: A sentence reading the instance element-by-element so the reader sees the mapping.

**How to fill it with a different idea:**
- Slot 1: close the abstract display by stating it is the canonical form.
- Slot 2: name a concrete instance (p, T, f₂) and announce you will display it.
- Slot 3: typeset the instance with a label.
- Slot 4: walk through every entry/mapping so nothing is left implicit.

**Original filled version:** "The function can be represented as a permutation in this form. For an example, consider p: [matrix p]. This permutation sends 1 to 2, 2 to 3, 3 to 1, 4 to 6, 5 to 5, and 6 to 4."

**Demonstration fill with a different idea:** "A linear map can be represented as a matrix in this form. For an example, consider T: ℝ³ → ℝ³: [3×3 matrix]. This transformation sends (1, 0, 0) to (2, −1, 0), (0, 1, 0) to (0, 3, 1), and (0, 0, 1) to (4, 0, 5)."

---

**SKELETON D — "Extend-and-warn" paragraph**
**Slots:**
- Slot 1: A definition of a secondary operation built on the primary object. (*Grammatical shape:* "[Primary objects] can also be applied one after another, known as [new term].")
- Slot 2: A convention for how that secondary operation is read. (*Grammatical shape:* "They are read [direction] in a [new term].")
- Slot 3: A worked illustration of the convention using a compound symbol. (*Grammatical shape:* "A [new term] g = [compound] would be evaluated by [order].")
- Slot 4: A property warning closing the section, introduced by "hence" or "therefore". (*Grammatical shape:* "[New terms] are not [property], hence [constraint].")

**How to fill it with a different idea:**
- Slot 1: pick a secondary operation (composition, convolution, nesting, iteration) and define it in one sentence.
- Slot 2: state the reading or evaluation order explicitly.
- Slot 3: write a three-letter/three-symbol compound and apply the rule.
- Slot 4: state a known limitation (non-commutativity, non-associativity, divergence) and the practical consequence.

**Original filled version:** "Permutations can also be applied one after another, known as compositions. They are read from right to left in a composition. A permutation g = pqr would be evaluated by applying r, then q and then p. Compositions of permutations are not commutative, hence these cannot be swapped."

**Demonstration fill with a different idea:** "Functions can also be applied one after another, known as composition. They are read from right to left in a composition. A function h = f ∘ g ∘ r would be evaluated by applying r first, then g, then f. Compositions of functions are not commutative in general, hence these cannot be reordered without changing the output."

## Express-Idea Vocabulary

**Sequencing / move-announcers**
- "A bijective function has the properties of" — opens a decomposition list ("A bijective function has the properties of injectivity and surjectivity").
- "For an example, consider" — pivots to a worked instance ("For an example, consider p").

**Cause / consequence**
- "Hence, a permutation, f, maps every element" — derives the named object's behaviour from the mechanism ("Hence, a permutation, f, maps every element of a set back").
- "hence these cannot be swapped" — closes with a practical consequence of a property ("Compositions of permutations are not commutative, hence these cannot be swapped").

**Specification / precision**
- "where the domain is the input" — pins down a technical term inside a parenthetical ("mapped to a unique element of the range set (where the domain is the input").
- "codomain is the set of all possible values" — same job, second item ("(codomain is the set of all possible values of the function)").

**Definition verbs / explanation verbs**
- "is a bijective function from a set to itself" — textbook class-membership definition ("A permutation is a bijective function from a set to itself").
- "known as" — labelling move ("can also be applied one after another, known as compositions").
- "can be represented as a permutation in this form" — form-introducer ("The function can be represented as a permutation in this form").

**Evidence / authority handling**
- "[QHH13]" — bracketed inline citation supporting the textbook definition ("A permutation is a bijective function from a set to itself [QHH13]").

**Reading-rule phrasing**
- "They are read from right to left" — convention statement ("They are read from right to left in a composition").
- "would be evaluated by applying" — worked-application framing ("A permutation g = pqr would be evaluated by applying r").

## How to Explain an Idea (replication steps)

This section uses the pattern: **definition → decomposition of a sub-term → mechanism synthesis → re-application via "Hence" → general notation → concrete instance → element-by-element decoding → secondary operation → reading convention → worked illustration → constraint warning.**

Step-by-step to explain a NEW idea the same way:

1. **Open with a self-referential claim** naming the object you settled on for your exploration. Use past tense ("The appropriate … I identified was …") so it reads as a justified choice, not a fact.
2. **Give the textbook definition in one sentence**, naming the class it belongs to and the source set/target set, and append a bracketed citation. This is your authority anchor.
3. **Identify the most unfamiliar word inside that definition** and announce it has two component properties. Use the phrasing "has the properties of X and Y:" so the reader expects a numbered list.
4. **Write a numbered list of the two properties**, each one a short definition followed by a parenthetical gloss that translates the technical vocabulary (domain, range, codomain, …).
5. **Collapse the two properties into a single mechanism sentence** ("[Object] [does X] to every element …"). This is what the reader carries forward; it is the reason "Hence" will work next.
6. **Use "Hence" to re-apply the mechanism to your named object** and introduce a variable label (f, T, p) for it. This shows the definition is not abstract — it lands on your case.
7. **State a general symbolic notation** for the object over a parameterised domain (size n, two vectors of length n, a 3×3 matrix), and typeset it.
8. **Verdict sentence**: assert that this notation *is* the canonical form of the object ("The function can be represented as a permutation in this form").
9. **Introduce a concrete instance** with "For an example, consider [label]:" and typeset the instance.
10. **Decode the instance entry-by-entry** so the reader sees every mapping, not just the shape. Use parallel "sends a to b" phrasing.
11. **Extend to a secondary operation** built on the primary object. Define it in one sentence and *name* it ("known as compositions").
12. **State the reading/evaluation convention** for the new operation in a single short sentence.
13. **Instantiate the convention** with a compound symbol and walk through the order of application.
14. **Close with a property warning** introduced by "hence", naming a non-property (non-commutativity, non-associativity) and its practical consequence. This stops the reader from misusing the operation.
