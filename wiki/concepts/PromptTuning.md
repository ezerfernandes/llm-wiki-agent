---
title: "Prompt Tuning"
type: concept
tags: [peft, soft-prompt, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Prompt Tuning

A [[SoftPrompt|soft-prompt]] [[PEFT]] method from **Lester, Al-Rfou, and Constant (2021)** — *"The Power of Scale for Parameter-Efficient Prompt Tuning."* Prepends a small number of learnable continuous prompt tokens to the **embedded input only** (not to every transformer layer). Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Prompt tuning prepends soft prompt tokens to only the embedded input."

## How it differs from siblings

| Method | Where soft prompts go |
|---|---|
| **Prompt tuning** (Lester et al. 2021) | Embedded input only |
| **[[PTuning\|P-Tuning]]** (Liu et al. 2021) | Input layer + small encoder |
| **[[PrefixTuning\|Prefix tuning]]** (Li & Liang 2021) | Every transformer layer |

Prompt tuning is the **simplest** variant — fewest places to modify, fewest parameters.

## The "power of scale" finding

Lester et al.'s key empirical result: **prompt tuning becomes more competitive with [[FullFinetuning|full finetuning]] as the base model gets larger**. At small models, prompt tuning underperforms full FT by a wide margin. At T5-XXL scale, the gap closes.

## Hard vs soft prompts (Ch 7)

| Property | [[HardPrompt\|Hard prompt]] | Soft prompt (this concept) |
|---|---|---|
| Form | Discrete tokens | Continuous vectors |
| Human-readable | Yes | No |
| Trainable | No | Yes (via backprop) |

## Position in PEFT taxonomy

Per Ch 7's analysis of 1,000+ huggingface/peft GitHub issues, prompt tuning is **less popular than [[lora|LoRA]]** but represents a growing subfield for practitioners who want more customization than prompt engineering but less commitment than full LoRA training.

## Connections

- [[PEFT]] — parent family.
- [[PrefixTuning]] / [[PTuning]] — sibling soft-prompt methods.
- [[HardPrompt]] / [[SoftPrompt]] — the underlying distinction.
- [[PromptEngineering]] — the discrete-prompt sibling discipline.
- [[lora|LoRA]] — the dominant alternative PEFT family.
- [[ai-engineering-ch07-finetuning]] — primary source.
