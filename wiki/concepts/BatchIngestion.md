---
title: "Batch Ingestion"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, data-pipeline]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Batch Ingestion

Collecting data into groups and processing it at scheduled intervals rather than continuously (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). Appropriate when real-time processing is not critical and slight prediction staleness does not hurt business outcomes — e.g., a retailer processing daily sales overnight to refresh inventory models each morning.

Advantages: amortizes startup cost across large volumes, uses schedulable (cheap, off-peak) resources, and simplifies error handling — failed batches retry or resume from checkpoints, and deterministic processing (same input → same output) eases debugging. Contrast with [[StreamIngestion|stream ingestion]]: batch optimizes throughput at the cost of latency, and is materially cheaper (no always-on infra). Worked example: a 1 TB job using 100 machines for 10 minutes vs streaming's dedicated 24/7 resources.

The choice between batch and streaming is "a judgment about how quickly data loses value and how much infrastructure cost that freshness justifies." Hybrids predominate.

## Connections

- [[StreamIngestion]] — the real-time counterpart and cost contrast.
- [[DataIngestion]] — the parent stage.
- [[ETL]] / [[ELT]] — transformation patterns batch ingestion typically uses.
- [[mlsysbook-ch04-data-engineering]] — source.
