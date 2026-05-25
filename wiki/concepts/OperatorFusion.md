---
title: "Operator Fusion"
type: concept
tags: [compiler, kernel, optimization, gpu]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Operator Fusion

**Combining multiple operators into a single kernel pass to avoid redundant memory access.** One of four kernel-writing techniques named in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Combine multiple operators into a single pass to avoid redundant memory access. For example, if two loops operate over the same array, they can be fused into one, reducing the number of times data is read and written."*

## Why fusion matters more than the others

Three of Ch 9's four kernel techniques ([[Vectorization|vectorization]], parallelization, [[LoopTiling|loop tiling]]) apply broadly:

> *"While vectorization, parallelization, and loop tiling can be applied broadly across different models, operator fusion requires a deeper understanding of a model's specific operators and architecture. As a result, operator fusion demands more attention from optimization engineers."*

Operator fusion's payoff is large because each fused pass eliminates **memory traffic** — and modern accelerators are typically [[MemoryBandwidthBound|memory-bandwidth-bound]] for many workloads. Removing one HBM round-trip per token per layer compounds quickly.

## Canonical example: FlashAttention

[[FlashAttention]] (Dao et al. 2022) is the most famous operator-fusion kernel: it fuses the attention computation (QK, softmax, attention × V) into a single CUDA kernel, never materializing the N×N attention matrix in HBM.

Ch 9's Figure 9-13 explicitly shows FlashAttention as the *"kernel that fuses together several common operators."*

## Compiler-driven fusion

[[Compiler|ML compilers]] perform operator fusion automatically as part of [[Lowering|lowering]]:
- `torch.compile` fuses many elementwise + reduction ops into Triton kernels.
- [[XLA]] is famous for aggressive operator fusion (especially on TPU).
- [[TVM]] / [[MLIR]] expose fusion as a pluggable pass.

But hand-fused kernels for "hot" workloads (attention, matmul) often still outperform compiler-emitted ones — the prize for operator-fusion expertise.

## Connections

- [[FlashAttention]] — canonical operator-fusion kernel.
- [[Compiler]] / [[Lowering]] — where automatic operator fusion happens.
- [[Kernel]] — what operator fusion produces.
- [[Vectorization]] / [[LoopTiling]] — sibling kernel techniques.
- [[MemoryBandwidthBound]] — the regime operator fusion targets.
- [[kernelfusion]] — adjacent existing concept page.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
