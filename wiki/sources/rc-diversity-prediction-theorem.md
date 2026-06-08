---
title: "Diversity prediction theorem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, decision-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Diversity_prediction_theorem
---

## Summary
This task implements Scott E. Page's diversity prediction theorem, which formalizes the "wisdom of the crowd": the squared error of a crowd's collective prediction equals the average individual squared error minus the predictive diversity. The key insight is that greater diversity among independent estimates reduces collective error, so a crowd of diverse opinions can outperform individual experts.

## Task Requirements
- Given a true value and a set of crowd estimates, compute and display the true value and the estimates.
- Compute the average individual error: the mean of the individual squared errors against the true value.
- Compute the collective (crowd) error: the squared error of the mean prediction against the true value.
- Compute the prediction diversity: the average squared distance from each individual prediction to the collective prediction.
- Verify Collective Error = Average Individual Error − Prediction Diversity.
- Demonstrate with at least two examples: true value 49 with estimates {48, 47, 51}, and true value 49 with estimates {48, 47, 51, 42}.

## Language Coverage
56 languages implement this task, spanning a broad mix of mainstream, functional, scientific, and esoteric languages. Representative implementations include C, C++, Java, Python, JavaScript, Haskell, Julia, R, Go, and Raku.

## Connections
- [[WisdomOfTheCrowd]] — the social-science phenomenon the theorem explains
- [[MeanSquaredError]] — the error metric underlying every term in the identity
- [[Variance]] — prediction diversity is the variance of the estimates about their mean
- [[DescriptiveStatistics]] — averaging and squared-deviation computations drive the task

## Contradictions
- None — reference task page.
