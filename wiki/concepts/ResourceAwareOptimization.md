---
title: "Resource-Aware Optimization"
type: concept
tags: [agentic-design-patterns, agents, resource-aware-optimization, cost-optimization, routing, model-selection, latency, fallback]
sources: [agentic-design-patterns-ch16-resource-aware]
last_updated: 2026-06-07
---

# Resource-Aware Optimization

**Resource-Aware Optimization** is the agentic design pattern in which an agent **dynamically monitors and manages its computational, temporal, and financial resources** during operation — making execution decisions to either hit a specified **resource budget** or **optimize efficiency**, rather than just sequencing actions. It is **pattern #16** of the 21 in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[agentic-design-patterns-ch16-resource-aware|Ch 16]]).

> *"Resource-Aware Optimization enables intelligent agents to dynamically monitor and manage computational, temporal, and financial resources during operation. This differs from simple planning, which primarily focuses on action sequencing."* — Ch 16

The pattern names a fundamental **quality-vs-resources trade-off**: always picking the best model/tool for every task is inefficient, but always picking the cheapest sacrifices quality. Resource-aware optimization is the machinery that arbitrates this trade-off at runtime — e.g. choosing an accurate-but-expensive model vs a faster, lower-cost one, or allocating extra compute for a refined answer vs returning a quicker, less-detailed one.

## How it works

The standardized solution is a **multi-agent** pipeline:

1. **[[ModelRouter|Router Agent]]** — classifies the **complexity** of an incoming request, then forwards it to the most suitable model/tool: a fast, inexpensive model for simple queries; a powerful one for complex reasoning. This is the [[Routing|routing]] pattern specialized to a **cost/complexity** criterion (rather than pure intent). The router can use a simple metric (query length: short → cheap, long → capable) or, more sophisticatedly, an LLM or ML model that analyzes query nuance. The model choice is also gated by **available budget and time**.
2. **[[CritiqueAgent|Critic / Critique Agent]]** — evaluates responses (accuracy, relevance) for self-correction and performance monitoring, and **feeds back to refine the routing logic over time**. By flagging suboptimal routing (a simple query sent to an expensive model, or a complex one sent to a cheap model that gives poor results) it performs **indirect budget management** that improves resource allocation and cost savings, and can signal [[ReinforcementLearning|RL]]/fine-tuning.
3. **Fallback** — when the preferred model is unavailable (overloaded, throttled), the system automatically switches to a default or more affordable model, ensuring [[GracefulDegradation|graceful degradation]] and service continuity instead of total failure.

The router's effectiveness can be improved by **prompt tuning** (crafting the routing prompt) and **fine-tuning the router LLM** on a dataset of queries paired with their optimal model choices.

## Worked example: hierarchical travel planner

A travel-planner agent uses a powerful LLM ([[gemini|Gemini]] Pro) for the **high-level planner** that breaks a complex request into a multi-step itinerary and makes logical decisions, then runs the simple, repetitive sub-tasks (flight lookups, hotel availability, restaurant reviews) on a faster, cheaper model (Gemini Flash). The expensive intelligence is spent only where deep context understanding is required.

## The broader spectrum of techniques

Ch 16's "Beyond Dynamic Model Switching" survey lists resource-aware levers beyond model routing:

- **[[DynamicModelSelection|Dynamic Model Switching]]** — strategic selection of LLMs by task intricacy and available compute (the core technique above).
- **Adaptive [[ToolUse|Tool Use]] & Selection** — choosing the most efficient tool per sub-task, weighing API costs, latency, and execution time.
- **Contextual Pruning & Summarization** — minimizing prompt token count (and thus inference cost) by summarizing and retaining only the most relevant interaction history. (Cf. [[SummarizationMemory]], [[PromptCaching]].)
- **Proactive Resource Prediction** — forecasting future workloads to allocate resources ahead of bottlenecks.
- **Cost-Sensitive Exploration** — in [[MultiAgentCollaboration|multi-agent systems]], extending optimization to **communication costs** between agents.
- **Energy-Efficient Deployment** — minimizing the energy footprint for resource-constrained / edge environments (cf. [[EnergyEfficiency]]).
- **Parallelization & Distributed Computing Awareness** — distributing workloads across machines for throughput (cf. [[Parallelization]]).
- **Learned Resource Allocation Policies** — agents adapt their allocation strategy over time from feedback/metrics.
- **Graceful Degradation & Fallback Mechanisms** — continuing at reduced capacity under severe constraints.

## Why it matters in agentic systems

LLM-based applications can be expensive and slow; without a dynamic management strategy, a system cannot adapt to varying task complexity or stay within budgetary and performance constraints. This pattern is what lets an agent **programmatically balance response quality against operational cost** — essential under strict API/compute budgets, in latency-sensitive applications, on battery-limited edge hardware, and in complex multi-step workflows where tasks have varying resource needs.

## Frameworks & products (Ch 16 hands-on)

- **[[GoogleADK|Google ADK]]** — multi-agent architecture with LLM-driven routing; uses Gemini Pro/Flash directly or integrates other models via [[LiteLLM]], plus built-in evaluation for refinement. The hands-on defines two identical-setup agents (`GeminiProAgent` on `gemini-2.5-pro`, `GeminiFlashAgent` on `gemini-2.5-flash`) and a `QueryRouterAgent(BaseAgent)` that routes by `query_length`.
- **[[gemini|Gemini]] Flash vs Pro** — the canonical cheap-vs-frontier model tier split.
- **[[openai|OpenAI]]** — the OpenAI example classifies prompts into `simple` (`gpt-4o-mini`), `reasoning` (`o4-mini`), or `internet_search` (`gpt-4o` + Google Custom Search).
- **[[OpenRouter]]** — unified API over hundreds of models with automated failover and cost-optimization; offers **Automated Model Selection** (`openrouter/auto`) and **[[SequentialModelFallback|Sequential Model Fallback]]** (a hierarchical `models` list). See its rankings leaderboard.
- **[[CrewAI]]** — named among the multi-agent frameworks supporting this orchestration.

## Relation to adjacent patterns

- **[[Routing]]** (Ch 2) — resource-aware optimization *is* routing, with the dispatch criterion being **cost/complexity/budget** rather than intent; the Router Agent is the same machinery.
- **[[ModelRouter]]** — the production-architecture model router whose cost-routing benefit (cheap model for easy queries) this pattern operationalizes end-to-end with a feedback loop.
- **[[Reflection]] / [[SelfCritique]]** (Ch 4) — the Critique Agent is the reflection/critique loop applied to *routing quality* and resource allocation.
- **[[ExceptionHandlingAndRecovery]] / [[GracefulDegradation]]** (Ch 12) — the fallback mechanism is model-level fallback + graceful degradation.
- **[[CostAndLatency]]** — the evaluation-criteria framing of the quality/cost/latency [[ParetoOptimization|Pareto]] trade-off this pattern resolves at runtime.
- **[[Prioritization]]** (Ch 20) — the sibling resource-constrained pattern: prioritization decides *which* task/goal to work on first (urgency, importance, dependencies), whereas resource-aware optimization decides *how cheaply* to execute each step. Both arbitrate under "limited resources" using cost/benefit criteria.

## Connections

- [[agentic-design-patterns-ch16-resource-aware]] — primary source (Gulli Ch 16).
- [[AgenticDesignPatterns]] — book hub; pattern #16.
- [[AntonioGulli]] — author.
- [[Routing]] / [[ModelRouter]] / [[QueryRouting]] — the routing pattern and its instances.
- [[DynamicModelSelection]] — cheap-vs-frontier switching by difficulty + budget.
- [[CritiqueAgent]] — the feedback agent refining routing logic.
- [[SequentialModelFallback]] — OpenRouter's hierarchical failover.
- [[GracefulDegradation]] / [[ExceptionHandlingAndRecovery]] — fallback on overload/throttle.
- [[CostAndLatency]] / [[Latency]] / [[InferenceOptimization]] — the efficiency axes optimized.
- [[PromptCaching]] / [[KVCache]] / [[Quantization]] / [[SummarizationMemory]] — adjacent cost-reduction levers.
- [[EnergyEfficiency]] — energy-efficient edge deployment.
- [[GoogleADK]] / [[gemini|Gemini]] / [[LiteLLM]] / [[CrewAI]] / [[openai|OpenAI]] / [[OpenRouter]] — frameworks/products in the hands-on examples.
- [[Reflection]] / [[SelfCritique]] — the critique loop the Critic Agent applies.
- [[MultiAgentCollaboration]] / [[Parallelization]] — multi-agent and distributed resource awareness.
