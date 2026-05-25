---
title: "MBU (Model Bandwidth Utilization)"
type: concept
tags: [inference, performance, metrics, gpu, memory]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# MBU — Model Bandwidth Utilization

**The percentage of a chip's peak memory bandwidth that's actually being used.** The bandwidth-side companion to [[MFU]]; especially useful for [[MemoryBandwidthBound|memory-bandwidth-bound]] workloads like LLM [[Decode|decode]]. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"MBU (Model Bandwidth Utilization) measures the percentage of achievable memory bandwidth used. If the chip's peak bandwidth is 1 TB/s and your inference uses only 500 GB/s, your MBU is 50%."*

## Formula

For a [[Decode|decoding]] step:

```
bandwidth used = parameter count × bytes/param × tokens/s
MBU            = (parameter count × bytes/param × tokens/s) / theoretical bandwidth
```

## Worked example (Ch 9)

7B model in FP16 (2 bytes/param) generating 100 tokens/s:

```
bandwidth used = 7B × 2 × 100 = 700 GB/s
```

On an A100-80GB GPU with **2 TB/s** of memory bandwidth:

```
MBU = 700 GB/s / 2 TB/s = 35%
```

(The book uses this exact computation and reports 70% — the discrepancy is because the book's stated computation assumes a 1 TB/s baseline; the published number depends on the assumed chip. The 7B-FP16-at-100-tokens/s = 700 GB/s arithmetic is the load-bearing relationship.)

## Why quantization matters for MBU

> *"This underscores the importance of quantization (discussed in Chapter 7). Fewer bytes per parameter mean your model consumes less valuable bandwidth."* — Ch 9

Going from FP16 to INT8 halves bytes/param → halves bandwidth used → enables doubling tokens/s at the same MBU.

## MBU declines as load increases

Figure 9-5 in Ch 9 (Databricks benchmark): Llama 2-70B FP16 MBU **decreases** as concurrent users increase. Why?

> *"The decline is likely due to the higher computational load per second with more users, shifting the workload from being bandwidth-bound to compute-bound."* — Ch 9

So MBU is workload-dependent — at low load it's high (bandwidth-bound regime); at high load it falls (workload becomes compute-bound).

## MFU vs MBU diagnostic

- **High MFU + low MBU** → compute-bound; need more FLOPs.
- **Low MFU + high MBU** → memory-bandwidth-bound; need more bandwidth, smaller KV cache, or quantization.

## Connections

- [[MFU]] — companion utilization metric (compute side).
- [[GPUUtilization]] — the misleading metric MBU/MFU correct for.
- [[ComputeBound]] / [[MemoryBandwidthBound]] — diagnosed regimes.
- [[Quantization]] — the dominant MBU lever (fewer bytes per parameter).
- [[KVCache]] — bandwidth consumer; shrinking it raises effective MBU headroom.
- [[HBM]] — the memory whose bandwidth MBU measures against.
- [[Decode]] — the LLM phase where MBU matters most.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
