---
title: "PEFT — Parameter-Efficient Finetuning"
type: concept
tags: [finetuning, peft, memory-efficient]
sources: [ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# PEFT — Parameter-Efficient Finetuning

The umbrella term for finetuning techniques that **achieve performance close to [[FullFinetuning|full finetuning]] while using several orders of magnitude fewer [[TrainableParameters|trainable parameters]]**. The motivating idea, per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]: reducing the number of trainable parameters cuts the memory needed for [[Gradient|gradients]] and [[OptimizerState|optimizer states]], which scale linearly with the trainable-parameter count. With [[Adam]] (the dominant transformer optimizer), each trainable parameter requires 3 values (gradient + 2 optimizer states) × bytes-per-value — so collapsing from 13B trainable to 1B trainable trims ~72 GB off the training memory footprint.

## Origin

[[Houlsby2019AdapterModules|Houlsby et al. (2019)]] — "Parameter-Efficient Transfer Learning for NLP." Inserted two adapter modules into each transformer block of [[bert|BERT]]; achieved **within 0.4% of full finetuning using 3% of the trainable parameters** on [[GLUE]]. This is the paper Ch 7 names as PEFT's progenitor.

## Two main families (per Ch 7)

### 1. Adapter-based / additive methods

Add trainable parameters to the model's architecture:

- **[[adapterlayers|Houlsby 2019 adapters]]** — original, but adds inference latency.
- **[[lora|LoRA]]** (Hu et al., 2021) — *the dominant variant*; rank-r factorization of weight delta; mergeable back into base weights → zero inference latency.
- **[[QLoRA]]** (Dettmers et al., 2023) — 4-bit-quantized base + LoRA adapter; lets a 65B model finetune on one 48 GB GPU.
- **[[BitFit]]** (Zaken et al., 2021) — train only bias parameters.
- **[[IA3]]** (Liu et al., 2022) — per-activation scaling vectors; strong for multi-task batching.
- **[[LongLoRA]]** (Chen et al., 2023) — LoRA + attention modifications for context extension.

### 2. Soft-prompt-based methods

Modify how the model processes input by introducing learnable continuous prompt tokens:

- **[[PrefixTuning|Prefix tuning]]** (Li & Liang, 2021) — soft prompts at every transformer layer.
- **[[PTuning|P-Tuning]]** (Liu et al., 2021) — soft prompts at the input layer.
- **[[PromptTuning|Prompt tuning]]** (Lester et al., 2021) — soft prompts on embedded input only.

## Popularity (Ch 7 data)

[[ChipHuyen|Huyen]] analyzed 1,000+ open issues on `huggingface/peft` (October 2024) as a proxy for technique usage. The result: **[[lora|LoRA]] dominates**, soft-prompt methods are less common but growing.

## Beyond parameter efficiency: sample efficiency

PEFT methods are typically also **sample-efficient**: full finetuning may need tens of thousands to millions of examples; PEFT can deliver strong performance with a few thousand. This is part of why PEFT is the default for application engineers.

## Frameworks (Ch 7)

- [[HuggingFacePEFT|Hugging Face PEFT]] — the reference library.
- [[Axolotl]] / [[Unsloth]] / [[LitGPT]] — wrap PEFT methods with sensible defaults.
- [[LLaMAFactory]] — multi-method finetuning framework.

## Theoretical justification: [[IntrinsicDimension|intrinsic dimension]]

Why does PEFT work? [[Li2018IntrinsicDimension|Li et al. (2018)]] and [[Aghajanyan2020IntrinsicDimension|Aghajanyan et al. (2020)]] argue that **pre-training implicitly compresses an LLM's intrinsic dimension** — the minimal-parameter manifold the model lives on. Larger models have *lower* intrinsic dimensions after pre-training. So a 175B-parameter model's *useful* behavioral surface is much smaller than its parameter count suggests, and modifications to that small surface (via low-rank or adapter parameters) are sufficient to retarget it.

## Connections

- [[FineTuning]] — the parent operation; PEFT is a memory-efficient subclass.
- [[FullFinetuning]] — the all-weights baseline PEFT competes against.
- [[PartialFinetuning]] — the older "freeze first-N layers" approach; parameter-*inefficient*.
- [[MemoryBottleneck]] — what PEFT exists to address.
- [[lora|LoRA]] / [[QLoRA]] / [[adapterlayers|Adapters]] / [[BitFit]] / [[IA3]] / [[LongLoRA]] — adapter-family members.
- [[PrefixTuning]] / [[PTuning]] / [[PromptTuning]] — soft-prompt family members.
- [[IntrinsicDimension]] — the theoretical underpinning.
- [[ai-engineering-ch07-finetuning]] — the primary source for this page.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* introduces PEFT as the **disadvantage-fix for full fine-tuning**:

> *"Updating all parameters of a model has a large potential of increasing its performance but comes with several disadvantages. It is costly to train, has slow training times, and requires significant storage. To resolve these issues, attention has been given to parameter-efficient fine-tuning (PEFT) alternatives that focus on fine-tuning pretrained models at higher computational efficiency."* — Ch 12

The chapter walks two PEFT-family techniques with diagrams and code:

1. **[[adapterlayers|Adapters]]** — Houlsby et al. (ICML 2019); add modular trainable components after attention + FFN in each Transformer block. *"Fine-tuning 3.6% of BERT's parameters reaches within 0.4% of full fine-tuning"* on GLUE. The chapter mentions **AdapterHub** (Pfeiffer et al. 2020) as the central repository and **LLaMA-Adapter** (Zhang et al. 2023) as the generative-model extension with zero-init attention.
2. **[[lora|LoRA]]** + **[[QLoRA]]** — the chapter's worked-recipe choice. *"As an alternative to adapters, low-rank adaptation (LoRA) was introduced and is at the time of writing a widely used and effective technique for PEFT."*

The chapter's pedagogical framing is **fewer-trainable-parameters as bottleneck-relief**: by training only a small subset, PEFT reduces training time, storage, and the VRAM footprint of the optimizer states + gradients. Combined with quantization ([[QLoRA]]), the chapter shows a 1.1B-parameter model fine-tunable on a free Colab T4.
