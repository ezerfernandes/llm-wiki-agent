---
title: "Llama"
type: entity
tags: [model-family, llm, meta, open-weight]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch02-tooling-and-installation, leh-ch05-supervised-fine-tuning, leh-ch06-preference-alignment, leh-ch07-evaluating-llms, leh-ch08-inference-optimization, leh-ch10-inference-pipeline-deployment, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch03-looking-inside-llms, ai-engineering-ch08-dataset-engineering, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

## What it is
Llama is the open-weight LLM family released by [[meta|Meta]] — Llama 1, Llama 2, Llama 3, and Llama 3.1 (with the book using Llama 3.1 8B as the fine-tune base). The family covers sizes from 1B to 405B parameters.

## In LLM Engineer's Handbook
Llama is one of the three LLM families ([[Mistral]], Llama, [[GPT]]) the LLM Twin training pipeline must be able to swap between (Ch. 1: [[leh-ch01-understanding-llm-twin-concept]]). The concrete base model is `meta-llama/Meta-Llama-3.1-8B` (Ch. 5: [[leh-ch05-supervised-fine-tuning]]); the comparison baseline is `meta-llama/Meta-Llama-3.1-8B-Instruct` (Ch. 7: [[leh-ch07-evaluating-llms]]). Ch. 8 ([[leh-ch08-inference-optimization]]) uses `meta-llama/Meta-Llama-3-8B-Instruct` to demonstrate LLM.int8() and NF4 quantization, and Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) deploys the fine-tuned `mlabonne/TwinLlama-3.1-8B-13` (derived from Llama 3.1 8B) on a SageMaker endpoint. Ch. 2 ([[leh-ch02-tooling-and-installation]]) mentions Llama 2/3 as foundation models served by [[AmazonBedrock]].

## Connections
- [[meta]] — publisher of the Llama family.
- [[Llama2_7BChat]] / [[Llama3_8BInstruct]] / [[LLaMA4Maverick]] — specific model entity pages.
- [[TwinLlama]] — the fine-tuned LLM Twin model derived from Llama 3.1 8B.
- [[Mistral]] / [[GPT]] — peer model families the book treats as swappable.
- [[HuggingFace]] — distribution channel for Llama weights.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 of *Hands-On LLMs* uses [[Llama|Llama 2]] as **the canonical anchor for LLM training cost**:

> "Llama 2 has been trained on a dataset containing 2 trillion tokens. Imagine the compute necessary to create that model!" — Ch 1

And later, in the VRAM / GPU section:

> "To create the Llama 2 family of models, for example, Meta used A100-80 GB GPUs. Assuming renting such a GPU would cost $1.50/hr, the total costs of creating these models would exceed $5,000,000! The models were trained for 3,311,616 GPU hours." — Ch 1

Llama is also one of four representative [[OpenSourceLLM|open-weights LLM]] families Ch 1 names (alongside [[Cohere]] Command R, [[Mistral]], and [[microsoft|Microsoft's]] Phi).

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]] (tokenizer)

Ch 2 surveys the **Llama 2 tokenizer** (which [[Phi3Mini|Phi-3]] reuses with added chat tokens):

- **Method**: [[BPE]].
- **Vocabulary size**: 32,000.
- **Standard special token**: `<s>` (beginning-of-text marker).

Llama 2's BPE tokenizer is the **direct ancestor of the Phi-3 tokenizer** Ch 2 uses as its primary worked example — Phi-3 adds chat-role tokens (`<|user|>`, `<|assistant|>`, `<|system|>`) on top of the same 32,000-token Llama 2 vocabulary.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] (architecture)

Ch 3 names **Llama 2** and **Llama 3** as the canonical 2024-era models using the **modern Transformer block recipe**:

- **[[GroupedQueryAttention|Grouped-query attention (GQA)]]** — *"Used by models like Llama 2 and 3."* The K/V projections are shared **within groups of attention heads** rather than per-head ([[multiheadattention|multi-head]]) or across all heads ([[multiqueryattention|MQA]]). GQA was introduced in *"GQA: Training generalized multi-query transformer models from multi-head checkpoints"* — built on top of MQA from [[NoamShazeer|Shazeer]] (2019).
- **[[PreNorm|Pre-normalization]]** placement, **[[RMSNorm|RMSNorm]]** instead of LayerNorm, **[[SwiGLU|SwiGLU]]** instead of ReLU activation.
- **[[RoPE|Rotary positional embeddings (RoPE)]]** applied at the attention step.

Llama 2 / Llama 3 are thus the **headline contemporary deployment** of the modern block bundle Ch 3 codifies. Ch 3 also notes that *"Transformer LLMs are composed of a series Transformer blocks (often in the range of six in the original Transformer paper, to over a hundred in many large LLMs)"* — Llama 3 405B with 126 blocks (per the [[transformer|Transformer page]]'s Ch 2 table) sits at the upper end of that range.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 is the wiki's most detailed treatment of the **Llama 3 data pipeline** — the chapter's single most-cited model. Key data points:

### Per-phase data mix (Dubey et al. 2024)

| Domain | Pre-training | SFT | Preference FT |
|---|---|---|---|
| General knowledge (English) | 50% | 82.0% | 52.7% |
| Math and reasoning | 25% | 5.9% | 21.2% |
| Coding | 17% | 6.9% | 14.9% |
| Multilingual | 8% | 5.2% | 3.0% |
| Exam-like | — | — | 8.1% |
| Long context | — | — | 0.1% |

### Llama 3 attribution for performance gains

> "Llama 3 doesn't deviate significantly from older Llama versions in terms of model architecture. Llama 3's performance gains are 'primarily driven by improvements in **data quality and diversity** as well as by increased training scale.'"

So the entire post-Llama-2 generation jump is credited to **dataset engineering**, not architecture.

### The 2.7M synthetic coding examples

The Llama 3 SFT pipeline used a verifiable AI-data-synthesis pipeline combining:

1. **Code generation** — AI generates problem descriptions + solutions in diverse languages.
2. **Code translation** — AI translates code across programming languages; filters via tests.
3. **[[CodeBackTranslation|Code back-translation]]** — AI generates code explanations + documentation; verifies via regeneration.

Result: **>2.7 million synthetic coding examples** for Llama 3.1 SFT — most of the chapter's "synthetic data" content sits inside this pipeline.

### The "know what it knows" principle

Quoted from the Llama 3 paper in both Ch 7 and Ch 8:

> "Post-training should align the model to 'know what it knows' rather than add knowledge."

The implication: synthetic data is appropriate for **format / style / behavior**, less appropriate for adding new factual knowledge.

### Human vs AI annotation in Llama 3

> "Human-generated data is more prone to errors and inconsistencies, particularly for nuanced safety policies. This led [Meta] to develop AI-assisted annotation tools to ensure high data quality."

A counter-result to the conventional "human data is gold-standard" framing — for *certain task types*, AI-assisted annotation is more consistent than human-only annotation.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* uses the **Llama architecture** as the substrate of its worked fine-tuning recipes via [[TinyLlama|TinyLlama-1.1B]] — a community-built Llama-architecture model at 1.1B parameters. The chapter's `LoraConfig.target_modules` list — `["k_proj", "gate_proj", "v_proj", "up_proj", "q_proj", "o_proj", "down_proj"]` — targets the **seven Llama-family projection layers** (attention Q/K/V/O + FFN up/gate/down), making the recipe **transferable** to Llama 2 / Llama 3 / Mistral / Phi by changing only the base-model ID.

Ch 12 also surfaces a **Llama 2 multi-reward-model design** as a canonical example of multi-objective preference tuning: separate reward models for **helpfulness** and **safety**, combined at the RL step. This is the wiki's first record of multi-objective reward modeling as a deliberate Llama 2 architectural choice.
