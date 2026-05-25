---
title: "Reflexion"
type: concept
tags: [concept, agents, reflection]
sources: [2604.27707-agentic-memory-is-a-memo, ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Reflexion

Stores verbal self-critiques in an episodic buffer (Shinn et al., 2023). Calls itself 'verbal reinforcement learning' but the model's weights remain unchanged.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

[[ChipHuyen|Huyen]] develops Reflexion (Shinn et al. 2023) as the **two-module refinement** over plain [[react|ReAct]]-style reflection:

> *"Reflection is separated into two modules: an evaluator that evaluates the outcome and a self-reflection module that analyzes what went wrong. ... The authors used the term 'trajectory' to refer to a plan. At each step, after evaluation and self-reflection, the agent proposes a new trajectory."*

The structural innovation: **separating evaluation from analysis**. ReAct interleaves Thought-Act-Observation but doesn't separate *"this step failed"* from *"this step failed because X."* Reflexion makes that split explicit:

| Module | Role |
|---|---|
| **Evaluator** | Decides whether the outcome is acceptable. |
| **Self-reflection** | Decides *why* it failed and how to revise the trajectory. |

**Worked example from Ch 6**: For a coding task where the evaluator finds that the generated code fails 1/3 of test cases, *"the agent then reflects the reason it failed is because it didn't take into account arrays where all numbers are negative. The actor then generates new code, taking into account all-negative arrays."*

**Position relative to [[ActorCriticAgent|actor-critic]]** (Ch 6 footnote): the evaluator + self-reflection split *"reminds [Huyen] of the actor-critic (AC) agent method (Konda and Tsitsiklis, 1999) in reinforcement learning."* Reflexion is the LLM-prompt-level realization of the actor-critic decomposition.
