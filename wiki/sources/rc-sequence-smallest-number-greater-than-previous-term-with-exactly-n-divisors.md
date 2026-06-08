---
title: "Sequence: smallest number greater than previous term with exactly n divisors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sequence:_smallest_number_greater_than_previous_term_with_exactly_n_divisors
---

## Summary
This Rosetta Code task asks the programmer to generate a sequence where each term a_n is the smallest natural number strictly greater than the previous term that has exactly n divisors. Unlike the related "smallest number with exactly n divisors" task, the strict monotonic constraint (each term must exceed the prior one) forces a running floor, so candidates are searched upward from one past the last term. The sequence corresponds to OEIS A069654.

## Task Requirements
- For each n (starting at 1), find the smallest natural number that is greater than the previous term and has exactly n divisors.
- The first term has no predecessor, so its lower bound is effectively 1.
- Display at least the first 15 terms of the sequence.

## Language Coverage
47 languages implement this task, showing broad coverage across systems, functional, scripting, and legacy languages. Representative implementations include C, C++, Java, Python, Go, Haskell, Julia, Perl, Raku, REXX, and Wren.

## Connections
- [[DivisorCountingFunction]] — the core operation is counting the divisors of a candidate
- [[NumberTheory]] — the problem is rooted in elementary number theory
- [[IntegerSequences]] — produces a monotonic integer sequence (OEIS A069654)
- [[BruteForceSearch]] — typical solutions scan candidates upward until the divisor count matches

## Contradictions
- None — reference task page.
