---
title: "Sum multiples of 3 and 5 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sum_multiples_of_3_and_5
---

## Summary
The task asks the programmer to write a function that returns the sum of all positive multiples of 3 or 5 below a given bound `n`, demonstrated for `n = 1000`. This is identical to Project Euler problem 1. The key insight is that a naive O(n) loop works for small `n`, but a closed-form approach using arithmetic-series sums (combined with inclusion-exclusion to avoid double-counting multiples of 15) yields an O(1) solution capable of handling enormous bounds like 1e20.

## Task Requirements
- Write a function that finds the sum of all positive multiples of 3 or 5 below `n`.
- Show the output for `n = 1000`.
- Extra credit: compute the result efficiently for `n = 1e20` or higher (requires big integers and a closed-form formula).

## Language Coverage
125 languages implement this task, giving very broad coverage spanning low-level assembly, mainstream and functional languages, and esoteric or vintage platforms. Representative implementations include C, C++, Java, Python, Rust, Haskell, Go, Common Lisp, Raku, and 360 Assembly.

## Connections
- [[NumberTheory]] — multiples and divisibility are the core domain.
- [[InclusionExclusionPrinciple]] — sum of multiples of 3 plus multiples of 5 minus multiples of 15.
- [[ArithmeticSeries]] — closed-form triangular-number sum enables the efficient O(1) solution.
- [[BigInteger]] — needed to handle the 1e20 extra-credit bound without overflow.
- [[ProjectEuler]] — this is Project Euler problem 1.

## Contradictions
- None — reference task page.
