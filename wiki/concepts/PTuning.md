---
title: "P-Tuning"
type: concept
tags: [peft, soft-prompt, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# P-Tuning

A [[SoftPrompt|soft-prompt]] [[PEFT]] method from **Liu et al. (2021)** — *"GPT Understands, Too"* — that prepends learnable continuous prompt tokens to the input, typically through a small encoder (LSTM or MLP). Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Soft prompt tuning as a subfield is characterized by a series of similar-sounding techniques that can be confusing, such as prefix-tuning (Li and Liang, 2021), P-Tuning (Liu et al., 2021), and prompt tuning (Lester et al., 2021). ... I've never met a single person who could explain to me, on the spot, the differences between these techniques."

## How it differs from siblings

| Method | Where soft prompts go | Distinct feature |
|---|---|---|
| **[[PrefixTuning\|Prefix tuning]]** | Every transformer layer | Per-layer prefixes |
| **P-Tuning** | Input layer (via encoder) | Uses a small encoder (LSTM/MLP) to produce prompt embeddings |
| **[[PromptTuning\|Prompt tuning]]** | Embedded input only | Simplest variant |

**P-Tuning v2** (Liu et al. 2022) extends P-Tuning with deep prompt tuning across all layers — converging closer to prefix tuning's design.

## When to use

- For NLU tasks where soft prompts have shown strength.
- When you want a middle ground between prompt tuning's simplicity and prefix tuning's per-layer depth.

For most application work, [[lora|LoRA]] / [[QLoRA]] dominate. P-Tuning appears in the wiki primarily as part of the soft-prompt taxonomy.

## Connections

- [[PEFT]] — parent family.
- [[PromptTuning]] / [[PrefixTuning]] — sibling soft-prompt methods.
- [[SoftPrompt]] — the underlying mechanism.
- [[ai-engineering-ch07-finetuning]] — primary source.
