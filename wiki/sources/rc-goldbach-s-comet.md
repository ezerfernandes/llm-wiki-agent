---
title: "Goldbach's comet (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Goldbach's_comet
---

## Summary
Goldbach's comet is the plot of the Goldbach function g(E), which counts the number of distinct ways an even integer E > 2 can be written as the sum of two primes. The task asks the programmer to compute this function for small even numbers and for one large value. The key insight is that for each even E one iterates over primes p ≤ E/2 and tests whether E − p is also prime, so an efficient prime test or sieve dominates performance.

## Task Requirements
- Compute the Goldbach function g(E) = number of distinct unordered prime pairs summing to even E (e.g. g(4)=1, g(22)=3).
- Find and show the first 100 G numbers (for the first 100 even numbers ≥ 4), preferably in a neat 10x10 table.
- Find and display the value of G(1000000).
- Stretch: compute G up to 2000 inclusive and render a 2D scatter chart (the "comet" shape).

## Language Coverage
33 languages implement this task, spanning array/APL-style languages and mainstream procedural ones. Representative implementations include Python, C++, Rust, Go, Java, Julia, Perl, Raku, J, and Wren.

## Connections
- [[GoldbachConjecture]] — the unproven conjecture this function illustrates
- [[PrimeNumbers]] — every decomposition is a pair of primes
- [[SieveOfEratosthenes]] — common technique for generating the primes needed
- [[NumberTheory]] — the branch of mathematics this problem belongs to

## Contradictions
- None — reference task page.
