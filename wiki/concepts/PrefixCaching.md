---
title: "Prefix Caching"
type: concept
tags: [serving, llm, kv-cache, optimization, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Prefix Caching

An LLM-serving optimization that **stores the [[KVCache|KV-cache]] of common instruction prefixes** — a 2,000-token system prompt, a shared RAG context — so many independent requests reuse the same precomputed hidden states instead of re-running prefill ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]).

This eliminates redundant prefill compute (the $O$ term) and reduces memory-transfer cost ($D_{\text{vol}}/\text{BW}$), directly lowering the energy footprint of RAG and chat applications. For multi-turn conversations it is "caching of the past": each turn processes only the *new* tokens, which is why [[ContinuousBatching|session affinity]] (routing follow-ups to the replica holding the cached context) matters — losing it can increase latency 2–5× on long conversations. Complements **KV-cache offloading** (spilling inactive context to host RAM/NVMe to prevent OOM).

## Connections

- [[KVCache]] — the structure being cached and reused across requests.
- [[LLMServing]] / [[ContinuousBatching]] / [[PagedAttention]] — the broader LLM-serving optimization set.
- [[TTFT]] — prefix-cache hits collapse the prefill phase, cutting TTFT.
- [[CostPerInference]] — skipping prefill reduces J/token and $/token.
- [[mlsysbook-ch13-model-serving]] — source.
