# Idea Flow Notes: business-management_7_may2021_gjkNKwxCMqvteD5H — Cost Comparison Observations

## Paragraph Flow (move by move)

**Paragraph 1 (Costing-note disclaimer, ~55 words):**

1. **Move: claim + scope-limit.** "*All cost estimates provided here are compiled using information available to us at the time of the initial teardown.*" → Hands forward by signalling a **temporal boundary** ("at the time of"), which forces the next sentence to explain *what happens when that boundary is crossed* — i.e. assumptions must be stated.
2. **Move: concession / evidence-handling.** "*Some assumptions have been made where concrete data is not yet available.*" → Hands forward by introducing an **acknowledged gap** ("not yet available"), which makes the next sentence the natural place to promise *closure* of that gap.
3. **Move: forward plan (implication for future reading).** "*We will continue to gather and refine this costing data throughout our on-going deep-dive teardown process and analysis.*" → Hands forward by stating an **ongoing action**, which makes a statement of *expected magnitude of change* the logical next move.
4. **Move: verdict / magnitude qualifier.** "*While we do not expect drastic cost changes, we do expect some adjustments.*" → **Terminal move** (closes the disclaimer with a calibrated reassurance: "some" but not "drastic").

(The preceding table — itemized components with prices, capped by a Total — is not a paragraph but a content move: a **ranked inventory of cost categories** with a summation. See next section.)

## What This Section Does (content sequence)

This is a **cost-comparison observation section**, and its content moves in this fixed order:

1. **Header identification** — device name + teardown date. Sets *what* is being costed and *when the snapshot was taken*.
2. **Component-by-component line items** with USD values. Sets up the reader to scan for the *heaviest cost drivers* and to compare them mentally.
3. **Summation line (Total).** This must come last because the total only becomes meaningful after every category has been listed.
4. **Costing-note disclaimer.** This must come after the table because the disclaimer retroactively qualifies the numbers above; placing it earlier would interrupt the reader before they have seen what is being qualified.

**Why this order:** the table is a snapshot whose authority depends on (a) the date it was taken and (b) an honest caveat about its precision. Date first establishes recency; the body delivers the raw figures; the Total converts them into a single comparable figure; the disclaimer governs how literally the reader should treat every number above it. Replicators should keep this 1→2→3→4 order; reordering breaks the implicit contract that the disclaimer governs the table.

## Paragraph Skeletons (replicable templates)

**SKELETON A — Component-cost row (slot template for one line item):**
`[Category name] [tab/whitespace] $[price with two decimals]`

- **What each slot holds:**
  - Slot 1 = a **noun phrase** naming a bill-of-materials category (e.g. "Memory: Non-Volatile").
  - Slot 2 = a **dollar amount**, always to two decimal places, no currency symbol on the left if the header already declared "$".
- **How to fill it with a different idea:** pick one functional subsystem of the device you are costing; pick a USD figure consistent with its share of the total; preserve the two-decimal format.
- **Original filled version:** "Display / Touchscreen  $31.00"
- **Demonstration fill with a different idea (different subject, same skeleton):**
  - "Hinge Assembly  $4.25"
  - "PCB: Main Logic  $18.75"

**SKELETON B — Summation line:**
`[Label word] [tab/whitespace] $[aggregate to two decimals]`

- **What each slot holds:**
  - Slot 1 = a single word signalling closure, here "Total".
  - Slot 2 = the **sum of every line item**, again to two decimals.
- **How to fill it:** write "Total" (or equivalent — "Grand Total", "Sum"); arithmetic-add every preceding row; format to two decimals.
- **Original filled version:** "Total  $290.00"
- **Demonstration fill (different subject):** "Total  $184.50"

**SKELETON C — Costing-note disclaimer (whole paragraph):**
`[Claim about data source]. [Concession about gaps]. [Forward plan]. [Magnitude verdict]`

- **What each slot holds:**
  - Slot 1 (Claim): full sentence, present perfect passive — "*All cost estimates … are compiled using information available to us at the time of the initial teardown.*" Sets a temporal frame.
  - Slot 2 (Concession): full sentence, present perfect active — "*Some assumptions have been made where concrete data is not yet available.*" Admits a gap created by Slot 1's frame.
  - Slot 3 (Forward plan): full sentence, future continuous — "*We will continue to gather and refine this costing data throughout our on-going deep-dive teardown process and analysis.*" Promises closure of Slot 2's gap.
  - Slot 4 (Magnitude verdict): concessive clause + corrective clause — "*While we do not expect drastic cost changes, we do expect some adjustments.*" Calibrates the reader's expectations.
- **How to fill it with a different idea:** keep the four-sentence shape and tense pattern; substitute only the *thing being costed* and the *process name*; keep "at the time of", "where concrete data is not yet available", and the "while … do" calibrator intact, since they are the load-bearing connectives.
- **Original filled version:** the four sentences quoted under Paragraph Flow above.
- **Demonstration fill (different subject, same skeleton):**
  - "All emissions figures provided here are compiled using information available to us at the time of the initial audit."
  - "Some assumptions have been made where concrete data is not yet available."
  - "We will continue to gather and refine this emissions data throughout our on-going deep-dive audit process and analysis."
  - "While we do not expect drastic figure changes, we do expect some adjustments."

**SKELETON D — Header block:**
`[Device name]` + `[Teardown Date label][tab][date]` + `[Applications Processor label][tab][–]`

- The dash `–` in place of a value is itself a structural signal meaning "category exists but value not disclosed at this snapshot"; it pairs with Slot 1 of Skeleton C.
- Demonstration fill: "Nokia 8 Sirocco" / "Teardown Date  April 2018" / "Applications Processor  –"

## Express-Idea Vocabulary

- **Sequencing / framing the snapshot:** "*at the time of the initial teardown*" — temporal anchor for everything above.
- **Evidence-handling / concession:** "*Some assumptions have been made where concrete data is not yet available*" — admits uncertainty without retracting the figures.
- **Forward plan (process verb):** "*gather and refine*" / "*continue … throughout our on-going*" — verbs of ongoing refinement, not one-off correction.
- **Contrast / calibration:** "*While we do not expect drastic cost changes, we do expect some adjustments*" — concessive "while …" paired with corrective "do".
- **Definition-by-format (non-verbal):** the two-decimal price format (`$31.00`, `$0.50`) functions as a precision marker; uniform width acts as a definition of "estimate" in this document.

## How to Explain an Idea (replication steps)

This section does **not** explain an idea in the narrative sense. Its replication pattern is **inventory-with-caveat**, a four-step procedure:

1. **Name the object and freeze the moment.** State the device + teardown date so the reader knows what they are looking at and how stale it may already be.
2. **List every cost category as a row with a uniform two-decimal price.** The uniformity is the explanation — it tells the reader every number carries the same assumed precision, which justifies the disclaimer that follows.
3. **Close with a Total.** This converts the row-by-row inventory into a single comparable figure; without it the table is unreadable as a cost.
4. **Append a four-sentence reliability disclaimer** in the exact order: data source → gap acknowledgement → ongoing-refinement promise → calibrated magnitude verdict. This sequence is non-reorderable because each sentence retroactively governs the interpretation of the table above it.
