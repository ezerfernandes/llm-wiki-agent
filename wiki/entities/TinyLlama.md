---
title: "TinyLlama"
type: entity
tags: [model, llama, open-source, small-llm, pretraining]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# TinyLlama

A **1.1B-parameter open-source LLM** with the [[Llama|Llama]] architecture, pretrained on a 3T-token corpus by the StatNLP Research Group at the Singapore University of Technology and Design (Zhang et al., arXiv:2401.02385). Designed to bring Llama-2-quality pretraining to a model small enough to run, fine-tune, and serve **on commodity hardware**.

Released variants include `TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T` (pretraining checkpoint, base model) and `TinyLlama/TinyLlama-1.1BChat-v1.0` (chat-tuned).

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] uses TinyLlama as its **base model for the worked fine-tuning recipes**. The chapter's deliberate pedagogical choice: at 1.1B parameters, TinyLlama fits the *"GPU-poor"* commitment of the book — loadable on a free Google Colab Tesla T4 even before quantization, and 4-bit-loadable in ~1 GB VRAM with [[QLoRA]].

### Two TinyLlama variants in Ch 12

| Variant | Role |
|---|---|
| `TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T` | **Base model** (pretrained only, no instruction tuning). The chapter's QLoRA SFT recipe turns this into an instruction-follower. |
| `TinyLlama/TinyLlama-1.1BChat-v1.0` | **Chat-tuned variant**. Used in Ch 12 only as the **tokenizer source** for `apply_chat_template` (so the chapter's generated SFT data uses the same `<\|user\|>...<\|assistant\|>` format the chat variant was trained on). For the DPO stage, the chapter loads a further-trained instruction-tuned TinyLlama *"that was first trained using full fine-tuning and then further aligned with DPO."* |

### Why TinyLlama for this chapter

The chapter doesn't explain its choice in detail but the operational rationale is clear:

- **Llama-family architecture** — same `q_proj / k_proj / v_proj / o_proj / up_proj / gate_proj / down_proj` projection-module names, so the QLoRA recipe's `target_modules` list (and `LoraConfig`) generalizes directly to the much larger Llama 2 / 3 / Mistral families.
- **3T-token pretraining** — high enough quality that SFT on 3,000 UltraChat examples meaningfully changes behavior.
- **1.1B parameters** — small enough that a single Colab T4 session can finish both SFT and DPO end-to-end.

## Connections

- [[Llama]] — the architecture family.
- [[meta|Meta]] — original architecture publisher (though TinyLlama itself is a community project).
- [[QLoRA]] / [[lora|LoRA]] / [[SFTTrainer]] / [[DPOTrainer]] — the fine-tuning stack applied in Ch 12.
- [[UltraChat]] / [[DistilabelIntelOrcaDPOPairs]] — the datasets the chapter pairs with TinyLlama.
- [[ChatTemplate]] — the `<\|user\|>...<\|assistant\|>` format the chat-variant tokenizer applies.
- [[GoogleColab]] — the recommended training environment.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
