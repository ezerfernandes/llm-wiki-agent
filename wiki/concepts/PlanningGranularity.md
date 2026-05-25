---
title: "Planning Granularity"
type: concept
tags: [agents, planning]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Planning Granularity

**Planning granularity** is the level of detail at which an agent's plan is expressed. Per [[ChipHuyen|Huyen]] in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]:

> *"A plan is a roadmap outlining the steps needed to accomplish a task. A roadmap can be of different levels of granularity. To plan for a year, a quarter-by-quarter plan is higher-level than a month-by-month plan, which is, in turn, higher-level than a week-to-week plan."*

## The trade-off

| Granularity | Generation | Execution |
|---|---|---|
| **High-level** (natural language) | Easier | Harder — needs translator to executable commands |
| **Detailed** (exact function calls) | Harder | Easier — direct invocation |

## Hierarchical planning as the resolution

> *"An approach to circumvent this trade-off is to plan hierarchically. First, use a planner to generate a high-level plan, such as a quarter-to-quarter plan. Then, for each quarter, use the same or a different planner to generate a month-to-month plan."*

This is the same pattern HTN (Hierarchical Task Network) planning uses in classical AI — high-level subgoals expanded into concrete actions.

## Natural-language plans vs exact-function-call plans

Huyen argues for natural-language plans with a downstream **translator** ("program generator" in [[Chameleon|Chameleon]] terminology):

> *"Using more natural language helps your plan generator become robust to changes in tool APIs. If your model was trained mostly on natural language, it'll likely be better at understanding and generating plans in natural language and less likely to hallucinate."*

Trade-off: you need a translator step, but translation is *"a much simpler task than planning and can be done by weaker models with a lower risk of hallucination."*

## Operational implications

- **Tool inventory changes break exact-function-call plans.** Rename `get_time()` → `get_current_time()` and every prompt + every example must be updated; finetuned plan-generators must be retrained.
- **Natural-language plans are portable across tool inventories.** The same plan can target different tool APIs by swapping the translator.

## Connections

- [[Planning]] — the parent concept.
- [[Agent]] — the system that plans.
- [[Chameleon]] — uses the program-generator translator approach.
- [[ControlFlow]] — the structure within which plan steps execute.
- [[FunctionCalling]] — the low-granularity API surface.
- [[ai-engineering-ch06-rag-agents]] — primary source.
