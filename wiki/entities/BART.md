---
title: "BART"
type: entity
tags: [cs324, llm]
sources: [cs324-modeling, cs324-training]
last_updated: 2026-06-04
---

BART (Lewis et al. 2019) is a Facebook encoder-decoder denoising sequence-to-sequence model. It is pretrained by corrupting input text — using token masking and sentence permutation, among other noise functions — and learning to reconstruct the original, making it effective for generation and comprehension tasks.

## Connections
- [[Transformer]] — BART is a Transformer encoder-decoder
- [[T5]] — related text-to-text denoising seq2seq model
- [[cs324-modeling]] — discussed in this CS324 lecture
- [[cs324-training]] — discussed in this CS324 lecture
