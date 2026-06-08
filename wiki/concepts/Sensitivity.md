---
title: "Sensitivity"
type: concept
tags: [evaluation, metrics, medical-ai, classification]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Sensitivity

The **true positive rate** — the fraction of actual positives a classifier correctly identifies. In medical AI it is often the binding metric: for [[DiabeticRetinopathyScreening|DR screening]], **>90% sensitivity is mandatory** because missed cases cause blindness (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]). Paired with [[Specificity|specificity]] (true negative rate, >80% target to avoid overwhelming referral systems), it replaces aggregate accuracy as the relevant objective for screening.

Sensitivity illustrates the lab-to-field gap: a DR model at [[AUC]] 0.99 in the lab dropped to **78% field sensitivity** on a five-year-old fundus camera. Production monitoring alerts when a seven-day rolling average drops below ~88% (2 pp under the 90% target).

## Connections

- [[Specificity]] — the complementary true-negative-rate metric.
- [[AUC]] — threshold-independent summary; AUC 0.99 ≠ acceptable sensitivity at the chosen operating point.
- [[ModelValidation]] — sensitivity is a primary gate criterion.
- [[DiabeticRetinopathyScreening]] — the running case study.
- [[mlsysbook-ch03-ml-workflow]] — source.
