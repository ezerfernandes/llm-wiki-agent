---
title: "Averages/Pythagorean means (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, statistics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Averages/Pythagorean_means
---

## Summary
This task asks the programmer to compute all three Pythagorean means — the arithmetic mean, geometric mean, and harmonic mean — over the integers 1 through 10 inclusive. The arithmetic mean is the sum divided by count, the geometric mean is the nth root of the product, and the harmonic mean is n divided by the sum of reciprocals. The key insight to demonstrate is the inequality A ≥ G ≥ H, which holds for any set of positive numbers.

## Task Requirements
- Compute the arithmetic mean of the set {1, …, 10}: the sum of the list divided by its length.
- Compute the geometric mean: the nth root of the product of the elements.
- Compute the harmonic mean: n divided by the sum of the reciprocals of the elements.
- Show that the arithmetic mean ≥ geometric mean ≥ harmonic mean for this set of positive integers.

## Language Coverage
126 languages implement this task, giving very broad coverage across paradigms — from systems and functional languages to BASIC dialects and array languages. Representative implementations include C, C++, Python, Haskell, Java, JavaScript, Rust, Julia, J, and APL.

## Connections
- [[ArithmeticMean]] — one of the three required means
- [[GeometricMean]] — nth root of the product, the second required mean
- [[HarmonicMean]] — reciprocal-based third required mean
- [[AmGmInequality]] — the A ≥ G ≥ H ordering the task asks to demonstrate
- [[NumericalAnalysis]] — root and reciprocal computations involve floating-point precision

## Contradictions
- None — reference task page.
