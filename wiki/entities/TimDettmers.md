---
title: "Tim Dettmers"
type: entity
tags: [person, researcher, quantization, peft]
sources: [ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Tim Dettmers

ML researcher known for **foundational work on LLM quantization and quantized finetuning**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], the author behind:

- **LLM.int8()** ([[Dettmers2022LLMint8|Dettmers et al., 2022]]) — making 8-bit LLM inference viable at scale; preserves quality via outlier handling.
- **[[QLoRA]]** (Dettmers, Pagnoni, Holtzman & Zettlemoyer, NeurIPS 2023) — 4-bit NF4 quantization of base + BF16 LoRA + paged optimizers; lets a 65B model finetune on a single 48 GB GPU.
- **[[NormalFloat4|NF4]]** — the 4-bit format designed around the normal distribution of pre-trained weights.
- **[[Bitsandbytes]]** — the open-source library that implements 8-bit and 4-bit quantization (alongside other contributors).

## The combined impact

[[ChipHuyen|Huyen]] credits Dettmers et al. throughout Ch 7's quantization section. The arc from LLM.int8() (2022) → QLoRA (2023) is the single biggest reason finetuning moved from "expensive cluster operation" to "single-GPU operation" for billion-parameter models.

## Affiliation

University of Washington PhD (with [[LukeZettlemoyer|Luke Zettlemoyer]]); has worked with [[meta|Meta AI]] and other institutions.

## Connections

- [[QLoRA]] / [[NormalFloat4]] / [[Bitsandbytes]] — his work products.
- [[lora|LoRA]] — the parent technique QLoRA quantizes.
- [[Quantization]] — the broader field he reshaped.
- [[ai-engineering-ch07-finetuning]] — wiki source citing this work.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* is the wiki's **first runnable end-to-end QLoRA recipe**, fulfilling the practical promise of Dettmers' research line: a 1.1B-parameter [[TinyLlama]] fine-tuned end-to-end (SFT + DPO) on a free Google Colab T4. The chapter walks all three QLoRA innovations attributed to Dettmers et al.:

1. **[[BlockwiseQuantization|Blockwise quantization]]** — per-block quantization constants.
2. **[[NormalFloat4|NF4]]** — quantize by bins distributed according to the normal distribution of pretrained weights.
3. **[[DoubleQuantization|Double quantization]] + [[PagedOptimizer|paged optimizers]]** — additional memory optimizations *"to further optimize this ... read about more in the QLoRA paper."*

The chapter's structural payoff for Dettmers' research: *"By removing those, we would go from 'Instruction tuning with QLoRA' to 'full instruction tuning'"* — the same training script flips between QLoRA and full FT by toggling two arguments, making Dettmers' quantization stack an **opt-in memory-saving overlay** rather than a separate research code path.
