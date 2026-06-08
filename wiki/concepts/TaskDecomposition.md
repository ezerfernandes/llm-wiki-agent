---
title: "Task Decomposition"
type: concept
tags: [agents, agentic-design-patterns, planning, task-decomposition, sub-goals, reasoning]
sources: [agentic-design-patterns-ch06-planning, agentic-design-patterns-ch07-multi-agent]
last_updated: 2026-06-07
---

# Task Decomposition

**Task decomposition** is the breaking down of a high-level objective into a sequence of smaller, manageable, actionable steps or **sub-goals**. It is the core mechanism of the [[Planning]] pattern: in [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) — [[agentic-design-patterns-ch06-planning|Chapter 6]] — the Planning pattern works by "decomposing a high-level objective into a sequence of smaller, actionable steps or sub-goals," which is what lets an agentic system manage complex workflows, orchestrate tools, and handle dependencies in a logical order.

## How it works
Given an initial state and a goal state, the agent decomposes the goal into intermediate sub-goals whose ordered achievement transitions the system from initial to goal state. Each sub-goal is small enough to map to a concrete action (a tool call, a sub-task, an interaction with another system). The agent then executes the sub-tasks in a logical order, invoking necessary tools and managing dependencies between them.

Gulli's chapter examples:
- **Employee onboarding** decomposes into a directed sequence of sub-tasks: creating system accounts, assigning training modules, coordinating with different departments.
- **Research-report generation** decomposes into distinct phases: information gathering, data summarization, content structuring, and iterative refinement (see [[DeepResearch]]).
- **Customer support** decomposes into diagnosis → solution implementation → escalation.

The chapter equates plan generation with task decomposition; the existing [[Planning]] page records the same equivalence from [[ChipHuyen|Huyen]]'s *AI Engineering* Ch 6 ("a sequence of manageable actions, so this process is also called task decomposition").

## Why it matters in agentic systems
Without decomposition, an agent struggles with multifaceted requests that involve multiple steps and dependencies, failing to strategize and producing incomplete or incorrect results. Decomposition is what transforms a simple reactive agent into a strategic executor that can proactively work toward a complex objective and adapt as it goes. [[react|ReAct]]-style agents decompose implicitly step-by-step; explicit-planning agents decompose up front into a reviewable plan (as in [[DeepResearch|Deep Research]]'s editable research plan).

## Connections
- [[Planning]] — the pattern task decomposition implements.
- [[agentic-design-patterns-ch06-planning]] — source.
- [[DeepResearch]] — decomposes a query into a multi-point research plan / sub-questions.
- [[react|ReAct]] — step-by-step implicit decomposition via think-act-observe.
- [[PromptDecomposition]] — the prompt-engineering cousin: splitting a complex prompt into chained subtask prompts (distinct level of abstraction).
- [[GoalOriented|Goal-Oriented Behavior]] — decomposition serves goal achievement (goal → sub-goals → actions).
- [[ToolUse]] — sub-goals map onto tool calls.
- [[MultiAgentCollaboration]] / [[agentic-design-patterns-ch07-multi-agent]] — Ch 7's pattern is predicated on task decomposition: each sub-problem is assigned to the specialized agent best suited to it.
- [[AgenticDesignPatterns]] — the book hub.
