---
title: "Properties of Equality"
type: concept
tags: [math, prealgebra, algebra, equations]
sources: [prealgebra-2e-ch08-solving-linear-equations, prealgebra-2e-ch02-language-of-algebra, prealgebra-2e-ch03-integers]
last_updated: 2026-06-07
---

# Properties of Equality

The **Properties of Equality** are the four operations you may perform on **both sides** of an [[Equation|equation]] without changing its solution set. They all rest on one idea — an equation is like a balanced scale, so *whatever you do to one side you must do to the other* to keep it balanced. They are the engine behind [[SolvingLinearEquations|solving linear equations]]: each one **undoes** the operation that is currently attached to the [[Variable|variable]], moving the equation toward the isolated form `x = (number)`.

For all real numbers `a`, `b`, and `c`:

| Property | Statement (`a = b ⟹`) | Undoes | Used to solve |
|---|---|---|---|
| **Addition** | `a + c = b + c` | a subtraction | `x − a = b` |
| **Subtraction** | `a − c = b − c` | an addition | `x + a = b` |
| **Multiplication** | `ac = bc` | a division | `x/a = b` |
| **Division** (`c ≠ 0`) | `a/c = b/c` | a multiplication | `ax = b` |

- **Addition / Subtraction** form an inverse pair: to undo `x + 7 = 12` subtract 7 (`x = 5`); to undo `x − 5 = 9` add 5 (`x = 14`).
- **Multiplication / Division** form an inverse pair: to undo `4x = −28` divide by 4 (`x = −7`); to undo `a/−7 = −42` multiply by `−7` (`a = 294`). For a fractional coefficient, multiplying by the [[Reciprocal|reciprocal]] is the cleanest use of the Multiplication Property: `(2/3)x = 18` ⇒ multiply by `3/2` ⇒ `x = 27`.

The `c ≠ 0` restriction appears only on the **Division** Property, because dividing by zero is undefined. (You may multiply both sides by 0, but it destroys information, so it is never used in solving.)

These properties were introduced incrementally across OpenStax [[Prealgebra]] 2e: Addition and Subtraction in Chapter 2 ([[Equation]] / [[prealgebra-2e-ch02-language-of-algebra]]), Division in Chapter 3 ([[DivisionPropertyOfEquality]] / [[prealgebra-2e-ch03-integers]]), and all four are gathered and applied together in Chapter 8 ([[prealgebra-2e-ch08-solving-linear-equations]]).

## Why they preserve solutions
Each property pairs an operation with its **inverse** (see [[IdentityInverseZeroProperties]]): adding `c` and subtracting `c` cancel, as do multiplying by `c` and dividing by `c`. Applying the same invertible operation to both sides yields an **equivalent equation** — one with exactly the same solutions — so a chain of such steps cannot introduce or lose solutions (with the standard caveat of avoiding multiplication/division by 0).

## How they drive solving
In the [[SolvingLinearEquations|General Strategy]], the Addition/Subtraction Properties **collect** variable terms on one side and constants on the other (steps 2–3), and the Multiplication/Division Properties **reduce the coefficient to 1** (step 4). After any of these steps, you simplify with the [[OrderOfOperations|order of operations]] and finally **check** by substituting back into the original equation.

## Connections
- [[Equation]] — what these properties operate on; the Addition/Subtraction methods start here.
- [[SolvingLinearEquations]] — the general strategy that sequences these properties.
- [[DivisionPropertyOfEquality]] / [[MultiplicationPropertyOfEquality]] — the multiply/divide inverse pair, on their own pages.
- [[Reciprocal]] — multiplying by the reciprocal applies the Multiplication Property to clear a fractional coefficient.
- [[IdentityInverseZeroProperties]] — the inverse operations that make each property reversible.
- [[Variable]] — what the properties isolate.
- [[prealgebra-2e-ch08-solving-linear-equations]] — source (Ch 8, consolidated).
