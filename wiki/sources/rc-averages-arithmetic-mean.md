---
title: "Averages/Arithmetic mean (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Averages/Arithmetic_mean
---

## Summary
This task asks the programmer to compute the arithmetic mean (the average) of a numeric vector: the sum of all elements divided by their count. The key wrinkle is the edge case of a zero-length input — since the mean of an empty set is ill-defined, the program may behave however it sees fit, ideally following the language's established convention for signaling math errors or undefined values (e.g. NaN, division-by-zero error, or empty result).

## Task Requirements
- Write a program that finds the mean (arithmetic average) of a numeric vector.
- Handle the zero-length input case: behavior is unspecified, but should follow the language's convention for math errors or undefined values when one exists.

## Language Coverage
213 languages implement this task, making it one of the most broadly covered entries on the site — reflecting its standing as a "Simple" probability-and-statistics primitive. Representative implementations span C, Python, Haskell, Java, Ruby, Go, Rust, APL, J, and MATLAB.

## Connections
- [[ArithmeticMean]] — the core statistical measure being computed
- [[SummationAndDivision]] — the underlying sum-divided-by-count operation
- [[ErrorHandling]] — handling the undefined empty-vector case via NaN or exceptions
- [[StatisticalMeasures]] — part of the related family of statistics tasks (mean, median, mode)

## Contradictions
- None — reference task page.
