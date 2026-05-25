---
title: "Seldon"
type: entity
tags: [product, mlops, model-serving, kubernetes, open-source]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
Seldon (Seldon Core / Seldon Deploy) is an MLOps platform for deploying, monitoring, and managing ML models on Kubernetes. Its open-source Seldon Core defines `SeldonDeployment` CRDs for model graphs and routing.

## In LLM Engineer's Handbook
Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) lists Seldon among alternative deployment platforms (with [[BentoML]], [[NvidiaTriton]], [[Modal]], [[GoogleCloudVertexAI]], [[AzureML]], [[Hopsworks]]) one could use instead of an [[AmazonSageMaker]] inference endpoint.

## Connections
- [[AmazonSageMaker]] — chosen alternative.
- [[Kubernetes]] — substrate Seldon Core runs on.
- [[BentoML]] / [[NvidiaTriton]] — peer model-serving stacks.
- [[ModelServing]] — capability.
