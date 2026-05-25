---
title: "Inference with Reference"
type: concept
tags: [inference, decoding, speculative-decoding, optimization]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Inference with Reference

A **[[SpeculativeDecoding|speculative-decoding]] variant in which the draft tokens come from the input context** rather than from a draft model. Introduced in *"Inference with Reference: Lossless Acceleration of Large Language Models"* (Yang et al. 2023) and covered in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]].

## The core idea

> *"Often, a response needs to reference tokens from the input. For example, if you ask your model a question about an attached document, the model might repeat a chunk of text verbatim from the document. Another example is if you ask the model to fix bugs in a piece of code, the model might reuse the majority of the original code with minor changes. Instead of making the model generate these repeated tokens, what if we copy these tokens from the input to speed up the generation?"* — Ch 9

So instead of a small draft model proposing the next K tokens, the algorithm **searches the input context** for a span that matches the current generation state and uses that as the draft.

## How it differs from speculative decoding

| | [[SpeculativeDecoding|Speculative decoding]] | Inference with reference |
|---|---|---|
| Draft source | Small draft model | Spans copied from input context |
| Extra model needed? | Yes | No |
| Best for | Any text | Text with overlap between input and output |
| Implementation | More code | Simpler — just substring search + verification |

## The key algorithmic challenge

> *"The key challenge is to develop an algorithm to identify the most relevant text span from the context at each decoding step. The simplest option is to find a text span that matches the current tokens."* — Ch 9

In practice this is an n-gram matching problem (closely related to [[PromptLookupDecoding]]).

## When it works

> *"Inference with reference doesn't require an extra model. However, it's useful only in generation scenarios where there's a significant overlap between contexts and outputs."* — Ch 9

Three domains where it's effective:
- **Retrieval / [[RAG]] systems** — model quotes retrieved chunks back.
- **Coding** — model edits / refactors existing code.
- **Multi-turn conversations** — model echoes parts of previous turns.

Yang et al. (2023) reports **~2× generation speedup** in such use cases.

## Connections

- [[SpeculativeDecoding]] — the parent technique.
- [[PromptLookupDecoding]] — a close relative; draft tokens from prompt n-grams.
- [[Medusa]] / [[LookaheadDecoding]] — alternative decoding accelerators.
- [[KVCache]] — the prefix structure that inference with reference complements.
- [[RAG]] — a primary use case (output overlaps retrieved context).
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
