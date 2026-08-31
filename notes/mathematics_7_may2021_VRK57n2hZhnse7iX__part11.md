# Idea Flow Notes: mathematics_7_may2021_VRK57n2hZhnse7iX — 2.3.3     Proof

## Paragraph Flow (move by move)

**Paragraph 1** (transition + object reminder)

- **Sentence 1** — *sequencing transition:* "The above information can now be implemented." Hands to next sentence because the reader expects the writer to *show* what is now being implemented — so the next move must name the object the implementation acts on.
- **Sentence 2** — *directive / restatement cue:* "Consider the two expressions of S again:" Hands to the equation block that follows because the verb "consider" creates a slot the reader must fill with a stated object.
- **Equation block** — *evidence / prior construction restated:* "S = τ1 ◦ τ2 ◦ · · · ◦ τk = β1 ◦ β2 ◦ · · · ◦ βm" Hands to Paragraph 2 by giving the reader the two equivalent forms that the next computation will substitute into.

**Paragraph 2** (introduce new quantity + algebraic expansion)

- **Sentence 1** — *directive / new object cue:* "Consider the value of ɛ in terms of the two expressions of the transpositions:" Hands to the equation chain by naming ɛ and pre-announcing that the two S-expressions will be inserted into it.
- **Equation chain** — *mechanism / worked derivation:* "ɛ = S ◦ S⁻¹ = (τ1 ◦ τ2 ◦ · · · ◦ τk) ◦ (β1 ◦ β2 ◦ · · · ◦ βm)⁻¹ = (τ1 ◦ τ2 ◦ · · · ◦ τk) ◦ (βm ◦ βm⁻¹ ◦ · · · ◦ β1)" Hands to Paragraph 3 because the manipulation ends with an inverted product that visibly counts to k + m — a counting claim the next paragraph must verbalise.

**Paragraph 3** (count + invoke theorem + verdict)

- **Sentence 1** — *observation / counting unpack:* "ɛ is expressed as a composition of k + m transpositions." Hands to the next sentence because it gives the reader a quantity (k + m) and the next sentence must judge it.
- **Sentence 2** — *theoretical claim / consequence:* "ɛ can only be expressed as an even number of transpositions, which indicates that k + m ≡ 0 (mod 2)." Hands to the verdict because the reader has now been given a parity constraint that allows a conclusion to be drawn.
- **Sentence 3 (cut off)** — *verdict / proof-closure cue:* "This proves the" — hands off-section (the proof target being concluded is outside this excerpt).

---

## What This Section Does (content sequence)

A *proof* section of this type sequences moves in this order:

1. **Transition cue from prior work** — announce that what was set up is about to be used. (Sets up the reader's expectation that a deduction is now happening.)
2. **Restatement of the previously established object** — recall the two equivalent forms of the key quantity so the reader has them in mind. (Sets up substitution in step 4.)
3. **Naming of the new object to be analysed** — pick a quantity (here ɛ = S ∘ S⁻¹) defined from the established one. (Sets up the algebraic expansion.)
4. **Worked derivation / substitution** — expand the new object using the two equivalent forms, step by step. (Produces a count or feature the theorem can bite on.)
5. **Verbal unpacking of the algebraic result** — translate the final symbolic form into a counting/structural claim. (Bridges the algebra to the theorem.)
6. **Application of a known theorem to that claim** — invoke an already-proven fact (here: parity of transposition decompositions) to constrain the quantity. (Forces the conclusion.)
7. **Verdict cue** — close with a "this proves the…" link to whatever was to be shown. (Hands back to the statement being proved.)

The order matters because each move *manufactures the input* the next move consumes: restatement makes substitution possible; substitution produces the count; the count is what the theorem needs.

---

## Paragraph Skeletons (replicable templates)

### SKELETON A — "restate, then introduce a new object built from it"

> "[Transition cue]. Consider the [object] again: [display of two equivalent forms of the object]."

1. **What each slot holds:**
   - Slot 1: a past-tense / settled-time transition phrase (verb in present perfect + adverb), e.g. "The above information can now be implemented."
   - Slot 2: imperative verb "Consider" + "the [object] again:" — a directive that frames the next display as a recap.
   - Slot 3: a displayed equation asserting two symbolic forms equal to each other.
2. **How to fill with a different idea:**
   - Slot 1: pick a piece of work just done (a definition, a lemma, a calculation) and announce it is now usable. Use "can now be used / applied / implemented."
   - Slot 2: name the central object of the previous section and the word "again" — the reader must have met it before.
   - Slot 3: write an equation of the form *X = [form 1] = [form 2]* where the two forms will be substituted later.
3. **Original fill:** "The above information can now be implemented. Consider the two expressions of S again:" S = τ1 ∘ τ2 ∘ · · · ∘ τk = β1 ∘ β2 ∘ · · · ∘ βm.
4. **Demonstration fill (different idea):** "The lemma on prime factorisations can now be applied. Consider the two factorisations of n again: n = p1^a1 · p2^a2 · · · pk^ak = q1^b1 · q2^b2 · · · qm^bm."

### SKELETON B — "compute a derived object by substitution, then count"

> "Consider the value of [new object] in terms of [prior object]: [expansion line 1 = expansion line 2 = expansion line 3]. [new object] is expressed as a composition of [count] [units]."

1. **What each slot holds:**
   - Slot 1: imperative "Consider the value of … in terms of …" — a directive naming a *new* quantity derived from the old one.
   - Slot 2: a chain of equalities where the new object is rewritten by replacing the old one with each of its two forms in turn, and any inversion is expanded.
   - Slot 3: a verbal unpacking sentence in present tense ("is expressed as") that converts the last line of the chain into a *count* of units.
2. **How to fill with a different idea:**
   - Slot 1: define a derived object from the one restated (e.g. f(x) − f(y), the conjugate, a commutator, a difference of two forms).
   - Slot 2: write three equal signs: original form → substitution of form 1 → simplification (e.g. inversion reverses order).
   - Slot 3: name the structural units being counted and state their total.
3. **Original fill:** "Consider the value of ɛ in terms of the two expressions of the transpositions:" ɛ = S ∘ S⁻¹ = (τ1 ∘ τ2 ∘ · · · ∘ τk) ∘ (β1 ∘ β2 ∘ · · · ∘ βm)⁻¹ = (τ1 ∘ τ2 ∘ · · · ∘ τk) ∘ (βm ∘ βm⁻¹ ◦ · · · ◦ β1). "ɛ is expressed as a composition of k + m transpositions."
4. **Demonstration fill (different idea):** "Consider the value of the commutator [g, h] in terms of the two expressions of g:" [g, h] = ghg⁻¹h⁻¹ = (g₁ g₂ · · · gₖ) h (g₁ g₂ · · · gₖ)⁻¹ h⁻¹ = (g₁ g₂ · · · gₖ) h (gₖ⁻¹ · · · g₂⁻¹ g₁⁻¹) h⁻¹. "[g, h] is expressed as a product of 2k + 2 of the original generators."

### SKELETON C — "invoke a parity/structural theorem to land the proof"

> "[object] can only be expressed as [structural constraint on [count]], which indicates that [count] [≡ or =] [value] (mod [base]). This proves the"

1. **What each slot holds:**
   - Slot 1: a *modal* sentence ("can only be") asserting an externally-proven constraint on how the object may be decomposed.
   - Slot 2: a "which indicates that" clause that converts the constraint on the structure into a modular arithmetic claim about the *count*.
   - Slot 3: a verdict cue "This proves the …" — unfinished, pointing forward to the statement being proved.
2. **How to fill with a different idea:**
   - Slot 1: state a known theorem about the *units* in slot 3 of Skeleton B (e.g. "every element of Aₙ requires an even number of transpositions").
   - Slot 2: match the theorem to the count using congruence language: "k + m ≡ 0 (mod 2)".
   - Slot 3: open with "This proves the" and leave the statement dangling — it belongs to the surrounding proof.
3. **Original fill:** "ɛ can only be expressed as an even number of transpositions, which indicates that k + m ≡ 0 (mod 2). This proves the"
4. **Demonstration fill (different idea):** "A reduced word in the Coxeter generators can only have even length when it equals the identity, which indicates that ℓ(w) ≡ 0 (mod 2). This proves the"

---

## Express-Idea Vocabulary

- **Sequencing / progression:** "can now be implemented" — marks the shift from setup to deduction: "The above information can now be implemented."
- **Directive / specification cue:** "Consider the [object] again:" — frames the next display as a recap: "Consider the two expressions of S again:"
- **Specification (re-expression in a chosen language):** "in terms of the two expressions" — tells the reader which tool will be used: "Consider the value of ɛ in terms of the two expressions of the transpositions."
- **Verbal unpacking of a symbol:** "is expressed as a composition of" — translates an algebraic form into a structural sentence: "ɛ is expressed as a composition of k + m transpositions."
- **Theoretical constraint / authority:** "can only be expressed as" — invokes an external theorem as a binding limit: "ɛ can only be expressed as an even number of transpositions."
- **Consequence / deduction connector:** "which indicates that" — turns the constraint into a numeric claim: "which indicates that k + m ≡ 0 (mod 2)."
- **Verdict / proof-closure verb:** "This proves the" — signals the conclusion lands here: "This proves the"

---

## How to Explain an Idea (replication steps)

The pattern this section uses is **definition → named object → algebraic substitution → structural count → external theorem → verdict**. To replicate it on a new idea:

1. **Open with a sequencing transition** that hands the reader from prior work into the deduction (e.g. "The lemma above can now be applied.").
2. **Restate the previously-built object in two equivalent symbolic forms**, side by side — this is the ammunition for substitution.
3. **Name a *new* quantity derived from the old one** using a short definition (here ɛ = S ∘ S⁻¹), framed with a directive ("Consider the value of … in terms of …").
4. **Expand the new quantity across several equal signs**, replacing the old quantity with each of its two forms in turn and simplifying any inversion/reversal step inline so the reader watches the algebra happen.
5. **Verbalise the final algebraic line** — convert the rewritten form into a count or structural description in plain English ("is expressed as a composition of k + m …").
6. **Apply an already-proven theorem** to that count, using the modal "can only be" so the reader sees the constraint is *external*, not freshly assumed.
7. **Translate the theorem's constraint into modular arithmetic** (or its equivalent) on the count, joined by "which indicates that".
8. **Close with the verdict cue "This proves the …"** — leave the statement being proved for the surrounding proof frame to complete.
