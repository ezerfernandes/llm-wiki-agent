---
title: "Smarandache prime-digital sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Smarandache_prime-digital_sequence
---

## Summary
The task asks the programmer to generate the Smarandache prime-digital sequence (SPDS): primes that are themselves prime AND whose every decimal digit is also prime. Since the only prime digits are 2, 3, 5, and 7, the key insight is that candidates can be restricted to numbers built solely from those four digits, dramatically narrowing the search space before applying a primality test. For example, 257 qualifies because it is prime and each of its digits (2, 5, 7) is prime.

## Task Requirements
- Show the first 25 SPDS primes.
- Show the hundredth SPDS prime.

## Language Coverage
45 languages implement this task. Coverage is broad, spanning systems, functional, scripting, and BASIC-family languages, including C, C++, Rust, Go, Haskell, Java, JavaScript, Python, Perl, Raku, Julia, and REXX.

## Connections
- [[PrimeNumbers]] — the sequence members and their digits must all be prime.
- [[PrimalityTest]] — each generated candidate must be checked for primality.
- [[NumberTheory]] — the task is a digit-property variant of an integer sequence.
- [[DigitManipulation]] — candidates are constrained to the prime digits 2, 3, 5, 7.
- [[IntegerSequences]] — corresponds to OEIS A019546.

## Contradictions
- None — reference task page.
