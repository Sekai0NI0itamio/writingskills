# Idea Flow Notes: physics_7_may2020_HrmahagW4GDrDzvJ — Volume                                                      Density

## Paragraph Flow (move by move)

**Paragraph 1** (formatting rationale)
1. *Specification of formatting convention + exception + cause*: "The values in Table 2 have been formatted to 3 significant figures and the uncertainties to 2 significant figures, with the exception of the mass—which has been formatted to 4 significant figures—because the balance featured higher precision."
   - Hand-off: the formatting question is closed, so the next sentence must now look at what the *values themselves* show → "We can see that the density values..."

**Paragraph 2** (internal comparison + reason)
1. *Observation claim + causal justification*: "We can see that the density values for the two balls are similar and this makes sense since they are made of the same material."
   - Hand-off: because the two experimental values agree internally, the next sentence tests them against the *external accepted value* → "These values are close to..."

**Paragraph 3** (external comparison to literature)
1. *Comparison + numerical range + source*: "These values are close to the accepted range for the density of steel: 7750–8050 kgm−3 (Wikipedia, 2019)."
   - Hand-off: "close" is qualitative; the next sentence must *quantify* how close → "Although the two values aren't exactly the same..."

**Paragraph 4** (concession + quantified verdict)
1. *Concession + numerical comparison + verdict label*: "Although the two values aren't exactly the same, the percentage difference is about 0.4%, which is negligible."
   - Hand-off: the *values* are settled as accurate; the next sentence shifts focus to the *uncertainties on those values* → "All of the percentage uncertainties are miniscule..."

**Paragraph 5** (uncertainty quality assessment + cause)
1. *Observation + mechanism (instrument quality)*: "All of the percentage uncertainties are miniscule, reflecting the high precision of the micrometre and the balance."
   - Hand-off: the *outcomes* of uncertainty propagation are judged; the next sentence must now expose the *method* that produced them → "The following uncertainty propagations were used..."

**Paragraph 6** (method statement)
1. *Transition + procedural setup for formulas*: "The following uncertainty propagations were used to calculate the uncertainties in the volumes and densities of the balls:"
   - Hand-off: the two propagation equations appear directly under this lead-in; logically, the formulas are the destination promised by "following."

## What This Section Does (content sequence)
1. **Formatting/significant-figure justification** — sets up that every number the reader sees is *deliberately* rounded, so later % comparisons are fair.
2. **Internal comparison (sample vs sample)** — checks that the two trials agree *with each other*, the cheapest first-pass validity test.
3. **External comparison (experiment vs accepted value)** — checks that the experiment agrees with *literature*, the second validity test.
4. **Quantified discrepancy + verdict** — converts "close" into a number, then stamps it "negligible" so the reader cannot dispute it.
5. **Uncertainty quality + instrumental cause** — defends the *size* of the error bars by attributing it to instrument precision.
6. **Method pointer to formulas** — retroactively justifies the error bars by showing how they were derived.

**Why this order:** each move answers the doubt the previous one raised. Formatting → "is the data honest?" → internal check → external check → "but how big is the gap?" → verdict → "and what about the uncertainties?" → method. A student replicating this on any measured physical constant gets a defensible validation arc.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Formatting rationale with exception:**
"The values in [dataset reference] have been formatted to [N] significant figures and the [second quantity] to [N], with the exception of [variable]—which has been formatted to [different N]—because [instrument/measurement reason]."

1. *Slots:* (i) dataset label, (ii) two parallel counts of significant figures, (iii) parenthetical exception introduced by an em-dash, (iv) `because`-clause naming the instrument feature.
2. *Filling instructions:* slot 1 — name the table the numbers came from; slot 2 — pick a standard sig-fig rule (e.g. 3 s.f.) and apply it to most columns; slot 3 — single out *one* variable whose instrument was more precise and give it a *higher* sig-fig count; slot 4 — name the actual instrument property ("higher precision", "digital readout", "±0.01 mm scale").
3. *Original fill:* "The values in Table 2 have been formatted to 3 significant figures and the uncertainties to 2 significant figures, with the exception of the mass—which has been formatted to 4 significant figures—because the balance featured higher precision."
4. *Demo fill (different topic — pendulum period experiment):* "The values in Table 4 have been formatted to 3 significant figures and the uncertainties to 1 significant figure, with the exception of the period—which has been formatted to 4 significant figures—because the photogate featured higher precision than the metre stick."

**SKELETON B — Internal agreement claim with shared-property reason:**
"We can see that the [measured quantity] values for the two [samples] are similar and this makes sense since they are [shared physical property]."

1. *Slots:* (i) observed quantity, (ii) two trial objects, (iii) shared material/property stated as a `since`-clause.
2. *Filling instructions:* slot 1 — pick the dependent variable you measured; slot 2 — refer to your two test items as "the two [objects]"; slot 3 — give the *single shared feature* that justifies why they should agree (same material, same temperature bath, same resistor, etc.).
3. *Original fill:* "We can see that the density values for the two balls are similar and this makes sense since they are made of the same material."
4. *Demo fill (specific heat experiment):* "We can see that the specific heat capacity values for the two copper blocks are similar and this makes sense since they are made of the same material."

**SKELETON C — Concession + quantified percentage + adjective verdict:**
"Although the two values aren't exactly the same, the percentage difference is about [X]%, which is [verdict adjective]."

1. *Slots:* (i) `Although` concession, (ii) numerical percentage to 1–2 sig figs, (iii) one-word evaluative adjective (`negligible`, `significant`, `considerable`).
2. *Filling instructions:* slot 1 — concede the residual gap; slot 2 — compute % difference and report it as "about X%"; slot 3 — choose adjective consistent with the number's size relative to the experiment's stated uncertainty.
3. *Original fill:* "Although the two values aren't exactly the same, the percentage difference is about 0.4%, which is negligible."
4. *Demo fill (refractive index):* "Although the two values aren't exactly the same, the percentage difference is about 2.1%, which is significant."

**SKELETON D — Uncertainty magnitude + causal mechanism:**
"All of the percentage uncertainties are [size adjective], reflecting the high precision of the [instrument 1] and the [instrument 2]."

1. *Slots:* (i) global size adjective for *all* percentage uncertainties, (ii) two specific instruments separated by "and the", (iii) the shared causal claim "high precision".
2. *Filling instructions:* slot 1 — pick one word describing magnitude (`miniscule`, `small`, `moderate`); slot 2 — name the two measuring devices; slot 3 — link size to instrument, not to skill, to keep it methodological.
3. *Original fill:* "All of the percentage uncertainties are miniscule, reflecting the high precision of the micrometre and the balance."
4. *Demo fill (SHM timing):* "All of the percentage uncertainties are small, reflecting the high precision of the stopwatch and the ruler."

## Express-Idea Vocabulary

- **Specification / exception:** "with the exception of the mass" — singles out one variable from a general rule.
- **Cause:** "because the balance featured higher precision" — justifies the exception just introduced.
- **Cause (informal):** "this makes sense since they are made of the same material" — links an observed similarity to a physical reason.
- **Comparison (external):** "These values are close to the accepted range" — benchmark against literature.
- **Evidence handling:** "7750–8050 kgm−3 (Wikipedia, 2019)" — bracketed source citation attached to the benchmark number.
- **Concession:** "Although the two values aren't exactly the same" — admits a gap before dismissing it.
- **Quantification + verdict:** "the percentage difference is about 0.4%, which is negligible" — number → one-word judgement.
- **Mechanism (verb):** "reflecting the high precision of the micrometre" — `-ing` participle naming cause.
- **Method pointer:** "The following uncertainty propagations were used to calculate" — announces formulas to come.

## How to Explain an Idea (replication steps)

This section uses an **internal-check → external-check → quantify → uncertainty-audit** pattern.

1. **Open with a data-honesty move.** State how the numbers in the table were rounded and *why* one column got a different precision (usually because one instrument was better). This pre-empts any "your data look dodgy" objection.
2. **Compare the trials to each other.** State that the two samples gave similar results and immediately supply the shared physical reason ("same material", "same temperature") that *makes* the similarity expected.
3. **Compare the trials to a literature value.** Quote an accepted range with a citation. Use "close to" — never "equal to".
4. **Quantify the residual gap and judge it.** Use `Although... percentage difference... which is [adjective]`. Pick the adjective by comparing the % to the % uncertainty.
5. **Audit the uncertainties themselves.** Comment on whether the percentage uncertainties are miniscule/small, and link that to the precision of the named instruments with `reflecting`.
6. **Point forward to the math.** End with a one-line "The following [equations] were used to calculate..." so the formulas that follow have explicit methodological signposting.
