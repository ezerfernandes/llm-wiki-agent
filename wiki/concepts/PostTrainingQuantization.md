---
title: "Post-Training Quantization (PTQ)"
type: concept
tags: [quantization, inference, optimization, mlsysbook]
sources: [ai-engineering-ch07-finetuning, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Post-Training Quantization (PTQ)

[[Quantization|Quantizing]] a model **after** it's been fully trained, with no further training required. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Quantization can happen during training or post-training. Post-training quantization (PTQ) means quantizing a model after it's been fully trained. PTQ is by far the most common. It's also more relevant to AI application developers who don't usually train models."

## The basic recipe

1. Load a pre-trained model in high precision (FP32 or FP16).
2. Determine quantization parameters (scale, zero-point) per tensor or per channel — typically from a small **calibration dataset** of representative inputs.
3. Convert weights to the target format (INT8, INT4, NF4, FP8, FP4, etc.).
4. Optionally convert activations using calibration statistics.
5. Save the quantized model; serve it.

## Why PTQ dominates

- **No retraining required** — no labeled data, no compute beyond a small calibration pass.
- **Supported out-of-the-box** by [[PyTorch]] / [[TensorFlow]] / [[HuggingFace]] transformers with a few lines of code.
- **Works on edge devices** that don't support training operations.

> "Some edge devices only support quantized inference. Therefore, frameworks for on-device inference, such as TensorFlow Lite and PyTorch Mobile, also offer PTQ." — Ch 7

## Common PTQ algorithms (named in Ch 1 / Ch 7 / Ch 9 of the book)

- **GPTQ** (Frantar et al. 2023) — per-layer weight error minimization, second-order info.
- **AWQ** — Activation-aware Weight Quantization.
- **SmoothQuant** — Move quantization difficulty from activations to weights.
- **GGUF** — File format / quantization scheme for llama.cpp.
- **LLM.int8()** ([[Dettmers2022LLMint8|Dettmers et al., 2022]]) — INT8 quantization with outlier handling.

## Limits

- Quality degrades as you push below 8 bits — [[QuantizationAwareTraining|QAT]] often outperforms PTQ at 4 bits and below.
- **Activation quantization** (vs weight-only) is harder; activations vary across inputs, so per-tensor static quantization can miss outliers.
- The KV cache (transformer attention) is its own quantization frontier — see Ch 9.

## Calibration & granularity ([[mlsysbook-ch10-model-compression|mlsysbook Ch 10]])

Ch 10's core PTQ mechanism is **uniform/affine quantization** with a [[Calibration|calibration]] step that selects the clipping range $[\alpha,\beta]$ from a small representative dataset: $s=(\beta-\alpha)/(2^b-1)$, $z=\text{round}(-\alpha/s)$. Calibration methods — **Max** (outlier-prone), **Entropy** (TensorRT default, minimizes KL), **Percentile** (99% clip). Granularity ladder: layerwise → groupwise → **channelwise (standard)** → sub-channelwise. Symmetric vs asymmetric ranges handle zero-centered vs skewed distributions. PTQ's hard limit: no mechanism to *recover* lost accuracy — if it drops below threshold (common for transformers where attention amplifies numerical differences), the only recourse is less-aggressive precision, which is why it motivates [[QuantizationAwareTraining|QAT]]. [[ActivationAwareWeightQuantization|AWQ]] is the activation-aware PTQ variant for LLM INT4. [[mlsysbook-ch10-model-compression]]

## Connections

- [[Quantization]] — parent family.
- [[QuantizationAwareTraining]] — the alternative (train-time).
- [[Calibration]] / [[ActivationAwareWeightQuantization]] — PTQ sub-mechanisms (mlsysbook Ch 10).
- [[mlsysbook-ch10-model-compression]] — affine math, calibration methods, granularity.
- [[NumericalRepresentation]] — what PTQ converts between.
- [[InferenceOptimization]] — the discipline PTQ serves.
- [[Dettmers2022LLMint8]] — foundational LLM-quantization work.
- [[HuggingFace]] / [[PyTorch]] / [[TensorFlow]] — frameworks with PTQ built-in.
- [[ai-engineering-ch07-finetuning]] — primary source.
