---
title: "Smith numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Smith_numbers
---

## Summary
A Smith number is a composite number whose digit sum equals the sum of the digits of all its prime factors (counted with multiplicity). For example, 166 = 2 × 83, and its digit sum 1+6+6 = 13 matches the prime-factor digit sum 2+8+3 = 13. The key insight is that primes are excluded by definition, since a prime trivially equals its own only factor.

## Task Requirements
- Compute the sum of the decimal digits of a number.
- Factor a number into its prime factors (with multiplicity), excluding the number itself.
- Sum the decimal digits across all those prime factors and compare to the number's own digit sum.
- Find and output all Smith numbers below 10000.

## Language Coverage
75 languages implement this task, spanning systems, functional, scripting, and assembly families. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, REXX, and 360 Assembly.

## Connections
- [[PrimeFactorization]] — the core subroutine for decomposing each candidate.
- [[DigitSum]] — comparison of decimal digit sums drives the membership test.
- [[NumberTheory]] — Smith numbers are a studied integer sequence (OEIS A006753).
- [[CompositeNumbers]] — only composites can qualify, as primes are excluded.

## Contradictions
- None — reference task page.
