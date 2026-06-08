---
title: "Boundary Erosion"
type: concept
tags: [mlops, technical-debt, architecture]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Boundary Erosion

A core ML [[TechnicalDebt|technical-debt]] pattern in which system boundaries dissolve because model behavior depends on the statistical properties of data flowing through the system rather than on explicit interfaces. A change to upstream data formatting can pass all unit tests while silently degrading downstream model accuracy. This implicit coupling produces **entanglement** — dependencies so intertwined that local modifications require global understanding.

Captured by the **CACHE principle**: *Change Anything Changes Everything*. Changing a feature's binning strategy or a hyperparameter can ripple unpredictably through downstream behavior. The defense is architectural: modularity, encapsulation, well-defined interfaces, and explicit separation between data ingestion, feature engineering, and modeling logic.

Defined in [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14), following Sculley et al. 2015.

## Connections
- [[TechnicalDebt]] — parent pattern family.
- [[CorrectionCascade]] — its sibling; what happens when teams try to repair eroded systems.
- [[FeedbackLoop]] / [[TrainingServingSkew]] — related debt failure modes.
- [[MLOps]] — separation-of-concerns principle as the remedy.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
