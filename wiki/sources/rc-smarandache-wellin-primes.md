---
title: "Smarandache-Wellin primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Smarandache-Wellin_primes
---

## Summary
A Smarandache-Wellin number is the integer formed by concatenating the first n prime numbers in base 10 (e.g. the 6th is 23571113). The task asks the programmer to find those S-W numbers that are themselves prime, plus a "Derived" variant built by counting how often each digit 0-9 appears, concatenating those frequencies, and stripping leading zeros. The key practical insight is that S-W primes grow enormous very quickly, so the stretch goals require big-integer arithmetic and probabilistic primality testing.

## Task Requirements
- Find and show the first three S-W numbers that are prime.
- Find and show the first three Derived S-W numbers that are prime.
- Stretch (big integers): for the 4th through 7th (optionally 8th) prime/probable-prime S-W numbers, report the index in the sequence, total digit count, and the last prime used to form each (search may start at index 22,077).
- Stretch: find and show up to the first twenty prime Derived S-W numbers along with their sequence index.

## Language Coverage
19 languages implement this task, a moderate spread typical of number-theory challenges that demand big-integer support. Representative implementations include C, C++, Go, Java, Julia, Nim, Perl, Python, Raku, and Wren.

## Connections
- [[PrimeNumbers]] — the sequence is built from successive primes
- [[PrimalityTesting]] — probabilistic tests are needed for the large stretch candidates
- [[BigInteger]] — arbitrary-precision arithmetic is required as concatenations explode in size
- [[NumberConcatenation]] — both S-W and Derived numbers are formed by digit/string concatenation
- [[DigitFrequencyCounting]] — Derived S-W numbers tally occurrences of each digit

## Contradictions
- None — reference task page.
