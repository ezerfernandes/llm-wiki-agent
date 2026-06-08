---
title: "Signed Number Arithmetic"
type: concept
tags: [math, prealgebra, integers, arithmetic]
sources: [prealgebra-2e-ch03-integers]
last_updated: 2026-06-07
---

# Signed Number Arithmetic

**Signed number arithmetic** is the set of rules for adding, subtracting, multiplying, and dividing [[Integer|integers]] (and signed numbers generally). It extends [[WholeNumberArithmetic|whole-number arithmetic]] to numbers that may be negative. OpenStax [[Prealgebra]] 2e develops it across Chapter 3.2–3.4 ([[prealgebra-2e-ch03-integers]]), first with a concrete **two-color counter model** (blue = +1, red = −1, where a blue–red **neutral pair** equals 0) and then as general sign rules.

## Addition (Ch 3.2)
Decide by comparing the **signs**:

- **Same signs** — add the [[AbsoluteValue|absolute values]] and **keep the common sign**. (`−5 + (−3) = −8`; with counters, all the same color, so you just count them.)
- **Different signs** — **subtract** the absolute values and take the **sign of the number with the larger absolute value**. (`−5 + 3 = −2`; some counters form neutral pairs, and you count what is left.)

## Subtraction (Ch 3.3): add the opposite
Subtraction is defined as **adding the opposite**, which reduces every subtraction to an addition handled by the rules above:

- `a − b = a + (−b)`
- `a − (−b) = a + b`

So `5 − (−3) = 5 + 3 = 8` and `−5 − 3 = −5 + (−3) = −8`. With counters, you may first add neutral pairs (which do not change the value) so that there are enough of the right color to "take away."

## Multiplication and Division (Ch 3.4)
Both operations share **one sign rule**, decided purely by whether the signs match:

- **Same signs → positive result** (positive·positive and negative·negative are both positive; likewise for quotients).
- **Different signs → negative result.**

Examples: `−9·3 = −27`, `−2(−5) = 10`, `−27 ÷ 3 = −9`, `−100 ÷ (−4) = 25`. Multiplication is repeated addition (`a·b` means "add `a`, `b` times"), and division is its inverse (`15 ÷ 3 = 5` because `5·3 = 15`).

**Multiplication / division by −1 gives the opposite:**
- `−1·a = −a` (e.g. `−1·7 = −7`, `−1(−11) = 11`)
- `a ÷ (−1) = −a`

## Exponents and order of operations
Watch the base when raising negatives to powers: `(−2)⁴ = 16` (the base is `−2`), but `−2⁴ = −16` (the opposite of `2⁴`). Multi-operation expressions follow the standard [[OrderOfOperations|order of operations]] — exponents, then multiply/divide left to right, then add/subtract left to right — now with signed results at each step.

## Connections
- [[Integer]] — the numbers these operations act on.
- [[AbsoluteValue]] — the add/subtract rules are phrased in terms of absolute values.
- [[NumberLine]] — addition can be modeled as moves left/right.
- [[WholeNumberArithmetic]] — the operation vocabulary (sum, difference, product, quotient) and algorithms it extends.
- [[OrderOfOperations]] — governs multi-operation signed expressions.
- [[DivisionPropertyOfEquality]] — uses these sign rules to solve `ax = b`.
- [[prealgebra-2e-ch03-integers]] — source (Ch 3.2–3.4).
