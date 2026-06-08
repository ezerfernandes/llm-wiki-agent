---
title: "Autoregressive Generation"
type: concept
tags: [serving, llm, inference, decoding, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Autoregressive Generation

Generation in which **each output token conditions on all previously generated tokens**, creating a serial dependency that prevents the parallelism exploited during training ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). From Greek *auto-* (self) + Latin *regressus* (going back) — the output "regresses" on itself; George Udny Yule introduced autoregressive models in 1927 for sunspot cycles.

This serial bottleneck is *why* LLM decode is **[[MemoryWall|memory-bandwidth bound]] rather than compute-bound**: the model weights must be read from VRAM once per token regardless of available compute. It also drives variable-length output (response length unknown at request time), which breaks fixed-batch assumptions and motivates [[ContinuousBatching|continuous batching]]. Speculative decoding breaks the serial bottleneck at the *runtime* layer (a draft model proposes k tokens, the target verifies them in one parallel pass) without changing the architecture.

## Connections

- [[LLMServing]] — the serving regime defined by this property.
- [[MemoryWall]] / [[TPOT]] — why per-token latency is bandwidth-limited.
- [[ContinuousBatching]] — the batching technique variable-length output demands.
- [[SpeculativeDecoding]] — breaks the serial dependency via draft+verify.
- [[GreedyDecoding]] / [[BeamSearch]] / [[NucleusSampling]] — token-selection strategies layered on top.
- [[mlsysbook-ch13-model-serving]] — source.
