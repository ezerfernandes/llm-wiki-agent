---
title: "DVC"
type: entity
tags: [tool, data-versioning, mlops, open-source]
sources: [leh-ch11-mlops-and-llmops, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

## What it is
DVC (Data Version Control) is an open-source Git-companion tool for versioning datasets, models, and ML pipelines. It stores large files in external object stores (S3, GCS, Azure Blob, SSH) while keeping pointers in Git.

## In LLM Engineer's Handbook
Ch. 11 ([[leh-ch11-mlops-and-llmops]]) names DVC as the canonical option for **data versioning** when codifying the six MLOps principles — alongside artifact systems in [[CometML]] / [[WeightsAndBiases]] / [[ZenML]] for unstructured data, and SQL version columns for structured data. The chapter pairs DVC with [[GitLFS]] in the broader "Git for data" theme.

## Connections
- [[GitLFS]] — peer Git-extension for large files.
- [[CometML]] / [[WeightsAndBiases]] / [[ZenML]] — alternative artifact-system-based versioning.
- [[Versioning]] — MLOps principle.
- [[MLOps]] — discipline.
- [[GitHub]] — typical Git remote DVC pairs with.
- [[mlsysbook-ch14-ml-operations]] — Ch 14 uses DVC for Git-like dataset versioning, recovering the Data_v term that pure code versioning loses.

