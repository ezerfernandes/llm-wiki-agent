---
title: "Data Cascade"
type: concept
tags: [ml-systems, mlsysbook, data-quality, mlops, foundations]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Cascade

A specific form of [[ConstraintPropagationPrinciple|constraint propagation]] in which a problem propagates through the [[MLSystemLifecycle|lifecycle]] **via data-quality failures** (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]; formalized in detail in Ch 4, Data Engineering). A blurry retinal image that slips past quality checks does not merely waste storage — it corrupts the training distribution, degrades model accuracy, and may produce a misdiagnosis months later in a clinic thousands of miles away.

Data cascades are why quality assurance must happen at the point of collection (so staff can recapture immediately) rather than being discovered weeks later during training. They are a leading cause of the lab-to-field gap and of the repeated iteration cycles ML projects require.

## Connections

- [[ConstraintPropagationPrinciple]] — data cascades are propagation through data-quality channels.
- [[DataEngineering]] — formalizes this failure mode (Ch 4).
- [[FourPillarsOfDataEngineering]] — the framework Ch 4 builds to prevent cascades; the "pipeline jungle" `zip_code` example is the canonical case.
- [[MLTechnicalDebt]] / [[DataDebt]] — the broader compounding-debt phenomena.
- [[DataDrift]] — one driver of downstream cascades.
- [[mlsysbook-ch03-ml-workflow]] / [[mlsysbook-ch04-data-engineering]] — sources.
