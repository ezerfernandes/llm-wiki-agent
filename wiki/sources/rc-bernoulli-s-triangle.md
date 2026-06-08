---
title: "Bernoulli's triangle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bernoulli's_triangle
---

## Summary
Bernoulli's triangle is an arithmetic figure similar to Pascal's triangle. It starts with a single 1 in row 0, and each new row n adds a 1 on the left and 2^n on the right; every interior element is the sum of the two elements directly above it. Equivalently, the entry at row n, column k equals the cumulative sum of binomial coefficients C(n,0) through C(n,k), so each row is the running partial sums of the corresponding Pascal's triangle row. Many integer sequences emerge within the triangle.

## Task Requirements
- Generate the first 15 rows of Bernoulli's triangle.
- Use whatever construction method is most convenient: row-recurrence (sum of two cells above, with 1 on the left and 2^n on the right) or the binomial partial-sum formula.

## Language Coverage
36 languages implement this task, spanning systems and scripting languages plus several BASIC and array-oriented dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and Wren.

## Connections
- [[PascalsTriangle]] — the closely related triangle whose row partial sums give Bernoulli's triangle
- [[BinomialCoefficient]] — entries are defined as cumulative sums of binomials C(n,k)
- [[Combinatorics]] — the figure arises from counting/binomial identities
- [[IntegerSequences]] — many OEIS sequences appear along its rows and diagonals

## Contradictions
- None — reference task page.
