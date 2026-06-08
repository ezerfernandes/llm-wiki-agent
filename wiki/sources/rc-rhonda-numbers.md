---
title: "Rhonda numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rhonda_numbers
---

## Summary
A positive integer n is a Rhonda number to base b when the product of its base-b digits equals b times the sum of n's prime factors (counted with multiplicity). For example, 25662 is Rhonda to base 10 because its digit product 2x5x6x6x2 = 720 equals 10 x (2+3+7+13+47), the base times the sum of its prime factors. The key insight is that Rhonda numbers only exist in composite (non-prime) bases.

## Task Requirements
- For each non-prime base b from 2 through 16, find and display at least the first 10 Rhonda numbers to base b, shown at least in base 10.
- Implementation requires factoring n into primes, summing those factors, computing the product of n's digits in base b, and testing equality against b times the prime-factor sum.
- Stretch goal: extend the search out to base 36.

## Language Coverage
23 languages implement this task, giving solid breadth across compiled, scripting, array, and functional paradigms. Representative implementations include ALGOL 68, C++, Go, Java, Python, Rust, Perl, Raku, Julia, J, and Wren.

## Connections
- [[PrimeFactorization]] — summing prime factors with multiplicity is the core arithmetic step
- [[NumberTheory]] — Rhonda numbers are a base-dependent integer property
- [[RadixConversion]] — extracting the base-b digits of n requires positional radix decomposition
- [[SmithNumbers]] — explicitly listed as a related digit/prime-factor task
- [[IntegerSequences]] — catalogued across many OEIS sequences (one per base)

## Contradictions
- None — reference task page.
