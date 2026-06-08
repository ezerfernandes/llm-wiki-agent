---
title: "Wave Quantization"
type: concept
tags: [gpu, performance, training, cuda, ml-systems, mlsysbook]
sources: [mlsysbook-ch08-model-training]
last_updated: 2026-06-05
---

# Wave Quantization

A GPU performance effect where **batch sizes (and tensor dimensions) that straddle a warp boundary launch additional, partially-filled [[Warp|warps]] that occupy the full step time while doing little useful work** — a hidden "quantization tax." Described in [[mlsysbook-ch08-model-training|mlsysbook Ch 8]] as a reason to treat batch size as quantized rather than continuous.

An NVIDIA GPU executes work in **warps of 32 threads** in lockstep. A batch of 32 uses all 32 lanes; a batch of **33** must launch a second warp that uses only 1/32 (~3%) of its lanes yet takes just as long as the first. So batch 33 launches the same two warps as batch 64 but runs at half the effective utilization — batch 32 is faster than 33, and batch 64 is as fast as 33.

## Key Points

- At cluster scale this becomes a **tail effect**: on an H100 (132 SMs) a workload at 1.01 waves forces the hardware to wait for a nearly-empty final wave before starting the next task.
- Quantified in the chapter: batch 33 → 2 warps, ~52% utilization, ~2× step time of batch 32; batch 65 → 3 warps, repeats at the next boundary.
- **Engineering rule**: choose batch sizes and hidden dimensions that are powers of two or multiples of 8/32/64. This compounds with the [[TensorCore|Tensor Core]] alignment requirement (inputs aligned to multiples of 8/16 for peak throughput).
- Libraries like [[cuDNN]] mitigate by dynamically selecting algorithms per input dimension, but cannot fully hide misaligned shapes.

## Connections

- [[Warp]] — the 32-thread lockstep unit that creates the quantization boundary.
- [[TensorCore]] — the alignment-to-8/16 requirement that compounds the tax.
- [[BatchSize]] — the parameter wave quantization makes effectively discrete.
- [[cuDNN]] — kernel-selection library that partly mitigates the effect.
- [[GPUUtilization]] — the metric wave quantization silently degrades.
- [[mlsysbook-ch08-model-training]] — defining source.
