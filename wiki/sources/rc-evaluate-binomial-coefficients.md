---
title: "Evaluate binomial coefficients (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Evaluate_binomial_coefficients
---

## Summary
This task asks the programmer to compute any binomial coefficient C(n, k), the number of ways to choose k items from n. A concrete check is that C(5, 3) must yield 10. The key insight is that evaluating the multiplicative form n(n-1)...(n-k+1) / k! avoids computing three large factorials separately, reducing overflow and unnecessary work.

## Task Requirements
- Calculate an arbitrary binomial coefficient C(n, k).
- Demonstrate correctness by outputting C(5, 3), which equals 10.
- The recommended formula is C(n, k) = n! / ((n-k)! · k!), equivalently the product n(n-1)...(n-k+1) divided by k(k-1)...1.

## Language Coverage
127 languages implement this task, spanning systems languages, scripting languages, functional languages, computer algebra systems, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Python, Haskell, Java, Perl, Common Lisp, and Mathematica / Wolfram Language.

## Connections
- [[BinomialCoefficient]] — the quantity being computed
- [[Combinatorics]] — the branch of mathematics this task belongs to
- [[Factorial]] — appears in the closed-form definition
- [[PascalsTriangle]] — binomial coefficients are its entries (cited as a related task)
- [[CombinationsAndPermutations]] — directly referenced related task

## Contradictions
- None — reference task page.
