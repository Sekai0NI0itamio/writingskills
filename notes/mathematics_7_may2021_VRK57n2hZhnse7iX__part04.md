# Idea Flow Notes: mathematics_7_may2021_VRK57n2hZhnse7iX — 2.2    The 15-puzzle

## Paragraph Flow (move by move)

**Paragraph 1** (5 sentences)

1. S1: *"The parallel between the permutations"* — **Claim/topic sentence**; announces the bridging idea. Hands to S2 by promising a parallel, so the next sentence must deliver one side of it.
2. S2: *"The permutation is an individual move"* — **Definition** of the first side of the parallel (permutation) inside the new domain. Hands to S3 by fulfilling half the parallel — the other half (the set) is still owed.
3. S3: *"The set is every possible position"* — **Definition** of the second side of the parallel. Hands to S4 because both terms are now defined, so the next move is the *relationship* between them.
4. S4: *"A valid scramble should be able to be represented"* — **Implication / composed operation**; shows how the two defined pieces combine into a real-world action. Hands to S5 because the composed operation requires a well-defined underlying object before it can be executed.
5. S5: *"The first step to mathematically defining the 15-puzzle is to decide upon a valid set of positions:"* — **Sequencing / procedural transition**; announces the next move in the build. Hands to Paragraph 2 by demanding a formal object to be shown.

**Paragraph 2** (set display + grid — treated as one move-pair)

- *"P = {1, 2, 3, 4 … 16}"* — **Formal definition** of the announced object. Hands to the grid by needing to ground the abstract set visually.
- *"This set of positions is represented on the puzzle below:"* followed by the 4×4 grid — **Visual specification / instantiation**; maps the formal set onto the concrete object. Hands to Paragraph 3 because the grid has just revealed a count mismatch (15 tiles, 16 positions) that demands an explanation.

**Paragraph 3** (4 sentences, last one cut off)

1. S1: *"There are only 15 tiles on the puzzle, but there are 16 positions, hence the 16-th position is shown."* — **Justification by cause** ("hence") of the anomaly the reader just noticed. Hands to S2 because the anomaly now needs a *conceptual* resolution, not a numerical one.
2. S2: *"It is important to note the distinction between a tile and a position."* — **Signposting / conceptual distinction**. Hands to S3 because the distinction has been flagged, so the next sentence must spell it out.
3. S3: *"Any given position on the puzzle may include any of the tiles, or have no tile."* — **Unpack of the distinction** with an exhaustive case ("any … or have no tile"). Hands to S4 (truncated: *"Since the difference between a tile…"*) — **Consequence** move: the unpack now triggers a downstream implication about what "difference" means in this model.

---

## What This Section Does (content sequence)

This is a **mathematical setup / formalisation section**. The ordered content moves are:

1. **Announce the bridge** between an existing mathematical concept and the investigated object (claim sentence).
2. **Define side A** of the bridge inside the new domain.
3. **Define side B** of the bridge inside the new domain.
4. **State the composed action** — how the two sides operate together to represent a real behaviour of the object.
5. **Name the first formalisation step** (procedural transition).
6. **Display the formal object** (a set / list / equation).
7. **Instantiate the formal object visually** so the reader can see it.
8. **Justify any apparent anomaly** the visualisation exposes, using a cause connective.
9. **Flag a conceptual distinction** that the anomaly depends on.
10. **Unpack the distinction exhaustively** so downstream reasoning is sound.

The order works because each move is the *precondition* for the next: the parallel must be announced before the terms can be redefined; the terms must be redefined before they can be composed; the composed action presupposes a formal object; the formal object must be shown before its visual instantiation can be justified; and any mismatch the visualisation produces can only be resolved once the reader has the vocabulary (tile vs position) to follow the argument.

---

## Paragraph Skeletons (replicable templates)

**SKELETON 1 — "Bridge-and-define" paragraph**

```
[Claim announcing a parallel between [existing concept] and [new context]]. 
[Concept A] is [definition inside the new context], where [extra detail]. 
[Concept B] is [definition inside the new context]. 
[A real-world action] should be able to be represented as [composition of the two concepts]. 
The first step to [verb-ing] the [new context] is to [next formal action]:
```

- **Slot 1** (claim): declarative sentence naming two things being linked. *Shape: noun phrase + "between A and B".*
  *Fill with a different idea:* pick a familiar structure (graphs, groups, vectors) and a puzzle/game/system you want to model.
- **Slot 2** (define A): one sentence, present tense, with a "where" clause giving a concrete clue.
- **Slot 3** (define B): one sentence, present tense, parallel in length to slot 2.
- **Slot 4** (compose): a "should be able to be represented as" sentence that names the *action* in the new context as the composition.
- **Slot 5** (transition): a "The first step to … is to …" sentence that points to the next paragraph.
- **Original fill:** *"The parallel between the permutations on a set and the 15-puzzle … The permutation is an individual move, where a piece changes position. The set is every possible position … A valid scramble should be able to be represented as a composition of permutations … The first step to mathematically defining the 15-puzzle is to decide upon a valid set of positions:"*
- **Demonstration fill (different idea):** *"The parallel between a graph and the London Underground map becomes clear quickly. The graph is a collection of nodes, where each station is a node. The edge is a direct rail connection between two nodes. A valid journey should be able to be represented as a path through the graph (an ordered list of edges). The first step to mathematically defining the network is to decide upon a valid set of stations."*

**SKELETON 2 — "Formal object + visual" paragraph**

```
[Formal object, displayed as a set/list/equation].


[This object] is represented on the [concrete instance] below:


[ASCII or labelled diagram of the instance, mirroring the indexing of the object].
```

- **Slot 1** (formal display): a single line of notation, centred or set off.
- **Slot 2** (warrant sentence): "This [object] is represented on the [instance] below:" — present tense, signposting.
- **Slot 3** (visual): a grid/list that uses the same indices as the formal object, in the same order.
- **Original fill:** the set P = {1…16} followed by the 4×4 grid numbered 1–16.
- **Demonstration fill (different idea):** *"V = {A, B, C, D, E, F, G, H}" displayed, then the claim "This set of vertices is represented on the chessboard below:", then an 8-square row labelled A–H."*

**SKELETON 3 — "Anomaly → distinction → unpack" paragraph**

```
There are only [N–1] [items] on the [instance], but there are [N] [slots], hence the [Nth] [slot] is shown. 
It is important to note the distinction between a(n) [item] and a(n) [slot]. 
[Any given] [slot] on the [instance] may include any of the [items], or have no [item]. 
Since the difference between a(n) [item] [continues into a consequence] …
```

- **Slot 1** (cause-justification): "There are only X … but there are Y, hence …" — explains the visual anomaly in one sentence.
- **Slot 2** (signpost): "It is important to note the distinction between … and …" — flags the conceptual move the next sentence will make.
- **Slot 3** (unpack): one sentence giving the exhaustive case ("any of … or have no …").
- **Slot 4** (consequence, cut-off in source): "Since the difference between …" — opens an implication the next paragraph will close.
- **Original fill:** *"There are only 15 tiles on the puzzle, but there are 16 positions, hence the 16-th position is shown. It is important to note the distinction between a tile and a position. Any given position on the puzzle may include any of the tiles, or have no tile."*
- **Demonstration fill (different idea):** *"There are only 7 notes in a scale, but there are 8 beats in the bar, hence the 8th beat is shown as a rest. It is important to note the distinction between a note and a beat. Any given beat on the bar may include any of the notes, or have no note. Since the difference between a note …"*

---

## Express-Idea Vocabulary

**Sequencing / procedural**
- *"The first step to mathematically defining"* — announces the next move; signals that a build is about to happen.

**Cause / consequence**
- *"hence the 16-th position is shown"* — "hence" closes the cause–effect gap created by the count mismatch.

**Definition / specification**
- *"The permutation is an individual move"* — "is" in the present tense as the standard definitional copula.
- *"The set is every possible position"* — parallel "is" construction to keep both definitions rhythmically matched.
- *"should be able to be represented as"* — modal phrase that turns a definition into a claim about expressiveness.

**Signposting / conceptual flag**
- *"It is important to note the distinction between a tile and a position"* — the canonical phrase for pausing to introduce a load-bearing distinction.

**Exhaustive specification**
- *"may include any of the tiles, or have no tile"* — "any … or have no …" template for case-exhaustive unpacking.

**Bridging / topic claim**
- *"The parallel between the permutations on a set and the 15-puzzle"* — "The parallel between X and Y" as a one-sentence way to announce a mapping.

---

## How to Explain an Idea (replication steps)

The section uses a **bridge-then-formalise pattern**: existing mathematical object → mapping claim → dual definition in the new context → composed action → formal display → visual instantiation → anomaly resolution via a conceptual distinction. To replicate it on a new idea:

1. **Pick two things** — one already-known mathematical structure (group, graph, vector, sequence …) and one real-world object or game you want to model.
2. **Write the claim sentence** in the form *"The parallel between [structure] and [object] become(s) clear quickly."* This promises the bridge and earns the reader's patience.
3. **Define side A** of the bridge *inside the new context* in one short sentence, adding a "where" clause that grounds it concretely.
4. **Define side B** with a parallel-length sentence so the pair reads as a matched pair, not a hierarchy.
5. **Compose them** in a "should be able to be represented as" sentence that names the *real action* in the object as the composed operation.
6. **Signal the next formal step** with "The first step to [verb-ing] the [object] is to [next action]:" — this is the hand-off to your formal display.
7. **Display the formal object** on its own line: a set, a list, an equation, a tuple of tuples.
8. **Instantiate it visually** with a labelled diagram whose indices match the formal object in order. Mismatch between object and diagram is *expected* — it sets up the next move.
9. **Justify the mismatch** in a "There are only X … but there are Y, hence …" sentence.
10. **Flag the conceptual distinction** the mismatch exposed with "It is important to note the distinction between a(n) X and a(n) Y."
11. **Unpack the distinction exhaustively** in one "may include any of the X, or have no X" sentence so the reader has every case before you close the section with the downstream consequence.
