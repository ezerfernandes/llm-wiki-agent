---
title: "Twin primes whose sum is square number (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Twin_primes_whose_sum_is_square_number
---

## Summary
The task asks the programmer to find and display all twin prime pairs below 10,000,000 whose sum is a perfect square. Twin primes are pairs (p, p+2) that are both prime, so their sum is 2p+2. The key insight is that since the sum of a twin pair (p, p+2) equals 2(p+1), and the pair is centered on p+1, the requirement reduces to checking which of these midpoints, doubled, form a perfect square.

## Task Requirements
- Enumerate twin prime pairs (p, p+2) where both members are prime.
- Restrict the search to pairs under 10,000,000.
- Display only those pairs whose sum (p + (p+2)) is a perfect square.

## Language Coverage
32 languages implement this task, spanning systems, scripting, functional, and array-oriented styles. Representative implementations include Ada, ALGOL 68, C++, Fortran, Java, Julia, Nim, Perl, Python, Raku, Rust, and Wren.

## Connections
- [[PrimeNumbers]] — the pairs must both be prime
- [[TwinPrimes]] — the core structure (p, p+2) being enumerated
- [[PerfectSquare]] — the sum must be a square number
- [[SieveOfEratosthenes]] — a common technique for generating primes up to the bound
- [[NumberTheory]] — the broader domain of the problem

## Contradictions
- None — reference task page.
