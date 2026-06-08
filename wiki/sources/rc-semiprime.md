---
title: "Semiprime (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Semiprime
---

## Summary
A semiprime is a natural number that is the product of exactly two (possibly equal) prime numbers — for example 1679 = 23 × 73, the number chosen as the length of the Arecibo message. The task is to write a function that decides whether a given number is semiprime. The standard insight is to trial-divide out prime factors and confirm that the total count of prime factors (with multiplicity) is exactly two.

## Task Requirements
- Implement a function that takes a number and returns whether it is semiprime.
- A number qualifies if it equals the product of exactly two primes, which need not be distinct (so squares of primes like 4, 9, 25 count).
- Equivalently, recognize members of OEIS A001358, also called biprimes or 2-almost primes.

## Language Coverage
87 languages implement this task, giving very broad coverage across paradigms and eras — from low-level assembly to modern functional languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, Raku, REXX, and Wolfram Language.

## Connections
- [[PrimeNumbers]] — semiprimes are defined entirely in terms of prime factors
- [[PrimeFactorization]] — the natural algorithm counts prime factors with multiplicity
- [[TrialDivision]] — common method for extracting and counting factors
- [[NumberTheory]] — semiprimes belong to the family of "almost prime" classifications
- [[IntegerSequences]] — corresponds to OEIS sequence A001358

## Contradictions
- None — reference task page.
