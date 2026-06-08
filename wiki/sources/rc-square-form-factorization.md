---
title: "Square form factorization (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Square_form_factorization
---

## Summary
The task is to implement Daniel Shanks's Square Form Factorization (SquFoF), an integer factorization algorithm invented around 1975 that excels at factoring numbers between 10^10 and 10^18 on 32-bit hardware. The algorithm walks a periodic cycle of binary quadratic forms (a, b, c) with discriminant D = 4N, applying a reduction operator (rho) that amounts to computing the continued fraction of √N. The key insight is that squaring any form in an ambiguous cycle lands it in the principal cycle, so detecting a "square form" (where coefficient c is a perfect square) and then tracking the inverse-square-root form backward to a symmetry point reveals an ambiguous form whose a (or a/2) divides N.

## Task Requirements
- Implement SquFoF to factor an integer N using binary quadratic forms f(x,y) = ax² + bxy + cy² with discriminant D = b² − 4ac.
- Use floor(√N) to build the principal form (1, b, c) and iterate the rho reduction operator through the form cycle.
- Detect square forms (where c is a perfect square) at even cycle indices, then reverse-track the ambiguous cycle to its symmetry point to extract a divisor.
- Maintain a queue of small early coefficients to skip, avoiding trivial factorizations (the a = 1 or a = 2 cases).
- Run five parallel instances on N, 3N, 5N, 7N, 11N to vary the periods; report failure when N is prime or the cube of a prime (only improper squares exist).

## Language Coverage
19 languages implement this task, a moderate breadth typical of a specialized number-theory algorithm. Representative implementations include ALGOL 68, C, C++, Go, Java, Julia, Nim, Pascal, Python, Perl, Raku, REXX, and Wren.

## Connections
- [[IntegerFactorization]] — SquFoF is a dedicated factoring algorithm in this family
- [[BinaryQuadraticForm]] — the core mathematical object whose cycles drive the method
- [[ContinuedFraction]] — rho reduction is essentially the continued fraction expansion of √N
- [[EuclideanAlgorithm]] — the reduction operator is described as a variant of Euclid's algorithm
- [[NumberTheory]] — discriminants, ambiguous forms, and divisor structure underpin the approach

## Contradictions
- None — reference task page.
