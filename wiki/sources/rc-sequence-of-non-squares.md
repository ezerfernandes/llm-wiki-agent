---
title: "Sequence of non-squares (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sequence_of_non_squares
---

## Summary
This task asks the programmer to demonstrate that the closed-form expression `n + floor(1/2 + sqrt(n))` generates exactly the natural numbers that are not perfect squares. The key insight is that this single formula skips every perfect square as `n` increases, producing the OEIS sequence A000037 (the non-squares) without any explicit testing or filtering.

## Task Requirements
- Print the values produced by `n + floor(1/2 + sqrt(n))` for `n` in the range 1 to 22.
- Verify that none of the generated values is a perfect square for all `n` less than one million.

## Language Coverage
117 languages implement this task, showing very broad coverage across functional, imperative, scripting, and BASIC-family languages. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, Perl, Lisp (Common Lisp/Scheme/Racket), and APL/J.

## Connections
- [[NumberTheory]] — concerns the distribution of perfect squares among naturals
- [[PerfectSquare]] — the formula is constructed precisely to avoid these values
- [[FloorFunction]] — the floor and integer square root are central to the closed form
- [[IntegerSequence]] — corresponds to OEIS A000037
- [[ClosedFormExpression]] — generates the sequence directly without iterative filtering

## Contradictions
- None — reference task page.
