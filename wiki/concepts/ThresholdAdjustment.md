---
name: ThresholdAdjustment
title: "Threshold Adjustment (Bias Mitigation)"
type: concept
tags: [responsible-ai, fairness, bias-mitigation, postprocessing]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Threshold Adjustment (Bias Mitigation)

A **postprocessing** [[Fairness|fairness]]-mitigation technique that sets different classification thresholds per group to equalize a chosen metric (e.g. lower Group B's threshold to match [[TruePositiveRate|TPR]]). Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], it requires **no model retraining** — separating the fairness mechanism from the training pipeline and avoiding retraining cycles costing thousands of GPU-hours (Hardt et al. 2016 showed [[EqualizedOdds|equalized odds]] is achievable this way).

Trade-off: equalizing TPR for a disadvantaged group typically raises that group's false positives — the "price of fairness" utility tax. It must be revalidated when deployment demographics or label processes change. A single fixed threshold on populations with different score distributions is "simultaneously correct for the combined population while systematically wrong for each subpopulation."

## Connections
- [[Fairness]] / [[EqualizedOdds]] / [[EqualOpportunity]] — what it equalizes.
- [[AdversarialDebiasing]] / [[Reweighting]] — sibling (in-/pre-processing) families.
- [[ParetoFrontier]] — the trade-off it traverses.
- [[mlsysbook-ch15-responsible-engineering]] — source.
