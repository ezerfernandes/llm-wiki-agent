---
title: "Prefix Tuning"
type: concept
tags: [prompt-tuning, peft, gradient-based]
sources: [2406.11695-mipro, ai-engineering-ch07-finetuning]
last_updated: 2026-05-23
---

# Prefix Tuning

Li & Liang (ACL 2021, arXiv:2101.00190). **Gradient-based prompt tuning** — prepend learnable continuous *prefix* vectors to the LM's hidden states at each layer; train these vectors via gradient descent while freezing the LM's weights. A parameter-efficient fine-tuning (PEFT) technique.

## Why it doesn't apply to LM programs

The [[2406.11695-mipro|MIPRO paper]] explicitly rules out prefix tuning and similar gradient-based prompt-tuning methods (e.g. [[AutoPrompt]]) as **inapplicable to LM-program optimization** because:

> *"We assume no access to the gradients or embeddings of the LMs involved, which rules out many RL and prompt-tuning algorithms (Zhang et al., 2022; Li and Liang, 2021; Shin et al., 2020). In addition, system designers generally have small datasets $\mathcal{D}$ and small budgets of LM calls for evaluating $\Phi$."*

That is, LM-program prompt optimization is a **black-box optimization** problem in the modern API-only LM regime; prefix tuning needs log-probs / gradients that commodified LM APIs no longer expose.

## Connections

- [[PromptOptimization]] — the parent task; prefix tuning is the gradient-based variant.
- [[AutoPrompt]] — sibling gradient-based prompt-tuning method.
- [[2406.11695-mipro|MIPRO]] — the wiki's reference paper for why prefix-tuning is excluded in the LM-program setting.
- PEFT — parameter-efficient fine-tuning family.
- [[lora|LoRA]] — alternative PEFT method that operates on weight-space rather than prompt-space.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

[[ChipHuyen|Huyen]]'s Ch 7 places prefix tuning inside the **[[SoftPrompt|soft-prompt-based]] PEFT family** — methods that don't add weight-space parameters but instead inject *learnable continuous prompt vectors* into the forward pass. The chapter names three confusable siblings:

- **[[PrefixTuning|Prefix tuning]]** (Li & Liang, 2021) — prepends soft-prompt tokens to the input **at every transformer layer**.
- **[[PTuning|P-Tuning]]** (Liu et al., 2021) — prepends soft-prompts at the input layer only (with a small encoder LSTM/MLP to produce them).
- **[[PromptTuning|Prompt tuning]]** (Lester et al., 2021) — prepends soft-prompts to the **embedded input only**, simplest variant.

Huyen's analysis of 1,000+ `huggingface/peft` issues finds soft-prompt methods are **less popular than [[lora|LoRA]]** but are growing — they appeal to practitioners who want more customization than prompt engineering but less commitment than full LoRA finetuning. The chapter's footnote: *"I've never met a single person who could explain to me, on the spot, the differences between these techniques."*

### Soft vs. hard prompts (Ch 7)

| Property | [[HardPrompt\|Hard prompt]] | [[SoftPrompt\|Soft prompt]] |
|---|---|---|
| Form | Discrete tokens ("I", "write", "a") | Continuous vectors |
| Human-readable | Yes | No |
| Trainable | No (static) | Yes (via backprop) |

The Ch 7 framing: *"Some people describe soft prompting as a crossover between prompt engineering and finetuning."*
