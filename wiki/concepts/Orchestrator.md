---
title: "Orchestrator (MLOps Pipeline Orchestrator)"
type: concept
tags: [mlops, orchestration, architecture]
sources: [leh-ch02-tooling-and-installation, leh-ch03-data-engineering, leh-ch11-mlops-and-llmops, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

## Definition
An **orchestrator** is the runtime that schedules and coordinates the steps of an ML pipeline — resolving DAG dependencies, materializing inputs/outputs, retrying failed steps, persisting versioned artifacts, and exposing pipeline state through a dashboard or API. Examples: [[ZenML]], [[Airflow]], [[Prefect]], [[Dagster]], [[Metaflow]], [[Kubeflow]], [[ArgoWorkflows]].

## In LLM Engineer's Handbook
[[leh-ch02-tooling-and-installation]] positions ZenML as "the bridge between ML and MLOps" and surveys the orchestrator landscape: Airflow (general DAG scheduler), Prefect, Metaflow (Netflix), Dagster, Argo Workflows, Kubeflow (Kubernetes-native). The book's chosen orchestrator is ZenML for its **stack abstraction** — pipeline code targets local, AWS, GCP, or Azure without modification. [[leh-ch03-data-engineering]] uses ZenML to run the data collection pipeline; [[leh-ch11-mlops-and-llmops]] makes the strongest claim: "starting with an orchestrator since day 0... forced us to decouple each pipeline and transfer the communication between them solely through various types of data storage." The orchestrator is therefore not just a scheduler — it is the discipline that prevents pipeline coupling and makes [[ContinuousTraining]] tractable.

## Key details
- Core responsibilities: DAG resolution, step scheduling, input materialization, output persistence, retry, observability.
- ZenML's stack abstraction lets one orchestrator drive heterogeneous compute (local, SageMaker, GCP Vertex AI, Azure ML, Kubernetes).
- Pipeline orchestrators are one of the four core MLOps components alongside model registry, feature store, and ML metadata store.
- Day-0 adoption is a strong recommendation: retrofitting an orchestrator after the fact requires re-plumbing every pipeline to versioned storage.

## Connections
- [[Pipeline]] — what an orchestrator runs.
- [[Step]] — the unit an orchestrator schedules.
- [[Stack]] — the runtime target an orchestrator binds to (ZenML-specific).
- [[ZenML]] / [[Airflow]] / [[Prefect]] / [[Dagster]] / [[Metaflow]] / [[Kubeflow]] / [[ArgoWorkflows]] — concrete orchestrators.
- [[MLOps]] / [[LLMOps]] — disciplines orchestrators support.
- [[ContinuousTraining]] — CT depends on orchestrator-managed triggers.
- [[FTIArchitecture]] — orchestrators express the FTI pattern as concrete pipelines.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 introduces a **distinct sibling notion**: the **[[AIPipelineOrchestration|AI pipeline orchestrator]]** — for synchronous, request-shaped LLM inference pipelines, not for batch-DAG-shaped training pipelines.

> *"An AI pipeline orchestrator is different from a general workflow orchestrator, like Airflow or Metaflow."* — Ch 10

The distinction:

| MLOps pipeline orchestrator (this page) | AI pipeline orchestrator ([[AIPipelineOrchestration]]) |
|---|---|
| Schedules training / ETL / batch jobs | Schedules per-request inference chains |
| Examples: [[ZenML]], [[Airflow]], [[Prefect]], [[Dagster]] | Examples: [[LangChain]], [[LlamaIndex]], [[Flowise]], [[Langflow]], [[Haystack]] |
| Operates at job-scheduling latency | Operates at request latency |
| Produces models | Serves models |

The two are **complementary**, not competing. A mature LLM application typically has *both*: an MLOps orchestrator for training/finetuning/data pipelines, plus an AI pipeline orchestrator for the inference path users hit.
