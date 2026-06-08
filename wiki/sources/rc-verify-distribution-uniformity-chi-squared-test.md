---
title: "Verify distribution uniformity/Chi-squared test (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, hypothesis-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Verify_distribution_uniformity/Chi-squared_test
---

## Summary
This task asks the programmer to write a function that decides whether a set of observed frequency counts could plausibly have been produced by a uniform distribution, using Pearson's chi-squared goodness-of-fit test at a 5% significance level. The function returns a boolean that is true exactly when the data is consistent with uniformity given the appropriate degrees of freedom. The key insight is comparing the computed chi-squared statistic against the critical value (or p-value) of the chi-squared distribution with k-1 degrees of freedom.

## Task Requirements
- Implement a function taking a set of frequency counts.
- Compute the chi-squared statistic against the expected uniform frequencies (each bucket equally likely).
- Use the chi-squared distribution with the appropriate degrees of freedom (number of categories minus one).
- Apply a 5% significance level; normally a two-tailed test is used for this problem.
- Return a boolean: true if and only if the counts are plausibly from a uniform distribution.

## Language Coverage
36 languages implement this task, spanning systems and scientific languages alongside statistics-oriented ones. Representative implementations include C, C++, Rust, Go, Java, Python, R, Julia, Fortran, and Mathematica/Wolfram Language.

## Connections
- [[ChiSquaredTest]] — the statistical hypothesis test this task implements.
- [[GoodnessOfFit]] — the broader class of tests measuring fit to an expected distribution.
- [[UniformDistribution]] — the null hypothesis distribution being verified.
- [[HypothesisTesting]] — significance levels and degrees of freedom drive the decision.
- [[GammaFunction]] — the chi-squared CDF/p-value computation relies on the incomplete gamma function.

## Contradictions
- None — reference task page.
