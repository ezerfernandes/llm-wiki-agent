---
title: "Erdős-primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Erdős-primes
---

## Summary
The task is to find Erdős primes, defined as prime numbers p for which every value p - k! is composite for all factorials k! satisfying 1 <= k! < p. The key insight is that a prime qualifies only if subtracting each factorial below it never lands on another prime, which combines a primality test with iteration over the small set of factorials less than p.

## Task Requirements
- Determine and display all Erdős primes less than 2500.
- Optionally report the total count of those primes.
- Stretch goal: show that the 7,875th Erdős prime is 999,721, the largest below 1,000,000.
- Reference is OEIS sequence A064152.

## Language Coverage
46 languages implement this task, spanning systems, scripting, array, and academic languages — representative examples include C, C++, Rust, Go, Java, Python, Perl, Raku, Julia, APL, and J.

## Connections
- [[PrimeNumbers]] — the core objects being tested and filtered
- [[Factorial]] — the offsets k! subtracted from each candidate prime
- [[PrimalityTest]] — needed both for the candidate and for each p - k! difference
- [[NumberTheory]] — the broader field defining this special prime sequence

## Contradictions
- None — reference task page.
