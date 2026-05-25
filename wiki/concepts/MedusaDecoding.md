---
title: "Medusa Decoding"
type: concept
tags: [inference, decoding, parallel-decoding, attention, optimization]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Medusa Decoding

**A [[ParallelDecoding|parallel-decoding]] technique in which the base model is extended with multiple decoding heads, each trained to predict a token at a specific future position; their candidates are verified via tree-based attention.** Introduced by Cai et al. (2024) in *Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads* — see also the [[Medusa]] page. Covered in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]].

## Architecture

> *"In Medusa, the original model is extended with multiple decoding heads, and each head is a small neural network layer that is then trained to predict a future token at a specific position. If the original model is trained to predict the next token xₜ₊₁, the kth head will predict the token xₜ₊ₖ₊₁."* — Ch 9

The original model is **frozen**; only the heads are trained.

## Verification: tree-based attention

> *"Medusa uses a tree-based attention mechanism to verify and integrate tokens. Each Medusa head produces several options for each position. These options are then organized into a tree-like structure to select the most promising combination."* — Ch 9

This contrasts with [[LookaheadDecoding|Lookahead's]] Jacobi-method verification (iterative regeneration of failed tokens).

## Performance number

> *"NVIDIA claimed Medusa helped boost Llama 3.1 token generation by up to 1.9× on their HGX H200 GPUs."* — Ch 9 (Eassa et al. 2024)

## Medusa-1 vs Medusa-2

The earlier wiki [[Medusa|Medusa]] page (from LLM Engineer's Handbook) notes:
- **Medusa-1** — fine-tunes only the speculation heads (base frozen).
- **Medusa-2** — jointly fine-tunes heads + base.

Both are supported by TGI.

## Trade-offs

> *"While the perspective of being able to circumvent sequential dependency is appealing, parallel decoding is not intuitive, and some techniques, like Medusa, can be challenging to implement."* — Ch 9

The implementation complexity is the main objection — head training, tree-attention machinery, and the verification path are all extra work.

## Connections

- [[Medusa]] — the existing wiki page (LLM Engineer's Handbook treatment).
- [[ParallelDecoding]] — parent family.
- [[LookaheadDecoding]] / [[JacobiDecoding]] — sibling parallel-decoding techniques.
- [[SpeculativeDecoding]] — alternative family.
- [[Attention]] — the mechanism Medusa's tree-attention specializes.
- [[Decode]] — the bottleneck Medusa addresses.
- [[Llama|Llama 3.1]] — the model NVIDIA tested Medusa on.
- [[NVIDIA]] — the source of the H200 number.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
