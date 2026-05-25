---
title: "Opik"
type: entity
tags: [tool, prompt-monitoring, observability, open-source, llmops]
sources: [leh-ch02-tooling-and-installation, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Opik is an open-source LLM observability / prompt-monitoring tool published by [[CometML]]. It captures full multi-step LLM traces (prompt templates, model IDs, token counts, latencies, costs) and exposes them in a UI for debugging and evaluation.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) introduces Opik as the LLM Twin's prompt-monitoring tool because "you cannot use standard logging tools as prompts are complex and unstructured chains" — alternatives [[Langfuse]] / [[Galileo]] / [[LangSmith]] were considered. Ch. 11 ([[leh-ch11-mlops-and-llmops]]) instruments the production RAG flow with Opik's `@track` decorator on `rag()`, `call_llm_service()`, `ContextRetriever.search()`, and `SelfQuery.generate()`, logging model IDs, embedding model, temperature, prompt + completion token counts, and per-step latency via `opik_context.update_current_trace(...)`.

## Connections
- [[CometML]] — publisher of Opik; same vendor as the experiment tracker the book uses.
- [[Langfuse]] / [[LangSmith]] / [[Galileo]] — prompt-monitoring alternatives.
- [[PromptMonitoring]] — discipline Opik implements.
- [[LLMOps]] — practice it serves.
- [[FastAPI]] — the business microservice where `@track` is wired in.
