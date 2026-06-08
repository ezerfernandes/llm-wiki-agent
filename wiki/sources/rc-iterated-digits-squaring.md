---
title: "Iterated digits squaring (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Iterated_digits_squaring
---

## Summary
Repeatedly replacing a natural number with the sum of the squares of its digits always converges to a fixed point of either 1 or 89. The task is to count how many starting integers in a large range (1 ≤ n < 100,000,000) end their chain at 89. The key insight is that the sum-of-digit-squares of an 8-digit number is small, so a naive per-number iteration is wasteful; a fast solution memoizes outcomes for the few thousand possible digit-square sums and counts via the multinomial number of digit combinations.

## Task Requirements
- Implement a step function that maps n to the sum of the squares of its decimal digits.
- Iterate that step until reaching the fixed point 1 or 89.
- Count how many integers in 1 ≤ n < 100,000,000 terminate at 89 (or the easier 1 ≤ n < 1,000,000 range for less credit).

## Language Coverage
72 languages implement this task, a broad spread covering systems, scripting, functional, and BASIC dialects. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, and X86 Assembly.

## Connections
- [[NumberTheory]] — the task is a classic digit-based number-theory problem (Project Euler 92).
- [[HappyNumbers]] — numbers converging to 1 under this map are exactly the happy numbers.
- [[DigitalRoot]] — a related iterated digit-transformation process.
- [[Memoization]] — the fast algorithm caches chain outcomes for the bounded set of digit-square sums.
- [[Recursion]] — the chain is naturally expressed as a recursive iterate-until-fixed-point function.

## Contradictions
- None — reference task page.
