---
title: "Pipeline (MLOps)"
type: concept
tags: [mlops, orchestration, architecture]
sources: [leh-ch02-tooling-and-installation, leh-ch03-data-engineering, leh-ch04-rag-feature-pipeline, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## Definition
A **pipeline** in the MLOps sense is a directed acyclic graph of steps — data extraction, transformation, training, evaluation, deployment — defined declaratively (often by decorating Python functions) and scheduled by an [[Orchestrator|orchestrator]]. Each step produces versioned outputs (artifacts) that downstream steps consume by reference, so a pipeline run is reproducible from any intermediate point.

## In LLM Engineer's Handbook
[[leh-ch02-tooling-and-installation]] introduces ZenML's pipeline primitive: `@pipeline` decorates a Python function and `@step` decorates each computational unit, e.g., `@pipeline def digital_data_etl(user_full_name, links): user = get_or_create_user(user_full_name); crawl_links(user=user, links=links)`. [[leh-ch03-data-engineering]] gives the worked example (the data collection pipeline). [[leh-ch04-rag-feature-pipeline]] expands it into a five-step batch RAG feature pipeline. [[leh-ch11-mlops-and-llmops]] surveys the broader pipeline ecosystem (Airflow, Prefect, Dagster, Metaflow, Kubeflow) and shows how ZenML pipelines materialize as SageMaker processing jobs once the active stack is switched to `aws-stack`.

## Key details
- Pipelines have a declarative shape (functions + steps) and a runtime shape (a [[DirectedAcyclicGraph|DAG]] executed by the orchestrator).
- Each step's outputs become typed, versioned [[Artifact|artifacts]] in object storage.
- Pipelines are configured at runtime via YAML files (e.g., `configs/digital_data_etl_maxime_labonne.yaml`) injected through `.with_options(config_path=...)`, decoupling code from per-run parameters.
- Pipelines can be triggered manually, by event (REST API), or on a schedule (cron).
- Pipeline-to-pipeline communication is the canonical CT pattern (`Client().trigger_pipeline(...)`).

## Connections
- [[Step]] — a pipeline's atomic unit of computation.
- [[Orchestrator]] — the runtime that schedules pipeline steps.
- [[Artifact]] — the versioned output a step produces.
- [[DirectedAcyclicGraph]] — the runtime structure of a pipeline.
- [[Stack]] — the ZenML abstraction selecting the infra a pipeline runs on.
- [[ZenML]] / [[Airflow]] / [[Prefect]] / [[Dagster]] / [[Metaflow]] / [[Kubeflow]] / [[ArgoWorkflows]] — concrete pipeline tools.
- [[ContinuousTraining]] — CT is the practice of triggering training pipelines automatically.
- [[FTIArchitecture]] — the architectural pattern composed of pipelines.
