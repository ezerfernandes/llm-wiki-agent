---
title: "Probabilistic choice (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, random-sampling, statistics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Probabilistic_choice
---

## Summary
The task asks the programmer to draw items from a discrete distribution: given a mapping of items to their target probabilities (which sum to one), generate a million random samples and compare the empirical frequencies against the target probabilities. The key technique is weighted random selection, typically implemented by accumulating a cumulative distribution and locating where a uniform random number falls within it.

## Task Requirements
- Accept a mapping of items to their required probability of occurrence.
- The probabilities must total one (subject to floating-point rounding).
- Generate one million items randomly according to those probabilities.
- Report the generated (empirical) frequency of each item alongside its target probability for comparison.
- Use the supplied test mapping (aleph 1/5, beth 1/6, gimel 1/7, daleth 1/8, he 1/9, waw 1/10, zayin 1/11, and heth 1759/27720 adjusted so the probabilities sum to 1).

## Language Coverage
78 languages implement this task, spanning systems languages, scripting languages, functional languages, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Julia, R, Perl, and Ruby.

## Connections
- [[ProbabilityDistribution]] — sampling from a discrete distribution
- [[CumulativeDistributionFunction]] — the standard mechanism for mapping a uniform draw to an item
- [[WeightedRandomSelection]] — the core algorithm the task exercises
- [[PseudorandomNumberGenerator]] — supplies the uniform random values
- [[MonteCarloMethod]] — comparing empirical frequencies to targets over many trials

## Contradictions
- None — reference task page.
