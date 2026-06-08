---
title: "Average loop length (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, monte-carlo, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Average_loop_length
---

## Summary
For a uniformly-random function f mapping {1..N} to {1..N}, the iterated sequence 1, f(1), f(f(1)), ... must eventually revisit a value because the domain is finite. The task is to estimate, for each N, the average number of steps until the first repeated value (the "rho" tail-plus-loop length). The key insight is that this expected length has a closed-form analytical expression, so a Monte Carlo simulation can be validated against the exact formula.

## Task Requirements
- For each N (the example runs N = 1..20), simulate many random mappings f: {1..N} → {1..N} and measure the length of the sequence until the first repetition.
- Report the average simulated length per N.
- Compute the same expected length analytically via a formula and (optionally) report the percent error between simulation and theory.

## Language Coverage
60 languages implement this task, giving broad coverage across functional, imperative, and scripting families. Representative implementations include C, C++, C#, Python, Java, Haskell, Julia, Rust, Go, Perl, and Raku.

## Connections
- [[MonteCarloMethod]] — the simulation half of the task averages over many random trials
- [[ProbabilityTheory]] — the analytical expectation derives from properties of random functions
- [[RandomMapping]] — iterating a random self-map produces the rho-shaped tail-and-cycle structure
- [[BirthdayProblem]] — the expected-collision length is closely related to birthday-paradox sums over N
- [[ExpectedValue]] — the closed-form result is the expectation of the first-repetition length

## Contradictions
- None — reference task page.
