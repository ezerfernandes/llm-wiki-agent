# DSPy Caching Tutorial

Source: https://dspy.ai/tutorials/cache/

## Introduction

DSPy's caching system is architected in three distinct layers:

1. **In-memory cache** — uses `cachetools.LRUCache` for rapid access
2. **On-disk cache** — uses `diskcache.FanoutCache` for persistent storage
3. **Prompt cache** — server-side, managed by LLM providers (OpenAI, Anthropic, etc.)

Both in-memory and on-disk caching are enabled by default without requiring additional configuration.

## Default Behavior

Cached responses execute dramatically faster than fresh calls and return `None` for usage metrics when `track_usage=True` is configured (because no actual provider call was made).

```python
import dspy
import os
import time

os.environ["OPENAI_API_KEY"] = "{your_openai_key}"

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"), track_usage=True)

predict = dspy.Predict("question->answer")

start = time.time()
result1 = predict(question="Who is the GOAT of basketball?")
print(f"Time elapse: {time.time() - start: 2f}\n\nTotal usage: {result1.get_lm_usage()}")

start = time.time()
result2 = predict(question="Who is the GOAT of basketball?")
print(f"Time elapse: {time.time() - start: 2f}\n\nTotal usage: {result2.get_lm_usage()}")
```

## Cache Configuration

### Disabling cache layers

```python
dspy.configure_cache(
    enable_disk_cache=False,
    enable_memory_cache=False,
)
```

### Managing capacity

```python
dspy.configure_cache(
    enable_disk_cache=True,
    enable_memory_cache=True,
    disk_size_limit_bytes=YOUR_DESIRED_VALUE,
    memory_max_entries=YOUR_DESIRED_VALUE,
)
```

### Parameters of `dspy.configure_cache`

- `enable_disk_cache` (bool) — toggle on-disk persistence
- `enable_memory_cache` (bool) — toggle in-memory LRU caching
- `disk_size_limit_bytes` (int) — max size in bytes for on-disk cache
- `memory_max_entries` (int) — max entries for in-memory cache
- `restrict_pickle` (bool) — enable restricted deserialization mode
- `safe_types` (list) — user-registered types allowed under restricted pickle

## Provider-Side Prompt Caching

Pass `cache_control_injection_points` to `dspy.LM()` to enable Anthropic/OpenAI prompt caching. Useful for long system prompts or repeated ReAct module calls.

```python
import dspy
import os

os.environ["ANTHROPIC_API_KEY"] = "{your_anthropic_key}"
lm = dspy.LM(
    "anthropic/claude-sonnet-4-5-20250929",
    cache_control_injection_points=[
        {
            "location": "message",
            "role": "system",
        }
    ],
)
dspy.configure(lm=lm)

predict = dspy.Predict("question->answer")
result = predict(question="What is the capital of France?")
```

## Restricted Pickle Mode (Security)

`restrict_pickle` restricts which types the cache is allowed to deserialize, preventing arbitrary code execution from corrupted cache files.

```python
dspy.configure_cache(restrict_pickle=True)
```

Default allowlist includes:
- LiteLLM and OpenAI response types (pydantic models for LM calls, embeddings, Responses API)
- NumPy array reconstruction helpers (for embedding caches)
- User-registered custom types via `safe_types`

Register custom types:

```python
from dataclasses import dataclass

@dataclass
class MyResult:
    score: float
    label: str

dspy.configure_cache(restrict_pickle=True, safe_types=[MyResult])
```

If a cached type isn't approved, cache treats it as a miss, returns `None`, and logs the rejected type. Nested custom types must all be registered separately.

## Custom Cache Subclass

Subclass `dspy.clients.Cache` and override `cache_key`, `get`, `put`:

```python
class CustomCache(dspy.clients.Cache):
    def __init__(self, **kwargs):
        {write your own constructor}

    def cache_key(self, request: dict[str, Any], ignored_args_for_cache_key: Optional[list[str]] = None) -> str:
        {write your logic of computing cache key}

    def get(self, request: dict[str, Any], ignored_args_for_cache_key: Optional[list[str]] = None) -> Any:
        {write your cache read logic}

    def put(
        self,
        request: dict[str, Any],
        value: Any,
        ignored_args_for_cache_key: Optional[list[str]] = None,
        enable_memory_cache: bool = True,
    ) -> None:
        {write your cache write logic}
```

Default `cache_key` hashes all litellm request arguments (excluding credentials). Override to ignore parameters like model selection.

### Example: message-only cache key (hits across different models)

```python
import dspy
import os
import time
from typing import Dict, Any, Optional
import orjson
from hashlib import sha256

os.environ["OPENAI_API_KEY"] = "{your_openai_key}"

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

class CustomCache(dspy.clients.Cache):

    def cache_key(self, request: dict[str, Any], ignored_args_for_cache_key: Optional[list[str]] = None) -> str:
        messages = request.get("messages", [])
        return sha256(orjson.dumps(messages, option=orjson.OPT_SORT_KEYS)).hexdigest()

dspy.cache = CustomCache(enable_disk_cache=True, enable_memory_cache=True, disk_cache_dir=dspy.clients.DISK_CACHE_DIR)

predict = dspy.Predict("question->answer")

start = time.time()
result1 = predict(question="Who is the GOAT of volleyball?")
print(f"Time elapse: {time.time() - start: 2f}")

start = time.time()
with dspy.context(lm=dspy.LM("openai/gpt-4.1-mini")):
    result2 = predict(question="Who is the GOAT of volleyball?")
print(f"Time elapse: {time.time() - start: 2f}")
```

Contrast: with default cache, switching the model under `dspy.context` would miss the cache because model name is part of the default key.

## Use Cases

1. Repeated identical requests — leverage in-memory + on-disk caches for speed
2. Different responses for identical requests — disable caching
3. Limited disk write permissions — disable disk cache, keep memory cache
4. Memory constraints — disable memory cache
5. Provider-side caching with ReAct modules — reduce latency/cost on similar prompts
6. Long system prompts — provider-side caching for constant context
7. Custom cache key logic — ignore params like model selection
8. Security-conscious caching — `restrict_pickle` prevents code execution from corrupted cache files
