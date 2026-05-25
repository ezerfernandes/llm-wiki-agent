---
title: "Dagster"
type: entity
tags: [tool, orchestrator, workflow, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Dagster is an open-source data orchestrator that models pipelines as graphs of typed, software-defined assets, with first-class support for testing, observability, and data lineage.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists Dagster among the orchestrator alternatives evaluated against [[ZenML]]; the authors prefer ZenML for its stack abstraction. Ch. 11 ([[leh-ch11-mlops-and-llmops]]) re-mentions Dagster as a peer of [[Airflow]] / [[Prefect]] / [[Metaflow]] / [[Kubeflow]] when surveying ML pipeline orchestrators.

## Connections
- [[ZenML]] — the orchestrator used in the book.
- [[Airflow]] / [[Prefect]] / [[Metaflow]] / [[Kubeflow]] — peer orchestrators.
- [[Orchestrator]] — category.
- [[DataPipeline]] — what Dagster runs.
