---
title: "Ultra useful primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ultra_useful_primes
---

## Summary
An ultra-useful prime is defined by the sequence where a(n) is the smallest positive integer k such that 2^(2^n) - k is prime. The key insight is that k must always be odd, since 2 raised to any power is even and subtracting an odd number yields the odd candidates that can be prime. The task explores these by descending from the huge Fermat-style power of two and searching for the nearest prime below it (OEIS A058220).

## Task Requirements
- Find and show the first 10 elements of the sequence a(n).
- Stretch goal: compute the next several elements, noting the values 2^(2^n) grow extremely fast (only 19 elements identified as of writing).

## Language Coverage
29 languages implement this task, spanning systems and scripting languages plus several BASIC dialects. Representative implementations include Ada, ALGOL 68, C, C#, Go, Java, Julia, Python, Perl, Raku, and Wren.

## Connections
- [[PrimeNumber]] — the sequence searches for primes just below powers of two
- [[NumberTheory]] — the task is rooted in properties of integers and primality
- [[PrimalityTest]] — finding the smallest k requires testing large candidates for primality
- [[BigInteger]] — values like 2^(2^n) require arbitrary-precision arithmetic
- [[OEIS]] — the sequence corresponds to OEIS A058220

## Contradictions
- None — reference task page.
