---
title: "ZenML"
type: entity
tags: [tool, orchestrator, mlops, open-source, platform]
sources: [leh-ch02-tooling-and-installation, leh-ch03-data-engineering, leh-ch04-rag-feature-pipeline, leh-ch10-inference-pipeline-deployment, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
ZenML is an open-source MLOps framework and SaaS platform that lets engineers define portable ML pipelines in Python (`@pipeline` / `@step` decorators) and run them on swappable infrastructure "stacks" (local, AWS, GCP, Azure, Kubernetes). It includes a model registry, artifact store with versioning, metadata tracking, and alerter components.

## In LLM Engineer's Handbook
ZenML is the central orchestrator of every pipeline in the LLM Twin. Ch. 2 ([[leh-ch02-tooling-and-installation]]) introduces it as "the bridge between ML and MLOps," sets it up locally on `127.0.0.1:8237`, and contrasts its **stack** abstraction with [[Airflow]] / [[Prefect]] / [[Metaflow]] / [[Dagster]] / [[ArgoWorkflows]] / [[Kubeflow]] (none of which abstract infrastructure away). Ch. 3 ([[leh-ch03-data-engineering]]) wraps the crawler ETL in a `@pipeline` (`digital_data_etl`) with two `@step`s and shows ZenML auto-versioning every output as an artifact with attached metadata. Ch. 4 ([[leh-ch04-rag-feature-pipeline]]) orchestrates the RAG feature pipeline (`feature_engineering`) the same way. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) configures ZenML's `aws-stack` so steps execute as SageMaker processing jobs, and Ch. 11 ([[leh-ch11-mlops-and-llmops]]) walks through full ZenML Cloud setup, switching stacks (`zenml stack set aws-stack`), the alerter component for Slack/Discord/email notifications, and chaining all pipelines into an `end_to_end_data` CT master pipeline (an explicit workaround for the free-tier 3-pipeline cap).

## Connections
- [[AmazonSageMaker]] — the orchestrator backend in the AWS stack.
- [[AmazonS3]] / [[AmazonECR]] — artifact store + container registry inside the stack.
- [[Airflow]] / [[Prefect]] / [[Dagster]] / [[Metaflow]] / [[ArgoWorkflows]] / [[Kubeflow]] — orchestrator alternatives compared.
- [[MongoDB]] / [[Qdrant]] — data stores ZenML pipelines read/write.
- [[CometML]] — experiment tracker that complements ZenML.
- [[MLOps]] / [[LLMOps]] — discipline ZenML implements.
- [[Artifact]] / [[Stack]] / [[Pipeline]] / [[Step]] — core ZenML concepts.
