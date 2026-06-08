---
title: "Kubeflow"
type: entity
tags: [tool, orchestrator, kubernetes, mlops, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch11-mlops-and-llmops, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

## What it is
Kubeflow is an open-source MLOps toolkit for running machine-learning workflows on Kubernetes. It provides pipeline orchestration, distributed training operators, and serving components.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists Kubeflow among the orchestrator alternatives evaluated against [[ZenML]]; the authors prefer ZenML because they want a cloud-agnostic abstraction without committing to a Kubernetes substrate. Ch. 11 ([[leh-ch11-mlops-and-llmops]]) re-lists Kubeflow as a peer orchestrator alongside [[Airflow]] / [[Prefect]] / [[Dagster]] / [[Metaflow]].

## Connections
- [[ZenML]] — chosen orchestrator in the book.
- [[Kubernetes]] — substrate Kubeflow runs on.
- [[ArgoWorkflows]] — sibling Kubernetes-native workflow engine.
- [[Orchestrator]] — category.
- [[MLOps]] — discipline.
- [[mlsysbook-ch14-ml-operations]] — Ch 14 cites Kubeflow as an ML-specific CI/CD layer (above general orchestrators) for data versioning, metric gating, and retraining triggers.

