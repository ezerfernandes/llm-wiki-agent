---
name: FalsePositiveRate
title: "False Positive Rate (FPR)"
type: concept
tags: [metrics, evaluation, fairness, classification]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# False Positive Rate (FPR)

The fraction of actual negatives a classifier incorrectly flags as positive: $FPR = FP / (FP + TN)$. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], per-group FPR (with [[TruePositiveRate|TPR]]) defines [[EqualizedOdds|equalized odds]]; FPR differences under 5 percentage points is a common screening-system fairness threshold.

In [[COMPAS]], Black defendants who did not re-offend were flagged high-risk at 44.9% vs. 23.5% for White defendants — an FPR disparity that calibration alone could never have surfaced. In high-stakes domains the choice of which error to minimize (false positives vs. false negatives) is itself a value judgment: in criminal justice a false positive (wrongly jailing) is typically considered worse.

## Connections
- [[TruePositiveRate]] — paired error rate.
- [[ConfusionMatrix]] — source matrix.
- [[EqualizedOdds]] — requires equal FPR across groups.
- [[COMPAS]] — the canonical FPR-disparity case.
- [[Fairness]] — parent property.
- [[mlsysbook-ch15-responsible-engineering]] — source.
