---
title: "Backpressure"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, streaming, reliability]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Backpressure

The flow-control problem in [[StreamIngestion|streaming systems]] where downstream components cannot keep pace with the incoming data rate (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). During traffic spikes the system must choose among three options, each with a cost: **buffer** (requires memory, adds latency), **sample** (loses data), or **push back to producers** (potentially causing their failure).

Backpressure is one of the complexities batch processing avoids; managing it well is part of why streaming carries a ~3×–10× cost premium. It is closely tied to data-freshness SLAs — meeting a 100 ms freshness SLA under backpressure demands very different infrastructure than a 1-hour SLA.

## Connections

- [[StreamIngestion]] — the regime where backpressure arises.
- [[CircuitBreaker]] / [[DeadLetterQueue]] — adjacent reliability mechanisms.
- [[mlsysbook-ch04-data-engineering]] — source.
