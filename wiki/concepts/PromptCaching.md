---
title: "Prompt Caching"
type: concept
tags: [inference, serving, optimization, caching, llm-engineering]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Prompt Caching

**Storing the processed (prefilled) form of an overlapping prompt segment so that subsequent queries with the same prefix don't re-process it.** Also called **context cache** or **prefix cache**. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Many prompts in an application have overlapping text segments. A prompt cache stores these overlapping segments for reuse, so you only need to process them once."*

Introduced by Gim et al. November 2023.

## What gets cached

- **System prompts** — typically reused on every query of an application.
- **Long documents** — when many user queries ask about the same book, codebase, or report.
- **Multi-turn conversation history** — older messages whose KV cache can be reused across turns.

The cache is essentially the [[KVCache]] of the cached prefix, stored alongside the cache key.

## Provider pricing (as of late 2024)

| Provider | Discount on cached tokens | Storage fee |
|---|---|---|
| **Google Gemini** | **75% off cached input tokens** | $1.00 per 1M tokens per hour |
| **Anthropic** | Up to **90% cost savings**, up to **75% latency reduction** | (varies by tier) |

## Anthropic's Table 9-3 latency-cost numbers

| Use case | TTFT no-cache | TTFT cached | Cost reduction |
|---|---|---|---|
| Chat with a 100K-token book | 11.5 s | **2.4 s** (–79%) | **–90%** |
| Many-shot prompt (10K tokens) | 1.6 s | 1.1 s (–31%) | –86% |
| 10-turn convo with long system prompt | ~10 s | ~2.5 s (–75%) | –53% |

## Back-of-the-envelope value

> *"If your system prompt is 1,000 tokens, and your application generates one million model API calls daily, a prompt cache will save you from processing approximately one billion repetitive input tokens a day!"* — Ch 9

The math: 1K-token system prompt × 1M calls/day = 10⁹ input tokens/day that don't need to be re-prefilled.

## Trade-offs

- **Cache storage is large.** Like the [[KVCache]], the prompt cache can be huge — and it's billable on managed APIs ($1/M-token-hour on Gemini).
- **DIY is hard.** "Implementing prompt caching can require significant engineering effort" unless you're using a model API with built-in support.
- **llama.cpp** has prompt caching but only at "whole prompt" / single-chat-session granularity (limited).

## Pairs naturally with

- **[[PrefillDecodeDisaggregation|Prefill-decode disaggregation]]** — cache lives on the prefill side; cache hits skip the prefill cluster entirely.
- **[[ContinuousBatching|Continuous batching]]** — cache-hit requests join the decode queue immediately without waiting for prefill.
- **[[MultiLoraServing|Multi-LoRA serving]]** — the *routing* counterpart to prompt caching (one is request routing by adapter, the other is prefix sharing).

## Connections

- [[KVCache]] — the underlying structure being cached and reused.
- [[Prefill]] — the phase prompt caching replaces with a lookup.
- [[PrefillDecodeDisaggregation]] — natural deployment pairing.
- [[ContinuousBatching]] — natural batching pairing.
- [[MultiLoraServing]] — sibling serving-routing technique.
- [[TTFT]] — the metric prompt caching most directly improves.
- [[Anthropic]] / [[google|Google]] / [[openai|OpenAI]] — provider implementations.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
