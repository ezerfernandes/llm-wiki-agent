---
title: "Activation Memory"
type: concept
tags: [memory, training, finetuning, transformers]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Activation Memory

The GPU memory consumed by **cached forward-pass activations needed for the backward pass** plus, for transformers, the **KV cache** of attention keys and values. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], activation memory **scales linearly with sequence length and batch size**, and *can dwarf the model-weight memory* at long context lengths.

## Why activations need to be stored

[[Backpropagation|Backprop]] needs the layer-wise inputs (post-activation) from the forward pass to compute the local gradients in the backward pass. So a naive training loop **caches every layer's activations on the forward pass** for use in the backward pass.

## Why this is a memory problem

> "If activations are stored for gradient computation, the memory needed for activations can dwarf the memory needed for the model's weights." — Ch 7, citing Korthikanti et al. (2022)

Concrete numbers (from the [[Korthikanti2022ActivationRecomputation|"Reducing Activation Recomputation in Large Transformer Models"]] paper Ch 7 cites): for the largest Megatron models, **activation memory exceeds weight memory at training-typical configurations**.

## The cheap rule of thumb (Ch 7)

For *inference*, Ch 7 assumes activation + KV-cache memory is **~20% of weight memory** — leading to the `N × M × 1.2` [[InferenceMemoryFormula|inference memory formula]]. This breaks down at long contexts. Use the formula as a lower bound.

## The mitigations

### [[GradientCheckpointing|Gradient checkpointing]] (= activation recomputation)

Don't cache activations on the forward pass. Instead, recompute them on the backward pass when needed. **Trades training time (~30% slower) for memory (~5–10× smaller activation footprint).** This is by far the most-used mitigation.

### [[FlashAttention|FlashAttention]]

Restructures the attention computation so activations never fully materialize in HBM. Saves activation memory specifically for the attention layer (which scales quadratically with sequence length and is the typical dominant term).

### Mixed precision / activation quantization

Store activations in lower precision (FP16 / BF16 / FP8) to halve or quarter the cost. Less common than weight quantization because **activations are more sensitive to precision** than weights.

### Pipeline / sequence parallelism

Spread activations across multiple devices.

## Connections

- [[MemoryBottleneck]] — Ch 7's umbrella concept.
- [[GradientCheckpointing]] / [[ActivationRecomputation]] — the standard mitigation.
- [[FlashAttention]] — the attention-specific mitigation.
- [[InferenceMemoryFormula]] — formula where activation memory contributes 20%.
- [[TrainingMemoryFormula]] — formula where activation memory can dwarf weights.
- [[Backpropagation]] — why activations need to be cached.
- [[Korthikanti2022ActivationRecomputation]] — citation.
- [[ai-engineering-ch07-finetuning]] — primary source.
