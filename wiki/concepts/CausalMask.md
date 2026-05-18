---
title: "Causal Mask"
type: concept
tags: [transformer, attention, sequence-models]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Causal Mask

The autoregressive constraint enforced inside a [[Transformer|Transformer]] decoder: attention at position $t$ is forbidden from attending to positions $> t$. Implemented as an additive mask that sets attention logits at future positions to $-\infty$ before the softmax, so their post-softmax weights are zero.

## Why it exists

A language-modeling / decoding-style task generates tokens left to right. At training time the decoder sees the full target sequence in parallel (for [[TeacherForcing|teacher forcing]]), but each position must be predicted using only its left context — otherwise the model would trivially copy the next token. At inference time the future tokens *do not exist* yet. The causal mask enforces this constraint at training so the model learns the same conditional distribution it must use at inference.

## Conceptual continuity with bi-RNN restrictions

The structural reason [[BidirectionalRNN|bi-RNNs]] cannot be used as decoders ([[d2l-recurrent-modern]] §bi-rnn — "no future at inference") generalizes directly: any architecture that lets position $t$ depend on positions $> t$ is unsuitable for autoregressive generation. Causal masking is the Transformer-era mechanism that imposes this restriction while keeping the parallelism advantage of unmasked self-attention.

## See also
- [[Transformer]] — the architecture causal masking is part of.
- [[SelfAttention]] / [[MultiHeadAttention]] — what the mask is applied to.
- [[BidirectionalRNN]] — the RNN-era illustration of the same constraint.
- [[1706.03762-attention-is-all-you-need]] — original Transformer paper introducing the mask.
