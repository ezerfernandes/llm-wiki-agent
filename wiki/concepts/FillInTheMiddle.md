---
title: "Fill-in-the-Middle (FIM)"
type: concept
tags: [nlp, code-llm, training-objective, tokenization]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Fill-in-the-Middle (FIM)

A training objective and **inference convention** that lets an [[AutoregressiveLanguageModel|autoregressive]] decoder-only LLM generate a completion conditioned on **both** prefix and suffix context — not just the prefix. Introduced in *"Efficient training of language models to fill in the middle"* (Bavarian et al., [[openai|OpenAI]], 2022).

At training time, training documents are randomly split into three spans — `prefix` | `middle` | `suffix` — and rearranged into the sequence `<fim_prefix> prefix <fim_suffix> suffix <fim_middle> middle <fim_end>`. The model then learns next-token prediction over this rearranged sequence, which means at inference time it can predict the missing `middle` given the surrounding `prefix` and `suffix`.

The mechanism is implemented as **three [[SpecialToken|special tokens]]** in the tokenizer's vocabulary:

| Tokenizer | Prefix token | Middle token | Suffix token | Pad |
|---|---|---|---|---|
| [[GPT4|GPT-4]] | `<\|fim_prefix\|>` | `<\|fim_middle\|>` | `<\|fim_suffix\|>` | — |
| [[StarCoder2]] | `<fim_prefix>` | `<fim_middle>` | `<fim_suffix>` | `<fim_pad>` |

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 names FIM tokens as one of the categories of [[SpecialToken|special tokens]] modern tokenizers add — *"These three tokens enable the LLM to generate a completion given not only the text before it but also considering the text after it."* The chapter notes that exact training details are beyond its scope but flags FIM as the canonical example of a tokenizer-encoded **training-time format** that becomes a runtime API.

## Why it matters for code

The classic autoregressive setup ("given prefix, predict next token") is left-to-right only. Real code completion in an IDE often has surrounding context — the user has placed their cursor inside an existing function, and the LLM should respect what comes after. FIM-trained models like [[StarCoder2]] (and the family of [[GitHubCopilot|GitHub Copilot]]-style code-completion models) handle this natively without needing a separate masked-language-model encoder.

## Connections

- [[SpecialToken]] — FIM tokens are a category of special tokens.
- [[Tokenizer]] / [[Tokenization]] — tokenizer-level mechanism.
- [[GPT4]] / [[StarCoder2]] — the two tokenizers in *Hands-On LLMs* Ch 2 that carry FIM tokens.
- [[AutoregressiveLanguageModel]] — the model class FIM augments.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
