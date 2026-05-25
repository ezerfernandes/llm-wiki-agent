---
title: "Online Inference"
type: concept
tags: [serving, latency, inference]
sources: [madewithml-serving, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Online Inference

Real-time, low-latency model predictions served per-request (vs batch). Drives [[ModelServing]] design around throughput, caching, and warm pools.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 distinguishes **online vs batch APIs** for foundation-model inference:

> *"Online APIs optimize for latency. Requests are processed as soon as they arrive. Batch APIs optimize for cost. If your application doesn't have strict latency requirements, you can send them to batch APIs for more efficient processing."*

### Streaming mode

Most online FM APIs support **streaming** — return each generated token as it's produced rather than waiting for the full response:

> *"This reduces the time the users have to wait until the first token. The downside of this approach is that you can't score a response before showing it to users, increasing the risk of users seeing bad responses. However, you can still retrospectively update or remove a response as soon as the risk is detected."* — Ch 9

Streaming is what makes [[TTFT]] / [[TPOT]] / [[TBT]] user-visible metrics.

### Online APIs can still batch

> *"Online APIs might still batch requests together as long as it doesn't significantly impact latency. The only real difference is that an online API focuses on lower latency, whereas a batch API focuses on higher throughput."* — Ch 9

I.e., **[[ContinuousBatching|continuous batching]]** is compatible with online inference — the per-request latency budget is preserved while opportunistically batching.

### Customer-facing vs offline use cases

Per Ch 9, **customer-facing** use cases (chatbots, code generation) → online. **Tolerant** use cases (synthetic data, periodic reports, onboarding bulk processing, recommendation pre-generation) → batch.

## Connections

- [[BatchInference]] — the cost-priority counterpart.
- [[TTFT]] / [[TPOT]] / [[TBT]] — the latency metrics online inference must respect.
- [[Goodput]] — the SLO-aware throughput metric for online services.
- [[ContinuousBatching]] — the batching mode compatible with online latency budgets.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
