---
title: "Multi-Scale Feedback"
type: concept
tags: [ml-systems, mlsysbook, feedback-loops, monitoring, foundations]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Multi-Scale Feedback

ML systems succeed by **orchestrating feedback loops across multiple timescales**, each serving a different optimization purpose (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]). In the DR case study the loops span ~five orders of magnitude:

- **Minute** loops catch a misconfigured camera before it produces a day of unusable images.
- **Daily** loops detect a clinic's sensitivity drifting below threshold.
- **Weekly** loops aggregate accuracy and run drift-detection tests ([[PopulationStabilityIndex|PSI]], [[KolmogorovSmirnovTest|KS]]).
- **Monthly** loops reveal demographic shifts requiring expanded training data.
- **Quarterly** loops re-evaluate whether the overall architecture still meets evolving clinical needs.

Fast loops enable quick correction of operational issues; slow loops enable strategic adaptation. The multi-scale structure prevents both **reactionary** changes (over-responding to daily noise) and **sluggish** adaptation (under-responding to meaningful trends). The corresponding monitoring hierarchy: operational metrics (seconds), proxy metrics (hours, no ground truth), model-performance metrics (weeks, needs labels).

## Connections

- [[FeedbackLoop]] — the general mechanism.
- [[SystemsThinking]] — multi-scale feedback is one of its three patterns.
- [[MLSystemLifecycle]] / [[MachineLearningLifecycle]] — the loops close the lifecycle.
- [[DataDrift]] / [[PopulationStabilityIndex]] / [[KolmogorovSmirnovTest]] — what the slower loops detect.
- [[mlsysbook-ch03-ml-workflow]] — source.
