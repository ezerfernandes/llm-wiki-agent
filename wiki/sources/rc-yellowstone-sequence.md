---
title: "Yellowstone sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Yellowstone_sequence
---

## Summary
The Yellowstone sequence (OEIS A098550), also called the Yellowstone permutation, is a permutation of the natural numbers. The task is to generate it: the first three terms are a(n) = n, and for n >= 4 each term is the smallest unused natural number that is relatively prime to the previous term a(n-1) yet shares a common factor with a(n-2). The key insight is the dual GCD constraint, which forces the characteristic spiking, geyser-like plot that gives the sequence its name.

## Task Requirements
- For n <= 3, set a(n) = n.
- For n >= 4, choose a(n) as the smallest number not already in the sequence such that gcd(a(n), a(n-1)) = 1 (relatively prime to the previous term) and gcd(a(n), a(n-2)) > 1 (not relatively prime to the term before that).
- Find and display the first 30 Yellowstone numbers.
- Extra: demonstrate plotting the first 100 terms with x = n and y = a(n).

## Language Coverage
61 languages implement this task, giving broad coverage across systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, J, and Wren.

## Connections
- [[GreatestCommonDivisor]] — the relatively-prime tests rely on GCD computation
- [[CoprimeIntegers]] — the dual coprimality / non-coprimality constraint defines each term
- [[NumberSequences]] — Yellowstone is an integer sequence cataloged as OEIS A098550
- [[Permutations]] — the sequence is a permutation of the natural numbers

## Contradictions
- None — reference task page.
