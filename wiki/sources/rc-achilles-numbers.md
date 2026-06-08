---
title: "Achilles numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Achilles_numbers
---

## Summary
An Achilles number is a positive integer that is "powerful but imperfect": every prime factor p appears at least squared in its factorization (powerful), yet the number itself is not a perfect power m^k for integers m, k > 1 (imperfect). The task asks the programmer to enumerate these numbers and a stronger variant. The key insight is combining a powerful-number test (each prime factor's exponent ≥ 2) with a perfect-power exclusion, and for the strong variant chaining the property through the Euler totient.

## Task Requirements
- Find and show the first 50 Achilles numbers.
- Find and show at least the first 20 strong Achilles numbers — Achilles numbers whose Euler totient φ(n) is also an Achilles number.
- For digit lengths 2 through 5 (at least), show the count of Achilles numbers having that many digits.

## Language Coverage
37 languages implement this task, spanning low-level assembly, mainstream high-level languages, and array/functional and computer-algebra systems. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Julia, Raku, J, and PARI/GP.

## Connections
- [[PrimeFactorization]] — the powerful-number test rests on the exponents in the prime factorization.
- [[PowerfulNumbers]] — Achilles numbers are exactly the powerful numbers that are not perfect powers.
- [[PerfectPower]] — numbers expressible as m^k (k > 1) are excluded.
- [[EulerTotient]] — defines the strong Achilles variant via φ(n).
- [[NumberTheory]] — the broader domain of the task.

## Solved in (Rosetta Code languages)
Solved in **35** of the wiki's catalogued languages (Rosetta Code shows 37 language sections for this task). (2 further RC language section(s) are outside the wiki's popularity-list language set.)

[[AArch64 Assembly]], [[Ada]], [[ALGOL 68]], [[ARM Assembly]], [[Arturo]], [[Ballerina]], [[BASIC256]], [[C]], [[C++]], [[COBOL]], [[Crystal]], [[Delphi]], [[EasyLang]], [[Factor]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Nim]], [[PARI-GP]], [[Perl]], [[Phix]], [[Pluto]], [[Python]], [[Quackery]], [[Raku]], [[RPL]], [[Ruby]], [[Rust]], [[Sidef]], [[Wren]], [[XPL0]]

## Contradictions
- None — reference task page.
