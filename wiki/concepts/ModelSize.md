---
title: "Model Size"
type: concept
tags: [neural-networks, memory, ml-systems, parameters, scaling]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Model Size

A model's parameter count, numerical precision, and required operations collectively define the **computational bargain it strikes with hardware** — the model's side of the [[IronLawOfMLSystems|silicon contract]]. Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]], parameter count alone is a *misleading* proxy for memory importance, because training state and activations scale differently.

## The MNIST anchor and the memory explosion

- The 784→128→64→10 net = **~109,386 parameters ≈ 438 KB in [[FP32]]** — already exceeding most L1 caches.
- [[GPT2|GPT-2]] = 1.5B parameters ≈ ~6 GB — a **~14,000× jump** that forces GPU memory over CPU RAM.

## Training vs inference memory

`Training Memory ≈ Weights + Optimizer States + Activations`. For the MNIST MLP at batch 32, **training needs ~4× the inference memory**:

- **Weights** (same in both phases).
- **Gradients** (same size as weights, training only).
- **[[OptimizerState|Optimizer state]]** — [[Adam]] stores momentum + variance (2× parameters); in mixed precision the full per-parameter training state is **~16 bytes/param (~8× the 2-byte FP16 inference weight)**, independent of model size.
- **[[ActivationMemory|Activations]]** — scale with batch size × layer widths; must be stored for [[Backpropagation|backprop]].

A model that fits one accelerator for inference often needs several for training — not from extra compute but from activation/optimizer storage, driving [[GradientCheckpointing|gradient checkpointing]] and [[ModelParallelism|model parallelism]].

## Connections

- [[IronLawOfMLSystems]] — the silicon-contract framing.
- [[WeightMatrix]] / [[MultiplyAccumulate]] — what parameters cost in compute.
- [[ActivationMemory]] / [[OptimizerState]] / [[Adam]] / [[TrainingMemoryFormula]] / [[InferenceMemoryFormula]] — the memory components.
- [[FP32]] / [[Quantization]] — precision's effect on footprint.
- [[GradientCheckpointing]] / [[ModelParallelism]] — responses to the capacity wall.
- [[mlsysbook-ch05-neural-computation]] — source.
