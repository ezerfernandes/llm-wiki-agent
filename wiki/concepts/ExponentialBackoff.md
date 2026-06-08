---
title: "Exponential Backoff"
type: concept
tags: [api, retry, rate-limit, distributed-systems, agentic-design-patterns]
sources: [hands-on-llm-ch04-text-classification, agentic-design-patterns-ch12-exception-handling]
last_updated: 2026-06-07
---

# Exponential Backoff

A retry strategy where the **sleep time between attempts doubles (or grows geometrically) after each failure** — typically with a maximum cap and a maximum retry count. Standard practice for **rate-limited APIs** including OpenAI, Anthropic, Cohere, and most cloud-service SDKs.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 names exponential backoff in the context of **OpenAI API rate limits**:

> "When dealing with external APIs, you might run into rate limit errors. These appear when you call the API too often as some APIs might limit the rate with which you can use it per minute or hour. To prevent these errors, we can implement several methods for retrying the request, including something referred to as **exponential backoff**. It performs a short sleep each time we hit a rate limit error and then retries the unsuccessful request. Whenever it is unsuccessful again, the sleep length is increased until the request is successful or we hit a maximum number of retries." — Ch 4

The chapter forward-references the OpenAI cookbook's exponential-backoff guide.

## Typical implementation

```python
import time
import random

def call_with_backoff(fn, max_retries=5, base=1.0, max_delay=60.0):
    for attempt in range(max_retries):
        try:
            return fn()
        except RateLimitError:
            delay = min(base * (2 ** attempt) + random.random(), max_delay)
            time.sleep(delay)
    raise
```

The **random jitter** (the `+ random.random()`) prevents synchronized retries from a fleet of clients ("thundering herd").

## Agentic Design Patterns (Gulli) perspective

[[agentic-design-patterns-ch12-exception-handling|Ch 12 of *Agentic Design Patterns*]] makes **retries** one of the five error-handling strategies of the [[ExceptionHandlingAndRecovery|Exception Handling and Recovery]] pattern — *"retrying the action or request, sometimes with slightly adjusted parameters, especially for transient errors."* Exponential backoff (with jitter) is the standard robust implementation of that strategy for an agent's fallible [[ToolUse|tool]]/API calls. The chapter also warns of the anti-pattern: a trading agent must *not* blindly retry a non-transient failure (an "insufficient funds" / "market closed" error) — retries are for **transient** faults, paired with [[Idempotency]] so a retried side-effect can't double-apply.

## Connections

- [[ExceptionHandlingAndRecovery]] — the agentic pattern whose "retries for transient errors" strategy this implements.
- [[GenerativeClassification]] — the Ch 4 setting where this matters.
- [[openai]] — the API provider whose rate limits Ch 4 addresses.
- [[ChatGPT]] — the model behind the rate limits in Ch 4.
- [[hands-on-llm-ch04-text-classification]] — primary source.
