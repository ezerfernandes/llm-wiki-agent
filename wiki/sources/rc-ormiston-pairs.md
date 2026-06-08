---
title: "Ormiston pairs (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ormiston_pairs
---

## Summary
An Ormiston pair is two consecutive prime numbers that are anagrams of each other — they share the same multiset of decimal digits but in a different arrangement. The first such pair is (1913, 1931). The key insight is combining a prime sieve or primality test with a digit-fingerprint comparison (e.g. sorting digits or counting digit frequencies) between each prime and its successor.

## Task Requirements
- Find and show the first 30 Ormiston pairs.
- Find and show the count of Ormiston pairs up to one million.
- Stretch: find and show the count of Ormiston pairs up to ten million.

## Language Coverage
31 languages implement this task, spanning systems, functional, array, and scripting families. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, and J.

## Connections
- [[PrimeNumbers]] — the pairs are drawn from consecutive primes
- [[Anagram]] — the defining condition is a digit anagram between the two primes
- [[SieveOfEratosthenes]] — common way to generate the prime stream efficiently
- [[OEIS]] — sequence A072274 catalogs Ormiston prime pairs

## Contradictions
- None — reference task page.
