---
title: "Golden ratio/Convergence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, iterative-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Golden_ratio/Convergence
---

## Summary
The golden ratio φ is the value of the continued fraction 1 + 1/(1 + 1/(1 + ...)), equal to (1 + √5)/2 ≈ 1.61803398875. This task explores its convergence by iterating the fixed-point recursion φ_{n+1} = 1 + 1/φ_n starting from φ_0 = 1, and measuring how many iterations are required to reach a given accuracy. The key insight is that because the continued fraction's denominators are the smallest possible positive integers, the golden ratio has the slowest convergence of any continued fraction.

## Task Requirements
- Iterate the recursion φ_{n+1} = 1 + 1/φ_n with the initial value φ_0 = 1.
- Track how many iterations are needed to converge toward φ.
- Report the iteration count and/or the successive approximations until a chosen tolerance is met.

## Language Coverage
56 languages implement this task. Coverage is broad across mainstream, functional, and historical/exotic languages, including Python, C, C++, Java, Go, Julia, Common Lisp, Scheme, Perl, Raku, Fortran, and niche entries such as EDSAC order code and Onyx (wasm).

## Connections
- [[GoldenRatio]] — the mathematical constant being approximated
- [[ContinuedFraction]] — the representation that defines φ and explains its slow convergence
- [[FixedPointIteration]] — the iterative scheme φ_{n+1} = 1 + 1/φ_n used here
- [[ConvergenceRate]] — the central topic, why this recursion converges slowly
- [[NumericalMethods]] — the broader field of iterative numerical approximation

## Contradictions
- None — reference task page.
