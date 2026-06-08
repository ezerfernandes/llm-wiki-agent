---
title: "Random numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability-statistics, randomness]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Random_numbers
---

## Summary
This task asks the programmer to generate a collection of 1000 normally (Gaussian) distributed pseudo-random numbers with a mean of 1.0 and a standard deviation of 0.5. The key insight is that most language runtimes only provide uniformly distributed random numbers, so the solution typically requires a transform — such as the Box-Muller method or the polar (Marsaglia) method — to convert uniform draws into normally distributed ones, then rescale and shift to the desired mean and standard deviation.

## Task Requirements
- Generate a collection of exactly 1000 random numbers.
- The numbers must follow a normal (Gaussian) distribution.
- The distribution must have a mean of 1.0.
- The distribution must have a standard deviation of 0.5.
- If only uniform random numbers are available, apply a known algorithm to produce normally distributed values.

## Language Coverage
116 languages implement this task, reflecting very broad coverage across general-purpose, scientific, and niche languages. Representative implementations include C, C++, Java, Python, Ruby, Rust, Go, Haskell, MATLAB, and R.

## Connections
- [[NormalDistribution]] — the target probability distribution being sampled.
- [[BoxMullerTransform]] — common method for converting uniform deviates to Gaussian ones.
- [[StandardDeviation]] — the spread parameter the task specifies (0.5).
- [[PseudorandomNumberGeneration]] — the underlying source of randomness in most runtimes.

## Contradictions
- None — reference task page.
