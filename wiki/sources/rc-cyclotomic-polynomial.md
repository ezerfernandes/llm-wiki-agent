---
title: "Cyclotomic polynomial (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, polynomials]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cyclotomic_polynomial
---

## Summary
The nth cyclotomic polynomial is the unique irreducible integer-coefficient polynomial of largest degree that divides x^n − 1 but divides no x^k − 1 for any k < n. The task asks the programmer to compute and display these polynomials. The key insight is the standard construction: x^n − 1 factors as the product of cyclotomic polynomials over all divisors d of n, so each cyclotomic polynomial can be obtained by dividing out the lower-order ones (polynomial division over the integers).

## Task Requirements
- Find and print the first 30 cyclotomic polynomials.
- Find and print the order n of the first 10 cyclotomic polynomials that contain n or -n as one of their coefficients (cf. OEIS A013594).

## Language Coverage
26 languages implement this task, a moderate spread covering systems, functional, scripting, and computer-algebra environments. Representative implementations include C++, C#, Go, Haskell, Java, JavaScript, Julia, Python, Perl, Raku, Rust, and Wren, plus algebra-oriented systems like Maple, Mathematica/Wolfram Language, and PARI/GP.

## Connections
- [[CyclotomicPolynomial]] — the mathematical object being computed
- [[NumberTheory]] — the branch of mathematics this task belongs to
- [[PolynomialDivision]] — the core operation used to extract each polynomial from x^n − 1
- [[RootsOfUnity]] — cyclotomic polynomials are the minimal polynomials of primitive nth roots of unity
- [[IrreduciblePolynomial]] — each cyclotomic polynomial is irreducible over the integers

## Contradictions
- None — reference task page.
