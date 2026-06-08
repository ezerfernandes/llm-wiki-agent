---
title: "Stream Ingestion"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, data-pipeline, streaming]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Stream Ingestion

Processing data in real-time as it arrives, consuming events continuously rather than accumulating batches (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). Essential when data loses value quickly — e.g., fraud detection scoring each transaction before it completes, since detection hours later is worthless.

The cost: streaming is ~3× (often an order of magnitude) more expensive per byte than [[BatchIngestion|batch]] because it requires always-on infrastructure, redundant processing for fault tolerance, and low-latency networking, with no batch economies of scale. Worked example: 1M events/s × 1 KB = 1 GB/s; streaming ~$120/day (100 always-on cores) vs batch ~$33/day. Streaming also introduces **[[Backpressure|backpressure]]** (buffer / sample / push back when downstream can't keep pace) and **data-freshness SLAs** (a 100 ms SLA needs different infra than a 1-hour SLA).

Streaming-tool choice is a [[CAPTheorem|CAP]] failure-mode choice: [[ApacheKafka|Kafka]] (CP), Pulsar (AP), [[Kinesis]]. Streaming premium is justified only when the value of sub-second latency exceeds the added cost.

## Connections

- [[BatchIngestion]] — the scheduled counterpart and cost contrast.
- [[Backpressure]] — the flow-control failure mode unique to streaming.
- [[CAPTheorem]] — governs streaming consistency/availability trade-offs.
- [[ApacheKafka]] / [[Kinesis]] — streaming platforms.
- [[DataIngestion]] — the parent stage.
- [[mlsysbook-ch04-data-engineering]] — source.
