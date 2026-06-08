---
title: "Chapter 20 — Prioritization (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, prioritization, task-ranking, urgency, importance, dependencies, dynamic-reprioritization, scheduling]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 20 of [[AntonioGulli|Antonio Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] presents the **Prioritization** pattern (Agentic Design Patterns, PDF pp 325–334): the mechanism by which an agent assesses and ranks competing tasks, goals, and actions by their significance, urgency, dependencies, and established criteria so it concentrates limited resources on the most critical work. It frames prioritization as four elements — criteria definition, task evaluation, scheduling/selection logic, and dynamic re-prioritization — operating across three levels (high-level goal selection, sub-task ordering, immediate action selection). The hands-on example builds a Project Manager agent in [[LangChain]] (with [[openai|OpenAI]] `gpt-4o-mini` via a [[react|ReAct]] agent + `AgentExecutor`) that creates, prioritizes (P0/P1/P2), and assigns tasks, defaulting sensibly when priority or assignee is unspecified.

## Key Claims
- Without a defined process for choosing the next action, agents in complex, dynamic environments suffer reduced efficiency, operational delays, or outright failure to hit key objectives; prioritization resolves this by ranking work on significance, urgency, dependencies, and criteria.
- Agent prioritization rests on four fundamental elements: (1) **criteria definition** (the rules/metrics for evaluation), (2) **task evaluation** (scoring each task against the criteria), (3) **scheduling / selection logic** (the algorithm picking the optimal next action or task sequence, possibly via a queue or planning component), and (4) **dynamic re-prioritization** (modifying priorities as circumstances change, e.g. a new critical event or approaching deadline).
- Common criteria are **urgency** (time-sensitivity), **importance** (impact on the primary objective), **dependencies** (whether a task is a prerequisite for others), **resource availability**, **cost/benefit analysis** (effort vs expected outcome), and **user preferences**.
- Task evaluation methods span a spectrum from **simple rules** to **complex scoring** to **reasoning by the LLM itself**.
- Prioritization operates at three levels: **high-level goal prioritization** (picking an overarching objective), **sub-task prioritization** (ordering steps within a plan), and **action selection** (choosing the next immediate action from available options).
- Dynamic re-prioritization is the distinctive agentic capability: it grants the agent autonomy to adapt focus in real time, which is "what separates a true agentic system from a simple automated script."
- Effective prioritization mirrors human team organization, where managers rank tasks by weighing input from all members; it makes agent behavior more intelligent, efficient, robust, and goal-aligned.

## Key Quotes
> "The prioritization pattern addresses this issue by enabling agents to assess and rank tasks, objectives, or actions based on their significance, urgency, dependencies, and established criteria." — chapter opening (PDF p 325)

> "Finally, dynamic re-prioritization allows the agent to modify priorities as circumstances change, such as the emergence of a new critical event or an approaching deadline, ensuring agent adaptability and responsiveness." — the four fundamental elements (PDF p 325)

> "This ability to self-manage its workflow is what separates a true agentic system from a simple automated script." — Conclusions (PDF p 334)

> "Use the Prioritization pattern when an Agentic system must autonomously manage multiple, often conflicting, tasks or goals under resource constraints to operate effectively in a dynamic environment." — Rule of thumb (PDF p 333)

## Connections
- [[Prioritization]] — the canonical concept page for this pattern (created from this chapter).
- [[AgenticDesignPatterns]] — the book hub; this is pattern 20 of 21.
- [[AgenticDesignPattern]] — the meta-concept this chapter instantiates.
- [[Planning]] / [[TaskDecomposition]] — prioritization orders the sub-tasks a planner produces; "scheduling/selection logic" may use "an advanced planning component."
- [[GoalSettingAndMonitoring]] — supplies the goals/sub-goals to be ranked; monitoring's replan arm triggers dynamic re-prioritization.
- [[ResourceAwareOptimization]] — prioritization under "limited resources"; both weigh cost/benefit, but RAO optimizes resource consumption while prioritization orders work.
- [[LangChain]] / [[openai|OpenAI]] / [[react|ReAct]] / [[Pydantic]] / [[MemoryManagement]] / [[ToolUse]] — the hands-on Project Manager agent stack.
- [[Scheduler]] / [[ProcessScheduling]] — the OS scheduling sense (distinct referent; cross-referenced, not merged).

## Contradictions
- None found. Complements [[GoalSettingAndMonitoring]] and [[ResourceAwareOptimization]] rather than conflicting; the OS-level [[Scheduler]]/[[ProcessScheduling]] pages share vocabulary ("scheduling," "queue," "priority") but address a different (kernel/process) domain.
