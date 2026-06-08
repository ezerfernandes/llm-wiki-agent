---
title: "Division Property of Equality"
type: concept
tags: [math, prealgebra, algebra, integers]
sources: [prealgebra-2e-ch03-integers, prealgebra-2e-ch08-solving-linear-equations]
last_updated: 2026-06-07
---

# Division Property of Equality

The **Division Property of Equality** states that dividing **both sides** of an equation by the **same nonzero number** preserves the equality:

> For numbers `a`, `b`, `c` with `c ≠ 0`: **if `a = b`, then `a/c = b/c`.**

It is introduced in OpenStax [[Prealgebra]] 2e Chapter 3.5 ([[prealgebra-2e-ch03-integers]]) and completes, for this stage, the set of equality properties used to solve one-step [[Equation|equations]]. Like the others it rests on the balance idea: doing the *same thing to both sides* keeps an equation balanced (an envelope-and-counter model — identical envelopes balanced against counters — makes this concrete, e.g. `2x = 6` splits into `x = 3`).

## Where it fits among the properties of equality
| Property | Statement (`a = b ⟹`) | Undoes |
|---|---|---|
| Addition | `a + c = b + c` | a subtraction |
| Subtraction | `a − c = b − c` | an addition |
| **Division** | `a/c = b/c`, `c ≠ 0` | a **multiplication** |

The Addition and Subtraction Properties (from [[Equation|Ch 2]]) solve `x + a = b` and `x − a = b`. The **Division Property** solves equations of the form `ax = b`, where the variable is **multiplied** by a coefficient: divide both sides by that coefficient. The requirement `c ≠ 0` matters because division by zero is undefined. Its inverse partner, the [[MultiplicationPropertyOfEquality|Multiplication Property of Equality]], solves `x/a = b`; in [[prealgebra-2e-ch08-solving-linear-equations|Chapter 8]] the two together form step 4 of the [[SolvingLinearEquations|General Strategy]] — reducing the variable's coefficient to 1 — and the full set of four [[PropertiesOfEquality|Properties of Equality]] is applied to multi-step and both-sides equations.

## Solving `ax = b` over the integers
1. Divide both sides by the coefficient of the variable.
2. Simplify both sides using [[SignedNumberArithmetic|signed-number arithmetic]] (the quotient's sign follows the same/different-signs rule).
3. **Check** by substituting the result into the original equation.

Examples: `7x = −49` → divide by 7 → `x = −7`; `−3y = 63` → divide by `−3` → `y = −21` (different signs give a negative quotient). To **check a solution** generally: substitute the value, simplify both sides, and confirm the equation is true.

These equations often come from **translating word problems** — e.g. "the product of −9 and `y` equals 108" becomes `−9y = 108`, solved by the Division Property to `y = −12`.

## Connections
- [[Equation]] — the broader concept; this adds to the addition/subtraction solving methods.
- [[SignedNumberArithmetic]] — the sign rules used when simplifying the quotient.
- [[Integer]] — the number system these equations are solved over here.
- [[Variable]] — what `ax = b` is solved for.
- [[MultiplicationPropertyOfEquality]] — the inverse partner; together they reduce a coefficient to 1.
- [[PropertiesOfEquality]] — the unified set of four properties (Ch 8).
- [[SolvingLinearEquations]] — the General Strategy that uses this in step 4.
- [[prealgebra-2e-ch03-integers]] — source (Ch 3.5).
- [[prealgebra-2e-ch08-solving-linear-equations]] — source (Ch 8.2–8.3, consolidated use).
