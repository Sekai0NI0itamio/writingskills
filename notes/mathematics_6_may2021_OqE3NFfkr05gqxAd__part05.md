# Idea Flow Notes: mathematics_6_may2021_OqE3NFfkr05gqxAd — version I will exclude some neighbourhoods, as we know without the need of a

## Paragraph Flow (move by move)

**Paragraph 1**
1. **Claim / consequence** — "going in circles around a neighbourhood will take longer" — names the inefficiency that motivates a cleaner model; hands to S2 because the reader now needs to *see* the layout being optimised over (consequence: we need a tractable map).
2. **Evidence / visual setup** — "In Figure 5 we have the image from google maps and in Figure 6 the simpler representation of the map" — supplies the two artefacts, raw and abstract; hands to S3 because the simplified map is the object the assumption now constrains.
3. **Assumption / condition-setting** — "we are only moving forward, we will not count paths moving backwards" — narrows the model so the next step is workable; hands to ¶2 by signalling "the next step" of construction.

**Paragraph 2**
1. **Transition / stage marker** — "The next step is to construct the graph" — announces the procedural move; hands to S2 because "graph" now requires unpacking.
2. **Definition (component 1)** — "At each intersection between two or more roads, we will set a vertex" — first rule; hands to S3 by parallelism (the other half of the structure).
3. **Definition (component 2)** — "each line that connect two vertices will be a weighted edge where the edges will have the distance associated" — second rule completing the structure; hands to S4 because a drawing decision now follows.
4. **Method choice / authorial decision** — "I chose to do two separate figures to show the vertices and the edges" — personal act of representation; hands to S5 by inviting justification.
5. **Cause / consequence (justification)** — "If they were only in one figure it would be a mess, therefore in two different figure it is much easier to understand" — counter-factual problem → chosen remedy; hands to S6 by delivering the first of the promised figures.
6. **Evidence reference** — "In Figure 7 we have the representation with vertices" — first visual deliverable; hands to S7 because the second figure was also promised.
7. **Evidence reference (with data spec)** — "in Figure 8 we have the representation of the edges where all values are in meters" — second visual, with units; hands to ¶3 because the source of those numbers still needs explaining.

**Paragraph 3**
1. **Evidence handling / source** — "I got the values using a tool in google maps to measure distances" — explains how the weights were produced; hands forward (text cuts off) by raising "the" next operation.

## What This Section Does (content sequence)

This is a **method / model-construction** section in a math exploration. The ordered moves are:

1. **State the cost of the naive strategy** (motivates why we model at all).
2. **Show the raw and abstracted map** side-by-side (gives the reader the visual ground truth + the working artefact).
3. **Fix an assumption that scopes the model** (one-way movement only).
4. **Mark the next procedural stage explicitly** ("The next step…").
5. **Define component 1 (vertex)**, then **component 2 (edge)** in parallel (so the reader sees the two-part structure).
6. **Announce a presentation choice**, then **justify it** with a counter-factual + consequence.
7. **Reference each resulting figure in turn** with what it contains and any units.
8. **Attribute the data source** so the numbers are traceable.

The order matters because: motivation → visual object → simplifying assumption → procedural verb → definitions of parts → display decision → figures → provenance. You cannot define "vertex" before announcing "construct the graph"; you cannot justify splitting the figures before showing the figures; you cannot cite units before the figure they belong to.

## Paragraph Skeletons (replicable templates)

**SKELETON A — "Constraint + assumption + visual setup" paragraph**
`"[Consequence that makes the naive approach costly]. In Figure [N] we have [the raw real-world artefact] and in Figure [N+1] [the cleaned schematic]. Also, we will need to make the same assumption we did in [the prior example], [rule A], [rule B]."`

1. Slot 1 — *consequence clause* (relative or noun clause stating the inefficiency). Slot 2 — *two-figure pair* (raw vs. simplified). Slot 3 — *assumption clause* with echo-back of the prior example.
2. To fill with a new idea: pick a real-world layout (river network, subway map, classroom desk grid), name a strategy that is slow/inefficient on it, draw or screenshot both the real and schematic versions, and state one directional or one-way restriction that you'll carry through.
3. Original fill: "going in circles around a neighbourhood will take longer. In Figure 5 we have the image from google maps and in Figure 6 the simpler representation of the map. Also, we will need to make the same assumption… we are only moving forward, we will not count paths moving backwards."
4. Demonstration fill (different idea): "running every branch of a decision tree exhaustively is computationally explosive. In Figure 2 we have the raw questionnaire with all follow-up paths and in Figure 3 the simplified decision tree. Also, we will need to make the same assumption we did in the pilot, each respondent answers once only, we will not count revisiting earlier nodes."

**SKELETON B — "Next-step + two definitions + display justification + figure pair" paragraph**
`"The next step is to [verb the construction]. At [location satisfying criterion X], we will set [component 1]. And [component 2] will [link them with property Y]. I chose to [display decision]. If [opposite decision] it would be [problem], therefore [chosen decision] it is much easier to understand. In Figure [N] we have [first deliverable]. And in Figure [N+1] we have [second deliverable] where [units/specification]."`

1. Slot 1 — *stage-marking clause* (noun phrase + to-infinitive). Slot 2 — *definition A* (where the first element is placed). Slot 3 — *definition B* (parallel construction with weighting/label rule). Slot 4 — *display choice* (first person past). Slot 5 — *counter-factual + remedy* (If… therefore…). Slot 6+7 — *figure pair with units*.
2. To fill with a new idea: pick a system that decomposes into two kinds of object (nodes + links, states + transitions, atoms + bonds). State the placement rule for object A, the linking rule for object B, justify why you'll show A and B separately, then reference two figures, giving units on the second.
3. Original fill: "The next step is to construct the graph. At each intersection… we will set a vertex. And each line… will be a weighted edge… I chose to do two separate figures… If they were only in one figure it would be a mess, therefore in two different figure it is much easier to understand. In Figure 7 we have… vertices. And in Figure 8 we have… the edges where all values are in meters."
4. Demonstration fill (different idea): "The next step is to assemble the state diagram. At each state the agent can legally occupy, we will set a node. And each permissible action will be a directed transition labelled with the reward. I chose to draw the nodes on one sheet and the transitions on a second. If they were only on one page it would be unreadable, therefore on two sheets the arrows are much easier to follow. In Figure 4 we have the labelled nodes. And in Figure 5 we have the transitions where all values are in points."

**SKELETON C — "Data-provenance mini-paragraph"**
`"In Figure [N], I got the [values/labels] using [tool or method] to [measure/derive them]."`

1. Slot 1 — *figure reference*, Slot 2 — *the quantities*, Slot 3 — *source tool*, Slot 4 — *verb of measurement*.
2. To fill: name the figure that carries numerical data, name the dataset element, name the real-world source (app, ruler, spreadsheet, formula), give the action.
3. Original: "In Figure 8, I got the values using a tool in google maps to measure distances."
4. Demonstration: "In Figure 5, I got the resistances using a multimeter across each resistor leg to measure ohms."

## Express-Idea Vocabulary

- **Sequencing / stage-marking:** "The next step is to construct the graph" — announces procedural move.
- **Cause / consequence:** "therefore in two different figure it is much easier to understand" — remedy follows from problem.
- **Contrast / counter-factual:** "If they were only in one figure it would be a mess" — sets up the choice by negating the alternative.
- **Specification / restatement:** "we are only moving forward, we will not count paths moving backwards" — pins the assumption twice for clarity.
- **Evidence handling — figure reference:** "In Figure 5 we have the image from google maps"; "In Figure 7 we have the representation with vertices"; "in Figure 8 we have the representation of the edges where all values are in meters" — three near-identical "In Figure N we have…" shells that deposit visuals in order.
- **Evidence handling — attribution:** "I got the values using a tool in google maps to measure distances" — first-person source citation.
- **Explanation verbs (definition):** "we will set a vertex"; "will be a weighted edge where the edges will have the distance associated" — *set as* and *be a… where…* build the two component rules.
- **Transitional echo:** "Also, we will need to make the same assumption we did in the example" — links this section back to a prior worked instance.

## How to Explain an Idea (replication steps)

This section runs a **constraint → visual model → assumption → procedure → component definitions → display justification → evidence → provenance** chain. To replicate it on a new idea:

1. **Open with the cost of the naive approach** — one sentence naming what goes wrong if you don't model (e.g. "searching every path is too slow"). This earns the reader's attention.
2. **Display the raw vs. simplified artefact** — two figure references, one literal, one cleaned up. The reader must see both to trust the abstraction.
3. **Fix the simplifying assumption explicitly**, and echo it (state the rule, then re-state it in negative form: "we only do X, we will not count Y").
4. **Mark the next stage** with "The next step is to [construct X]". This is the procedural hinge.
5. **Define component 1** ("At [wherever], we set [thing 1]").
6. **Define component 2 in parallel** ("And [thing 2] will [link/weight] them"). Two coordinated sentences make the bipartite structure obvious.
7. **Announce your display choice in the first person** ("I chose to…").
8. **Justify with a counter-factual → consequence pair** ("If [opposite], it would be [bad], therefore [choice] is much [easier]").
9. **Deposit the two figures in turn**, adding units or specifications on the second one so the data is interpretable.
10. **Close with provenance** — name the tool, dataset, or method that produced the numbers, in one short "I got the values using…" sentence.

Follow steps 1→10 in order and you reproduce the same logical cadence on any modelling task (state machines, electrical circuits, supply chains, kinship diagrams) without copying the words.
