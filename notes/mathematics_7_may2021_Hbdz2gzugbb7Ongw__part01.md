# Idea Flow Notes: mathematics_7_may2021_Hbdz2gzugbb7Ongw — A Behaviour of angles in double pendulums                                                                   ii

## Paragraph Flow (move by move)

The text is a single structural block (a contents listing) with eleven enumerated lines. I treat it as one paragraph and map each line as a move.

**Paragraph 1 (11 moves)**

**Move 1 — Baseline declaration.** Quote: *"Behaviour of standard double pendulum"*. Function: names the reference/origin case (no perturbation applied). Hands to next by *contrast — the very next lines introduce small deviations FROM this standard*, so the reader expects "what changes when X is tweaked?"

**Move 2 — First perturbation: initial angle 1.** Quote: *"Behaviour after 5% increase in θ10"*. Function: specifies a controlled ±5% variation of the first initial angle. Hands forward by *parallel construction* — the next move mirrors this exact phrasing for θ₂₀, training the reader that angles come as a paired set.

**Move 3 — Second perturbation: initial angle 2.** Quote: *"Behaviour after 5% increase in θ20"*. Function: completes the angle pair, isolating the role of the second rod's release position. Hands forward by *category shift* — angles are exhausted, so velocities must come next in the initial-condition group.

**Move 4 — Third perturbation: initial angular velocity 1.** Quote: *"Behaviour after small initial ω10"*. Function: shifts from positional to dynamical initial state, first rod. Hands forward by *pairing*, same logic as angles.

**Move 5 — Fourth perturbation: initial angular velocity 2.** Quote: *"Behaviour after small initial ω20"*. Function: pairs the velocity set. Hands forward by *transition to a new parameter class* — initial conditions are now fully explored, so the system parameters themselves (mass, length) become the variation axis.

**Move 6 — Fifth perturbation: mass 1.** Quote: *"Behaviour after 5% increase in m1"*. Function: introduces a structural (not initial-condition) parameter, again first index. Hands forward by *mirroring*.

**Move 7 — Sixth perturbation: mass 2.** Quote: *"Behaviour after 5% increase in m2"*. Function: closes the mass pair. Hands forward by *category shift* — only lengths remain among system parameters.

**Move 8 — Seventh perturbation: length 1.** Quote: *"Behaviour after 5% increase in l1"*. Function: first length variable. Hands forward by *mirroring*.

**Move 9 — Eighth perturbation: length 2.** Quote: *"Behaviour after 5% increase in l2"*. Function: closes the length pair. Hands forward by *exhaustion transition* — all systematic single-parameter perturbations are now catalogued, so the section pivots from "what changes" to "what simplifies".

**Move 10 — Approximation case 1.** Quote: *"Approximation to single pendulum: small angle"*. Function: introduces a limiting/idealising regime. Hands forward by *paired approximation* — the reader anticipates a companion limit.

**Move 11 — Approximation case 2.** Quote: *"Approximation to double pendulum: large angle"*. Function: second limiting regime, framed as a contrast to the small-angle limit. Closes the list by *closure of the parameter space* — no further entry is needed; the appendix structure is complete.

## What This Section Does (content sequence)

This is an **appendix contents/roadmap section**. Its ordered job sequence is:

1. **Establish the baseline** (unperturbed system) — sets the reference point against which every later change is measured.
2. **Vary initial angles in pairs** (θ₁₀, then θ₂₀) — tests sensitivity to release configuration.
3. **Vary initial angular velocities in pairs** (ω₁₀, then ω₂₀) — tests sensitivity to release dynamics.
4. **Vary structural parameters in pairs** — mass (m₁, m₂), then length (l₁, l₂).
5. **Move from variation to idealisation** — small-angle limit (collapses to single pendulum), then large-angle limit (other behavioural regime).

The order matters because: the baseline must come first or perturbations lose meaning → initial-condition perturbations are grouped together (positions then velocities) → structural perturbations come after → idealisations come last because they synthesise rather than probe. Another student replicating this on a different system (e.g. coupled oscillators, predator–prey model) would: name the default → perturb each controllable input systematically → end with limiting regimes.

## Paragraph Skeletons (replicable templates)

**SKELETON 1 — Single-line entry (variation case).**
`"[Behaviour noun] after [quantifier] [increase/decrease] in [parameter symbol]"`
- Slot 1: noun phrase naming what is observed ("Behaviour of", "Phase portrait of", "Oscillation of"). Grammatically: noun + preposition phrase.
- Slot 2: a numerical magnitude expressed as a percentage or ratio ("5% increase", "10% decrease", "small initial").
- Slot 3: parameter symbol with subscript indexing position in the system.
- **Fill instructions**: Pick one variable of your model; declare a precise numerical perturbation; keep the subscript consistent so paired entries can be written the same way.
- **Original filled**: *"Behaviour after 5% increase in m1"*.
- **Demonstration fill (different idea)**: *"Phase portrait after 10% decrease in α₁"* (predator–prey model).

**SKELETON 2 — Baseline entry.**
`"[Behaviour noun] of standard [system name]"`
- Slot 1: generic observation noun.
- Slot 2: canonical/control version of the system.
- **Fill instructions**: Name your system and explicitly mark the unperturbed version as the reference ("standard", "baseline", "default", "unperturbed").
- **Original filled**: *"Behaviour of standard double pendulum"*.
- **Demonstration fill**: *"Trajectory of baseline Lotka–Volterra system"*.

**SKELETON 3 — Approximation/limit entry.**
`"Approximation to [simplified system]: [regime condition]"`
- Slot 1: the simpler system this approximates.
- Slot 2: the condition under which the simplification holds.
- **Fill instructions**: Identify one limiting regime of your model where it reduces to a known simpler form, name the regime condition precisely.
- **Original filled**: *"Approximation to single pendulum: small angle"*.
- **Demonstration fill**: *"Approximation to linear oscillator: small amplitude"*.

## Express-Idea Vocabulary

This section is deliberately sparse in connectives — its logic is carried by **structural parallelism**, not conjunctions. The grouping vocabulary it relies on:

- **Sequencing / enumeration**: implicit via numbering (A.1, A.2 … A.11) and page dots. The sequence itself is the argument.
- **Specification / precision marker**: the colon in *"Approximation to single pendulum: small angle"* — narrows the previous label to a precise regime.
- **Variation indicator**: *"after 5% increase in"* — quantifies the deviation from the baseline named in Move 1.
- **Qualifier of magnitude**: *"small initial"* — marks a non-percentage perturbation (qualitative, not quantitative).
- **Indexing / pair-marker**: subscripts on symbols (θ10, θ20, ω10, ω20, m1, m2, l1, l2) — the changing subscript alone signals "the second member of the pair".
- **Contrast-as-pair-completion**: no explicit "whereas" — the contrast between paired entries is carried by *which subscript changes next*.

## How to Explain an Idea (replication steps)

The pattern this section uses is **systematic enumeration by single-variable perturbation from a baseline**, ending in **limiting-case idealisation**. To replicate with a new idea:

1. **Name the baseline case** as line one — the unmodified system, explicitly marked as the reference.
2. **List every variable of your model** that can be perturbed. Group them: first all initial-condition variables (one pair at a time), then all structural parameters (one pair at a time).
3. **For each variable, write one entry that perturbs it by a stated, consistent amount** (e.g. "5% increase") — keep the perturbation size uniform so comparisons remain valid.
4. **Within each group, pair the entries** by matching indices/subscripts so the reader sees you have not forgotten the second instance.
5. **End with one or two limiting/approximation entries**, phrased as "Approximation to [simpler system]: [regime]". These close the exploration by showing where the model simplifies.
6. **Number the entries sequentially (A.1, A.2 …)** and add a page reference — the numbering does the connective work that prose connectives would otherwise do.

The whole point of this pattern: the reader can scan the list and instantly see *what was varied, by how much, and what was held fixed* — logical coverage is communicated through structure rather than argument.
