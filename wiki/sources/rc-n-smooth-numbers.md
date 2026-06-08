---
title: "N-smooth numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/N-smooth_numbers
---

## Summary
An n-smooth number is a positive integer whose prime factors are all less than or equal to n (where n is itself prime). The task asks the programmer to generate these numbers in order for various values of n. The key insight is that n-smooth numbers can be built incrementally by multiplying smaller smooth numbers by each allowed prime, generalizing the Hamming-number merge algorithm to an arbitrary set of primes.

## Task Requirements
- Calculate and show the first 25 n-smooth numbers for each prime n from 2 through 29.
- Calculate and show three numbers starting from the 3,000th n-smooth number for each prime n from 3 through 29.
- (Optional) Calculate and show twenty numbers starting from the 30,000th n-smooth number for n = 503, 509, and 521.
- All n ranges are inclusive and only prime values of n are used; 1 (unity) is always included; output each n's list horizontally.

## Language Coverage
37 languages implement this task, showing broad coverage across functional, imperative, and array-oriented styles. Representative implementations include C, C++, Python, Go, Rust, Haskell, Java, Julia, Perl, Raku, and Wren.

## Connections
- [[SmoothNumber]] — the central concept being generated
- [[HammingNumbers]] — 5-smooth numbers are the classic special case
- [[PrimeFactorization]] — definition rests on a number's prime factors
- [[NumberTheory]] — the mathematical domain of the task
- [[MergeAlgorithm]] — ordered generation via merging prime-multiplied streams

## Contradictions
- None — reference task page.
