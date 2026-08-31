# Idea Flow Notes: mathematics_7_november2016_6jvDzQbdmBzKpwM1 — Note that by the chain rule, d cos

## Paragraph Flow (move by move)

**Paragraph 1**
- S1 — *Procedure + result* (tool application): "By the chain rule, d cos θ/dt = d cos θ/dD · dD/dt = (−v_h cos θ − v_r) d cos θ/dD." — invokes a named rule, then computes a derivative form. Hands the reader to S2 because the substitution is *the next logical use* of this derivative expression.
- S2 — *Transition / instruction*: "Substituting this in," — tells the reader an operation is about to happen. Hands to S3 by cause (the substitution is performed next).
- S3 — *Result / unpack* (numbered equation): "v_h cos²θ − v_h = D(−v_h cos θ − v_r) d cos θ/dD (6)" — produces the labelled consequence of the substitution. Hands to Paragraph 2 by *new instance*: an equation now sits on the page needing identification.

**Paragraph 2**
- S1 — *Classification / verdict*: "This is now a first-order separable differential equation" — names what equation (6) IS. Hands to S2 by consequence: a named class dictates a method (rearrange for separation).
- S2 — *Transition / procedure*: "Rearranging," — announces a manipulation step. Hands to S3 by cause.
- S3 — *Specification / result*: rearranged form isolating "1/D" on the left. Hands to Paragraph 3 because the rearranged shape *invites* the next named operation.

**Paragraph 3**
- S1 — *Procedure (transition)*: "Integrating with respect to D," — names the operation and the variable. Hands to S2 by cause (the integral must now be written out).
- S2 — *Result / unpack*: integral equation with "∫dD/D" on the left and a single compound integral on the right. Hands to Paragraph 4 by *specification*: the compound RHS now needs to be broken apart.

**Paragraph 4**
- S1 — *Decomposition / unpack*: "ln|D| + c_1 = −1/2 ∫(2v_h cos θ)/(v_h cos²θ − v_h) d cos θ − (v_r/v_h) ∫d cos θ/(v_h cos²θ − v_h)" — left side integrated, right side split into two pieces with a deliberate numerator multiplication (the "2v_h cos θ"). Hands to Paragraph 5 by cause: each piece is now individually integrable.

**Paragraph 5**
- S1 — *Result / evaluation*: "ln|D| + c_1 = −1/2 ln|v_h cos²θ − v_h| − ..." — first integral is evaluated to a logarithm; the second is deliberately left open. Hands off-page by *consequence* (continuation implied by the trailing minus).

## What This Section Does (content sequence)

The ordered moves are:
1. **Name a tool** ("By the chain rule…") → sets up a derivative needed later.
2. **Apply the tool** to produce an expression for a single derivative.
3. **Substitute** that expression into a previously derived (unstated) equation.
4. **Display the resulting equation with a label** ((6)) — labels are signposts for cross-reference.
5. **Classify the new equation** ("first-order separable…") — classification dictates method.
6. **Announce rearrangement** ("Rearranging,") — verbal cue that algebra, not new idea, is happening.
7. **Show the rearranged form**, isolating a term so the structure matches a known technique.
8. **Announce the technique** ("Integrating with respect to D,") — same verbal pattern as step 6.
9. **Write the resulting integral equation** with constant of integration on the LHS.
10. **Decompose the RHS integral** into pieces whose numerators match derivatives of denominators (preparation step).
11. **Evaluate the prepared pieces one at a time**, leaving unresolved pieces trailing.

**Why this order:** each move is *forced* by the shape of the previous one. You cannot substitute before computing the derivative; you cannot rearrange before identifying the class; you cannot integrate before isolating terms; you cannot decompose before announcing integration. A student replicating the sequence with another derivation should: **tool → apply → substitute → label → classify → rearrange → announce technique → execute → decompose → evaluate.**

## Paragraph Skeletons (replicable templates)

**SKELETON A — Tool-application paragraph**
> "By the **[named rule]**, **[computed expression = intermediate form]**. Substituting this in, **[resulting equation] (label)**."

- *Slots:* (1) a calculus rule by name; (2) the derivative computed via that rule; (3) the equation produced by substitution; (4) an equation number.
- *How to fill with a different idea:* slot 1 — pick a rule that links two derivative expressions (chain, product, quotient); slot 2 — write the equality chain showing substitution of intermediate terms; slot 3 — write the cleaned-up equation with one variable isolated; slot 4 — number it for later reference.
- *Original fill:* "By the chain rule, d cos θ/dt = d cos θ/dD · dD/dt = (−v_h cos θ − v_r) d cos θ/dD. Substituting this in, v_h cos²θ − v_h = D(−v_h cos θ − v_r) d cos θ/dD (6)."
- *Demonstration fill (different idea):* "By the product rule, d(uv)/dx = u dv/dx + v du/dx = (2x)(3x²) + (x²)(6x) = 12x³. Substituting this in, dA/dx = 12x³ + 4x (7)." (area-of-rectangle derivation)

**SKELETON B — Classification + manipulation paragraph**
> "This is now a **[class of equation]**. **[Transition verb]-ing,** **[rearranged form isolating target term]**."

- *Slots:* (1) the equation class by name; (2) an -ing verb announcing pure algebra; (3) the rearranged equation.
- *How to fill with a different idea:* slot 1 — name the class in one noun ("homogeneous", "linear", "exact"); slot 2 — use a gerund that signals manipulation not insight ("Rearranging", "Dividing through", "Factoring"); slot 3 — show the manipulated form with one key term on one side.
- *Original fill:* "This is now a first-order separable differential equation in D and cos θ. Rearranging, 1/D = (−v_h cos θ − v_r)/(v_h cos²θ − v_h) · d cos θ/dD."
- *Demonstration fill (different idea):* "This is now a linear first-order differential equation in y and x. Integrating factor, μ(x) = e^∫(1/x)dx = x. Multiplying through, x dy/dx + y = 2x²."

**SKELETON C — Operation announcement + integral setup paragraph**
> "**[Operation] with respect to [variable],** **[integral equation with constant on left]**."

- *Slots:* (1) operation name in -ing form; (2) the variable of integration; (3) the integral form with constant of integration on the LHS.
- *How to fill with a different idea:* slot 1 — pick the operation your shape invites; slot 2 — name the variable you integrate "with respect to"; slot 3 — write ∫d[var]/[var] on the left = compound integral on the right.
- *Original fill:* "Integrating with respect to D, ∫dD/D = ∫(−v_h cos θ − v_r)/(v_h cos²θ − v_h) d cos θ. ln|D| + c_1 = …"
- *Demonstration fill:* "Integrating with respect to t, ∫dt/t = ∫(2/(1+t)) dt. ln|t| + c = 2 ln|1+t| + c₂."

**SKELETON D — Integral decomposition paragraph**
> "[evaluated left] = **[coefficient] ∫[prepared numerator]/[original denominator] d[var]** − **[coefficient] ∫d[var]/[original denominator]**"

- *Slots:* (1) the already-integrated LHS; (2) one piece written with a *prepared* numerator (a derivative of the denominator); (3) the leftover piece; (4) one shared denominator across both pieces.
- *How to fill with a different idea:* keep the denominator identical across both integrals; force one numerator to be a constant multiple of the denominator's derivative so that piece becomes a log.
- *Original fill:* "ln|D| + c_1 = −1/2 ∫(2v_h cos θ)/(v_h cos²θ − v_h) d cos θ − (v_r/v_h) ∫d cos θ/(v_h cos²θ − v_h)"
- *Demonstration fill:* "ln|y| + c = ∫(2x)/(x² + 1) dx − 3 ∫dx/(x² + 1). ln|y| + c = ln|x² + 1| − 3 arctan x."

## Express-Idea Vocabulary

- **Tool announcement / sequencing:** "By the chain rule" — anchors the move in a named rule rather than ad hoc algebra.
- **Continuation transition:** "Substituting this in" — short -ing phrase telling the reader an operation follows.
- **Classification / verdict:** "This is now a first-order separable" — names the shape; the verb "is now" frames the previous equation as freshly re-identified.
- **Manipulation announcement:** "Rearranging," — gerund cue that *only* algebraic form is changing.
- **Operation announcement:** "Integrating with respect to D" — gerund + "with respect to" + variable, the standard template for triggering an integral.
- **Implicit specification via labels:** "(6)" — equation tags act as referential anchors for later substitution or citation.
- **Decomposition cue:** the silent split of one integral into a "−1/2 ∫…" minus "−(v_r/v_h) ∫…" pair — no connective word, just the minus sign itself doing the rhetorical job of "split into two cases".
- **Trailing continuation:** the closing "− …" of the final line — em-dash / ellipsis leaving a hook for the next section.

## How to Explain an Idea (replication steps)

This section uses the pattern: **invoke-rule → substitute → label → classify → rearrange → announce-technique → execute → decompose → evaluate**. It is a *worked-derivation* pattern, not a definitional or comparative one. Each step is justified by the *shape* left behind by the previous step.

To explain any new derivable result with the same pattern:
1. **Open with "By the [named rule]…"** and write the equality chain that produces a useful intermediate derivative.
2. **Add "Substituting this in,"** as a one-clause bridge; immediately write the resulting equation and **give it a number in parentheses**.
3. **Begin the next paragraph with "This is now a [class of equation]."** — name the class with one precise noun phrase so the reader knows which toolkit applies.
4. **Follow with a one-word gerund transition** ("Rearranging", "Dividing through", "Completing the square") and show the rewritten form isolating a target term.
5. **Begin the next paragraph with "[Operation]-ing with respect to [variable],"** using the operation whose preconditions your isolated form just satisfied.
6. **Write the integral equation** with a "+ c₁" on the LHS — the constant must appear here, not later.
7. **Decompose the RHS integral** into pieces that share a common denominator; multiply one numerator so it equals a constant times the derivative of that denominator.
8. **Evaluate the prepared piece to a logarithm**, and leave any unprepared piece trailing (with "− …" or "and the remaining term is …") so the derivation visibly continues rather than concluding.
