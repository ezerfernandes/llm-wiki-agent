---
title: "Model Dimension"
type: concept
tags: [transformer, architecture]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Model Dimension

The **size of the per-token vector** flowing through a Transformer LLM. Each [[TokenStream|token stream]]'s input and output vectors share this size; embeddings, residual stream, sublayer inputs and outputs are all `d_model`-dimensional.

> "Each processing stream takes a vector as input and produces a final resulting vector of the same size (often referred to as the model dimension)." — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

## Examples

| Model | d_model |
|---|---|
| Original Transformer (base) | 512 |
| Original Transformer (big) | 1,024 |
| [[Phi3Mini|Phi-3-mini]] | 3,072 |
| [[Llama|Llama 2 / Llama 3]] 7B | 4,096 |
| [[Llama|Llama 2 / Llama 3]] 13B | 5,120 |
| [[Llama|Llama 2 / Llama 3]] 70B | 8,192 |
| [[Llama|Llama 3]] 405B | 16,384 |

(Llama figures from the [[transformer|Transformer page]]'s Ch 2 table.)

## What it determines

- **Embedding matrix size**: `|vocab| × d_model` parameters.
- **Per-block parameters**: roughly `4 × d_model²` from attention projections + `8 × d_model²` from a 4× expansion FFN (these scale as `d_model²`).
- **KV cache memory**: scales with `d_model` (per layer, per head).
- **LM head size**: `d_model × |vocab|`.

## See also

- [[TokenStream]] — the per-position vector carrier this is the size of.
- [[transformer]] — the architecture.
- [[KVCache]] — the cache that scales with `d_model`.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
