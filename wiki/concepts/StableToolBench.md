---
title: "StableToolBench"
type: concept
tags: [dataset-engineering, synthetic-data, tool-use, agents]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# StableToolBench

**Guo et al. (2024) — a benchmark/dataset that uses AI to simulate API outputs, so tool-use models can be trained without actually calling the APIs.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]]:

> "Imagine you want to train a model to interact with a set of APIs. Instead of making actual API calls — which might be costly or slow — you can use an AI model to simulate the expected outcomes of those calls."

## Why simulation > real API calls for training

| Constraint | Real APIs | AI-simulated APIs |
|---|---|---|
| Cost per call | $$$ (rate limits, billing) | Just model inference |
| Speed | Variable network latency | Predictable |
| Reproducibility | Stateful real services drift | Snapshotable |
| Availability | Service may be down | Always available |
| Safety | Real side effects possible | Pure simulation |

## The deeper claim

AI can simulate the outcomes of **arbitrary programs**, not just APIs. The same principle extends to:

- Database queries
- File system operations
- External calculators
- Search-engine results

If verification is cheap (or possible), AI-simulated outcomes can replace expensive real interactions in training.

## Connections

- [[Simulation]] — parent technique.
- [[AIPoweredDataSynthesis]] — parent category.
- [[ToolUse]] / [[Agent]] — the downstream consumer (tool-using agents).
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
