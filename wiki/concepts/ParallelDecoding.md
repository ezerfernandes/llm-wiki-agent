---
title: "Parallel Decoding"
type: concept
tags: [inference, decoding, optimization, autoregressive]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Parallel Decoding

**Generating multiple future tokens simultaneously**, breaking the sequential autoregressive dependency. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Instead of making autoregressive generation faster with draft tokens, some techniques aim to break the sequential dependency. Given an existing sequence of tokens x₁, x₂,…,xₜ, these techniques attempt to generate xₜ₊₁, xₜ₊₂,…,xₜ₊ₖ simultaneously. This means that the model generates xₜ₊₂ before it knows that the token before it is xₜ₊₁."*

## Why it works

> *"This can work because the knowledge of the existing sequence often is sufficient to predict the next few tokens. For example, given 'the cat sits', without knowing that the next token is 'on', 'under', or 'behind', you might still predict that the word after it is 'the'."* — Ch 9

The intuition: language has enough redundancy that K positions can sometimes be predicted in parallel from the same prefix, with subsequent verification catching cases where they don't fit together.

## The two principal techniques

| Technique | Mechanism | Verification |
|---|---|---|
| **[[LookaheadDecoding|Lookahead decoding]]** (Fu et al. 2024) | Same decoder generates K parallel tokens | [[JacobiAlgorithm|Jacobi method]] iteratively regenerates failed tokens (a.k.a. [[JacobiDecoding]]) |
| **[[Medusa|Medusa]]** (Cai et al. 2024) | Multiple decoding heads, each trained to predict a future position | Tree-based attention over per-head options |

### Lookahead decoding (Jacobi)

1. K future tokens are generated in parallel.
2. These K tokens are verified for coherence/consistency with context.
3. If one or more tokens fail, only the failed tokens are regenerated.
4. Refine until all pass verification.

This is the Jacobi iterative-update pattern: multiple parts of a solution updated simultaneously and independently.

### Medusa (multi-head)

Each Medusa head is a small neural network layer attached to the model that predicts a *specific future position*. If the original model predicts token `xₜ₊₁`, head `k` predicts `xₜ₊ₖ₊₁`. Heads train alongside (the base is frozen). At inference, each head produces several candidates per position; a tree-based attention mechanism picks the most promising sequence.

NVIDIA reported Medusa boosting Llama 3.1 token generation by **up to 1.9× on HGX H200 GPUs** (Eassa et al. 2024).

## Trade-off vs speculative decoding

| | [[SpeculativeDecoding]] | Parallel decoding |
|---|---|---|
| Token order | Sequential (draft model generates left-to-right) | Parallel (positions K independently) |
| Architectural change | Optional (draft model can be separate) | Yes (Medusa heads / Jacobi setup) |
| Implementation difficulty | Easy (~50 lines PyTorch) | Higher (especially Medusa) |
| Cleanest implementation | Drop-in for most models | Requires retraining heads (Medusa) or extra inference machinery (Lookahead) |

Ch 9's assessment:

> *"While the perspective of being able to circumvent sequential dependency is appealing, parallel decoding is not intuitive, and some techniques, like Medusa, can be challenging to implement."*

## Connections

- [[SpeculativeDecoding]] — the alternative family of decoding accelerators.
- [[LookaheadDecoding]] / [[JacobiDecoding]] — Jacobi-method-based parallel decoding.
- [[Medusa]] / [[MedusaDecoding]] — multi-head parallel decoding.
- [[JacobiAlgorithm]] — the iterative numerical method behind lookahead decoding.
- [[Decode]] — the sequential phase parallel decoding tries to circumvent.
- [[KVCache]] — the structure all decoding accelerators touch.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
