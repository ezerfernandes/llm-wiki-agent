---
title: "Model Evaluation"
type: concept
tags: [evaluation, metrics]
sources: [madewithml-evaluation, mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Model Evaluation

The practice of measuring model quality on held-out data using metrics like [[PrecisionRecall]], [[MeanSquaredError]], and [[ModelCalibration]]. Distinct from [[OfflineEvaluation]] vs [[OnlineEvaluation]]; informs deployment decisions.

Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]) sharply distinguishes evaluation from [[ModelValidation|validation]]: evaluation measures accuracy on a held-out i.i.d. test set, whereas validation is a multi-dimensional *gate* testing the full deployment constraint surface (latency SLOs, fairness, cost, robustness). A model can pass evaluation and still fail validation — DR AUC 0.99 in the lab fell to 78% field [[Sensitivity|sensitivity]].
