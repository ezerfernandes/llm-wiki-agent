---
title: "AUC (Area Under the ROC Curve)"
type: concept
tags: [evaluation, metrics, classification, medical-ai]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# AUC (Area Under the ROC Curve)

The area under the receiver operating characteristic curve (true positive rate vs. false positive rate across all classification thresholds), ranging from 0.5 (random) to 1.0 (perfect). Unlike accuracy, AUC is **threshold-independent and robust to class imbalance**, making it the standard summary metric for medical screening (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]).

Crucial systems caveat: **AUC alone cannot validate deployment readiness.** A model with AUC 0.99 can still produce unacceptable [[Sensitivity|sensitivity]] at the specific operating threshold chosen for deployment — exactly what happened to the [[DiabeticRetinopathyScreening|DR system]] (AUC 0.99 in the lab, 78% sensitivity in the field).

## Connections

- [[Sensitivity]] / [[Specificity]] — the per-threshold operating points AUC summarizes.
- [[ModelEvaluation]] / [[ModelValidation]] — AUC measures algorithm quality; deployment needs more.
- [[DiabeticRetinopathyScreening]] — the running case study.
- [[mlsysbook-ch03-ml-workflow]] — source.
