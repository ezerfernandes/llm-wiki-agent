---
title: "Faulhaber's formula (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, polynomials]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Faulhaber's_formula
---

## Summary
Faulhaber's formula, named after Johann Faulhaber, expresses the sum of the p-th powers of the first n positive integers as a polynomial of degree (p+1) in n, with coefficients derived from Bernoulli numbers. The task is to generate and display the first 10 of these closed-form polynomial expressions, starting at p = 0. The key insight is that summing fixed powers always yields a polynomial one degree higher, and its coefficients can be computed exactly using Bernoulli numbers and binomial coefficients.

## Task Requirements
- Generate the first 10 closed-form expressions for the sum of p-th powers, starting with p = 0 (i.e. p = 0 through p = 9).
- Each expression should be the (p+1)-degree polynomial in n equal to the sum of the first n p-th powers.
- Coefficients are computed using Bernoulli numbers and binomial coefficients (exact rational arithmetic is expected).

## Language Coverage
39 languages implement this task, spanning systems languages, functional languages, computer-algebra systems, and scripting languages. Representative implementations include C, C++, Haskell, Java, Python, Julia, Perl, Raku, Rust, Mathematica/Wolfram Language, and Maxima.

## Connections
- [[BernoulliNumbers]] — the coefficients of each Faulhaber polynomial are built from Bernoulli numbers
- [[BinomialCoefficient]] — used together with Bernoulli numbers to assemble the polynomial coefficients
- [[PolynomialArithmetic]] — the result is a degree (p+1) polynomial requiring exact symbolic/rational manipulation
- [[RationalArithmetic]] — exact fractional coefficients must be tracked to print correct closed forms

## Contradictions
- None — reference task page.
