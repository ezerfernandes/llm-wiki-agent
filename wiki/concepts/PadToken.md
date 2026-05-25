---
title: "`[PAD]` Token"
type: concept
tags: [nlp, tokenization, special-token]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# `[PAD]` Token

The **padding** [[SpecialToken|special token]] used to fill unused positions in a model's input batch so that all sequences in the batch have the same length — the input-tensor-rectangularity requirement of GPU-batched Transformer inference. Spelled `[PAD]` in [[bert|BERT]], `<pad>` in [[FLANT5|Flan-T5]] and [[Galactica]].

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

> "A padding token used to pad unused positions in the model's input (as the model expects a certain length of input, its context-size)." — Ch 2 (in the BERT special-tokens enumeration)

## How it works in practice

When a batch contains sequences of lengths 5, 8, and 12, the tokenizer pads the shorter sequences with `[PAD]` to length 12. An **attention mask** (a 0/1 vector of the same length) tells the model which positions to ignore — pad positions get 0 and are masked out of the attention computation so they contribute no gradient and produce no learned representation.

## Connections

- [[SpecialToken]] — parent category.
- Attention mask — the companion mask that tells the model to ignore pad positions (pre-existing wiki convention; see [[Padding]] for the related concept).
- [[bert]] / [[FLANT5]] / [[Galactica]] — models whose tokenizers ship a pad token.
- [[Tokenizer]] / [[Tokenization]] — where pad tokens live.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
