---
title: "Quantization-Aware Training (QAT)"
type: concept
tags: [quantization, training, finetuning, mlsysbook]
sources: [ai-engineering-ch07-finetuning, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
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

## Mechanics ([[mlsysbook-ch10-model-compression|mlsysbook Ch 10]])

Ch 10 spells out the implementation. QAT inserts **fake-quantization nodes** that perform a quantize→clip→dequantize round-trip in the forward pass (simulating INT8 while staying in floating point), then uses the **[[StraightThroughEstimator|Straight-Through Estimator]]** in the backward pass — treating rounding's derivative as 1 within the valid range so gradients flow. The model thereby *learns* weight distributions that tolerate quantization. Two implementation details: scale factors must track evolving weight distributions via EMA (not stay static), and batch-norm running statistics must be computed on fake-quantized activations.

Concrete payoff: BERT-Base retains **99.1% of FP32 GLUE (QAT) vs 96.8% (PTQ)** — a 2.3-point gap that often decides whether a model meets a production threshold. Costs 20–50% extra training time. Decision rule: *start with PTQ, measure; invest in QAT only if PTQ falls short.* [[mlsysbook-ch10-model-compression]]

## Connections

- [[Quantization]] — parent family.
- [[PostTrainingQuantization]] — the cheaper, more-common alternative.
- [[StraightThroughEstimator]] — the gradient trick that makes QAT trainable (mlsysbook Ch 10).
- [[mlsysbook-ch10-model-compression]] — fake-quant nodes, STE, PTQ↔QAT decision rule.
- [[MixedPrecisionTraining]] — neighboring technique.
- [[LLMQAT]] — Liu et al. 2023, mentioned in Ch 7 (4-bit weights/activations + 16-bit embeddings).
- [[CharacterAI]] — INT8 native training case study.
- [[ai-engineering-ch07-finetuning]] — primary source.
