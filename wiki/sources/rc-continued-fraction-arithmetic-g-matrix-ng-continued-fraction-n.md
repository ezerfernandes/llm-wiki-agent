---
title: "Continued fraction/Arithmetic/G(matrix ng, continued fraction n) (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, continued-fractions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Continued_fraction/Arithmetic/G(matrix_ng,_continued_fraction_n)
---

## Summary
This task implements Bill Gosper's algorithm for performing exact arithmetic on a single continued fraction using a "baby" 2x2 integer matrix `[[a1, a], [b1, b]]` as state. The machine alternately consumes input terms from a continued fraction N and emits output terms: it emits a term when the integer parts of a/b and a1/b1 agree, otherwise it ingests another input term. The key insight is that a single Mobius (linear fractional) transformation encoded in the matrix lets you compute expressions like (a·n + c) / (b·n + d) term-by-term without floating-point error, ulps, or epsilons.

## Task Requirements
- Maintain internal state as a 2x2 matrix and support three operations: input a term, output a term, and handle exhausted input.
- Input term t: update state to `[[a + a1*t, a1], [b + b1*t, b1]]`.
- Output term t: update state to `[[b1, b], [a1 - b1*t, a - b*t]]`.
- When input is exhausted (inject infinity): update state to `[[a1, a1], [b1, b1]]`.
- Output a term only when integer parts of a/b and a1/b1 are equal; otherwise input a term. Terminate when both b1 and b are zero.
- Demonstrate: [1;5,2] + 1/2, [3;7] + 1/2, [3;7] divided by 4.
- Using a sqrt(2) generator, compute 1/sqrt(2), then compute (1 + 1/sqrt(2)) / 2 (the first step toward the arithmetic-geometric mean).

## Language Coverage
38 languages implement this task, a solid mid-sized cross-section spanning systems, functional, and scripting languages. Representative implementations include C, C++, Rust, Go, Haskell, OCaml, Common Lisp, Python, Julia, Java, Perl, and Raku.

## Connections
- [[ContinuedFractions]] — the core representation the algorithm operates on
- [[MobiusTransformation]] — the linear fractional map encoded by the state matrix
- [[GosperAlgorithm]] — the term-by-term arithmetic technique being implemented
- [[ArithmeticGeometricMean]] — the downstream goal this task sets up
- [[ExactArithmetic]] — computing without floating-point ulps or epsilons

## Contradictions
- None — reference task page.
