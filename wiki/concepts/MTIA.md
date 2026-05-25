---
title: "MTIA (Meta Training and Inference Accelerator)"
type: concept
tags: [hardware, meta, ai-accelerator, inference, training]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# MTIA — Meta Training and Inference Accelerator

**[[meta|Meta]]'s custom AI accelerator, designed for both training and inference workloads.** Mentioned in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]] as one of three inference-specialized accelerators alongside AWS Inferentia and Apple Neural Engine:

> *"Examples of such chips include the Apple Neural Engine, AWS Inferentia, and MTIA (Meta Training and Inference Accelerator)."*

## Design context

Although the name includes "training," MTIA in practice has been most prominent for **inference workloads** in Meta's serving fleet — particularly recommendation models and increasingly LLM-class inference. Per Ch 9's framing of inference-specialized chips:

- Optimized for lower precision (FP8 / INT8 / BF16).
- Memory bandwidth prioritized over capacity.
- Tighter integration with Meta's serving infrastructure.

## Strategic motivation

Meta deploys models at extreme scale (recommendations, ranking, LLM inference for [[Llama|Llama]]-class models in production). Custom silicon lets Meta:
- Avoid NVIDIA pricing and supply constraints.
- Tune the chip exactly for Meta's workloads.
- Co-design the chip with Meta's compiler stack.

## Wider trend

Ch 9 frames MTIA as part of a broader pattern: hyperscalers building inference-specialized chips because **inference accounts for up to 90% of ML costs for deployed AI systems** (Desislavov et al. 2023). Similar bets: AWS Inferentia, Google Edge TPU, Apple Neural Engine.

## Connections

- [[meta|Meta]] — the developer.
- [[AIAccelerator]] — umbrella concept.
- [[Inferentia]] / [[AppleNeuralEngine]] — sibling inference accelerators.
- [[GoogleTPU]] — broader-purpose Google equivalent.
- [[Llama]] — Meta's frontier LLM family that MTIA serves (alongside NVIDIA + AMD).
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
