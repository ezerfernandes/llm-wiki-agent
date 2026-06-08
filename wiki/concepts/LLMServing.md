---
title: "LLM Serving"
type: concept
tags: [serving, inference, llm, autoregressive, kv-cache, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# LLM Serving

Serving large language models introduces **three properties absent from traditional fixed-output serving** ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]):

1. **[[Autoregressive|Autoregressive generation]]** — each token depends on all previous tokens, so output is inherently sequential (no training-style parallelism).
2. **Variable-length output** — response length is unknown at request time, invalidating fixed-batch assumptions.
3. **Stateful [[KVCache|KV-cache]] memory** — grows with every generated token, often exceeding the model weights, creating dynamic memory pressure.

Decode is **[[MemoryWall|memory-bandwidth bound]]** (arithmetic intensity ≈ 1 FLOP/byte: the full weight tensor must be read per token), so "adding compute cores yields zero latency improvement — only faster memory or smaller models help." This splits user-perceived latency into two metrics: **[[TTFT]]** (prefill phase, compute-bound) and **[[TPOT]]** (decode phase, bandwidth-bound). Production targets: TTFT < 500 ms, TPOT < 50 ms (~20 tok/s, faster than reading), >1,000 tok/s aggregate. Streaming responses (chunked HTTP) make TTFT the responsiveness lever and TPOT the fluidity lever.

The throughput levers: **[[ContinuousBatching|continuous batching]]** (iteration-level rescheduling), **[[PagedAttention]]** (cut KV-cache fragmentation 40–80% → <4%), **[[PrefixCaching|prefix caching]]** (reuse shared system-prompt/RAG KV state), KV-cache offloading to host/NVMe, [[SpeculativeDecoding|speculative decoding]] (~2–3×), [[GroupedQueryAttention|GQA]], and weight-only INT4 quantization. The 8B Llama-3/H100 case study: KV-cache *memory capacity* bounds concurrency; *bandwidth* bounds decode latency; *prefill compute* bounds full-request throughput.

## Connections

- [[TTFT]] / [[TPOT]] — the two-phase latency metrics (prefill vs decode).
- [[ContinuousBatching]] / [[PagedAttention]] / [[KVCache]] — the throughput trifecta.
- [[PrefixCaching]] / [[SpeculativeDecoding]] / [[GroupedQueryAttention]] — KV-cache and decode optimizations.
- [[Autoregressive]] — the serial dependency behind the memory wall.
- [[MemoryWall]] / [[RooflineModel]] — why decode is bandwidth-bound.
- [[GreedyDecoding]] / [[BeamSearch]] / [[NucleusSampling]] — decoding strategies and their cost.
- [[vLLM]] / [[TensorRTLLM]] — engines implementing these techniques.
- [[Llama3]] — the 8B production case study.
- [[ModelServing]] / [[CostPerInference]] — the practice and the energy/$/token economics.
- [[mlsysbook-ch13-model-serving]] — source.
