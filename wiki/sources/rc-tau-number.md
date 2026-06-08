---
title: "Tau number (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tau_number
---

## Summary
A Tau number (also called a refactorable number) is a positive integer that is evenly divisible by its own count of positive divisors. The task is to generate and display the first 100 such numbers at run-time, without using precomputed literals, sets, or arrays of the answer values. The key insight is that solving it requires computing the divisor-count function (tau) for each candidate and testing the divisibility condition.

## Task Requirements
- Compute, for each candidate integer, the count of its positive divisors (the tau function).
- A number qualifies as a Tau number if it is divisible by that divisor count.
- Show the first 100 Tau numbers.
- The numbers must be generated during run-time — no string literals, hardcoded sets, or arrays of integers holding the answers.

## Language Coverage
86 languages implement this task, reflecting broad coverage across paradigms and eras. Representative implementations include C, C++, Rust, Go, Python, Haskell, Java, JavaScript, Julia, Raku, Forth, and the venerable ALGOL 60.

## Connections
- [[NumberTheory]] — the task is rooted in divisor properties of integers.
- [[DivisorFunction]] — computing tau (the count of divisors) is the core subroutine.
- [[RefactorableNumber]] — the formal name for these integers.
- [[Divisibility]] — the qualifying test is a divisibility condition.

## Contradictions
- None — reference task page.
