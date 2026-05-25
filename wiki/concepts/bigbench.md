---
title: "BIG-bench"
type: concept
tags: [benchmark, evaluation, google]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# BIG-bench

[[google|Google]]'s **Beyond the Imitation Game** benchmark (Srivastava et al. 2022). A collection of **214 sub-benchmarks** spanning a wide range of language-model capabilities. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Google's BIG-bench (2022) alone has 214 benchmarks."

## Notable sub-benchmark

[[TwentyQuestionsTask|`twenty_questions`]] — a task-based-evaluation example used by Ch 4 to illustrate multi-turn task evaluation: one model picks a concept (apple, car, computer), another asks yes/no questions and tries to guess it; scored on success + turns required.

## BBH

**[[BigBenchHard|BBH (BIG-bench Hard)]]** is the *reasoning-focused subset* (Suzgun et al. 2022); used on HuggingFace's [[OpenLLMLeaderboard|Open LLM Leaderboard]] June 2024 refresh.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[google|Google]] — author.
- [[BigBenchHard]] — reasoning subset.
- [[TwentyQuestionsTask]] — task-based-eval example.
- [[PublicBenchmark]] — the largest single public benchmark collection (by count).
