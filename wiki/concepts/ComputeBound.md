---
title: "Compute-Bound"
type: concept
tags: [inference, performance, hardware, roofline]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Compute-Bound

A **workload whose time-to-complete is determined by the number of arithmetic operations the hardware can perform**, not by data movement. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]], this is one of two basic computational-bottleneck regimes for inference workloads (the other being [[MemoryBandwidthBound|memory bandwidth-bound]]).

## The classifier: arithmetic intensity

Workloads are classified by **[[ArithmeticIntensity|arithmetic intensity]]** — operations per byte of memory access. The [[RooflineModel|Roofline model]] (Williams et al. 2009) places workloads on a log-log chart of throughput vs. arithmetic intensity; whether the workload sits under the "compute roof" or the "bandwidth roof" determines the bottleneck.

## Examples

- **Password decryption** — heavy math, small data → compute-bound (Huyen's introductory example).
- **[[Prefill|Prefill]] phase of LLM inference** — many tokens processed in parallel through dense matrix multiplications → compute-bound. This is why TTFT is dominated by computational throughput.
- **Image-generation models** like Stable Diffusion → typically compute-bound.

## How to speed up compute-bound workloads

> *"A compute-bound workload might be sped up by spreading it out to more chips or by leveraging chips with more computational power (e.g., a higher FLOP/s number)."* — Ch 9

In other words: scale-out parallelism, more FLOP/s per chip, or lower-precision compute (FP8 / INT8 — fewer bits per op but more ops per cycle).

## Compute-bound vs MFU

Compute-bound workloads typically achieve **higher [[MFU]]** (Model FLOP/s Utilization) and lower [[MBU]] (Model Bandwidth Utilization) — because the chip's FLOPs are the binding constraint, not bandwidth.

## Connections

- [[MemoryBound]] / [[MemoryBandwidthBound]] — the opposite regime; [[mlsysbook-ch05-neural-computation|mlsysbook Ch 5]] contrasts dense [[GEMM]]/[[MatrixMultiplication|matmul]] (compute-bound) against element-wise [[ReLU]] (memory-bound) and notes the whole-network "Logic to Arithmetic" shift creates compute-bound workloads.
- [[mlsysbook-ch05-neural-computation]] — neural-computation framing.
- [[ArithmeticIntensity]] — the classifier.
- [[RooflineModel]] — Williams et al. 2009's cost model.
- [[Prefill]] — the compute-bound phase of LLM inference.
- [[MFU]] / [[MBU]] — utilization metrics that diagnose which regime you're in.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
