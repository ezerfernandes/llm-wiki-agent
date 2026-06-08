---
name: EqualOpportunity
title: "Equal Opportunity"
type: concept
tags: [responsible-ai, fairness, metrics, evaluation]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Equal Opportunity

A group-[[Fairness|fairness]] metric requiring **equal [[TruePositiveRate|true positive rates]] across groups** — i.e. among *qualified* individuals, the selection rate should not depend on group membership. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], it is the weaker relaxation of [[EqualizedOdds|equalized odds]] (TPR only, not also FPR), formalized by Hardt et al. (2016).

In the chapter's loan example, Group A achieves 90% TPR vs. Group B's 60% — a **30 percentage-point** disparity meaning qualified Group-B applicants face a 4× higher false-negative (rejection) rate. This far exceeds the common 5pp high-stakes threshold and signals the model learned stricter criteria for the minority group.

## Connections
- [[Fairness]] — parent concept.
- [[EqualizedOdds]] — the stronger criterion (adds FPR equality).
- [[DemographicParity]] / [[Calibration]] — alternative criteria it can conflict with.
- [[TruePositiveRate]] / [[ConfusionMatrix]] — computation.
- [[ThresholdAdjustment]] — per-group threshold tuning equalizes TPR as a postprocessing step.
- [[mlsysbook-ch15-responsible-engineering]] — source.
