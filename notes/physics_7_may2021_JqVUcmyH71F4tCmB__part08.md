# Idea Flow Notes: physics_7_may2021_JqVUcmyH71F4tCmB — Rocket

## Paragraph Flow (move by move)

There is effectively **one paragraph** here, the table itself plus its caption. I'll treat each structural layer as a move.

**Paragraph 1 (Table + caption)**

- **Move 1 — Variable naming (claim/definition):** `"~vb ~hb ∆~hc ~hmax tc tmax"` — six symbolic headers are introduced. The reader is told *what will be measured*. → Hands the reader to Move 2 because **symbols without units are unreadable**; the next line specifies the meaning of the symbols.
- **Move 2 — Unit specification (specification/precision):** `"(ms−1) (m) (m) (m) (s) (s)"` — units are slotted directly under each header. → Hands the reader to Move 3 because **now that dimension is fixed, the magnitude of each variable can be presented** without ambiguity.
- **Move 3 — Evidence (data rows A → R):** `"A 642.9 1553.2 21085.6 …"` — eighteen rockets' theoretical values are listed. The ordering principle is **descending velocity** (A = 642.9, R = 150.1). → Hands the reader to Move 4 because **unlabeled data is unowned**; the caption names the dataset.
- **Move 4 — Caption (labelling / verdict):** `"Table 5: Theoretical calculated data retrieved for each rocket."` — labels the block, flags it as *theoretical* (not empirical), and ties it to the rocket corpus of the investigation. → Closes the paragraph; the table is now self-identifying for any later reference ("as shown in Table 5…").

## What This Section Does (content sequence)

For a **data-presentation section** of this kind (a single results table), the logical move order is:

1. **Header symbols first** — declares *which variables* will be shown. Sets up units.
2. **Units immediately below** — converts symbols into measurable quantities. Sets up valid comparison.
3. **Ordered data rows** — delivers the *evidence* in a sortable sequence (here: descending `~vb`). Sets up a pattern the reader can read off.
4. **Caption last** — retrospectively *names and scopes* the table, links it to the wider investigation ("theoretical", "each rocket"), and lets later sections back-reference it.

**Why this order:** symbol → unit → magnitude → label mirrors how a reader must decode any table: first know *what*, then *in what unit*, then *how big*, then *what is this called.* Re-ordering (caption on top, units last) would force the reader to revisit the table when they hit unknown terms.

## Paragraph Skeletons (replicable templates)

**SKELETON 1 — Variable declaration row**
> [Symbol₁] [Symbol₂] [Symbol₃] [Symbol₄] [Symbol₅] [Symbol₆]

1. **Slot hold:** Six (or more) abbreviated mathematical/physical symbols, each representing one independent quantity; grammatical shape = bare noun phrases separated by whitespace.
2. **How to fill differently:** Slot 1–6: pick the six variables your investigation will compare. Use Greek letters, tildes (~) for *approximate* or *theoretical*, subscripts to fix meaning (e.g. `~hb` = approximate burnout altitude). Order from "fastest-changing" to "slowest-changing" so the table reads left-to-right with the most diagnostic variable first.
3. **Original fill:** `"~vb ~hb ∆~hc ~hmax tc tmax"` — six rocket-flight variables, tilde-marked to flag them as theoretical approximations.
4. **Demonstration fill (different idea):** `"~Ia  ~Ra  ∆~θc  ~ωmax  τc  τmax"` — six variables for a theoretical DC-motor experiment (current, resistance, angular displacement, max speed, characteristic time, max time).

**SKELETON 2 — Unit row**
> (unit₁) (unit₂) (unit₃) (unit₄) (unit₅) (unit₆)

1. **Slot hold:** SI unit (or domain-standard unit) of each header symbol, in parentheses, **aligned vertically** under its symbol. Grammatical shape = parenthetical noun.
2. **How to fill differently:** For each header symbol, write the matching unit in parentheses. Use superscripts (m², s⁻¹) for compound units. Keep alignment perfect so the eye pairs symbol↔unit automatically.
3. **Original fill:** `"(ms−1) (m) (m) (m) (s) (s)"` — velocity, three altitudes, two times.
4. **Demonstration fill:** `"(A) (Ω) (rad) (rads−1) (s) (s)"` — motor current, resistance, angle, angular velocity, two times.

**SKELETON 3 — Ordered data block + caption**
> [Label₁] v₁₁ v₁₂ v₁₃ v₁₄ v₁₅ v₁₆
> [Label₂] v₂₁ v₂₂ v₂₃ v₂₄ v₂₅ v₂₆
> … (n rows, sorted by column-1 descending)
> Table N: [adjective] [noun-phrase] [past-participle clause] for each [subject].

1. **Slot hold:** Row label (A, B, C…) followed by n numeric values matching the headers; final line is a numbered table caption containing four elements — ordinal ("Table 5"), epistemic qualifier ("theoretical"/"experimental"), noun phrase describing the dataset, and a "retrieved for each X" tail that ties the table to the investigation's specimen set.
2. **How to fill differently:** Slot 1: give each specimen a single-letter label A–Z. Slot 2: enter the value of each header variable for that specimen, rounded to 3–4 sig figs. Slot 3: sort the rows by the first variable descending. Slot 4: write a caption of the form `Table [number]: [theoretical|experimental|raw|processed] [data-type] [retrieved/collected/measured] for each [specimen].`
3. **Original fill:** rows A→R sorted by `~vb` descending; `"Table 5: Theoretical calculated data retrieved for each rocket."`
4. **Demonstration fill:** rows M1→M18 sorted by `~Ia` descending; `"Table 2: Theoretical calculated data retrieved for each motor."`

## Express-Idea Vocabulary

Because this section is a table rather than prose, traditional connectives are absent. The "vocabulary of expression" here is the **typographic and structural lexicon** that does the same job:

- **Sequencing / ordering:** *descending order of row labels A→R* — implicit in `"A 642.9 … R 150.1"`; the alphabetical letterring plus monotonically-decreasing first column *is* the "firstly → next → finally" of a table.
- **Specification / precision:** *parenthesised units* — `"(ms−1)"`, `"(m)"`; they convert abstract symbols into measurable quantities, doing the work "in particular" or "that is" would do in prose.
- **Evidence handling / sourcing:** *epistemic qualifier in caption* — `"Theoretical calculated data"`; equivalent to "according to the model" or "this suggests", flagging that values come from computation, not measurement.
- **Explanation / labelling verbs:** *"retrieved for"* — `"retrieved for each rocket"`; equivalent to "obtained from", a neutral verb that attributes the dataset to the calculation process without claiming experimental authority.
- **Concession / scope marker:** *"each"* — `"for each rocket"`; equivalent to "for every instance", establishing that the dataset covers the full specimen set, not a sample.

## How to Explain an Idea (replication steps)

This section does **not** rely on a definitional or causal explanation pattern — it relies on a **structured-evidence pattern**: *declare what is being measured → declare the units → present the evidence in an ordered sweep → name the table.*

Step-by-step replication for any new dataset:

1. **Step 1 — Choose your variables.** Pick the smallest set of quantities that fully characterises each specimen (here: 6 rocket-flight variables). Use symbolic notation so the table header is compact.
2. **Step 2 — Symbol-with-unit pairing.** Place every symbol on a top row, then place its SI unit directly below in parentheses. Vertical alignment is non-negotiable — the eye must pair symbol to unit without searching.
3. **Step 3 — Order the rows meaningfully.** Sort specimens by the most diagnostic variable (here: descending `~vb`) so the table itself communicates a trend before any prose does.
4. **Step 4 — Round to consistent significant figures.** Use the same decimal precision per column (here: one decimal place) so columns are visually comparable.
5. **Step 5 — Number the table sequentially** (`Table 1`, `Table 2`, …) so other sections can refer back without ambiguity.
6. **Step 6 — Write the caption in four parts:** ordinal + epistemic qualifier (`theoretical`/`experimental`) + noun-phrase description of the data + `"retrieved/measured for each [specimen]"` to tie the block to the investigation's specimen set.
