---
title: "ML Workflow"
type: concept
tags: [ml-systems, mlsysbook, workflow, ml-lifecycle, mlops, foundations]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# ML Workflow

The **engineering discipline of orchestrating the [[MLSystemLifecycle|ML lifecycle]]** — making constraints explicit at each development stage and tracing how they propagate across stages. In Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]), the *lifecycle* is **what gets traversed** (the six stages) while the *workflow* is **how the traversal is managed**. The Workflow marks the transition from *model researcher* (optimizes individual elements — a better architecture, cleaner dataset, faster accelerator) to *systems engineer* (orchestrates those elements into production systems that reliably deliver value).

It prevents failures like the chapter's day-153 cautionary tale (a 96%-accurate 4 GB model discarded because the target tablet had 512 MB) by ensuring deployment constraints shape every decision from day one. The conceptual lifecycle is the *what/why*; [[MLOps]] is the *how* (the operational machinery that implements it at scale).

## Connections

- [[MLSystemLifecycle]] / [[MachineLearningLifecycle]] — what the workflow orchestrates.
- [[StageInterfaceSpecification]] — the API-contract mechanism that operationalizes the discipline.
- [[ConstraintPropagationPrinciple]] / [[IterationTax]] — the quantitative laws that justify systematic workflow management.
- [[SystemsThinking]] — the analytical stance the workflow embodies.
- [[MLOps]] — the operational implementation of the lifecycle at scale.
- [[mlsysbook-ch03-ml-workflow]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 operationalizes the workflow's Operations phase (deployment, CI/CD, monitoring & triggering) as the MLOps infinity loop.

