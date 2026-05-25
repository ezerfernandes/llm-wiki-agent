---
title: "Monitoring"
type: concept
tags: [mlops, operations]
sources: [madewithml-monitoring, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Monitoring

Tracking system and model health signals in production. Encompasses [[ModelMonitoring]], infrastructure metrics, and [[observability|observability]] practices to catch failures before users do.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

[[ai-engineering-ch10-architecture-feedback|Ch 10]] uses **monitoring** narrowly — *"the act of tracking a system's information"* — and reserves **[[observability]]** for *"the whole process of instrumenting, tracking, and debugging the system."* Monitoring is the verb; observability is the discipline.

### What to monitor in an AI app

Ch 10 sorts metrics into six groups (most are application-specific; design around your failure modes, not standard checklists):

- **Format failures** — easiest to detect. Track invalid-JSON rate, schema-mismatch rate, repairable-vs-unrepairable split.
- **Open-ended quality** — factual consistency, conciseness, creativity, positivity — often via [[LLMAsAJudge|AI judges]].
- **Safety** — toxicity, PII leakage, [[FalseRefusalRate|false refusal rate]], guardrail-trigger rate, abnormal-query detection ([[UsagePatternMonitoring]]).
- **Conversational signals** — early-termination rate, average turns/conversation, tokens-per-input/output, output-token-distribution drift.
- **Latency** — [[TTFT]], [[TPOT]], total latency. Per-user.
- **Cost** — token volume, TPS (tokens-per-second), RPS (requests-per-second), cache hit rate.

### Per-component metrics

> *"Each component in an application pipeline has its own metrics. For example, in a RAG application, the retrieval quality is often evaluated using context relevance and context precision. A vector database can be evaluated by how much storage it needs to index the data and how long it takes to query the data."* — Ch 10

### North-star correlation

> *"Given that you'll likely have multiple metrics, it's useful to measure how these metrics correlate to each other and, especially, to your business north star metrics."* — Ch 10

Strong correlation with [[BusinessMetric|north-star metrics]] (DAU, session duration, [[StickinessMetric|stickiness]]) reveals which monitoring metrics to optimize; absence of correlation reveals which to *stop* optimizing.

### Spot checks vs exhaustive checks

> *"Spot checks involve sampling a subset of data to quickly identify issues, while exhaustive checks evaluate every request for a comprehensive performance view."* — Ch 10

Combination is the typical strategy.

### Slicing by axis

Metrics must be breakable down by: users, releases, prompt/chain versions, prompt/chain types, time. Aggregate metrics hide regressions confined to specific cohorts.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — Ch 10 source.
- [[observability]] — the broader discipline this is part of.
- [[ModelMonitoring]] / [[PromptMonitoring]] — sub-disciplines.
- [[MTTD]] / [[MTTR]] / [[ChangeFailureRate]] — DevOps observability-quality metrics.
- [[RequestTrace]] / [[Logging]] — the diagnostic substrate.
- [[DriftDetection]] / [[SilentModelUpdate]] — AI-app-specific failure modes.
- [[BusinessMetric]] / [[StickinessMetric]] / [[EngagementMetric]] — north-star metrics to correlate against.
