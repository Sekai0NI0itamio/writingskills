# Idea Flow Notes: mathematics_7_may2018_INu6ipizvRpfgvBI — which can be made, given a number of telephones (that is, the maximum number of edges which

## Paragraph Flow (move by move)

**Paragraph 1 — "Consider 4 vertices"**
- S1: *"Consider 4 vertices."* — Move: **setup / first instance**. Hands to next by naming a count the reader must now subject to a rule.
- S2: *"An edge connects two vertices and no vertex can have a degree of more than 1."* — Move: **constraint statement**. Hands to next by giving the exact cap (degree ≤ 1) that determines the edge count.
- S3: *"Therefore, the maximum number of connections (edges) we can have is 2."* — Move: **verdict / consequence**. Hands to next by giving the base-case number that the next paragraph will have to accommodate or contradict.

**Paragraph 2 — "Consider 5 vertices"**
- S1: *"Consider 5 vertices."* — Move: **parallel setup / +1 increment**. Hands to next by signalling "same test, one more vertex" — a deliberate contrast with the previous count.
- S2: *"Connecting 4 vertices can be done with 2 edges (as shown above), leaving 1 vertex which can't connect to another."* — Move: **evidence by reference + leftover identification**. Hands to next by reusing the prior verdict *and* naming the unmatchable remainder, so the reader can predict the answer.
- S3: *"Therefore, the number of connections we can have is also 2."* — Move: **verdict (with the connector "also" flagging continuity)**. Hands to next by showing that the count did not rise, prompting the test of a further count.

**Paragraph 3 — "Consider 6 vertices"**
- S1: *"Consider 6 vertices."* — Move: **parallel setup / next increment**. Hands to next by escalating the test to an even count where a new outcome is expected.
- S2: *"Connecting 6 vertices can be done with 3 edges, leaving no vertices.."* — Move: **unpack / pairing shown explicitly**. Hands to next by completing the pairing and leaving no remainder — the reader can now verify the count.
- S3: *"Therefore, the number of connections we can have is 3."* — Move: **verdict / pattern confirmation**. Hands to next (citation line) by closing the case ladder with the largest count shown.

**Paragraph 4 — citation line**
- *"IB Maths Resources from British International School Phuket…"* — Move: **source attribution**. No further content hand-off required.

## What This Section Does (content sequence)

This is a **worked-examples ladder**: it tests a rule by incrementing a single variable (vertex count) and recording the verdict each time.

1. **Smallest meaningful instance first** — because you need a base case before you can compare.
2. **Constraint stated up front** — because every verdict depends on the rule the reader just read.
3. **Verdict computed** — because the pattern can only be seen if each step closes with a number.
4. **Next instance (+1)** — because the reader must see whether the count rises, holds, or breaks.
5. **Reference to the previous verdict** — so the reader sees continuity rather than a fresh calculation.
6. **Identification of what is left over** — because the cap (degree ≤ 1) is exposed via the unmatchable remainder.
7. **New verdict** — because each step must terminate in a fresh number to build the sequence 2, 2, 3…
8. **Repeat until a trend is visible** — because induction-by-example only works if the reader has seen enough rungs.

A student replicating this on a different topic would: pick the simplest valid case, state the governing rule, derive the value, then walk the input up while explicitly leaning on each prior result.

## Paragraph Skeletons (replicable templates)

**Skeleton A — Base-case paragraph (first rung)**
SKELETON: "Consider [n] [units]. [Constraint governing the system]. Therefore, the [measured quantity] [we] can have is [result]."

1. *Slots:* (i) command-verb imperative opening naming a count; (ii) one-sentence rule the reader must hold in mind; (iii) "Therefore,"-led verdict naming the quantity and the number.
2. *Fill it differently:* slot 1 — choose the smallest count that makes the rule meaningful and name the units; slot 2 — write the single binding constraint in plain English; slot 3 — apply the constraint and announce the number, using "Therefore,".
3. *Original fill:* "Consider 4 vertices. An edge connects two vertices and no vertex can have a degree of more than 1. Therefore, the maximum number of connections (edges) we can have is 2."
4. *Demonstration fill (different idea):* "Consider 4 runners. Each race has 2 runners and no runner may start more than 1 race in the round. Therefore, the maximum number of races we can stage is 2."

**Skeleton B — Continuation paragraph (subsequent rung, leaning on the previous)**
SKELETON: "Consider [n+1] [units]. Connecting [n] [units] can be done with [prior result] [pairs], leaving [state of remainder]. Therefore, the [measured quantity] [we] can have is [new result]."

1. *Slots:* (i) matching "Consider …" opening one unit larger; (ii) reference back to the previous verdict inside a parenthetical "(as shown above)"; (iii) a leftover descriptor ("1 vertex which can't connect", "no vertices"); (iv) "Therefore," verdict, optionally preceded by "also" when the number is unchanged.
2. *Fill it differently:* slot 1 — repeat the same opening verb and add exactly one to your chosen unit; slot 2 — restate the previous verdict as a known fact; slot 3 — describe what the new unit(s) can or cannot pair up with; slot 4 — close with the new number.
3. *Original fill:* "Consider 5 vertices. Connecting 4 vertices can be done with 2 edges (as shown above), leaving 1 vertex which can't connect to another. Therefore, the number of connections we can have is also 2."
4. *Demonstration fill (different idea):* "Consider 5 runners. Pairing 4 runners can be done in 2 races (as shown above), leaving 1 runner who cannot be paired with another. Therefore, the number of races we can stage is also 2."

## Express-Idea Vocabulary

- **Sequencing / case marking:** *"Consider 4 vertices."* / *"Consider 5 vertices."* / *"Consider 6 vertices."* — three parallel openings that escalate by one each time.
- **Cause / consequence verdict:** *"Therefore, the maximum number of connections (edges) we can have is 2."* — and its two sister sentences using the same *"Therefore, the number of connections"* stem.
- **Continuity / no-change flag:** *"the number of connections we can have is also 2."* — the word "also" carries the logic of "same rule, same answer".
- **Reference to prior work:** *"as shown above"* inside *"can be done with 2 edges (as shown above)"* — anchors the new paragraph in the old.
- **Constraint phrasing:** *"no vertex can have a degree of more than 1"* — the rule stated in the negative to fix an upper bound.
- **Quantifier / scoping:** *"An edge connects two vertices"* — defines the unit of the system before any counting begins.

## How to Explain an Idea (replication steps)

The pattern is **incremental case analysis by worked example**: rule → smallest case → verdict → +1 case reusing prior verdict → verdict → repeat.

1. **Pick the rule that caps the system** and write it in one plain sentence (e.g. "no unit may pair more than once").
2. **Choose the smallest input where the rule actually bites** — too small and the example is trivial, too large and the base case is hidden.
3. **Open the paragraph with the imperative "Consider …"** naming that input count; this signals "worked example" to the reader.
4. **State the verdict** with a *"Therefore,"* clause naming the quantity being maximised and the number it reaches.
5. **Increment the input by exactly one** and open the next paragraph with the same *"Consider …"* construction so the parallel is visible.
6. **Lean on the previous verdict** using a parenthetical like *"(as shown above)"* — this is what turns the paragraph from a fresh calculation into a ladder.
7. **Name the remainder** ("leaving 1 vertex which can't connect") so the reader sees *why* the count did or did not rise.
8. **Close with another *"Therefore,"* verdict**, adding *"also"* when the number is unchanged so the continuity is signalled.
9. **Stop when a trend is legible** (here: 2, 2, 3) — do not keep climbing past the point where the reader can predict the next rung.
