---
title: "LitGPT"
type: entity
tags: [tool, finetuning, framework, lightning-ai, open-source]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# LitGPT

An open-source finetuning + pretraining framework from **Lightning AI** (the company behind PyTorch Lightning). Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], named among the "great finetuning frameworks available" alongside [[LLaMAFactory]], [[Unsloth]], [[HuggingFacePEFT|HF PEFT]], and [[Axolotl]].

## What it offers

- Clean, readable PyTorch Lightning-based training scripts for 20+ LLM architectures (Llama, Mistral, Phi, Gemma, Falcon, etc.).
- Full finetuning, [[lora|LoRA]], [[QLoRA]], and prompt tuning.
- Built-in support for distributed training across multiple GPUs / nodes.
- Strong reproducibility story (Lightning's design ethos).

## Position relative to siblings

- **[[Unsloth]]** is faster on single-GPU; LitGPT is more flexible for multi-GPU.
- **[[Axolotl]]** is more config-driven; LitGPT is more scriptable.
- **[[LLaMAFactory]]** supports more methods; LitGPT is cleaner per-method.
- **[[HuggingFacePEFT|HF PEFT]]** is the underlying method library; LitGPT wraps training around it.

## Affiliation

Lightning AI — the company that originated [[PyTorchLightning|PyTorch Lightning]]. [[SebastianRaschka|Sebastian Raschka]] is associated with the company and contributes to its educational content.

## Connections

- [[FineTuning]] / [[lora|LoRA]] / [[QLoRA]] — supported methods.
- [[PyTorchLightning]] — underlying training framework.
- [[SebastianRaschka]] — associated voice.
- [[LLaMAFactory]] / [[Unsloth]] / [[Axolotl]] / [[HuggingFacePEFT]] — siblings.
- [[ai-engineering-ch07-finetuning]] — wiki source.
