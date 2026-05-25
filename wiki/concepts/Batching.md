---
title: "Batching (Inference Serving)"
type: concept
tags: [inference, serving, optimization, throughput, latency]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Batching (Inference Serving)

**Grouping multiple inference requests together to share a forward pass and amortize per-step overhead.** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"One of the easiest ways to reduce your cost is batching. In production, your inference service might receive multiple requests simultaneously. Instead of processing each request separately, batching the requests that arrive around the same time together can significantly reduce the service's throughput."*

Huyen's bus analogy: *"If processing each request separately is like everyone driving their own car, batching is like putting them together on a bus. A bus can move more people, but it can also make each person's journey longer."*

## The three batching strategies

| | [[StaticBatching|Static]] | [[DynamicBatching|Dynamic]] | [[ContinuousBatching|Continuous]] |
|---|---|---|---|
| **Trigger** | Batch size N filled | Size N OR time T elapsed | Always — admit when slots open |
| **Bus analogy** | Bus leaves only when full | Bus leaves on schedule or full | Bus replaces passengers on the fly |
| **First-request latency** | Bad — wait for last | Bounded by T | Excellent — no batch-wait |
| **Compute efficiency** | Excellent | Sometimes wastes slots | Excellent (sustained) |
| **Implementation** | Easy | Easy | Hard |
| **Use in 2024** | Rare in production LLM | Common | Dominant |

## Latency–throughput trade-off

Batching is the canonical lever in the **latency–throughput trade-off**. LinkedIn's AI team reported it's "not uncommon to double or triple the throughput if you're willing to sacrifice TTFT and TPOT." This is exactly why **[[Goodput|goodput]]** (SLO-respecting throughput) is more useful than raw throughput as a target.

## Why naive batching fails for LLMs

> *"In naive batching implementations, all batch requests have to be completed before their responses are returned. For LLMs, some requests might take much longer than others. If one request in a batch generates only 10 response tokens and another request generates 1,000 response tokens, the short response has to wait until the long response is completed before being returned to the user. This results in unnecessary latency for short requests."* — Ch 9

This is the structural problem **[[ContinuousBatching|continuous batching]]** (Orca, Yu et al. 2022) solves: completed responses leave the batch immediately and new requests fill their slot.

## Connections

- [[StaticBatching]] / [[DynamicBatching]] / [[ContinuousBatching]] — the three strategies.
- [[Goodput]] — the better optimization target than raw throughput.
- [[TTFT]] / [[TPOT]] — the per-request latencies batching trades off against throughput.
- [[PrefillDecodeDisaggregation]] — orthogonal serving-side optimization that pairs naturally.
- [[PromptCaching]] — orthogonal serving-side optimization.
- [[BatchInference]] / [[OnlineInference]] — adjacent macro-level distinctions (when to invoke the model at all).
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
