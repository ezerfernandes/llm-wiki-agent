---
title: "Wilcoxon Signed-Rank Test"
type: concept
tags: [statistics, hypothesis-testing, non-parametric]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# Wilcoxon Signed-Rank Test

A non-parametric hypothesis test for whether the mean difference between paired observations is zero. Used when samples are matched (paired) but the differences cannot be assumed normal. Equivalent in role to the paired *t*-test but rank-based rather than mean-based.

## Use in the [[2406.11695-mipro|MIPRO paper]]

The MIPRO paper uses Wilcoxon signed-rank tests *"between the averages of all runs for each example in the test set"* between MIPRO's run-averages and the second-best optimizer's run-averages on each task. This is the basis for the paper's significance claims — *"MIPRO wins on 5/7 tasks with Wilcoxon significance ($p < .05$)"*.

The pairing structure is per-example, not per-run — which gives the test more statistical power than aggregating to per-run scores first.

## Connections

- [[HypothesisTesting]] — parent concept.
- [[2406.11695-mipro|MIPRO]] — the wiki's reference paper for Wilcoxon's use in optimizer benchmarking.
- [[DSPyOptimizerBenchmark]] — the benchmark where Wilcoxon underwrites the significance claims.
