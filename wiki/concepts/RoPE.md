---
title: "Rotary Positional Embeddings (RoPE)"
type: concept
tags: [transformer, positional-encoding, attention]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Rotary Positional Embeddings (RoPE)

A relative-aware [[positionalencoding|positional-encoding]] scheme introduced by Su et al. in *"RoFormer: Enhanced Transformer with rotary position embedding"*. RoPE encodes positional information by **rotating vectors in their embedding space** — capturing absolute and relative token positions simultaneously — and is **applied at the attention step, not at the start of the forward pass**.

## Where it differs from the original Transformer

The original [[1706.03762-attention-is-all-you-need|Transformer]] used **absolute positional embeddings** added to token embeddings once at the bottom of the model, either static (sinusoidal) or learned. RoPE instead **rotates the query and key vectors by an angle proportional to their position** just before the relevance-scoring step inside attention:

> "Instead of the static, absolute embeddings that are added in the beginning of the forward pass, rotary embeddings are a method to encode positional information in a way that captures absolute and relative token position information. It is based on the idea of rotating vectors in their embeddings space. In the forward pass, they are added in the attention step." — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

> "During the attention process, the positional information is mixed in specifically to the queries and keys matrices just before we multiply them for relevance scoring." — Ch 3

The mechanism is **per-layer**: every attention layer's queries and keys receive the rotation, rather than position appearing once at the input.

## Why the move to relative-aware positions

Two practical pressures motivate the move from absolute to RoPE:

1. **[[SequencePacking|Sequence packing]]** during training packs multiple short documents into one fixed-length context. Telling the model that the first token of Document 50 (packed at absolute position 50) is at position 50 misleads it — there is no actual preceding context. Relative-aware encodings sidestep this.
2. **Scale**. *"Some challenges arise from such methods when we scale up models, which requires us to find ways to improve their efficiency."* — Ch 3.

## Deployment

- **[[Phi3Mini|Phi-3-mini]]** — uses `Phi3RotaryEmbedding` (visible in the model print-out from Ch 3).
- **[[Llama|Llama 2]] / [[Llama|Llama 3]]** — RoPE is part of the modern 2024-era block recipe (pre-norm + [[RMSNorm]] + [[SwiGLU]] + [[GroupedQueryAttention|GQA]] + RoPE).

## See also

- [[positionalencoding]] — the umbrella concept; sinusoidal / learned / RoPE alternatives.
- [[SequencePacking]] — the training-time motivation for relative-aware encodings.
- [[selfattention]] / [[multiheadattention]] — the place where RoPE is injected.
- [[transformer]] — the architecture.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
