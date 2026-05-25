---
title: "`[UNK]` Token"
type: concept
tags: [nlp, tokenization, special-token]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# `[UNK]` Token

The **unknown** [[SpecialToken|special token]] — the tokenizer's fallback when it encounters a character or word it has no specific encoding for. Spelled `[UNK]` in [[bert|BERT]], `<unk>` in [[FLANT5|Flan-T5]] / [[Galactica]] / similar.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

> "An unknown token that the tokenizer has no specific encoding for." — Ch 2 (in the BERT special-tokens enumeration)

The chapter's worked tour shows **two tokenizers that fail visibly via `[UNK]`** on the contrived test string:

- **BERT uncased** — the 🎵 emoji and the Chinese character 鸟 both become `[UNK]` `[UNK]`. *"The emoji and Chinese characters are gone and replaced with the `[UNK]` special token indicating an 'unknown token.'"*
- **Flan-T5** — same failure: emoji and Chinese chars both become `<unk>` `<unk>`. *"The emoji and Chinese characters are both replaced by the `<unk>` token, making the model completely blind to them."*

By contrast, [[GPT2|GPT-2]] / [[GPT4|GPT-4]] / [[StarCoder2]] / [[Galactica]] / [[Phi3Mini|Phi-3]]'s tokenizers (all [[BPE]] with byte-level fallback) decompose the emoji into multiple representable bytes — no `[UNK]` needed.

## Why `[UNK]` failures matter

When a tokenizer emits `[UNK]`, the model **loses information** about what was originally there. Two practical consequences:

1. The output may reference the `[UNK]` content nonsensically.
2. Round-tripping `decode(encode(x)) != x` — the original character is destroyed; `decode` produces literal `[UNK]` text.

Byte-level / byte-fallback tokenizers eliminate `[UNK]` entirely at the cost of slightly longer sequences.

## Connections

- [[SpecialToken]] — parent category.
- [[ByteLevelTokenization]] — the alternative that avoids `[UNK]` failures.
- [[bert]] / [[FLANT5]] — tokenizers that emit `[UNK]` for emoji / non-Latin chars in Ch 2's demo.
- [[Tokenizer]] / [[Tokenization]] — parent layer.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
