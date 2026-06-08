---
title: "Multiply-Accumulate (MAC)"
type: concept
tags: [hardware, ml-systems, neural-networks, compute]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Multiply-Accumulate (MAC)

The atomic operation of neural computation: `a ← a + (b × c)`. A neural network's compute cost is measured in MACs, because the [[ArtificialNeuron|neuron]]'s weighted sum, the layer's [[MatrixMultiplication|matrix multiply]], and ultimately the whole [[ForwardPropagation|forward pass]] reduce to streams of multiply-accumulates.

Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]]:

- A neuron over N inputs = **N MACs**; a layer of M neurons = **M×N MACs**.
- One MNIST digit through a 784→128→64→10 net = **109,184 MACs** — "not one of which is a logical branch."
- **FLOP vs MAC accounting**: accelerators are marketed in FLOPs because a fused multiply-add (FMA) counts as *two* floating-point operations. So an [[NVIDIA]] H100 rated ~1,000 TFLOP/s dense FP16 ≈ **~500 trillion MAC/s** by the one-MAC-per-multiply-accumulate convention.

Every layer-size and [[BatchSize|batch-size]] decision ultimately reduces to *how many MACs fit within the latency and power budget*. Modern accelerator datapaths (FMA units, [[TensorCore|Tensor Cores]]) exist to execute MACs at maximum throughput.

## Connections

- [[ArtificialNeuron]] / [[MatrixMultiplication]] / [[GEMM]] — what MACs add up to.
- [[ForwardPropagation]] — the pass measured in MACs.
- [[ArithmeticIntensity]] / [[RooflineModel]] — FLOP/byte ratios built on MAC counts.
- [[TensorCore]] / [[GPU]] / [[NVIDIA]] — hardware that executes MACs (e.g. the H100).
- [[mlsysbook-ch05-neural-computation]] — source.
