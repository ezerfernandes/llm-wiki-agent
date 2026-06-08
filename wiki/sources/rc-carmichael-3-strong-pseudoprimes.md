---
title: "Carmichael 3 strong pseudoprimes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Carmichael_3_strong_pseudoprimes
---

## Summary
The task asks the programmer to find Carmichael numbers that factor as a product of exactly three distinct primes, Prime1 × Prime2 × Prime3 with Prime1 < Prime2 < Prime3, enumerating all such numbers for every Prime1 up to 61. These composites are notable because they satisfy Fermat's Little Theorem for all bases coprime to them, defeating naive Fermat-based primality tests. The key insight is a constructive search (from Jameson's notes): for each Prime1, iterate over a helper value h3 and a divisor d, derive candidate Prime2 and Prime3 by closed-form formulas, and keep the triple only when both derived values are prime and a final congruence holds.

## Task Requirements
- For each Prime1 from the primes up to 61, find all Carmichael numbers of the form Prime1 × Prime2 × Prime3 with Prime1 < Prime2 < Prime3.
- Use the given pseudocode: loop 1 < h3 < Prime1, then 0 < d < h3 + Prime1.
- Accept a candidate only when (h3+Prime1)·(Prime1−1) mod d == 0 and −Prime1² mod h3 == d mod h3.
- Compute Prime2 = 1 + ((Prime1−1)·(h3+Prime1)/d) and reject if not prime.
- Compute Prime3 = 1 + (Prime1·Prime2/h3) and reject if not prime.
- Reject unless (Prime2·Prime3) mod (Prime1−1) == 1; otherwise the product is a Carmichael number.

## Language Coverage
51 languages implement this task, spanning systems and functional languages alongside scripting and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, J, Perl, Raku, and REXX.

## Connections
- [[CarmichaelNumber]] — the central object the task enumerates
- [[FermatsLittleTheorem]] — the primality criterion these composites fool
- [[PrimalityTesting]] — the broader context, including [[MillerRabinTest]]
- [[ModularArithmetic]] — congruence conditions drive the search
- [[NumberTheory]] — the mathematical domain of the problem

## Contradictions
- None — reference task page.
