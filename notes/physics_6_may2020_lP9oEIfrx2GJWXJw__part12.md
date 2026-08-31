# Idea Flow Notes: physics_6_may2020_lP9oEIfrx2GJWXJw — statistical deviation among samples and those arising from constants rather than the

## Paragraph Flow (move by move)

**Paragraph 1 — Lead-in + bulleted enumeration**

- **Move 1 (context, completing prior sentence):** "direct uncertainty in the dependent variable." — picks up a half-finished thought so the reader knows the frame is *what direct uncertainty has missed*.
- **Move 2 (claim + transition into list):** "This signifies that there exist other sources of error, that may include:" — opens with the demonstrative "This" to bind back to Move 1 (cause→consequence link), then uses "may include:" as a list-launcher that hands the reader to the first bullet.

- **Bullet 1 — Lateral motion** (one sentence, two moves):
  - *Identification:* "Lateral motion of the bob" — names the source.
  - *Mechanism (energy-conservation argument):* "potential energy is converted to this kinetic energy too" — uses physics reasoning to justify why the source is *non-negligible*; the trailing "too" hands to Bullet 2 by signalling "another such overlooked conversion".

- **Bullet 2 — Rotational Energy** (one sentence, two moves):
  - *Identification:* "Rotational Energy" — names the source.
  - *Magnitude verdict:* "this might be more significant than assumed" — escalates the previous bullet's concern; the hedge "might" keeps it a judgement rather than a measurement, setting up Bullet 3 where the student moves from magnitude to validity.

- **Bullet 3 — Varying amplitudes** (one sentence, three moves):
  - *Identification:* "Varying amplitudes" — names the source.
  - *Initial verdict (justified by assumption):* "the effect this has might be correctly neglected as per the assumption" — accepts the source *can* be ignored *because of* the model assumption; the dash then pivots.
  - *Concession / counter-evaluation:* "however, this might have effects on the other sources of error, impacting the validity of the assumptions made" — "however" reverses direction; the nested consequence ("effects on the other sources… impacting the validity") chains cause→effect twice, handing the reader to Bullet 4 where a *specific* mechanism that breaks the model is named.

- **Bullet 4 — Drag due to string** (one sentence, three moves):
  - *Identification + model-incompatibility:* "Drag due to string – this is not necessarily compliant with the Stokes' law model" — names source then states it *breaks the chosen model* (reason for why it can't be folded into existing equations).
  - *Implication:* "and hence cannot be included in the exponential decay" — "hence" turns the model-incompatibility into a concrete mathematical consequence; this sets up the need for external support.
  - *Authority-backed magnitude claim:* "As shown by Mohazzabi (et al)2, this is a non-negligible effect." — "As shown by" introduces an external citation to settle the magnitude question the reader is now asking.

- **Bullet 5 — Dry, Structural Damping** (one sentence, two moves):
  - *Identification + mitigating condition:* "Dry, Structural Damping – these effects are less impactful since the string is tied below the rod" — "since" gives the geometric reason for the reduced impact.
  - *Mechanism of *added* damping (qualifier):* "due to heating effects in the string itself, there might be additional non-negligible damping produced or general distortion of the oscillations." — "due to" specifies the physical cause; "or" widens the consequence to cover two failure modes, closing the list on an open-ended note.

## What This Section Does (content sequence)

This is an **error-source enumeration inside an evaluation section**. The ordered moves are:

1. **Anchor to direct uncertainty** — establishes what the *known* error budget already contains (statistical + constant).
2. **Claim incompleteness** — asserts that direct uncertainty is not the whole story.
3. **Enumerate neglected sources one by one** — ordered roughly from "physically obvious energy losses" (lateral, rotational) → "assumption-validity threats" (amplitudes) → "model-breaking effects" (drag) → "secondary physical effects" (damping).
4. **For each source: name → mechanism → magnitude verdict** — three-part micro-structure repeated.
5. **Allow concession** — at least one item must reverse a previous "can be ignored" judgement so the evaluation reads honest.
6. **Cite an authority once** — for the source whose non-negligibility cannot be derived from first principles in this report.

The ordering matters: obvious physics first builds the reader's trust; the concession in the middle prevents the list reading like a checklist the student is steamrolling; the authority citation near the end shows epistemic humility on the one effect the student cannot argue from the experiment itself.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Energy-split" bullet**
> [Source] – [energy form A] is converted to this [energy form B] too

1. *Slot 1 — Source (noun phrase, italicisable).* Pick a physical quantity that the model collapses into one form but reality splits. *Slot 2 — Energy/quantity pair.* Two short noun phrases joined by "is converted to this … too"; the trailing "too" is essential — it links back to an already-discussed conversion.
2. *To reuse with a new idea:* choose a measurement where your model assumes one energy mode; find the second mode the apparatus actually wastes energy into; name both.
3. *Original:* "Lateral motion of the bob – potential energy is converted to this kinetic energy too"
4. *Demo (different subject — calorimetry):* "Conduction to the surroundings – thermal energy is converted to this kinetic energy of air molecules too"

---

**SKELETON B — "Magnitude vs assumption" bullet**
> [Source] – this might be [more / less] significant than assumed

1. *Slot 1 — Source (noun phrase).* *Slot 2 — Comparative magnitude judgement.* "might be" + comparative + "than assumed"; the comparative always pits the source against the *modeller's prior expectation*, not against zero.
2. *To reuse with a new idea:* take a source, decide whether reality makes it worse or milder than the simplifying assumption predicted, then write the comparative.
3. *Original:* "Rotational Energy – this might be more significant than assumed"
4. *Demo (different subject — projectile range):* "Crosswind drag – this might be more significant than assumed"

---

**SKELETON C — "Concession that loops back" bullet**
> [Source] – the effect this has might be correctly neglected as per the assumption – however, this might have effects on the other sources of error, impacting the validity of the assumptions made.

1. *Slot 1 — Source.* *Slot 2 — Initial permission-to-ignore (justified by referring to "the assumption").* *Slot 3 — Reversal introduced by "however".* *Slot 4 — Nested consequence* (effects on *other* sources → impacts validity of assumptions). The reversal must reach one level up — it must threaten a sibling item, not just itself.
2. *To reuse with a new idea:* pick a source you can defensibly ignore *under one assumption*; then find the second-order channel through which that source disturbs another assumption in your model.
3. *Original:* "Varying amplitudes – the effect this has might be correctly neglected as per the assumption – however, this might have effects on the other sources of error, impacting the validity of the assumptions made."
4. *Demo (different subject — resistor heating experiment):* "Ambient temperature drift – the effect this has might be correctly neglected as per the assumption of isothermal leads – however, this might have effects on the other sources of error, impacting the validity of the assumptions made."

---

**SKELETON D — "Model-breaking + authority" bullet**
> [Source] – this is not necessarily compliant with the [model name], and hence cannot be included in the [mathematical form]. As shown by [Author] (et al)[n], this is a non-negligible effect.

1. *Slot 1 — Source.* *Slot 2 — Model-incompatibility statement* ("not necessarily compliant with"). *Slot 3 — Mathematical consequence* ("hence cannot be included in the …"). *Slot 4 — Authority citation with "As shown by".* *Slot 5 — Magnitude verdict* ("non-negligible effect"). The "hence" must convert the *modelling* problem into a *mathematical* problem — that's what makes the citation necessary.
2. *To reuse with a new idea:* identify (a) the named model your report uses, (b) the source that violates one of its preconditions, (c) the equation you therefore can't put that source into, and (d) one external paper that quantified it.
3. *Original:* "Drag due to string – this is not necessarily compliant with the Stokes' law model, and hence cannot be included in the exponential decay. As shown by Mohazzabi (et al)2, this is a non-negligible effect."
4. *Demo (different subject — RC discharge):* "Electrode polarisation – this is not necessarily compliant with the ideal-capacitor model, and hence cannot be included in the simple exponential decay. As shown by Bard (et al)1, this is a non-negligible effect."

## Express-Idea Vocabulary

**Sequencing / list-launching**
- "that may include:" → "…there exist other sources of error, that may include:" — hands reader into a list.

**Cause / consequence**
- "is converted to this kinetic energy too" → "potential energy is converted to this kinetic energy too" — physical-cause connector.
- "and hence cannot be included" → "and hence cannot be included in the exponential decay" — logical consequence of a prior incompatibility.
- "due to" → "due to heating effects in the string itself" — specifies physical cause.

**Contrast / concession**
- "however" → "however, this might have effects on the other sources of error" — reverses a prior permission-to-ignore.
- "might be more significant than assumed" → "this might be more significant than assumed" — magnitude re-evaluation.

**Specification / qualification**
- "as per the assumption" → "the effect this has might be correctly neglected as per the assumption" — binds a claim to a named assumption.
- "not necessarily compliant with" → "this is not necessarily compliant with the Stokes' law model" — softens a model-breaking claim.

**Evidence handling**
- "As shown by [author] (et al)[n]" → "As shown by Mohazzbi (et al)2, this is a non-negligible effect." — external citation as magnitude arbiter.

**Explanation / mechanism verbs**
- "is converted to" → energy bookkeeping.
- "compliant with" → model-fit vocabulary; treats a physical law like a contract.
- "included in" → equation-placement vocabulary.

## How to Explain an Idea (replication steps)

The section uses the pattern **"claim of incompleteness → enumerated source-by-source audit, each with mechanism + magnitude verdict, with one concession and one authority citation."**

To replicate with a new idea:

1. **State what the existing error budget already covers** (one half-sentence that hooks to a prior calculation).
2. **Claim that this coverage is insufficient** — use "This signifies that there exist other …".
3. **Pick 4–5 overlooked sources**, ordered from most physically obvious to most model-breaking.
4. **For each source, write one short sentence** containing: (a) the source's name, (b) the mechanism by which it disturbs the measurement (energy split, model violation, or geometric mitigation), and (c) a magnitude verdict (more / less / non-negligible) with the *reason* embedded in the same clause ("since the string is tied below the rod", "as per the assumption").
5. **Insert exactly one concession** mid-list: a source you first say can be ignored, then reverse with "however" so the reversal threatens a sibling assumption, not itself.
6. **Cite one external authority** for the source whose non-negligibility you cannot derive from your own data — use "As shown by [Author] (et al)[n]" as the formula.
7. **Close on a source whose magnitude is uncertain** ("might be additional … produced") rather than a tidy summary — leaves the evaluation open-ended, signalling honest uncertainty.
