---
title: "Monte Carlo methods (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, simulation, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Monte_Carlo_methods
---

## Summary
The task asks for a Monte Carlo simulation that estimates the value of pi by random sampling. The key insight is geometric: a circle inscribed in a square (with the circle's diameter equal to the square's side) occupies pi/4 of the square's area, so the fraction of uniformly random points that land inside the circle approximates pi/4. Multiplying that fraction by 4 yields an estimate of pi whose accuracy improves with more samples.

## Task Requirements
- Write a function that runs the simulation with a variable (parameterized) number of random sample points.
- For each sampled point inside the unit square, test whether it falls within the inscribed circle (e.g. x^2 + y^2 <= r^2).
- Estimate pi as 4 times the ratio of points inside the circle to total points.
- Show results for several different sample sizes to demonstrate convergence.
- Reference value provided for languages lacking a built-in pi: 3.141592653589793238462643383280.

## Language Coverage
91 languages implement this task, a very broad cross-section spanning systems, scripting, functional, statistical, and assembly languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Julia, R, MATLAB, and even EDSAC order code and 360 Assembly.

## Connections
- [[MonteCarloMethod]] — the core stochastic sampling technique being demonstrated
- [[EstimatingPi]] — the specific numerical target of this simulation
- [[RandomNumberGeneration]] — uniform random sampling underpins the method
- [[LawOfLargeNumbers]] — explains why the estimate converges as samples increase
- [[NumericalIntegration]] — Monte Carlo sampling as a form of approximate integration

## Contradictions
- None — reference task page.
