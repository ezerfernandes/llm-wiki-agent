---
title: "Goal Failure"
type: concept
tags: [agents, evaluation, failure-mode]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Goal Failure

**Goal failure** is one of the [[PlanningFailure]] sub-modes named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]: **the agent fails to achieve the goal**, even though its individual plan steps may all be valid.

## Two sub-cases

1. **Wrong task**: the agent's plan doesn't solve the task at all. *"Imagine you ask the model to plan a two-week trip from San Francisco to Hanoi with a budget of $5,000. The agent might plan a trip from San Francisco to Ho Chi Minh City"* — wrong destination.
2. **Solves the task but violates constraints**: the agent does the task but ignores constraints. *"...or plan a two-week trip from San Francisco to Hanoi that will be way over the budget."*

## The overlooked time constraint

> *"A common constraint that is often overlooked by agent evaluation is time. In many cases, the time an agent takes matters less, because you can assign a task to an agent and only need to check in when it's done. However, in many cases, the agent becomes less useful with time. For example, if you ask an agent to prepare a grant proposal and the agent finishes it after the grant deadline, the agent isn't very helpful."*

A correct plan that completes after the deadline is still a goal failure — time is a goal constraint even when it's not stated explicitly.

## Why this category matters

Most agent benchmarks measure **per-step validity** but not **goal achievement**. An agent can have 100% valid-step-rate and still fail every task if it consistently misreads the goal. Goal-failure evaluation requires task-level rubrics — was the goal achieved? Were the constraints respected? — that go beyond mechanical step counting.

## Connections

- [[PlanningFailure]] — parent.
- [[ReflectionFailure]] — sibling — *believing* the goal was reached when it wasn't.
- [[AgentEfficiency]] — time-as-goal-constraint overlap.
- [[TravelPlannerBenchmark]] — benchmark that explicitly tests goal + constraint satisfaction.
- [[Agent]] — parent abstraction.
- [[ai-engineering-ch06-rag-agents]] — primary source.
