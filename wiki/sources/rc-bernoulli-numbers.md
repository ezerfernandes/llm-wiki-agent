---
title: "Bernoulli numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, rational-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bernoulli_numbers
---

## Summary
This task asks the programmer to compute and display the Bernoulli numbers B0 through B60 as exact, reduced fractions. The key insight is that Bernoulli numbers are rational, so exact arbitrary-precision rational arithmetic (or big-integer numerators/denominators) is required rather than floating point. The task adopts the modern NIST convention where B1 = +1/2.

## Task Requirements
- Show the Bernoulli numbers B0 through B60.
- Suppress output of values equal to zero (all odd Bernoulli numbers except B1 are zero).
- Express each Bernoulli number as a reduced fraction (most are improper).
- Index each number so the reader can tell which Bn is shown.
- Optionally align the solidi (the fraction slashes) for extra credit.
- A suggested approach is the Akiyama–Tanigawa algorithm operating on a working array of rationals.

## Language Coverage
66 languages implement this task, spanning systems, scripting, functional, and computer-algebra ecosystems. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, Mathematica, Maxima, PARI/GP, and REXX.

## Connections
- [[BernoulliNumbers]] — the mathematical sequence being computed
- [[RationalArithmetic]] — exact fraction representation and reduction
- [[ArbitraryPrecisionArithmetic]] — numerators/denominators exceed machine integers near B60
- [[NumberTheory]] — domain in which Bernoulli numbers are central
- [[AkiyamaTanigawaAlgorithm]] — recurrence suggested for generating the values

## Contradictions
- None — reference task page.
