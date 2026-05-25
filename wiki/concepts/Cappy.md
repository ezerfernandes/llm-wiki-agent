---
title: "Cappy"
type: concept
tags: [reward-model, llm-as-judge, google]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Cappy

**Cappy** ([[google|Google]] 2023) is a specialized lightweight [[RewardModel|reward model]] developed as a specialized [[LLMAsAJudge|AI judge]]. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "Cappy is an example of a reward model developed by Google (2023). Given a pair of (prompt, response), Cappy produces a score between 0 and 1, indicating how correct the response is. Cappy is a lightweight scorer with **360 million parameters**, much smaller than general-purpose foundation models."

## Why small specialized judges win

Cappy is a concrete example of Ch 3's *"small, specialized judges can be more reliable than larger, general-purpose judges for specific judgments."* Three trade-offs that favor specialized over general:

1. **Latency**: 360M params runs orders of magnitude faster than a frontier LM judge.
2. **Cost**: API spend is dramatically lower.
3. **Reliability on its trained criterion**: a model trained specifically for correctness scoring can outperform a general-purpose model prompted for the same task.

## Position in the specialized-judge taxonomy

Ch 3's three specialized-judge types:
1. **[[RewardModel|Reward models]]** ← Cappy lives here.
2. [[ReferenceBasedJudge|Reference-based judges]] (BLEURT, Prometheus).
3. [[PreferenceModel|Preference models]] (PandaLM, JudgeLM).

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[RewardModel]] — parent category.
- [[ReferenceBasedJudge]] / [[PreferenceModel]] — sibling specialized-judge types.
- [[LLMAsAJudge]] — broader paradigm.
- [[google|Google]] — developer.
- [[ComparisonData]] / [[rlhf|RLHF]] — the broader context for reward models.
