---
title: "DSPy Cache"
type: concept
tags: [dspy, caching, performance, security]
sources: [dspy-cache-tutorial]
last_updated: 2026-05-24
---

## Overview

DSPy provides a three-layer caching system to reduce latency and cost across repeated LM calls. Both the in-memory and on-disk layers are **enabled by default** — programs using [[DSPyPredict]], [[DSPyModules]], or any module that ultimately calls [[DSPyLM]] benefit automatically.

## The Three Layers

| Layer | Implementation | Scope | Default |
|---|---|---|---|
| In-memory | `cachetools.LRUCache` ([[LRUCache]]) | Process lifetime | On |
| On-disk | `diskcache.FanoutCache` | Persistent across runs | On |
| Provider-side | Vendor [[PromptCaching]] ([[anthropic|Anthropic]] / [[openai|OpenAI]]) | Provider-managed | Off (opt-in) |

A request flows: memory hit → disk hit → provider call (which may itself hit provider-side cache).

## `dspy.configure_cache` Parameters

- `enable_disk_cache` (bool) — toggle on-disk persistence
- `enable_memory_cache` (bool) — toggle in-memory LRU
- `disk_size_limit_bytes` (int) — max size of on-disk cache
- `memory_max_entries` (int) — max entries in memory
- `restrict_pickle` (bool) — restricted deserialization mode (security)
- `safe_types` (list) — additional types allowed under restricted pickle

```python
dspy.configure_cache(
    enable_disk_cache=True,
    enable_memory_cache=True,
    disk_size_limit_bytes=2_000_000_000,
    memory_max_entries=10_000,
)
```

## Cache Key

The default `cache_key` hashes **all** litellm request arguments (excluding credentials). This means the model name is part of the key — switching from `gpt-4o-mini` to `gpt-4.1-mini` for the same prompt misses the cache.

Cached responses return `None` for `result.get_lm_usage()` when [[DSPyLM|track_usage]] is enabled, because no provider call was made.

## Provider-Side Prompt Caching

Opt in via `cache_control_injection_points` on `dspy.LM()`:

```python
lm = dspy.LM(
    "anthropic/claude-sonnet-4-5-20250929",
    cache_control_injection_points=[
        {"location": "message", "role": "system"},
    ],
)
dspy.configure(lm=lm)
```

Recommended whenever a long static system prompt or tool schema is sent on every call — e.g., [[DSPyTools|ReAct]] tool loops, large few-shot demos, or [[DSPyAdapters|adapter]]-injected schemas.

## Restricted Pickle (Security)

`restrict_pickle=True` swaps in an allowlist-based deserializer. Allowlist covers:

- LiteLLM and OpenAI response types (pydantic models for LM calls, embeddings, Responses API)
- NumPy array reconstruction helpers (for embedding caches)
- Any types passed via `safe_types`

```python
from dataclasses import dataclass

@dataclass
class MyResult:
    score: float
    label: str

dspy.configure_cache(restrict_pickle=True, safe_types=[MyResult])
```

Unapproved cached types are treated as **cache misses** (return `None`) with a log entry — not raised exceptions. Nested custom types must each be registered separately.

**Why it matters:** without restriction, a tampered on-disk cache file could trigger arbitrary code execution during unpickling. Critical if the cache directory is shared, synced, or otherwise reachable by untrusted parties.

## Custom Cache Subclass

Subclass `dspy.clients.Cache` to override key computation or storage. Common pattern: ignore the model so semantically-equivalent prompts share a hit across model versions.

```python
import orjson
from hashlib import sha256
from typing import Any, Optional

class CustomCache(dspy.clients.Cache):
    def cache_key(self, request: dict[str, Any], ignored_args_for_cache_key: Optional[list[str]] = None) -> str:
        messages = request.get("messages", [])
        return sha256(orjson.dumps(messages, option=orjson.OPT_SORT_KEYS)).hexdigest()

dspy.cache = CustomCache(
    enable_disk_cache=True,
    enable_memory_cache=True,
    disk_cache_dir=dspy.clients.DISK_CACHE_DIR,
)
```

Match base class signatures (or accept `**kwargs`) to avoid runtime errors. Assign the instance to `dspy.cache` after construction.

## When to Disable

- **Need fresh responses every run** — disable both layers.
- **Read-only filesystem / containerized env** — `enable_disk_cache=False`, keep memory.
- **Memory-constrained worker** — `enable_memory_cache=False`, keep disk.
- **Benchmarking / [[DSPyEvaluation|evaluation]] runs** where cache hits would distort latency or cost numbers — disable for the run, re-enable after.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-cache-tutorial]] — canonical receipt: the three-layer architecture ([[LRUCache]] / `diskcache.FanoutCache` / provider-side), `dspy.configure_cache(...)` parameters, `restrict_pickle=True` + `safe_types=[...]` security mode, and the `dspy.clients.Cache` subclass pattern for custom key computation.
- [[dspy-output-refinement-tutorial]] — [[DSPyBestOfN|`dspy.BestOfN`]] / [[DSPyRefine|`dspy.Refine`]] vary the **rollout ID** across N attempts as the canonical *intentional* cache-bypass mechanism — same prompt, distinct rollouts, no in-memory / on-disk hit.

## Related

- [[DSPyLM]] — surface where `cache_control_injection_points` is wired
- [[DSPyPredict]], [[DSPyModules]] — beneficiaries of caching
- [[DSPyAsync]] — async modules share the same cache
- [[DSPyEvaluation]], [[DSPyOptimization]] — long optimizer runs benefit massively from disk cache
- [[PromptCaching]] — generic provider-side concept
- [[LRUCache]] — eviction strategy used by the memory layer
