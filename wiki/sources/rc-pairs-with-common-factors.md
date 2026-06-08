---
title: "Pairs with common factors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pairs_with_common_factors
---

## Summary
This task asks the programmer to generate a sequence where term a(n) counts the pairs (x, y) with 1 < x < y <= n that share at least one common prime factor (i.e. are not coprime). The key insight is that rather than enumerating all O(n^2) pairs, each term can be computed directly via the closed-form formula a(n) = n(n-1)/2 + 1 − Σ(i=1..n) φ(i), where φ is Euler's totient function — counting coprime pairs and subtracting from the total. The sequence corresponds to OEIS A185670.

## Task Requirements
- Compute a(n) = the number of pairs (x, y), 1 < x < y <= n, having at least one common prime factor.
- Find and display the first one hundred terms of the sequence.
- Find and display the one thousandth term.
- Note that if p is prime, a(p) equals the previous term a(p-1).
- Stretch goal: find and display the ten thousandth, one hundred thousandth, and one millionth terms.

## Language Coverage
27 languages implement this task, spanning systems languages, functional languages, and array/math-oriented tools. Representative implementations include C, C++, Go, Java, Python, Rust-adjacent Nim, Julia, Perl, Raku, J, and Wren.

## Connections
- [[EulerTotientFunction]] — the formula relies on Φ to count coprime pairs
- [[NumberTheory]] — built on prime factorization and coprimality
- [[GreatestCommonDivisor]] — naive approaches test whether gcd(x,y) > 1
- [[SieveOfEratosthenes]] — efficient totient summation often uses a sieve
- [[IntegerSequences]] — the result is OEIS sequence A185670

## Contradictions
- None — reference task page.
