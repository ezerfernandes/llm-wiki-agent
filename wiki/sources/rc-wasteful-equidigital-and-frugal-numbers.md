---
title: "Wasteful, equidigital and frugal numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Wasteful,_equidigital_and_frugal_numbers
---

## Summary
This task classifies positive integers by comparing l(n), the number of digits of n in base b, against D(n), the total count of base-b digits across all of n's prime factors plus the digits of any exponent greater than 1. A number is wasteful (extravagant) if l(n) < D(n), equidigital if l(n) = D(n), and frugal if l(n) > D(n). The key insight is that the classification is base-dependent — for example, 32 is frugal in base 2 but equidigital in base 10 — and 1 is equidigital in every base by convention.

## Task Requirements
- Implement the digit count D(n): factor n, then sum base-b digit lengths of each prime factor and of each exponent greater than 1.
- Compute l(n), the count of base-b digits of n itself.
- For base 10, show the first 50 and the 10,000th number in each of the three categories (wasteful, equidigital, frugal).
- Count how many numbers below 1,000,000 fall into each category.
- Bonus: repeat the analysis for base 11, displaying results as base-10 values.
- Exclude 0 from all categories; treat 1 as equidigital in any base.

## Language Coverage
17 languages implement this task, spanning systems and functional styles as well as scientific and scripting languages. Representative entries include C++, Java, Python, Ruby, Perl, Raku, Julia, F#, Nim, Phix, and Wren.

## Connections
- [[IntegerFactorization]] — D(n) requires the prime factorization of n with exponents.
- [[PrimeNumbers]] — the prime factors and their exponents drive the digit count.
- [[NumberBases]] — classification depends on the base b used to count digits.
- [[NumberTheory]] — these are OEIS-cataloged integer sequences (A046758/A046759/A046760).

## Contradictions
- None — reference task page.
