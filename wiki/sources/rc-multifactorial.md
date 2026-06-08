---
title: "Multifactorial (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Multifactorial
---

## Summary
The task generalizes the factorial: instead of multiplying every descending integer, a multifactorial of "degree" d multiplies terms that decrease by d each step (n, n-d, n-2d, ...) down to the smallest positive integer. The single exclamation mark gives the ordinary factorial (degree 1), double-factorial is degree 2, and so on. The key insight is parameterizing the step size, so one function with arguments n and degree covers the whole family. The task follows the Wolfram MathWorld definition rather than the differing Wikipedia formula.

## Task Requirements
- Write a function that, given n and the degree (number of exclamation marks / step size), computes the multifactorial.
- All terms in the product must remain positive integers.
- Use the function to generate and display a table of the first ten members (n = 1 to 10) for the first five degrees (1 through 5).

## Language Coverage
99 languages implement this task, showing very broad coverage across functional, imperative, and array-oriented paradigms. Representative implementations include Python, Haskell, C, Java, Go, Rust, Julia, J, Mathematica, and Raku.

## Connections
- [[Factorial]] — the degree-1 special case this task generalizes.
- [[NumberTheory]] — multifactorials are integer products studied in combinatorics and number theory.
- [[Recursion]] — natural recursive definition multiplying n by the multifactorial of n-degree.
- [[ProductSequence]] — the result is a stepped product of an arithmetic-like sequence of integers.

## Contradictions
- None — reference task page.
