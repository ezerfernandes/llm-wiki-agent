---
title: "Apache Airflow"
type: entity
tags: [tool, orchestrator, workflow, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch11-mlops-and-llmops, ai-engineering-ch10-architecture-feedback, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

## What it is
Apache Airflow is an open-source workflow orchestration platform that lets engineers author, schedule, and monitor data pipelines as Python-defined directed acyclic graphs (DAGs). Originally developed at Airbnb, it is one of the dominant orchestrators in data engineering.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) names Airflow among the orchestrator alternatives ([[Prefect]], [[Dagster]], [[Metaflow]], [[ArgoWorkflows]], [[Kubeflow]]) that the authors compared against [[ZenML]], ultimately choosing ZenML for its cloud-agnostic "stack" abstraction. Ch. 11 ([[leh-ch11-mlops-and-llmops]]) re-lists Airflow as an ML pipeline orchestrator option alongside the other contenders.

## Connections
- [[ZenML]] — the orchestrator the book actually uses.
- [[Prefect]] / [[Dagster]] / [[Metaflow]] / [[ArgoWorkflows]] / [[Kubeflow]] — other orchestrators compared.
- [[DataPipeline]] / [[DirectedAcyclicGraph]] — what Airflow runs.
- [[Orchestrator]] — category Airflow belongs to.
- [[mlsysbook-ch14-ml-operations]] — Ch 14 lists Apache Airflow among orchestration tools (with Prefect, dbt) for automated, freshness-maintaining data pipelines.


## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 references Airflow as the **counter-example** to AI pipeline orchestrators:

> *"An AI pipeline orchestrator is different from a general workflow orchestrator, like Airflow or Metaflow."* — Ch 10

The distinction Ch 10 draws: Airflow is a **DAG scheduler** for batch-shaped data/ML pipelines (training jobs, ETL, data preparation), while AI-pipeline orchestrators ([[LangChain]], [[LlamaIndex]], [[Flowise]], [[Langflow]], [[Haystack]]) operate at *request latency* on user-facing inference pipelines and are closer to a routing/function-composition layer.

The two are complementary rather than competing: Airflow runs the [[ai-engineering-ch07-finetuning|finetuning]] / [[ai-engineering-ch08-dataset-engineering|dataset]] pipelines that produce models; an AI pipeline orchestrator runs the inference chain that serves them.
