---
title: "Statistics/Basic (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, random-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Statistics/Basic
---

## Summary
This task asks the programmer to generate samples of uniformly random real numbers in [0, 1], then compute their mean and standard deviation, and display a histogram of the data. Key insight: as the sample size grows, the standard deviation of a uniform [0, 1] distribution converges toward its theoretical value of 1/sqrt(12) (≈ 0.2887). An "extra" challenge highlights single-pass (streaming) computation of mean and variance so that arbitrarily large datasets can be processed without storing every value.

## Task Requirements
- Use the language's random number generator to produce real numbers in the range [0, 1] (open or closed range is fine).
- Generate samples of size 100, 1,000, and 10,000 (optionally larger), computing the mean and standard deviation for each.
- Display a histogram of one of these sample sets, typically binned into intervals.
- Observe and comment on the pattern in the standard deviation as sample size increases.
- Extra: Show how mean, stddev, and histogram can be computed in a single pass for a dataset too large to hold in memory (e.g. a trillion numbers), using the identity variance = mean(x^2) - mean(x)^2.

## Language Coverage
67 languages implement this task, spanning systems languages, scripting, functional, and array/statistics-oriented languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, R, MATLAB/Octave, and J.

## Connections
- [[StandardDeviation]] — the primary dispersion measure computed.
- [[ArithmeticMean]] — the central tendency measure computed.
- [[Histogram]] — the visualization required by the task.
- [[UniformDistribution]] — the [0, 1] source distribution whose stddev converges to 1/sqrt(12).
- [[StreamingAlgorithms]] — single-pass mean/variance computation for the extra challenge.

## Contradictions
- None — reference task page.
