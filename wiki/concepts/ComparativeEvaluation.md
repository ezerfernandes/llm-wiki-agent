---
title: "Comparative Evaluation"
type: concept
tags: [evaluation, methodology, ranking]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Comparative Evaluation

**Comparative evaluation** evaluates models *"against each other and computes a ranking from comparison results"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]). The alternative to [[PointwiseEvaluation|pointwise evaluation]] (score each model independently then rank by score).

## Why comparative beats pointwise for subjective tasks

> "For responses whose quality is subjective, comparative evaluation is typically easier to do than pointwise evaluation. For example, it's easier to tell which song of the two songs is better than to give each song a concrete score."

## History in AI

- **2021** — first used by [[anthropic|Anthropic]] to rank different models.
- Now powers [[ChatbotArena|LMSYS Chatbot Arena]], the dominant crowdsourced LLM leaderboard.
- [[ChatGPT]] *"occasionally asks users to compare two outputs side by side"* — comparative data collected as part of the in-product feedback loop.

## The pipeline

1. For each request, select two (or more) models to respond.
2. An evaluator (human or AI) picks the **winner** (or "tie").
3. After many matches, a [[RatingAlgorithm|rating algorithm]] (e.g., [[EloRating|Elo]], [[BradleyTerry|Bradley-Terry]], [[TrueSkill]]) converts pairwise win rates into a global ranking.

## Ranking correctness criterion

Ch 3's definition: *"A ranking is correct if, for any model pair, the higher-ranked model is more likely to win in a match against the lower-ranked model."* Through this lens, **model ranking is a predictive problem** — historical match outcomes predict future ones.

## Comparative ≠ A/B testing

> "In A/B testing, a user sees the output from one candidate model at a time. In comparative evaluation, a user sees outputs from multiple models at the same time."

This distinction matters for product instrumentation: A/B test measures *behavioral lift* in isolation; comparative test measures *preference* given a side-by-side view.

## Three structural challenges (Ch 3)

1. **[[ScalabilityBottleneck|Scalability]]** — pairs grow quadratically; LMSYS evaluated 57 models with 244K comparisons = only ≈153 per pair across 1,596 pairs. The [[TransitivityAssumption|transitivity assumption]] helps but is contested for AI.
2. **Lack of standardization and quality control** — crowdsourced prompts are dominated by "hello"/"hi"; users can't fact-check; some users maliciously prefer toxic responses.
3. **Comparative-to-absolute gap** — *"Comparative evaluation tells us which model is better. It doesn't tell us how good a model is or whether this model is good enough for our use case."* A 51% win rate's downstream impact is unpredictable.

## What questions are unsuitable for preference voting

> "Imagine asking the model 'Is there a link between cell phone radiation and brain tumors?' and the model presents two options, 'Yes' and 'No', for you to choose from. Preference-based voting can lead to wrong signals."

Preference voting works only when **voters are knowledgeable on the subject**. Suitable for AI-as-intern tasks (speeding up things the user already knows how to do); unsuitable for AI-as-oracle tasks (asking AI things the user doesn't know).

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[PointwiseEvaluation]] — the orthogonal approach.
- [[RatingAlgorithm]] / [[EloRating]] / [[BradleyTerry]] / [[TrueSkill]] — algorithms that consume comparative signals.
- [[WinRate]] — the basic comparative signal.
- [[TransitivityAssumption]] — load-bearing simplification.
- [[ChatbotArena]] / [[MTBench]] / [[AlpacaEval]] — leaderboards built on this paradigm.
- [[ABTesting]] — what comparative evaluation is NOT.
- [[ComparisonData]] — the related preference-data form used in RLHF.
- [[LLMAsAJudge]] — when the comparing evaluator is an AI judge.
