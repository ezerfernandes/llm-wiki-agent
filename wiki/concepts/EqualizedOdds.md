---
name: EqualizedOdds
title: "Equalized Odds"
type: concept
tags: [responsible-ai, fairness, metrics, evaluation]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Equalized Odds

A group-[[Fairness|fairness]] metric requiring **both equal [[TruePositiveRate|true positive rates]] and equal [[FalsePositiveRate|false positive rates]] across groups**. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], it was formalized by Hardt et al. (2016); the weaker [[EqualOpportunity|equal opportunity]] relaxes it to TPR alone.

## Key results
- **Impossibility theorem**: when group base rates differ, equalized odds and [[Calibration|calibration]] cannot both hold (Kleinberg et al. 2016; Chouldechova 2017). [[COMPAS]] satisfied calibration but violated equalized odds — disparate error rates were *mathematically inevitable*.
- **Postprocessing achievability**: equalized odds can be achieved by adjusting prediction thresholds per group ([[ThresholdAdjustment|threshold adjustment]]), requiring **no model retraining** — separating the fairness mechanism from the training pipeline and avoiding retraining cycles costing thousands of GPU-hours.

## Connections
- [[Fairness]] — parent concept.
- [[EqualOpportunity]] — the TPR-only relaxation.
- [[Calibration]] / [[DemographicParity]] — criteria it conflicts with under differing base rates.
- [[ConfusionMatrix]] / [[TruePositiveRate]] / [[FalsePositiveRate]] — computation.
- [[COMPAS]] — the canonical equalized-odds violation.
- [[ThresholdAdjustment]] — the postprocessing fix.
- [[mlsysbook-ch15-responsible-engineering]] — source.
