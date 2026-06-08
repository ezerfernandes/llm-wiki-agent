---
title: "Memory Bandwidth"
type: concept
tags: [hardware, performance, mlsysbook, physics]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# Memory Bandwidth

The **rate at which data (model parameters, activations) moves from memory to the processor** — the $\text{BW}$ term in the [[IronLawOfMLSystems|iron law]]'s data term $D_{vol}/\text{BW}$. Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) argues bandwidth, not raw processor speed, is the binding constraint for many modern workloads.

The "thousands of megawatt-hours" consumed by GPT-scale models are dominated not by arithmetic but by the physically expensive process of fetching billions of weights through the memory hierarchy: **moving one byte from off-chip DRAM costs ~145× a FP16 op and ~800× an INT8 op** (≈160 pJ vs ~1.1 pJ vs ~0.2 pJ). Data movement requires charging/discharging wires over macroscopic distances; arithmetic is local. Therefore minimizing $D_{vol}$ is the primary lever for *both* speed and energy — the "energy tax."

This is why GPT-2/Llama-style decode is **bandwidth-bound** (billions of unique weights loaded per token, each used once) while batched ResNet-50 is **compute-bound** (small filters reused many times).

## Connections

- [[IronLawOfMLSystems]] — the data term it governs.
- [[MemoryWall]] — the single-node regime's binding constraint.
- [[RooflineModel]] / [[ArithmeticIntensity]] / [[MemoryBandwidthBound]] — the analysis tools.
- [[gpumemoryhierarchy]] / [[GPU]] — the hardware substrate.
- [[LighthouseModel]] — GPT-2/Llama as the bandwidth probe.
- [[mlsysbook-ch01-introduction]] — source.
