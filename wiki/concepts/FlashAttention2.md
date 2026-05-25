---
title: "FlashAttention-2"
type: concept
tags: [llm-engineering, attention, gpu]
sources: [leh-ch08-inference-optimization, hands-on-llm-ch03-looking-inside-llms, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

## Definition
Tri Dao's 2023 sequel to FlashAttention; SRAM-tiled attention with online softmax.

## In LLM Engineer's Handbook
FlashAttention-2 (2023 sequel by [[TriDao]] to the original [[flashattention]] kernel) retains the SRAM-tiled exact-attention design and online softmax — block-by-block softmax statistics with running max and running normalizer to avoid materializing the N x N attention matrix in HBM — and improves parallelism for ~2x throughput over v1. Requires the `flash-attn` package. Supported by [[TGI]], [[vLLM]], and [[TensorRTLLM]].

## In *Hands-On LLMs* Ch 3
[[hands-on-llm-ch03-looking-inside-llms|Ch 3]] cites both *"FlashAttention: Fast and memory-efficient exact attention with IO-awareness"* and *"FlashAttention-2: Faster attention with better parallelism and work partitioning"* as the canonical references for the IO-aware attention kernel that *"provides significant speedups for both training and inference of Transformer LLMs on GPUs."*

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 contextualizes FlashAttention-2 by emphasizing the **hardware-specific lifecycle** of kernels:

> *"Kernels are optimized for a hardware architecture. This means that whenever a new hardware architecture is introduced, new kernels need to be developed. For example, FlashAttention (Dao et al., 2022) was originally developed primarily for NVIDIA A100 GPUs. Later on, FlashAttention-3 was introduced for H100 GPUs (Shah et al., 2024)."*

So the FlashAttention lineage from Ch 9's view:
- **v1** (Dao 2022) — A100 era; introduced the IO-aware tiling.
- **v2** (Dao 2023) — better parallelism / work partitioning.
- **v3** (Shah et al. 2024) — Hopper H100 (FP8, async + TMA paths).

Each generation re-targets the kernel to a specific hardware architecture's memory hierarchy and compute units — the canonical example of why kernel writing is hardware-dependent.
