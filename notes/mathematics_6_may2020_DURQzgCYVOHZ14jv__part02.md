# Idea Flow Notes: mathematics_6_may2020_DURQzgCYVOHZ14jv — however in order to get into that much detail, we need to first understand what modular arithmetic is

## Paragraph Flow (move by move)

**Paragraph 1** (headlined "PRIME NUMBERS")
- Sentence 1: *"A prime number p is a natural number greater than 1, that is not a product of two smaller natural numbers."* — **DEFINITION** of the core term. Hands to next by leaving open the question "what, then, are the non-primes?" — the definition creates a binary that the next sentence fills.
- Sentence 2: *"A natural number greater than 1 that is not a prime number is called a composite number."* — **COMPLEMENT-DEFINITION** (negation of S1). Hands to next by completing the binary pair, so two categories now exist and need concrete instances.

**Paragraph 2**
- Sentence 1: *"For instance, number 7 is a prime number because the only ways of writing it as a product is through, 1×7 or 7×1."* — **EXAMPLE** of the first category + **UNPACK** (lists the factorisations). Hands to next by signposting a contrast ("However"), inviting the reader to test the boundary.
- Sentence 2: *"However 6 is a composite number because despite the fact that it can be written as 6×1; and 1×6, it can also be written as 3×2 and 2×3."* — **CONTRAST-EXAMPLE** + **MECHANISM** (extra factorisation reveals compositeness). Hands to next by proving the definition works in a non-trivial case, justifying the upcoming importance claim.

**Paragraph 3**
- Sentence 1: *"Prime numbers are central in number theory, because every natural number greater than 1 is either a prime itself or can be factorized as a product of primes that is unique up to their order."* — **CLAIM of importance + SPECIFICATION** (the "either… or…" structure specifies why). Hands to next by ending the unit on primes and motivating the next unit (modular arithmetic) as the natural next concept.

**Paragraph 4** (headlined "MODULAR ARITHMETIC")
- Sentence 1: *"Modular arithmetic is a system of arithmetic that works with integers and their remainders."* — **DEFINITION** of the new core term (mirrors the move used to open Paragraph 1). Hands to next by signalling that the definition needs unpacking.
- Sentence 2: *"In modular"* — **TRANSITION/UNPACK** (incomplete in the excerpt). Hands forward by opening the scope for the next clause.

## What This Section Does (content sequence)

This section is a **glossary-meets-motivation** block. The ordered moves are:
1. **Heading** — signals a new term is coming.
2. **Core definition** — gives the necessary condition the rest of the section depends on.
3. **Complement definition** — closes the binary so no case is left un-named.
4. **Positive worked example** — proves the definition has bite on a trivial case.
5. **Contrast worked example** — proves the definition actually distinguishes, not just labels.
6. **Importance claim + reason** — elevates the term from fact to topic-worthy.
7. **Heading + definition of next term** — bridges into the next concept using the same scaffolding.

The order matters because each move **sets up the next**: you cannot contrast examples until both categories are named (1→2→3); you cannot justify "central in number theory" until the reader has seen the definition discriminate (1→2→3→4→5); and you cannot motivate the new term until the old one has been elevated (6→7). A student replicating this should always go **define → mirror-define → example → counter-example → elevate**.

## Paragraph Skeletons (replicable templates)

**SKELETON A — the defining-paragraph pair**
`[Heading]. [Term A] is [category noun], [necessary condition clause]. [Term A]'s complement is called [Term B], defined as [negation of the necessary condition].`
- Slots: slot 1 = bold heading; slot 2 = the named concept; slot 3 = a noun-of-classification + a relative clause with one restriction; slot 4 = the binary opposite and a restated negation.
- Fill instructions: pick a mathematical (or any technical) term that splits a set into two named sub-sets; write the definition so that the second sub-set is forced by negating the first.
- Original fill: "PRIME NUMBERS. A prime number p is a natural number greater than 1, that is not a product of two smaller natural numbers. A natural number greater than 1 that is not a prime number is called a composite number."
- Demo fill (different idea): "EVEN NUMBERS. An even integer n is an integer expressible as 2k for some integer k. An integer that cannot be so expressed is called an odd integer."

**SKELETON B — the worked-example paragraph**
`For instance, [positive case] is [category A] because the only [test] is [trivial list]. However [counter case] is [category B] because despite the fact that it can be written as [trivial list], it can also be written as [non-trivial list].`
- Slots: slot 1 = a positive instance; slot 2 = the category it falls into; slot 3 = the diagnostic test; slot 4 = the list of trivial options; slot 5 = a contrasting instance; slot 6 = the opposite category; slot 7 = the same trivial list (parallelism); slot 8 = the extra list that breaks the test.
- Fill instructions: choose a property; pick one element that barely satisfies it (only trivial representations) and one element that superficially satisfies but has a hidden extra representation.
- Original fill: "For instance, number 7 is a prime number because the only ways of writing it as a product is through 1×7 or 7×1. However 6 is a composite number because despite the fact that it can be written as 6×1 and 1×6, it can also be written as 3×2 and 2×3."
- Demo fill: "For instance, 9 is a perfect square because the only integer whose square equals 9 is 3 (and −3). However 12 is not a perfect square because despite the fact that √12 ≈ 3.46, no integer squared equals 12; its nearest square factors are 4×3 and 2×2×3."

**SKELETON C — the importance claim**
`[Topic] is central in [field], because [general claim that reduces every member of the domain to [topic].`
- Slots: slot 1 = the term just defined; slot 2 = the broader discipline; slot 3 = a biconditional-style statement using "either… or…" that covers the whole domain.
- Fill instructions: state why the term deserves attention by showing that nothing in the field escapes it — every element is either an instance or built from instances.
- Original fill: "Prime numbers are central in number theory, because every natural number greater than 1 is either a prime itself or can be factorized as a product of primes that is unique up to their order."
- Demo fill: "Convex functions are central in optimisation, because every continuous function on a closed interval is either convex on some sub-interval or can be bounded above by the supremum of a family of convex functions via the convex envelope construction."

## Express-Idea Vocabulary

**Sequencing**
- "For instance" — opens *"For instance, number 7 is a prime number…"* (signals a worked illustration follows).

**Cause / consequence**
- "because" — appears twice: *"because the only ways of writing it…"* and *"because every natural number greater than 1…"* (ties each claim to its mechanism or warrant).

**Contrast / concession**
- "However" — opens *"However 6 is a composite number…"* (forces the reader to re-test the definition).
- "despite the fact that" — inside *"despite the fact that it can be written as 6×1"* (admits the surface similarity before breaking it).

**Specification**
- "either… or…" — *"either a prime itself or can be factorized as a product of primes…"* (closes the gap in the domain so the claim is total).

**Explanation verbs / definitional glue**
- "is" — *"A prime number p is a natural number…"*
- "is called" — *"is called a composite number"* (mirrors the definitional register).
- "can be factorized as" — *"can be factorized as a product of primes"* (turns a static definition into a constructive process).

## How to Explain an Idea (replication steps)

This section relies on the **definition → mirror-definition → positive example → contrasting example → importance-with-reason** pattern.

Step 1 — **Define the term in one relative clause.** Restrict it to the smallest necessary condition (e.g. *"not a product of two smaller natural numbers"*). Do not yet mention the opposite category.
Step 2 — **State the complement.** Negate the defining condition and name the resulting category (e.g. *"composite number"*). The reader now sees a binary.
Step 3 — **Give a trivial positive example.** Pick a number/object that satisfies the definition only by the obvious route (e.g. 7 with 1×7). This proves the definition can be met.
Step 4 — **Give a contrasting example with explicit mechanism.** Pick a number/object that looks like it could belong to the first category but fails because of a hidden alternative (e.g. 6, which also has 3×2). Use *"However"* + *"despite the fact that"* to mark the contrast.
Step 5 — **Elevate with a universal claim.** State that the concept is central because *every* member of the domain is either an instance or built from instances (use *"either… or…"*). This converts a glossary entry into a topic-worthy concept and naturally hands off to the next definition.
