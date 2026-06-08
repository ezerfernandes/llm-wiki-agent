---
title: "Earliest difference between prime gaps (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Earliest_difference_between_prime_gaps
---

## Summary
A prime gap is the difference between two adjacent primes; for each even gap value (2, 4, 6, ...) there is a known minimal starting prime that produces that gap. This task treats gaps differing by exactly two as "adjacent" and asks, for each order of magnitude m from 10^1 to 10^6, to find the first pair of adjacent gaps whose minimal starting prime values differ by more than m. The key insight is that although every even gap value eventually occurs, the minimal starting primes do not increase monotonically with gap size, so the differences jump around irregularly.

## Task Requirements
- Determine, for each even gap value, the minimal starting prime that produces that gap (e.g. gap 2 starts at 3, gap 4 at 7, gap 6 at 23).
- Treat two gaps that differ by exactly 2 as adjacent.
- For each order of magnitude m from 10^1 through 10^6, find the first adjacent gap pair where the absolute difference of their minimal starting primes exceeds m, reporting the gaps and their start values.
- Stretch goal: extend the search to 10^7, 10^8, and higher orders of magnitude.

## Language Coverage
22 languages implement this task, giving solid coverage across systems, functional, scripting, and array languages. Representative implementations include C++, Go, Rust, Java, Python, Perl, Raku, Julia, F#, and Wren.

## Connections
- [[PrimeNumbers]] — the task is built entirely on sequences of primes
- [[PrimeGap]] — the difference between adjacent primes is the central object
- [[SieveOfEratosthenes]] — a common method for generating the primes needed
- [[NumberTheory]] — prime gaps and their conjectured distribution are number-theoretic
- [[Conjecture]] — relies on the conjecture that every even gap value eventually appears

## Contradictions
- None — reference task page.
