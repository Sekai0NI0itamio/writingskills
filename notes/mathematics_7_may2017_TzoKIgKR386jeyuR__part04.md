# Idea Flow Notes: mathematics_7_may2017_TzoKIgKR386jeyuR — Variables                                                     Explanation

## Paragraph Flow (move by move)

**Paragraph 1 — Opening claim before Equation 2**
- Sentence 1 — **Claim**: "From the above we can create 3 differential equations that represent the rates of change" → *Hands off by*: invoking the table just shown, it commits the writer to produce three equations next, so the reader expects Equation 2 to follow as the first of the three promised.

**Paragraph 2 — Unpack of Equation 2**
- Sentence 1 — **Reference + probabilistic setup**: "(Refer to Equation 2) The probability that a person from the 𝑆 population group meeting" → *Hands off by*: naming the first multiplicative factor of the equation, so the next sentence must supply the next factor.
- Sentence 2 — **Specification (next factor)**: "The probability that the interaction between the 𝑆 and 𝐼 person is infectious is 𝑖." → *Hands off by*: completing the infection-probability ingredient, it forces the reader to ask "where does the contact frequency come from?" — answered next.
- Sentence 3 — **Specification (final factor)**: "The number of interactions per day in the population is (𝑁 × 𝛼)." → *Hands off by*: giving the last multiplicative ingredient, so the synthesis claim becomes available now.
- Sentence 4 — **Synthesis / verdict**: "Thus all of the variables multiplied results in the rate of change" → *Hands off by*: producing a magnitude statement, it triggers the obvious "but what about the minus sign?" question — answered next.
- Sentence 5 — **Sign justification / mechanism**: "Note that a negative sign is put in front of the equation as" → *Hands off by*: closing the S-compartment story, it leaves the I-compartment as the natural next case.

**Paragraph 3 — Unpack of Equation 3**
- Sentence 1 — **Reference + contrast marker**: "(Refer to Equation 3) Contrary to the previous equation, the first part" → *Hands off by*: signaling a contrast, it forces an explicit justification sentence.
- Sentence 2 — **Unpack / mechanism (justifies the contrast)**: "as the rate of decrease of the number of people being infected in the 𝑆 population" → *Hands off by*: closing the gain-from-S term, it opens the loss-from-recovery term that the "However" pivot announces.
- Sentence 3 — **Contrast pivot**: "However, as the people in in the 𝐼 population group recover, the number of people" → *Hands off by*: introducing a new opposing process, it demands the corresponding rate term next.
- Sentence 4 — **Specification (recovery term)**: "The rate at which the number of people in the 𝐼 population group decreasing over time can be given by −𝐼(𝑡) × 𝑟" → *Hands off by*: completing Equation 3, it leaves the R-compartment — the obvious remaining case — as the logical next step.

**Paragraph 4 — Unpack of Equation 4**
- Sentence 1 — **Reference + identity claim**: "(Refer to Equation 4) The number of people that recover over time is equal to" → *Hands off by*: giving the equation's plain-language reading, it invites the writer to anchor it back to the previous equation.
- Sentence 2 — **Cross-link / consequence**: "which is the negative of the second part of the previous equation." → *Hands off by*: tying the final equation to the prior one, it closes the three-equation system and ends the section.

---

## What This Section Does (content sequence)

A "Variables + Equation Exposition" section in IB coursework runs in this fixed order:

1. **Variable inventory** (table) — *why first*: every symbol that will appear on the right-hand side must be defined before it is used, otherwise the equations that follow are unreadable.
2. **Overarching claim about the system** — *why second*: announces that *n* equations will follow and names the model class, so the reader knows what genre of mathematics is coming.
3. **Equation 1, presented visually** — *why third*: gives the reader an object to look at before any prose explanation.
4. **Term-by-term probabilistic unpack of Equation 1** — *why fourth*: multiplies the individual factors in the same left-to-right order they appear in the formula, so the reader can map each spoken word to each symbol.
5. **Sign/direction justification for Equation 1** — *why fifth*: once the magnitude is built up, the remaining symbol (the minus) needs a one-sentence mechanism so nothing is left unmotivated.
6. **Equation 2, presented visually** — *why sixth*: shifts to the next dependent variable in the natural S→I→R narrative.
7. **Unpack of Equation 2 by contrast with Equation 1, then by adding a new term** — *why seventh*: piggy-backs on what was just explained ("contrary to the previous equation…") so the reader only has to learn the *delta*, then appends the recovery term.
8. **Equation 3, presented visually** — *why eighth*: completes the system.
9. **Unpack of Equation 3 as the negative of a prior piece** — *why ninth*: the easiest explanation is to point back, because Equation 3 is structurally forced by Equations 1 and 2.

The general principle: *show the symbol, then narrate the symbol from left factor to right factor, then close the loop by linking each new equation to the one before.*

---

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Term-by-term multiplicative unpack + sign justification"**
1. **What each slot holds**
   - Slot 1: Cross-reference opener naming the equation ("Refer to Equation X").
   - Slot 2: Plain-language statement of factor 1, matching the first term on the RHS.
   - Slot 3: Plain-language statement of factor 2, matching the second term on the RHS.
   - Slot 4: Plain-language statement of factor 3, matching the third term on the RHS.
   - Slot 5: Synthesis sentence beginning "Thus…" tying all factors together as "the rate of change of…"
   - Slot 6: Sign / direction note beginning "Note that…" giving the physical reason for a +/−.
2. **How to fill it with a DIFFERENT idea**
   - Slot 1: write the equation label exactly as it appears in the display.
   - Slot 2–4: pick the three symbols that are being multiplied on the RHS; describe each one as a probability / rate / count using everyday language; keep them in left-to-right order.
   - Slot 5: join the factors with "multiplied" and restate what the whole product *is* (the derivative's meaning).
   - Slot 6: identify which way the quantity moves (increases or decreases) over time and state the cause in one clause beginning with "as".
3. **Original filled version** — the Equation 2 paragraph: "(Refer to Equation 2) The probability that a person from the 𝑆 population group… The probability that the interaction… is 𝑖. The number of interactions per day… is (𝑁 × 𝛼). Thus all of the variables multiplied results in the rate of change… Note that a negative sign is put in front… as the number of people… decreases over time as people are infected."
4. **Demonstration fill (different idea, same skeleton)** — *Cooling of a hot drink (Newton's Law of Cooling)*: "(Refer to Equation 1) The temperature difference between the drink and the surrounding air is (𝑇(𝑡) − 𝑇ₐ). The rate at which heat leaves the drink per degree of difference is 𝑘. The area over which heat is lost is 𝐴. Thus all of the variables multiplied results in the rate of change of the drink's temperature over time. Note that a negative sign is put in front of the equation as the temperature of the drink decreases over time as heat is lost to the air."

**SKELETON B — "Contrast with previous equation + additive new term"**
1. **What each slot holds**
   - Slot 1: Cross-reference opener with explicit contrast marker ("Refer to Equation Y. Contrary to the previous equation…").
   - Slot 2: Unpack of the part that mirrors (or negates) the prior equation, phrased as a reason clause beginning "as".
   - Slot 3: Pivot word ("However,") introducing an opposing process affecting the same compartment.
   - Slot 4: Specification of the new term, finishing "thus forming the second part of the equation."
2. **How to fill it with a DIFFERENT idea**
   - Slot 1: start the new equation by saying its first term is the *negative* of the previous equation's RHS — this is your mirror.
   - Slot 2: explain that the sign flip exists because what one compartment loses another gains (conservation).
   - Slot 3: name a *different* process that drains the same compartment (here: recovery; substitute removal, decay, leakage, etc.).
   - Slot 4: state the rate of that process as a product of the compartment's size and a per-capita rate; close with "thus forming the second part of the equation."
3. **Original filled version** — the Equation 3 paragraph: "(Refer to Equation 3) Contrary to the previous equation, the first part of the equation is the negative… as the rate of decrease… is the negative of the rate of increase… However, as the people in in the 𝐼 population group recover… The rate at which the number of people in the 𝐼 population group decreasing… can be given by −𝐼(𝑡) × 𝑟, thus forming the second part of the equation."
4. **Demonstration fill (different idea, same skeleton)** — *Predator–prey, predator equation*: "(Refer to Equation 2) Contrary to the previous equation, the first part of the equation is the negative of 𝑑𝑥/𝑑𝑡, as the rate of decrease of the prey population is the negative of the rate of increase of the predator population. However, as the predators die of natural causes, the number of predators in the population decreases. The rate at which the number of predators decreasing over time can be given by −𝑦(𝑡) × 𝑚, thus forming the second part of the equation."

**SKELETON C — "Single-sentence equation explanation by cross-link"**
1. **What each slot holds**
   - Slot 1: Cross-reference opener.
   - Slot 2: Identity claim describing what the left-hand side equals in words.
   - Slot 3: Relative clause ("which is…") pointing back to the matching term in the previous equation.
2. **How to fill it with a DIFFERENT idea**
   - Slot 1: name the final equation in the system.
   - Slot 2: restate the equation as "the quantity that [does X] is equal to [compartment size] times [per-capita rate]".
   - Slot 3: explicitly say it is the negative of the corresponding term already explained, so the reader's understanding transfers automatically.
4. **Original filled version** — the Equation 4 paragraph: "(Refer to Equation 4) The number of people that recover over time is equal to the number of people in the 𝐼 population multiplied by the probability of recovery from the epidemic, which is the negative of the second part of the previous equation."
4. **Demonstration fill (different idea, same skeleton)** — *Prey equation in predator–prey*: "(Refer to Equation 3) The number of prey eaten over time is equal to the number of prey in the population multiplied by the encounter rate with predators, which is the negative of the second part of the previous equation."

---

## Express-Idea Vocabulary

- **Sequencing / referencing the artefact**: "(Refer to Equation 2)", "(Refer to Equation 3)", "(Refer to Equation 4)" — used to anchor every paragraph to the visual equation it explains.
- **Cross-link / contrast**: "Contrary to the previous equation, the first part of the equation is the negative of 𝑑𝑆(𝑡)/𝑑𝑡" — used to delegate the first half of a new equation to one already explained.
- **Causal / mechanistic conjunctions**: "as the rate of decrease of the number of people being infected in the 𝑆 population" (causal "as"), "as the people in in the 𝐼 population group recover" (causal "as"), "as the number of people in the 𝑆 population group decreases over time" (causal "as").
- **Synthesis / verdict markers**: "Thus all of the variables multiplied results in the rate of change", "thus forming the second part of the equation", "which is the negative of the second part of the previous equation" — used to convert multi-factor lists into a single claim.
- **Specification / quantifier sentences**: "The probability that a person from the 𝑆 population group meeting a person", "The probability that the interaction between the 𝑆 and 𝐼 person", "The number of interactions per day in the population" — three short subject–verb–complement sentences, one per multiplicative factor.
- **Sign / direction flag**: "Note that a negative sign is put in front of the equation as the number of people in the 𝑆 population group decreases over time as people are infected" — used to mop up the remaining symbol once the magnitude is built.
- **Definition opener (earlier in section, via table caption)**: "The average number of interactions between people in the population per capita per unit time" — variable-definition pattern reused in the table row.
- **Identity / equivalence phrasing**: "The number of people that recover over time is equal to the number of people in the 𝐼 population multiplied by" — used for the shortest equation.

---

## How to Explain an Idea (replication steps)

**Pattern: Definition → Visual Equation → Term-by-Term Unpack → Sign/Direction Note → Contrast-with-Previous for each following equation → Final equation by cross-link.**

Use this exact sequence when you must explain a system of three or more linked equations to a reader who only knows your defined variables:

1. **Define every symbol that will appear on the right-hand side**, in a table, before any equation is written (sets the alphabet).
2. **State the structural claim** ("From the above we can create n differential equations that represent…") so the reader knows the count and the model class.
3. **Display Equation 1 visually**, on its own line, with a numbered label.
4. **Open the explanatory paragraph with a cross-reference** ("Refer to Equation 1") so the reader pairs text with image.
5. **Unpack the equation left-to-right**: one sentence per multiplicative factor, in the order the factors appear on the RHS, each phrased as "The [quantity] is [symbol]." — this guarantees no factor is skipped.
6. **Synthesise with a "Thus…" sentence** that names what the whole product represents (e.g. "the rate of change of the S population group over time").
7. **Justify the remaining sign or direction in one "Note that…" sentence**, giving the physical/combinatorial reason.
8. **Display Equation 2 visually**, then **unpack it as a contrast to Equation 1**: start with "Contrary to the previous equation, the first part of the equation is the negative of [prior RHS]" and append "as [conservation/complementary-flow reason]."
9. **Add the *new* term with a "However," pivot** that introduces a second opposing process affecting the same compartment, then state the new rate as "The rate at which [compartment] [decreases/increases]… can be given by [expression], thus forming the second part of the equation."
10. **Display Equation 3 visually**, then **explain it in one or two sentences by pointing back**: state what the LHS equals in words, then finish with a relative clause ("which is the negative of the second part of the previous equation") so the reader's prior understanding does the work.
