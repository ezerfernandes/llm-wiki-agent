---
title: "Mixtral 8x7B"
type: entity
tags: [model, llm, mistral, moe, open-weights]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Mixtral 8x7B

[[Mistral|Mistral]]'s **mixture-of-experts language model** — 8 experts × 7B parameters per expert. The canonical worked example in [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]'s discussion of [[MixtureOfExperts|MoE]] sparsity and **why parameter count alone is misleading**.

## The parameter-count arithmetic (Ch 2)

| Counting | Total |
|---|---|
| Naive (8 × 7B) | 56B |
| **Actual** (after shared parameters) | **46.7B** |
| **Active per token** (at each layer, only 2 experts active) | **12.9B** |

> "While this model has 46.7 billion parameters, its cost and speed are the same as a 12.9-billion-parameter model." — Ch 2

## Why this matters

Mixtral 8x7B is **the textbook case for why "how big is the model?" is a malformed question for [[MixtureOfExperts|MoE]] models**:
- Naive count overstates (8 × 7B ≠ actual count due to shared params).
- Total count overstates the inference cost (only 12.9B active at any moment).
- The 46.7B vs 12.9B gap is exactly the MoE sparsity advantage.

## Tokenization detail (cross-referenced)

Per [[ai-engineering-ch01-intro|Ch 1]]: Mixtral 8x7B vocabulary = **32,000 tokens** — vs [[GPT4|GPT-4]]'s 100,256. The smaller vocabulary is one of several factors making Mixtral cheaper to operate.

## Connections
- [[Mistral|Mistral]] — the builder.
- [[MixtureOfExperts]] — the architecture.
- [[FoundationModel]] / [[LargeLanguageModel]] — broader categories.
- [[Jamba]] — peer hybrid-MoE architecture (Transformer + Mamba + MoE).
- [[Tokenization]] — vocabulary-size context.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[ai-engineering-ch01-intro]] — vocabulary cross-reference.
