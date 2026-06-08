---
title: "Modified random distribution (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, random-number-generation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Modified_random_distribution
---

## Summary
The task asks the programmer to bias a uniform random number generator so its output follows an arbitrary probability shape supplied by a `modifier(x)` function. The key technique is rejection sampling: draw two uniform values, keep the first only when a second uniform value falls below `modifier(first)`, and loop otherwise. With a 'V'-shaped modifier the resulting samples cluster near 0 and 1 and thin out near 0.5.

## Task Requirements
- Implement the given rejection-sampling loop over a uniform RNG `rgen()` producing values in 0.0..1.0.
- Define a 'V'-shaped modifier, e.g. `modifier(x) = 2*(0.5 - x)` for x < 0.5 else `2*(x - 0.5)`.
- Generate at least 10,000 numbers under the modified probability.
- Render a textual histogram with 11 to 21 bins showing the distribution, and show the output on the page.

## Language Coverage
32 languages implement this task, spanning systems, scripting, functional, and array languages. Representative examples include Python, Rust, Go, Haskell, Java, JavaScript, Julia, Perl, Raku, and R.

## Connections
- [[RejectionSampling]] — the core method for sampling from a target distribution
- [[ProbabilityDistribution]] — the modifier defines a non-uniform target density
- [[RandomNumberGeneration]] — builds on a uniform RNG primitive
- [[Histogram]] — used to visualize the empirical output distribution
- [[MonteCarloMethods]] — repeated random sampling to approximate a distribution

## Contradictions
- None — reference task page.
