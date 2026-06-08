---
title: "Multiplicative order (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Multiplicative_order
---

## Summary
The multiplicative order of an integer `a` relative to a modulus `m` is the least positive integer `n` such that `a^n ≡ 1 (mod m)`. For example, the order of 37 modulo 1000 is 100. The task asks for an implementation that stays efficient for large numbers by exploiting structure rather than brute-force searching.

## Task Requirements
- Compute the least `n > 0` with `a^n ≡ 1 (mod m)` (assuming `a` and `m` are coprime).
- Use the efficient algorithm: via the Chinese Remainder Theorem, compute the order for each prime power `p^k` of `m`, then combine the per-component results with the least common multiple.
- For each prime power, note that the order must divide Euler's totient `φ(p^k)`; factor that bound and, for each prime factor `q^e`, find the least `d` such that `(q^d)·(t/q^e)` works as an exponent.
- Routines for prime-power factorization may be assumed available from a library.

## Language Coverage
37 languages implement this task, spanning systems, functional, scripting, and CAS/math-oriented languages. Representative entries include C, C++, C#, Java, Python, Haskell, Go, Julia, Perl, Raku, REXX, and Mathematica/Wolfram Language.

## Connections
- [[ModularArithmetic]] — the order is defined by congruence modulo `m`.
- [[ChineseRemainderTheorem]] — splits the problem across prime-power components of `m`.
- [[EulerTotient]] — `φ(p^k)` bounds the order, which must divide it.
- [[LeastCommonMultiple]] — recombines per-prime-power orders.
- [[ModularExponentiation]] — the binary/fast-power method underlies the checks.

## Contradictions
- None — reference task page.
