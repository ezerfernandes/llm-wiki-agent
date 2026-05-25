---
title: "Memory Bottleneck (Finetuning)"
type: concept
tags: [finetuning, hardware, gpu, training]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Memory Bottleneck (Finetuning)

[[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]'s framing of finetuning's **#1 cost driver**: GPU memory. Foundation models are too big for naive [[FullFinetuning|full finetuning]] on most hardware, and the techniques that make finetuning viable ([[PEFT|PEFT]], [[Quantization|quantization]], [[GradientCheckpointing|gradient checkpointing]], [[CPUOffloading|CPU offloading]], [[ModelMerging|merging]]) all exist to attack this bottleneck.

> "Some might say that you're not doing AI until you've seen a 'RuntimeError: CUDA out of memory' error." — Ch 7, footnote

## The three memory contributors

1. **Model weights** — `N × M` bytes (parameter count × bytes per parameter).
2. **[[ActivationMemory|Activations + KV cache]]** — grows linearly with sequence length and batch size; ~20% of weight memory at typical sizes, but can dwarf weights at long contexts.
3. **[[TrainableParameters|Trainable parameters]] × ([[Gradient|gradients]] + [[OptimizerState|optimizer states]])** — the *training-only* term that makes finetuning much more expensive than inference.

## [[InferenceMemoryFormula|Inference]] vs. [[TrainingMemoryFormula|training]] memory

| Mode | Approximate formula |
|---|---|
| Inference | `N × M × 1.2` |
| Training | `weights + activations + gradients + optimizer states` |

For a 13B model in FP16 ([[Adam]]):
- Inference: 13B × 2 × 1.2 = **31.2 GB**.
- Training: 26 GB (weights) + activations + 13B × 3 × 2 bytes (78 GB for gradients + 2 Adam states) = **~104+ GB**.

This is why **inference fits on a 40 GB A100 but full FT of the same model does not**.

## Lever 1: reduce *trainable* parameters → [[PEFT|PEFT]]

Cutting trainable parameters from 13B to, say, 4.7M ([[lora|LoRA]] on GPT-3 175B style) drops the gradient + optimizer-state footprint from ~78 GB to ~28 MB. **This is the single biggest lever.**

## Lever 2: reduce *bits per value* → [[Quantization|quantization]]

A 10B model in FP32 = 40 GB; in FP16 = 20 GB; in INT8 = 10 GB; in INT4 = 5 GB. Most effective for the *base model weights* in [[QLoRA]]; less common for gradients/activations during training (sensitive to precision).

## Lever 3: don't store activations → [[GradientCheckpointing|gradient checkpointing]]

Recompute activations during the backward pass instead of caching them on the forward pass. Trades training time for memory.

## Lever 4: use CPU as overflow → [[CPUOffloading|CPU offloading]]

[[DeepSpeed]] (Rasley et al., 2020) pioneered offloading optimizer states and gradients to CPU memory when GPU memory is exhausted.

## Lever 5: cache, don't re-encode → prompt caching (Ch 9 territory)

A cross-feature lever; reduces inference memory pressure rather than finetuning memory pressure.

## Architecture-level consequence

> "Inference and training having distinct memory profiles is one of the reasons for the divergence in chips for training and inference, as discussed in Chapter 9." — Ch 7

The memory profile asymmetry is what drives the training-vs-inference hardware market split ([[NVIDIA]] H100/H200 for training; specialized inference accelerators for serve).

## Connections

- [[FineTuning]] / [[FullFinetuning]] / [[PEFT]] — the operations memory constrains.
- [[InferenceMemoryFormula]] / [[TrainingMemoryFormula]] — the back-of-the-napkin math.
- [[TrainableParameters]] / [[FrozenParameters]] / [[OptimizerState]] / [[ActivationMemory]] — the components.
- [[Quantization]] / [[GradientCheckpointing]] / [[CPUOffloading]] / [[MixedPrecisionTraining]] — the levers.
- [[lora|LoRA]] / [[QLoRA]] — the PEFT methods that operationalize the levers.
- [[DeepSpeed]] / [[ZeRO]] — the CPU-offloading framework.
- [[ai-engineering-ch07-finetuning]] — primary source.
