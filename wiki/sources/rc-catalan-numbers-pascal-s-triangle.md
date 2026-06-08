---
title: "Catalan numbers/Pascal's triangle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Catalan_numbers/Pascal's_triangle
---

## Summary
This task asks the programmer to print the first 15 Catalan numbers, but with a specific twist: they must be derived from Pascal's triangle rather than computed via the usual closed-form factorial or product formula. The key insight is that each Catalan number equals the difference between a central binomial coefficient and an adjacent one in the same row, so the entire sequence can be generated using only addition and subtraction.

## Task Requirements
- Output the first 15 Catalan numbers.
- Obtain each number by extracting values from Pascal's triangle (e.g. C(n) = C(2n, n) - C(2n, n+1)).
- Use the addition-based construction of Pascal's triangle rather than direct factorial computation.

## Language Coverage
86 languages implement this task, giving very broad coverage spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Python, Haskell, Java, JavaScript, APL, and REXX.

## Connections
- [[CatalanNumbers]] — the integer sequence (OEIS A000108) the task generates.
- [[PascalsTriangle]] — the binomial-coefficient triangle used as the extraction source.
- [[BinomialCoefficient]] — the central values whose differences yield Catalan numbers.
- [[Combinatorics]] — the branch of math counting structures these numbers enumerate.
- [[NumberTheory]] — the broader domain of integer-sequence computation.

## Contradictions
- None — reference task page.
