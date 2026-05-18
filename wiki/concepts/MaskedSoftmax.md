---
title: "Masked Softmax"
type: concept
tags: [attention, engineering]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Masked Softmax

An engineering primitive ubiquitous inside attention layers: a softmax that ignores positions outside a valid-length window. Implemented by **setting masked entries to a large negative constant ($-10^6$) before softmax**, rather than branching with `if/else` — because optimized linear-algebra kernels prefer wasted compute over conditional control flow on GPUs.

```
def masked_softmax(X, valid_lens):
    # X: (batch, queries, keys)
    # Replace positions beyond valid_lens on the last axis with -1e6
    # so their exp() is effectively zero.
    ...
```

[[d2l-attention-and-transformers|D2L]] §attention-scoring-functions introduces this as the canonical pattern for two distinct uses:

- **Padding masks.** Batched sequences are padded to a common length; padding tokens should contribute zero to any attention output. `valid_lens` is a per-example length vector.
- **Causal / autoregressive masks.** Decoder self-attention restricts position $t$ to attend only to positions $\le t$, preserving autoregressiveness. Implemented by a lower-triangular mask of $-\infty$.

The "$-10^6$ instead of $-\infty$" trick avoids NaN gradients from $0 \times \infty$ products.

## See also

- [[AttentionMask]] · [[Softmax]] · [[AttentionPooling]] · [[SelfAttention]] · [[CausalMask]]
