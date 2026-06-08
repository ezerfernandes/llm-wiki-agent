---
title: "Operator Fusion"
type: concept
tags: [compiler, kernel, optimization, gpu, mlsysbook, serving]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch10-model-compression, mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
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

## The architectural-efficiency lens ([[mlsysbook-ch10-model-compression|mlsysbook Ch 10]])

Ch 10 places operator fusion in its *architectural efficiency* dimension and quantifies it with the canonical **Conv-BN-ReLU** pattern: unfused = 6 memory transfers ($\text{Memory}=2NM$); fused = 2 ($\text{Memory}=2M$) — a 3× transfer reduction, computing batchnorm + ReLU in registers. For a 28×28×256 ResNet-50 layer this is ~50% bandwidth reduction; across the net it cuts kernel launches from 159 → 53 (each ~5–10 µs). Speedup is workload-dependent: element-wise 2–4×, Conv-BN-Act 1.5–2×, GEMM 1.2–1.5×, attention 2–4× ([[flashattention|FlashAttention]] tiling, $\mathcal{O}(S^2)\to\mathcal{O}(S)$). *"The arithmetic is identical; only the memory access pattern changes."* It is the chapter's prototypical Region-1 "free lunch" (no accuracy cost). [[mlsysbook-ch10-model-compression]]

## Connections

- [[FlashAttention]] — canonical operator-fusion kernel.
- [[ModelCompression]] / [[mlsysbook-ch10-model-compression]] — fusion as the architectural-efficiency "free lunch."
- [[Compiler]] / [[Lowering]] — where automatic operator fusion happens.
- [[Kernel]] — what operator fusion produces.
- [[Vectorization]] / [[LoopTiling]] — sibling kernel techniques.
- [[MemoryBandwidthBound]] — the regime operator fusion targets.
- [[kernelfusion]] — adjacent existing concept page.
- [[LayerFusion]] — the serving-runtime framing ([[mlsysbook-ch13-model-serving|Ch 13]]: TensorRT drops ResNet-50 from ~50→~15 kernels).
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
- [[mlsysbook-ch13-model-serving]] — Ch 13 lists operator fusion as "the most potent graph-level optimization" in node-level serving optimization (the static serving graph enables aggressive fusion unsafe during training); 2–5× typical gain on memory-bound layers.
