---
title: "Additive primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Additive_primes
---

## Summary
An additive prime is a prime number whose decimal digit sum is itself prime. The task asks the programmer to find and display every additive prime below 500, and optionally report how many there are. The key insight is that it composes two simple tests — primality of the number and primality of its digit sum — so a basic prime check plus digit-sum reduction is all that is needed.

## Task Requirements
- Determine and display all additive primes less than 500.
- An additive prime qualifies when both the number and the sum of its decimal digits are prime.
- Optionally, also show the count of additive primes found.

## Language Coverage
106 languages implement this task, reflecting very broad coverage spanning assembly, classic, functional, and modern scripting languages. Representative examples include Python, C, C++, Rust, Go, Haskell, Java, Ada, Raku, and AArch64 Assembly.

## Connections
- [[PrimeNumbers]] — the core predicate applied to both the candidate and its digit sum
- [[DigitSum]] — the digit-sum reduction that defines the "additive" property
- [[NumberTheory]] — the branch of mathematics this sequence (OEIS A046704) belongs to
- [[SieveOfEratosthenes]] — a common technique for generating the primes to test

## Contradictions
- None — reference task page.
