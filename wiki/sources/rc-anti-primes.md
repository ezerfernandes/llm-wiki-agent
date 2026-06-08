---
title: "Anti-primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Anti-primes
---

## Summary
Anti-primes — also called highly composite numbers (OEIS A002182) — are the natural numbers that have strictly more divisors than every smaller natural number. The task is to generate and display the first twenty such numbers. The key insight is that each anti-prime sets a new record for the divisor count, so the core operation is counting divisors of successive integers and keeping only those that beat the previous maximum.

## Task Requirements
- Generate the first twenty anti-primes (highly composite numbers).
- A number qualifies if it has more divisors (factors) than any smaller natural number.
- Show the resulting sequence in the output.

## Language Coverage
107 languages implement this task, giving very broad coverage across assembly, functional, scripting, and mainstream compiled languages. Representative examples include C, C++, Python, Java, Haskell, Rust, Go, Julia, Perl, and Common Lisp.

## Connections
- [[HighlyCompositeNumbers]] — the formal name for the sequence being generated.
- [[DivisorCounting]] — the central operation: counting the number of factors of an integer.
- [[NumberTheory]] — the mathematical domain the task belongs to.
- [[FactorsOfAnInteger]] — a related Rosetta Code task that supplies the divisor-enumeration subroutine.
- [[SieveOfEratosthenes]] — a related technique sometimes used to accelerate factorization.

## Contradictions
- None — reference task page.
