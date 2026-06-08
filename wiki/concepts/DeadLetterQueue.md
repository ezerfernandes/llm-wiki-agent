---
title: "Dead Letter Queue"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, reliability]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Dead Letter Queue

Separate storage for data that fails processing after multiple retry attempts (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). A pipeline processing financial transactions routes malformed data to a DLQ rather than losing critical records or halting all processing, enabling later analysis and reprocessing.

In ML systems, DLQs serve a **dual purpose** beyond failure analysis: systematic review of DLQ contents surfaces (1) schema violations indicating upstream changes, (2) edge-case patterns the model should handle, and (3) data-quality issues needing source-system fixes. The chapter's example: a fraud-detection DLQ revealed transactions from a new payment type the model had never seen, prompting targeted data collection and retraining. This transforms DLQs from passive error storage into **active sources for identifying model blind spots**. KWS uses DLQs to store failed recognition attempts, revealing underrepresented acoustic conditions.

## Connections

- [[CircuitBreaker]] — sibling reliability primitive.
- [[Idempotency]] — safe reprocessing of DLQ contents.
- [[ActiveLearning]] — DLQ contents are a source of high-value edge cases.
- [[mlsysbook-ch04-data-engineering]] — source.
