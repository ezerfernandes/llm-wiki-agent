---
title: "Arithmetic Intensity"
type: concept
tags: [performance, roofline, hardware]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch02-ml-systems, mlsysbook-ch05-neural-computation, mlsysbook-ch06-network-architectures, mlsysbook-ch08-model-training, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch12-benchmarking, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
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
- [[BottleneckPrinciple]] / [[IronLawOfMLSystems]] — in [[mlsysbook-ch02-ml-systems|mlsysbook Ch 2]], low batch-1 arithmetic intensity ($I = O/D_{vol}$ below the hardware balance point $R_{peak}/\text{BW}$) is why ResNet-50 inference is memory-bound on both an A100 and a mobile NPU.
- [[MatrixMultiplication]] / [[GEMM]] / [[MemoryBound]] — per [[mlsysbook-ch05-neural-computation|mlsysbook Ch 5]], N×N matmul ≈ 2N/(3s) FLOP/byte (high) vs element-wise [[ReLU]] at ~1/(2s) ≈ 0.125 FLOP/byte (low) — the gap that makes dense layers the preferred workload; small MNIST stays <1 FLOP/byte, far below A100/H100 ridge points.
- [[ai-engineering-ch09-inference-optimization]] / [[mlsysbook-ch02-ml-systems]] / [[mlsysbook-ch05-neural-computation]] — sources.
- [[mlsysbook-ch06-network-architectures]] — uses arithmetic intensity as each architecture's "signature": [[ResNet|ResNet-50]] ~40 FLOP/byte (compute-bound), [[MobileNetV2|MobileNet]] ~21 (balanced), [[GPT2|GPT-2]] inference ~0.5 (bandwidth-bound) — a ~80× gap that determines each family's "natural" hardware home; the chapter's "FLOPs ≠ speed" fallacy (MobileNet can run *slower* than ResNet on a GPU) follows directly.
- [[mlsysbook-ch08-model-training]] — Ch 8 classifies every *training* op: dense [[GEMM]] $\mathcal{O}(n)$ FLOP/byte (compute-bound) vs activation functions ~0.5, attention softmax ~5, LayerNorm ~10 (all memory-bound). Materialized GPT-2-Small attention has intensity $d_{\text{head}}/2 = 32$ → below the A100 ridge → memory-bound (the gap [[FlashAttention]] closes). **Larger batches raise intensity**, shifting ops into the compute-bound regime — the physics behind the batch-size–utilization relationship.
- [[mlsysbook-ch11-hardware-acceleration]] — makes AI the central hardware-selection metric: for a dense layer AI ≈ batch size (batch-1 ≈1, batch-256 ≈205 on a 2048² FP16 layer); GPT-2 batch-1 decode (AI ≈1) hits <1% A100 utilization; ridge points rose V100 ~140 → H100 ~295 FLOP/byte, pushing low-reuse ops further into the memory-bound regime.
- [[mlsysbook-ch12-benchmarking]] — Ch 12 uses AI to *interpret* system benchmarks: ResNet-50 (~300 FLOP/byte, compute-bound) hits 85–90% A100 utilization while BERT batch-1 (~3 FLOP/byte, memory-bound) reaches ~3% → ~85% at batch-32; AI is the [[RooflineModel|roofline]] "speed-of-light" check in micro-benchmarking.
- [[mlsysbook-ch16-conclusion]] — the conclusion makes the **Arithmetic Intensity Law** invariant #6 of the [[ThirteenQuantitativeInvariants|thirteen]] ($R_{attainable}=\min(R_{peak}, I\times\text{BW})$, "adding compute to a memory-bound model yields zero gain") and applies it to the 70B [[Llama|Llama 2]]-on-H100 decode (AI ≈ 1, ≈ 295× memory-bound) — the binding constraint for [[GenerativeAI|generative AI]] token serving, addressed by batching (raise $I$) or INT4 quantization (cut $D_{vol}$).
