---
title: "Sequence of primes by trial division (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sequence_of_primes_by_trial_division
---

## Summary
The task asks the programmer to generate a sequence of prime numbers using trial division, where each candidate is tested for primality by attempting to divide it by smaller numbers (typically previously found primes or all integers up to its square root). The sequence may be bounded or unbounded and may start from 2 or from some given value. The key insight is that primality testing can be framed as a filtering or sieving operation over the integers.

## Task Requirements
- Generate a sequence of primes via trial division.
- Test each candidate for primality by trying to divide it by other numbers (primes or any chosen divisors).
- The sequence may be bounded (up to a limit) or unbounded, and may begin at 2 or above a given value.
- The implementation may be organized as a filtering operation or a sieving operation.
- May reuse an `is_prime` function from the Primality by trial division task.

## Language Coverage
89 languages implement this task, reflecting very broad coverage typical of fundamental number-theory exercises. Representative implementations include Python, C, C++, Java, Haskell, Rust, Go, Ruby, Perl, and Raku.

## Connections
- [[PrimeNumber]] — the mathematical objects being generated
- [[TrialDivision]] — the primality-testing algorithm used
- [[SieveOfEratosthenes]] — a related alternative for prime generation
- [[NumberTheory]] — the broader domain of the task

## Contradictions
- None — reference task page.
