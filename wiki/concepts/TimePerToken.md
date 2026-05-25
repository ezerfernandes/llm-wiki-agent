---
title: "Time Per Token"
type: concept
tags: [latency, metric, inference]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Time Per Token

A latency metric for generative inference. Alternative phrasing for [[TPOT|time per output token]] used in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]'s discussion of LM latency:

> "There are multiple metrics for latency for foundation models, including but not limited to time to first token, time per token, time between tokens, time per query, etc."

Since autoregressive LMs generate token by token, **time-per-token × tokens generated ≈ total generation time**. Reducing output length is therefore a direct latency lever:

> "You can control the total latency observed by users by careful prompting, such as instructing the model to be concise."

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[TPOT]] — canonical name for the same metric.
- [[TTFT]] / [[TimeBetweenTokens]] / [[TimePerQuery]] — sibling latency metrics.
- [[CostAndLatency]] — the parent eval bucket.
