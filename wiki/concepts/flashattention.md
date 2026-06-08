---
title: "FlashAttention"
type: concept
tags: [attention, gpu, systems, kernel, optimization]
sources: [2205.14135-flashattention, hands-on-llm-ch03-looking-inside-llms, ai-engineering-ch09-inference-optimization, mlsysbook-ch08-model-training, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
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

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3's intuition-level framing of the same kernel:

> "Flash Attention is a popular method and implementation that provides significant speedups for both training and inference of Transformer LLMs on GPUs. It speeds up the attention calculation by optimizing what values are loaded and moved between a GPU's shared memory (SRAM) and high bandwidth memory (HBM)." — Ch 3

The chapter cites both *"FlashAttention: Fast and memory-efficient exact attention with IO-awareness"* and the follow-up *"FlashAttention-2: Faster attention with better parallelism and work partitioning"* — the same papers this page treats formally above. *Hands-On LLMs* Ch 3 is the **pedagogical pointer** for readers approaching FlashAttention from an LLM-internals direction rather than the systems / IO-complexity direction.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 places FlashAttention as **the canonical attention-kernel optimization** — one of three buckets in attention-mechanism optimization (alongside "redesign the mechanism" and "optimize the KV cache"):

> *"One of the most well-known kernels optimized for attention computation is FlashAttention (Dao et al., 2022). This kernel fused together many operations commonly used in a transformer-based model to make them run faster."*

Figure 9-13 in Ch 9 shows FlashAttention as the operator-fusion exemplar.

### Hardware specificity

Ch 9 makes the hardware-specificity explicit:

> *"Kernels are optimized for a hardware architecture. This means that whenever a new hardware architecture is introduced, new kernels need to be developed. For example, FlashAttention (Dao et al., 2022) was originally developed primarily for NVIDIA A100 GPUs. Later on, FlashAttention-3 was introduced for H100 GPUs (Shah et al., 2024)."*

This is one of the load-bearing points of the kernel-writing section: **new hardware → new kernels**.

### FlashAttention and operator fusion

Ch 9 names four kernel-writing techniques ([[Vectorization|vectorization]], parallelization, [[LoopTiling|loop tiling]], [[OperatorFusion|operator fusion]]). FlashAttention is the **operator-fusion exemplar** — it fuses Q-K-multiply, softmax, attention-V-multiply (and during backward, the recomputation steps) into a single CUDA kernel.

## From [[mlsysbook-ch08-model-training|mlsysbook Ch 8 (Model Training)]]

Ch 8 uses FlashAttention as the **exemplar of IO-aware algorithm design** — *"an algorithm's runtime is determined not by FLOP count but by memory traffic."* Standard attention materializes the $S{\times}S$ score matrix in HBM (4096-len, 16 heads ≈ 4.0 GB just for scores) and spends 70–80% of attention time waiting on memory; tiling Q/K/V into [[SRAM]] blocks (20+ TB/s, ~10× HBM) with **online softmax** drops memory from $\mathcal{O}(S^2)$ to $\mathcal{O}(S)$ at the same $\mathcal{O}(S^2 d)$ FLOPs, shifting attention from memory-bound to **compute-bound on the [[RooflineModel|roofline]]** for a 2–4× training speedup. The backward pass *recomputes* score/probability blocks rather than reading stored full matrices. The chapter's benchmark table is explicitly illustrative (representative chapter numbers, not verbatim from Dao et al.); the load-bearing pattern is OOM→fits + larger backward-pass gains. Default above 512 tokens, mandatory above 2,048. [[FlashAttention2]] reaches 50–73% of A100 peak; FlashAttention-3 ~740 TFLOP/s (~75% peak) on H100 via FP8.

- [[mlsysbook-ch08-model-training]] — IO-aware design exemplar; roofline regime shift; training-time benchmarks.
- [[RooflineModel]] / [[ArithmeticIntensity]] — the framework that explains *why* tiling helps (memory- → compute-bound).
- [[GradientCheckpointing]] — composes with FlashAttention for 4–8× larger trainable models.
