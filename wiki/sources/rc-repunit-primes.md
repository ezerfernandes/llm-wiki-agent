---
title: "Repunit primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Repunit_primes
---

## Summary
A repunit is a number consisting entirely of the digit 1 in a given base (1, 11, 111, ...), expressible as (b^n - 1)/(b - 1). This task asks the programmer to find, for each base from 2 through 16, which repunits are prime, reporting them compactly by their digit count n rather than the full value. The key insight is that a repunit can only be prime if its digit count n is itself prime, so only prime n need to be tested, and in base 2 these correspond exactly to the Mersenne prime exponents.

## Task Requirements
- For each base 2 through 16, find the repunit primes expressed as digit counts, up to a limit of n = 1000.
- Display the results on the page, grouped by base.
- Optionally test only prime digit counts, since composite digit counts always yield composite repunits.
- Stretch goal: raise the limit to 2700 (or as high as patience allows).

## Language Coverage
27 languages implement this task, spanning systems and compiled languages, functional languages, scripting languages, and math-oriented tools. Representative implementations include C++, Go, Java, Julia, Python, Perl, Raku, Ruby, Scheme, F#, Mathematica/Wolfram Language, and PARI/GP.

## Connections
- [[RepunitNumbers]] — the central object: numbers of the form (b^n - 1)/(b - 1).
- [[PrimalityTesting]] — each candidate repunit must be checked for primality, often with probabilistic tests for large n.
- [[MersennePrimes]] — base-2 repunit primes are exactly the Mersenne primes 2^p - 1.
- [[CircularPrimes]] — repunit primes are by definition also circular primes.
- [[NumberTheory]] — the divisibility argument that composite digit counts force composite repunits.

## Contradictions
- None — reference task page.
