---
title: "Sliding-Window Attention"
type: concept
tags: [attention, efficiency, long-context]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Sliding-Window Attention

A [[LocalAttention|local-attention]] variant that restricts each position's attention to a **fixed-size window of immediately preceding tokens**. Introduced by Beltagy, Peters & Cohan in *"Longformer: The long-document transformer"*, cited by [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] as one of the efficient-attention mechanisms motivated by the cost of full attention as Transformers grew.

## Mechanism

Each token's attention is limited to a sliding window of size `w` over the previous tokens (and, in encoder settings, also forward tokens). This makes attention O(n·w) instead of O(n²) — linear in sequence length for fixed window size.

## Trade-off

- **Saves**: linear-time attention; long sequences become tractable.
- **Costs**: per-block view is bounded by `w` tokens; full receptive field requires stacking layers — depth grows the effective context, similar to how stacked convolutions grow CNN receptive fields.

## See also

- [[LocalAttention]] — the umbrella concept.
- [[FlashAttention]] — the orthogonal IO-side optimization.
- [[transformer]] — the architecture.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
