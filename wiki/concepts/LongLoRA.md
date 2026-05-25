---
title: "LongLoRA"
type: concept
tags: [peft, lora, long-context, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# LongLoRA

A [[lora|LoRA]] variant from **Chen et al. (2023)** that adds **attention-modification techniques to expand context length** during PEFT finetuning. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "LongLoRA (Chen et al., 2023) is a LoRA variant that incorporates attention-modification techniques to expand context length."

## What it solves

Naive [[lora|LoRA]] finetuning doesn't change a model's positional encoding behavior — and many base models are trained with short context windows (4K, 8K, 16K tokens). Extending the context to 32K+ via standard LoRA tends to degrade quality.

LongLoRA adds two ideas on top of LoRA:
1. **Shifted sparse attention (S²-Attn)** during training — splits the sequence into chunks and shifts attention within each, reducing quadratic attention cost.
2. **Trainable embeddings and normalizations** — LoRA freezes most of the model; LongLoRA selectively unfreezes positional embeddings + normalization to better handle longer contexts.

## When to use

- When you need to extend context length beyond the base model's training length.
- When you don't want the full memory cost of [[FullFinetuning|full finetuning]] for long-context support.
- Alongside other long-context techniques (RoPE scaling, YaRN).

## Caveats

> "Compared to other finetuning techniques, long-context finetuning is harder to do. The resulting model might also degrade on shorter sequences." — Ch 7

LongLoRA inherits this — long-context-extended models can lose performance on short-context tasks.

## Connections

- [[lora|LoRA]] — parent method.
- [[LongContextFinetuning]] — parent operation category.
- [[PEFT]] — broader family.
- [[ContextLength]] — what LongLoRA extends.
- [[positionalencoding|Positional Encoding]] — the part of the architecture LongLoRA selectively retunes.
- [[ai-engineering-ch07-finetuning]] — primary source.
