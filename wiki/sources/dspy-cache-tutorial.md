---
title: "DSPy Caching Tutorial"
type: source
tags: [dspy, caching, tutorial, performance]
date: 2026-05-24
source_file: raw/dspy-cache-tutorial.md
---

## Summary
Official DSPy tutorial covering its three-layer caching architecture: in-memory ([[LRUCache]] via `cachetools`), on-disk (`diskcache.FanoutCache`), and provider-side prompt cache. Documents `dspy.configure_cache` parameters, restricted-pickle security mode, custom `dspy.clients.Cache` subclassing for bespoke key logic, and provider-side `cache_control_injection_points` for Anthropic/OpenAI. Both memory and disk layers are enabled by default; cached calls return `None` for usage when `track_usage=True`.

## Key Claims
- DSPy ships with three independent cache layers (memory, disk, provider) — all controllable independently.
- In-memory and on-disk caches are **on by default**; no configuration needed for basic speed-ups on repeated identical requests.
- Cached responses report `None` usage under `track_usage=True` because no provider call occurs.
- `dspy.configure_cache` controls toggling and capacity (`disk_size_limit_bytes`, `memory_max_entries`).
- Default cache key hashes **all** litellm request arguments (excluding credentials) — including the model name, so switching models misses the cache.
- Subclassing `dspy.clients.Cache` and overriding `cache_key`/`get`/`put` allows custom logic (e.g., key on `messages` only to share hits across models).
- `restrict_pickle=True` enables an allowlist-based deserializer that defends against arbitrary code execution from tampered cache files; allowlist covers LiteLLM/OpenAI response types and NumPy reconstruction helpers by default, plus user-registered `safe_types`.
- Unapproved types under restricted pickle are treated as cache misses (return `None`) with a logged rejection — not raised exceptions.
- Provider-side prompt caching is opted into via `cache_control_injection_points` on `dspy.LM()`; recommended for long static system prompts and repeated [[DSPyReAct|ReAct]] tool loops.

## Key Quotes
> "DSPy's caching system is architected in three distinct layers: In-memory cache (using cachetools.LRUCache), On-disk cache (using diskcache.FanoutCache), and Prompt cache (server-side, managed by LLM providers)." — tutorial intro

> "restrict_pickle mode restricts which types the cache is allowed to deserialize." — security section

## Connections
- [[DSPyCache]] — primary concept page distilled from this tutorial
- [[DSPyLM]] — `dspy.LM(...)` is where `cache_control_injection_points` is configured
- [[DSPyPredict]] — example module used to demonstrate cache hits
- [[DSPyModules]] — caching applies to all module calls, including ReAct
- [[PromptCaching]] — generic concept of provider-side prompt caching that DSPy exposes
- [[LRUCache]] — in-memory layer implementation strategy
- [[DSPyAsync]] — async modules share the same cache infrastructure

## Contradictions
- None identified against existing wiki content. Complements existing DSPy pages by filling a previously undocumented surface area (caching).
