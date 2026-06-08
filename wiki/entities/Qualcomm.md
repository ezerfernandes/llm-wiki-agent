---
title: "Qualcomm"
type: entity
tags: [company, hardware, mobile, soc, npu]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Qualcomm

Qualcomm is a semiconductor company whose **Snapdragon** mobile and automotive [[SystemOnChip|SoCs]] exemplify heterogeneous AI acceleration.

## Snapdragon AI Engine ([[mlsysbook-ch11-hardware-acceleration]])

The Snapdragon AI Engine coordinates CPU cores, GPU shaders, a DSP, and a dedicated [[NeuralProcessingUnit|NPU]] across a shared memory hierarchy. Workloads are distributed by operator type: computer-vision kernels on the GPU's parallel shaders, audio on DSP arithmetic units, transformer attention on NPU matrix engines. The Snapdragon 8 Gen 3 memory controller uses priority-based arbitration (camera processing outranks background AI) to meet real-time constraints under a 3–7 W budget while managing thermal throttling and battery life.

## Snapdragon Ride (automotive)

The Snapdragon Ride platform coordinates multiple AI accelerators across safety domains, with redundant processing elements for functional safety and time-triggered scheduling that provides temporal isolation between safety-critical and convenience functions — meeting deterministic sub-100 ms perception-to-action latency.

## See also
- [[SystemOnChip]] — the heterogeneous architecture Snapdragon embodies.
- [[NeuralProcessingUnit]] — the matrix engine for on-device inference.
- [[Apple]] / [[NVIDIA]] / [[Tesla]] — other custom-silicon players.
- [[mlsysbook-ch11-hardware-acceleration]] — Snapdragon AI Engine and Ride platform.
