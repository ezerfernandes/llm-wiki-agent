---
title: "State Space Model"
type: concept
tags: [architecture, sequence-models, transformer-alternative, long-context]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# State Space Model

A sequence-modeling architecture family, introduced by **Gu et al. 2021a**, that has shown strong promise for **long-range memory** — a core weakness of transformer architectures. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], SSMs are one of the most credible architectural alternatives to transformers as of 2024.

## Why they matter

Standard [[transformer|Transformer]] self-attention has **O(n²) complexity in sequence length n** and the [[KVCache|KV cache]] grows with the context length. SSMs scale **linearly with sequence length** for inference compute — making them attractive for very long contexts.

## Architectural evolution (Ch 2 timeline)

| Year | Model | Contribution |
|---|---|---|
| 2021 | **S4** (Gu et al., *"Efficiently Modeling Long Sequences with Structured State Spaces"*) | Made SSMs more efficient via structured state matrices. |
| 2022 | **H3** (Fu et al., *"Hungry Hungry Hippos"*) | Added a mechanism to recall early tokens and compare tokens across sequences — analogous to attention but more efficient. |
| 2023 | **[[Mamba]]** (Gu and Dao, *"Mamba: Linear-Time Sequence Modeling with Selective State Spaces"*) | Scaled SSMs to **3B parameters**; matches transformers 2× its size on LM benchmarks; linear inference scaling; works on real data up to million-length sequences. |
| 2024 | **[[Jamba]]** (Lieber et al.) | Hybrid Transformer–Mamba **MoE**, 52B total / 12B active params, fits one 80GB GPU; strong up to 256K context. |

## Position in the broader landscape

Per Ch 2:

> "While transformer-based models are dominating, as of this writing, several alternative architectures are gaining traction."

SSMs sit alongside [[RWKV]] (RNN-based, parallelizable training) as the two most prominent non-transformer architectures cited. Both target the same long-context weakness.

## What SSMs don't solve

> "Modeling long sequences remains a core challenge in developing LLMs. ... [However,] having no context length limitation doesn't guarantee good performance with long context."

Architectural support for long context is necessary but not sufficient.

## Connections
- [[Mamba]] — the 3B-param breakout SSM.
- [[Jamba]] — the hybrid Transformer–Mamba follow-up.
- [[RWKV]] — the parallel-trainable RNN-based alternative.
- [[transformer|Transformer]] — the dominant architecture SSMs aim to replace.
- [[ContextLength]] — the dimension SSMs target.
- [[ai-engineering-ch02-foundation-models]] — primary source.
