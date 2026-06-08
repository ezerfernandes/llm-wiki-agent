---
title: "Faulhaber's triangle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, rational-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Faulhaber's_triangle
---

## Summary
The task asks the programmer to generate Faulhaber's triangle, whose rows are the rational coefficients of the polynomials that give closed-form sums of integer powers (sum of k^p for k=1..n). These coefficients come from Faulhaber's formula, which expresses each power-sum polynomial using binomial coefficients and Bernoulli numbers. The key insight is that exact rational arithmetic is required, since the coefficients are fractions like 1/6, 1/2, -1/30.

## Task Requirements
- Show the first 10 rows of Faulhaber's triangle, where row p holds the coefficients of the polynomial for the sum of p-th powers.
- (Extra credit) Use the 18th row to compute the sum of k^17 for k from 1 to 1000.

## Language Coverage
40 languages implement this task, spanning systems, functional, scripting, and math-oriented languages. Representative implementations include C, C++, Rust, Go, Haskell, Java, Python, Perl, Raku, Julia, and Wolfram Language.

## Connections
- [[BernoulliNumbers]] — the formula's coefficients depend directly on Bernoulli numbers
- [[BinomialCoefficients]] — Faulhaber's formula sums over binomial coefficients
- [[RationalArithmetic]] — exact fractions are needed for the coefficients
- [[FaulhabersFormula]] — the closed-form identity the triangle encodes
- [[Polynomials]] — each row represents a power-sum polynomial

## Contradictions
- None — reference task page.
