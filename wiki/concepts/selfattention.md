---
title: "Self-Attention"
type: concept
tags: [attention, mechanism]
sources: [1706.03762-attention-is-all-you-need, d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Self-Attention

Self-attention (sometimes called *intra-attention*) is an attention mechanism that relates different positions of a single sequence in order to compute a representation of that sequence. Queries, keys, and values all originate from the same input — in contrast to encoder-decoder attention where queries come from the decoder and keys/values from the encoder.

[[1706.03762-attention-is-all-you-need]] is the first sequence transduction model to rely entirely on self-attention, removing recurrence and convolution. Earlier work used self-attention only as one component alongside recurrent networks (e.g. for reading comprehension, abstractive summarization, textual entailment).

## Properties

Compared to recurrent and convolutional layers (Table 1 of [[1706.03762-attention-is-all-you-need]]):

| Layer | Complexity / layer | Sequential ops | Max path length |
|---|---|---|---|
| Self-Attention | O(n²·d) | O(1) | O(1) |
| Recurrent | O(n·d²) | O(n) | O(n) |
| Convolutional | O(k·n·d²) | O(1) | O(log_k n) |
| Self-Attention (restricted) | O(r·n·d) | O(1) | O(n/r) |

Two consequences shape modern LLMs:
- **Parallelism.** O(1) sequential operations means training can fully utilize accelerators within a sequence — the practical win that made very large models trainable.
- **Constant path length.** Any two positions are one attention hop apart, making long-range dependencies easier to learn than in recurrent or strided-convolutional networks.

## Variants

- **Encoder self-attention.** Each position attends to all positions in the previous layer — used in the encoder of the Transformer.
- **Masked (causal) self-attention.** Used in the decoder; positions can only attend to themselves and earlier positions, preserving auto-regressive generation. Implemented by setting masked entries to −∞ before softmax.
- **Restricted self-attention.** A neighborhood of size r; trades coverage for cost on long sequences (max path length becomes O(n/r)). Flagged as future work in the original paper; later realized in efficient-attention literature.

## In practice

Self-attention is implemented as [[ScaledDotProductAttention]] and almost always wrapped in [[MultiHeadAttention]]. The key, query, and value matrices are produced by linear projections of the same input.

A side benefit emphasized by the appendix of [[1706.03762-attention-is-all-you-need]] is **interpretability**: individual attention heads visibly track long-range dependencies (e.g. completing the phrase *making...more difficult*), perform anaphora resolution, and align with syntactic structure.

## See also
- [[Transformer]]
- [[MultiHeadAttention]]
- [[ScaledDotProductAttention]]
