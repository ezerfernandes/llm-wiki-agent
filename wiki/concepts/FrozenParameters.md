---
title: "Frozen Parameters"
type: concept
tags: [training, finetuning, memory]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Frozen Parameters

Parameters **kept unchanged during finetuning**. The complement of [[TrainableParameters|trainable parameters]]. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "The parameters that are kept unchanged are frozen parameters."

## Memory implications

A frozen parameter requires storage for **its value only** — no gradient, no optimizer state. So freezing a parameter saves the 6 bytes (FP16 [[Adam]]) of gradient + optimizer-state overhead per parameter. **Freezing is the cheapest possible memory optimization** when training quality permits.

Frozen parameters still participate in the **forward pass** (to compute downstream activations and propagate signal) and still appear in the **backward pass** (to propagate gradients through to *trainable* parameters downstream of them). But no gradient is stored *for* the frozen parameter itself.

## Where freezing shows up

- **[[FullFinetuning|Full finetuning]]** — zero frozen parameters.
- **[[PartialFinetuning|Partial finetuning]]** — earlier layers frozen, later layers trainable.
- **[[PEFT|PEFT]] methods** — the entire base model is frozen; only adapter / soft-prompt parameters are trainable.
- **[[lora|LoRA]]** — `W` is frozen; `A` and `B` are trainable. The LoRA update `W' = W + (α/r)·W_AB` is computed at serve time without touching `W`.

## A subtle point

Even though a frozen parameter contributes no gradient *for itself*, **the gradient computation still flows backward through it** to update earlier trainable parameters. So freezing reduces *storage* but not necessarily *backward-pass FLOPs* — depending on the model graph structure.

## Connections

- [[TrainableParameters]] — the counterpart concept.
- [[PEFT]] / [[lora|LoRA]] / [[adapterlayers|adapters]] — the methods that freeze the entire base.
- [[PartialFinetuning]] — partial freeze.
- [[TrainingMemoryFormula]] — the formula frozen parameters cheaply reduce.
- [[ai-engineering-ch07-finetuning]] — primary source.
