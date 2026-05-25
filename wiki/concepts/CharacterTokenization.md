---
title: "Character Tokenization"
type: concept
tags: [nlp, tokenization]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Character Tokenization

[[Tokenization|Tokenization]] scheme where every token in the vocabulary is **one character**. Each text becomes a sequence of single-character tokens.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

> "This is another method that can deal successfully with new words because it has the raw letters to fall back on. While that makes the representation easier to tokenize, it makes the modeling more difficult. Where a model with subword tokenization can represent 'play' as one token, a model using character-level tokens needs to model the information to spell out 'p-l-a-y' in addition to modeling the rest of the sequence." — Ch 2

The chapter's **context-length tradeoff** observation:

> "Subword tokens present an advantage over character tokens in the ability to fit more text within the limited context length of a Transformer model. So with a model with a context length of 1,024, you may be able to fit about three times as much text using subword tokenization than using character tokens (subword tokens often average three characters per token)." — Ch 2

So character tokenization buys **zero OOV failures** at the cost of **3× longer sequences** — usually a bad tradeoff at the scale of modern LLMs, where context length is one of the binding constraints.

## Connections

- [[Tokenization]] — parent.
- [[WordTokenization]] / [[SubwordEmbedding|subword]] / [[ByteLevelTokenization]] — alternatives.
- [[ContextLength]] — the resource character tokenization burns faster.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
