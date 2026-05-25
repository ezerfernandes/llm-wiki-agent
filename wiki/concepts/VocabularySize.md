---
title: "Vocabulary Size"
type: concept
tags: [nlp, tokenization, llm-engineering]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Vocabulary Size

The **number of distinct tokens** a [[Tokenizer|tokenizer]] can produce — and therefore the number of rows in the language model's [[TokenEmbedding|token-embedding]] matrix.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

> "How many tokens to keep in the tokenizer's vocabulary? (30K and 50K are often used as vocabulary size values, but more and more we're seeing larger sizes like 100K.)" — Ch 2

The chapter's comparative tokenizer tour tabulates vocabulary sizes across model generations:

| Model | Year | Vocabulary size | Tokenization method |
|---|---|---|---|
| [[bert\|BERT-base uncased]] | 2018 | 30,522 | [[WordPiece]] |
| [[bert\|BERT-base cased]] | 2018 | 28,996 | [[WordPiece]] |
| [[GPT2]] | 2019 | 50,257 | [[BPE]] |
| [[FLANT5\|Flan-T5]] | 2022 | 32,100 | [[SentencePiece]] |
| [[Galactica]] | 2022 | 50,000 | [[BPE]] |
| [[GPT4]] | 2023 | ~100,000 | [[BPE]] |
| [[StarCoder2]] | 2024 | 49,152 | [[BPE]] |
| [[Phi3Mini\|Phi-3]] / [[Llama]] 2 | 2023–24 | 32,000 | [[BPE]] |

## Tradeoffs

**Larger vocabularies** mean:
- **Shorter token sequences** (fewer tokens per text) → less context-window pressure, lower latency, lower per-token costs.
- **Larger embedding matrix** (~`vocab_size × embedding_dim`) → more model parameters, more memory.
- **Sparser training signal** per rare token → harder to learn good representations for tail tokens.

**Smaller vocabularies** mean:
- **Longer token sequences** → more compute per text.
- **Better-trained per-token embeddings** for the tokens that do exist (each sees more occurrences).
- **More fall-through to subword-piece composition** for rare words.

The empirical trend post-2022 is **toward larger vocabularies** ([[GPT4|GPT-4]] at ~100K), reversing the earlier 30–50K convention as model designers prioritize context-window economy.

## Connections

- [[Tokenization]] / [[Tokenizer]] — what vocabulary size parameterizes.
- [[BPE]] / [[WordPiece]] / [[SentencePiece]] — the algorithms whose target vocab size this is.
- [[TokenEmbedding]] — the embedding matrix sized by vocabulary size.
- [[ContextLength]] — the resource competing with vocabulary size.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
