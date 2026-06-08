---
title: "Prioritization (Agentic Pattern)"
type: concept
tags: [agents, agentic-design-patterns, prioritization, task-ranking, urgency, importance, dependencies, dynamic-reprioritization, scheduling, action-selection]
sources: [agentic-design-patterns-ch20-prioritization]
last_updated: 2026-06-07
---

# Prioritization (Agentic Pattern)

**Prioritization** is the agentic design pattern by which an agent **assesses and ranks** competing tasks, objectives, and actions — by their significance, urgency, dependencies, and established criteria — so it concentrates limited resources on the most critical work. It is the 20th of the 21 patterns in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] (see [[agentic-design-patterns-ch20-prioritization|Ch 20]]). In complex, dynamic environments an agent faces "numerous potential actions, conflicting goals, and limited resources"; without a defined process for choosing what to do next it suffers reduced efficiency, operational delays, or outright failure to meet objectives. This pattern is the decision discipline that prevents that.

> This is the **agentic decision-making** sense of "prioritization / scheduling / queue / priority." For the operating-system sense — kernel run-queues, process priority, preemption — see [[ProcessScheduling]], [[Scheduler]], and [[InterruptPriority]]. Same vocabulary, different referent: those pages rank *processes for a CPU*; this page ranks *tasks/goals/actions for an LLM agent* using semantic criteria (importance, dependencies, cost/benefit) often evaluated by the model's own reasoning.

## Why it matters
Effective prioritization is what lets an agent "act purposefully and logically" amid an overwhelming number of choices. By focusing on the highest-priority items the agent's behavior becomes more **intelligent, efficient, robust, and aligned with its strategic goals**, and it can dynamically adapt to changing circumstances and manage constrained resources. The pattern mirrors human team organization, where a manager ranks tasks by weighing input from all members. Crucially, the *dynamic* form of prioritization — adjusting focus in real time — is "what separates a true agentic system from a simple automated script."

## The four fundamental elements
Agent prioritization typically decomposes into four parts:

1. **Criteria definition** — establishing the rules or metrics for evaluating a task.
2. **Task evaluation** — assessing each candidate task against those criteria.
3. **Scheduling / selection logic** — the algorithm that, given the evaluations, selects the optimal next action or task sequence, "potentially utilizing a queue or an advanced planning component."
4. **Dynamic re-prioritization** — modifying priorities as circumstances change (a new critical event, an approaching deadline), ensuring adaptability and responsiveness.

## Criteria (what to weigh)
The criteria definition step typically draws on:

- **Urgency** — the time-sensitivity of the task.
- **Importance** — its impact on the primary objective.
- **Dependencies** — whether the task is a prerequisite for others (dependency-aware ordering).
- **Resource availability** — readiness of the necessary tools or information.
- **Cost/benefit analysis** — effort versus expected outcome.
- **User preferences** — for personalized agents.

This urgency-vs-importance weighting echoes classic **Eisenhower-style** prioritization (sorting work by the two axes of urgency and importance), now applied autonomously by the agent rather than a human planner.

## Task evaluation (how to score)
Evaluation methods span a spectrum:

- **Simple rules** — deterministic if/then logic.
- **Complex scoring** — numeric ranking against weighted criteria.
- **Reasoning by the LLM** — the model itself judges relative priority from natural-language context.

## Three levels of prioritization
Prioritization can occur at distinct granularities:

- **High-level goal prioritization** — selecting an overarching objective.
- **Sub-task prioritization** — ordering the steps within a [[Planning|plan]].
- **Action selection** — choosing the next immediate action from available options.

## Dynamic re-prioritization
The hallmark agentic capability: rather than committing to a fixed ordering, the agent continuously re-ranks work as conditions change — a new high-severity alert arrives, a deadline approaches, a resource frees up. This grants the autonomy to adapt focus in real time and is the feature most emphasized in the chapter's Key Takeaways and Conclusions.

## How it works — the hands-on Project Manager agent
The chapter's example builds a Project Manager agent in [[LangChain]] driven by [[openai|OpenAI]] `gpt-4o-mini`:

- A `SuperSimpleTaskManager` keeps tasks in an in-memory dict (O(1) lookup) of [[Pydantic|Pydantic]] `Task` models, each with `id`, `description`, an optional `priority` (**P0** highest / **P1** medium / **P2** lowest), and an optional `assigned_to`.
- Four [[ToolUse|tools]] (Pydantic-validated args) wrap it: `create_new_task`, `assign_priority_to_task`, `assign_task_to_worker`, and `list_all_tasks`.
- A [[react|ReAct]] agent (`create_react_agent`) runs inside a [[LangChain|LangChain]] `AgentExecutor` with [[MemoryManagement|ConversationBufferMemory]]. A `ChatPromptTemplate` instructs it to: create the task first (to get an ID), map urgency cues like "urgent"/"ASAP"/"critical" → **P0**, assign a named worker if mentioned, and **default sensibly** (P1 priority, "Worker A") when priority or assignee is unspecified — then list the final state.
- The async `run_simulation` exercises two scenarios: an urgent feature request with a designated worker, and a less-urgent content review with minimal detail (testing the default-assignment path).

```
Prompt ─▶ Agent ─▶ rank tasks against criteria ─▶ Priority 1, 2, 3 … n
   ▲          │
   User ◀── Output
```

## Practical applications
- **Automated customer support** — urgent requests (system outage) over routine ones (password reset); preferential treatment for high-value customers.
- **Cloud computing** — allocate to critical apps at peak demand; relegate batch jobs to off-peak to cut cost.
- **Autonomous driving** — braking to avoid a collision takes precedence over lane discipline or fuel efficiency.
- **Financial trading** — rank trades by market conditions, risk tolerance, profit margins, real-time news.
- **Project management** — rank board tasks by deadlines, dependencies, team availability, strategic importance.
- **Cybersecurity** — rank alerts by threat severity, potential impact, asset criticality.
- **Personal assistants** — organize calendar events, reminders, notifications by user-defined importance, deadlines, and context.

## Rule of thumb
Use Prioritization when an agentic system must autonomously manage multiple, often conflicting, tasks or goals under resource constraints to operate effectively in a dynamic environment.

## Connections
- [[AgenticDesignPatterns]] — the book hub; [[agentic-design-patterns-ch20-prioritization|Ch 20]] is the source. Pattern 20 of 21.
- [[AgenticDesignPattern]] — the meta-concept this pattern instantiates.
- [[Planning]] / [[TaskDecomposition]] — prioritization orders the sub-tasks a planner generates; the "selection logic" may delegate to a planning component.
- [[GoalSettingAndMonitoring]] — supplies the goals and sub-goals to be ranked; the monitoring loop's replan/escalate arm triggers dynamic re-prioritization.
- [[ResourceAwareOptimization]] — sibling pattern under "limited resources"; RAO optimizes *how much* resource each step consumes, while prioritization decides *which* work to do first (both use cost/benefit criteria).
- [[ToolUse]] / [[react|ReAct]] / [[Pydantic]] / [[MemoryManagement]] — the building blocks of the hands-on agent.
- [[LangChain]] / [[openai|OpenAI]] — the framework and model used in the example. (Compare sibling-pattern chapters that also demonstrate [[GoogleADK|Google ADK]] and [[crewai|CrewAI]].)
- [[ProcessScheduling]] / [[Scheduler]] / [[InterruptPriority]] — the OS/hardware scheduling sense of priority; cross-referenced as a distinct domain.
