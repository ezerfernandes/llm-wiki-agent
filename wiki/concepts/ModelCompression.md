---
title: "Model Compression"
type: concept
tags: [inference, optimization, compression, quantization, distillation, pruning]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Model Compression

**Techniques that reduce a model's size** — and, as a consequence, often make it faster to serve. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Model compression involves techniques that reduce a model's size. Making a model smaller can also make it faster."*

The umbrella for several distinct techniques covered in *AI Engineering*.

## The four families

| Family | What it does | Status in 2024 |
|---|---|---|
| **[[Quantization|Quantization]]** | Reduce precision (FP32 → FP16 → INT8 → INT4 → ...) | **Dominant**, easy to use, works out of the box |
| **[[KnowledgeDistillation|Distillation]]** | Train a smaller model to mimic a larger one | Common; uses AI-generated data |
| **[[Pruning|Pruning]]** | Remove unimportant nodes or zero out parameters | Encouraging but less common (harder, smaller gains, hardware-dependent) |
| **[[LowRankFactorization|Low-rank factorization]]** | Approximate weight matrices as products of smaller matrices | Foundation of LoRA-style PEFT; less common as pure compression |

## Why quantization dominates

> *"Weight-only quantization is by far the most popular approach since it's easy to use, works out of the box for many models, and is extremely effective. Reducing a model's precision from 32 bits to 16 bits reduces its memory footprint by half. However, we're close to the limit of quantization — we can't go lower than 1 bit per value."*

The 1-bit floor is theoretically near at hand — see [[BitNetB158]] (Microsoft 2024) for the 1.58-bit work.

## Why distillation is common

A distilled model can be substantially smaller while matching behavior on a target task. [[DistilBERT]] is the canonical baseline (40% smaller, 60% faster, 97% capability). [[ai-engineering-ch08-dataset-engineering|Ch 8]] discusses distillation as an AI-data-synthesis use case in detail.

## Why pruning is rare

> *"In practice, as of this writing, pruning is less common. It's harder to do, as it requires an understanding of the original model's architecture, and the performance boost it can bring is often much less than that of other approaches. Pruning also results in sparse models, and not all hardware architectures are designed to take advantage of the resulting sparsity."*

Frankle & Carbin (2019, the *lottery-ticket-hypothesis* paper) showed pruning can remove > 90% of non-zero parameters of certain trained networks "without compromising accuracy." But the engineering effort vs. quantization is unfavorable.

## Model compression and the autoregressive bottleneck

Ch 9 frames compression as one of three model-level levers (the other two: overcoming the [[Decode|autoregressive decoding]] bottleneck, and optimizing the [[Attention|attention mechanism]]). Compression alone doesn't solve autoregression — but it **multiplies** the effects of every other optimization by reducing the bytes that must be moved per token.

## Connections

- [[Quantization]] — the dominant family.
- [[knowledgedistillation]] — the second most common family.
- [[Pruning]] — the third (less common) family.
- [[LowRankFactorization]] — fourth family; appears prominently in [[lora|LoRA]].
- [[Sparsity]] — the byproduct of pruning that hardware may or may not exploit.
- [[InferenceOptimization]] — broader discipline; model compression is one branch.
- [[ai-engineering-ch07-finetuning]] — depth on quantization.
- [[ai-engineering-ch08-dataset-engineering]] — depth on distillation.
- [[ai-engineering-ch09-inference-optimization]] — the umbrella source.
