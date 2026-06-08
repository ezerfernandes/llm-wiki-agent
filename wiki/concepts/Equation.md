---
title: "Equation (and Solving by Addition/Subtraction)"
type: concept
tags: [math, prealgebra, algebra]
sources: [prealgebra-2e-ch02-language-of-algebra, prealgebra-2e-ch08-solving-linear-equations]
last_updated: 2026-06-07
---

# Equation (and Solving by Addition/Subtraction)

An **equation** is two [[AlgebraicExpression|expressions]] connected by an equal sign, such as `x + 7 = 12`. The equal sign asserts that the two sides have the **same value**. This is exactly what distinguishes an equation from an expression: an expression (like `x + 7`) has no equals sign and is *evaluated* or *simplified*, while an equation (like `x + 7 = 12`) makes a claim of equality and is *solved*. OpenStax [[Prealgebra]] 2e (Chapter 2, [[prealgebra-2e-ch02-language-of-algebra]]) introduces equations in 2.1 and the first solving techniques in 2.3.

A **solution** of an equation is a value of the [[Variable|variable]] that makes the equation a **true statement** when substituted in. To *check* whether a number is a solution, replace the variable with that number, simplify both sides using the [[OrderOfOperations|order of operations]], and see whether the two sides are equal. For example, `x = 5` is a solution of `x + 7 = 12` because `5 + 7 = 12` is true, while `x = 6` is not because `6 + 7 = 13 ≠ 12`.

**Solving** an equation means finding its solution(s) by **isolating the variable** — getting the variable alone on one side. The two tools introduced here are the properties of equality, which rest on the idea that doing the *same thing to both sides* keeps an equation balanced (like keeping a scale level):

- **Subtraction Property of Equality** — for any numbers `a, b, c`: if `a = b`, then `a − c = b − c`. Use it to undo an *addition*. To solve `x + 7 = 12`, subtract 7 from both sides: `x + 7 − 7 = 12 − 7`, so `x = 5`.
- **Addition Property of Equality** — for any numbers `a, b, c`: if `a = b`, then `a + c = b + c`. Use it to undo a *subtraction*. To solve `x − 5 = 9`, add 5 to both sides: `x − 5 + 5 = 9 + 5`, so `x = 14`.

The standard procedure is therefore: (1) use the appropriate property to isolate the variable, (2) simplify both sides, and (3) **check** by substituting the result back into the original equation. These two properties handle one-step equations of the form `x + a = b` and `x − a = b`; [[prealgebra-2e-ch03-integers|Chapter 3]] adds the [[DivisionPropertyOfEquality|Division Property of Equality]] for equations like `ax = b` (and extends solving to the [[Integer|integers]]). [[prealgebra-2e-ch08-solving-linear-equations|Chapter 8]] adds the [[MultiplicationPropertyOfEquality|Multiplication Property]] and unifies all four [[PropertiesOfEquality|Properties of Equality]] into a single [[SolvingLinearEquations|General Strategy for Solving Linear Equations]] — handling multi-step equations, variables on both sides, and fraction/decimal coefficients.

Equations are often built by **translating a sentence**. The words *is, is equal to, is the same as, gives, was, will be* signal the equal sign; you translate the phrase on each side into an [[AlgebraicExpression|expression]] and join them with `=`. For instance, "the sum of a number and 3 is 11" becomes `n + 3 = 11`, which then solves to `n = 8`. This translate-then-solve pattern is how the chapter handles real-world application problems (deductibles, discounts, and the like).

## Connections
- [[AlgebraicExpression]] — the two sides of an equation; an equation joins two of them with `=`.
- [[Variable]] — what an equation is solved for.
- [[OrderOfOperations]] — used to simplify and to check both sides.
- [[PropertiesOfEquality]] — the full set of four equality properties (Ch 8).
- [[SolvingLinearEquations]] — the General Strategy that sequences them.
- [[DivisionPropertyOfEquality]] / [[MultiplicationPropertyOfEquality]] — the multiply/divide inverse pair.
- [[LinearEquation]] — the first-degree equations these methods solve.
- [[prealgebra-2e-ch02-language-of-algebra]] — source (Ch 2.3).
- [[prealgebra-2e-ch08-solving-linear-equations]] — source (Ch 8, the consolidated strategy).
