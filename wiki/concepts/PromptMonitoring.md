---
title: "Prompt Monitoring"
type: concept
tags: [llmops, observability, monitoring, llm-engineering]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch02-tooling-and-installation, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## Definition
**Prompt monitoring** is the LLMOps practice of logging the complete trace of every LLM interaction — user input, prompt template, input variables, retrieved context, generated answer, token counts, latency at each step — and surfacing those traces in a queryable, alertable observability layer. It is the LLM-specific analogue of structured logging for chained, unstructured, non-deterministic prompt pipelines.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] names prompt monitoring as a first-class requirement of the inference pipeline: every query, enriched prompt, and answer must flow through a monitoring system that can alert or trigger remediation. [[leh-ch02-tooling-and-installation]] justifies a dedicated tool ([[Opik]], with [[Langfuse]], LangSmith, Galileo as alternatives) because "standard logging tools cannot capture chained, unstructured prompt traces." [[leh-ch11-mlops-and-llmops]] gives the deepest treatment: prompt monitoring is the **distinctive LLMOps practice**, instrumented via Opik's `@track` decorator on the business-microservice functions (`rag()`, `call_llm_service()`, `ContextRetriever.search()`, `SelfQuery.generate()`). The chapter argues monitoring must always log three things on a trace — **model configuration** (model IDs, temperature, embedding model), **total tokens** (impacts serving cost), and **per-step duration** (locates bottlenecks) — and must live in the business microservice (not the LLM microservice) because only the business layer has the end-to-end view needed for a meaningful trace.

## Key details
- Traces, not events: a single user query becomes one trace with multiple linked steps (query rewrite, retrieval, prompt construction, LLM call, post-processing).
- Five LLM-specific latency metrics that all need recording: **TTFT** (time to first token), **TBT** (time between tokens), **TPS** (tokens per second), **TPOT** (time per output token), and **total latency**.
- Tool stack: [[Opik]] (Comet ML), [[Langfuse]], [[LangSmith]], [[WeightsAndBiases]], Galileo.
- Tracing granularity is a judgement call — too much produces noise; too little misses root causes.
- Instrumentation pattern: decorate the public business-layer functions, then attach metadata via `opik_context.update_current_trace(...)`.

## Connections
- [[LLMOps]] — prompt monitoring is the discipline's signature practice.
- [[Monitoring]] / [[ModelMonitoring]] — generic monitoring parents.
- [[Opik]] / [[Langfuse]] / [[LangSmith]] / [[WeightsAndBiases]] — vendor stack.
- [[Hallucination]] — a failure mode prompt monitoring helps catch.
- [[Guardrail]] — complementary safety layer; prompt monitoring observes, guardrails enforce.
- [[TTFT]] / [[TPOT]] — the per-token latency metrics monitored.
- [[rag]] — the multi-step pipeline traces typically instrument.
