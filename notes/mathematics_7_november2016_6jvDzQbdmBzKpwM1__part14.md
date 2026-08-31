# Idea Flow Notes: mathematics_7_november2016_6jvDzQbdmBzKpwM1 — While solving the question, a number of assumptions were made regarding the nature of the answers,

## Paragraph Flow (move by move)

### Paragraph 1
1. **Move:** Claim (Assumption)  
   **Quote:** “namely the continuity and differentiability of D(t) and cos θ(t), justified with reference to the physical context of the questions.”  
   **Hand‑off:** The sentence introduces the core assumption; the next sentence will address what follows if that assumption does not hold.

2. **Move:** Implication (Consequence)  
   **Quote:** “No other proof is offered for these assumptions, and if they are false, the results of this paper will be invalid.”  
   **Hand‑off:** The conditional clause raises a risk, prompting the following sentence to soften that risk with justification.

3. **Move:** Concession / Justification  
   **Quote:** “However, given the physical context, it is believed that these assumptions are reasonable.”  
   **Hand‑off:** The concession directly answers the concern from the previous sentence, clearing the way for a new paragraph that discusses an edge case.

### Paragraph 2
1. **Move:** Specification (Edge‑case definition)  
   **Quote:** “when θ₀ = 0° or 180°, i.e. when the human runs directly towards or away from a raptor, the method outlined is invalid.”  
   **Hand‑off:** This defines a concrete situation where the general method fails, prompting the next sentence to resolve the issue.

2. **Move:** Resolution / Explanation  
   **Quote:** “In these cases however, k is trivial to determine, and is simply v_r+v_0 k or v_r−v_0 k respectively, as correctly predicted by Equation 10, so the final results of this paper are unaffected.”  
   **Hand‑off:** Provides a straightforward calculation that directly answers the “invalid” claim and confirms overall validity.

---

## What This Section Does (content sequence)

1. **State core assumptions** – The paragraph opens with a claim of continuity/differentiability, establishing what is taken for granted.  
2. **Declare stakes if assumptions fail** – The next sentence spells out the logical consequence (invalid results), creating tension the authors must resolve.  
3. **Justify the assumptions** – A concession softens the risk by appealing to the physical context, reassuring the reader.  
4. **Identify a special case where the method is invalid** – A new paragraph introduces a limitation, specifying the condition.  
5. **Give a simple alternative for that case** – The authors show the calculation is trivial and consistent with an earlier equation.  
6. **Affirm overall robustness** – The paragraph ends by confirming that despite the exception, the final results remain valid.

**Why this order?**  
Each move builds on the previous one: assumptions → risk → mitigation → exception → resolution → overall reassurance. This creates a logical “claim‑concession‑exception‑resolution” arc that guides the reader from a high‑level premise to a concrete conclusion.

---

## Paragraph Skeletons (replicable templates)

### Skeleton A – Assumption‑Consequence‑Justification

| Slot | Content | Shape |
|------|---------|-------|
| S1 | Core assumption (what you assume) | Noun phrase + “are/is assumed” |
| S2 | Conditional consequence (what follows if false) | Conditional clause (“if X, Y will be invalid”) |
| S3 | Justification (why the assumption is plausible) | Subordinate clause (“because/ given …”) |
| S4 | Concession/reassurance (mitigation of risk) | “However, … it is believed …” |

**How to fill with a different idea**

- **S1:** Choose a mathematical property relevant to your model (e.g., “the uniform convergence of the series”).  
- **S2:** State the consequence of that property failing (e.g., “if it does not hold, the derived bound cannot be guaranteed”).  
- **S3:** Cite a contextual reason why the property is expected (e.g., “given the boundedness of the coefficients”).  
- **S4:** Offer a concession (e.g., “Nevertheless, the numerical tests suggest it is satisfied”).  

**Original fill (from text)**  

> “The continuity and differentiability of **D(t)** and **cos θ(t)** are assumed, justified with reference to the physical context of the questions. No other proof is offered for these assumptions, and **if they are false, the results of this paper will be invalid**. However, **given the physical context**, it is believed that these assumptions are reasonable.”

**Demonstration fill**  

> “The uniform convergence of the Fourier series **fₙ(x)** is assumed, justified with reference to the boundedness of the coefficients. No other proof is offered for this assumption, and **if it does not hold, the error estimate cannot be trusted**. However, **given the Dirichlet conditions**, it is believed that the series converges uniformly on the interval.”

---

### Skeleton B – Edge‑Case → Failure → Simple Resolution → Overall Validation

| Slot | Content | Shape |
|------|---------|-------|
| S1 | Specification of the edge case (condition + illustration) | “When X, i.e., …” |
| S2 | Declaration of method failure (why it fails) | “the method … is invalid (because …)” |
| S3 | Direct calculation in the edge case | “In this case, Y is trivial to determine: Z” |
| S4 | Link to an established result + overall reassurance | “as predicted by Equation N, so the final results remain unaffected.” |

**How to fill with a different idea**

- **S1:** Identify a parameter value that makes a general technique inapplicable (e.g., “when the Reynolds number equals the critical value”).  
- **S2:** Explain the underlying reason the technique breaks down (e.g., “the linearization assumes a small perturbation”).  
- **S3:** Provide the simplified formula that applies (e.g., “the drag coefficient reduces to C_D = 0.47”).  
- **S4:** Show consistency with a known formula and assert overall validity (e.g., “as given by the empirical law, so the model’s predictions stay consistent”).  

**Original fill (from text)**  

> “When **θ₀ = 0° or 180°**, i.e. when the human runs directly towards or away from a raptor, the method outlined is invalid **(as θ and hence cos θ do not change with D)**. In these cases however, **k is trivial to determine, and is simply v_r+v_0 k or v_r−v_0 k respectively**, as correctly predicted by Equation 10, so the final results of this paper are unaffected.”

**Demonstration fill**  

> “When **the discount rate r equals zero**, i.e. when there is no time preference, the standard NPV formula is invalid **(as the exponential factor becomes unity and the series diverges)**. In this case however, **the net present value reduces to the sum of the cash flows**, as directly follows from the limiting case of the formula, so the project appraisal remains consistent with the static payback method.”

---

## Express‑Idea Vocabulary

### Sequencing
- **Also** – “Also, when θ₀ = 0° or 180° …” (introduces a new paragraph or step)

### Cause / Consequence
- **if they are false, the results … will be invalid** – “if they are false, the results of this paper will be invalid.”  
- **so the final results … are unaffected** – “so the final results of this paper are unaffected.”

### Contrast / Concession
- **However, given the physical context, it is believed …** – “However, given the physical context, it is believed that these assumptions are reasonable.”  
- **In these cases however, …** – “In these cases however, k is trivial to determine …”

### Specification
- **namely** – “namely the continuity and differentiability of D(t) and cos θ(t) …”  
- **i.e.** – “i.e. when the human runs directly towards or away from a raptor”  
- **as** (introducing reason) – “as θ and hence cos θ do not change with D”

### Evidence Handling
- **justified with reference to** – “justified with reference to the physical context of the questions.”  
- **as correctly predicted by Equation 10** – “as correctly predicted by Equation 10”

### Explanation Verbs
- **are assumed** – “the continuity and differentiability … are assumed”  
- **is believed** – “it is believed that these assumptions are reasonable”  
- **is invalid** – “the method outlined is invalid”  
- **is trivial to determine** – “k is trivial to determine”  
- **is unaffected** – “the final results … are unaffected”

---

## How to Explain an Idea (replication steps)

**Pattern:** **Assumption → Consequence → Justification → Exception → Simple Resolution → Overall Validation**

**Step‑by‑step instructions**

1. **State the core assumption(s).**  
   - Choose a property that your model relies on (e.g., continuity, boundedness).  
   - Phrase it as a clear claim: “X is assumed …”

2. **Define the consequence of violation.**  
   - Write a conditional sentence: “If X does not hold, Y will be invalid.”  
   - Keep the consequence immediate and concrete.

3. **Provide a justification for the assumption.**  
   - Use a concession: “However, because of [contextual reason], X is believed to be reasonable.”  
   - Cite physical, empirical, or theoretical support.

4. **Identify a special case where the general method fails.**  
   - Begin with “When …, i.e., …” to specify the condition.  
   - Explain why the method breaks down (“the method … is invalid (as …)”).

5. **Give a direct, simplified solution for that case.**  
   - Show that the needed quantity can be computed trivially: “In this case, Z is trivial to determine: Z = …”

6. **Link the solution to an established result and confirm overall robustness.**  
   - Quote a known equation or law that predicts the simplified result.  
   - End with a reassuring statement: “Thus, the final results remain unaffected.”

7. **Review the logical flow.**  
   - Ensure each sentence answers the previous one (answer → next point, contrast → concession, etc.).  
   - Add transition words (“However”, “Also”, “In this case”) to signal the intended move.

By following these steps, any student can reproduce the “assumption‑concession‑exception‑resolution” structure demonstrated in the examined text.
