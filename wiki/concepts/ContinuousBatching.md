---
title: "Continuous Batching (In-Flight Batching)"
type: concept
tags: [inference, optimization, serving, llm-engineering]
sources: [leh-ch08-inference-optimization, leh-ch10-inference-pipeline-deployment, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

## Definition
**Continuous batching** (a.k.a. **in-flight batching**) is an LLM-serving optimization that dynamically evicts completed requests from a running batch and immediately admits waiting requests in their place — keeping the accelerator saturated rather than waiting for the slowest request to finish before forming the next batch. It is one of the primary throughput-multipliers in modern LLM inference engines.

## In LLM Engineer's Handbook
[[leh-ch08-inference-optimization]] introduces continuous batching as one of three foundational generation-loop optimizations (alongside static KV cache + `torch.compile` and speculative decoding). The chapter notes the technique is tuned via a *waiting-served ratio* hyperparameter and is supported by all three production inference engines surveyed: [[TextGenerationInference|TGI]], vLLM, and TensorRT-LLM. [[leh-ch10-inference-pipeline-deployment]] highlights continuous batching as TGI's headline performance feature in the SageMaker DLC: "Continuous batching of incoming requests, thus improving throughput by dynamically batching requests as they arrive." Together with static KV cache and speculative decoding, continuous batching is cited as part of the recipe that yields 2–4× inference speedups with no quality loss.

## Key details
- Evicts finished requests and admits waiting ones *mid-batch* — does not wait for the full batch to complete.
- Tuned via a waiting-served ratio hyperparameter.
- Supported by TGI, vLLM, and TensorRT-LLM out of the box.
- Pairs naturally with [[PagedAttention]] (which removes contiguous-allocation waste from the KV cache).
- Critical for high-traffic serving where request length distributions are heavy-tailed.

## Connections
- [[InferenceOptimization]] — the broader technique family.
- [[PagedAttention]] — complementary KV-cache optimization that enables fine-grained admission.
- [[SpeculativeDecoding]] / [[flashattention]] — sibling generation-loop optimizations.
- [[TextGenerationInference]] / [[vLLM]] / [[TensorRTLLM]] — engines that implement continuous batching.
- [[BatchInference]] / [[OnlineInference]] — broader batching modes.
- [[KVCache]] — the cache continuous batching must manage carefully.
- [[ModelServing]] — the practice continuous batching optimizes.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 places continuous batching as **the third and dominant** of three [[Batching|batching]] strategies (after [[StaticBatching|static]] and [[DynamicBatching|dynamic]]) and credits the **Orca paper** (Yu et al. 2022) as the introduction:

> *"Continuous batching allows responses in a batch to be returned to users as soon as they are completed. It works by selectively batching operations that don't cause the generation of one response to hold up another, as introduced in the paper Orca (Yu et al., 2022). After a request in a batch is completed and its response returned, the service can add another request into the batch in its place, making the batching continuous. It's like a bus that, after dropping off one passenger, can immediately pick up another passenger to maximize its occupancy rate."*

### The problem continuous batching solves

> *"In naive batching implementations, all batch requests have to be completed before their responses are returned. For LLMs, some requests might take much longer than others. If one request in a batch generates only 10 response tokens and another request generates 1,000 response tokens, the short response has to wait until the long response is completed before being returned to the user."* — Ch 9

The head-of-line blocking that static and dynamic batching produce, eliminated.

### Aliases

Continuous batching is also called **in-flight batching** (especially in NVIDIA/TensorRT-LLM contexts).
