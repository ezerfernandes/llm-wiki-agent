---
title: "OpenRouter"
type: entity
tags: [organization, llm-routing, infrastructure, api-aggregator, agentic-design-patterns]
sources: [2603.19247-prompt-optimization-jailbreaking, agentic-design-patterns-ch16-resource-aware]
last_updated: 2026-06-07
---

# OpenRouter

Provider-aggregation routing layer for LLM APIs. Single API surface that fans out to multiple frontier and open-weights model providers. Conceptual sibling to [[LiteLLM]]; both reduce per-provider client logic to a unified call.

## In this wiki

- [[2603.19247-prompt-optimization-jailbreaking]] — used for inference against all four target models (Qwen-3 8B, LLaMA-4 Maverick, Gemini 2.5 Pro, Claude 4.5 Sonnet) at $T = 0.7$ with max 5,000 tokens (retry bumps to 8,000). The single routing layer is what makes the cross-vendor red-teaming experiment tractable.

## Two routing methodologies ([[agentic-design-patterns-ch16-resource-aware|Agentic Design Patterns Ch 16]])

[[agentic-design-patterns-ch16-resource-aware|Ch 16 (Resource-Aware Optimization)]] uses OpenRouter as a hands-on example, describing it as *"a unified interface to hundreds of AI models via a single API endpoint... automated failover and cost-optimization."* The chapter calls the chat-completions endpoint (`https://openrouter.ai/api/v1/chat/completions`) via `requests` and documents two distinct routing modes:

- **Automated Model Selection** — `"model": "openrouter/auto"` routes the request to an optimized model chosen from a curated set, predicated on the prompt's content; the model that actually processed the request is returned in the response metadata. (A managed form of [[DynamicModelSelection|dynamic model selection]].)
- **[[SequentialModelFallback|Sequential Model Fallback]]** — a hierarchical `"models": [...]` list providing operational redundancy: the primary is tried first, and on any error (unavailability, rate-limiting, content filtering) the request re-routes to the next model until one succeeds or the list is exhausted. Final cost and returned model id = the model that completed the request. This is the [[GracefulDegradation|graceful-degradation]] mechanism of the [[ResourceAwareOptimization|Resource-Aware Optimization]] pattern.

OpenRouter also publishes a rankings **leaderboard** (`openrouter.ai/rankings`) ordering models by cumulative token production, and surfaces latest models across providers (ChatGPT, [[gemini|Gemini]], Claude).

## Connections

- [[LiteLLM]] — sibling provider-abstraction layer (used by [[DSPy]] for the same purpose); [[GoogleADK|ADK]] integrates non-Gemini models through LiteLLM, an alternative to OpenRouter for the same cross-provider goal.
- [[DSPy]] — the framework consuming OpenRouter in the source paper.
- [[ResourceAwareOptimization]] / [[SequentialModelFallback]] / [[DynamicModelSelection]] — the Ch 16 pattern and its mechanisms OpenRouter implements.
- [[GracefulDegradation]] — the fallback principle behind sequential model fallback.
- [[2603.19247-prompt-optimization-jailbreaking]] — primary wiki source.
- [[agentic-design-patterns-ch16-resource-aware]] — Ch 16 source.
