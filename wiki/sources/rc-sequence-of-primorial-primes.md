---
title: "Sequence of primorial primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sequence_of_primorial_primes
---

## Summary
The task is to find the indices n for which the n'th primorial (the product of the first n primes) plus or minus one is itself prime. These indices form the sequence of primorial primes (OEIS A088411). The key insight is that the output consists of the small index values n, not the huge primorial numbers themselves, though arbitrary-precision arithmetic is required to test primality of the intermediate primorial±1 values.

## Task Requirements
- Generate and display the first ten values of the sequence.
- The sequence begins at n = 1 (resolving an ambiguity in references).
- For each candidate n, compute primorial(n) and test whether primorial(n) − 1 or primorial(n) + 1 is prime.
- Probabilistic primality tests are permitted provided the shown output is correct.
- Extended-precision integers are needed for intermediate results, but program output must show only the small indices.
- Optional extended task: show the first twenty members of the sequence.

## Language Coverage
35 languages implement this task, showing strong breadth across functional, imperative, and array paradigms. Representative implementations include C, C++, Go, Java, Python, Haskell, Julia, Perl, Raku, Ruby, Wren, and PARI/GP.

## Connections
- [[PrimeNumbers]] — the core domain; requires generating primes and primality testing
- [[Primorial]] — the running product of the first n primes that this task builds on
- [[BigIntegerArithmetic]] — arbitrary-precision math needed for the intermediate primorial values
- [[ProbabilisticPrimalityTest]] — Miller-Rabin-style tests allowed for checking primorial ± 1
- [[IntegerSequences]] — the result is OEIS sequence A088411

## Contradictions
- None — reference task page.
