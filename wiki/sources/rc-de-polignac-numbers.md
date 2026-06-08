---
title: "De Polignac numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/De_Polignac_numbers
---

## Summary
A de Polignac number is a positive odd integer that cannot be expressed as the sum of a power of 2 and a prime number, disproving Alphonse de Polignac's 1800s conjecture that every positive odd integer could be so formed. The task is to generate these numbers (1 and 127 are early examples, and there are infinitely many). The key insight is that for a candidate odd number, you only need to test the finite set of powers of 2 less than it, checking whether the remainder is prime.

## Task Requirements
- Find and display the first fifty de Polignac numbers.
- Stretch: find and display the one-thousandth de Polignac number.
- Stretch: find and display the ten-thousandth de Polignac number.

## Language Coverage
61 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages — representatives include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, Ada, and Fortran.

## Connections
- [[NumberTheory]] — the task is rooted in additive number theory and a disproved conjecture.
- [[PrimeNumbers]] — each candidate requires a primality test on the remainder after subtracting a power of 2.
- [[PowersOfTwo]] — only powers of 2 below the candidate need to be enumerated.
- [[PrimalityTest]] — the core inner check determining whether a candidate qualifies.

## Contradictions
- None — reference task page.
