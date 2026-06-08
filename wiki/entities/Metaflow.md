---
title: "Metaflow"
type: entity
tags: [tool, orchestrator, ml-framework, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch11-mlops-and-llmops, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

## What it is
Metaflow is an open-source Python framework for building and managing real-life data-science workflows, originally developed at Netflix. It provides decorators for steps, automatic artifact versioning, and managed compute backends.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists Metaflow among the orchestrator alternatives evaluated against [[ZenML]]. Ch. 11 ([[leh-ch11-mlops-and-llmops]]) lists Metaflow as a peer of [[Airflow]] / [[Prefect]] / [[Dagster]] / [[Kubeflow]] when surveying MLOps orchestrators.

## Connections
- [[ZenML]] — chosen orchestrator.
- [[Airflow]] / [[Prefect]] / [[Dagster]] / [[Kubeflow]] — peers.
- [[Orchestrator]] — category.
- [[MLOps]] — discipline Metaflow targets.
- [[mlsysbook-ch14-ml-operations]] — Ch 14 cites Metaflow as an ML-specific platform layering higher-level abstractions over general CI/CD orchestrators.

