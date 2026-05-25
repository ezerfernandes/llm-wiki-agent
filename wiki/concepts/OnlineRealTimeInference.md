---
title: "Online Real-Time Inference"
type: concept
tags: [deployment, inference, serving, architecture, latency]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**Online real-time inference** is a deployment archetype in which clients call a synchronous HTTP / gRPC endpoint and block (or stream) until the response is available. Optimized for low latency; the user is on the other end of the connection waiting for an answer.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] identifies online real-time inference as one of three fundamental ML serving archetypes (alongside [[AsynchronousInference]] and [[OfflineBatchTransform]]) and the chosen archetype for the LLM Twin. The chapter cites Google's 2016 mobile-site study — "53% of visits are abandoned if a mobile site takes longer than 3 s to load" — to argue user-experience latency budgets dominate this archetype. Online real-time inference is implemented via REST (accessible, slower due to JSON serialization), [[gRPC]] (faster, schema-coupled), or streaming protocols like [[WebSockets]] / [[ServerSentEvents]] for token-by-token LLM output. The chapter notes a crucial nuance: **lower per-request latency translates to higher throughput only when requests are parallelized**; with batching, latency and throughput can be coupled in the opposite direction (200 ms × batch-of-60 = 300 RPS even though latency is 2× a 100 ms × batch-of-20 = 200 RPS configuration).

## Key details
- Synchronous request/response; client blocks (or streams tokens) until done.
- Latency budget typically <1-3s end-to-end; per-token streaming improves perceived latency.
- Streaming variants: SSE (one-way), WebSockets (bidirectional).
- AWS implementation: SageMaker real-time endpoints (the LLM Twin uses these).
- Pairs with [[ApplicationAutoScaling]] for elastic capacity.

## Connections
- [[OnlineInference]] — the broader umbrella concept.
- [[AsynchronousInference]] — queue-mediated alternative.
- [[OfflineBatchTransform]] — batch alternative.
- [[Latency]] / [[InstructionThroughput]] — the metrics this archetype optimizes.
- [[ServerSentEvents]] / [[WebSockets]] — streaming protocols.
- [[ContinuousBatching]] — server-side optimization that improves throughput while maintaining per-request latency.
- [[AWSSageMakerInferenceEndpoint]] — the AWS realization.
- [[MicroservicesArchitecture]] — the topology this archetype typically uses.
