---
title: "LLaMA-Factory"
type: entity
tags: [tool, finetuning, framework, open-source]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# LLaMA-Factory

An open-source finetuning framework that **supports a wide range of finetuning methods** (full, LoRA, QLoRA, prefix tuning, prompt tuning, RLHF, DPO) across many base model families ([[Llama]], [[qwen|Qwen]], [[Mistral]], [[bert|BERT]], etc.) with a unified configuration interface. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "You can also finetune using one of many great finetuning frameworks available, such as LLaMA-Factory, unsloth, PEFT, Axolotl, and LitGPT. They support a wide range of finetuning methods, especially adapter-based techniques."

## Position in the framework landscape

Among single-machine finetuning frameworks cited in Ch 7:

- **[[HuggingFacePEFT|HF PEFT]]** — the reference library; method-focused.
- **LLaMA-Factory** — broad model support; config-driven.
- **[[Axolotl]]** — config-file-driven; production-popular.
- **[[Unsloth]]** — speed-focused; 2× faster, less memory.
- **[[LitGPT]]** — from Lightning AI; pretraining + finetuning oriented.

LLaMA-Factory differentiates by **breadth of supported methods and base models in one tool**.

## Repository

GitHub: `hiyouga/LLaMA-Factory`.

## When to choose LLaMA-Factory

- You want to try multiple finetuning methods on the same base without learning multiple frameworks.
- You want a config-driven workflow rather than imperative training scripts.
- You're working with a base model family the framework supports first-class.

## Connections

- [[FineTuning]] / [[PEFT]] / [[lora|LoRA]] / [[QLoRA]] — the methods supported.
- [[HuggingFacePEFT]] / [[Axolotl]] / [[Unsloth]] / [[LitGPT]] — sibling frameworks.
- [[ai-engineering-ch07-finetuning]] — wiki source.
