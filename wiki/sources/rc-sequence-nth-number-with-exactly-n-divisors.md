---
title: "Sequence: nth number with exactly n divisors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sequence:_nth_number_with_exactly_n_divisors
---

## Summary
This task asks the programmer to compute the sequence whose nth term is the nth positive integer that has exactly n divisors. For each index n, you scan integers, count how many divisors each has, and select the nth one whose divisor count equals n. The sequence corresponds to OEIS A073916, and the key insight is combining a divisor-counting routine with a per-index search loop.

## Task Requirements
- For each n, find the nth positive integer having exactly n divisors.
- Show at least the first 15 terms of the resulting sequence.

## Language Coverage
25 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, D, Go, Haskell, Java, Julia, Python, Perl, Raku, REXX, and Wren.

## Connections
- [[NumberTheory]] — the task is grounded in integer divisor properties
- [[DivisorFunction]] — each term depends on counting divisors d(k)
- [[IntegerSequences]] — produces an OEIS-cataloged sequence (A073916)
- [[PrimeFactorization]] — divisor counts derive from prime factor exponents

## Contradictions
- None — reference task page.
