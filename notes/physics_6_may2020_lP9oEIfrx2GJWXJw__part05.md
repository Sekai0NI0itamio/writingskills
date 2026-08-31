# Idea Flow Notes: physics_6_may2020_lP9oEIfrx2GJWXJw — to be valid, as a consequence of fluid flow becoming increasingly

## Paragraph Flow (move by move)

**Paragraph 1 — Turbulence concession**
- S1 *concession + flag for verification:* "turbulent – citation needed" → hands off by raising an unverified claim that demands a consequence, so the next sentence names what is at stake.
- S2 *consequence (cause→effect):* "Hence, this impacts the validity of the exponential relationship" → hands off because a consequence claim needs evidence, so the next sentence points to where it lives.
- S3 *evidence pointer:* "Data supporting this can be found in the appendix" → hands off to the reader (externally) by closing the validity loop with a referral.

**Paragraph 2 — Amplitude selection (one complex sentence, four moves)**
- Clause 1 *decision stated:* "This was selected to be a small amplitude - 5°" → hands off because a chosen value requires justification, signalled by "for the reason that."
- Clause 2 *first reason (cause→outcome):* "this ensures a low velocity" → hands off by tacking on a second, parallel reason with "as well as."
- Clause 3 *second reason (problem to avoid):* "the difficulty faced in ensuring strictly 2-dimensional motion at higher amplitudes" → hands off because that difficulty needs to be unpacked mechanically, signalled by the dash.
- Clause 4 *mechanism (cause→consequence) unpacking the difficulty:* "as decay occurred, small lateral displacements caused significant circular motion" → hands off by completing the justification, leaving the next paragraph (a new design variable) free to begin.

**Paragraph 3 — Shape of bob**
- S1 *consequence + contrast example:* "This impacts the drag force experienced by the bob" then "a more aerodynamic bob would experience lesser" → hands off because the impact has been named but the chosen counter-measure has not yet been stated.
- S2 *decision with scientific reason:* "A spherical bob was chosen to maximize the applicability of Stokes' Law" → hands off to the next variable by closing the justification loop.

**Paragraph 4 — Length of string (single sentence, two-step chain)**
- S1 *causal chain (variable → intermediate → final quantity):* "due to its effects on the angular frequency, which in turn impacts the calculated value" → hands off to the next variable because the chain ends at a calculated quantity, leaving the next variable to start its own chain.

**Paragraph 5 — Mass of bob**
- S1 *causal link back to assumption:* "This is a consequence of the assumption that viscous drag" → hands off because the consequence is named but its counter-factual (what variation would do) is not yet specified.
- S2 *conditional/hypothetical (incomplete):* "Variation of the bob mass would mean that at heavier masses" → cuts off mid-clause, so the move opens a hypothetical without resolving it; the section simply ends.

## What This Section Does (content sequence)

This is a **design-justification** sequence. The moves are:
1. **Concede a limitation** that touches the mathematical model (turbulence → exponential fit), so the reader knows the validity ceiling before justifications begin.
2. **Justify the headline experimental choice** (amplitude = 5°) with a dual reason: one positive outcome, one problem-avoided, the second then mechanically unpacked so the reader sees *why* the problem is real.
3. **List subsidiary variables one by one**, each in the same micro-pattern: (a) what physical quantity the variable governs, (b) the choice made, (c) the scientific law or downstream quantity that justifies the choice.
4. **Order variables by decreasing causal proximity** to the final calculated quantity: drag (acts on the bob directly) → angular frequency (governs period) → mass (acts through the drag assumption).
   The order matters because each later variable cites a consequence set up by an earlier assumption (mass variation is meaningful *because* viscous drag is dominant).

## Paragraph Skeletons (replicable templates)

**SKELETON A — Limitation concession with consequence and evidence pointer**
`"[Term] – citation needed. Hence, this impacts the validity of [the mathematical relationship]. Data supporting this can be found in [appendix/figure]."`

1. *Slots:* (i) a term whose status is uncertain (noun phrase), (ii) the derived relationship whose validity is threatened (noun phrase), (iii) a location for the supporting evidence (noun phrase).
2. *How to fill differently:* Slot 1 — pick a term from your own experiment that is hard to verify (e.g. "Laminar", "Steady-state", "Isothermal"). Slot 2 — name the equation or fit you derived (e.g. "linear heat-conduction relation"). Slot 3 — point to a specific labelled appendix.
3. *Original:* "turbulent – citation needed. Hence, this impacts the validity of the exponential relationship. Data supporting this can be found in the appendix."
4. *Demo fill:* "Laminar – citation needed. Hence, this impacts the validity of the linear Ohm's-law fit. Data supporting this can be found in Appendix C."

**SKELETON B — Headline choice with dual reason + mechanism**
`"This was selected to be [option] - [value] - for the reason that this ensures [positive outcome], as well as [difficulty faced] at [higher/extreme alternative] – as [process], [cause] caused [consequence]."`

1. *Slots:* (i) option (noun), (ii) numerical value, (iii) desired physical outcome, (iv) named difficulty, (v) extreme condition, (vi) physical process, (vii) small perturbation, (viii) unwanted outcome.
2. *How to fill differently:* Slot 1 — pick the headline parameter of your own experiment. Slot 2 — give the numeric value with units. Slot 3 — state what the small value buys you. Slot 4 — name the *specific* problem that appears at the large extreme. Slots 6–8 — unpack that problem with a cause→consequence mechanism (one temporal link, one causal verb).
3. *Original:* "This was selected to be a small amplitude - 5° - for the reason that this ensures a low velocity, as well as the difficulty faced in ensuring strictly 2-dimensional motion at higher amplitudes – as decay occurred, small lateral displacements caused significant circular motion."
4. *Demo fill:* "This was selected to be a low drive frequency - 50 Hz - for the reason that this ensures a small inductive reactance, as well as the difficulty faced in isolating the signal at higher frequencies – as the coil warmed, random thermal fluctuations caused significant noise spikes."

**SKELETON C — Variable impact → contrast example → choice for law applicability**
`"This impacts the [quantity] experienced by the [object] – for instance, [alternative] would experience [comparative]. A [chosen option] was chosen to maximize the applicability of [law/principle]."`

1. *Slots:* (i) physical quantity, (ii) experimental object, (iii) hypothetical alternative shape/material, (iv) comparative outcome (adjective), (v) chosen option, (vi) named scientific law.
2. *How to fill differently:* Slot 1 — identify which quantity the variable governs in your experiment. Slot 2 — name the moving part. Slot 3 — state a real alternative you rejected. Slot 4 — compare magnitudes ("lesser", "greater"). Slot 6 — name the textbook principle whose idealised geometry matches your choice.
3. *Original:* "This impacts the drag force experienced by the bob – for instance, a more aerodynamic bob would experience lesser. A spherical bob was chosen to maximize the applicability of Stokes' Law."
4. *Demo fill:* "This impacts the magnetic flux experienced by the rotor – for instance, a soft-iron rotor would experience greater. A copper-coil rotor was chosen to maximize the applicability of Faraday's Law."

**SKELETON D — Two-step causal chain to the calculated quantity**
`"Maintaining this is important due to its effects on [intermediate quantity], which in turn impacts the calculated value of [final quantity]."`

1. *Slots:* (i) intermediate physical quantity, (ii) final calculated quantity (often the report's key result).
2. *How to fill differently:* Slot 1 — pick the quantity that mediates between the variable and your final number. Slot 2 — name that final number using the variable letter from your own report.
3. *Original:* "Maintaining this is important due to its effects on the angular frequency, which in turn impacts the calculated value of 𝑥N."
4. *Demo fill:* "Maintaining this is important due to its effects on the magnetic field strength, which in turn impacts the calculated value of ℰ."

## Express-Idea Vocabulary

**Sequencing / move-opening:** "for the reason that" ("for the reason that this ensures"), "as well as" ("as well as the difficulty faced"), "for instance" ("for instance, a more aerodynamic bob").

**Cause / consequence:** "Hence, this impacts" ("Hence, this impacts the validity"), "due to its effects on" ("due to its effects on the angular frequency"), "which in turn impacts" ("which in turn impacts the calculated"), "This is a consequence of" ("This is a consequence of the assumption"), causal verb "caused" ("small lateral displacements caused significant").

**Contrast / concession:** "as well as" doubling as additive-concessive ("as well as the difficulty faced").

**Specification:** "for instance" marking the comparative case ("for instance, a more aerodynamic bob").

**Evidence handling:** "citation needed" ("turbulent – citation needed"), "Data supporting this can be found" ("Data supporting this can be found in the appendix"), impact-flag "This impacts" ("This impacts the drag force").

**Explanation verbs:** "impacts" (effect), "experience" (passive reception by object), "ensures" (guarantee of outcome), "chosen to maximize" (selection logic), "caused" (mechanical causation).

## How to Explain an Idea (replication steps)

The dominant pattern is **CONSTRAINT → PHYSICAL MECHANISM → JUSTIFICATION VIA LAW OR DOWNSTREAM QUANTITY**.

1. **Open with a concession or constraint** that names what you are *not* assuming (e.g. "turbulent – citation needed"). This sets the validity ceiling before justifications begin.
2. **State the headline choice and its value** in a single dash-bracketed noun phrase (e.g. "small amplitude - 5° -").
3. **Attach a positive reason** introduced by "for the reason that this ensures [outcome]".
4. **Attach a second, parallel reason** introduced by "as well as [difficulty] at [extreme]". The contrast ("as well as") signals that two independent justifications exist.
5. **Unpack the second reason mechanically** with a dash, then a temporal cue ("as [process]") and a causal verb ("caused"), producing a cause→consequence mini-chain.
6. **For each subsidiary variable**, restate the pattern in compressed form: name the variable → name the physical quantity it impacts → give a one-clause comparative ("[alternative] would experience [comparative]") → state the choice made → cite the scientific law it satisfies **or** the downstream calculated quantity it feeds (use "which in turn impacts the calculated value of").
7. **Where the variable depends on a prior assumption**, anchor it explicitly: "This is a consequence of the assumption that [X]". This shows the variable chain rather than treating variables as isolated facts.
8. **Close each variable on a reason**, never on a bare fact, so every bullet ends with a justification that the reader can verify.
