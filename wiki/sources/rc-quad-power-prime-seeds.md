---
title: "Quad-power prime seeds (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Quad-power_prime_seeds
---

## Summary
The task asks the programmer to generate "quad-power prime seeds": positive integers n for which all four expressions n+n+1, n²+n+1, n³+n+1, and n⁴+n+1 evaluate to prime numbers simultaneously. The core challenge is iterating over candidate seeds and applying a primality test to each of the four derived values, short-circuiting as soon as one fails. This sequence corresponds to OEIS A219117.

## Task Requirements
- Find and display the first fifty quad-power prime seeds (or as many as the language's math capabilities reasonably support).
- Stretch: find and display the position and value of the first seed whose value exceeds one million, two million, and three million.

## Language Coverage
24 languages implement this task, giving solid coverage across mainstream and niche ecosystems. Representative implementations include C, Go, Java, Python, Julia, Perl, Raku, Ruby, Wren, and Mathematica / Wolfram Language, alongside specialized entries such as ALGOL 68, Factor, J, and RPL.

## Connections
- [[PrimeNumbers]] — every derived value must be prime
- [[PrimalityTest]] — the central operation applied to four expressions per candidate
- [[NumberTheory]] — the task concerns properties of integer-valued polynomials
- [[PolynomialEvaluation]] — n^k + n + 1 forms must be computed for k = 1..4
- [[OEIS]] — the sequence is cataloged as A219117

## Contradictions
- None — reference task page.
