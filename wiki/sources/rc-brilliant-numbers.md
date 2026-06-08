---
title: "Brilliant numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Brilliant_numbers
---

## Summary
A brilliant number is a semiprime — a product of exactly two primes — whose two prime factors have the same number of base-10 digits (e.g. 9 = 3×3, 14 = 2×7, 78083 = 113×691). They are notable in cryptography and for benchmarking prime-factoring algorithms. The key insight is that brilliant numbers can be generated efficiently by pairing primes drawn from the same digit-length band rather than factoring every integer.

## Task Requirements
- Find and display the first 100 brilliant numbers.
- For orders of magnitude 1 through 6, find the first brilliant number greater than or equal to that order of magnitude and report its position (count of brilliant numbers up to that point).
- Stretch goal: continue the same computation for larger orders of magnitude.

## Language Coverage
42 languages implement this task. Coverage spans systems and scripting languages alike, including C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, Nim, and Wren.

## Connections
- [[SemiprimeNumbers]] — brilliant numbers are the digit-balanced subset of semiprimes
- [[PrimeNumbers]] — factors must both be prime
- [[SieveOfEratosthenes]] — common technique for generating the candidate prime bands
- [[IntegerFactorization]] — the application domain (testing factoring algorithms)

## Contradictions
- None — reference task page.
