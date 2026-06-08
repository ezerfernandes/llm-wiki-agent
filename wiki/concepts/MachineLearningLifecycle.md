---
title: "Machine Learning Lifecycle"
type: concept
tags: [ml-systems, mlsysbook, ml-lifecycle, mlops, foundations]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Machine Learning Lifecycle

The **iterative engineering process of building, deploying, monitoring, and retraining ML systems, where each stage feeds information back to earlier stages because model performance degrades continuously after deployment** (formal definition, Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]). Six stages: **Problem Definition → Data Collection & Preparation → Model Development & Training → Evaluation & Validation → Deployment & Integration → Monitoring & Maintenance.**

Three properties distinguish it from a traditional software lifecycle:

- **It is a closed loop, not a linear pipeline.** Accuracy decays at a rate proportional to the divergence $\mathcal{D}(P_t \lVert P_0)$ between current and training distributions, requiring periodic retraining that re-incurs the full compute cost — making the lifecycle a *budgeting* problem, not just an engineering process.
- **It degrades when the world changes, not when code changes.** Accuracy erodes through [[DataDrift|data drift]] even when code, infrastructure, and configuration are untouched.
- **Deployment is the beginning of the feedback loop, not the end.** Monitoring surfaces drift → drift triggers retraining → retraining produces a new model that re-enters deployment.

Often realized as **two parallel pipelines**: a data pipeline (collection → ingestion → analysis → labeling → validation → preparation) and a model pipeline (training → evaluation → validation → deployment), unified by feedback arrows. Closely related to CRISP-DM (1996), which first codified data-intensive development as six interconnected iterative phases.

## Connections

- [[MLWorkflow]] — the engineering discipline of orchestrating this lifecycle.
- [[MLSystemLifecycle]] — the Ch 1 framing of the same cyclical arc.
- [[ConstraintPropagationPrinciple]] — why late-stage discoveries cost exponentially more.
- [[FeedbackLoop]] / [[MultiScaleFeedback]] — the loops that make it cyclical.
- [[DataDrift]] / [[DistributionShift]] — the drift that drives continuous retraining.
- [[MLOps]] — the operational implementation.
- [[mlsysbook-ch03-ml-workflow]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 closes the lifecycle loop: production telemetry triggers retraining, making the lifecycle circular rather than linear.

