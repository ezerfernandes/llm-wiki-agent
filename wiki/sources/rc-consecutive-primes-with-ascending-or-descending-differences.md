---
title: "Consecutive primes with ascending or descending differences (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Consecutive_primes_with_ascending_or_descending_differences
---

## Summary
This task asks the programmer to find the longest run of consecutive prime numbers whose successive gaps (differences between adjacent primes) are strictly increasing, and separately the longest run whose gaps are strictly decreasing. The search is bounded to primes below 1,000,000. The key insight is that one scans the prime sequence while tracking the current monotonic run of gaps, resetting whenever monotonicity breaks and remembering the best run seen.

## Task Requirements
- Generate the consecutive primes below 1,000,000.
- Find the longest sequence of consecutive primes whose pairwise differences are strictly ascending; display that sequence.
- Find the longest sequence whose pairwise differences are strictly descending; display that sequence.
- If multiple sequences share the maximum length, only the first one needs to be shown.

## Language Coverage
35 languages implement this task, giving broad coverage across systems, functional, scripting, and array-oriented styles. Representative implementations include C, C++, C#, Go, Rust, Java, Haskell, F#, Python, Perl, Raku, Julia, Ruby, and J.

## Connections
- [[PrimeNumbers]] — the sequence being scanned and filtered
- [[SieveOfEratosthenes]] — common way to enumerate primes below the bound
- [[PrimeGaps]] — the differences between consecutive primes drive the task
- [[MonotonicSequence]] — runs of strictly ascending or descending gaps

## Contradictions
- None — reference task page.
