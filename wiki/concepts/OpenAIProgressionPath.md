---
title: "OpenAI Progression Path (Finetuning)"
type: concept
tags: [finetuning, model-selection, openai]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# OpenAI Progression Path (Finetuning)

One of two finetuning development paths [[ChipHuyen|Chip Huyen]] cites from [[openai|OpenAI]]'s finetuning best-practices documentation in [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]. The "progression" path starts cheap and scales up:

## The four steps

1. **Test your finetuning code** using the **cheapest and fastest model** to make sure the code works as expected. (Ch 7's footnote: *"In college, I made the painful mistake of letting my model train overnight, only to have it crash after eight hours because I tried to save the checkpoint in a nonexistent folder."*)
2. **Test your data** by finetuning a **middling model**. If the training loss doesn't go down with more data, something might be wrong.
3. **Run a few more experiments** with the **best model** to see how far you can push performance.
4. **Once you have good results**, do a **training run with all models** to **map out the price/performance frontier** and select the model that makes the most sense for your use case.

## Why this order

- **Cheapest first** catches code bugs (much cheaper than catching them in the expensive model).
- **Middling next** catches data bugs (the middle model is sensitive enough to reveal data problems without breaking the bank).
- **Best last** establishes the ceiling for what your data + recipe can achieve.
- **All-models final** lets you pick the model on the price/performance frontier — Pareto-optimal for your task.

## Counterpart: [[OpenAIDistillationPath|distillation path]]

The other OpenAI-recommended approach: start with the strongest possible model on a small dataset, use that finetuned teacher to generate more data, and train a cheaper student on the synthetic data. See [[OpenAIDistillationPath]].

## When to choose the progression path

- You have **enough labeled data** that you don't need synthetic generation.
- You want **cost transparency** across the model size spectrum.
- You're not sure yet which model class is right for the task.

## Connections

- [[OpenAIDistillationPath]] — the alternative path.
- [[FineTuning]] — parent operation.
- [[ModelSelection]] — the broader decision framework.
- [[openai|OpenAI]] — source of the recommendation.
- [[ai-engineering-ch07-finetuning]] — primary source.
