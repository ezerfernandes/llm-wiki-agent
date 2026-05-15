---
title: "Recomputation"
type: concept
tags: [systems, training, optimization]
sources: [2205.14135-flashattention]
last_updated: 2026-05-10
---

# Recomputation

A training-time technique that **drops activations during the forward pass and recomputes them during the backward pass** instead of caching them in memory. Trades extra FLOPs for reduced memory footprint — and, on memory-bound workloads, can trade them for reduced wall-clock time.

Originally proposed as **gradient checkpointing** (Chen et al. 2016) to fit larger models in fixed GPU memory by recomputing activations selectively along the network depth. The "every k layers" variant cuts activation memory from O(L) to O(L/√L) at the cost of one extra forward pass.

## In FlashAttention

[[2205.14135-flashattention]] uses recomputation specifically for the attention matrix. Standard attention writes the N×N matrices S = QKᵀ and P = softmax(S) to HBM during the forward pass so the backward can read them. FlashAttention stores only (m, ℓ, O) — Θ(N) auxiliary state — and **recomputes S, P on-chip** from blocks of Q, K, V during the backward.

The net effect:
- More FLOPs in the backward (recompute instead of read).
- Many times fewer HBM accesses.
- Faster backward in wall-clock terms, because attention is memory-bound.

This is the key distinction from prior gradient checkpointing: earlier implementations also recomputed, but only after writing the activations to HBM first — they reduced memory but not HBM traffic. FlashAttention's tiling avoids the write entirely.

## See also
- [[FlashAttention]]
- [[IOComplexity]]
