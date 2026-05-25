---
title: "Partial Finetuning"
type: concept
tags: [finetuning, training]
sources: [ai-engineering-ch07-finetuning, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Partial Finetuning

A pre-PEFT finetuning regime where **only a subset of the base model's layers are unfrozen and trained**. The canonical instance: freeze the first N − 1 layers, finetune only the last layer. The motivation is straightforward — *the layers closest to the output are typically the most task-specific*, while earlier layers learn general features.

## Why it's been mostly replaced

Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], partial finetuning **reduces memory but is parameter-inefficient**. From the [[Houlsby2019AdapterModules|Houlsby et al. (2019)]] paper:

> "With BERT large (Devlin et al., 2018), you'd need to update approximately 25% of the parameters to achieve performance comparable to that of full finetuning on the GLUE benchmark."

In other words: partial FT needs roughly 25% of the trainable parameters to match [[FullFinetuning|full finetuning]] on GLUE. Compare that to [[lora|LoRA]] (which needed 0.0027% of GPT-3's parameters to match full FT on similar tasks) — partial FT looks wasteful in retrospect.

## Connections

- [[FineTuning]] — parent operation.
- [[FullFinetuning]] — all-parameter alternative.
- [[PEFT]] / [[lora|LoRA]] / [[adapterlayers|adapters]] — the parameter-efficient successors that obsoleted partial FT for most workflows.
- [[Houlsby2019AdapterModules]] — the paper that motivated the PEFT successors.
- [[ai-engineering-ch07-finetuning]] — primary source.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 provides **runnable empirical numbers** for partial fine-tuning on `bert-base-cased` + Rotten Tomatoes, via the [[LayerFreezing]] idiom (`param.requires_grad = False`):

| Regime | Trainable params (approx.) | F1 (1 epoch) |
|---|---|---|
| Full FT | 100% | **0.85** |
| Freeze blocks 0–9, train block 11 + head | ~10% | **0.80** |
| Freeze everything except classifier head | ~0.2% | **0.63** |

Ch 11's empirical result extends the Houlsby-et-al-2019 *"25%-of-params"* result: **even just block 11 + head** (well below 25%) gets 0.80 F1 — *"although we generally want to train as many layers as possible, you can get away with training less if you do not have the necessary computing power."* The chapter's iterative-block experiment (Figure 11-7) shows *"training only the first five encoder blocks is enough to almost reach the performance of training all encoder blocks."*

This is the wiki's **first runnable demonstration** of partial-FT for an encoder model. Notable contrast with LoRA: LoRA achieves the same compute reduction with **decoupled adapter weights** that can be swapped at inference time; partial FT just freezes blocks and is simpler but irreversible per checkpoint.
