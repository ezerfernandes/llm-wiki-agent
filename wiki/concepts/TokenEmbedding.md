---
title: "Token Embedding"
type: concept
tags: [nlp, embeddings, llm, transformer]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Token Embedding

The **per-token dense vector** that a language model holds for every entry in its [[Tokenizer|tokenizer]]'s vocabulary. The collection of all token embeddings is the **embedding matrix**, of shape `vocab_size × embedding_dim`, and constitutes a substantial fraction of a pretrained model's weights.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

> "The language model holds an embedding vector for each token in the tokenizer's vocabulary. When we download a pretrained language model, a portion of the model is this embeddings matrix holding all of these vectors. Before the beginning of the training process, these vectors are randomly initialized like the rest of the model's weights, but the training process assigns them the values that enable the useful behavior they're trained to perform." — Ch 2

Ch 2's central distinction: token embeddings are **[[StaticEmbedding|static]]** in the sense that they are looked up by ID (every occurrence of the same token ID retrieves the same vector pre-context). The model then **transforms these static input embeddings into [[ContextualEmbedding|contextualized embeddings]]** — one per input position, dependent on surrounding tokens — that downstream layers actually use.

The chapter pairs this with the **tokenizer-model binding** observation: *"a pretrained language model is linked with its tokenizer and can't use a different tokenizer without training"* — because the token-ID-to-embedding-vector mapping is learned jointly.

## Mechanics

For input token IDs `[1, 14350, 385, ...]`:
1. The model performs an embedding-lookup: each ID indexes a row of the embedding matrix.
2. The resulting `seq_len × embedding_dim` tensor is the **input** to the first Transformer block.
3. Subsequent layers produce **[[ContextualEmbedding|contextualized]]** per-position vectors — each token's representation now depends on the whole sequence.

## Dimensions in practice

- [[bert|BERT]]-base: 768 (with 30,522-token vocabulary → ~23M params just for input embeddings).
- [[deberta|DeBERTa v3 xsmall]]: 384 — the dimension of the chapter's `"Hello world"` worked example.
- [[GPT3|GPT-3]] 175B: 12,288.
- [[Llama|Llama 2]] 7B: 4,096.

## Connections

- [[Embedding]] — the parent concept.
- [[StaticEmbedding]] / [[ContextualEmbedding]] — the input-side vs output-side distinction.
- [[WordEmbedding]] — the historical precursor (word2vec-style standalone embeddings).
- [[Tokenizer]] / [[Tokenization]] — the layer that produces the token IDs token embeddings index.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
- [[Word2Vec]] — the simpler model whose entire output is a token-embedding matrix.
