---
title: "Idempotency"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, reliability, distributed-systems]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Idempotency

The property that a transformation produces identical output given identical input, regardless of when, where, or how many times it executes (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). From Latin *idem* + *potens* — "having the same power when applied again."

The intuition: a light switch (flip to "on" twice → still on) is idempotent; a toggle switch (each press flips state) is not. In data pipelines we want light-switch behavior. A non-idempotent transform that **appends** to a log creates duplicates on retry — silently corrupting training data with repeated examples that bias the model. An idempotent transform **upserts** by key (insert if absent, update if present), guaranteeing the same final state on retry.

This is essential for reliability: it makes retries after partial failures safe, enables checkpoint-restart on terabyte-scale jobs, and supports distributed reprocessing where partial failures are common. It pairs with [[DeterministicTransformation|determinism]] (no dependence on time, RNG, or mutable global state) to guarantee reproducible training.

## Connections

- [[DeterministicTransformation]] — the complementary reproducibility property.
- [[TrainingServingConsistency]] — both serve pipeline reliability.
- [[CircuitBreaker]] / [[DeadLetterQueue]] — the retry machinery idempotency makes safe.
- [[mlsysbook-ch04-data-engineering]] — source.
