---
title: "Berkeley Function Calling Leaderboard"
type: concept
tags: [benchmark, agents, function-calling, evaluation]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Berkeley Function Calling Leaderboard

The **Berkeley Function Calling Leaderboard (BFCL)** is the canonical benchmark for evaluating LLMs on **[[FunctionCalling|function-calling]] tasks**, from the [[UCBerkeley|UC Berkeley]] group behind [[Gorilla]]. Cited in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as one of three named agent benchmarks (alongside [[AgentOpsEvalHarness]] and [[TravelPlannerBenchmark]]).

## What it measures

BFCL evaluates [[PlanningFailure|planning failures]] at the function-calling layer:

- Does the model select the **right tool**?
- Does it pass the **right parameter names**?
- Does it pass the **right parameter values** (the hardest sub-task)?
- Does it handle **multi-turn** function-calling correctly?

## Position relative to other agent benchmarks

| Benchmark | Focus |
|---|---|
| **BFCL** | Tool selection + parameter correctness — the per-call atom |
| [[AgentOpsEvalHarness]] | End-to-end agent execution harness |
| [[TravelPlannerBenchmark]] | Goal-driven multi-step planning + constraint satisfaction |

BFCL is the most-cited tool-use benchmark in the function-calling-API era because it isolates the **single most failure-prone component** of agent execution — the tool call itself.

## Connections

- [[FunctionCalling]] — what BFCL evaluates.
- [[PlanningFailure]] — the failure family BFCL most directly measures.
- [[Gorilla]] / [[UCBerkeley]] — institutional origin.
- [[AgentOpsEvalHarness]] / [[TravelPlannerBenchmark]] — sibling agent benchmarks.
- [[Agent]] — the application surface.
- [[ai-engineering-ch06-rag-agents]] — primary source.
