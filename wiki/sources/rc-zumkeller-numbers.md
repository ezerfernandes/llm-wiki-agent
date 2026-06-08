---
title: "Zumkeller numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors, partition]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Zumkeller_numbers
---

## Summary
A Zumkeller number is one whose set of divisors can be split into two disjoint subsets with equal sums (e.g. 6's divisors {1,2,3,6} split into {1,2,3} and {6}, each summing to 6). The task is to detect such numbers, which reduces to a subset-sum / partition test on the divisors. A key insight is that a number can only be Zumkeller if its divisor sum sigma(n) is even and the number is abundant or perfect; odd Zumkeller numbers additionally require the abundance A(n) = sigma(n) - 2n to be even.

## Task Requirements
- Write a routine to determine whether a number is a Zumkeller number.
- Find and display the first 220 Zumkeller numbers.
- Find and display the first 40 odd Zumkeller numbers.
- Optional stretch goal: find and display the first 40 odd Zumkeller numbers that do not end in 5.

## Language Coverage
42 languages implement this task, spanning systems languages, scripting languages, functional languages, and even hand-written assembly. Representative implementations include Python, C++, C#, Rust, Go, Haskell, Julia, Raku, Java, REXX, and AArch64 Assembly.

## Connections
- [[NumberTheory]] — Zumkeller numbers are defined in terms of integer divisors and their sums.
- [[Divisors]] — the routine must enumerate all divisors of each candidate.
- [[SubsetSumProblem]] — partitioning divisors into two equal-sum sets is a subset-sum/partition test.
- [[AbundantNumbers]] — Zumkeller numbers are a refinement of abundant/perfect numbers.

## Contradictions
- None — reference task page.
