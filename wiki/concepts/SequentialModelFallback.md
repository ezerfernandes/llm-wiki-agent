---
title: "Sequential Model Fallback"
type: concept
tags: [agentic-design-patterns, agents, fallback, reliability, routing, cost-optimization, openrouter]
sources: [agentic-design-patterns-ch16-resource-aware]
last_updated: 2026-06-07
---

# Sequential Model Fallback

**Sequential Model Fallback** is a reliability mechanism in which a request is attempted against a **hierarchical list of models in order**: the primary model is tried first, and if it fails for *any* reason — service unavailability, rate-limiting, content filtering — the request is automatically **re-routed to the next model in the sequence**, continuing until one succeeds or the list is exhausted. It is the model-level realization of the [[ResourceAwareOptimization|Resource-Aware Optimization]] pattern's **fallback** strategy and a concrete form of [[GracefulDegradation|graceful degradation]].

This is one of [[OpenRouter]]'s two routing methodologies described in [[agentic-design-patterns-ch16-resource-aware|Ch 16 of *Agentic Design Patterns*]] (the other being **Automated Model Selection**, `"model": "openrouter/auto"`):

```json
{
  "models": ["anthropic/claude-3.5-sonnet", "gryphe/mythomax-l2-13b"],
  ...
}
```

> *"Should this primary model fail to respond due to any number of error conditions — such as service unavailability, rate-limiting, or content filtering — the system will automatically re-route the request to the next specified model in the sequence. This process continues until a model in the list successfully executes the request or the list is exhausted."* — Ch 16

**Cost/identity attribution.** The final cost of the operation and the model identifier returned in the response correspond to the model that **successfully completed** the computation — not the failed primaries.

## Why it matters in agentic systems

Frontier models are subject to outages, throttling, and content-policy refusals. A fallback chain provides **operational redundancy** so an agent maintains service continuity instead of failing completely — switching to a default or more affordable backup model when the preferred one is unavailable. It is the failure-time complement to [[DynamicModelSelection|dynamic model selection]]'s success-time choice.

## Connections

- [[ResourceAwareOptimization]] — the pattern whose fallback strategy this implements.
- [[GracefulDegradation]] — the broader principle (partial/continued service beats total failure).
- [[OpenRouter]] — the provider exposing this via a hierarchical `models` list.
- [[DynamicModelSelection]] — the complementary success-time model choice.
- [[ExceptionHandlingAndRecovery]] — Ch 12's fault-tolerance pattern; fallback is one of its strategies.
- [[ModelRouter]] / [[Routing]] — the routing layer this sits within.
- [[agentic-design-patterns-ch16-resource-aware]] — source.
