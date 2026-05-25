---
title: "TRL"
type: entity
tags: [tool, fine-tuning, library, hugging-face, open-source]
sources: [leh-ch05-supervised-fine-tuning, leh-ch06-preference-alignment, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

## What it is
TRL (Transformer Reinforcement Learning) is Hugging Face's open-source library of post-training algorithms for LLMs. It provides `SFTTrainer`, `DPOTrainer`, `PPOTrainer`, `KTOTrainer`, `RewardTrainer`, and trainers for IPO/ORPO — all built on top of `transformers` with FSDP and DeepSpeed support.

## In LLM Engineer's Handbook
Ch. 5 ([[leh-ch05-supervised-fine-tuning]]) names TRL as the most up-to-date of the three recommended fine-tuning libraries ([[TRL]] / [[Axolotl]] / [[Unsloth]]), and uses `SFTTrainer` (`learning_rate=3e-4`, `lr_scheduler_type="linear"`, `packing=True`, `optim="adamw_8bit"`, `num_train_epochs=3`) to produce `mlabonne/TwinLlama-3.1-8B`. Ch. 6 ([[leh-ch06-preference-alignment]]) uses TRL's `DPOTrainer` with `ref_model=None` (adapter-only), `beta=0.5`, and a split `max_prompt_length`/`max_length` to DPO-fine-tune the SFT checkpoint into `mlabonne/TwinLlama-3.1-8B-DPO`.

## Connections
- [[HuggingFace]] — publisher.
- [[Unsloth]] — pairs with TRL for accelerated single-GPU training.
- [[lora]] / [[QLoRA]] — adapter techniques applied via TRL.
- [[DPO]] / [[rlhf]] / [[SupervisedLearning]] — algorithms TRL implements.
- [[TwinLlama]] — model trained with TRL.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] of *Hands-On LLMs* uses TRL as the **trainer library** of its four-package fine-tuning stack ([[transformers]] + [[peft|PEFT]] + [[bitsandbytes]] + TRL). Both stages of the worked recipe run through TRL:

- **`trl.SFTTrainer`** — QLoRA supervised fine-tuning of [[TinyLlama|TinyLlama-1.1B]] on 3,000 [[UltraChat]] examples. Config: `dataset_text_field="text"`, `max_seq_length=512`. Consumes a [[LoraConfig|`peft.LoraConfig`]] via `peft_config`. Single-epoch training ≈ 1 hour on a free Google Colab Tesla T4.
- **`trl.DPOConfig`** + **`trl.DPOTrainer`** — direct preference optimization on top of the SFT-merged TinyLlama, using `argilla/distilabel-intel-orca-dpo-pairs`. Config: `beta=0.1`, `learning_rate=1e-5` (10× lower than SFT), `lr_scheduler_type="cosine"`, `warmup_ratio=0.1`, `max_steps=200`, `max_prompt_length=512`, `max_length=512`. Same QLoRA substrate as the SFT stage — only the trainer + dataset changes.

Ch 12's structural point: TRL's `SFTTrainer` and `DPOTrainer` are **regime-swappable on top of the same QLoRA substrate** — the cleanest demonstration of TRL as the post-training-pipeline-substrate the wiki has on record.
