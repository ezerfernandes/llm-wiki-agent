---
title: "Instruction Tuning"
type: concept
tags: [stub, training, llm, sft]
sources: [2604.14585-prompt-optimization-coin-flip, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Instruction Tuning

**Instruction tuning** is the post-pretraining supervised-fine-tuning stage in which an LM is trained on `(instruction, response)` pairs so it learns to follow natural-language directives. Combined with [[rlhf|RLHF]] / preference optimization, it produces the helpful-assistant policy that defines deployment-ready LMs.

## In the coin-flip framing

[[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] invoke instruction tuning + RLHF as the **mechanistic explanation** for why agent prompts in [[CompoundAISystem|compound AI systems]] do not interact:

> *"Instruction-tuning and RLHF train models to produce consistent outputs across diverse input phrasings — effectively compressing a wide range of input styles into a narrow output distribution. ... The pipeline behaves as a composition of independently-robust functions: coupling requires agents to depend on each other's phrasing, but instruction-tuning specifically eliminates phrasing sensitivity."*

This is the wiki's first concept-page handle for instruction tuning — held as a stub for future expansion when a canonical instruction-tuning paper enters the corpus.

## Connections

- [[rlhf]] — sibling post-pretraining stage.
- [[2604.14585-prompt-optimization-coin-flip]] — invokes IT/RLHF as the mechanism behind the agent-independence result.
- [[AgentCoupling]] — the structural property IT/RLHF eliminates.
- [[CompoundAISystem]] — the compositional target.
- [[ModelSpecificityShelfLife]] — IT/RLHF post-training is the channel through which base models absorb scaffold techniques over time.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* walks **the wiki's first runnable instruction-tuning recipe end-to-end**: turning a pretrained-only base model (`TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T`) into an instruction-following chat model via [[QLoRA]] + [[SFTTrainer]] on 3,000 [[UltraChat]] examples — on a free Google Colab Tesla T4 in roughly an hour.

### Why instruction tuning is necessary

The chapter's blunt framing of the pretraining-only base model:

> *"A pretrained model itself will not follow instructions but instead attempts to predict each next word. It may even create new questions."* — Ch 12

Instruction tuning (SFT on `(instruction, response)` pairs in chat-template format) is the **regime transition** from completion machine to instruction follower.

### The recipe (Ch 12)

1. **[[ChatTemplate|Chat template]]** — load the chat-variant tokenizer (`TinyLlama/TinyLlama-1.1BChat-v1.0`) just to call `apply_chat_template(...)`, producing `<|user|>\n{prompt}</s>\n<|assistant|>\n{response}</s>` formatted examples.
2. **Dataset** — `HuggingFaceH4/ultrachat_200k` `test_sft` split, shuffled, sliced to 3,000 examples.
3. **[[QLoRA]]** — 4-bit NF4 quantization of the base + LoRA adapter (`r=64`, `α=32`, all 7 Llama-family projection layers).
4. **[[SFTTrainer]]** — 1 epoch, `lr=2e-4`, cosine schedule, `paged_adamw_32bit` optimizer.
5. **Merge** — `peft.AutoPeftModelForCausalLM.from_pretrained(...).merge_and_unload()` fuses the LoRA delta into the base.
6. **Inference** — `transformers.pipeline("text-generation")` with the same chat template; verify the model now follows instructions.

### Position vs preference tuning

Ch 12 positions instruction tuning as **stage 1 of a two-stage post-training pipeline**, followed by [[PreferenceFinetuning|preference tuning]] ([[DPO]]) on top. Both stages reuse the same QLoRA substrate — only the trainer ([[SFTTrainer]] vs [[DPOTrainer]]) and dataset change.
