---
title: "Specificity"
type: concept
tags: [evaluation, metrics, medical-ai, classification]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Specificity

The **true negative rate** — the fraction of actual negatives a classifier correctly identifies. In [[DiabeticRetinopathyScreening|DR screening]] the target is **>80% specificity**, because false positives overwhelm referral systems even when [[Sensitivity|sensitivity]] is high (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]). The Gulshan et al. (2016) DR model reached 93.4% specificity alongside 97.5% sensitivity and AUC 0.99.

A subtler systems trap is **positive predictive value (PPV)**: a model at 95% lab accuracy can drop to 50% PPV in a low-prevalence population, making it clinically useless despite strong technical metrics — which is why a single model needs different operating thresholds per deployment site.

## Connections

- [[Sensitivity]] — the complementary true-positive-rate metric.
- [[AUC]] — threshold-independent summary spanning all sensitivity/specificity operating points.
- [[ModelValidation]] — specificity is a gate criterion.
- [[DiabeticRetinopathyScreening]] — the running case study.
- [[mlsysbook-ch03-ml-workflow]] — source.
