---
title: "Successive prime differences (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Successive_prime_differences
---

## Summary
This task filters the sequence of increasing primes to find groups of *successive* primes whose consecutive gaps match a specified pattern of differences. For example, a single difference of 2 yields twin primes like (3,5) and (5,7), while a difference list of [2,4] yields triples like (5,7,11) where 7 is two more than 5 and 11 is four more than 7. The key insight is that order matters: a pattern of [4,2] produces entirely different groups than [2,4], and a list of n differences produces groups of n+1 successive primes.

## Task Requirements
- Use the list of primes less than 1,000,000.
- For each given difference pattern, report the first group, the last group, and the total count of groups found.
- Run for these patterns: [2], [1], [2,2], [2,4], [4,2], and [6,4,2].
- Differences must be matched in the exact order given, against consecutive primes.
- Prime generation is secondary; using a built-in or library sieve is encouraged.

## Language Coverage
42 languages implement this task, spanning systems and functional languages alongside scripting and array-oriented ones. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, J, and Wolfram Language.

## Connections
- [[PrimeNumbers]] — the task operates over the sequence of primes
- [[TwinPrimes]] — the difference-of-2 case directly produces twin prime pairs
- [[SieveOfEratosthenes]] — the recommended method for generating the prime list
- [[NumberTheory]] — prime gaps and constellations are number-theoretic structures

## Contradictions
- None — reference task page.
