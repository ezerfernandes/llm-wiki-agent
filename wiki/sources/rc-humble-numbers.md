---
title: "Humble numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Humble_numbers
---

## Summary
Humble numbers are positive integers whose only prime factors are 2, 3, 5, and 7 (i.e. they can be written as 2^i × 3^j × 5^k × 7^m with i, j, k, m ≥ 0). Also known as 7-smooth numbers, they are a generalization of Hamming numbers, which restrict factors to 2, 3, and 5. The key insight is that each new humble number is the smallest unseen multiple of an existing one by 2, 3, 5, or 7, so they are generated efficiently by merging four ordered streams.

## Task Requirements
- Show the first 50 humble numbers in a horizontal list.
- Show, for each digit-count x from 1 up to some n, the count of humble numbers having exactly x decimal digits.
- Display as many of these per-digit counts as is feasible or reasonable, on separate lines.
- Show all output on the task page.

## Language Coverage
61 languages implement this task, giving broad coverage across functional, imperative, and array-oriented styles. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, J, Julia, Raku, and REXX.

## Connections
- [[SmoothNumbers]] — humble numbers are exactly the 7-smooth numbers.
- [[HammingNumbers]] — the closely related 5-smooth analogue, generated the same way.
- [[PrimeFactorization]] — the defining condition is a constraint on prime factors.
- [[MergingOrderedSequences]] — the standard generation merges streams multiplied by 2, 3, 5, 7.

## Contradictions
- None — reference task page.
