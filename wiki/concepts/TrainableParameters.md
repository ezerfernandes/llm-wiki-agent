---
title: "Trainable Parameters"
type: concept
tags: [training, finetuning, memory]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Trainable Parameters

A parameter that **can be updated during finetuning**, as opposed to a [[FrozenParameters|frozen parameter]] that is kept unchanged. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

- During **[[Pretraining|pre-training]]**, all model parameters are trainable.
- During **inference**, no model parameters are trainable.
- During **finetuning**, *some or all* model parameters may be trainable.

## Why this matters for memory

The [[TrainingMemoryFormula|training memory formula]] tells us each trainable parameter requires storage for its **[[Gradient|gradient]] + [[OptimizerState|optimizer states]]**. With [[Adam]] at FP16, that's 6 bytes per trainable parameter. So:

- 13B fully trainable → 13B × 6 = **78 GB** for gradients + optimizer states.
- 1B trainable → 1B × 6 = **6 GB**.
- 4.7M trainable ([[lora|LoRA]] on GPT-3 175B) → 4.7M × 6 = **~28 MB**.

The collapse from 78 GB to 28 MB is the entire reason [[PEFT|PEFT]] exists.

## The fundamental PEFT motivation

> "The more trainable parameters, the higher the memory footprint. You can reduce memory requirement for finetuning by reducing the number of trainable parameters. Reducing the number of trainable parameters is the motivation for PEFT, parameter-efficient finetuning." — Ch 7

## Where Ch 7 expects you to set the threshold

Ch 7's working definition of "parameter-efficient" — *several orders of magnitude fewer trainable parameters than full finetuning, with performance close to full FT*. [[Houlsby2019AdapterModules|Houlsby et al. (2019)]] hit it with 3% of BERT's parameters; [[lora|LoRA]] hit 0.0027% of GPT-3's.

## Connections

- [[FrozenParameters]] — the unchanged-during-FT counterpart.
- [[PEFT]] — the family of techniques that minimize trainable parameters.
- [[FullFinetuning]] — all parameters trainable.
- [[PartialFinetuning]] — some layers trainable (older approach).
- [[lora|LoRA]] — the dominant low-trainable-parameter method.
- [[TrainingMemoryFormula]] / [[MemoryBottleneck]] — the cost framework.
- [[OptimizerState]] / [[Gradient]] — the per-trainable-parameter costs.
- [[ai-engineering-ch07-finetuning]] — primary source.
