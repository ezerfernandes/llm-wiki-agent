---
title: "Unsloth"
type: entity
tags: [tool, fine-tuning, library, open-source, gpu]
sources: [leh-ch02-tooling-and-installation, leh-ch05-supervised-fine-tuning, leh-ch06-preference-alignment]
last_updated: 2026-05-22
---

## What it is
Unsloth (by Daniel and Michael Han) is an open-source fine-tuning library that rewrites the attention and MLP kernels for popular open-weight LLMs (Llama, Mistral, Gemma, Qwen, Phi) to deliver **2–5× faster training and up to 80% less memory** vs stock `transformers`/`peft`. It also auto-converts checkpoints to GGUF and supports LoRA + QLoRA on a single GPU.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) introduces Unsloth as the book's fine-tuning framework, integrated through the Hugging Face model registry. Ch. 5 ([[leh-ch05-supervised-fine-tuning]]) uses `FastLanguageModel.from_pretrained("meta-llama/Meta-Llama-3.1-8B", max_seq_length=2048)` with LoRA `r=32, lora_alpha=32` to fine-tune TwinLlama in 50 minutes on an A100 via [[TRL]]'s `SFTTrainer`. Ch. 6 ([[leh-ch06-preference-alignment]]) calls `PatchDPOTrainer()` first to enable Unsloth's DPO support, then re-uses `FastLanguageModel` to DPO-fine-tune `mlabonne/TwinLlama-3.1-8B` into `mlabonne/TwinLlama-3.1-8B-DPO`.

## Connections
- [[TRL]] — Hugging Face fine-tuning library Unsloth integrates with.
- [[HuggingFace]] — ecosystem Unsloth plugs into.
- [[lora]] / [[QLoRA]] — adapter techniques Unsloth accelerates.
- [[Llama3_8BInstruct]] — base model Unsloth fine-tunes in the book.
- [[TwinLlama]] — output of the Unsloth-driven training.
- [[NVIDIA]] — GPU vendor Unsloth's custom kernels target.
- [[MaximeLabonne]] — author who wrote the book's Unsloth-based SFT/DPO recipes.
