---
title: "Chain of Debates (CoD)"
type: concept
tags: [reasoning, multi-agent, agentic-design-patterns, debate, microsoft]
sources: [agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
---

# Chain of Debates (CoD)

**Chain of Debates (CoD)** is a formal multi-agent reasoning framework — proposed by [[microsoft|Microsoft]] — in which **multiple, diverse models collaborate and argue to solve a problem**, moving beyond a single AI's [[ChainOfThought|chain of thought]]. It is documented in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] as one of the [[ReasoningTechniques|Reasoning Techniques]] ([[agentic-design-patterns-ch17-reasoning|Ch 17]]).

## How it works

CoD operates like an **AI council meeting**: different models present initial ideas, critique each other's reasoning, and exchange counterarguments. Functioning as an **AI version of peer review**, it creates a transparent and trustworthy record of the reasoning process.

## Why it matters in agentic systems

The primary goals are to **enhance accuracy, reduce bias, and improve the overall quality** of the final answer by leveraging collective intelligence. CoD represents a **shift from a solitary agent providing an answer to a collaborative team of agents** working together to find a more robust and validated solution — the chapter's signal that reasoning is moving from single-model deliberation to [[multiagentsystems|multi-agent]] societies.

It is the *linear* form of multi-agent debate; [[GraphOfDebates|Graph of Debates (GoD)]] generalizes the same idea into a non-linear network of supporting/refuting arguments.

## Connections
- [[agentic-design-patterns-ch17-reasoning]] — source (Ch 17).
- [[ReasoningTechniques]] — the chapter's parent pattern.
- [[microsoft|Microsoft]] — the framework's originator.
- [[GraphOfDebates]] — the graph generalization of debate-based reasoning.
- [[ChainOfThought]] — the single-model technique CoD moves beyond.
- [[multiagentsystems]] / [[MultiAgentCollaboration]] — the multi-agent paradigm CoD instantiates.
- [[Reflection]] / [[SelfBiasJudge]] — separate-critic debate as a bias-mitigation mechanism (cf. the Producer-Critic model).
- [[MultiAgentSystemSearch]] — debate ("Debate" agent block) is one of the building blocks MASS optimizes over.
- [[LLMAsAJudge]] — peer-review-style cross-model critique.
