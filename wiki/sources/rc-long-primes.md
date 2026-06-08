---
title: "Long primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Long_primes
---

## Summary
A long prime (also called a full reptend prime, cyclic number, or maximal period prime) is a prime p whose reciprocal 1/p has a decimal period of exactly p-1, the greatest period any integer can have. The task asks the programmer to identify these primes by computing the repeating decimal period of 1/p. The key insight is that the period of 1/p equals the multiplicative order of 10 modulo p, so a prime is long precisely when 10 is a primitive root mod p.

## Task Requirements
- List all long primes up to 500 (preferably on one line).
- Report the count of long primes up to each of 500, 1000, 2000, 4000, 8000, 16000, and 32000.
- Optionally report the count up to 64000.
- Show all output.

## Language Coverage
51 languages implement this task, spanning compiled, functional, scripting, and array languages — including C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, Ruby, J, and REXX.

## Connections
- [[PrimeNumbers]] — long primes are a special subset of primes.
- [[MultiplicativeOrder]] — the decimal period of 1/p equals the order of 10 mod p.
- [[PrimitiveRoot]] — a prime is long iff 10 is a primitive root modulo it.
- [[ModularArithmetic]] — period computation relies on repeated modular operations.
- [[RepeatingDecimal]] — the period length of a unit fraction defines the property.

## Contradictions
- None — reference task page.
