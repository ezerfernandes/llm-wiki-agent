---
title: "Modal"
type: entity
tags: [product, serverless, gpu, cloud, platform]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
Modal is a serverless cloud platform optimized for running Python workloads on demand, including GPU-backed jobs and HTTP endpoints. It is popular for ML inference and batch processing.

## In LLM Engineer's Handbook
Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) lists Modal among alternative deployment platforms (with [[Seldon]], [[BentoML]], [[NvidiaTriton]], [[Hopsworks]], [[GoogleCloudVertexAI]], [[AzureML]], [[AzureOpenAI]], [[AmazonBedrock]]) one could use instead of an [[AmazonSageMaker]] inference endpoint.

## Connections
- [[AmazonSageMaker]] — chosen alternative.
- [[Serverless]] — Modal's deployment model.
- [[ModelServing]] — capability.
