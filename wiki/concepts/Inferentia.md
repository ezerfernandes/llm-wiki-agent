---
title: "AWS Inferentia"
type: concept
tags: [hardware, aws, ai-accelerator, inference]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# AWS Inferentia

**Amazon Web Services's custom inference-specialized AI accelerator.** Mentioned in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]] as one of three specialized inference chips alongside Apple Neural Engine and [[MTIA|Meta MTIA]]:

> *"Examples of such chips include the Apple Neural Engine, AWS Inferentia, and MTIA (Meta Training and Inference Accelerator)."*

## Inference-specific design choices

Per Ch 9's general framing of inference-specialized chips:

> *"Chips designed for inference are often optimized for lower precision and faster memory access, rather than large memory capacity."*

For Inferentia, this translates to:
- Heavy use of low-precision math (INT8, BF16) — inference can tolerate quantization that training can't.
- Bandwidth optimization over peak-FLOPS — autoregressive decode is [[MemoryBandwidthBound|memory-bandwidth-bound]].
- Tighter integration with AWS's networking stack for serving.

## Where Inferentia fits in AWS

Inferentia is one of two AWS AI chip families:
- **Inferentia** — inference-only.
- **Trainium** — training and inference (a successor designed for both).

Both run via the **AWS Neuron SDK**, which provides a compiler and runtime targeting the chips from PyTorch / TensorFlow / JAX.

## Why dedicated inference chips emerged

Desislavov et al. (2023) — cited in Ch 9 — found inference **can exceed the cost of training in commonly used systems, and accounts for up to 90% of ML costs for deployed AI systems.** The economic case for purpose-built inference silicon is what gave us Inferentia, MTIA, Apple Neural Engine, and Google Edge TPU.

## Connections

- [[AIAccelerator]] — umbrella concept.
- [[MTIA]] / [[AppleNeuralEngine]] — sibling inference-specialized chips.
- [[Amazon|AWS]] — the owner.
- [[Quantization]] — heavily exploited by Inferentia for FP/INT throughput.
- [[MemoryBandwidthBound]] — the regime Inferentia is tuned for.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
