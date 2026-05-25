---
title: "Quantization-Aware Training (QAT)"
type: concept
tags: [quantization, training, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Quantization-Aware Training (QAT)

A training mode that **simulates low-precision arithmetic during training** so the resulting model performs well when later quantized for inference. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Quantization-aware training (QAT) aims to create a model with high quality in low precision for inference. With QAT, the model simulates low-precision (e.g., 8-bit) behavior during training, which allows the model to learn to produce high-quality outputs in low precision."

## How it differs from PTQ

| Approach | Training cost | Inference quality at low precision |
|---|---|---|
| **[[PostTrainingQuantization\|PTQ]]** | Zero | OK at INT8; degrades at ≤INT4 |
| **QAT** | Equal or higher than full-precision training | Better at low precision |
| **Train directly in low precision** | Lower than QAT | Best at low precision (potentially) |

QAT itself **doesn't reduce training time** — its forward and backward passes still run in higher precision, just with "fake quantization" operators inserted to expose the model to low-precision behavior. *"QAT can even increase training time due to the extra work of simulating low-precision behavior."* (Ch 7)

## Training directly in low precision

Distinct from QAT: Ch 7 separately discusses **training directly in lower precision**. [[CharacterAI]] (2024) trained their models entirely in INT8 — this eliminates the train/serve precision mismatch *and* speeds up training. But:

> "Training in lower precision is harder to do, as backpropagation is more sensitive to lower precision." — Ch 7

The compounding-error footnote in Ch 7 is the deep reason — small rounding errors in weight updates accumulate across many training steps.

## When QAT is the right choice

- You need to deploy at INT4 or below.
- PTQ causes unacceptable quality regression.
- You have the training budget to do it.
- You're a model developer; QAT is mostly model-developer territory, not application-developer territory.

## Connections

- [[Quantization]] — parent family.
- [[PostTrainingQuantization]] — the cheaper, more-common alternative.
- [[MixedPrecisionTraining]] — neighboring technique.
- [[LLMQAT]] — Liu et al. 2023, mentioned in Ch 7 (4-bit weights/activations + 16-bit embeddings).
- [[CharacterAI]] — INT8 native training case study.
- [[ai-engineering-ch07-finetuning]] — primary source.
