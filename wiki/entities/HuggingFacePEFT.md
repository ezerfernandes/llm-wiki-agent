---
title: "Hugging Face PEFT"
type: entity
tags: [tool, library, hugging-face, peft, open-source, fine-tuning]
sources: [ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Hugging Face PEFT

**`peft`** — Hugging Face's open-source library implementing [[PEFT|parameter-efficient fine-tuning]] methods on top of [[transformers]]. Provides `LoraConfig` ([[lora|LoRA]]), `PrefixTuningConfig`, `PromptTuningConfig`, `IA3Config`, `AutoPeftModelForCausalLM`, `prepare_model_for_kbit_training`, and the `merge_and_unload()` API for fusing adapters back into a base model. The canonical adapter implementation across the wiki's fine-tuning sources.

## Summary

`peft` lets a base [[transformers]] model be wrapped with a trainable adapter (LoRA / prefix / IA3) without modifying the base weights. The adapter is saved separately, can be merged back at inference time for zero overhead, and integrates with [[trl|TRL]]'s `SFTTrainer` / `DPOTrainer` via the `peft_config` argument.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

[[ChipHuyen|Huyen]] Ch 7 names `huggingface/peft` as the **reference PEFT library** and uses its GitHub-issues distribution (1,000+ issues, October 2024) as a real-world proxy for technique popularity — finding that [[lora|LoRA]] dominates open-issue traffic.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 uses `peft` as the **adapter library** of its four-package fine-tuning stack ([[transformers]] + `peft` + [[bitsandbytes]] + [[trl|TRL]]). Specifically:

- **`peft.LoraConfig`** — configures the QLoRA adapter: `r=64`, `lora_alpha=32`, `lora_dropout=0.1`, `bias="none"`, `task_type="CAUSAL_LM"`, `target_modules=["k_proj", "gate_proj", "v_proj", "up_proj", "q_proj", "o_proj", "down_proj"]` (all seven Llama-family projection layers).
- **`peft.prepare_model_for_kbit_training`** — utility to make a quantized [[bitsandbytes]] model trainable.
- **`peft.AutoPeftModelForCausalLM.from_pretrained(...).merge_and_unload()`** — reloads the base model in 16-bit precision and merges the LoRA delta back into the frozen base weights. Used iteratively in Ch 12's DPO recipe: merge the SFT adapter into the base, then merge the DPO adapter into the SFT-merged model.

## Connections

- [[HuggingFace]] — the publisher.
- [[transformers]] — the base library `peft` extends.
- [[trl]] — TRL's trainers consume `peft_config`.
- [[PEFT]] / [[lora|LoRA]] / [[QLoRA]] — the techniques `peft` implements.
- [[LoraConfig]] / [[AutoPeftModelForCausalLM]] / [[PrepareModelForKBitTraining]] — specific `peft` APIs.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
