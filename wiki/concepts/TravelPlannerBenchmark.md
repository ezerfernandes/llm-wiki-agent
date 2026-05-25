---
title: "TravelPlanner Benchmark"
type: concept
tags: [benchmark, agents, planning, evaluation]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# TravelPlanner Benchmark

**TravelPlanner** is the third agent benchmark Huyen names in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] (alongside [[BerkeleyFunctionCallingLeaderboard]] and [[AgentOpsEvalHarness]]). It evaluates an agent's ability to **plan a complex multi-day trip** under explicit constraints (budget, dates, preferences) — the canonical test for **end-to-end goal + constraint satisfaction**.

## Why it's structurally informative

Trip planning sits at the intersection of every agent failure family:

- **[[PlanningFailure|Planning]]**: must produce a valid plan over many steps, calling multiple tools.
- **[[ToolFailure|Tool]]**: requires correctly using search APIs, flight/hotel lookup, weather, distance.
- **[[GoalFailure|Goal]]**: must hit destination and stay under budget.
- **[[ReflectionFailure|Reflection]]**: must recognize when a draft itinerary blows the budget and revise.
- **[[AgentEfficiency|Efficiency]]**: cost per planned trip matters.

This is why Huyen calls it out — it's a microcosm of the full agent-failure taxonomy.

## The canonical Ch 6 illustration

Huyen uses *"two-week trip from San Francisco to Hanoi with a budget of $5,000"* as the [[GoalFailure|goal-failure]] running example — both *"plan a trip from San Francisco to Ho Chi Minh City"* (wrong destination) and *"plan a two-week trip from San Francisco to Hanoi that will be way over the budget"* (constraint violation) are concrete TravelPlanner failure cases.

## Connections

- [[BerkeleyFunctionCallingLeaderboard]] / [[AgentOpsEvalHarness]] — sibling agent benchmarks.
- [[Agent]] / [[Planning]] — what TravelPlanner evaluates.
- [[GoalFailure]] — the most-relevant failure family.
- [[ControlFlow]] — multi-day trips usually require if-statement and for-loop control flows.
- [[ai-engineering-ch06-rag-agents]] — primary source.
