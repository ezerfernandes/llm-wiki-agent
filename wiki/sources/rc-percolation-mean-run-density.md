---
title: "Percolation/Mean run density (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, monte-carlo, probability]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Percolation/Mean_run_density
---

## Summary
Given a random binary vector of length n where each element is 1 with probability p (and 0 otherwise), a "run" is a maximal group of consecutive 1s bounded by 0s or the vector ends. The task is to estimate the mean run density K(p) = R_n / n through Monte Carlo simulation and verify that it converges to the theoretical limit p(1 - p) as n grows. The key insight is that simulated values are noisy for finite n, so each estimate must be averaged over many trials (t >= 100).

## Task Requirements
- Generate a vector of n values that are 1 with probability p, else 0.
- Count R_n, the number of runs of consecutive 1s in the vector.
- Compute R_n / n averaged over t >= 100 trials to reduce randomness.
- For p in {0.1, 0.3, 0.5, 0.7, 0.9}, vary n and show how the estimate approaches the theoretical K(p) = p(1 - p).
- Display the simulated results alongside the expected analytic value.

## Language Coverage
31 languages implement this task, spanning systems, scripting, and functional styles. Representative implementations include C, C++, D, Go, Rust-adjacent FreeBASIC, Haskell, Java, JavaScript, Julia, Python, Perl, Raku, Racket, and Wren.

## Connections
- [[MonteCarloSimulation]] — estimates K(p) by averaging over many random trials.
- [[PercolationTheory]] — the broader family of percolation simulation tasks this belongs to.
- [[ProbabilityDistributions]] — each cell is an independent Bernoulli(p) trial.
- [[RandomNumberGeneration]] — required to populate the binary vector stochastically.

## Contradictions
- None — reference task page.
