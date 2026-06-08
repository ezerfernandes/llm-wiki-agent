---
title: "P-value correction (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, multiple-comparisons]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/P-value_correction
---

## Summary
Given a list of p-values from many simultaneous hypothesis tests, adjust them to control the false-positive (Type 1 error) rate that inflates when many comparisons are made at once. The adjusted values (sometimes called q-values) are pushed upward but remain within [0,1]. The key insight is that several distinct procedures exist, each trading statistical power against control strength, and most rely on first sorting the p-values and applying rank-dependent scaling factors.

## Task Requirements
- Take one fixed list of 50 p-values supplied in the task.
- Return the p-values corrected for multiple comparisons.
- Support the recognized correction methods, typically: Benjamini-Hochberg (FDR), Benjamini-Yekutieli, Holm, Hochberg, Hommel, and Bonferroni.
- Ensure all corrected values stay in the [0,1] range.

## Language Coverage
23 languages implement this task, spanning systems and scientific languages plus statistics-focused environments. Representative implementations include C, C++, Go, Java, JavaScript, Julia, Python, R, Rust, SAS, and Stata.

## Connections
- [[PValue]] — the statistical quantity being adjusted
- [[FalseDiscoveryRate]] — the error rate the correction controls
- [[MultipleComparisonsProblem]] — the underlying statistical issue
- [[BonferroniCorrection]] — the simplest of the supported methods
- [[Sorting]] — most methods require ranking the p-values first

## Contradictions
- None — reference task page.
