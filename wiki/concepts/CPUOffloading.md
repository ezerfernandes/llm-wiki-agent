---
title: "CPU Offloading"
type: concept
tags: [memory, training, distributed-training, deepspeed]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# CPU Offloading

A memory-management technique that **moves tensors (typically optimizer states, gradients, or even model weights) from GPU memory to CPU memory** when GPU memory is exhausted, swapping them back in as needed. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Techniques that focus on making better use of hardware memory include CPU offloading. Instead of trying to fit the whole model on GPUs, you can offload the excess memory onto CPUs, as demonstrated by DeepSpeed (Rasley et al., 2020)."

## The canonical implementation: [[DeepSpeed]]

[[DeepSpeed]] introduced **[[ZeRO]] (Zero Redundancy Optimizer)** with progressive offloading stages:

- **ZeRO Stage 1**: partition optimizer states across GPUs.
- **ZeRO Stage 2**: partition optimizer states + gradients.
- **ZeRO Stage 3**: partition optimizer states + gradients + weights.
- **ZeRO-Offload**: move ZeRO-partitioned state to CPU memory.
- **ZeRO-Infinity**: extend to NVMe storage when CPU memory is exhausted.

[[QLoRA]] uses **paged optimizers**, a specific kind of CPU offloading: optimizer states are paged to CPU like virtual memory pages, brought back to GPU only when needed.

## The trade-off

| Storage tier | Bandwidth | Capacity | Latency |
|---|---|---|---|
| GPU HBM | ~3 TB/s | ~80 GB | ns |
| CPU DRAM | ~100 GB/s | ~TB | μs |
| NVMe SSD | ~7 GB/s | ~TB | ms |

Each step down sacrifices bandwidth for capacity. Training that swaps frequently to slower tiers is **bandwidth-bound** and runs slower wall-clock, but it **runs at all** instead of OOM-ing.

## When to use

- When you can't reduce memory enough via [[Quantization|quantization]] + [[GradientCheckpointing|checkpointing]] + [[PEFT]] alone.
- When you have lots of CPU memory and tolerable disk I/O.
- For [[FullFinetuning|full finetuning]] on hardware that wouldn't otherwise support it.

## When not to

- When you have enough GPU memory — the overhead is wasted.
- When wall-clock training time is critical and you'd rather use a bigger GPU.
- When your interconnect (PCIe / CXL) is the binding constraint.

## Connections

- [[MemoryBottleneck]] — the umbrella problem.
- [[DeepSpeed]] / [[ZeRO]] — the canonical implementation.
- [[QLoRA]] — paged optimizers.
- [[GradientCheckpointing]] / [[MixedPrecisionTraining]] — orthogonal mitigations.
- [[Quantization]] — reduces what needs offloading in the first place.
- [[ai-engineering-ch07-finetuning]] — primary source.
