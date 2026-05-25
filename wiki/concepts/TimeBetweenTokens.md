---
title: "Time Between Tokens"
type: concept
tags: [latency, metric, inference, streaming]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Time Between Tokens

A **streaming smoothness** latency metric named in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "There are multiple metrics for latency for foundation models, including but not limited to time to first token, time per token, time between tokens, time per query, etc."

Distinct from [[TPOT|time per token]] — time-between-tokens measures the *inter-arrival* time between consecutive streamed tokens (the user's perceived smoothness of the stream), not the model's average generation time. A model can have low TPOT but spiky inter-arrival times that feel laggy.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[TPOT]] / [[TimePerToken]] — distinct but related metric.
- [[TTFT]] / [[TimePerQuery]] — sibling latency metrics.
- [[CostAndLatency]] — the parent eval bucket.
