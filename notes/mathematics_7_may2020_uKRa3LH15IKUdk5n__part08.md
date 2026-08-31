# Idea Flow Notes: mathematics_7_may2020_uKRa3LH15IKUdk5n — expression for f(x), the expression for f(x) can be approximated by summation of the change in y value (the

## Paragraph Flow (move by move)

**Paragraph 1 (formula statement + variable definitions)**

1. "height) of each segment of the wire." — **context** (completes a sentence carried over from a prior section, naming what is being summed). Hands to next by *anchoring the physical meaning* of the upcoming sum.
2. "This is expressed mathematically as:" — **transition/formula label** (announces an equation immediately below). Hands to next by *promising a formula that needs unpacking*.
3. `f = Σ ∆yᵢ` — **evidence/formula** (the approximate-length formula itself). Hands to next because *the symbols are not yet named*.
4. "Where ∆y is the segment's height, and n is the total number of segments." — **definition** (defines both symbols in the formula). Hands to next by *creating a need to compute ∆y*.

**Paragraph 2 (identifying and expressing the tool vector)**

1. "To find ∆y the properties of the vector T_c can be applied." — **claim** (announces that a previously defined vector is the instrument for the missing piece). Hands to next by *naming the tool that must now be characterised*.
2. "The vector T_c is the same as the vector T_x but it is the tension vector tangential to segment number c rather than point x." — **comparison/specification** (relates the new symbol to a known one, then differentiates it). Hands to next by *concluding that the relationship gives an explicit expression*.
3. "Thus T_c is:" — **transition** (links the verbal description to its symbolic form). Hands to next by *introducing the formula that must be simplified*.

**Paragraph 3 (deriving the simplified form of ∆y)**

1. "If each segment of wire is straight and considered to be 1 unit long, since tension vectors in a wire are always tangential to the wire; the tension vector at segment c is colinear with the segment number c." — **premise + mechanism** (lays down physical assumptions and the geometric consequence). Hands to next by *entitling a simplification*.
2. "Thus the height of any segment c is equal to the y component of the unit vector in the direction of T_c, which is mathematically expressed as:" — **implication/formula label** (states the geometric consequence in symbolic form). Hands to next because *the expression still has a magnitude to remove*.
3. "∆y_c = |T_c/T_c| sin α" — **evidence/formula** (the intermediate form with the magnitude ratio). Hands to next by *inviting justification for the simplification*.
4. "since:" — **transition** (signals a side-derivation). Hands to next because *a small lemma follows*.
5. "|T_c|/|T_c| = 1" — **evidence** (justifies cancelling the magnitude ratio). Hands to next by *delivering the reduced result*.
6. "∆y_c = sin α" — **verdict/formula** (the simplified final result). Hands to next by *still needing α defined*.
7. "Where α is the angle between the vector T_c and the x axis." — **definition** (names the remaining symbol). Hands to next by *reaching forward to the next case (one-unit straight wire)*.

## What This Section Does (content sequence)

This is a **mathematical derivation block**, not a method or discussion block. The ordered content moves are:

1. **Goal statement + master formula** — sets up the overall approximation (`f = Σ ∆yᵢ`).
2. **Variable definitions for the master formula** — names every symbol so the reader can read the next step.
3. **Tool identification** — picks the previously-derived object (`T_c`) that will be re-used.
4. **Tool characterisation** — relates the new vector to a known vector and writes it out.
5. **Assumption list** — fixes physical conditions (straight, unit length, tangential) needed before simplifying.
6. **Geometric consequence** — converts the conditions into a claim about the y-component.
7. **Intermediate formula** — writes the claim as a symbolic expression with a magnitude still present.
8. **Justifying lemma** — inserts a small derivation (`|T|/|T| = 1`) to justify cancellation.
9. **Reduced formula** — states the simplified final form (`∆y = sin α`).
10. **Final variable definition** — names the remaining angle.

**WHY this order:** Each move narrows the reader's focus — from whole-wire expression → single segment → vector tool → geometric conditions → reduced symbolic form. You cannot define `∆y` until the sum is on the page; you cannot express `T_c` until the reader has met `T_x`; you cannot cancel `|T_c|` until the unit-length assumption has been installed. Replicable principle: **announce → name symbols → fetch a previously-built tool → install assumptions → derive → cancel → re-state → name leftover symbols**.

## Paragraph Skeletons (replicable templates)

**Skeleton A — "Master formula + variable glossary"**
SKELETON: *"[This quantity] is expressed mathematically as: [EQUATION]. Where [symbol 1] is [definition 1], and [symbol 2] is [definition 2]."*

- Slot 1 (`[This quantity]`): a noun phrase naming what is being summed/expressed. Grammatically a singular noun phrase preceded by a definite article.
- Slot 2 (`[EQUATION]`): a one-line centred display equation using summation, product, or piecewise notation.
- Slot 3 (`[symbol]` + `[definition]`): two parallel clauses joined by "and"; each defines one symbol in plain physical terms.
- **How to fill with a new idea:** Pick a quantity you want to approximate as a sum or product (e.g. arc length, total energy, total displacement). Write the master formula using standard notation. Then in the "where" clause, define every symbol that appears in the equation using one short noun phrase each.
- **Original fill:** "This is expressed mathematically as: f = Σ ∆yᵢ. Where ∆y is the segment's height, and n is the total number of segments."
- **Demonstration fill (different idea — approximating the total drag force on an irregular surface):** "The total drag force is expressed mathematically as: F_D = Σ ∆Fᵢ. Where ∆F is the force on each strip, and n is the total number of strips."

**Skeleton B — "Tool retrieval by analogy"**
SKELETON: *"To find [target], the [properties] of [tool] can be applied. [Tool] is [similar to previously-known object] but [distinguishing feature]. Thus [tool] is: [FORMULA]."*

- Slot 1 (`[target]`): the symbol you just defined and need to evaluate.
- Slot 2 (`[tool]`): a symbol already established earlier in the paper.
- Slot 3 (`[similar…]`): the prior version of that tool, named explicitly.
- Slot 4 (`[distinguishing feature]`): a prepositional phrase ("at point …", "for segment …") that creates the new instance.
- Slot 5 (`[FORMULA]`): the explicit expression for the new instance.
- **How to fill:** Choose a quantity that was defined but not yet computed. Pick a previously-defined vector/function that has an obvious general form. Create one indexed variant (e.g. at point c instead of at point x). Write out the new formula by analogy.
- **Original fill:** "To find ∆y the properties of the vector T_c can be applied. The vector T_c is the same as the vector T_x but it is the tension vector tangential to segment number c rather than point x. Thus T_c is: [formula]."
- **Demonstration fill (different idea — shear stress at a particular node in a beam):** "To find the bending moment at a given cross-section, the properties of the internal force vector V_j can be applied. The vector V_j is the same as the vector V at the origin but it is the resultant force normal to node j rather than the origin. Thus V_j is: [formula]."

**Skeleton C — "Assumption → geometric simplification → formula"**
SKELETON: *"If [assumption 1], since [physical reason]; [geometric consequence]. Thus [result], which is mathematically expressed as: [INTERMEDIATE FORM]. since: [LEMMA]. [REDUCED FORM]. Where [leftover symbol] is [definition]."*

- Slot 1 (`[assumption]`): an "If…" conditional establishing a simplifying condition (unit length, straight, etc.).
- Slot 2 (`[physical reason]`): a "since…" clause explaining *why* the assumption lets you conclude something.
- Slot 3 (`[geometric consequence]`): a verbal claim linking the assumption to a measurable quantity.
- Slot 4 (`[INTERMEDIATE FORM]`): a symbolic expression still carrying the leftover magnitude.
- Slot 5 (`[LEMMA]`): a one-line justification (often `|X|/|X| = 1`).
- Slot 6 (`[REDUCED FORM]`): the cleaned-up expression.
- Slot 7 (`[leftover symbol]`): any symbol in the reduced form still undefined.
- **How to fill:** List one simplifying physical assumption; convert it into a geometric or vector consequence; write the consequence symbolically with the extra term visible; insert a one-line lemma that neutralises the extra term; re-state the cleaned form; finish by defining whatever remains.
- **Original fill:** "If each segment of wire is straight and considered to be 1 unit long, since tension vectors in a wire are always tangential to the wire; the tension vector at segment c is colinear with the segment number c. Thus the height of any segment c is equal to the y component of the unit vector in the direction of T_c, which is mathematically expressed as: ∆y_c = |T_c/T_c| sin α. since: |T_c|/|T_c| = 1. ∆y_c = sin α. Where α is the angle between the vector T_c and the x axis."
- **Demonstration fill (different idea — slope of a straight road segment):** "If each road segment is straight and considered to be 1 unit long, since gradient vectors are always aligned with the road; the gradient vector at segment c is colinear with the segment number c. Thus the vertical rise of segment c is equal to the y component of the unit vector in the direction of G_c, which is mathematically expressed as: ∆h_c = |G_c/G_c| sin β. since: |G_c|/|G_c| = 1. ∆h_c = sin β. Where β is the angle between the gradient vector and the horizontal axis."

## Express-Idea Vocabulary

- **Sequencing / formula-introducers:** "This is expressed mathematically as" (used to **precede every display equation**); "Thus" (used at the **head of a sentence that delivers a result**); "since" (used to **flag a side-justification** that supports a simplification).
- **Cause / consequence:** "Thus" carries the bulk of causal work — "Thus the height of any segment c is equal to…" and "Thus T_c is:"; "since" supplies the reason — "since tension vectors in a wire are always tangential".
- **Contrast / distinction:** "but" — "the same as the vector T_x but it is the tension vector tangential to segment number c"; "rather than" — "tangential to segment number c rather than point x" (creates the new indexed instance by negation).
- **Specification / narrowing:** "rather than" reappears as a precision device; "If each segment of wire is straight and considered to be 1 unit long" — a conditional that installs a narrowing assumption.
- **Evidence handling:** "since" introduces physical reasoning as evidence for a geometric claim; "|T_c|/|T_c| = 1" presented as a standalone lemma.
- **Explanation verbs:** "is the same as" (drawing analogy between two vectors); "can be applied" (justifying why a previously-built tool is reused — "the properties of the vector T_c can be applied"); "is equal to" (converting a geometric claim into an equality — "the height of any segment c is equal to the y component…"); "is mathematically expressed as" (the official label that turns a verbal claim into a display equation).

## How to Explain an Idea (replication steps)

This section relies on the pattern **definition → tool-retrieval → condition-installation → simplification → lemma → result → leftover-definition**. It is a *worked derivation*, not an authority-application or comparison.

Step-by-step replication for a NEW idea:

1. **State the goal in words.** Write one sentence declaring what the section will derive ("This is expressed mathematically as: …" line).
2. **Write the master formula.** Put it in a centred display line using summation/product notation if possible.
3. **Define every symbol in the master formula.** Use a "Where [symbol] is [plain-English definition], and [symbol] is [plain-English definition]" clause so the reader can read the next step without guessing.
4. **Identify what still needs computing and fetch the tool.** Open the next paragraph with "To find [target], the [properties] of [previously-derived object] can be applied." This forces reuse of earlier work.
5. **Relate the new tool to its known ancestor.** Use "The [tool] is the same as [ancestor] but [distinguishing feature]" — the "but" + "rather than" pair is what creates the new indexed instance.
6. **Write the new formula explicitly.** Follow with "Thus [tool] is: [formula]."
7. **Install the simplifying assumptions.** Use "If [condition], since [reason];" — at least one assumption and one physical reason.
8. **State the geometric consequence of the assumptions.** One sentence claiming what now follows ("Thus the [measurable] of [object] is equal to the [component] of the [unit vector] in the direction of [tool]").
9. **Write the intermediate symbolic form** containing the extra magnitude term.
10. **Insert a justifying lemma** ("since: |X|/|X| = 1" or equivalent) on its own line.
11. **Re-state the reduced form** without the cancelled term.
12. **Define any leftover symbol** with a closing "Where [symbol] is [definition]" sentence before carrying the reader to the next case.
