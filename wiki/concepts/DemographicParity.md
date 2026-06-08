---
name: DemographicParity
title: "Demographic Parity"
type: concept
tags: [responsible-ai, fairness, metrics, evaluation]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Demographic Parity

A group-[[Fairness|fairness]] metric requiring **equal positive-prediction (e.g. approval) rates across groups**. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], it is computed from [[ConfusionMatrix|confusion matrices]] as $(TP+FP)/\text{total}$ per group; a gap indicates unequal treatment in decisions.

In the chapter's loan worked example, Group A's approval rate exceeds Group B's, producing a demographic-parity disparity. It is the metric closest to the four-fifths / [[DisparateImpact|disparate impact]] selection-rate test. Achieving it can require a "price of fairness" utility tax (e.g. via [[ThresholdAdjustment|threshold adjustment]] that raises false positives for the disadvantaged group).

It conflicts with [[EqualizedOdds|equalized odds]] and [[Calibration|calibration]] when base rates differ between groups (impossibility theorem).

## Connections
- [[Fairness]] — parent concept.
- [[EqualOpportunity]] / [[EqualizedOdds]] / [[Calibration]] — the other criteria it can conflict with.
- [[ConfusionMatrix]] / [[FalsePositiveRate]] / [[TruePositiveRate]] — computation substrate.
- [[DisparateImpact]] — the legal analogue (selection-rate ratio ≥0.8).
- [[mlsysbook-ch15-responsible-engineering]] — source.
