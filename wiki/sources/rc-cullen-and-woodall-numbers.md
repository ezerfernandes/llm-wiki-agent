---
title: "Cullen and Woodall numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing, bignum]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cullen_and_Woodall_numbers
---

## Summary
The task asks the programmer to generate Cullen numbers (of the form n × 2^n + 1) and Woodall numbers (of the form n × 2^n − 1), which for any given n differ by exactly 2. The core challenge in the stretch goals is primality: Cullen and Woodall primes grow astronomically fast (the 3rd Cullen prime occurs at n = 4713 and has 1423 digits), so detecting them requires arbitrary-precision arithmetic and an efficient primality test.

## Task Requirements
- Write procedures to compute Cullen numbers (n × 2^n + 1) and Woodall numbers (n × 2^n − 1).
- Find and display the first 20 of each.
- Stretch: find the first 5 Cullen primes expressed by their index n.
- Stretch: find the first 12 Woodall primes expressed by their index n.
- Primes are reported by the value of n rather than the full evaluated number, since the numbers become very large.

## Language Coverage
46 languages implement this task, spanning systems languages, scripting languages, and math-oriented environments. Representative implementations include C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, PARI/GP, and Mathematica/Wolfram Language; the breadth shows which ecosystems offer convenient bignum and primality support.

## Connections
- [[NumberTheory]] — Cullen and Woodall numbers are classical integer sequences.
- [[PrimalityTesting]] — the stretch goals hinge on testing very large numbers for primality.
- [[ArbitraryPrecisionArithmetic]] — Cullen/Woodall primes exceed machine word sizes and require bignum support.
- [[OEIS]] — the task references sequences A002064, A003261, A005849, and A002234.

## Contradictions
- None — reference task page.
