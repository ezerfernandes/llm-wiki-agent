---
title: "Asynchronous Inference"
type: concept
tags: [deployment, inference, serving, architecture]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**Asynchronous inference** is a deployment archetype in which a client submits a request to a queue, the server processes it when capacity allows, and the result is returned via polling or push notification. It decouples request arrival from processing — smoothing traffic spikes and trading latency for cost efficiency.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] identifies asynchronous inference as one of three fundamental ML serving archetypes (alongside [[OnlineRealTimeInference]] and [[OfflineBatchTransform]]). The chapter argues asynchronous inference excels when: (a) jobs take more than ~5 minutes, (b) traffic spikes can be smoothed by a queue rather than by scaling GPU VMs 10×, or (c) cost optimization beats latency (e.g., document summarization, deepfake processing, keyword extraction). It is the right archetype for any job where the user can tolerate not getting an immediate response — and the cost savings from running on smaller GPU fleets typically dominate.

## Key details
- Queue-mediated; client polls or receives a webhook.
- Smooths spikes — no need to provision for peak.
- Trades latency for cost (cheaper GPU fleets, less idle capacity).
- AWS implementation: SageMaker Asynchronous Inference endpoints, SQS-based job queues.
- Anti-pattern for chatbots or anything user-facing where ~1s latency is required.

## Connections
- [[OnlineRealTimeInference]] — the synchronous low-latency archetype.
- [[OfflineBatchTransform]] — the bulk-processing archetype.
- [[ModelServing]] — the parent practice.
- [[ApplicationAutoScaling]] — the mechanism async inference reduces the need for.
- [[BatchInference]] — broader concept that overlaps with async.
- [[AmazonSageMaker]] — the AWS service implementing async inference endpoints.
