---
title: "Primes: n*2^m+1 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Primes:_n*2^m+1
---

## Summary
For each positive integer n, the task is to find the smallest non-negative exponent m such that n × 2^m + 1 is prime, then display that prime. The sequence of such smallest primes corresponds to OEIS A050921. The key insight is that for a given n one searches upward over m (multiplying by 2 each step and adding 1) until a prime is found, since not every n yields a prime at m = 0.

## Task Requirements
- Find and display the first 45 such primes (one per n).
- Stretch: extend to the first 50 primes.
- Stretch harder: extend to the first 400 primes, specifically calling out term 383.
- For each n use the smallest valid non-negative integer m.

## Language Coverage
26 languages implement this task, spanning systems and scripting languages with strong arbitrary-precision arithmetic support since later terms grow large. Representative implementations include Ada, ALGOL 68, Java, Julia, Nim, Perl, Phix, Python, Raku, and Wren.

## Connections
- [[PrimeNumbers]] — the core property being tested for each candidate value
- [[PrimalityTesting]] — efficiently checking n × 2^m + 1 for primeness, often probabilistic for large m
- [[NumberTheory]] — the underlying domain and OEIS sequence A050921
- [[ArbitraryPrecisionArithmetic]] — needed because candidates can exceed machine-word size for higher terms

## Contradictions
- None — reference task page.
