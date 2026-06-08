---
title: "Dynamic Model Selection"
type: concept
tags: [agentic-design-patterns, agents, cost-optimization, routing, model-selection, latency]
sources: [agentic-design-patterns-ch16-resource-aware]
last_updated: 2026-06-07
---

# Dynamic Model Selection

**Dynamic Model Selection** (also "dynamic model switching") is the core technique of the [[ResourceAwareOptimization|Resource-Aware Optimization]] pattern: at runtime, an agent **strategically selects which language model to invoke** based on the intricacy of the task at hand and the available computational resources. Simple queries are deployed to a lightweight, cost-effective model; complex, multifaceted problems are escalated to a more sophisticated, resource-intensive model.

> *"Dynamic Model Switching is a critical technique involving the strategic selection of large language models based on the intricacies of the task at hand and the available computational resources."* — [[agentic-design-patterns-ch16-resource-aware|Ch 16]]

## The cheap-vs-frontier tier split

The canonical realization is a **two-tier (or N-tier) model menu** keyed by complexity and budget:

| Tier | Example models | Used for |
|---|---|---|
| **Cheap / fast** | [[gemini|Gemini]] Flash, `gpt-4o-mini` | Simple factual recall, repetitive web/tool queries, straightforward questions |
| **Frontier / expensive** | [[gemini|Gemini]] Pro, `gpt-4o`, reasoning models (`o4-mini`) | Complex reasoning, deep analysis, high-level planning |

The selection is made by a **[[ModelRouter|Router Agent]]** — on a simple metric (query length) or via an LLM/ML classifier of query nuance — and is **gated by budget and time**: the more powerful model is chosen only when resource availability permits. Ch 16's OpenAI example adds a third axis, classifying prompts as `simple` / `reasoning` / `internet_search` and selecting a model per class.

## Why it matters in agentic systems

A single fixed model for all traffic is either over-paying on easy queries or under-performing on hard ones. Dynamic model selection makes the **quality-vs-cost-vs-latency trade-off** a runtime decision rather than a static one, so an agent stays within a budget and meets latency SLAs while still reaching for frontier capability when a task genuinely needs it. In a **hierarchical agent** (e.g. a travel planner), the planner runs on a frontier model while simple sub-tasks run on the cheap tier — spending expensive intelligence only where deep context is required.

## Connections

- [[ResourceAwareOptimization]] — the parent pattern this is the core technique of.
- [[ModelRouter]] / [[Routing]] — the routing machinery that performs the selection.
- [[ModelSelection]] — the broader (classical-ML and AI-engineering) model-selection concept; this is the *runtime, per-query* specialization.
- [[CritiqueAgent]] — feeds back to refine which model gets which query.
- [[CostAndLatency]] — the trade-off axes this balances.
- [[gemini|Gemini]] (Flash/Pro) / [[openai|OpenAI]] (gpt-4o / gpt-4o-mini / o4-mini) — the tiered model families.
- [[OpenRouter]] — its `openrouter/auto` automated selection is a managed form of this.
- [[GracefulDegradation]] / [[SequentialModelFallback]] — the failure-mode complement (switch model on unavailability).
- [[agentic-design-patterns-ch16-resource-aware]] — source.
