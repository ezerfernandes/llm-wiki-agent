---
title: "OpenAI Distillation Path (Finetuning)"
type: concept
tags: [finetuning, distillation, model-selection, openai]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# OpenAI Distillation Path (Finetuning)

One of two finetuning development paths [[ChipHuyen|Chip Huyen]] cites from [[openai|OpenAI]]'s finetuning best-practices documentation in [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]. The "distillation" path starts with a strong teacher on little data, then trains a cheaper student on synthetic data:

## The three steps

1. **Start with a small dataset and the strongest model you can afford.** Train the best possible model with this small dataset. Because the base model is already strong, it requires less data to achieve good performance.
2. **Use this finetuned model to generate more training data.**
3. **Use this new dataset to train a cheaper model.**

## Why this order

- **Strong + small data**: the teacher's pre-existing capability lets it learn the task from few examples — you don't have to pay for huge data acquisition up front.
- **Teacher generates data**: the teacher's outputs become labeled training data for the student. This is **[[knowledgedistillation|knowledge distillation]]** in the data-augmentation sense.
- **Student is cheaper**: the goal is a model at deployable size/cost while inheriting the teacher's quality.

## Counterpart: [[OpenAIProgressionPath|progression path]]

The other OpenAI-recommended approach: start cheap, scale up to map the price/performance frontier. See [[OpenAIProgressionPath]].

## When to choose the distillation path

- You have **little labeled data** but compute to run a strong teacher.
- You want a **specific deployable model size** (the student) and need to bootstrap data for it.
- You're confident a strong teacher's outputs are reliable enough to train against.

## When this path is risky

- The teacher hallucinates → the student learns to hallucinate.
- Synthetic data is less diverse than real data → student overfits.
- Without filtering, low-quality teacher outputs degrade the student.

The fix: pair distillation with **quality filtering** (e.g., teacher-student agreement, [[GeneratorValidatorConsistency|generator-validator consistency]] as in [[2507.03152-medval|MedVAL]]).

## Connections

- [[OpenAIProgressionPath]] — the alternative path.
- [[knowledgedistillation]] — the broader technique.
- [[FineTuning]] — parent operation.
- [[SyntheticData]] — the intermediate artifact.
- [[openai|OpenAI]] — source of the recommendation.
- [[ai-engineering-ch07-finetuning]] — primary source.
