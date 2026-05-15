---
title: "Scaled Dot-Product Attention"
type: concept
tags: [attention, mechanism]
sources: [1706.03762-attention-is-all-you-need]
last_updated: 2026-05-10
---

# Scaled Dot-Product Attention

The specific attention function used inside [[MultiHeadAttention]] in the [[Transformer]]. Defined in §3.2.1 of [[1706.03762-attention-is-all-you-need]]:

```
Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V
```

where Q (queries) and K (keys) have dimension d_k, and V (values) has dimension d_v. In matrix form, Q, K, V are batched stacks of vectors and the operation runs over all queries simultaneously.

## The scaling factor

Dot-product attention is the same as multiplicative attention except for the 1/√d_k scaling. The paper motivates the scale via the variance of the dot product:

> "To illustrate why the dot products get large, assume that the components of q and k are independent random variables with mean 0 and variance 1. Then their dot product, q·k = Σ qᵢkᵢ, has mean 0 and variance d_k."

When d_k is large, raw dot products grow in magnitude and push softmax into low-gradient regions. Dividing by √d_k normalizes the variance back to 1 and keeps softmax in a well-conditioned regime.

## Comparison to additive attention

The two most common attention compatibility functions are:

- **Additive (Bahdanau)** — uses a feed-forward network with a single hidden layer.
- **Dot-product (multiplicative)** — what we use here, plus the 1/√d_k scaling.

They have similar theoretical complexity, but dot-product attention is "much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code." Without scaling, additive attention outperforms dot-product attention for large d_k; the scaling factor closes that gap.

## Masking

When used in the decoder, illegal connections (queries attending to future positions) are zeroed by setting their pre-softmax values to −∞ — preserving the auto-regressive property. See [[SelfAttention]] for the masked variant.

## See also
- [[Transformer]]
- [[MultiHeadAttention]]
- [[SelfAttention]]
