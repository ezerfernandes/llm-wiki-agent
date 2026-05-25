---
title: "Arithmetic Intensity"
type: concept
tags: [performance, roofline, hardware]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Arithmetic Intensity

**The number of arithmetic operations a workload performs per byte of memory accessed** — the central classifier in the [[RooflineModel|Roofline model]] (Williams et al. 2009). Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Mathematically, an operation can be classified as compute-bound or memory bandwidth-bound based on its arithmetic intensity, which is the number of arithmetic operations per byte of memory access."*

## Why it matters

- **Low arithmetic intensity** → workload is **[[MemoryBandwidthBound|memory bandwidth-bound]]**: each byte you load is reused only a small number of times, so memory bandwidth dominates wall-clock. Typical of LLM [[Decode|decode]] steps.
- **High arithmetic intensity** → workload is **[[ComputeBound|compute-bound]]**: each byte you load is reused many times in arithmetic, so peak FLOP/s dominates. Typical of LLM [[Prefill|prefill]] and image-generation diffusion models.

## Visualization

The Roofline chart (Figure 9-2 in Ch 9) plots achievable throughput on the y-axis vs. arithmetic intensity on the x-axis (both log scale). The "roof" has two slopes:
- Diagonal slope (left) = memory bandwidth ceiling.
- Flat ceiling (right) = peak compute (FLOP/s).

A workload's arithmetic intensity determines which side of the ridge point it sits on — and therefore which optimization lever (more bandwidth vs. more FLOPs) will speed it up.

## NVIDIA Nsight

> *"Profiling tools like NVIDIA Nsight will show you a roofline chart to tell you whether your workload is compute-bound or memory bandwidth-bound."* — Ch 9

Nsight Compute is the de facto NVIDIA-side tool for this.

## Levers that change arithmetic intensity

- **Batching** raises arithmetic intensity (more compute per loaded weight) → can shift a workload from bandwidth-bound to compute-bound. This is why batching usually helps throughput but eventually hits a compute ceiling.
- **[[Quantization|Quantization]]** lowers bytes per parameter → can paradoxically raise arithmetic intensity *or* relieve bandwidth depending on how the quantized values are used.
- **[[FlashAttention]]** restructures attention to reuse on-chip-cached data more times → effectively raises arithmetic intensity by reducing redundant HBM reads.

## Connections

- [[RooflineModel]] — Williams et al. 2009; the cost model arithmetic intensity lives in.
- [[ComputeBound]] / [[MemoryBandwidthBound]] — the two regimes it classifies.
- [[MFU]] / [[MBU]] — the utilization metrics arithmetic intensity helps explain.
- [[Prefill]] / [[Decode]] — the two LLM phases with opposite arithmetic intensity profiles.
- [[FlashAttention]] / [[Quantization]] — techniques that change effective arithmetic intensity.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
