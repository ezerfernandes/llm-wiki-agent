---
title: "Circuit Breaker"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, reliability, distributed-systems]
sources: [mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Circuit Breaker

A cascade-failure-prevention pattern for ML data pipelines (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]), named after the electrical safety device and exhibiting three states: **closed** (normal flow), **open** (faults blocked), **half-open** (recovery probe).

When a feature-computation service fails repeatedly, the circuit breaker opens after a failure threshold and stops calling it — so the caller does not wait on timeouts that would cascade into its own failure. While open, the pipeline falls back to cached or default features rather than blocking on a dead service. It pairs with bulkhead isolation, exponential backoff (1s→2s→4s), progressive timeouts, and [[DeadLetterQueue|dead letter queues]] in the chapter's "graceful degradation" reliability toolkit.

## Connections

- [[DeadLetterQueue]] — sibling reliability primitive for failed records.
- [[Backpressure]] — adjacent flow-control concern.
- [[Idempotency]] — makes the retries circuit breakers manage safe.
- [[mlsysbook-ch04-data-engineering]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 adapts the circuit breaker for ML's semantic-failure mode: accuracy degradation needs different thresholds than availability, leaving naive breakers blind to plausible-but-wrong predictions.

