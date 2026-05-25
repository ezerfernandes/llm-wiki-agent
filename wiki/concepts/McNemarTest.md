---
title: "McNemar's Test"
type: concept
tags: [statistics, classification, paired-test, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# McNemar's Test

**Non-parametric test for paired nominal data** that detects differences in classification outcomes between two methods on the same examples. Used to evaluate whether one classifier is significantly better than another on a fixed test set.

## Use in MedVAL

[[2507.03152-medval]] §2.3.3 applies McNemar's test pairwise between **baseline vs MedVAL** for each of the 10 LMs × 4 risk levels (= 40 comparisons), with **Bonferroni correction** at Type I error $\alpha = 0.05$. Results reported via `statsmodels` in Python. Conclusion: distillation improvements are **$p < 0.001$ significant** on the smaller open-source LMs; the larger proprietary LMs show improvements that are not always significant after Bonferroni correction ($p > 0.1$).

## Connections
- [[2507.03152-medval]] — the application paper.
- [[NonInferiorityTest]] / [[KrippendorffAlpha]] / [[CohensKappa]] — sibling statistical tools.
- [[F1Score]] — the underlying metric the test compares.
