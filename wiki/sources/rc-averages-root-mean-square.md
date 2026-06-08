---
title: "Averages/Root mean square (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Averages/Root_mean_square
---

## Summary
This task asks the programmer to compute the root mean square (RMS), also called the quadratic mean, of the integers 1 through 10. The RMS is obtained by averaging the squares of the values and then taking the square root of that mean. The key insight is that it is a simple two-pass (or single-pass accumulation) reduction: sum of squares divided by count, then square-rooted.

## Task Requirements
- Compute the root mean square of the numbers 1 to 10.
- Apply the formula: square each number, take the mean of those squares, then take the square root of that mean.
- The expected result is sqrt((1^2 + 2^2 + ... + 10^2) / 10) ≈ 6.2048.

## Language Coverage
145 languages implement this task, making it one of the broadly covered statistical-measure tasks on Rosetta Code, spanning everything from systems languages to array and stack languages. Representative implementations include C, C++, Rust, Go, Python, Haskell, Java, JavaScript, APL, and J.

## Connections
- [[RootMeanSquare]] — the quadratic mean this task defines
- [[ArithmeticMean]] — closely related averaging measure (mean of values vs mean of squares)
- [[StatisticalMeasures]] — family of related Rosetta Code averaging tasks
- [[Reduction]] — implemented as a fold/accumulate over the sequence
- [[SquareRoot]] — final operation applied to the mean of squares

## Contradictions
- None — reference task page.
