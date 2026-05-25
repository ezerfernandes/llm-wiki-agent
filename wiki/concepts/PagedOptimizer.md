---
title: "Paged Optimizer"
type: concept
tags: [optimizer, quantization, qlora, memory-optimization, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models, ai-engineering-ch07-finetuning]
last_updated: 2026-05-23
---

# Paged Optimizer

A **paged optimizer** keeps optimizer state (e.g., Adam's first- and second-moment estimates) in **CPU memory** and **pages it onto the GPU on demand** when the optimizer step runs — preventing OOM crashes during the spikes that long-sequence training causes. Introduced by [[TimDettmers|Dettmers]] et al. as part of the **[[QLoRA]]** paper alongside [[NormalFloat4|NF4]] and [[DoubleQuantization|double quantization]].

The canonical incarnation is **[[PagedAdamW32bit|`paged_adamw_32bit`]]** — a paged variant of [[Adam|AdamW]] keeping the optimizer states in FP32.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] uses `optim="paged_adamw_32bit"` for both the SFT and DPO training runs:

> *"The paged optimizers used in the original QLoRA paper."* — Ch 12 explaining the `optim` field

This is one of *"more elegant methods to further optimize this like double quantization and paged optimizers, which you can read about more in the QLoRA paper"* (Ch 12).

## Why it matters

Without paging, the optimizer states live alongside the gradients and parameters on the GPU. During long-sequence forward passes (especially when paired with [[GradientCheckpointing|gradient checkpointing]]), VRAM utilization spikes; if the spike exceeds the GPU's memory at the moment the optimizer step runs, training crashes. Paging lets the spike subside before the optimizer states are pulled back to the GPU, smoothing the memory profile.

## Connections

- [[QLoRA]] — the parent technique.
- [[NormalFloat4|NF4]] / [[DoubleQuantization]] — the two other QLoRA innovations.
- [[bitsandbytes]] — the library that ships `paged_adamw_32bit`.
- [[Adam|AdamW]] — the underlying optimizer.
- [[PagedAdamW32bit]] — the canonical implementation name.
- [[TimDettmers]] — first author of the QLoRA paper.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
- [[ai-engineering-ch07-finetuning]] — Huyen's parallel coverage.
