---
title: "Gradient Checkpointing"
type: concept
tags: [memory, training, finetuning, optimization]
sources: [ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Gradient Checkpointing

A memory-saving training technique that **doesn't store activations on the forward pass; instead, it recomputes them when needed on the backward pass**. Also called **[[ActivationRecomputation|activation recomputation]]**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "One way to reduce the memory needed for activations is not to store them. Instead of storing activations for reuse, you recompute activations when necessary. This technique is called gradient checkpointing or activation recomputation. While this reduces the memory requirements, it increases the time needed for training due to the recomputation."

## The trade-off

| Approach | Activation memory | Training time |
|---|---|---|
| Cache all activations (default) | High (can exceed weight memory) | Standard |
| Gradient checkpointing | Low (only checkpointed activations cached) | ~30% slower (extra forward passes) |

For finetuning a foundation-scale model, the memory savings are essential and the wall-clock cost is acceptable.

## How it works

The forward pass divides the model into segments. At segment boundaries, **checkpoints** save the activations. Between checkpoints, activations are not cached. During the backward pass, when activations between checkpoints are needed, the forward pass for that segment is **re-run from the checkpoint** to materialize them.

If you checkpoint `√L` evenly-spaced layers in an `L`-layer network, you get an `O(√L)` activation-memory profile instead of `O(L)`, at the cost of a single extra forward pass through the model.

## When to use

- Whenever **[[ActivationMemory|activation memory]] is the binding constraint** (long contexts, large batches, deep models).
- In combination with [[PEFT]] — even with [[lora|LoRA]] freezing most params, activations of the *frozen* base still need to be cached for backprop through the LoRA adapters. Checkpointing helps here.
- Standard in most [[FullFinetuning|full FT]] runs of foundation-scale models.

## Built-in support

- [[PyTorch]]: `torch.utils.checkpoint`.
- [[TensorFlow]]: `tf.recompute_grad`.
- [[DeepSpeed]] / [[ColossalAI]] / [[HuggingFacePEFT|HF PEFT]]: enabled via a single config flag.

## Connections

- [[ActivationMemory]] — what gradient checkpointing reduces.
- [[ActivationRecomputation]] — alternate name.
- [[MemoryBottleneck]] — the umbrella problem.
- [[Backpropagation]] — the algorithm that requires activations.
- [[FlashAttention]] — orthogonal attention-specific recomputation.
- [[ai-engineering-ch07-finetuning]] — primary source.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* enables `gradient_checkpointing=True` in both the SFT and DPO `TrainingArguments` — paired with `fp16=True` and the `paged_adamw_32bit` optimizer to fit the [[TinyLlama|TinyLlama-1.1B]] + [[QLoRA]] training run inside a free Google Colab Tesla T4. The chapter doesn't dwell on the mechanism but treats it as a standard memory-saving knob that combines with QLoRA's quantization to enable the *"1 GB VRAM to load + a couple of GB for training"* budget the recipe targets.
