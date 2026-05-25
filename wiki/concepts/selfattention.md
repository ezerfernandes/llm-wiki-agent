---
title: "Self-Attention"
type: concept
tags: [attention, mechanism]
sources: [1706.03762-attention-is-all-you-need, d2l-attention-and-transformers, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
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

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1's pedagogical framing: *"self-attention can attend to different positions within a single sequence, thereby more easily and accurately representing the input sequence. Instead of processing one token at a time, it can be used to look at the entire sequence in one go."* The chapter also contrasts encoder self-attention (bidirectional, sees forward + back) with decoder masked self-attention (causal — *"only attend to previous tokens to prevent 'looking into the future'"*) — the same distinction this page formalizes above, in the chapter's intuition-first style.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 walks the self-attention mechanism in **two pedagogical steps**:

1. **Relevance scoring**. *"The relevance scoring step of attention is conducted by multiplying the query vector of the current position with the keys matrix. This produces a score stating how relevant each previous token is. Passing that by a softmax operation normalizes these scores so they sum up to 1."*
2. **Combining information**. *"Now that we have the relevance scores, we multiply the value vector associated with each token by that token's score. Summing up those resulting vectors produces the output of this attention step."*

The chapter is explicit that **three projection matrices** ([[QueryProjection|query]] / [[KeyProjection|key]] / [[ValueProjection|value]]) are the learned attention parameters — each multiplied with the input to produce the per-position Q/K/V vectors that feed into the two-step computation above.

Ch 3 also walks the **autoregressive / causal** framing in concrete pedagogical terms: *"this figure also shows the autoregressive nature of decoder Transformer blocks ... they can only pay attention to previous tokens. Contrast this to BERT, which can pay attention to both sides (hence the B in BERT stands for bidirectional)."* — the same masked-decoder distinction this page formalizes above.

Ch 3's example — *"The dog chased the squirrel because it ___"* — illustrates attention's role: deciding whether *"it"* refers to *the dog* or *the squirrel* requires incorporating context, which is what self-attention does. *"In a trained Transformer LLM, the attention mechanism makes that determination. Attention adds information from the context into the representation of the 'it' token."*
