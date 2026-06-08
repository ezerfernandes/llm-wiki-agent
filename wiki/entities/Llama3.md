---
title: "Llama 3"
type: entity
tags: [meta, llm, model, serving, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Llama 3

Meta's open-weight large language model family, used as the **production serving case study** in [[mlsysbook-ch13-model-serving|mlsysbook Ch 13]] (the 8-billion-parameter variant on a single NVIDIA H100 SXM5).

The worked profile: 4-bit AWQ weights ≈ 3.5 GB; a 1,000-token prompt + 256-token response under SLOs of TTFT < 200 ms and TPOT < 20 ms. Prefill at ~10,000 tok/s ⇒ TTFT ≈ 120 ms (compute-bound); decode theoretical ≈ 1.0 ms/token, realized TPOT a few ms (**[[MemoryWall|memory-bandwidth bound]]** — the full 3.5 GB weight tensor is read per token). With ~72 GB free VRAM holding ~2.2M KV-cache tokens (via [[PagedAttention]] + [[GroupedQueryAttention|GQA]]), concurrent batch reaches ~1,700+ requests. The case study's lesson: **KV-cache memory capacity bounds concurrency, bandwidth bounds decode latency, prefill compute bounds full-request throughput** — and at 70B-class scale, batch-32 hits the 80 GB OOM zone at just 8k context.

## Connections

- [[LLMServing]] — the serving regime the case study exemplifies.
- [[TTFT]] / [[TPOT]] — the two-phase metrics the case study targets.
- [[KVCache]] / [[PagedAttention]] / [[GroupedQueryAttention]] — the memory-management mechanisms.
- [[MemoryWall]] — why decode latency is bandwidth-bound.
- [[Quantization]] — the 4-bit AWQ weights.
- [[CostPerInference]] — the $/token economics derived from this profile.
- [[Meta]] — the developer.
- [[mlsysbook-ch13-model-serving]] — source.
