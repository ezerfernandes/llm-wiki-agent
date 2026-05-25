---
title: "BitFit — Bias-Term Finetuning"
type: concept
tags: [peft, adapter, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# BitFit — Bias-Term Finetuning

A [[PEFT]] method from **Zaken et al. (2021)** — finetune **only the bias parameters** of a transformer, leaving all weight matrices frozen. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "[[lora|LoRA]] is by far the most popular adapter-based method, and it will be the topic of the following section. Other adapter-based methods include BitFit (Zaken et al., 2021), which came out around the same time LoRA did."

## What's striking about BitFit

A typical transformer has very few bias parameters compared to weight parameters — far less than 1%. Finetuning only the biases:
- Trainable parameter count is tiny.
- Memory footprint is minimal.
- The result is sometimes competitive with [[FullFinetuning|full finetuning]] for downstream tasks.

This was a surprising empirical finding when the BitFit paper landed — *most of the relevant adaptation can happen in the bias terms alone*.

## Where BitFit fits

- **Same era as [[lora|LoRA]]** — both papers came out in 2021.
- **Lost to LoRA in adoption** — LoRA's broader applicability won the developer mindshare.
- **Pedagogically useful**: BitFit demonstrates the extreme of "how few parameters can you train and still get good performance" — even before LoRA-style factorization tricks.

## When to consider BitFit

- Extreme memory constraints where even LoRA is too much.
- Research / teaching contexts where the minimal-parameter regime is the point.
- As a baseline for PEFT method comparisons.

For most application contexts, [[lora|LoRA]] / [[QLoRA]] are the default; BitFit appears in the wiki primarily for completeness.

## Connections

- [[PEFT]] — parent family.
- [[lora|LoRA]] — the contemporaneous winner.
- [[IA3]] — sibling minimal-parameter method.
- [[FineTuning]] — parent operation.
- [[ai-engineering-ch07-finetuning]] — primary source.
