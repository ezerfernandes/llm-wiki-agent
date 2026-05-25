---
title: "TTFT (Time to First Token)"
type: concept
tags: [latency, metrics, inference, autoregressive]
sources: [ai-engineering-ch01-intro, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# TTFT — Time to First Token

**The time elapsed between submitting a request to a foundation-model API and receiving the first generated token back.** One of three latency metrics named in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1's]] [[UsefulnessThreshold|usefulness threshold]] discussion (the others being [[TPOT|TPOT]] and total latency).

## What TTFT measures

TTFT captures the *startup* cost of an inference: prompt tokenization, KV-cache initialization, prefill computation across all prompt tokens, and any network/queueing overhead. After TTFT, generation enters its steady-state per-token cadence (measured by [[TPOT]]).

In a chat or streaming UI, **TTFT is the user-visible "how responsive does this feel?" metric** — even if the full response takes 5 seconds, if the first token appears in 200ms the experience feels alive.

## Position in the latency budget

Ch 1's latency framing:

- **Total latency = TTFT + (TPOT × output length)**

For [[AutoregressiveLanguageModel|autoregressive]] models, sequential generation amplifies output-length sensitivity — so optimizing TTFT alone isn't enough for long outputs. But TTFT is usually the single largest user-perception-of-speed lever.

## Chapter coverage

Chapter 9 of *AI Engineering* is the deep dive on [[InferenceOptimization|inference optimization]], where TTFT-targeted techniques (prefill batching, paged attention, prompt caching) live.

## Connections

- [[InferenceOptimization]] — the discipline that targets TTFT.
- [[TPOT]] — companion latency metric (steady-state per-token).
- [[UsefulnessThreshold]] — the planning framework where TTFT is a deployment-readiness bar.
- [[AutoregressiveLanguageModel]] — the model class whose sequential nature makes latency metrics necessary.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 deepens TTFT into a full **distribution-aware** metric:

### Percentiles, not averages

> *"It's more helpful to look at latency in percentiles, as they tell you something about a certain percentage of your requests. The most common percentile is the 50th percentile, abbreviated as p50 (median). ... Typically, the percentiles you'll want to look at are p90, p95, and p99."*

Example: 10 requests with TTFT values 100/102/100/100/99/104/110/90/**3000**/95 ms have an average TTFT of **390 ms** — but the outlier (3000 ms) hides the fact that p50 is around 100 ms.

### TTFT vs Time-to-Publish

For [[ChainOfThought|CoT]] / [[Agent|agentic]] queries where intermediate plan/action tokens aren't shown to users, model-internal TTFT can differ dramatically from user-visible "first token." Ch 9 introduces [[TimeToPublish]] as the explicit user-visible variant.

### What TTFT depends on

- Prefill compute → determined by input length, model size, hardware FLOP/s.
- KV-cache initialization → depends on KV-cache architecture (MQA/GQA help).
- [[PromptCaching|Prompt cache]] hits → can drop TTFT 79% on a 100K-token cached prompt (Anthropic numbers).
- [[PrefillDecodeDisaggregation|Prefill-decode disaggregation]] → eliminates compute contention with concurrent decode jobs.

### The TTFT/TPOT trade-off

> *"Reducing TTFT at the cost of higher TPOT is possible by shifting more compute instances from decoding to prefilling and vice versa."* — Ch 9

This is the **prefill:decode instance ratio** lever — 2:1–4:1 for TTFT priority; 1:2–1:1 for TPOT priority.
