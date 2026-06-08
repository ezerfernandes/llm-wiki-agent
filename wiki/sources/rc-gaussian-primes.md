---
title: "Gaussian primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, complex-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Gaussian_primes
---

## Summary
The task asks the programmer to identify Gaussian primes — prime elements among the Gaussian integers (complex numbers a + bi with integer parts). The key insight is the classification rule: when both a and b are non-zero, the number is a Gaussian prime exactly when its norm a² + b² is an ordinary prime; when one part is zero, the other must be a rational prime of the form 4n + 3 (times a unit). Rational primes not of that form, such as 5 = (2+i)(2−i), split and are therefore not Gaussian primes.

## Task Requirements
- Find and display all Gaussian primes whose norm is less than 100 (i.e. within radius 10 of the origin on the complex plane).
- Plot the Gaussian prime points on a Cartesian real/imaginary plane out to at least radius 50.
- Exploit the octogonal symmetry: if a² + b² is prime, so are the swapped, negated, and conjugate variants.

## Language Coverage
26 languages implement this task, spanning systems, functional, array, and scripting families — including C, C++, Rust, Nim, Java, F#, Common Lisp, Julia, Python, Perl, Raku, J, and Wren. The plotting requirement also draws in graphics-capable environments like Mathematica/Wolfram Language and Uiua.

## Connections
- [[ComplexNumbers]] — Gaussian integers are complex numbers with integer real and imaginary parts.
- [[GaussianIntegers]] — the ring Z[i] in which these primes live.
- [[PrimeNumbers]] — the norm test reduces Gaussian primality to ordinary primality.
- [[NumberTheory]] — the 4n+3 classification stems from sums-of-two-squares theory.
- [[FermatsTheoremOnSumsOfTwoSquares]] — explains why primes ≡ 1 mod 4 split while ≡ 3 mod 4 remain prime.

## Contradictions
- None — reference task page.
