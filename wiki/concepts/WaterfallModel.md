---
title: "Waterfall Model"
type: concept
tags: [software-engineering, process, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Waterfall Model

The traditional sequential software process — requirements → system design → implementation → testing → deployment (Royce 1970) — in which each phase produces artifacts that feed the next and **requirements are finalized before implementation begins**, a practice inherited from physical manufacturing.

Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]) explains why it **fails for ML**: its core assumption (a stable specification) breaks when *the training data itself is the specification* and its properties can only be discovered through empirical iteration. ML systems need continuous feedback loops where deployment insights reshape data collection — exactly what waterfall's rigid phase gates prevent. Applying waterfall (or unmodified agile) to ML is the chapter's first named **Fallacy**.

## Connections

- [[MLSystemLifecycle]] / [[MachineLearningLifecycle]] — the cyclical alternative ML requires.
- [[ContinuousDeployment]] — the cadence ML needs that waterfall release cycles can't supply.
- [[FeedbackLoop]] — the missing element in linear models.
- [[mlsysbook-ch03-ml-workflow]] — source.
