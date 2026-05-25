---
title: "Directed Acyclic Graph (DAG)"
type: concept
tags: [graph-theory, orchestration, architecture]
sources: [leh-ch02-tooling-and-installation]
last_updated: 2026-05-22
---

## Definition
A **directed acyclic graph (DAG)** is a graph whose edges have a direction and which contains no cycles — every traversal from a node returns to a strict descendant, never to the starting node. In MLOps and data engineering, DAGs are the canonical model for pipelines: nodes are steps, edges express data dependencies, and the absence of cycles guarantees a finite topological ordering for execution.

## In LLM Engineer's Handbook
[[leh-ch02-tooling-and-installation]] explains that every ZenML pipeline run is visualized as a DAG in the dashboard: the static `@pipeline` function definition is parsed into a DAG whose nodes are `@step` invocations and whose edges are the data flow between them. The DAG model is what enables fan-out parallelism, dependency-based caching, and reliable retries — the orchestrator can schedule any subset of nodes whose upstream dependencies are satisfied. The same DAG abstraction underpins Airflow, Prefect, Dagster, Metaflow, Argo Workflows, and Kubeflow.

## Key details
- Acyclicity gives a topological order — a sound execution schedule exists if and only if the graph is acyclic.
- Nodes can be skipped (cached) if their inputs are unchanged.
- Sub-DAGs can be retried in isolation.
- Independent sub-trees can be executed in parallel.
- Loops (e.g., training epochs) are encoded inside steps, not in the DAG itself; the DAG remains acyclic.

## Connections
- [[Pipeline]] — the MLOps abstraction whose runtime form is a DAG.
- [[Step]] — the unit at each DAG node.
- [[Orchestrator]] — the runtime that traverses the DAG.
- [[ZenML]] / [[Airflow]] / [[Prefect]] / [[Dagster]] — concrete DAG-based orchestrators.
- [[ComputationalGraph]] — adjacent concept in deep-learning frameworks.
