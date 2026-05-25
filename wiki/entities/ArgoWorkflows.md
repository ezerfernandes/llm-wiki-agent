---
title: "Argo Workflows"
type: entity
tags: [tool, orchestrator, kubernetes, open-source]
sources: [leh-ch02-tooling-and-installation]
last_updated: 2026-05-22
---

## What it is
Argo Workflows is an open-source, container-native workflow engine for orchestrating parallel jobs on Kubernetes. Each step in an Argo workflow runs in its own container, with DAG or step-list dependencies.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) names Argo Workflows among the orchestrator alternatives that the authors evaluated against [[ZenML]] before choosing ZenML for its cloud-portable "stack" abstraction.

## Connections
- [[ZenML]] — chosen orchestrator.
- [[Kubernetes]] — substrate Argo runs on.
- [[Kubeflow]] — sibling Kubernetes-native workflow tooling.
- [[Orchestrator]] — category.
