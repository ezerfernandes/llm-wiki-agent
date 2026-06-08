---
title: "Factorial primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Factorial_primes
---

## Summary
A factorial prime is a prime number that is exactly one less or one more than a factorial — that is, a non-negative integer n yields a factorial prime when either n! - 1 or n! + 1 is prime. The task asks the programmer to find these primes, noting the corresponding n and whether 1 was added or subtracted. The key practical insight is that factorials grow extremely fast, so the stretch goal quickly requires arbitrary-precision integers and probabilistic primality testing rather than deterministic checks.

## Task Requirements
- Find and show the first 10 factorial primes, starting counting from 1! (ignore 0! since both 0! and 1! equal 1).
- For each, show the prime itself, the factorial number n it corresponds to, and whether 1 is added or subtracted.
- Stretch goal: if the language supports arbitrary-sized integers, continue for at least the next 19 factorial primes.
- Numbers above roughly 2^64 may use a probable-prime test instead of deterministic primality.
- If a number has more than 40 digits, show only the first 20 and last 20 digits plus the total digit count.
- References OEIS:A088054 and the related task Sequence of primorial primes.

## Language Coverage
46 languages implement this task, spanning mainstream, functional, and esoteric ecosystems. Representative implementations include C++, Java, Python, Go, Haskell, Julia, Perl, Raku, Kotlin, and OCaml, with niche entries like LOLCODE, Uiua, RPL, and Frink.

## Connections
- [[FactorialPrime]] — the central sequence this task generates.
- [[Factorial]] — the underlying function whose neighbors are tested.
- [[PrimalityTesting]] — deciding whether n! ± 1 is prime.
- [[ProbabilisticPrimalityTest]] — needed for large candidates beyond deterministic feasibility.
- [[ArbitraryPrecisionArithmetic]] — required because factorials grow super-exponentially.

## Contradictions
- None — reference task page.
