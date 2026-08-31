# Idea Flow Notes: biology_7_may2021_f2EKQVzK41czTZ1f — 30 seconds by hand.

## Paragraph Flow (move by move)

**Paragraph 1** — (Treatment 3, one sentence, one move)
- Move 1: **procedure with instrument stated**, "using a pipette 0.5 ml of the microalgae concentrated extract" → names tool, then volume, then source. Hands the reader to the next clause by **action sequence** (dissolving must follow measuring).
- Move 2: **dissolving step**, "C. zofingiensis was dissolved in an erlenmeyer flask containing 100 ml" → completes the preparation logic set up by Move 1: the volume that was measured has to go somewhere, and that somewhere is the 100 ml flask. Hands to Move 3 by **time-bound action** (once dissolved, stirring is the next manual step).
- Move 3: **duration/finish**, "then stirred for 30 seconds by hand" → closes the paragraph with a definite endpoint. No continuation because a new paragraph introduces a new dilution.

**Paragraph 2** — (Treatment 4, one sentence, three moves)
- Move 1: **procedure with instrument**, "using a 50 ml graduated cylinder 20 ml of the 0.5% solution (treatment 3) were taken" → retrieves the product of the previous paragraph, which is why the parenthetical reference is mandatory. Hands forward by **cause**: the previous concentration must be diluted, so the next move has to specify the new volume.
- Move 2: **new flask volume**, "poured into an erlenmeyer flask containing 80 ml of water" → completes the dilution setup. Hands forward by **time**: dilution is finished only when mixing/storing is recorded.
- Move 3: **duration + result-of-dilution**, "the solution was then stored for 30 seconds by hand resulting in a concentration 0.1%" → states both time and the math outcome (20 in 100 → 0.1%). Closes paragraph; next paragraph starts a new dilution cycle.

**Paragraph 3** — (Treatment 5 + closing notes, two sentences, four moves)
- Move 1: **procedure with new instrument**, "using a 10 ml syringe, 10 ml of the 0.1% solution were taken" → forces a tool change (syringe, not cylinder) and signals that volume changes with concentration. Hands forward by **specification**: new volume needs new flask volume.
- Move 2: **new flask volume + concentration outcome**, "poured into an erlenmeyer flask containing 90 ml of water, the solution was then stored for 30 seconds by hand resulting in a concentration 0.01%" → delivers the final diluted value (10 in 100 → 0.01%). Hands forward by **consequence**: serial dilutions always raise the error question.
- Move 3: **reason-for-volume (justification)**, "An excess amount of the treatments were prepared in order to avoid errors" → explains *why* the volumes described were generous. The "in order to" makes it explicitly causal.
- Move 4: **repeat-for-reliability**, "Preparation of treatments was repeated for each course of treatments" → closes the section by transferring the reader out of single runs into replication logic.

## What This Section Does (content sequence)

This is a **serial-dilution procedure block**. The ordered content moves are:

1. **Highest-concentration stock** (Treatment 3): instrument + measured volume of raw extract + flask solvent + fixed mixing time.
2. **First dilution** (Treatment 4): instrument + volume taken *from the previous treatment* + new flask volume + new concentration.
3. **Second dilution** (Treatment 5): same pattern, each variable shrinking with concentration.
4. **Justification of volume excess** (causal explanation of why over-preparing).
5. **Replication statement** (closes the procedure by noting repetition across trials).

**Why this order works:** the reader cannot compute a dilution without knowing the previous concentration, so the chain must run from concentrated → dilute, with each step back-referencing the prior treatment in parentheses. The justification and replication notes are deliberately *last* — placing them earlier would interrupt the dilution arithmetic and force the reader to mentally re-thread the chain.

## Paragraph Skeletons (replicable templates)

**Skeleton A — Dilution step paragraph**
SKELETON: "[Tool] [X] ml of the [previous concentration] solution (Treatment N) were taken and poured into an erlenmeyer flask containing [Y] ml of water, the solution was then stored for [T] by hand resulting in a concentration [Z]%."

1. **Slots:**
   - Tool: noun phrase ("a 50 ml graduated cylinder", "a 10 ml syringe").
   - X / previous concentration / Treatment reference: number + % + parenthetical.
   - Y (flask volume): number in ml.
   - T (mixing time): "30 seconds by hand" or comparable unit.
   - Z (final concentration): the computed %.
2. **How to fill with a different idea:** slot 1 = pick a lab tool whose precision matches the volume you're withdrawing; slot 2 = state the volume you're taking, name the solution by its *previous* % (not its source), and cite the prior treatment in parentheses so the reader can trace back; slot 3 = set flask volume so total = X + Y is the same across dilutions (here always 100 ml); slot 4 = keep mixing time constant; slot 5 = compute Z as (X / (X+Y)) × previous %.
3. **Original filled version:** "using a 50 ml graduated cylinder 20 ml of the 0.5% solution (treatment 3) were taken and poured into an erlenmeyer flask containing 80 ml of water, the solution was then stored for 30 seconds by hand resulting in a concentration 0.1%."
4. **Demonstration fill (different subject):** "using a 25 ml volumetric pipette 25 ml of the 2.0 M stock (Preparation 3) were transferred into a volumetric flask containing 75 ml of distilled water, the solution was then inverted for 30 seconds resulting in a concentration 0.5 M."

**Skeleton B — Stock/starting-solution paragraph**
SKELETON: "[Tool] [X] ml of the [raw material] was dissolved in an erlenmeyer flask containing [Y] ml of water then stirred for [T]."

1. **Slots:**
   - Tool + X ml: precise measuring instrument and volume of raw material.
   - Raw material: the pure extract/compound (with species/taxon if biological).
   - Y ml of water: solvent volume.
   - T: mixing duration in seconds/minutes.
2. **How to fill:** slot 1 = choose the smallest-volume instrument that can still accurately deliver your raw mass; slot 2 = name the raw material specifically (species, compound, powder); slot 3 = pick Y so X + Y = a round total that simplifies later dilutions; slot 4 = state mixing time in the same units used in every later dilution so the reader expects consistency.
3. **Original filled version:** "using a pipette 0.5 ml of the microalgae concentrated extract C. zofingiensis was dissolved in an erlenmeyer flask containing 100 ml of water then stirred for 30 seconds by hand."
4. **Demonstration fill (different subject):** "using a micropipette 1.0 ml of the saffron concentrated extract Crocus sativus was dissolved in a beaker containing 99 ml of ethanol then agitated for 30 seconds by hand."

**Skeleton C — Closing justification + replication**
SKELETON: "An excess amount of the treatments were prepared in order to [avoid X]; Preparation of treatments was repeated for each [trial/course] of treatments."

1. **Slots:**
   - "in order to" clause: a methodological risk you are pre-empting (errors, evaporation, spillage, sampling shortfall).
   - "each course": the unit of repetition — trials, days, groups, replicates.
2. **How to fill:** slot 1 = state the *specific* failure mode you suspect (pipetting loss, evaporation, insufficient volume for sub-sampling); slot 2 = name the grouping variable the writer is replicating over (time, group, condition).
3. **Original filled version:** "An excess amount of the treatments were prepared in order to avoid errors; Preparation of treatments was repeated for each course of treatments."
4. **Demonstration fill (different subject):** "An excess volume of each concentration was prepared in order to compensate for pipetting loss; Preparation of concentrations was repeated for each experimental run."

## Express-Idea Vocabulary

- **Sequencing / order of operations:** "then stirred for", "then stored for 30 seconds" — mark the temporal micro-steps inside each treatment.
- **Procedure-naming verbs:** "dissolved in", "poured into", "taken and poured" — state the action each tool performs.
- **Causal connectors:** "in order to avoid errors" — explicit purpose clause explaining *why* a methodological choice was made.
- **Result / outcome markers:** "resulting in a concentration 0.1%", "resulting in a concentration 0.01%" — convert arithmetic into a named concentration.
- **Specification / referent-back:** "(treatment 3)", "the 0.5% solution" — tie the current step to the prior step's output rather than to the original raw material.
- **Replication markers:** "repeated for each course of treatments" — flag that the chain above is run more than once.

## How to Explain an Idea (replication steps)

This section uses a **chain-of-conversions pattern with back-references**: each paragraph takes the *output* of the previous paragraph, applies one arithmetic transformation (here, a 1:4 dilution), and states the new value. The reader is never asked to compute — the answer is given — but every step depends on the prior step's stated value.

To replicate with a NEW idea:

1. **State the stock first.** Name the raw material, the tool, and the volume drawn; specify the receiving volume so the *starting* concentration is unambiguous.
2. **Begin each subsequent paragraph with a back-reference.** Open with "the [previous %] solution (Treatment N)" so the reader's mental calculation has both inputs immediately.
3. **State tool, volume taken, and receiving volume in that order** within the same clause, so the arithmetic reads left-to-right (taken / total).
4. **Lock the total volume constant** across dilutions (here 100 ml every time) so the reader only has to track the numerator.
5. **Close the clause with the new concentration** using "resulting in a concentration [X]%" — name the value, do not show the working.
6. **Keep the mixing time identical** across paragraphs ("30 seconds by hand") so the only variable is concentration.
7. **After the chain ends, justify methodological excess** ("in order to avoid errors") and then **declare replication** ("repeated for each course of treatments") — these two moves belong at the *end* because they retroactively apply to every paragraph above them.
