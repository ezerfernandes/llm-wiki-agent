---
title: "Soft Prompt"
type: concept
tags: [peft, soft-prompt, prompt-engineering]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Soft Prompt

A **continuous, trainable vector** prepended to a language model's input or hidden states, used in place of (or alongside) discrete-token prompts. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Soft prompt-based methods modify how the model processes the input by introducing special trainable tokens. These additional tokens are fed into the model alongside the input tokens. They are called soft prompts because, like the inputs (hard prompts), soft prompts also guide the model's behaviors."

## Soft vs hard prompt (Ch 7)

| Property | [[HardPrompt\|Hard prompt]] | Soft prompt |
|---|---|---|
| **Form** | Discrete tokens (`"I"`, `"write"`, `"a"`, `"lot"`) | Continuous vectors (resemble embeddings) |
| **Human-readable** | Yes | No |
| **Trainable** | No (static) | Yes (via backprop) |
| **Interpretable** | Yes | No |
| **Where used** | Standard prompting | [[PrefixTuning]] / [[PTuning]] / [[PromptTuning]] |

## Why they work

Soft prompts can encode richer "instructions" than a comparable number of discrete tokens because they live in a continuous vector space — they're not constrained to existing token embeddings. They can also be **trained per task** while the model itself stays frozen.

## Limitations

- **Not transferable to closed APIs** — providers like [[openai|OpenAI]] don't expose ways to inject continuous vectors at input. Soft prompts only work with open-weight models you can run yourself.
- **Not human-readable** — you can't inspect or edit a learned soft prompt the way you can a hard prompt.
- **Hard to debug** — when a soft prompt underperforms, the only fix is more training; you can't reason about its content.

## Position relative to [[PromptEngineering|prompt engineering]] and [[FineTuning|finetuning]]

> "Some people describe soft prompting as a crossover between prompt engineering and finetuning." — Ch 7

Soft prompts share **prompt engineering's per-task customization** and **finetuning's gradient-based training**. They're a midpoint with characteristic trade-offs.

## Connections

- [[HardPrompt]] — the discrete-token counterpart.
- [[PromptTuning]] / [[PrefixTuning]] / [[PTuning]] — the three methods that use soft prompts.
- [[PEFT]] — parent family.
- [[PromptEngineering]] — the discrete-prompt discipline.
- [[FineTuning]] — the gradient-based parent.
- [[ai-engineering-ch07-finetuning]] — primary source.
