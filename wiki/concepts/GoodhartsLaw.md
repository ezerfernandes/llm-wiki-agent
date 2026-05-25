---
title: "Goodhart's Law"
type: concept
tags: [evaluation, measurement, benchmarks, alignment, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# Goodhart's Law

> **"When a measure becomes a target, it ceases to be a good measure."**
> — Marilyn Strathern, *"'Improving ratings': audit in the British University system,"* European Review 5.3 (1997): 305–321.

The classic warning from economics and education research, applied in the LLM era to **benchmark optimization**: once a metric is treated as the target of optimization, the metric stops being a useful signal of the underlying behavior it was supposed to measure.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] closes its *Evaluating Generative Models* section by quoting Goodhart's Law and giving a deliberately reductio-ad-absurdum example:

> *"In the context of LLMs, when using a specific benchmark, we tend to optimize for that benchmark regardless of the consequences. For instance, if we focus purely on optimizing for generating grammatically correct sentences, the model could learn to only output one sentence: 'This is a sentence.' It is grammatically correct but tells you nothing about its language understanding capabilities. Thus, the model may excel at a specific benchmark but potentially at the expense of other useful capabilities."* — Ch 12

This is the chapter's framing for **why no single benchmark suffices**, why public-leaderboard overfit is a real risk, and why human evaluation remains the gold standard.

## Connections to the broader wiki

This is the same concept other sources in the wiki invoke under different names:
- [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]'s **[[BehaviorBasedFailure|behavior-based failure]] vs [[InformationBasedFailure|information-based failure]]** taxonomy implicitly assumes Goodhart's Law: optimizing for the wrong failure mode leads to a model that scores well on the metric you trained on while still failing on the metric you care about.
- [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]'s warning about [[DataLeakage|data leakage]] from public benchmarks into training corpora is one mechanism through which Goodhart's Law degrades public benchmarks.
- The **alignment-tax** family ([[AlignmentTax]]) and the [[Sycophancy|sycophancy]] failure mode are Goodhart-on-RLHF: the reward model becomes the target, and the policy learns to game the reward model rather than to be genuinely helpful.

## Practical advice from Ch 12

Three practitioner moves the chapter explicitly recommends:

1. **Use multiple benchmarks** (which is why leaderboards aggregate several — [[OpenLLMLeaderboard]] uses MMLU + HellaSwag + TruthfulQA + GSM8k + …).
2. **Add domain-specific evaluation** matched to the intended use case (*"for coding, HumanEval would be more logical than GSM8k"*).
3. **Keep human evaluation in the loop** — *"you are the best evaluator. Human evaluation remains the gold standard."*

## Connections

- [[Benchmark]] / [[OpenLLMLeaderboard]] / [[MMLU]] / [[HellaSwag]] / [[TruthfulQA]] / [[GSM8K]] / [[HumanEval]] — the metrics Goodhart's Law warns against over-optimizing.
- [[LLMAsAJudge]] / [[ChatbotArena]] — eval methods designed in part to be Goodhart-robust by being adaptive.
- [[AlignmentTax]] / [[Sycophancy]] / [[DegenerateFeedbackLoop]] — failure modes that are special cases of Goodhart's Law.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
