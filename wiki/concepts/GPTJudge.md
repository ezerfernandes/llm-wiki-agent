---
title: "GPT-judge"
type: concept
tags: [evaluation, llm-as-judge, factuality, fine-tuning]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# GPT-judge

The **fine-tuned [[LLMAsAJudge|AI judge]] paired with [[TruthfulQA]]** (Lin et al. 2022). Predicts whether a model response is truthful with **90-96% accuracy** vs human labels — one of the strongest empirical points for AI-judge credibility in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]].

## What it is

A GPT model fine-tuned on TruthfulQA's reference data to score binary truthfulness on (question, response) pairs. The human expert baseline on TruthfulQA is 94% — GPT-judge approaches that.

## Position

A **specialized AI judge**, not a general-purpose one. Sibling to other specialized judges Ch 3 named:
- [[Cappy]] (Google, 360M reward model)
- [[BLEURT]] (reference-based similarity scorer)
- [[Prometheus2]] (1-5 reference-based judge)
- [[PandaLM]] / [[JudgeLM]] (preference models)

GPT-judge is uniquely paired with [[TruthfulQA]] — you don't use it for general-purpose evaluation.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[TruthfulQA]] — paired benchmark.
- [[LLMAsAJudge]] — broader paradigm.
- [[ReferenceBasedJudge]] — closest sibling category.
- [[FactualConsistency]] / [[GlobalFactualConsistency]] — what it scores.
