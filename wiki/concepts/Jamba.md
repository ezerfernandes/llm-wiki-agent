---
title: "Jamba"
type: concept
tags: [architecture, state-space-model, transformer-alternative, moe, long-context]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Jamba

A **hybrid Transformer–Mamba [[MixtureOfExperts|MoE]] language model** introduced by **Lieber et al. (2024)** in *"Jamba: A Hybrid Transformer–Mamba Language Model"*. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], Jamba represents the most ambitious attempt to scale [[StateSpaceModel|SSMs]] further by combining the two architectures rather than choosing between them.

## Architecture

Jamba **interleaves blocks of transformer and Mamba layers** rather than picking one. Layered on top is a sparse mixture-of-experts mechanism.

## Scale and efficiency

- **52B total parameters** (the dense-equivalent size).
- **12B active parameters per token** (the inference cost — MoE sparsity).
- Designed to **fit in a single 80GB GPU**.
- Small memory footprint vs vanilla transformers — the key practical advantage.

## Empirical results

- Strong on standard language-model benchmarks.
- Long-context evaluations show competitive performance up to **256K tokens**.

## Why it matters

Jamba is the chapter's strongest argument that SSMs are not just a research curiosity. By combining [[Mamba]]'s linear-time properties with [[transformer|Transformer]] expressivity and MoE sparsity, Jamba demonstrates a viable path to even-longer-context models at production scale.

## Connections
- [[Mamba]] — the SSM half of the hybrid.
- [[transformer|Transformer]] — the other half.
- [[StateSpaceModel]] — broader architecture family.
- [[MixtureOfExperts]] — the sparsity mechanism Jamba combines with the hybrid backbone.
- [[ContextLength]] — Jamba's headline strength.
- [[ai-engineering-ch02-foundation-models]] — primary source.
