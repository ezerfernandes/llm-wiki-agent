---
title: "Technical Debt"
type: concept
tags: [software-engineering, maintainability]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Technical Debt

The accumulated future cost of expedient design and implementation shortcuts — the metaphorical "interest" paid when quick decisions must later be reworked. In ML systems this debt compounds faster than in traditional software because the "source code" includes data, configuration, and pipelines, not just program logic (see [[MLTechnicalDebt]]). Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]) ties it to the [[ConstraintPropagationPrinciple|constraint propagation principle]]: decisions made in ignorance of downstream constraints create debt that escalates exponentially across lifecycle stages.

## Connections

- [[MLTechnicalDebt]] — the ML-specific entanglement / hidden-feedback / undeclared-consumer mechanisms.
- [[ConstraintPropagationPrinciple]] — late discoveries are debt coming due.
- [[Reproducibility]] — a primary mitigation.
- [[mlsysbook-ch03-ml-workflow]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 catalogs ML technical-debt patterns (boundary erosion, correction cascades, undeclared consumers, feedback loops) where interest compounds as silent accuracy decay (5%/95% rule; ML Test Score).

