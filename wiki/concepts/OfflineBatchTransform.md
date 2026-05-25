---
title: "Offline Batch Transform"
type: concept
tags: [deployment, inference, serving, architecture]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**Offline batch transform** is a deployment archetype in which the inference job runs on a schedule: pull data from a warehouse / data lake, process it in bulk on a fixed-size compute cluster, write results to object storage or a database, and shut down. Optimized for throughput, not latency.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] identifies offline batch transform as one of three fundamental ML serving archetypes (alongside [[OnlineRealTimeInference]] and [[AsynchronousInference]]). The chapter argues offline batch transform is appropriate when *predictions can be stale* — e.g., daily movie recommendations — but is unacceptable for high-freshness use cases like a social-media feed where 1-hour-old predictions look broken. The trade-off is sharpened: offline batch transforms optimize for cost-per-prediction at the expense of latency, and pair naturally with workloads where the entire input population (every user, every product) needs scoring at once.

## Key details
- Pull-process-push: bulk extract → bulk transform → bulk load.
- Run on a schedule (cron); no real-time API surface.
- Optimized for hardware utilization (large batch sizes saturate GPU/CPU).
- Unsuitable for stale-sensitive applications.
- AWS implementation: SageMaker Batch Transform jobs.

## Connections
- [[OnlineRealTimeInference]] — the low-latency synchronous archetype.
- [[AsynchronousInference]] — the queue-mediated middle ground.
- [[BatchInference]] — broader concept the offline batch transform instantiates.
- [[ETL]] — same shape as a classical ETL job.
- [[ModelServing]] — the parent practice.
- [[AmazonSageMaker]] — the AWS service implementing batch transform jobs.
