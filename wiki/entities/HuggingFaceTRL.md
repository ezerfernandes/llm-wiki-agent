---
title: "Hugging Face TRL"
type: entity
tags: [tool, library, hugging-face, rlhf, dpo, sft, open-source, post-training]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Hugging Face TRL

**`trl` — Transformer Reinforcement Learning** — Hugging Face's open-source library of post-training algorithms for LLMs. Sibling entity page to [[trl]] (which is also indexed at the lowercase slug for cross-source convergence); both refer to the same library. Provides `SFTTrainer`, `DPOTrainer`, `PPOTrainer`, `KTOTrainer`, `RewardTrainer`, and trainers for IPO / ORPO — all built on top of [[transformers]] with FSDP and DeepSpeed support, and integrated with [[peft|PEFT]] adapters via `peft_config`.

## Summary

TRL is the canonical post-training library across the wiki's fine-tuning sources. [[leh-ch05-supervised-fine-tuning|LEH Ch 5]] names it the most up-to-date of three recommended fine-tuning libraries (TRL / [[Axolotl]] / [[Unsloth]]); [[leh-ch06-preference-alignment|LEH Ch 6]] uses `DPOTrainer` to align an 8B Llama-3; [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]] walks both `SFTTrainer` (over [[UltraChat]]) and `DPOTrainer` (over [[DistilabelIntelOrcaDPOPairs|orca-dpo-pairs]]) on a 1.1B [[TinyLlama]] base.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 uses TRL as the **trainer library** of its four-package fine-tuning stack ([[transformers]] + [[peft|PEFT]] + [[bitsandbytes]] + TRL). Specifically:

- **`trl.SFTTrainer`** — supervised fine-tuning trainer; consumes `peft_config` (the [[LoraConfig]]), `dataset_text_field="text"`, `max_seq_length=512`. Used to QLoRA-fine-tune TinyLlama on 3,000 UltraChat examples in ~1 hour on a free Google Colab Tesla T4.
- **`trl.DPOConfig`** + **`trl.DPOTrainer`** — direct preference optimization trainer; `beta=0.1`, `learning_rate=1e-5`, `lr_scheduler_type="cosine"`, `max_steps=200`, `warmup_ratio=0.1`, `max_prompt_length=512`, `max_length=512`. Used to DPO-tune the SFT-merged TinyLlama on `argilla/distilabel-intel-orca-dpo-pairs`.
- **Same [[LoraConfig]] for both stages** — Ch 12's structural point: TRL's `SFTTrainer` and `DPOTrainer` are **regime-swappable** on top of the same QLoRA substrate; only the trainer + dataset changes.

## Connections

- [[trl]] — sibling slug for the same library.
- [[HuggingFace]] — the publisher.
- [[transformers]] / [[peft]] / [[bitsandbytes]] — the companion libraries Ch 12 stacks with TRL.
- [[SFTTrainer]] / [[DPOTrainer]] / [[DPOConfig]] — specific TRL APIs.
- [[DPO]] / [[PPO]] / [[ORPO]] / [[rlhf]] — preference-tuning algorithms TRL implements.
- [[SupervisedFinetuning]] / [[PreferenceFinetuning]] — the two-stage post-training pipeline Ch 12 walks via TRL.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
