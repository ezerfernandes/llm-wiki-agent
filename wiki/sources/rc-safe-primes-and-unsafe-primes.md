---
title: "Safe primes and unsafe primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Safe_primes_and_unsafe_primes
---

## Summary
A prime p is a "safe prime" if (p-1)/2 is also prime; otherwise it is an "unsafe prime". The corresponding prime (p-1)/2 is called a Sophie Germain prime. The task is to enumerate and count both kinds, which reduces to a standard primality test combined with the simple (p-1)/2 check.

## Task Requirements
- Find and display on one line the first 35 safe primes.
- Display the count of safe primes below 1,000,000 and below 10,000,000.
- Find and display on one line the first 40 unsafe primes.
- Display the count of unsafe primes below 1,000,000 and below 10,000,000.
- (Optional) Display counts and threshold numbers with thousands separators (commas).

## Language Coverage
51 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, and REXX.

## Connections
- [[PrimeNumbers]] — both definitions are built on primality of p and (p-1)/2.
- [[SophieGermainPrime]] — the prime (p-1)/2 corresponding to a safe prime.
- [[PrimalityTest]] — the core operation repeated for each candidate.
- [[SieveOfEratosthenes]] — a common way to precompute primes below the count thresholds.
- [[NumberTheory]] — the mathematical domain this classification belongs to.

## Contradictions
- None — reference task page.
