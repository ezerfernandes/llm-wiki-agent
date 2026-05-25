---
title: "Request Trace"
type: concept
tags: [observability, monitoring, debugging, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Request Trace

**A reconstructed end-to-end timeline of a single request's path through the pipeline — every component it hit, every tool it called, every prompt it sent, every output produced, and how long each step took.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]: *"A trace is the detailed recording of a request's execution path through various system components and services."*

(Disambiguation: this is the *observability* notion of trace, distinct from the [[Trace|linear-algebra trace]] of a matrix.)

## What a trace contains in an AI application

> *"In an AI application, tracing reveals the entire process from when a user sends a query to when the final response is returned, including the actions the system takes, the documents retrieved, and the final prompt sent to the model. It should also show how much time each step takes and its associated cost, if measurable."* — Ch 10

Concretely:

- The raw query.
- The router decision (which model / tool / intent class).
- The retrieval results (documents pulled).
- The final assembled prompt.
- The model output (and any intermediate outputs in a chain).
- Tool calls and their outputs.
- Latency per step; cost per step (where measurable).

## Logs vs traces

The Ch 10 distinction:

| Logs | Traces |
|---|---|
| Append-only records of discrete events | Reconstructed timelines linking related events |
| *"Disjointed events"* | *"Linked … to form a complete timeline"* |
| Answer "what happened at time T?" | Answer "what happened to *this* request?" |

A trace is built **from** logs (or from purpose-built spans), tagged with request IDs and parent/child links.

## The debugging payoff

> *"Ideally, you should be able to trace each query's transformation step-by-step through the system. If a query fails, you should be able to pinpoint the exact step where it went wrong: whether it was incorrectly processed, the retrieved context was irrelevant, or the model generated a wrong response."* — Ch 10

Without traces, multi-component AI applications are effectively unobservable — a bad response could come from any step, and you have no way to localize the fault.

## Tools

Ch 10 shows a [[LangSmith|LangSmith]] trace visualization in Figure 10-11. The space is mature: [[LangSmith]], LangChain tracing, OpenTelemetry-backed agent tracers, vendor-specific dashboards on [[ModelGateway|gateway]] products.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[observability]] / [[Monitoring]] — parent disciplines.
- [[Logging]] / [[StructuredLogging]] — the substrate traces are built from.
- [[LangSmith]] — Ch 10's named visualization tool.
- [[EvaluationTrace]] — a sibling tracing concept for evaluation runs.
- [[MTTD]] / [[MTTR]] — the metrics traces lower.
- [[Trace]] — disambiguation: linear-algebra trace, unrelated.
