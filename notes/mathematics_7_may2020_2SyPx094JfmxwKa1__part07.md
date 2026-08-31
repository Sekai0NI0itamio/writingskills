# Idea Flow Notes: mathematics_7_may2020_2SyPx094JfmxwKa1 — Substituting the integral with a definite integral,

## Paragraph Flow (move by move)

**Paragraph 1** — *Calculation chain proving b_n = 0*

- Sentence 1: **Setup of integral** — "$b_n = \int_0^1 2t \cdot \sin(n\pi t)\, dt$" — establishes the quantity to be evaluated. Hands reader forward by *defining the object* of the whole calculation.
- Sentence 2: **Unpack (antiderivative substitution)** — "= [-\pi n t \cdot \cos(n\pi t) + \sin(n\pi t)]" — applies integration by parts. Hands reader forward as the *result of evaluating* the previous setup.
- Sentence 3: **Evaluation across limits** — "= [(0 + 0) - (\pi n \cdot \cos(-\pi n) + \sin(-n\pi))] - [(-\pi n \cdot \cos(\pi n) + \sin(n\pi)) - (0 + 0)]" — substitutes bounds. Hands reader forward by *simplification*.
- Sentence 4: **Simplification to zero** — "$= \frac{2}{n\pi} \cdot 0 = 0$" — collapses trigonometric terms and delivers the verdict. Hands reader forward by *opening the next quantity* (c_n needs b_n = 0).

**Paragraph 2** — *Transition + computation of c_n*

- Sentence 1: **Bridge/claim** — "Using the relation aforementioned, the Fourier coefficients $c_n$ … can also be calculated" — *names what is about to happen* and why (it relies on b_n just shown = 0). Hands reader forward by *invoking the prior result*.
- Sentence 2: **Computation using relation** — "$c_n = \frac{a_n - b_n}{2} - i\frac{a_n + b_n}{2} = \dots = \frac{2 - 2(-1)^n}{n\pi} \cdot i$" — substitutes b_n = 0 and a_n from earlier into the bridge formula. Hands reader forward by *producing the input needed for the final synthesis*.

**Paragraph 3** — *Synthesis of the final series*

- Sentence 1: **Verdict statement** — "Therefore, the Fourier series of a periodic function $f(x) = \dots$ with a period of 2 is" — *announces the answer*. Hands reader forward by *promising two forms*.
- Sentence 2: **Dual-form presentation** — "$f(t) = \frac{1}{2} + \sum\dots \cos(n\pi t)$, or $f(t) = \sum\dots e^{i n\pi t}$, in its exponential form" — delivers both trigonometric and exponential forms. Hands reader forward by *closing the section* (nothing follows logically — this is the terminal claim).

## What This Section Does (content sequence)

This is a **method/calculation section** that moves in a fixed order:

1. **Demonstrate a key vanishing intermediate** — first show that a particular coefficient (b_n) evaluates to zero, because everything downstream needs that fact.
2. **Bridge to the next computation using explicit reference** — state that "the relation aforementioned" lets a new quantity be obtained; this signals the reader that prior results are being recycled.
3. **Compute the new quantity by substitution** — plug the known coefficient(s) into the bridge formula to get the exponential Fourier coefficients c_n.
4. **Announce the final object with "Therefore"** — state that the full Fourier series for the piecewise function has been obtained.
5. **Give the result in two equivalent forms** — present the trigonometric form and the exponential form side by side, so the reader sees both representations.

*Why this order:* each move *consumes* the result of the previous one. You cannot announce the series
