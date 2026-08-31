# Idea Flow Notes: physics_6_may2020_lP9oEIfrx2GJWXJw — The energy comes both from the potential energy of the bob at initial

## Paragraph Flow (move by move)

**Paragraph 1** (assumption handling)
1. *Move:* **Continuation/specification** (fragment tail) — "release, as well as torsion in the string." → *Hands reader to next by:* completing the catalogue of residual effects before pivoting to consequences.
2. *Move:* **Consequence claim** — "The portion of the effect due to the potential energy would affect the validity of equation (6), and hence is minimized." → *Hands reader to next by:* setting up a residual that still needs disposing of.
3. *Move:* **Concession + verdict** — "Minimal rotation still exists, but this is considered negligible." → *Hands reader to next by:* closing the assumption block, so the next paragraph can move to a different assumption.

**Paragraph 2** (assumption with epistemic caveat)
1. *Move:* **Claim** — "Exponential decay is the trend followed by the energy, and hence amplitude of the pendulum." → *Hands reader to next by:* announcing an assumption that immediately needs justifying.
2. *Move:* **Contrast/concession** — "While theory does support this, it is impossible to prove that this is the case by experiment." → *Hands reader to next by:* introducing an epistemic limit that demands a procedural workaround.
3. *Move:* **Implication of the caveat** — "It can only be demonstrated with some uncertainty – as a consequence, this is an important assumption when linearization is being performed." → *Hands reader to next by:* locating the assumption inside a procedure, which the next block (Experimental Design) will operationalise.

**Paragraph 3** (header) — *Move:* **Section transition marker** — "a. Experimental Design:" → *Hands reader to next by:* signalling a complete change in register from justification to apparatus.

**Paragraph 4** (apparatus lead-in)
1. *Move:* **Setup statement** — "A simple pendulum was constructed as depicted in the figures below:" → *Hands reader to next by:* deferring detail to the figures, so captions must follow.

**Paragraph 5** (caption 1) — *Move:* **Labelling/specification** — "Fig. 1 – A side view of the apparatus" → *Hands reader to next by:* completing the apparatus documentation before another view is supplied.

**Paragraph 6** (caption 2)
1. *Move:* **Specification of figure content** — "Fig. 2 – An image depicting the vertically calibrated bob (against the photogate)." → *Hands reader to next by:* introducing a feature that then needs explaining.
2. *Move:* **Procedural note** — "It was horizontally shifted for conducting oscillations." → *Hands reader to next by:* connecting the set-up to the procedure, priming the reader for measured values.

**Paragraph 7** (measured values) — *Move:* **Data presentation + instrument provenance** — "Experimental Values: l = 0.739m ± 0.0005m / d = 0.0248m ± 0.00005m (measured using Vernier Caliper)" → *Hands reader to next by:* giving the numerical inputs the rest of the design will rely on.

## What This Section Does (content sequence)

The section executes this ordered sequence:

1. **Dispose of a residual assumption** by stating which effect dominates, why it would invalidate equation (6), and how it is minimised — sets a precedent of justifying every modelling choice.
2. **Quantify what survives** the disposal ("Minimal rotation still exists, but this is considered negligible") — pre-empts the reader's doubt about the cleanliness of the setup.
3. **Introduce the next assumption** ("exponential decay… of the energy, and hence amplitude") and immediately **flag the epistemic limit** (theory supports it, but experiment cannot prove it) — teaches the reader that the experiment relies on assumption, not proof.
4. **Localise the assumption inside a procedure** ("important assumption when linearization is being performed") — converts the abstract caveat into a concrete operation step.
5. **Transition to design** via a labelled header — marks a clean break from justification into construction.
6. **Announce the apparatus** in one sentence, pointing to figures — lets images do descriptive heavy lifting.
7. **Caption the figures** with both content (side view, calibration) and a procedural micro-note (the bob was shifted) — fuses documentation with method.
8. **List measured values with uncertainties and the instrument used** — supplies the inputs the reader will need to evaluate everything downstream.

**Why this order works:** justification before construction establishes credibility for the apparatus; the epistemic caveat explicitly grants that the experiment will *use* (not prove) the assumption, so when the apparatus section appears the reader already knows what to look for. Apparatus description → figures → values follows the natural reading order: what it is → what it looks like → what numbers it produced.

## Paragraph Skeletons (replicable templates)

**Skeleton A — "Dispose of an unwanted effect"**
SKELETON: "[residual effect], as well as [second residual]. The portion of the effect due to [cause] would affect the validity of [equation/ref], and hence is minimized. [Trace amount] still exists, but this is considered negligible."

1. *Slots:* (i) catalogue of residual effects — noun phrases; (ii) cause that threatens validity — noun phrase; (iii) reference target — equation number or named relation; (iv) trace residue — noun phrase; (v) verdict on residue — adjective or qualifier.
2. *Fill instructions:* Slot 1: pick two named physical effects left over from a previous step; slot 2: identify which one is theoretically large enough to bias your model; slot 3: point at a specific equation you derived earlier; slot 4: name the bit that you can't actually remove; slot 5: judge it negligible by argument (small quantity, short timescale, etc.).
3. *Original filled version:* "release, as well as torsion in the string. The portion of the effect due to the potential energy would affect the validity of equation (6), and hence is minimized. Minimal rotation still exists, but this is considered negligible."
4. *Demonstration fill (different idea):* "thermal expansion of the rod, as well as friction at the pivot. The portion of the effect due to conduction through the clamp would affect the validity of equation (3), and hence is minimized. A small residual heat flux still exists, but this is considered negligible over the 30 s interval."

---

**Skeleton B — "Assumption with epistemic caveat, then procedural implication"**
SKELETON: "[Trend] is the trend followed by [quantity A], and hence [quantity B]. While theory does support this, it is impossible to prove that this is the case by experiment. It can only be demonstrated with some uncertainty – as a consequence, this is an important assumption when [operation] is being performed."

1. *Slots:* (i) named mathematical trend — noun phrase; (ii) directly-observed quantity — noun phrase; (iii) derived/dependent quantity — noun phrase; (iv) epistemic limit clause — concessive clause; (v) operation the assumption licences — gerund phrase.
2. *Fill instructions:* Slot 1: name a clean mathematical behaviour (linear, exponential, logarithmic); slot 2: pick the measured signal; slot 3: pick the quantity you extract from that signal; slot 4: write a concession that names the gap between theory and finite data; slot 5: name the data-processing step (linearisation, differentiation, integration, fitting) that the assumption makes tractable.
3. *Original filled version:* "Exponential decay is the trend followed by the energy, and hence amplitude of the pendulum. While theory does support this, it is impossible to prove that this is the case by experiment. It can only be demonstrated with some uncertainty – as a consequence, this is an important assumption when linearization is being performed."
4. *Demonstration fill (different idea):* "A linear relationship is the trend followed by the voltage drop, and hence the current through the cell. While theory does support this, it is impossible to prove that this is the case by experiment. It can only be demonstrated with some uncertainty – as a consequence, this is an important assumption when the gradient is being extracted."

---

**Skeleton C — "Apparatus lead-in with figure delegation"**
SKELETON: "A simple [apparatus] was constructed as depicted in the figures below:"

1. *Slots:* (i) apparatus type — noun phrase.
2. *Fill instructions:* State in one clause that the apparatus exists, in the simplest possible terms, then immediately offload detail onto figures by pointing at them.
3. *Original filled version:* "A simple pendulum was constructed as depicted in the figures below:"
4. *Demonstration fill (different idea):* "A simple RC discharge circuit was constructed as depicted in the figures below:"

---

**Skeleton D — "Caption that fuses description with procedure"**
SKELETON: "Fig. N – [brief description of figure]. [One-line procedural note about how the setup was used]."

1. *Slots:* (i) figure description — noun phrase; (ii) procedural micro-note — past-tense clause.
2. *Fill instructions:* Slot 1: describe what the reader will literally see (viewpoint, key component); slot 2: state one thing that was done to the apparatus during the run (position, scale, offset).
3. *Original filled version:* "Fig. 2 – An image depicting the vertically calibrated bob (against the photogate). It was horizontally shifted for conducting oscillations."
4. *Demonstration fill (different idea):* "Fig. 4 – A close-up of the resistor mounted on the breadboard. It was momentarily short-circuited to discharge the capacitor before each trial."

---

**Skeleton E — "Measurement with uncertainty and instrument"**
SKELETON: "[Symbol] = [value] ± [uncertainty] (measured using [Instrument])"

1. *Slots:* (i) symbol — single letter or short label; (ii) numerical value with unit; (iii) absolute uncertainty with unit; (iv) instrument — proper noun.
2. *Fill instructions:* Slot 1: match the variable used in your equations; slot 2: give a value to the precision of the instrument; slot 3: state the instrument's stated resolution (do not invent precision); slot 4: name the device verbatim ("Vernier Caliper", "digital multimeter", "metre rule").
3. *Original filled version:* "l = 0.739m ± 0.0005m / d = 0.0248m ± 0.00005m (measured using Vernier Caliper)"
4. *Demonstration fill (different idea):* "R = 9.97 kΩ ± 0.01 kΩ (measured using digital multimeter) / C = 220 µF ± 2 µF (measured using LCR meter)"

## Express-Idea Vocabulary

- **Sequencing / handover:** *"While theory does support this"* — concedes, then escalates; *"It can only be demonstrated with some uncertainty"* — narrows scope before procedure.
- **Cause / consequence:** *"and hence is minimized"* — links threat to remedy; *"as a consequence, this is an important assumption when linearization is being performed"* — turns caveat into constraint.
- **Contrast / concession:** *"but this is considered negligible"* — concedes residue, dismisses it; *"While theory does support this, it is impossible to prove"* — paired concession/refusal.
- **Specification:** *"The portion of the effect due to the potential energy"* — isolates the relevant sub-effect.
- **Evidence handling:** *"it is impossible to prove that this is the case by experiment"* — names the evidentiary gap; *"It can only be demonstrated with some uncertainty"* — re-frames experiment as illustrative, not conclusive.
- **Explanation verbs:** *"would affect the validity"* (threat-verb), *"is minimized"* (procedural verb), *"is considered negligible"* (judgement verb), *"is the trend followed by"* (pattern-naming verb), *"as depicted in the figures"* (delegation verb), *"measured using"* (provenance verb).

## How to Explain an Idea (replication steps)

The dominant pattern is **"Justify-then-localise"**: you defend a modelling choice by tracing it from effect → equation-threat → mitigation, then move on to flag an epistemic limit and *anchor it to a specific procedure*. Applied to apparatus, the same author shifts to a **"Lead-in → figure delegation → caption-with-procedure → value-with-instrument"** micro-pattern.

Steps to replicate on a NEW idea:

1. **Name the unwanted effect** in catalogue form ("X, as well as Y") so the reader knows exactly what you are trying to dispose of.
2. **Trace the threat to an equation** you have previously derived ("would affect the validity of equation (n)"), making the link explicit rather than implied.
3. **State the mitigation** with a cause-verb ("and hence is minimized") so the response to the threat is visible.
4. **Concede the residue** and judge it ("still exists, but this is considered negligible") — never claim total elimination.
5. **Open the next assumption** by stating it as a chain ("Trend → followed by A → and hence B") to show how one quantity inherits behaviour from another.
6. **Insert an epistemic caveat** ("While theory does support this, it is impossible to prove… by experiment") to mark what the experiment *cannot* deliver.
7. **Re-cast the caveat as a procedural licence** ("as a consequence, this is an important assumption when [operation] is being performed") so the assumption is tied to a concrete data-processing step, not floating.
8. **Pivot to design** with a labelled header so the reader registers a change in register.
9. **Announce the apparatus in one clause**, delegating description to figures ("as depicted in the figures below").
10. **In each caption, mix description with procedure** — one image, one sentence of what was done to it.
11. **Close with measured values** formatted as symbol = value ± uncertainty, with the instrument named in parentheses — never drop the instrument.
