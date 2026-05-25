---
title: "Edward Hu"
type: entity
tags: [person, researcher, lora, peft]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Edward Hu

ML researcher, **first author of the [[lora|LoRA]] paper** — *"LoRA: Low-Rank Adaptation of Large Language Models"* (Hu, Shen, Wallis, Allen-Zhu, Li, Wang, Wang, Chen — ICLR 2022). Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], LoRA is the dominant [[PEFT]] technique in current use; Hu's paper is the chapter's longest single citation.

## Contribution

The LoRA paper introduced the **low-rank update parametrization** `W' = W + (α/r)·A·B` that lets you finetune a model by training just `A` and `B` (both small) while keeping `W` frozen. This:

- Cuts trainable parameters by **several orders of magnitude**.
- Adds **zero inference latency** (because A·B can be merged into W at serving time).
- Enables **[[MultiLoraServing|multi-LoRA serving]]** — many adapters share one base.

The empirical headline from the paper: **GPT-3 175B can be effectively finetuned using just 4.7M trainable LoRA parameters** (0.0027% of the original) matching or beating full finetuning on multiple benchmarks.

## Affiliation

[[microsoft|Microsoft]] Research at the time of the LoRA paper. Later academic and industry positions.

## Connections

- [[lora|LoRA]] — his foundational contribution.
- [[QLoRA]] / [[LongLoRA]] / [[ReLoRA]] / [[GaLore]] — descendants/variants.
- [[PEFT]] — the field LoRA dominates.
- [[ai-engineering-ch07-finetuning]] — wiki source.
