---
title: "Continued fraction (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Continued_fraction
---

## Summary
The task is to write a program that evaluates a generalized continued fraction of the form a0 + b1/(a1 + b2/(a2 + ...)) and prints its real-number approximation. The key insight is that such fractions converge quickly to a real value when computed from the bottom up (or iteratively from the top), so truncating at enough terms yields an accurate result. It must be tested by reproducing the square root of 2, Napier's constant (e), and Pi using the given sequences of a-terms and b-numerators.

## Task Requirements
- Implement a routine that generates and evaluates a continued fraction given coefficient sequences a_N and b_N.
- Print a real (decimal) representation of the resulting value.
- Compute sqrt(2): a0 = 1, a_N = 2, b_N = 1.
- Compute e (Napier's constant): a0 = 2, a_N = N, b_1 = 1, b_N = N-1.
- Compute Pi: a0 = 3, a_N = 6, b_N = (2N-1)^2.

## Language Coverage
81 languages implement this task, spanning systems and functional languages, scripting, and math/symbolic environments. Representative implementations include C, C++, Rust, Go, Java, Haskell, OCaml, Python, Perl, Raku, Julia, and Mathematica / Wolfram Language.

## Connections
- [[ContinuedFraction]] — the mathematical object the task evaluates
- [[NumericalApproximation]] — finite truncation yields a real-valued estimate
- [[NapiersConstant]] — one of the three test values (e)
- [[SquareRootOfTwo]] — periodic continued fraction test case
- [[Pi]] — generalized continued fraction expansion test case

## Contradictions
- None — reference task page.
