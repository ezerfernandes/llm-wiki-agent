---
title: "FlashAttention"
type: concept
tags: [attention, gpu, systems, kernel, optimization]
sources: [2205.14135-flashattention]
last_updated: 2026-05-10
---

# FlashAttention

An **IO-aware, exact** implementation of softmax attention on GPUs, introduced in [[2205.14135-flashattention]] (Dao, Fu, Ermon, Rudra & Ré, 2022). FlashAttention computes the same `softmax(QKᵀ/√d)·V` as standard attention but never materializes the N×N attention matrix in HBM. The result is a single fused CUDA kernel that is **simultaneously faster and lower-memory** than the standard PyTorch implementation — without changing what the model computes.

## Two ideas

1. **Tiling.** Split Q, K, V into row/column blocks that fit on-chip SRAM. Compute partial softmax statistics (`m_i` running max, `ℓ_i` running normalizer) per block and rescale-and-accumulate the output incrementally. The full N×N matrix is never assembled.
2. **Recomputation.** Drop the standard practice of writing S, P ∈ ℝ^{N×N} to HBM for the backward pass. Save only (m, ℓ, O) — Θ(N) — and **recompute** S, P on-chip from blocks of Q, K, V during the backward. Trades FLOPs for HBM bandwidth; net wall-clock win because attention is memory-bound.

## IO complexity

Standard attention: Θ(Nd + N²) HBM accesses.
FlashAttention: Θ(N²d²M⁻¹) HBM accesses, where M is on-chip SRAM size.

For typical d (64–128) and M (~100 KB on A100), d²/M ≪ 1, so FlashAttention does **many times fewer** HBM accesses than the standard implementation. [[2205.14135-flashattention]] also proves a matching lower bound: Θ(N²d²M⁻¹) is asymptotically optimal among exact attention algorithms.

See [[IOComplexity]] for the cost model.

## Why it matters to the wiki

- **Default attention kernel.** FlashAttention (and its successors FlashAttention-2 / -3) is the de-facto attention implementation behind essentially every modern Transformer training and inference stack. The [[Transformer]] architecture page treats FlashAttention as the canonical implementation.
- **Long context becomes affordable.** [[2205.14135-flashattention]] is the first Transformer to beat chance on Path-X (16K) and Path-256 (64K) — and the speed dividend is what enables every long-context LLM in the wiki (the 2026 papers' agentic harnesses, [[2604.28181-synthetic-computers-at-scale]]'s 8h/2000-turn simulations, etc., presuppose attention that scales).
- **Exactness.** FlashAttention is **exact**, not approximate; it does not compete with model-quality interventions (RL recipes, pretraining changes) in the rest of the wiki. It is a pure systems result that those interventions stack on top of.

## Extensions

- **Block-sparse FlashAttention** (this paper): adds a block-sparsity mask; IO scales by the sparsity ratio. Faster than every approximate-attention baseline tested; scales to 64K.
- **FlashAttention-2** (Dao 2023): better parallelism and work partitioning across thread blocks; ~2× over v1.
- **FlashAttention-3** (Shah et al. 2024): Hopper-specific (H100) kernels using async/TMA and FP8 paths.

## See also
- [[IOComplexity]]
- [[KernelFusion]]
- [[GpuMemoryHierarchy]]
- [[Recomputation]]
- [[Transformer]]
- [[SelfAttention]]
