---
title: "Time Per Query"
type: concept
tags: [latency, metric, inference]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Time Per Query

The **end-to-end latency** metric per inference request — named in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] as one of the four key latency metrics ([[TTFT]], [[TimePerToken|time per token]], [[TimeBetweenTokens|time between tokens]], time per query).

Captures everything from request submission to final response: [[TTFT]] + (generation tokens × time-per-token) + any post-processing. Most relevant for non-streaming use cases where the user waits for the full response.

The example evaluation table in Ch 4 (Table 4-3) lists *"Time per total query (P90) < 1m hard, < 30s ideal"* — a practical example bound for a customer-facing app.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[TTFT]] / [[TimePerToken]] / [[TimeBetweenTokens]] — sibling metrics.
- [[CostAndLatency]] — the parent eval bucket.
