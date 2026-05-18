---
title: "Multi-Head Attention"
type: concept
tags: [attention, mechanism]
sources: [1706.03762-attention-is-all-you-need, d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Multi-Head Attention

Multi-head attention runs several attention functions in parallel on different learned linear projections of the queries, keys, and values, then concatenates and projects the results. Introduced in [[1706.03762-attention-is-all-you-need]] (§3.2.2) as the attention block used everywhere in the [[Transformer]].

## Definition

```
MultiHead(Q, K, V) = Concat(head_1, …, head_h) Wᴼ
where head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)
```

with parameter matrices `W_i^Q ∈ ℝ^(d_model × d_k)`, `W_i^K ∈ ℝ^(d_model × d_k)`, `W_i^V ∈ ℝ^(d_model × d_v)`, and `Wᴼ ∈ ℝ^(h·d_v × d_model)`. The attention function used in each head is [[ScaledDotProductAttention]].

The original paper uses h = 8, with d_k = d_v = d_model / h = 64. Because each head runs at reduced dimensionality, total compute is similar to one full-dimensional attention head.

## Why multiple heads

> "Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this." — [[1706.03762-attention-is-all-you-need]]

The ablation (Table 3 row A) shows single-head attention is 0.9 BLEU worse than h=8; quality also drops with too many heads (h=32). Reducing d_k (Table 3 row B) hurts quality, suggesting "compatibility is not easy and a more sophisticated compatibility function than dot product may be beneficial."

The appendix visualizations show different heads specializing — some track long-distance dependencies, others perform anaphora resolution, others mirror syntactic structure.

## Three uses in the Transformer

1. **Encoder-decoder attention.** Queries from the previous decoder layer; keys and values from the encoder output. Lets every decoder position attend over all encoder positions — replacing the bottleneck attention of older seq2seq models.
2. **Encoder self-attention.** Queries, keys, values all from the previous encoder layer.
3. **Masked decoder self-attention.** Queries, keys, values from the previous decoder layer, with future positions masked to −∞ before softmax to preserve the auto-regressive property.

## See also
- [[Transformer]]
- [[SelfAttention]]
- [[ScaledDotProductAttention]]
