---
title: "Hard Prompt"
type: concept
tags: [prompt-engineering, peft-adjacent]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Hard Prompt

The **standard discrete-token prompt** — what's normally meant by "prompt" in prompt engineering. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], named as the counterpart to [[SoftPrompt|soft prompts]]:

> "Hard prompts are human-readable. They typically contain discrete tokens such as 'I', 'write', 'a', and 'lot'. ... Hard prompts are static and not trainable."

## What it is

A sequence of tokens from the model's vocabulary — exactly what users type into a chat interface or what an application sends to an LLM API. Examples:

- `"You are a helpful assistant."` (system prompt)
- `"Summarize the following article in 3 sentences."` (instruction)
- `"Q: What is 2+2?\nA: 4\nQ: What is 3+5?\nA:"` (few-shot)

## Why "hard"

The term was coined retroactively after [[SoftPrompt|soft prompts]] emerged — "hard" because the tokens are **fixed**, **discrete**, and **non-trainable** by backprop (you can't differentiate the loss w.r.t. token IDs).

## How hard and soft prompts combine

Per Ch 7: hard and soft prompts can be used together. Models that support PEFT-style soft prompts typically prepend them to the embedded form of the user's hard prompt, so the model sees `[soft_prompt_vectors] + [hard_prompt_embeddings] + [generated_tokens]`.

## Connections

- [[SoftPrompt]] — the trainable counterpart.
- [[PromptEngineering]] — the discipline of authoring hard prompts.
- [[PromptTuning]] / [[PrefixTuning]] / [[PTuning]] — methods that use soft prompts.
- [[ai-engineering-ch07-finetuning]] — primary source.
