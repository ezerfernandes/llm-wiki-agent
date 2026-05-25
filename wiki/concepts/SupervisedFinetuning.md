---
title: "Supervised Finetuning"
type: concept
tags: [post-training, sft, alignment, llm]
sources: [ai-engineering-ch02-foundation-models, ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Supervised Finetuning

**SFT** is the first step of [[posttraining|post-training]]: finetune the pre-trained model on high-quality **(prompt, response) demonstration data** to optimize it for conversations instead of text completion. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Finetune the pre-trained model on high-quality instruction data to optimize models for conversations instead of completion."

## Why it's needed

A pre-trained model is optimized for **next-token prediction**, not conversation. If you input *"How to make pizza"* into a pre-trained model, it might:

1. **Add more context to the question** — *"for a family of six?"*
2. **Add follow-up questions** — *"What ingredients do I need? How much time would it take?"*
3. **Give the instructions on how to make pizza.**

Only option 3 is what users actually want. SFT teaches the model to default to option 3.

> *"A friend used this analogy: a pre-trained model talks like a web page, not a human."*

## Demonstration data

SFT trains on **(prompt, response) pairs called demonstration data**. The model **clones the demonstrated behavior** — hence the alternative name [[BehaviorCloning|behavior cloning]].

InstructGPT's labelers:
- ≈**90% had at least a college degree**.
- More than **1/3 had a master's degree**.
- **30 minutes per (prompt, response) pair** for some tasks (long-context summarization).
- **~$10/pair × 13,000 pairs = ~$130,000** total annotation cost — and that's just labor.

## Alternatives to expensive human labeling

- **[[LAION|LAION]]** mobilized 13,500 volunteers worldwide → 10,000 conversations / 161,443 messages / 35 languages / 461,292 quality ratings. Caveat: skewed demographics (90% male per self-report — Köpf et al. 2023).
- **[[googledeepmind|DeepMind]]'s Gopher** used heuristics to filter conversation-like text from web data (alternating `[A]: ... [B]: ...` paragraphs).
- **AI-generated [[SyntheticData|synthetic data]]** — discussed in Ch 8.

## Skipping pre-training is possible but worse

> "Technically, you can train a model from scratch on the demonstration data instead of finetuning a pre-trained model, effectively eliminating the self-supervised pre-training step. However, the pre-training approach often has returned superior results." — Ch 2

## Terminology ambiguity

Ch 2 explicitly avoids the term **instruction finetuning** because:
- Some use it as a synonym for SFT.
- Some use it to cover both SFT and [[PreferenceFinetuning|preference finetuning]].

To stay unambiguous, Huyen uses *SFT* and *preference finetuning* as the two distinct stages.

## Connections
- [[posttraining]] — the parent training stage.
- [[PreferenceFinetuning]] — the follow-on stage that aligns SFT outputs with human preference.
- [[DemonstrationData]] — the (prompt, response) input format.
- [[BehaviorCloning]] — the SFT learning paradigm.
- [[rlhf]] / [[DPO]] / [[RLAIF]] — the techniques used in the subsequent preference-finetuning stage.
- [[FineTuning]] — the broader operation SFT specializes.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[InternalKnowledgeMismatch]] — the hallucination hypothesis that SFT-induced behavior cloning is causally tied to.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7 reframes SFT as **one of several finetuning sub-types** the application engineer chooses from, alongside [[PreferenceFinetuning|preference finetuning]], [[ContinuedPretraining|continued pre-training]], [[InfillingFinetuning|infilling]], and [[LongContextFinetuning|long-context]] finetuning. [[ChipHuyen|Huyen]] notes that for SFT:

- Responses can be **open-ended** (summarization) or **close-ended** (classification).
- High-quality instruction data is **challenging and expensive** for tasks needing factual consistency, domain expertise, or political correctness. Ch 8 covers acquisition.
- The **[[PromptLossWeight|prompt loss weight]]** hyperparameter (default ~10%) controls how much prompts contribute to the loss vs. responses. Set it low because at inference time the model generates only responses — though never 0%, so the model still learns prompt structure.
- SFT can be combined with **[[ModelMerging|model merging]]** for multi-task setups — finetune separately per task, then merge, avoiding [[CatastrophicForgetting|catastrophic forgetting]].

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* is **the wiki's first runnable SFT recipe for generative LLMs** (vs Ch 7 / Ch 2's abstract framing). The chapter frames SFT as the **transition from completion to instruction-following**:

> *"SFT can also be used for other tasks, like classification, but is often used to go from a base generative model to an instruction (or chat) generative model."* — Ch 12

### The worked SFT recipe (Ch 12)

- **Base model**: `TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T` — pretrained-only [[TinyLlama]].
- **Trainer**: [[SFTTrainer|`trl.SFTTrainer`]] + [[QLoRA]] (4-bit NF4 + LoRA r=64 / α=32 on all 7 Llama-family projection layers).
- **Dataset**: 3,000 [[UltraChat]] examples in `<|user|>...<|assistant|>` [[ChatTemplate|chat-template]] format.
- **Hyperparameters**: 1 epoch (*"higher values tend to degrade performance"*), `lr=2e-4`, cosine schedule, `paged_adamw_32bit` optimizer, fp16 + gradient checkpointing.
- **Hardware**: Google Colab Tesla T4 (free tier) ≈ 1 hour wall-clock.
- **Merge step**: `peft.AutoPeftModelForCausalLM.from_pretrained(...).merge_and_unload()` to bake the LoRA delta into the base in 16-bit precision for inference.

### The toggle-between-SFT-and-full-FT framing

> *"By removing the `quantization_config` parameter when loading the model and skip the creation of `peft_config` ... we would go from 'Instruction tuning with QLoRA' to 'full instruction tuning.'"* — Ch 12

The chapter's structural point: the same training script flips between QLoRA-SFT and full-FT-SFT by toggling two arguments — making PEFT an **opt-in memory-saving overlay** rather than a separate code path.

### Position in the pipeline

Ch 12 positions SFT as **stage 1 of post-training**, immediately followed by [[PreferenceFinetuning|preference tuning]] ([[DPO]]). Both stages reuse the same [[QLoRA]] substrate — only the trainer ([[SFTTrainer]] vs [[DPOTrainer]]) and dataset (UltraChat vs `argilla/distilabel-intel-orca-dpo-pairs`) change.
