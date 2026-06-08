---
title: "Descending primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Descending_primes
---

## Summary
The task asks the programmer to generate and display every prime number whose decimal digits are strictly decreasing from left to right (e.g. 5, 31, 97, 421). The key insight is that the candidate space is tiny and bounded: since each digit must be strictly smaller than the one before, every candidate corresponds to a non-empty subset of the digits 1–9 arranged in descending order, so one can enumerate these combinations and primality-test them rather than scanning all integers. This makes the problem a small combinatorial generate-and-filter exercise.

## Task Requirements
- Generate all primes whose decimal digits are in strictly descending order.
- Show the complete list of such primes.

## Language Coverage
49 languages implement this task, spanning systems, functional, scripting, and array/stack paradigms. Representative implementations include C, C++, C#, Java, Rust, Go, Python, Haskell, Raku, Perl, Julia, and J.

## Connections
- [[PrimeNumbers]] — every candidate must be primality-tested
- [[PrimalityTest]] — the filtering step applied to each generated number
- [[Combinatorics]] — candidates are descending-ordered subsets of digits 1–9
- [[DigitManipulation]] — the descending-digit constraint drives generation
- [[AscendingPrimes]] — directly related companion Rosetta Code task

## Contradictions
- None — reference task page.
