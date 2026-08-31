# Idea Flow Notes: mathematics_7_may2017_TzoKIgKR386jeyuR — are no net birth rates and death rates, as well as immigration to and emigration from the

## Paragraph Flow (move by move)

**Item 1 (truncated — tail of sentence only):**
- S1 (incomplete statement): "are no net birth rates and death rates, as well as immigration to and emigration from the population." → **content move: specification (closing the demographic boundary).** → The reader is being told what is *excluded* from the model. The truncation is supplied by the reader's prior heading; the sentence hands the reader to Item 2 by *shifting domain* from demographics to post-infection status.

**Item 2 — "Immunity upon recovery":**
- S1 (title + claim): "A person is immune from the epidemic upon recovery." → **claim**: states the rule. Hands to S2 by *inviting restatement* ("upon recovery" begs "in other words…").
- S2 (restatement trigger): "In other words, if a person from the 𝐼 population has recovered, he or she would be put into the 𝑅 population group." → **definition/restatement + mechanism**: maps the rule onto the SIR notation. Hands to S3 by *consequence* ("put into R" begs "and so cannot…").
- S3 (consequence): "He or she would be immune to infection by the epidemic and thus unable to be classed as the 𝑆 population again." → **implication** via "thus". Closes the item; hands to Item 3 by *new domain* (immunity → probability).

**Item 3 — "Constant probability of infection":**
- S1 (title + claim): "There is a constant probability of infection, and the probability of infection of the epidemic would not change for people of different ages, genders, races etc." → **claim + specification**. The first clause asserts; the second clause enumerates *what does not vary*. Hands to Item 4 by *moving to a different exclusion* (probability vs. inheritance).

**Item 4 — "No inheritance of disease":**
- S1 (claim): "There is no inheritance of the epidemic, which also means that immunity of the disease is not inheritable as well." → **claim + secondary implication** ("which also means that"). One sentence does two jobs at once: denies genetic transmission AND denies inherited immunity. Hands to Item 5 by *new domain* (biology → mixing behaviour).

**Item 5 — "Homogenous mixing":**
- S1 (claim + definition): "There is homogenous mixing of the population, meaning that all members of the population have an equal number of interactions with each other over time." → **claim + unpacking** via "meaning that". The second clause is the *mechanism* (equal interactions). No hand-off sentence — this is the terminal item.

**Overall logic path across items:** Title (label) → Restatement in model language (where applicable) → Consequence/secondary implication → Close. Each item is a *closed unit*; the list is sequenced by *what aspect of reality is being stripped away* (demographics → recovery status → individual variation → genetics → contact structure).

---

## What This Section Does (content sequence)

This is an **assumptions/limitations list** for a mathematical model. The ordered moves are:

1. **Demographic closure assumption** — strip births, deaths, migration so the total population is fixed.
2. **Post-infection state assumption** — define what happens to recovered individuals (here: move to R, immune for life).
3. **Parameter uniformity assumption** — assert that infection probability does not vary across sub-populations.
4. **Non-biological-transmission assumption** — exclude hereditary routes.
5. **Contact-structure assumption** — assume uniform (well-mixed) contact rates.

**Why this order:**
- Move 1 sets the *container* (a fixed pool of people).
- Move 2 defines how individuals *change compartment* within that container.
- Move 3 simplifies the *rate parameter* governing transitions.
- Move 4 removes an *alternative pathway* into the S/I/R compartments.
- Move 5 simplifies the *network* over which transmission occurs.

The underlying logic is: **container first → compartment rules → transition rates → excluded pathways → contact topology.** A student replicating this on, say, a predator–prey model would list assumptions in the same causal order: closed ecosystem → reproduction rule → constant interaction rate → no migration of genes → uniform distribution of prey.

---

## Paragraph Skeletons (replicable templates)

### Skeleton A — "Restated claim + consequence" (used in Item 2)

> SKELETON: "[Label]. [Claim restating the rule in plain words]. In other words, [technical reformulation mapping the rule onto the model's variables]. [Consequence using 'thus' or equivalent], so [downstream implication that closes the assumption]."

1. **Slot 1 — Label:** A short noun phrase naming the assumption (e.g., "Immunity upon recovery"). Shape: 2–4 words, often "-ion/-ment/-ence" nominalisation.
2. **Slot 2 — Claim:** A sentence stating the rule in everyday terms. Shape: declarative, present tense, generic subject ("A person…", "An individual…").
3. **Slot 3 — Technical reformulation:** Begins with "In other words," and re-expresses the rule using model variables. Shape: conditional ("if X, then Y") referencing the model's compartments/symbols.
4. **Slot 4 — Consequence:** Begins with "thus" / "therefore" / "as a result." Shape: declarative stating what is *excluded* or *prevented* by the rule.

**Original fill:** "Immunity upon recovery. A person is immune from the epidemic upon recovery. In other words, if a person from the 𝐼 population has recovered, he or she would be put into the 𝑅 population group. He or she would be immune to infection by the epidemic and thus unable to be classed as the 𝑆 population again."

**Demonstration fill (different idea — predator–prey model):** "Carrying capacity reached. A prey population stops growing once the environment is saturated. In other words, if the prey count equals the carrying capacity 𝐾, the growth rate becomes zero. The population therefore remains fixed at 𝐾 and thus cannot exceed this ceiling."

---

### Skeleton B — "Single-sentence claim with embedded secondary implication" (used in Item 4)

> SKELETON: "[Label]. [Main claim denying X], which also means that [secondary consequence denying Y as well]."

1. **Slot 1 — Label:** Short noun phrase (e.g., "No inheritance of disease").
2. **Slot 2 — Main denial:** A clause stating the primary thing the model excludes. Shape: "There is no X."
3. **Slot 3 — Secondary denial:** Begins with "which also means that" and adds a *parallel* exclusion that follows from the first. Shape: another negative clause, often introduced with "as well."

**Original fill:** "No inheritance of disease. There is no inheritance of the epidemic, which also means that immunity of the disease is not inheritable as well."

**Demonstration fill (different idea — chemical decay model):** "No chain reaction. There is no neutron-induced fission in the decay chain, which also means that daughter isotopes cannot trigger further decay as well."

---

### Skeleton C — "Claim + enumerative specification" (used in Item 3)

> SKELETON: "[Label]. [General claim stating constancy], and [the constant] would not change for [enumerated list of varying factors]."

1. **Slot 1 — Label:** Short noun phrase (e.g., "Constant probability of infection").
2. **Slot 2 — General claim:** Asserts uniformity. Shape: "There is a constant X."
3. **Slot 3 — Enumeration:** Begins "and … would not change for" and lists 2–5 demographic/contextual axes across which the parameter is invariant.

**Original fill:** "Constant probability of infection. There is a constant probability of infection, and the probability of infection of the epidemic would not change for people of different ages, genders, races etc."

**Demonstration fill (different idea — diffusion model):** "Constant diffusion coefficient. There is a constant diffusion coefficient, and the diffusion coefficient of the solute would not change for regions of different temperature, concentration, pressure etc."

---

### Skeleton D — "Claim + meaning-clause unpacking" (used in Item 5)

> SKELETON: "[Label]. [Claim asserting the structural property], meaning that [mechanistic unpacking of what the property implies in practice]."

1. **Slot 1 — Label:** Short noun phrase (e.g., "Homogenous mixing").
2. **Slot 2 — Structural claim:** Names the property. Shape: "There is X of the Y."
3. **Slot 3 — Mechanism:** Begins "meaning that" and states what the property *entails* operationally. Shape: a clause describing equal/identical behaviour across the population.

**Original fill:** "Homogenous mixing. There is homogenous mixing of the population, meaning that all members of the population have an equal number of interactions with each other over time."

**Demonstration fill (different idea — random-walk stock model):** "Unbiased steps. There is unbiased stepping in the price walk, meaning that every trader has an equal probability of buying or selling at each tick."

---

## Express-Idea Vocabulary

**Sequencing / enumeration**
- "In other words," — restating into model language. *"In other words, if a person from the 𝐼 population has recovered…"*
- (Implicit) numbered ordering "1, 2, 3, 4, 5." — sets up assumption list rhythm.

**Cause / consequence**
- "thus" — marks downstream consequence. *"He or she would be immune to infection by the epidemic and thus unable to be classed as the 𝑆 population again."*

**Specification (listing what does/doesn't vary)**
- "would not change for people of different ages, genders, races etc." — enumerates axes of invariance.

**Explanatory unpacking**
- "meaning that" — converts a label into a mechanism. *"There is homogenous mixing of the population, meaning that all members…"*
- "which also means that" — adds a *second* parallel implication in the same sentence. *"There is no inheritance of the epidemic, which also means that immunity…is not inheritable as well."*

**Definition / labelling verbs**
- "is immune from" — defines post-recovery state. *"A person is immune from the epidemic upon recovery."*
- "put into" — assigns to a compartment. *"he or she would be put into the 𝑅 population group."*
- "classed as" — assigns to a compartment on the alternative side. *"unable to be classed as the 𝑆 population again."*

**Hedging / generalisation markers**
- "etc." — signals the enumeration list is non-exhaustive. *"people of different ages, genders, races etc."*
- "over time" — temporal qualifier that softens the structural claim. *"equal number of interactions…over time."*

---

## How to Explain an Idea (replication steps)

This section relies on the pattern: **Label → Plain claim → Model-language restatement → Consequence/Unpacking**, with each item being a self-contained micro-paragraph that closes before the next begins.

**Step-by-step instructions to explain a new idea (e.g., assumptions of a logistic growth model) using the same pattern:**

1. **Pick the assumption to state.** Give it a short noun-phrase label (2–4 words) that captures the *thing being simplified*. Place it at the start of the item.

2. **State the rule in plain language.** Write one declarative sentence using a generic subject ("A population…", "An individual…", "The system…") and present tense. This is the *claim* — what the model assumes.

3. **Reformulate in the model's variables.** Open with "In other words," (or equivalent) and translate the rule into the symbols/compartments/parameters of *your* model. Use a conditional ("if X, then Y") so the reader sees the transition.

4. **State the consequence or secondary implication.** Either (a) use "thus" / "therefore" to mark what *follows* from the rule, OR (b) use "which also means that" to add a parallel exclusion, OR (c) use "meaning that" to unpack the mechanism. Choose *one* of these three connectives — don't stack.

5. **Move to a different domain for the next item.** The list should rotate across *categories* of simplification: container → compartments → parameters → excluded pathways → contact/network structure. Each new item should attack a *new* aspect of reality the model ignores.

6. **Close the item.** No hand-off sentence is needed — the next numbered item is itself the transition.

**Diagnostic check — does your item sound right?**
- Does it have a 2–4-word label? ✓
- Does it use a model-specific variable/parameter somewhere? ✓
- Does it use exactly one of {thus / which also means that / meaning that}? ✓
- Does it close on a *consequence*, not a new claim? ✓
