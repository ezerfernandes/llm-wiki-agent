---
title: "Permutation test (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Permutation_test
---

## Summary
The task asks the programmer to implement a permutation test, a nonparametric statistical procedure that judges whether a medical treatment had a significantly stronger effect than a placebo. Given fixed treatment and control measurements, the program exhaustively considers every way the pooled volunteers could have been split into groups of the same two sizes and recomputes the difference in group means each time. The key insight is that under the null hypothesis (no treatment effect) every such relabeling is equally likely, so the fraction of relabelings producing a difference at least as extreme as the observed one is a p-value computed without distributional assumptions.

## Task Requirements
- Use the supplied table of treatment (n=9) and control (m=10) measurements, which may be hardcoded.
- Enumerate every alternative assignment of the n+m pooled values into a treatment group of size n and a control group of size m; the count equals the binomial coefficient C(n+m, n).
- For each assignment, compute the mean of each group and the difference (treatment mean minus control mean).
- Report the percentage of groupings whose difference is less than or equal to the observed difference, and the percentage strictly greater; the two must sum to 100%.
- No conclusion need be drawn from the result.

## Language Coverage
47 languages implement this task, spanning systems languages, scripting languages, functional languages, and statistics-oriented tools. Representative implementations include Python, R, C, C++, Rust, Go, Haskell, Julia, Perl, and Common Lisp.

## Connections
- [[PermutationTest]] — the statistical method being implemented
- [[BinomialCoefficient]] — counts the number of alternative groupings, C(n+m, n)
- [[HypothesisTesting]] — the inferential framework producing the p-value
- [[Combinations]] — generating each subset assignment of the pooled data
- [[NonparametricStatistics]] — the broader class of distribution-free tests

## Contradictions
- None — reference task page.
