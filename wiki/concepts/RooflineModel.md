---
title: "Roofline Model"
type: concept
tags: [performance, hardware, parallel-computing]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Roofline Model

A **hardware-performance cost model** introduced by Williams, Waterman, and Patterson (2009) that classifies a workload as **[[ComputeBound|compute-bound]]** or **[[MemoryBandwidthBound|memory bandwidth-bound]]** based on its **[[ArithmeticIntensity|arithmetic intensity]]** (operations per byte of memory access). Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"The concepts of compute-bound or memory bandwidth-bound were introduced in the paper 'Roofline' (Williams et al., 2009). Mathematically, an operation can be classified as compute-bound or memory bandwidth-bound based on its arithmetic intensity, which is the number of arithmetic operations per byte of memory access."*

## The chart

The roofline chart plots **achievable throughput (y, log scale)** against **arithmetic intensity (x, log scale)**, and consists of two "rooflines":

- **Diagonal "roof"** (left side): the peak memory bandwidth × arithmetic intensity ceiling — the maximum throughput you can achieve given bandwidth alone.
- **Flat "roof"** (right side): the peak compute (FLOP/s) ceiling — the absolute maximum throughput the chip can produce.

The intersection (the "ridge point") separates bandwidth-bound (left) from compute-bound (right). The chart is so named because it resembles a roof.

## Why it matters for AI inference

- **LLM [[Prefill|prefill]]** sits to the right of the ridge → compute-bound. Solution: more FLOPs.
- **LLM [[Decode|decode]]** sits to the left of the ridge → memory bandwidth-bound. Solution: more bandwidth, smaller KV cache, lower-precision weights, or restructured attention.

Knowing which side you're on tells you which optimization lever to pull. The roofline diagnoses *whether the workload is the problem* before you blame the hardware.

## Tooling

> *"Profiling tools like NVIDIA Nsight will show you a roofline chart to tell you whether your workload is compute-bound or memory bandwidth-bound."* — Ch 9

NVIDIA Nsight Compute generates roofline charts automatically for CUDA kernels. Most AI compilers / profilers ([[XLA]], [[torch.compile]] traces) can also be coerced into producing one.

## Terminology note

The original Roofline paper uses *memory-bound* to mean *memory-bandwidth-bound* — same as Ch 9's preferred usage. The AI-engineer-popular sense of *memory-bound* (capacity, i.e. OOM) is *not* the Roofline sense.

## Connections

- [[ArithmeticIntensity]] — the x-axis of the chart.
- [[ComputeBound]] / [[MemoryBandwidthBound]] — the two regimes.
- [[MFU]] / [[MBU]] — utilization metrics derived from the same conceptual framework.
- [[Prefill]] / [[Decode]] — the two LLM phases the roofline separates.
- [[InferenceOptimization]] — the discipline this model serves.
- [[GPU]] / [[HBM]] / [[SRAM]] — the memory hierarchy whose bandwidths feed the chart's roofs.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
