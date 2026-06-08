---
title: "Anaprimes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, anagrams]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Anaprimes
---

## Summary
Anaprimes are prime numbers that are anagrams of one another, using exactly the same digits with the same frequency but in a different order (e.g. 149, 419, 491, 941). The task investigates how primes cluster into equivalence classes under the "is an anagram of" relation and asks the programmer to find the largest such class within increasing digit ranges. The key insight is that sorting a number's digits yields a canonical key that groups all anagrams together, so primes can be bucketed by that key.

## Task Requirements
- Find prime numbers that are anagrams of each other.
- For each upper bound, determine the largest anagram group of primes and report its count, minimum member, and maximum member:
  - up to three digits (below 1,000)
  - up to four digits (below 10,000)
  - up to five digits (below 100,000)
  - up to six digits (below 1,000,000)
- Stretch goal: extend the same analysis to seven-, eight-, and nine-digit ranges (below 10,000,000; 100,000,000; 1,000,000,000).

## Language Coverage
29 languages implement this task, spanning systems, functional, scripting, and array languages. Representative examples include Ada, C++, C#, Go, Haskell, Java, Python, Perl, Raku, Rust, J, and Wren.

## Connections
- [[PrimeNumber]] — the elements being grouped are primes, requiring a primality test or sieve.
- [[SieveOfEratosthenes]] — an efficient way to enumerate primes up to a billion.
- [[Anagram]] — equivalence is defined by digit-permutation, i.e. anagrams of the decimal representation.
- [[EquivalenceClass]] — primes are partitioned into classes by a canonical sorted-digit key.
- [[Hashing]] — bucketing by sorted-digit key relies on a hash map keyed on the canonical form.

## Contradictions
- None — reference task page.
