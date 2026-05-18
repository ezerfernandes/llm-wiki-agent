---
title: "Queries, Keys, Values (QKV)"
type: concept
tags: [attention, mechanism, foundational]
sources: [d2l-attention-and-transformers, 1706.03762-attention-is-all-you-need]
last_updated: 2026-05-16
---

# Queries, Keys, Values (QKV)

The three-tensor abstraction underneath every [[Attention|attention mechanism]]. By analogy with a classical database — keys $\mathbf{k}_i$ index records, values $\mathbf{v}_i$ are payloads, and a query $\mathbf{q}$ retrieves a payload by some compatibility function with the keys — the [[d2l-attention-and-transformers|D2L attention chapter]] defines attention as:

$$\textrm{Attention}(\mathbf{q}, \mathcal{D}) = \sum_{i=1}^m \alpha(\mathbf{q}, \mathbf{k}_i)\,\mathbf{v}_i$$

over a database $\mathcal{D} = \{(\mathbf{k}_i, \mathbf{v}_i)\}_{i=1}^m$, with scalar attention weights $\alpha$ derived from a [[AttentionScoringFunctions|scoring function]] passed through softmax. This generalizes:

- **Exact key lookup** — one-hot $\alpha$ (the traditional database query).
- **[[AveragePooling|Average pooling]]** — uniform $\alpha_i = 1/m$.
- **Convex-combination retrieval** — softmax of a learned compatibility.

## Where each comes from in a Transformer

- **[[SelfAttention|Self-attention]].** Queries, keys, and values are all linear projections of the *same* input tensor $\mathbf{X}$: $\mathbf{Q} = \mathbf{X}\mathbf{W}^Q$, $\mathbf{K} = \mathbf{X}\mathbf{W}^K$, $\mathbf{V} = \mathbf{X}\mathbf{W}^V$.
- **Encoder–decoder cross-attention.** Queries come from the previous decoder layer; keys and values come from the encoder output. Each decoder position can attend to every source position.
- **[[BahdanauAttention|Bahdanau attention]].** Query = previous decoder state $\mathbf{s}_{t'-1}$; key = value = encoder hidden state $\mathbf{h}_t$.

## See also

- [[Attention]] · [[AttentionPooling]] · [[AttentionScoringFunctions]] · [[ScaledDotProductAttention]] · [[MultiHeadAttention]] · [[SelfAttention]] · [[Transformer]]
