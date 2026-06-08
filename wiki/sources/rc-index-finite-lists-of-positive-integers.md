---
title: "Index finite lists of positive integers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Index_finite_lists_of_positive_integers
---

## Summary
The task exploits the fact that the set of all finite lists of positive integers is countable, meaning each such list can be put into one-to-one correspondence with a natural number. The programmer must implement a `rank` function that maps any finite list of arbitrarily large positive integers to a single integer, and an `unrank` function that inverts it. The key insight is choosing an encoding scheme (e.g. prime factorization, interleaved-digit, or pairing-function approaches) that is reversible.

## Task Requirements
- Write a `rank` function assigning an integer to any finite, arbitrarily long list of arbitrarily large positive integers.
- Write an `unrank` function that is the exact inverse of `rank`.
- Demonstrate by picking a random-length list of random positive integers, ranking it to an integer, then unranking back to recover the original list.
- Extra credit: make `rank` a true bijection and show `unrank(n)` for n from 0 to 10.

## Language Coverage
29 languages implement this task, spanning functional, imperative, and array-oriented styles. Representative implementations include Haskell, Python, Julia, Go, Java, Perl, Raku, J, Racket, and Wren.

## Connections
- [[Countability]] — the mathematical premise that finite integer lists form a countable set
- [[Bijection]] — the extra-credit requirement for a one-to-one, onto mapping
- [[InverseFunction]] — `unrank` must precisely invert `rank`
- [[PairingFunction]] — a common technique (e.g. Cantor pairing) for encoding sequences as single integers
- [[PrimeFactorization]] — an alternative encoding using prime exponents to represent list elements

## Contradictions
- None — reference task page.
