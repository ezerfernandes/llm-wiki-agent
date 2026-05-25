---
title: "Tool Failure"
type: concept
tags: [agents, evaluation, failure-mode, tools]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Tool Failure

**Tool failure** is one of the three top-level agent failure families in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] (sister to [[PlanningFailure]] and [[AgentEfficiency]]). It is the failure mode where **the correct tool is called correctly, but the tool returns the wrong output**.

## The three sub-modes

| Sub-mode | Description |
|---|---|
| **Wrong output** | The tool just returns incorrect results — an image captioner returns a wrong description, an SQL generator returns an incorrect query. |
| **Translation error** | If the plan is high-level natural language and a translator converts to executable commands ([[PlanningGranularity|high-granularity planning]]), the translator can introduce errors. |
| **Missing tool** | The agent doesn't have access to the right tool for the task — *"the task involves retrieving the current stock prices from the internet, and the agent doesn't have access to the internet."* |

## How to evaluate

> *"Tool failures are tool-dependent. Each tool needs to be tested independently. Always print out each tool call and its output so that you can inspect and evaluate them."*

Tool failures cannot be debugged at the agent level — they need **per-tool benchmarks**. For translation modules specifically, build a translation benchmark separate from the agent benchmark.

## Detecting missing-tool failures

> *"Detecting missing tool failures requires an understanding of what tools should be used. If your agent frequently fails on a specific domain, this might be because it lacks tools for this domain. Work with human domain experts and observe what tools they would use."*

This is structurally different from planning or output failures — the *absence* of a capability is hard to detect from outputs alone; it shows up as systematically wrong answers in a domain.

## Connections

- [[PlanningFailure]] / [[AgentEfficiency]] — sibling failure families.
- [[ToolInventory]] — the inventory whose gaps cause missing-tool failures.
- [[PlanningGranularity]] — the translator step whose errors fall here.
- [[Agent]] — parent abstraction.
- [[ai-engineering-ch06-rag-agents]] — primary source.
