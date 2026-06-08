---
title: "One-two primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/One-two_primes
---

## Summary
The task asks the programmer to generate the sequence a(n) in which each term is the smallest n-digit prime (base 10) composed entirely of the digits 1 and 2. The key insight is that for each digit length n there are 2^n candidates formed only from 1s and 2s, so an efficient solution enumerates these candidates in ascending order and returns the first one that passes a primality test. It is conjectured (but unproven) that such a prime exists for every n; no counterexamples are known up to several thousand digits.

## Task Requirements
- Find and show the first 20 elements of the sequence, covering n = 1 digit through n = 20 digits (or as many as the language reasonably supports).
- Stretch: show abbreviated values for n = 100 through 2000 in increments of 100.
- For the abbreviated display, replace any leading run of 1s with the count of those 1s and show the remainder of the number.

## Language Coverage
24 languages implement this task, spanning systems and compiled languages (C, Rust, Go, Ada, Nim), array/functional languages (J, Uiua, Quackery), and higher-level scripting and math languages (Python, Perl, Raku, Julia, Sidef, Mathematica/Wolfram Language, Wren). The stretch goal pushes toward bignum and probabilistic primality support since later terms reach thousands of digits.

## Connections
- [[PrimeNumbers]] — the sequence consists entirely of primes.
- [[PrimalityTesting]] — large candidates require probabilistic tests such as Miller-Rabin.
- [[CombinatorialGeneration]] — candidates are the 2^n strings over the digit alphabet {1, 2}.
- [[BignumArithmetic]] — the stretch goal works with numbers up to 2000 digits.
- [[OEIS]] — corresponds to sequence A036229.

## Contradictions
- None — reference task page.
