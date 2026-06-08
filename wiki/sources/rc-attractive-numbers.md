---
title: "Attractive numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Attractive_numbers
---

## Summary
The task defines an "attractive number" as one whose total count of prime factors — counted with multiplicity, not just distinct ones — is itself a prime number. For example, 20 = 2 × 2 × 5 has three prime factors, and since 3 is prime, 20 is attractive. The core insight is that the property depends on bigomega(n) (the number of prime factors with multiplicity) being prime.

## Task Requirements
- Determine, for each number, the count of its prime factors counting multiplicity.
- Test whether that count is itself a prime number.
- Show all attractive numbers in the sequence up to and including 120.

## Language Coverage
98 languages implement this task, reflecting very broad coverage across mainstream, functional, assembly, and esoteric languages. Representative implementations include Python, C, C++, Rust, Go, Haskell, Java, Julia, Perl, Raku, and lower-level entries like 8080 Assembly and LLVM.

## Connections
- [[PrimeFactorization]] — counting prime factors with multiplicity is the central operation
- [[PrimeNumbers]] — the count of factors must itself be tested for primality
- [[NumberTheory]] — the task is a classic integer-property sequence problem
- [[OEIS]] — corresponds to OEIS sequence A063989

## Contradictions
- None — reference task page.
