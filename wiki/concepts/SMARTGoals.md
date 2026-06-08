---
title: "SMART Goals"
type: concept
tags: [goal-setting, agents, agentic-design-patterns, success-criteria, metrics]
sources: [agentic-design-patterns-ch11-goal-setting]
last_updated: 2026-06-07
---

# SMART Goals

**SMART** is a goal-quality mnemonic: a well-formed objective should be **S**pecific, **M**easurable, **A**chievable, **R**elevant, and **T**ime-bound. In [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[agentic-design-patterns-ch11-goal-setting|Ch 11]]) it is the prescribed standard for the goals an agent is given under the [[GoalSettingAndMonitoring|Goal Setting and Monitoring]] pattern — it is the chapter's sole cited reference (the [SMART criteria](https://en.wikipedia.org/wiki/SMART_criteria) Wikipedia article).

## Why it matters for agents
A goal that is vague or unmeasurable cannot be monitored: there is no way for the agent to render a success verdict against it. SMART forces the goal into a form that yields concrete **success criteria / metrics**, which are *"essential for effective monitoring"* and feed the agent's [[FeedbackLoop|feedback loop]]:
- **Specific** — an unambiguous objective the planner can decompose into sub-goals.
- **Measurable** — defines the metrics the [[Monitoring|monitor]] tracks (e.g. accuracy, completion time, false-positive/negative rate, "all checklist items pass").
- **Achievable** — bounded so the agent can plausibly reach it within its tools/capabilities.
- **Relevant** — tied to the actual user/business outcome (cf. north-star [[BusinessMetric|business metrics]]).
- **Time-bound** — a deadline; an otherwise-correct plan that finishes after the deadline is still a [[GoalFailure|goal failure]] (the often-overlooked **time constraint**).

## Connections
- [[GoalSettingAndMonitoring]] — the pattern that applies SMART to agent objectives.
- [[GoalOriented]] — the characteristic SMART goals direct.
- [[GoalFailure]] — violating a constraint (e.g. the time bound) is a goal failure even with valid steps.
- [[Planning]] / [[TaskDecomposition]] — a Specific goal is what gets decomposed into sub-goals.
- [[Monitoring]] — Measurable goals supply the metrics monitoring tracks.
- [[agentic-design-patterns-ch11-goal-setting]] — source.
