---
title: "Polynomial long division (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, algebra, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Polynomial_long_division
---

## Summary
This task asks the programmer to implement polynomial long division: given a numerator polynomial N and a divisor polynomial D, compute the quotient q and remainder r such that N = q*D + r with the degree of r less than the degree of D. Polynomials are represented as coefficient vectors (the i-th element holds the coefficient of x^i), so multiplying by a monomial becomes a right-shift of the vector. The key insight is that the algorithm mirrors numeric long division: repeatedly cancel the leading term of N using a shifted, scaled copy of D until N's degree drops below D's.

## Task Requirements
- Represent polynomials as ordered coefficient vectors (i-th element = coefficient of x^i).
- Implement a `degree` helper returning the index of the last non-zero element (-infinity if all zero).
- Implement `polynomial_long_division(N, D)` returning the quotient and remainder vectors per the given pseudocode.
- Loop while degree(N) >= degree(D): shift D right, compute the quotient coefficient, subtract the scaled shifted divisor from N; the leftover N becomes r.
- Error handling for bad allocations or inputs is not mandatory.
- Demonstrate with the Wikipedia-derived example dividing -42 - 12x^2 + x^3 by -3 + x, yielding q = x^2 - 9x - 27 and r = -123.

## Language Coverage
54 languages implement this task, spanning systems and functional languages as well as math-oriented environments. Representative examples include C, C++, C#, Java, Python, Haskell, Common Lisp, OCaml, Fortran, Julia, Mathematica/Wolfram Language, and J.

## Connections
- [[Polynomial]] — the algebraic objects being divided
- [[LongDivision]] — the numeric algorithm this generalizes
- [[EuclideanDivision]] — the quotient-and-remainder structure N = q*D + r
- [[VectorRepresentation]] — coefficient vectors with monomial multiplication as a shift
- [[PolynomialDerivative]] — related Rosetta Code task

## Contradictions
- None — reference task page.
