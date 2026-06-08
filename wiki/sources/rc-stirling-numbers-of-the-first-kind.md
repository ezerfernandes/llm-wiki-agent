---
title: "Stirling numbers of the first kind (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Stirling_numbers_of_the_first_kind
---

## Summary
Stirling numbers of the first kind (cycle numbers) count the permutations of n elements that decompose into exactly k disjoint cycles. They appear as the coefficients when falling or rising factorials are expanded as polynomials. The task is to compute them, typically via the recurrence S1(n, k) = S1(n-1, k-1) + (n-1)·S1(n-1, k) for the unsigned form, where the only difference for the signed form is a minus sign that makes S1(n, k) negative when n + k is odd.

## Task Requirements
- Write a routine to compute Stirling numbers of the first kind, choosing the most appropriate method (a built-in or library is acceptable).
- Generate and display a table/triangle of S1(n, k) values up to S1(12, 12); rows/columns for n == 0 or k == 0 and zero entries (k > n) are optional.
- State whether signed or unsigned numbers are shown.
- If the language supports big integers, find and display the maximum value of S1(n, k) for n == 100.

## Language Coverage
40 languages implement this task, spanning systems languages, functional languages, array languages, and CAS/big-integer environments. Representative implementations include C, C++, D, Go, Rust-adjacent Crystal, Haskell, Julia, Python, Raku, J, Mathematica/Wolfram Language, and Wren.

## Connections
- [[StirlingNumbersSecondKind]] — companion task counting set partitions rather than permutation cycles.
- [[LahNumbers]] — related triangular array connecting rising and falling factorials.
- [[Combinatorics]] — these numbers count permutations grouped by cycle structure.
- [[Recurrence]] — the standard generation method is a two-term recurrence over a triangle.
- [[BigIntegers]] — required for S1(100, k), whose values overflow fixed-width integers.

## Contradictions
- None — reference task page.
