---
title: "Slice Analysis"
type: concept
tags: [mlops, debugging, monitoring, fairness]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Slice Analysis

Evaluating model performance across subpopulations (slices) rather than only in aggregate, because metrics averaged across all traffic can mask severe degradation in specific segments. Worked example from [[mlsysbook-ch14-ml-operations]]: overall accuracy of **91%** looks acceptable, but slicing by device reveals Desktop 94% / iOS 92% / Android 88% / **Tablet 62%** — the tablet failure (5% of traffic) is invisible in the aggregate. Degradation localized to one slice suggests a data-coverage or labeling issue; it is step 3 of the [[ModelDebugging|debugging decision tree]] and a core technique in cohort-based monitoring (also used by [[Netflix]]).

## Connections
- [[ModelDebugging]] — slice analysis is a key debugging technique.
- [[ModelMonitoring]] — cohort/per-segment monitoring.
- [[SHAP]] — feature attribution within a problematic slice.
- [[MLOps]] — observable-degradation principle.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
