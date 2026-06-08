---
title: "Sexy primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sexy_primes
---

## Summary
Sexy primes are prime numbers that differ from one another by six (the name puns on the Latin word for six, *sex*). The task asks the programmer to find sexy prime groups of increasing size — pairs, triplets, quadruplets, and quintuplets — where each member differs from the next by 6, plus the "unsexy" primes that have no prime partner six away in either direction. A key insight is that only one quintuplet (5 11 17 23 29) can exist, since one of five terms with common difference 6 must be divisible by 5.

## Task Requirements
- For pairs, triplets, quadruplets, and quintuplets, find and display the count of each sexy-prime group type below 1,000,035.
- Display at most the last 5 (below the limit) of each group type.
- Find and display the count of unsexy primes below 1,000,035.
- Find and display the last 10 unsexy primes below the limit.
- Note that 1000033 must NOT be counted as a pair (it is sexy but its partner exceeds the limit), and must NOT be listed as unsexy since it is in fact sexy.

## Language Coverage
41 languages implement this task, spanning systems, scripting, functional, and array languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and J.

## Connections
- [[PrimeNumbers]] — the task is built entirely on primality testing
- [[NumberTheory]] — sexy primes are a studied constructed-prime-pattern in this field
- [[SieveOfEratosthenes]] — a common way to generate primes below the limit efficiently
- [[ModularArithmetic]] — explains why only one sexy prime quintuplet can exist

## Contradictions
- None — reference task page.
