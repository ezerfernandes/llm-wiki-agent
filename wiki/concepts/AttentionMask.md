---
title: "Attention Mask"
type: concept
tags: [transformers, attention]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Attention Mask

A binary or additive mask applied inside [[scaleddotproductattention]] that zeros out (or sets to -inf) disallowed token interactions — used for padding (variable-length batches) and causal masking (autoregressive decoding). Critical for correct [[transformer]] behavior in both [[BERT]]-style encoders and decoder LMs.
