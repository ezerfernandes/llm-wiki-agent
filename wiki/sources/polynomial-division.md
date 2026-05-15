---
title: "Polynomial Division"
type: source
tags: [math, polynomials]
date: 2026-05-10
source_file: raw/polynomials/polynomial-division.md
---

## Summary
Let \\(P(x)\\) and \\(D(x)\\) be [[polynomials|polynomials]] in \\(\mathbb{R}[x]\\) with \\(D(x) \neq 0\\). The division algorithm asserts the existence of unique polynomials \\(Q(x)\\) and \\(R(x)\\) in \\(\mathbb{R}[x]\\) such that:

## Key Claims
- **The division algorithm** — Let \\(P(x)\\) and \\(D(x)\\) be [[polynomials|polynomials]] in \\(\mathbb{R}[x]\\) with \\(D(x) \neq 0\\).
- **Properties of polynomial division** — The division algorithm gives rise to several properties that follow directly from the uniqueness of the quotient and the remainder, or from the behaviour of the degree under polynomial operations.
- **Polynomial long division** — The long division algorithm involves repeatedly dividing the leading term of the current remainder by the leading term of \\(D(x)\\), subtracting the resulting product, and continuing this process until the degree of the remainder is less…
- **Example 1** — Consider the polynomials \\(P(x) = x^3 + 2x^2 - x - 2\\) and \\(D(x) = x - 1\\).
- **Example 2** — The following example illustrates a case where the division is not exact: the remainder \\(R(x)\\) is a nonzero polynomial whose degree is strictly less than \\(\deg D(x)\\).
- **The remainder theorem and the factor theorem** — The division algorithm leads to a result that connects polynomial division with the evaluation of a polynomial at a specific point.
- **Example 3** — As an application of the remainder theorem, consider the polynomial:
- **Rational functions and polynomial division** — When the division of two polynomials is performed without separating the remainder, the result is represented as a [[RationalFunctions|rational function]] where \\(D(x) \neq 0\\):
- **Polynomial division and the GCD** — Polynomial division is the basic operation underlying the computation of the greatest common divisor of two polynomials.

## Key Quotes
> Source page: algebrica.org — see `source_file`.

## Connections
- [[polynomials|Polynomials]] — polynomials
- [[integers|Integers]] — integers
- [[rings|Rings]] — ring
- [[fields|Fields]] — field
- [[SyntheticDivision]] — synthetic division method
- [[roots-of-a-polynomial|RootsOfAPolynomial]] — roots
- [[RationalFunctions]] — rational function
- [[partial-fraction-decomposition|PartialFractionDecomposition]] — partial fraction decomposition

## Contradictions
None.
