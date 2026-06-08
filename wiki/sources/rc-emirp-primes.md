---
title: "Emirp primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Emirp_primes
---

## Summary
An emirp (the word "prime" spelled backwards) is a prime number that becomes a *different* prime when its decimal digits are reversed; palindromic primes are explicitly excluded. The task asks the programmer to generate emirps in order and report several specific results. The key implementation insight is combining a primality test with a digit-reversal step, while filtering out numbers whose reversal equals themselves.

## Task Requirements
- Show the first twenty emirps.
- Show all emirps between 7,700 and 8,000.
- Show the 10,000th emirp.
- In each list the numbers must be in ascending order.
- The same program should be invoked once per requirement; the method for selecting a range versus specific values is left to the programmer.

## Language Coverage
77 languages implement this task, giving broad coverage across systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Ruby, Perl, Raku, and REXX.

## Connections
- [[PrimeNumbers]] — the underlying objects being filtered.
- [[PrimalityTest]] — needed both for the candidate and its digit-reversal.
- [[DigitReversal]] — the operation that defines the emirp condition.
- [[PalindromicNumbers]] — explicitly excluded because their reversal is unchanged.
- [[NumberTheory]] — the broader mathematical domain.

## Contradictions
- None — reference task page.
