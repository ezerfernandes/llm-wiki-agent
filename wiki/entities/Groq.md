---
title: "Groq"
type: entity
tags: [company, hardware, ai-accelerator, inference]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Groq

**Mountain View-based AI inference hardware company; designer of the Language Processing Unit (LPU).** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"The success of NVIDIA GPUs has inspired many accelerators designed to speed up AI workloads, including ... Groq's Language Processing Unit (LPU) ..."*

## The LPU thesis

Groq's distinguishing claim: an **inference-only**, **deterministic-latency** chip optimized specifically for sequential autoregressive token generation. Designed in deliberate contrast to GPUs:

- **No HBM** — uses on-chip SRAM as primary working memory.
- **No dynamic scheduling** — execution is fully deterministic, making latency highly predictable.
- **Optimized for [[Decode|decoding]]** — the [[MemoryBandwidthBound|memory-bandwidth-bound]] phase that dominates LLM serving cost.

Groq's public benchmarks claim much higher tokens/s for inference than equivalent-class GPU setups (e.g. 500+ tokens/s on Llama-class models). The trade-off is **less flexibility** and tighter memory budgets (because no HBM).

## Where Groq appears in Ch 9

A single mention in the accelerator zoo — no detailed treatment. But the LPU is a useful illustration of the *inference-specialized accelerator* category Ch 9 highlights, alongside [[Inferentia|AWS Inferentia]], [[MTIA|Meta MTIA]], and [[AppleNeuralEngine|Apple Neural Engine]].

## Connections

- [[AIAccelerator]] — umbrella category.
- [[Inferentia]] / [[MTIA]] / [[AppleNeuralEngine]] — sibling inference accelerators.
- [[NVIDIA]] / [[AMD]] / [[Cerebras]] / [[Graphcore]] — competing AI hardware vendors.
- [[Decode]] / [[MemoryBandwidthBound]] — the regime the LPU is optimized for.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
