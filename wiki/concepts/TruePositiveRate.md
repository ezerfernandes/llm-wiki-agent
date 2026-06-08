---
name: TruePositiveRate
title: "True Positive Rate (TPR)"
type: concept
tags: [metrics, evaluation, fairness, classification]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# True Positive Rate (TPR)

The fraction of actual positives a classifier correctly identifies: $TPR = TP / (TP + FN)$ (recall / sensitivity). Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], TPR computed *per group* from [[ConfusionMatrix|confusion matrices]] is the basis of [[EqualOpportunity|equal opportunity]] (equal TPR) and [[EqualizedOdds|equalized odds]] (equal TPR and FPR).

In the chapter's loan example, a 90% (Group A) vs. 60% (Group B) TPR gap means qualified minority applicants suffer a 4× higher false-negative rate — a fairness violation invisible in aggregate accuracy.

## Connections
- [[FalsePositiveRate]] — the complementary error rate.
- [[ConfusionMatrix]] — TP/FP/TN/FN source.
- [[EqualOpportunity]] / [[EqualizedOdds]] — fairness metrics built on TPR.
- [[Fairness]] — parent property.
- [[mlsysbook-ch15-responsible-engineering]] — source.
