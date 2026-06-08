---
title: "Solving Linear Equations"
type: concept
tags: [math, prealgebra, algebra, equations]
sources: [prealgebra-2e-ch08-solving-linear-equations]
last_updated: 2026-06-07
---

# Solving Linear Equations

**Solving** a [[LinearEquation|linear equation]] means finding the value of the [[Variable|variable]] that makes it a true statement — i.e. **isolating the variable** so the equation reads `x = (number)`. The method is to apply the [[PropertiesOfEquality|Properties of Equality]] (always to *both sides*) to peel away whatever is attached to the variable, working in reverse of the [[OrderOfOperations|order of operations]]. OpenStax [[Prealgebra]] 2e Chapter 8 ([[prealgebra-2e-ch08-solving-linear-equations]]) packages this into one **General Strategy** that subsumes every earlier one-step technique.

## General Strategy for Solving Linear Equations
1. **Simplify each side** as much as possible. Use the [[DistributiveProperty|Distributive Property]] to remove parentheses, then **combine like terms**.
2. **Collect all variable terms to one side** using the Addition or Subtraction Property of Equality.
3. **Collect all constant terms to the other side** using the Addition or Subtraction Property of Equality.
4. **Make the variable's coefficient equal to 1** using the Multiplication or Division Property of Equality.
5. **Check** the solution by substituting it back into the *original* equation.

**Tip (Ch 8.3):** when variables appear on both sides, make the "variable side" the one where the variable has the **larger coefficient** — this keeps you working with positive coefficients and makes the arithmetic easier. Example: `8x − 9 = 7x + 5` ⇒ subtract `7x` from both sides ⇒ `x − 9 = 5` ⇒ add 9 ⇒ `x = 14`.

## Equation types and how the strategy specializes
- **One-step, additive** — `x + a = b` or `x − a = b`: only step needed is the Addition/Subtraction Property (the original [[Equation]] method).
- **One-step, multiplicative** — `ax = b` or `x/a = b`: only the Division/Multiplication Property is needed ([[DivisionPropertyOfEquality]], [[MultiplicationPropertyOfEquality]]). A bare `−x = 2` is read as `−1·x = 2`, then divided by `−1`.
- **Multi-step, one side** — e.g. `3x − 7 − 2x − 4 = 1`: simplify first (step 1), then finish.
- **Variables on both sides** — `ax + b = cx + d`: the full five-step strategy.
- **With parentheses** — `3(n − 4) − 2n = −3`: distribute in step 1.
- **Fraction or decimal coefficients** — clear them first (below), then apply the strategy.

## Clearing fractions and decimals (Ch 8.4)
Fractional or decimal coefficients are easiest to handle by first turning the equation into an **all-integer** equivalent:
1. Find the **LCD of all the fractions** in the equation (the [[LeastCommonMultiple|least common multiple]] of the denominators).
2. **Multiply both sides** by that LCD — this *clears the fractions* (Multiplication Property of Equality). Multiply **every term** on both sides.
3. Solve the resulting integer equation with the General Strategy.

For **decimals**, do the same by multiplying both sides by the appropriate power of 10 (10, 100, 1000, …) so every coefficient becomes an integer — equivalently, rewrite each decimal as a [[Fraction|fraction]] (`0.8 = 8/10`, `0.06 = 6/100`) and clear. Example: `0.25x + 0.10(x + 4) = 2.5` ⇒ multiply by 100 ⇒ `25x + 10(x + 4) = 250`.

## Checking
A solution is verified by **substituting it into the original equation**, simplifying both sides with the [[OrderOfOperations|order of operations]], and confirming the two sides are equal. Checking against the *original* (not a rewritten) equation catches arithmetic slips made during solving.

## Connections
- [[PropertiesOfEquality]] — the four moves that power every step.
- [[Equation]] — the underlying object; one-step solving starts there.
- [[LinearEquation]] — the class of equations this strategy solves.
- [[DistributiveProperty]] — removes parentheses in step 1.
- [[LeastCommonMultiple]] — supplies the LCD that clears fractions.
- [[FractionArithmetic]], [[DecimalArithmetic]], [[SignedNumberArithmetic]] — the arithmetic done along the way.
- [[Reciprocal]] — an alternative to the Division Property for a fractional coefficient.
- [[OrderOfOperations]] — used to simplify and to check.
- [[prealgebra-2e-ch08-solving-linear-equations]] — source (Ch 8.3–8.4).
