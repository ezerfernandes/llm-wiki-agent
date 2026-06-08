---
title: "Chapter 16 — Resource-Aware Optimization (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, resource-aware-optimization, cost-optimization, routing, model-selection, fallback, latency]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 16 of [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] introduces **[[ResourceAwareOptimization|Resource-Aware Optimization]]** (pattern #16): enabling agents to dynamically monitor and manage **computational, temporal, and financial** resources during operation, choosing actions to hit a resource budget or optimize efficiency rather than just sequencing tasks. The core mechanism is a **Router Agent** that classifies an incoming request's complexity and dispatches simple queries to a fast/cheap model (e.g. Gemini Flash) and complex ones to a powerful/expensive model (e.g. Gemini Pro), with a **Critic/Critique Agent** that evaluates responses and feeds back to improve the routing logic, plus **fallback** to a backup model for graceful degradation. The chapter gives hands-on examples in [[GoogleADK|Google ADK]], the [[openai|OpenAI]] API, and [[OpenRouter]], then surveys a broader spectrum of resource-aware techniques. (Agentic Design Patterns, PDF pp 246–261.)

## Key Claims
- Resource-Aware Optimization differs from simple planning (action sequencing): it makes execution decisions to **achieve goals within resource budgets or to optimize efficiency** — e.g. accurate-but-expensive vs faster-cheaper models, or more compute for a refined answer vs a quick less-detailed one.
- A **fallback mechanism** is a key strategy: when a preferred model is unavailable (overloaded/throttled), the system automatically switches to a default or more affordable model to maintain **service continuity** and **graceful degradation** instead of failing completely.
- Use cases: **cost-optimized LLM usage** (budget-bounded model choice), **latency-sensitive operations** (faster, less-comprehensive reasoning path), **energy efficiency** (edge/limited-power devices conserving battery), **fallback for reliability**, **data-usage management** (summarized retrieval vs full downloads to save bandwidth), and **adaptive task allocation** (multi-agent agents self-assign by current load/time).
- The canonical hands-on system assesses each question's difficulty: simple queries → a cost-effective model (Gemini Flash); complex inquiries → a more powerful model (Gemini Pro), with the choice also gated by **budget and time** availability — dynamic model selection.
- In a hierarchical travel-planner agent, the **planner** (high-level itinerary reasoning) uses Gemini Pro while the simple, repetitive sub-tasks (flight lookups, hotel availability, restaurant reviews) run on Gemini Flash.
- **[[GoogleADK|Google ADK]]** supports this via multi-agent architecture; model flexibility lets it use various Gemini models directly or integrate other models through **[[LiteLLM]]**, and its LLM-driven routing supports adaptive behavior. Built-in evaluation features assess agent performance for refinement.
- A **Router Agent** can route on a simple metric (query length: short→cheap, long→capable) or, more sophisticatedly, use an LLM or ML model to analyze query nuance/complexity; the LLM router can be improved by **prompt tuning** and **fine-tuning on query→optimal-model datasets**.
- The **Critic/Critique Agent** evaluates responses for self-correction, performance monitoring (accuracy/relevance metrics), and signaling RL/fine-tuning; by flagging suboptimal routing (e.g. simple→Pro or complex→Flash) it contributes **indirect budget management** that improves resource allocation and cost savings.
- The OpenAI example classifies each prompt into **simple** (`gpt-4o-mini`), **reasoning** (`o4-mini`), or **internet_search** (`gpt-4o` + Google Custom Search) to avoid wasting compute on simple requests.
- **[[OpenRouter]]** offers a unified interface to hundreds of models with two routing methodologies: **Automated Model Selection** (`"model": "openrouter/auto"` picks an optimized model from a curated set by prompt content) and **Sequential Model Fallback** (`"models": [...]` tries a hierarchical list, re-routing on error — unavailability, rate-limiting, content filtering — until one succeeds; final cost/model = the successful one).
- Beyond dynamic model switching, the chapter lists further techniques: **Adaptive Tool Use & Selection**, **Contextual Pruning & Summarization** (cut prompt token count to reduce inference cost), **Proactive Resource Prediction**, **Cost-Sensitive Exploration** (multi-agent communication costs), **Energy-Efficient Deployment**, **Parallelization & Distributed Computing Awareness**, **Learned Resource Allocation Policies**, and **Graceful Degradation / Fallback Mechanisms**.

## Key Quotes
> "Resource-Aware Optimization enables intelligent agents to dynamically monitor and manage computational, temporal, and financial resources during operation. This differs from simple planning, which primarily focuses on action sequencing." — Pattern overview

> "A key strategy in this category is the fallback mechanism, which acts as a safeguard when a preferred model is unavailable due to being overloaded or throttled. To ensure graceful degradation, the system automatically switches to a default or more affordable model, maintaining service continuity instead of failing completely." — Pattern overview

> "A Router Agent can direct queries based on simple metrics like query length... However, a more sophisticated Router Agent can utilize either LLM or ML models to analyze query nuances and complexity... a query requesting a factual recall is routed to a flash model, while a complex query requiring deep analysis is routed to a pro model." — Hands-On (ADK)

> "While not directly managing the budget, the Critique Agent contributes to indirect budget management by identifying suboptimal routing choices... which leads to poor results. This informs adjustments that improve resource allocation and cost savings." — Critique Agent

> "OpenRouter offers a unified interface to hundreds of AI models via a single API endpoint. It provides automated failover and cost-optimization." — Hands-On (OpenRouter)

## Connections
- [[ResourceAwareOptimization]] — the named pattern (#16) this chapter defines (primary concept).
- [[AgenticDesignPatterns]] — book hub; this is pattern #16.
- [[AntonioGulli]] — author.
- [[Routing]] / [[ModelRouter]] — the routing pattern and its production model-router instance; resource-aware routing dispatches by *cost/complexity*, not just intent.
- [[DynamicModelSelection]] — cheap-vs-frontier model switching by task difficulty + budget.
- [[CritiqueAgent]] — the feedback agent that refines routing logic and enables indirect budget management.
- [[GracefulDegradation]] — fallback to a default/affordable model on overload/throttle.
- [[SequentialModelFallback]] — OpenRouter's hierarchical model-list failover.
- [[CostAndLatency]] / [[Latency]] — the cost/latency/quality trade-off this pattern programmatically balances.
- [[InferenceOptimization]] / [[PromptCaching]] / [[KVCache]] / [[Quantization]] — adjacent efficiency levers the chapter's "spectrum" of techniques sits alongside.
- [[EnergyEfficiency]] — energy-efficient deployment on edge/limited-power devices.
- [[GoogleADK]] / [[gemini|Gemini]] (Flash vs Pro) / [[LiteLLM]] / [[CrewAI]] — frameworks/products.
- [[openai|OpenAI]] (gpt-4o / gpt-4o-mini / o4-mini) / [[OpenRouter]] — the other two hands-on stacks.
- [[Reflection]] / [[SelfCritique]] — the Critic Agent is the resource-routing application of the reflection/critique loop.
- [[ExceptionHandlingAndRecovery]] — Ch 12's fallback strategy generalizes here to model-level fallback.

## Contradictions
- None found. The chapter is consistent with the routing framing on [[Routing]]/[[ModelRouter]] (it specializes routing to a *cost/complexity* criterion) and with the fallback/graceful-degradation framing already on [[GracefulDegradation]] and [[ExceptionHandlingAndRecovery]].
