---
title: "Duffinian numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Duffinian_numbers
---

## Summary
A Duffinian number is a composite number k that is relatively prime to its sigma sum (the sum of all divisors of k, including 1 and k itself). The key insight is to combine a compositeness test with a GCD check: compute sigma(k), then verify gcd(k, sigma(k)) equals 1. Duffinian numbers are common, and consecutive runs of them form Duffinian twins, triplets, and rarely quadruplets/quintuplets, but never six in a row.

## Task Requirements
- Find and show the first 50 Duffinian numbers.
- Find and show at least the first 15 Duffinian triplets (three consecutive Duffinian numbers).

## Language Coverage
47 languages implement this task, giving broad coverage across functional, imperative, and array paradigms. Representative implementations include C++, Python, Java, Haskell, Julia, Rust, Go, Perl, Raku, and Wren.

## Connections
- [[NumberTheory]] — Duffinian numbers are defined via divisor and primality properties.
- [[DivisorFunction]] — the sigma sum is the sum-of-divisors function σ(k).
- [[GreatestCommonDivisor]] — the relatively-prime test reduces to gcd(k, σ(k)) = 1.
- [[CompositeNumbers]] — only composite k qualify, excluding primes.

## Contradictions
- None — reference task page.
