---
title: "Planning Failure"
type: concept
tags: [agents, evaluation, failure-mode]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Planning Failure

**Planning failure** is one of the three top-level agent-failure families in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] (sister to [[ToolFailure]] and [[AgentEfficiency|efficiency failure]]). It is the failure mode where **the plan itself is wrong** — even before tool execution.

## The taxonomy

Huyen names four sub-modes:

| Sub-mode | Description |
|---|---|
| **Invalid tool** | Plan calls `bing_search`, but `bing_search` isn't in the agent's tool inventory. |
| **Valid tool, invalid parameters** | Plan calls `lbs_to_kg` with two parameters when it requires one. |
| **Valid tool, incorrect parameter values** | Plan calls `lbs_to_kg(lbs=100)` when the user said 120. |
| **[[GoalFailure\|Goal failure]]** | Plan solves a *different* task than the goal, or solves the goal but violates constraints. |

A subtle fifth sub-mode is **[[ReflectionFailure|reflection failure]]**: the agent insists it has accomplished a task when it has not (the *"assign 50 people to 30 hotel rooms, agent assigns only 40 and insists it's done"* example).

## Evaluation methodology

Huyen recommends a structured planning evaluation dataset of `(task, tool_inventory)` tuples. For each task, generate K plans and compute:

1. Out of all generated plans, how many are valid?
2. For a given task, how many plans must the agent generate, on average, to get a valid plan?
3. Out of all tool calls, how many are valid?
4. How often are invalid tools called?
5. How often are valid tools called with invalid parameters?
6. How often are valid tools called with incorrect parameter values?

## Diagnostic patterns

- **Per-task analysis**: what task types does the agent fail on most? Hypothesize why.
- **Per-tool analysis**: which tools cause most planning failures? Some tools are structurally harder to use — better prompting, more examples, or finetuning can help; if all fail, swap the tool.

## The implicit time constraint

> *"A common constraint that is often overlooked by agent evaluation is time. ... If you ask an agent to prepare a grant proposal and the agent finishes it after the grant deadline, the agent isn't very helpful."*

Time is a [[GoalFailure|goal-failure]] dimension that's easy to miss — a plan that succeeds in 10 hours when a 1-hour plan was needed is still a planning failure.

## Connections

- [[ToolFailure]] / [[AgentEfficiency]] — sibling failure families.
- [[GoalFailure]] / [[ReflectionFailure]] — sub-modes.
- [[FunctionCalling]] — the API surface where the invalid-tool / invalid-parameter classes manifest.
- [[Hallucination]] — the root cause of most planning failures.
- [[BerkeleyFunctionCallingLeaderboard]] / [[AgentOpsEvalHarness]] / [[TravelPlannerBenchmark]] — agent benchmarks that measure planning failures.
- [[Agent]] / [[Planning]] — parent abstractions.
- [[ai-engineering-ch06-rag-agents]] — primary source.
