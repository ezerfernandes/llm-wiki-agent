---
title: "Statistics/Normal distribution (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, random-number-generation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Statistics/Normal_distribution
---

## Summary
This task asks the programmer to generate a large set of normally (Gaussian) distributed random numbers starting only from a uniform random number generator, then compute the dataset's mean and standard deviation and display a histogram of the values. The key insight is that uniform deviates can be transformed into normal deviates using methods such as the Box-Muller transform or the central limit theorem (summing many uniform samples). The task also asks whether the language has native support for normal random number generation.

## Task Requirements
- Take a uniform random number generator and produce a large set of numbers following a normal (Gaussian) distribution.
- Calculate the dataset's mean and standard deviation.
- Show a histogram of the data.
- Mention any native language support for generating normally distributed random numbers.

## Language Coverage
47 languages implement this task, showing broad coverage across general-purpose, statistical, and scientific languages. Representative implementations include C, C++, Python, Julia, R, Haskell, Go, Rust, MATLAB / Octave, Mathematica / Wolfram Language, and SAS, with statistically oriented environments like R and Stata leaning on built-in normal generators.

## Connections
- [[NormalDistribution]] — the target distribution to be sampled.
- [[BoxMullerTransform]] — common method to derive normal deviates from uniform ones.
- [[CentralLimitTheorem]] — alternative basis: summing uniform samples approximates a normal distribution.
- [[RandomNumberGeneration]] — the underlying uniform generator being transformed.
- [[StandardDeviation]] — one of the summary statistics required.

## Contradictions
- None — reference task page.
