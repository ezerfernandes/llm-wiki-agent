---
title: "MIG (Multi-Instance GPU)"
type: concept
tags: [serving, gpu, multi-model, isolation, nvidia, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# MIG (Multi-Instance GPU)

NVIDIA technology (introduced with the A100) that **partitions a single physical GPU into up to seven independent instances**, each with dedicated streaming multiprocessors, memory controllers, and L2 cache ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). Available on A100, A30 (4 instances), H100, H200, and newer data-center GPUs.

Unlike software sharing ([[CUDAMPS|MPS]] or time-slicing), MIG provides **hardware-level isolation**: a runaway kernel in one partition cannot affect another's performance or memory, eliminating the "noisy neighbor" problem and enabling per-model SLO guarantees on shared hardware. The trade-off is granularity — partitions follow fixed profiles (e.g., 1g.5gb, 2g.10gb on A100), so resources cannot be divided arbitrarily. For multi-model serving, the choice is between consistent latency (MIG) and maximum utilization (shared CUDA streams / MPS). Older GPUs (V100, T4) get only time-multiplexed CUDA stream sharing.

## Connections

- [[CUDAMPS]] — the software-sharing alternative (shared context, weaker isolation).
- [[InferenceServer]] — multi-model serving where MIG provides per-model isolation.
- [[GPU]] / [[CUDA]] / [[GPUUtilization]] — the hardware and the consistency-vs-utilization trade-off.
- [[NVIDIA]] — the vendor.
- [[mlsysbook-ch13-model-serving]] — source.
