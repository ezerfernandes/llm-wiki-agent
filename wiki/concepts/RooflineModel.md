---
title: "Roofline Model"
type: concept
tags: [performance, hardware, parallel-computing]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch02-ml-systems, mlsysbook-ch05-neural-computation, mlsysbook-ch06-network-architectures, mlsysbook-ch08-model-training, mlsysbook-ch10-model-compression, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch12-benchmarking, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
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

## In ML systems ([[mlsysbook-ch02-ml-systems|mlsysbook Ch 2]])

Reddi uses the roofline informally to show that the *same* [[ResNet|ResNet-50]] is compute-bound during batched training but memory-bound for single-image (batch-1) inference — on *both* a cloud A100 and a mobile NPU, since batch-1 has low [[ArithmeticIntensity|arithmetic intensity]] below the ridge point. The systems lesson: [[Quantization|quantization]] (cutting bytes) often beats faster hardware (more FLOP/s), because both platforms are bandwidth-limited at batch=1. [[DeploymentSpectrum|Deployment-paradigm]] selection must account for this training-vs-inference roofline shift.

## Connections

- [[ArithmeticIntensity]] — the x-axis of the chart.
- [[BottleneckPrinciple]] / [[IronLawOfMLSystems]] — the mlsysbook framing the roofline informally serves.
- [[ComputeBound]] / [[MemoryBandwidthBound]] — the two regimes.
- [[MFU]] / [[MBU]] — utilization metrics derived from the same conceptual framework.
- [[Prefill]] / [[Decode]] — the two LLM phases the roofline separates.
- [[InferenceOptimization]] — the discipline this model serves.
- [[GPU]] / [[HBM]] / [[SRAM]] — the memory hierarchy whose bandwidths feed the chart's roofs.
- [[MemoryBound]] / [[mlsysbook-ch05-neural-computation]] — Ch 5 uses the roofline to show small MNIST (arith. intensity <1 FLOP/byte) sits deep on the memory-bound slope, far left of the A100/H100 ridge points (hundreds of FLOP/byte), so a CPU can match a GPU on it.
- [[ai-engineering-ch09-inference-optimization]] / [[mlsysbook-ch02-ml-systems]] — sources.
- [[mlsysbook-ch10-model-compression]] — Ch 10 uses the roofline to explain *why* [[Quantization|quantization]] speedup depends on regime: bandwidth-bound LLM decode gets ~2–4× from halving bytes, while compute-bound MLPs need INT8 *arithmetic* units to benefit — "quantization speedup depends on which side of the ridge you occupy."
- [[mlsysbook-ch06-network-architectures]] — applies roofline reasoning per architecture: [[ResNet|ResNet-50]] (~40 FLOP/byte) saturates ALUs while [[GPT2|GPT-2]] inference (~0.5) starves for bandwidth — same operation falling on either side of the A100 ridge point determines whether a faster *processor* or faster *memory* helps.
- [[mlsysbook-ch08-model-training]] — Ch 8 uses the roofline as *the* training-bottleneck diagnostic: it plots GPT-2 ops (MatMul compute-bound, LayerNorm/Softmax memory-bound) and shows **[[FlashAttention]] moving standard attention from below to above the ridge point** (memory- → compute-bound). The ridge point itself shifts with precision (A100 ~78 FLOP/byte TF32, ~156 FP16/BF16), making precision selection inseparable from roofline analysis.
- [[mlsysbook-ch11-hardware-acceleration]] — Ch 11 makes the roofline the chapter's organizing diagnostic: ridge points rose V100 ~140 → A100 ~153 → H100 ~295 FLOP/byte ("rising ridge"); batch size is the key lever (AI ≈ batch); the GPT-2 batch-1 ceiling is <1% A100 utilization; and the optimization-by-intensity-regime table maps each AI band to a concrete technique ([[KernelFusion|fusion]], [[Tiling|tiling]], precision reduction).
- [[mlsysbook-ch12-benchmarking]] — Ch 12 uses the roofline to *interpret system benchmarks*: A100 ridge ≈153 FLOP/byte; ResNet-50 (AI ≈300) hits 85–90% util while BERT batch-1 (AI ≈3) reaches only ~3% util → ~85% at batch-32; it is the micro-benchmark kernel-profiler diagnostic (Nsight) and the SOL ("speed of light") check against which achieved throughput is judged.
- [[mlsysbook-ch16-conclusion]] — the conclusion runs a closing roofline as the diagnostic instrument of the [[ThirteenQuantitativeInvariants|thirteen invariants]]: serving one token of a 70B [[Llama|Llama 2]] on an H100 (FP16) is ≈ 295× memory-bound ($T_{mem}\approx 41.8$ ms vs $T_{comp}\approx 0.14$ ms, AI ≈ 1) — so you must batch users or quantize to INT4, not tune compute kernels.
