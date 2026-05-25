---
title: "John Schulman"
type: entity
tags: [person, openai, researcher, rl, alignment]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# John Schulman

[[openai|OpenAI]] co-founder, prominent reinforcement-learning researcher. Original author of **[[PPO|Proximal Policy Optimization]]** (2017) — the RL algorithm at the heart of [[rlhf|RLHF]]. Cited in [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]] in two roles:

## 1. UC Berkeley talk (April 2023) on hallucinations

Schulman's framing of [[Hallucination|hallucination]] cause:

> "Models are trained to mimic responses written by labelers. If these responses use the knowledge that the labelers have but the model doesn't have, we're effectively teaching the model to hallucinate. ... Schulman also believes that **LLMs know if they know something**, which, in itself, is a big claim."

If LLMs do know what they know, hallucinations can be reduced by forcing models to answer only based on what they know. Schulman proposed two solutions:
1. **Verification.** For each response, ask the model to retrieve the sources it bases the response on.
2. **Better reward function.** Train the [[RewardModel|reward model]] to **punish making things up more heavily** — current RMs train on comparisons (A > B) without explanations of *why*; a more discriminating loss could push toward calibrated confidence.

## 2. The empirical contradiction

In the same talk, Schulman said OpenAI found that **RLHF helps reduce hallucinations** — but the InstructGPT paper (Ouyang et al. 2022) shows the opposite: **RLHF made hallucination worse** vs SFT alone, even though labelers preferred the RLHF model overall.

Ch 2 flags this as an open empirical question.

## Connections
- [[openai|OpenAI]] — employer (co-founder).
- [[PPO]] — Schulman's foundational 2017 paper.
- [[rlhf]] — the algorithm PPO powers.
- [[InternalKnowledgeMismatch]] — the hallucination hypothesis Schulman extended.
- [[LeoGao]] — proposed the first version of the same hypothesis.
- [[Hallucination]] — the phenomenon discussed.
- [[ai-engineering-ch02-foundation-models]] — primary source.
