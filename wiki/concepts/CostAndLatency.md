---
title: "Cost and Latency"
type: concept
tags: [evaluation, criteria, ai-engineering, latency, cost, pareto]
sources: [ai-engineering-ch04-evaluate-ai-systems, agentic-design-patterns-ch16-resource-aware, agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-07
---

# Cost and Latency

The **fourth bucket** of evaluation criteria in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]'s taxonomy. *"A model that generates high-quality outputs but is too slow and expensive to run will not be useful. When evaluating models, it's important to balance model quality, latency, and cost."*

## Pareto framing

Per Ch 4, cost-latency-quality optimization is a [[ParetoOptimization|Pareto optimization]] problem:

> "When optimizing for multiple objectives, it's important to be clear about what objectives you can and can't compromise on. For example, if latency is something you can't compromise on, you start with latency expectations for different models, filter out all the models that don't meet your latency requirements, and then pick the best among the rest."

## Latency metrics

- **[[TTFT|Time to first token]]** — perceived responsiveness.
- **[[TPOT|Time per output token]]** / **[[TimePerToken|Time per token]]** — generation speed (autoregressive: more tokens = more total latency).
- **[[TimeBetweenTokens|Time between tokens]]** — smoothness of streaming.
- **[[TimePerQuery|Time per query]]** — end-to-end.

> "It's important to differentiate between the must-have and the nice-to-have. If you ask users if they want lower latency, nobody will ever say no. But high latency is often an annoyance, not a deal breaker."

## Cost economics

Two regimes:
- **Model APIs**: charged per input/output token; cost per token is roughly fixed regardless of scale. Many applications minimize tokens via prompt and output engineering.
- **Self-hosting**: cost is mostly compute. Cost-per-token shrinks with utilization. *"If you've already invested in a cluster that can serve a maximum of 1 billion tokens a day, the compute cost remains the same whether you serve 1 million tokens or 1 billion tokens a day."*

The economics flip at some scale — *"companies need to reevaluate whether it makes more sense to use model APIs or to host their own models."*

## Why 7B and 65B models exist

GPUs ship with 16 / 24 / 48 / 80 GB of memory. Popular model sizes max out these configurations:

> "It's not a coincidence that many models today have 7 billion or 65 billion parameters."

## Example evaluation table (Ch 4, Table 4-3)

| Criterion | Metric | Benchmark | Hard requirement | Ideal |
|---|---|---|---|---|
| Cost | Cost per output token | (your math) | < $30/1M tokens | < $15/1M tokens |
| Scale | TPM (tokens per minute) | (your traffic) | > 1M TPM | > 1M TPM |
| Latency | TTFT (P90) | Internal prompt set | < 200ms | < 100ms |
| Latency | Time per query (P90) | Internal prompt set | < 1m | < 30s |
| Overall quality | Elo score | [[ChatbotArena]] | > 1200 | > 1250 |
| Code | [[PassAtK|pass@1]] | [[HumanEval]] | > 90% | > 95% |
| Factual consistency | Internal GPT metric | Internal hallucination set | > 0.8 | > 0.9 |

## Runtime resolution: Resource-Aware Optimization ([[agentic-design-patterns-ch16-resource-aware|Gulli Ch 16]])

Where Huyen frames cost/latency/quality as a model-*selection-time* [[ParetoOptimization|Pareto]] filter, [[agentic-design-patterns-ch16-resource-aware|*Agentic Design Patterns* Ch 16]] turns the same trade-off into a **per-query runtime decision**: the [[ResourceAwareOptimization|Resource-Aware Optimization]] pattern uses a [[ModelRouter|Router Agent]] to dispatch each request to a cheap or frontier model by complexity and budget ([[DynamicModelSelection|dynamic model selection]]), with a [[CritiqueAgent|Critique Agent]] tuning the routing for cost savings. Same three axes (quality, cost, latency), resolved continuously at inference rather than once at model-pick time.

## As production metrics: latency + token-usage monitoring ([[agentic-design-patterns-ch19-evaluation|Gulli Ch 19]])

[[EvaluationAndMonitoring|Ch 19 (Evaluation and Monitoring)]] treats cost and latency as **operational monitoring** targets for deployed agents, not just selection-time criteria. **Latency monitoring** measures per-request processing duration; *"simply printing latency data to the console is insufficient"* — persist it to time-series DBs ([[InfluxDB]], [[Prometheus]]), data warehouses ([[Snowflake]], [[GoogleBigQuery|BigQuery]]), or observability platforms ([[Datadog]], [[Splunk]], [[Grafana]]). **Token-usage tracking** (the chapter's `LLMInteractionMonitor` accumulating input/output token counts per interaction) is the cost-side metric — billing scales with tokens, so efficient token use cuts operational expense and flags prompt-engineering improvements. This is the runtime-telemetry sibling of Ch 4's selection-time table.

## Connections

- [[EvaluationAndMonitoring]] — Ch 19's runtime latency + token-usage monitoring (persisted to telemetry sinks).
- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[ResourceAwareOptimization]] / [[DynamicModelSelection]] / [[ModelRouter]] — Ch 16's runtime, per-query resolution of this trade-off.
- [[DomainSpecificCapability]] / [[GenerationCapability]] / [[InstructionFollowingCapability]] — sibling buckets.
- [[ParetoOptimization]] — methodology framing.
- [[TTFT]] / [[TPOT]] / [[TimePerToken]] / [[TimeBetweenTokens]] / [[TimePerQuery]] — specific metrics.
- [[UsefulnessThreshold]] — the threshold framing this feeds.
- [[InferenceService]] / [[ModelAPI]] — what gets benchmarked.
