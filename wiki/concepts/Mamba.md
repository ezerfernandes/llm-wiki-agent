---
title: "Mamba"
type: concept
tags: [architecture, state-space-model, transformer-alternative, long-context]
sources: [ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Mamba

A [[StateSpaceModel|state-space-model]] LLM introduced by **Gu and Dao (2023)** in *"Mamba: Linear-Time Sequence Modeling with Selective State Spaces"*. The first SSM to scale to **3 billion parameters** and match transformer performance at meaningful scale. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], Mamba is the architectural-alternative result that most clearly demonstrated SSMs are a viable competitor to transformers for language modeling.

## Headline results

- **Mamba-3B outperforms transformers of the same size** on language modeling.
- **Matches transformers 2× its size** (i.e. ≈6B-param transformers).
- **Linear inference scaling** with sequence length, vs **quadratic for transformers**.
- Real-data performance keeps improving up to **million-length sequences**.

## What makes it different from earlier SSMs

Per Ch 2's brief lineage, Mamba's selective-state-space mechanism extends prior SSM work (S4, H3) with input-dependent state transitions — letting the model selectively retain or forget information based on the current token, somewhat analogous to attention but in linear time.

## What it doesn't solve

> "Modeling long sequences remains a core challenge in developing LLMs. An architecture that has shown a lot of promise in long-range memory is SSMs (state space models). ... However, in practice, having no context length limitation doesn't guarantee good performance with long context." — Ch 2

Linear-scaling inference is *necessary* but not *sufficient* for strong long-context performance.

## Follow-up: [[Jamba]]

Lieber et al. (2024) introduced **[[Jamba]]** — a hybrid Transformer–Mamba MoE that interleaves Transformer and Mamba layers to scale SSMs further. 52B total / 12B active params, fits a single 80GB GPU, strong on 256K-context benchmarks.

## Connections
- [[StateSpaceModel]] — parent architecture family.
- [[Jamba]] — the hybrid Transformer–Mamba successor.
- [[RWKV]] — peer transformer-alternative.
- [[transformer|Transformer]] — the dominant architecture Mamba competes with.
- [[ContextLength]] — Mamba's main advantage.
- [[ai-engineering-ch02-foundation-models]] — primary source.

## In *Hands-On LLMs* Ch 1

[[hands-on-llm-ch01-introduction-to-llms|Ch 1]] cites Mamba (Gu & Dao, 2023, *"Mamba: Linear-Time Sequence Modeling with Selective State Spaces"*, arXiv:2312.00752) as one of two prominent 2023-era Transformer alternatives (alongside [[RWKV]]):

> "Apart from the widely popular Transformer architecture, new promising architectures have emerged such as Mamba and RWKV. These novel architectures attempt to reach Transformer-level performance with additional advantages, like larger context windows or faster inference." — Ch 1

The chapter also references the [[MaartenGrootendorst|Maarten Grootendorst]]'s own *"A Visual Guide to Mamba and State Space Models"* explainer (Ch 1, footnote 12) — the co-author's published walkthrough that pairs with the textual citation.
