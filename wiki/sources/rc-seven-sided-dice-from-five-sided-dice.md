---
title: "Seven-sided dice from five-sided dice (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, random-number-generation, rejection-sampling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Seven-sided_dice_from_five-sided_dice
---

## Summary
Given a uniform generator `dice5` that returns integers 1–5, the task is to build `dice7` that returns integers 1–7 with equal probability, using only `dice5` as the source of randomness. The key insight is rejection sampling: roll `dice5` twice to produce one of 25 equiprobable outcomes, discard 4 of them, and partition the remaining 21 into 7 groups of 3 so each value 1–7 is equally likely. The result must be validated as uniform over at least one million calls.

## Task Requirements
- Implement `dice7` using only `dice5` (an equal-probability 1–5 generator) for entropy.
- `dice7` must return integers 1–7 with equal probability.
- Verify the output distribution is uniform across at least 1,000,000 calls using the Simple Random Distribution Checker.
- Suggested approach: call `dice5` twice (25 outcomes), reject 4 combinations, split the other 21 into 7 groups of 3, return the group index.

## Language Coverage
58 languages implement this task, spanning systems, functional, scripting, BASIC-family, and even hardware-description languages. Representative entries include C, C++, Go, Rust-adjacent D, Haskell, Python, Ruby, Java, JavaScript, Julia, and Verilog.

## Connections
- [[RejectionSampling]] — the core technique for discarding biased outcomes
- [[UniformDistribution]] — the property the generated dice must satisfy
- [[RandomNumberGeneration]] — building one RNG from another
- [[ProbabilityAndStatistics]] — the task category and verification basis
- [[ChiSquaredTest]] — typical method for checking distribution uniformity

## Contradictions
- None — reference task page.
