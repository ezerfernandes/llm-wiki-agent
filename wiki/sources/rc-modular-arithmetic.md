---
title: "Modular arithmetic (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, operator-overloading]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Modular_arithmetic
---

## Summary
Modular arithmetic operates on integers under a congruence relation: two numbers are congruent modulo m if they differ by an integer multiple of m, and the equivalence classes form the ring Z/mZ. The task asks the programmer to redefine the addition and multiplication operators (via a custom class or a library) so they work transparently on modular integers. The key insight is that the demonstration function f(x) = x^100 + x + 1 must be written agnostically, behaving identically whether given ordinary integers or modular ones, since it is just an algebraic expression valid over any ring.

## Task Requirements
- Implement modular integers, ideally by overloading/redefining the `+` and `*` operators (own class or dedicated library).
- Define a generic function f(x) = x^100 + x + 1 that does not know whether its argument is a plain integer or a modular integer.
- Use congruence modulus 13 and compute f(10).
- Multiplicative inverse is explicitly not required for this task.

## Language Coverage
48 languages implement this task, spanning classic systems and functional languages alike: C, C++, C#, Java, Rust, Go, Haskell, Common Lisp, Python, Ruby, Perl, and Julia are all represented.

## Connections
- [[ModularArithmetic]] — the core number-theoretic structure being modeled
- [[OperatorOverloading]] — the primary technique for making operators work on a custom modular type
- [[QuotientRing]] — Z/mZ as the algebraic ring formed by the equivalence classes
- [[FiniteField]] — Z/qZ becomes GF(q) when q is a prime power
- [[ModularExponentiation]] — related task needed to evaluate x^100 efficiently

## Contradictions
- None — reference task page.
