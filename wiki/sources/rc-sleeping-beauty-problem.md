---
title: "Sleeping Beauty problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, monte-carlo, decision-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sleeping_Beauty_problem
---

## Summary
This task asks the programmer to write a Monte Carlo simulation of the classic Sleeping Beauty thought experiment from decision theory. A fair coin is tossed: on heads the subject is woken once (Monday), on tails she is woken twice (Monday and Tuesday) with her memory wiped between wakings. Each time she is woken she is asked to estimate the probability that the coin came up heads. The key insight the simulation reveals is that, counting per-waking rather than per-coin-toss, the proportion of heads converges to 1/3 (the "thirder" position) rather than 1/2.

## Task Requirements
- Simulate the experiment over many trials using a fair coin toss.
- On heads, register a single waking; on tails, register two wakings.
- Count the number of wakings that occurred after a heads toss versus the total number of wakings.
- Report the proportion of heads-on-waking as a credence or percentage, demonstrating convergence toward 1/3.

## Language Coverage
50 languages implement this task, showing broad coverage across paradigms and eras. Representative implementations include Python, C, C++, Java, Go, Haskell, Julia, Perl, Raku, Ruby, and Fortran, alongside niche entries such as J, Factor, and REXX.

## Connections
- [[MonteCarloMethod]] — the simulation technique used to estimate the proportion
- [[ProbabilityTheory]] — underlying framework for credence and conditional reasoning
- [[DecisionTheory]] — the field that originated the problem
- [[BayesianInference]] — relevant to the thirder/halfer credence debate
- [[RandomNumberGeneration]] — required for fair coin tossing

## Contradictions
- None — reference task page.
