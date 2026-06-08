---
title: "Dice game probabilities (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Dice_game_probabilities
---

## Summary
Compute the probability that one player's dice-sum total exceeds another's across two scenarios. In the first, player one rolls nine four-sided dice versus player two's six six-sided dice; in the second, five ten-sided dice versus six seven-sided dice. The key insight is to build each player's sum distribution (e.g., by repeated convolution or generating functions), then compare the two distributions over all outcome pairs to accumulate the win probability. The task is adapted from Project Euler Problem 205.

## Task Requirements
- For the first set (9 dice of 4 faces vs. 6 dice of 6 faces), compute the probability the first player's total strictly exceeds the second's (ties count as draws, not wins).
- For the second set (5 dice of 10 faces vs. 6 dice of 7 faces), compute the same win probability.
- Output both probabilities.

## Language Coverage
53 languages implement this task, spanning systems, functional, scripting, and array languages. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, J, and Julia.

## Connections
- [[ProbabilityDistribution]] — each player's dice sum forms a discrete distribution to be compared
- [[Convolution]] — combining single-die distributions into a multi-die sum distribution
- [[GeneratingFunctions]] — polynomial multiplication encodes the sum distribution efficiently
- [[Combinatorics]] — counting favorable vs. total outcome combinations
- [[Memoization]] — caching subproblem sum counts speeds recursive distribution building

## Contradictions
- None — reference task page.
