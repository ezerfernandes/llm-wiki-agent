---
title: "AgentOps Evaluation Harness"
type: concept
tags: [benchmark, agents, evaluation, harness]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# AgentOps Evaluation Harness

The **AgentOps evaluation harness** is one of three agent benchmarks Huyen names in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] — alongside the [[BerkeleyFunctionCallingLeaderboard]] and the [[TravelPlannerBenchmark]]. AgentOps positions itself as the **production-side** counterpart: a harness for **operating** agents in production with observability, tracing, and cost monitoring.

## What it covers

Where BFCL evaluates atomic function-calling accuracy and TravelPlanner evaluates end-to-end goal completion, AgentOps covers:

- **Tracing**: end-to-end agent run traces (Thought-Act-Observation steps, tool invocations, token counts).
- **Cost**: per-run dollar tracking across model + tool API calls.
- **Per-action analysis**: which steps are slow, which are expensive, which fail.
- **Production-style evaluation**: integration into CI/CD for agent regression detection.

## Position relative to LLM observability

AgentOps is the **agent-specific** layer in the broader LLM-observability ecosystem ([[Langfuse]], [[LangSmith]], [[Opik]], etc.). The distinguishing concern is that agents have **multi-step traces with tool-call branches**, not just single-prompt-single-response interactions.

## Connections

- [[BerkeleyFunctionCallingLeaderboard]] / [[TravelPlannerBenchmark]] — sibling agent benchmarks.
- [[Agent]] / [[Planning]] / [[ToolInventory]] — the system AgentOps operates on.
- [[AgentEfficiency]] — the metrics AgentOps surfaces (cost, latency).
- [[Langfuse]] / [[LangSmith]] / [[Opik]] — broader LLM observability peers.
- [[ai-engineering-ch06-rag-agents]] — primary source.
