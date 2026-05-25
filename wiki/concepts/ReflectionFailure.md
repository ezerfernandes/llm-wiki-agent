---
title: "Reflection Failure"
type: concept
tags: [agents, evaluation, failure-mode, reflection]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Reflection Failure

**Reflection failure** is the [[PlanningFailure]] sub-mode in which **the agent is convinced it has accomplished the task when it hasn't**. It is the most subtle failure mode in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] because it can't be caught by output validation alone — the agent's own self-evaluation says everything is fine.

## The canonical example

> *"You ask the agent to assign 50 people to 30 hotel rooms. The agent might assign only 40 people and insist that the task has been accomplished."*

The agent has executed valid plan steps, called valid tools with valid parameters, and produced a plausible-looking output. Its reflection step incorrectly concludes that *"50 people are assigned"* when only 40 are.

## Why reflection is fallible

[[reflexion|Reflexion]] and [[react|ReAct]] both rely on the **same model** to plan, act, and reflect. If the model's reasoning failed on planning, the same reasoning will fail on reflection — *"asking the model that just made the mistake to evaluate whether it made a mistake"* is a known anti-pattern.

Mitigations:

- **Separate scorer model**: a different model evaluates the actor's output.
- **Deterministic checks**: count-based, type-based, format-based validators that don't rely on LM judgment.
- **External tools**: query the database, run the test suite, validate against a ground truth.

## Why this is the wiki's [[Hallucination|hallucination]] cousin

A reflection failure is a **hallucinated success signal** — the agent generates the claim *"task complete"* without evidence. This is structurally identical to hallucinating a fact: confident assertion without grounding. The mitigations are similarly grounded in *external verification*.

## Connections

- [[PlanningFailure]] — parent.
- [[GoalFailure]] — sibling — *not reaching* the goal, vs *believing* you reached it.
- [[reflexion|Reflexion]] / [[react|ReAct]] — patterns where reflection failure is most visible.
- [[Hallucination]] — the structural cousin.
- [[LLMAsAJudge]] / [[SelfCritique]] — the mechanisms that fail.
- [[SelfBiasJudge]] — the bias that drives reflection failure.
- [[ai-engineering-ch06-rag-agents]] — primary source.
