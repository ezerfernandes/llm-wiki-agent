---
title: "Stack (ZenML Stack)"
type: concept
tags: [mlops, orchestration, architecture, cloud]
sources: [leh-ch02-tooling-and-installation, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## Definition
A **stack** in ZenML's vocabulary is a named set of infrastructure components — orchestrator, object store, container registry, experiment tracker, alerter — that together define a runtime target for pipelines. Switching from local execution to AWS production is a single `zenml stack set aws-stack` command; the pipeline code stays identical.

## In LLM Engineer's Handbook
[[leh-ch02-tooling-and-installation]] introduces the stack abstraction as ZenML's primary differentiator over Airflow, Prefect, Metaflow, Dagster, Argo, and Kubeflow: "The beauty of this is that ZenML doesn't vendor-lock you into any cloud platform. It completely abstracts away the implementation of your Python code from the infrastructure it runs on." The book's production stack pairs [[AmazonSageMaker|SageMaker]] (orchestrator + compute), [[AmazonS3|S3]] (artifact storage), and [[AmazonECR|ECR]] (container registry). [[leh-ch11-mlops-and-llmops]] adds the deployment dimension: switching stacks lets the same `digital_data_etl`, `feature_engineering`, `training`, and `deploy` pipelines run locally during development and on SageMaker processing jobs in production with zero code changes — only configuration changes.

## Key details
- Components inside a stack: orchestrator, object store, container registry, optional experiment tracker, optional alerter, optional secrets manager.
- Stacks are switched with `zenml stack set <name>`; pipelines do not need re-instrumentation.
- Each stack can be configured asynchronously (`zenml orchestrator update aws-stack --synchronous=False`) to avoid CLI-blocking long jobs.
- The pattern is the LLMOps version of Twelve-Factor App's "config in env, not in code."

## Connections
- [[Pipeline]] — what runs on a stack.
- [[Orchestrator]] — a stack's primary component.
- [[ZenML]] — the orchestrator whose stack abstraction this concept describes.
- [[Artifact]] — stored in the stack's object store.
- [[AmazonSageMaker]] / [[AmazonS3]] / [[AmazonECR]] — the production stack the book uses.
- [[MLOps]] — discipline the stack abstraction supports.
