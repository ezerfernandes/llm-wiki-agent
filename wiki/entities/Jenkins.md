---
name: Jenkins
title: "Jenkins"
type: entity
tags: [tool, cicd, automation, open-source]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Jenkins

An open-source automation server widely used as a general-purpose [[CICD]] orchestrator. In [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14) it appears as the example CI tool that manages version-control events and execution logic — fetching data, preprocessing, triggering training, logging experiments (with MLflow), containerizing, and deploying to staging via [[Kubernetes]]. For ML workloads it is layered beneath domain-specific platforms ([[Kubeflow]], [[Metaflow]], Prefect) that add data versioning, model-metric gating, and retraining triggers Jenkins alone does not provide.

## Connections
- [[CICD]] — the practice Jenkins orchestrates.
- [[Kubeflow]] / [[Metaflow]] — ML-specific layers added above Jenkins.
- [[MLflow]] — experiment tracking paired with Jenkins pipelines.
- [[GitHubActions]] — alternative general-purpose CI/CD orchestrator.
- [[MLOps]] — development-infrastructure tooling.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
