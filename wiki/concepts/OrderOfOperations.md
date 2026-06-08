---
title: "Order of Operations"
type: concept
tags: [math, prealgebra, algebra, arithmetic]
sources: [prealgebra-2e-ch02-language-of-algebra]
last_updated: 2026-06-07
---

# Order of Operations

The **order of operations** is the agreed-upon convention for the sequence in which the operations in an [[AlgebraicExpression|expression]] are carried out, so that everyone simplifying the same expression arrives at the same value. Without it, `2 + 3 · 4` could be read as `5 · 4 = 20` or `2 + 12 = 14`; the convention fixes the answer at 14. OpenStax [[Prealgebra]] 2e (Chapter 2, [[prealgebra-2e-ch02-language-of-algebra]]) introduces it in section 2.1 and relies on it throughout the rest of the book.

The rule is usually remembered by the acronym **PEMDAS** — *Please Excuse My Dear Aunt Sally*:

1. **P**arentheses (and other grouping symbols — brackets `[ ]`, braces `{ }`): simplify what is inside, **innermost grouping first**.
2. **E**xponents: simplify all powers next.
3. **M**ultiplication and **D**ivision: perform them **left to right**, in the order they appear.
4. **A**ddition and **S**ubtraction: perform them **left to right**, in the order they appear.

The most common misconception is that multiplication always comes before division (and addition before subtraction). It does not. Multiplication and division have **equal priority** and are done left to right; likewise addition and subtraction. In `12 ÷ 2 · 3`, you divide first because it appears first, giving `6 · 3 = 18`, not `12 ÷ 6 = 2`. The "MD" and "AS" pairs in PEMDAS are tie-broken by left-to-right reading, not by the letter order.

This convention is what makes "**evaluate** the expression" and "**simplify** the expression" well-defined operations in [[AlgebraicExpression|algebra]]. When you evaluate, you first substitute the given value for each [[Variable|variable]] and then apply these four steps. A frequent slip is mishandling exponents: in `2x²` the exponent applies only to `x` (step 2 before the multiplication of step 3), so `2x²` at `x = 3` is `2 · 9 = 18`, whereas `(2x)²` groups first and gives `6² = 36`.

## Connections
- [[AlgebraicExpression]] — what the order of operations is applied to.
- [[Variable]] — substituted before the operations are carried out when evaluating.
- [[Exponent]] — exponents are step 2 of the order.
- [[Equation]] — simplifying both sides uses the order of operations.
- [[prealgebra-2e-ch02-language-of-algebra]] — source (Ch 2.1).
