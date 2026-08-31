# Idea Flow Notes: mathematics_7_may2018_INu6ipizvRpfgvBI — However, this solution would be a waste of time and would also not give an exact formula which

## Paragraph Flow (move by move)

**Paragraph 1**
1. "can be used to get the number of combinations for any integer n." — Move: context (acknowledges a known method exists). Hand-off: sets up a contrast with the chosen approach.
2. "What will be done instead is an analysis of the problem to see a pattern as n is increased." — Move: transition/claim (pivots to the chosen method). Hand-off: signals that the section will build understanding incrementally rather than stating a formula directly.

**Paragraph 2**
1. "Consider 2 people (A and B) who each have a telephone." — Move: example (introduces the base case). Hand-off: anchors the reader with the simplest possible scenario.
2. "We know that there can be 2 combinations for this case: either they are connected or they are not." — Move: claim/evidence (states the count and the binary logic). Hand-off: establishes the two-state reasoning that will be reused for larger cases.

**Paragraph 3**
1. "Consider 3 people (A, B and C) who each have a telephone." — Move: setup (extends the base case by one element). Hand-off: introduces the new variable C that must be accounted for.
2. "Firstly, we know that there must be combinations included where a person isn't connected. Let this be person C. So A and B have a combination: 2 (either they are connected or they are not)." — Move: evidence/unpack (isolates the sub-case where C is absent). Hand-off: provides the first component of the total count.
3. "Now consider the situation where C is connected to someone. C will have a choice between 2 people to connect to." — Move: new instance (introduces the second sub-case). Hand-off: sets up the multiplicative reasoning that follows.
4. "Then when the person is connected to that one person, the other disconnected person will have only 1 connection combination: they must remain disconnected." — Move: mechanism (explains the constraint on the remaining person). Hand-off: supplies the second factor for the Product Principle.
5. "Therefore, we multiply the values of 2 (from the choices of C) and 1 to make 2. This is known as the Product Principle (AND rule); we must say that C connects to someone AND the other person connects to someone." — Move: definition/mechanism (names and applies the Product Principle). Hand-off: produces the count for the "C connected" sub-case, which must now be combined with the previous sub-case.
6. "Then we must add this multiplied value with the number of ways A and B can connect. 2 + 2 = 4. This is known as the Addition Principle (OR rule)." — Move: definition/mechanism (names and applies the Addition Principle). Hand-off: combines sub-cases into a total.
7. "We must say that A and B are connected with C disconnected OR C is connected AND the other person is connected." — Move: specification (states the logical disjunction explicitly). Hand-off: justifies why addition is the correct operation before the verdict.
8. "Therefore, there are 4 ways that 3 telephones can connect to each other." — Move: verdict (states the final count). Hand-off: completes the n=3 case and prepares the reader for the n=4 extension.

**Paragraph 4**
1. "Consider 4 people (A, B, C and D) who each have a telephone." — Move: setup (extends by one more element). Hand-off: mirrors the structure of the n=3 paragraph.
2. "Using the same process as in the previous example with 3 people, consider the situation where D isn't connected to anyone. There are 4 ways that A, B and C can connect to each other." — Move: evidence/transition (reuses the prior result). Hand-off: provides the first sub-case count by direct reference to the previous paragraph.
3. "Now consider the situation where D is connected to another person. There are 3 people for D to choose from." — Move: new instance (introduces the second sub-case). Hand-off: supplies the number of choices for D.
4. "When D is connected to someone else, there are 2 other people who are not connected. They can connect 2 ways (as seen above)." — Move: evidence/mechanism (identifies the remaining people and reuses the known result). Hand-off: provides the second factor for multiplication.
5. "Therefore, applying the Product Principle and the Addition Principle: 4 + 3(2) = 4 + 6 = 10. This is, indeed, the correct number of ways in which 4 telephones can connect to each other." — Move: mechanism/verdict (combines principles and states the result). Hand-off: confirms the pattern holds and leads into the generalization.

**Paragraph 5**
1. "Following the examples above, a general solution for n telephones will be: the combination of n − 1 telephones + the product of (n − 1) telephones and the combination of n − 2 telephones, where the combination of 0 and 1 telephones is 1." — Move: claim/definition (states the recursive formula). Hand-off: abstracts the observed pattern into a general rule.
2. "To illustrate this, a recursive Python program which calculates the number of combinations is shown below:" — Move: transition/example (introduces the code illustration). Hand-off: moves from abstract formula to concrete implementation.
3. The code block `def T(n): if n == 0: return 1 else: return T(n-1) + (n-1) * T(n-2)` — Move: mechanism/example (implements the formula). Hand-off: demonstrates the formula in code, then invites scrutiny of its efficiency.

**Paragraph 6**
1. "This code has a minor efficiency error: it recursively invokes the function T twice (once in T(n − 1) and another in T(n − 2))." — Move: problem identification (flags a flaw). Hand-off: creates a need for a solution.
2. "A solution to this issue is shown below:" — Move: transition (signals the fix). Hand-off: leads into the improved implementation.
3. The improved code block — Move: mechanism/example (provides the optimized version). Hand-off: concludes the section with a working implementation.

## What This Section Does (content sequence)

1. **Approach statement** — declares that the section will analyze the pattern as n increases rather than derive a closed-form formula; this sets the reader's expectation for an incremental, example-driven method.
2. **Base case (n=2)** — establishes the simplest scenario with a direct count and binary logic; this anchors the reasoning so that every later case has a known starting point.
3. **Case n=3 with sub-case decomposition** — splits the problem into "C disconnected" and "C connected" sub-cases, applies the Product Principle and Addition Principle, and states the total; this teaches the decomposition method that will be reused.
4. **Case n=4 reusing the same decomposition** — applies the identical splitting strategy to a larger case, referencing the n=3 result; this demonstrates scalability and reinforces the pattern before generalization.
5. **General recursive formula and Python implementation** — abstracts the observed pattern into a recurrence relation and implements it in code; this moves from concrete examples to a reusable rule.
6. **Efficiency critique and optimized code** — identifies a flaw in the naive recursion and provides an improved version; this completes the analysis by addressing a practical limitation.

The order works because each case builds on the previous one: the reader sees the method work twice at small scales before encountering the abstract formula, so the generalization feels motivated rather than asserted. Another student replicating this sequence would start with the simplest non-trivial case, decompose it into mutually exclusive sub-cases, name the counting principles used, extend to the next case reusing the same decomposition, then generalize.

## Paragraph Skeletons (replicable templates)

**SKELETON 1 — Base case setup**
"Consider [number] people ([labels]) who each have a [item]. We know that there can be [number] combinations for this case: either they are [state A] or they are [state B]."

1. Slots: `[number]` = integer (cardinal); `[labels]` = comma-separated person labels; `[item]` = singular noun; `[number]` = integer; `[state A]` / `[state B]` = binary complementary states.
2. To fill differently: pick the simplest non-trivial scenario for your topic, name the agents, state the count, and give the two mutually exclusive outcomes. Use past-tense observation with one concrete detail.
3. Original: "Consider 2 people (A and B) who each have a telephone. We know that there can be 2 combinations for this case: either they are connected or they are not."
4. Different fill: "Consider 3 light switches (S1, S2, S3) that each have two positions. We know that there can be 8 combinations for this case: either the circuit is open or it is closed."

**SKELETON 2 — Sub-case decomposition**
"Consider the situation where [new element] isn't connected to anyone. There are [previous result] ways that [previous elements] can connect to each other. Now consider the situation where [new element] is connected to another person. There are [n−1] people for [new element] to choose from."

1. Slots: `[new element]` = a single label; `[previous result]` = number (verbatim from prior case); `[previous elements]` = comma-separated labels; `[n−1]` = integer expression; `[new element]` = same label as first slot.
2. To fill differently: introduce the next increment to your system, state the count carried over from the prior case when the new element is inactive, then state how many options the new element has when active. Use "consider" to frame each sub-case.
3. Original: "Consider the situation where D isn't connected to anyone. There are 4 ways that A, B and C can connect to each other. Now consider the situation where D is connected to another person. There are 3 people for D to choose from."
4. Different fill: "Consider the situation where shelf S4 is empty. There are 8 arrangements for shelves S1, S2, and S3. Now consider the situation where S4 holds a book. There are 3 shelves for S4 to be placed on."

**SKELETON 3 — Principle application and verdict**
"Therefore, applying the [Principle 1] and the [Principle 2]: [calculation]. This is, indeed, the correct number of ways in which [n] [items] can connect to each other."

1. Slots: `[Principle 1]` = named counting principle; `[Principle 2]` = named counting principle; `[calculation]` = arithmetic expression with intermediate steps; `[n]` = integer; `[items]` = plural noun.
2. To fill differently: after completing the arithmetic from your decomposed sub-cases, name the two principles that justified your multiplication and addition steps, state the full calculation, and declare the final count. Use "therefore" to signal the conclusion.
3. Original: "Therefore, applying the Product Principle and the Addition Principle: 4 + 3(2) = 4 + 6 = 10. This is, indeed, the correct number of ways in which 4 telephones can connect to each other."
4. Different fill: "Therefore, applying the Multiplication Rule and the Sum Rule: 6 + 4(3) = 6 + 12 = 18. This is, indeed, the correct number of ways in which 6 books can be arranged on 3 shelves."

**SKELETON 4 — Generalization with implementation**
"Following the examples above, a general solution for n [items] will be: [formula], where [base cases]. To illustrate this, a [tool] which [purpose] is shown below."

1. Slots: `[items]` = plural noun; `[formula]` = recursive or closed-form expression; `[base cases]` = clause specifying initial values; `[tool]` = implementation medium; `[purpose]` = infinitive phrase describing what the tool does.
2. To fill differently: after observing the pattern across concrete cases, state the general rule in symbols, specify the base-case values, then introduce a code or diagrammatic illustration of the rule. Use "following" to signal the move from examples to abstraction.
3. Original: "Following the examples above, a general solution for n telephones will be: the combination of n − 1 telephones + the product of (n − 1) telephones and the combination of n − 2 telephones, where the combination of 0 and 1 telephones is 1. To illustrate this, a recursive Python program which calculates the number of combinations is shown below."
4. Different fill: "Following the examples above, a general solution for n steps of a staircase will be: the sum of step n−1 and step n−2, where step 0 equals 1 and step 1 equals 1. To illustrate this, a recursive Python program which counts the climbing ways is shown below."

## Express-Idea Vocabulary

**Sequencing:**
- "Firstly" — "Firstly, we know that there must be combinations included where a person isn't connected."
- "Then" — "Then we must add this multiplied value with the number of ways A and B can connect."
- "Following the examples above" — "Following the examples above, a general solution for n telephones will be…"

**Cause / consequence:**
- "Therefore" — "Therefore, there are 4 ways that 3 telephones can connect to each other."
- "Therefore, applying" — "Therefore, applying the Product Principle and the Addition Principle: 4 + 3(2) = 4 + 6 = 10."

**Specification:**
- "We must say that" — "We must say that A and B are connected with C disconnected OR C is connected AND the other person is connected."
- "where the combination of 0 and 1 telephones is 1" — "…the combination of n − 2 telephones, where the combination of 0 and 1 telephones is 1."

**Evidence handling:**
- "as seen above" — "They can connect 2 ways (as seen above)."
- "We know that" — "We know that there can be 2 combinations for this case."

**Explanation / naming verbs:**
- "This is known as" — "This is known as the Product Principle (AND rule)."
- "This is known as" — "This is known as the Addition Principle (OR rule)."

## How to Explain an Idea (replication steps)

The pattern this section relies on is **concrete case → sub-case decomposition → principle naming → arithmetic combination → verdict → generalization**.

1. State the simplest non-trivial instance of your problem and give the direct count with its binary or mutually exclusive outcomes.
2. Add one more element to the system and split the new cases into two mutually exclusive sub-cases: the new element inactive, and the new element active.
3. For the inactive sub-case, carry over the total from the previous case unchanged.
4. For the active sub-case, count the choices the new element has, then count the ways the remaining inactive elements can be arranged by referencing the prior case's result.
5. Multiply the choices from the active sub-case using the Product Principle (AND rule) and state the principle by name.
6. Add the inactive and active sub-case totals using the Addition Principle (OR rule) and state the principle by name.
7. Declare the final count as the verdict for that case size.
8. Repeat steps 2–7 for one additional case size, explicitly referencing the prior result to show the pattern.
9. Abstract the observed recurrence into a general formula with named base cases.
10. Implement the formula in code or another representational tool, then flag one practical limitation and provide an improved version.
