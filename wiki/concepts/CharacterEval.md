---
title: "CharacterEval"
type: concept
tags: [benchmark, evaluation, roleplaying, reward-model]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# CharacterEval

A **[[Roleplaying|roleplaying]] benchmark** by Tu et al. (2024) discussed in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "CharacterEval used human annotators and trained a reward model to evaluate each roleplaying aspect on a five-point scale."

## Position

Sibling to [[RoleLLM]] (Wang et al. 2023). The two differ in methodology:

| | RoleLLM | CharacterEval |
|---|---|---|
| Scoring | Similarity scores + AI judge | Trained reward model |
| Annotators | AI | Human |
| Scale | (ranking) | 5-point |

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Roleplaying]] — what it measures.
- [[RoleLLM]] — sibling benchmark.
- [[RewardModel]] — methodology used.
- [[InstructionFollowingCapability]] — parent capability.
