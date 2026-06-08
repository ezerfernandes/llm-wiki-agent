---
title: "Blum integer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Blum_integer
---

## Summary
A Blum integer is a semiprime n = p × q whose two distinct prime factors are each congruent to 3 mod 4 (i.e., of the form 4t + 3). The task asks the programmer to generate these integers in order: list the first 50, identify the 26,828th, and as a stretch goal find the 100,000th through 400,000th. The key insight is recognizing that a valid factor must satisfy both primality and the residue condition p ≡ 3 (mod 4).

## Task Requirements
- Find and display the first 50 Blum integers.
- Display the 26,828th Blum integer.
- Stretch: find the 100,000th, 200,000th, 300,000th, and 400,000th Blum integers.
- Stretch: for the first 400,000 Blum integers, show the percentage distribution (to 3 decimal places) by final decimal digit — which can only be 1, 3, 7, or 9.

## Language Coverage
38 languages implement this task, spanning systems languages, functional languages, scripting languages, and computer-algebra systems. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, Mathematica/Wolfram Language, and REXX.

## Connections
- [[Semiprime]] — a Blum integer is a special case of a semiprime
- [[PrimeFactorization]] — determining p and q requires factoring n
- [[ModularArithmetic]] — the 3 mod 4 congruence condition on each factor
- [[NumberTheory]] — Blum integers arise in number-theoretic cryptography
- [[PrimalityTest]] — each candidate factor must be verified prime

## Contradictions
- None — reference task page.
