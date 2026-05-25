---
title: "Prompt Loss Weight"
type: concept
tags: [training, finetuning, sft, hyperparameters]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Prompt Loss Weight

A [[SupervisedFinetuning|SFT]] hyperparameter that controls **how much the prompt tokens contribute to the training loss compared to the response tokens**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "For instruction finetuning, each example consists of a prompt and a response, both of which can contribute to the model's loss during training. During inference, however, prompts are usually provided by users, and the model only needs to generate responses. Therefore, response tokens should contribute more to the model's loss during training than prompt tokens."

## The dial

| Value | Effect |
|---|---|
| **100%** | Prompts contribute equally to responses; model learns prompts and responses symmetrically. |
| **10%** (Ch 7 default) | Model learns mostly from responses, a little from prompt structure. |
| **0%** | Model learns only from responses; prompt tokens are masked from the loss. |

## Why the 10% default

The reasoning at inference time:
- The user provides the prompt; the model receives it as context.
- The model only **generates the response**.
- So the response is what the model needs to produce well; the prompt is just input.

A 100% weight would over-emphasize prompt prediction, wasting capacity on something the model never needs to generate. A 0% weight loses some useful signal about prompt structure (e.g., when prompts in the training distribution share a format the model benefits from internalizing).

10% is the empirical middle ground that has become the default in most SFT frameworks.

## When to deviate

- **Higher weight (~25–50%)** when the prompt format is itself part of what you're teaching (e.g., teaching the model how to interpret a new tool description format).
- **Lower weight (0%)** when you want the model to act purely as a response generator and avoid any prompt-token influence.

## Connections

- [[SupervisedFinetuning]] — where this hyperparameter applies.
- [[InstructionTuning]] — the parent operation.
- [[BatchSize]] / [[LearningRate]] / [[NumberOfEpochs]] — sibling hyperparameters.
- [[ai-engineering-ch07-finetuning]] — primary source.
