---
title: "Deming's funnel (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Deming's_funnel
---

## Summary
Simulates W. Edwards Deming's classic management demonstration of dropping marbles through a funnel at a target, then applying four progressively more aggressive compensation rules to the funnel's position. The task asks the programmer to run all four rules over a fixed set of 50 pseudorandom (dx, dy) displacements and report the mean and standard deviation of the landing positions for each rule. The key insight is that deterministically over-adjusting for a random process makes results worse, not better — rules 2, 3, and 4 each degrade performance versus simply leaving the funnel still (rule 1).

## Task Requirements
- Apply four positioning rules to a provided set of 50 pseudorandom x and y displacements:
  - Rule 1: keep the funnel directly over the target.
  - Rule 2: shift the funnel to compensate for each drop's miss relative to its current position.
  - Rule 3: as rule 2, but first re-center over the target, then compensate relative to the target.
  - Rule 4: move the funnel directly over the last landing spot.
- For each rule, compute the mean and standard deviation of the resulting x and y values.
- Stretch goal 1: generate fresh pseudorandom data using a Gaussian radial displacement (sd 1.0) with a uniformly distributed angle.
- Stretch goal 2: show scatter plots of all four results.

## Language Coverage
45 languages implement this task, spanning systems, functional, scripting, and array/statistical languages. Representative solutions include C++, Rust, Go, Haskell, Java, Python, Julia, R, Racket, Perl, and Raku.

## Connections
- [[StandardDeviation]] — the core summary statistic computed per rule.
- [[GaussianDistribution]] — drives the stretch-goal random displacements.
- [[MonteCarloSimulation]] — randomized repeated-trial modeling of the funnel drops.
- [[FeedbackControl]] — the rules illustrate harmful over-compensation in a control loop.
- [[StatisticalProcessControl]] — Deming's demonstration of tampering with a stable process.

## Contradictions
- None — reference task page.
