---
title: "Agent Efficiency"
type: concept
tags: [agents, evaluation, cost, latency]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Agent Efficiency

**Agent efficiency** is the third top-level agent evaluation axis in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] (sister to [[PlanningFailure]] and [[ToolFailure]]). It captures the case where *"an agent might generate a valid plan using the right tools to accomplish a task, but it might be inefficient."*

## The three metrics

| Metric | Question |
|---|---|
| **Step count** | How many steps does the agent need, on average, to complete a task? |
| **Cost** | How much does the agent cost, on average, to complete a task? |
| **Per-action time** | How long does each action typically take? Are there especially slow or expensive actions? |

## Why all three matter together

- **Step count** drives [[CompoundErrorAccumulation|compound error accumulation]] — fewer steps = exponentially higher end-to-end accuracy at fixed per-step accuracy.
- **Cost** is the production constraint. Tasks with $10 of API cost per run can't be deployed at consumer scale.
- **Per-action time** drives user-perceived latency, especially for interactive agents.

## Calibration vs human baselines

> *"You can compare these metrics with your baseline, which can be another agent or a human operator. When comparing AI agents to human agents, keep in mind that humans and AI have very different modes of operations, so what's considered efficient for humans might be inefficient for AI, and vice versa."*

Concrete example from Ch 6: *"Visiting 100 web pages might be inefficient for a human agent who can visit only one page at a time, but trivial for an AI agent that can visit all the web pages at once."* This is why **per-step cost is a better metric than per-step time** for agents — parallelism can hide latency but not cost.

## Connections

- [[PlanningFailure]] / [[ToolFailure]] — sibling failure families.
- [[CompoundErrorAccumulation]] — the structural reason step-count compression matters.
- [[CostAndLatency]] — the broader evaluation dimension.
- [[Agent]] / [[Planning]] — parent abstractions.
- [[ControlFlow]] — parallel control flow is the main efficiency lever.
- [[ai-engineering-ch06-rag-agents]] — primary source.
