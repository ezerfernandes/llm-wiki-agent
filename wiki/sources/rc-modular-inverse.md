---
title: "Modular inverse (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Modular_inverse
---

## Summary
The task asks the programmer to compute the modular multiplicative inverse of an integer a modulo m: the integer x such that a·x ≡ 1 (mod m), equivalently a·x = 1 + k·m for some integer k. The key insight is that this inverse exists if and only if a and m are coprime, and it is found via the extended Euclidean algorithm (or, when m is prime, via Fermat's little theorem). The concrete instance to solve is the inverse of 42 modulo 2017.

## Task Requirements
- Compute the modular inverse of 42 modulo 2017.
- Implementations may roll the algorithm by hand, use a dedicated library, or call a language built-in.
- Find x such that 42·x ≡ 1 (mod 2017).
- The coprimality precondition for existence may be assumed (the task says to ignore it).

## Language Coverage
105 languages implement this task, spanning systems languages, scripting languages, functional languages, and computer-algebra systems with native support. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Julia, Perl, and PARI/GP (the latter offering a built-in modular inverse).

## Connections
- [[ModularArithmetic]] — the inverse is defined in the ring of integers modulo m
- [[ExtendedEuclideanAlgorithm]] — standard method to compute the inverse and the Bézout coefficients
- [[GreatestCommonDivisor]] — coprimality (gcd = 1) is the existence condition
- [[FermatsLittleTheorem]] — gives the inverse as a^(m−2) mod m when m is prime
- [[NumberTheory]] — the broader mathematical domain of the task

## Contradictions
- None — reference task page.
