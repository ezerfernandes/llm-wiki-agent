---
title: "Model Calibration"
type: concept
tags: [evaluation, probability, mlsysbook]
sources: [madewithml-evaluation, mlsysbook-ch03-ml-workflow, mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Model Calibration

The property that a model's predicted probabilities match empirical frequencies (e.g., 70% confidence means correct 70% of the time). Critical for downstream decision-making and tied to [[ModelEvaluation]] and [[ProbabilisticPerspective]].

In Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]), calibration is a distinct [[ModelValidation|validation]] dimension: clinicians use a [[DiabeticRetinopathyScreening|DR model]]'s confidence scores for triage, so a miscalibrated model that assigns 90% confidence to uncertain cases misdirects clinical workflows more dangerously than a less accurate but well-calibrated alternative. Platt scaling and temperature scaling correct calibration post-training.

In [[mlsysbook-ch12-benchmarking|Ch 12]], calibration becomes a **model-benchmarking** dimension: [[Quantization|compression]] frequently degrades it even while preserving accuracy (INT8 MobileNetV2 raises [[ExpectedCalibrationError|ECE]] 0.031→0.089), a failure invisible to aggregate accuracy but decisive for any confidence-thresholded pipeline — fixed via temperature scaling ($T$≈1.5–2.5).

## Connections

- [[ExpectedCalibrationError]] — the metric (ECE) that quantifies calibration; thresholds and reliability diagrams.
- [[Quantization]] / [[ModelCompression]] — the compression operations that silently degrade calibration.
- [[mlsysbook-ch12-benchmarking]] — calibration as a compression-validation dimension beyond top-line accuracy.
- [[mlsysbook-ch03-ml-workflow]] / [[madewithml-evaluation]] — sources.
