---
title: "TTFT (Time to First Token)"
type: concept
tags: [latency, metrics, inference, autoregressive, mlsysbook, serving]
sources: [ai-engineering-ch01-intro, ai-engineering-ch09-inference-optimization, mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
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

## From [[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]

Ch 13 frames TTFT as the metric of the **prefill phase**, which is *compute-bound* (the prompt's tokens process in parallel) — contrasting with [[TPOT]]'s memory-bandwidth-bound decode phase. TTFT measures responsiveness, TPOT measures fluidity (the "rhythm" of token arrival). A model can have fast TTFT but sluggish TPOT if the [[MemoryWall|memory wall]] binds. Production targets: TTFT < 500 ms (1,000-token prompt). In the 8B [[Llama3|Llama 3]]/H100 case study, prefill at ~10,000 tok/s gives TTFT ≈ 120 ms (within a 200 ms SLO); [[PrefixCaching|prefix caching]] collapses prefill (and TTFT) for shared prompts. See also [[LLMServing]], [[mlsysbook-ch13-model-serving]].
