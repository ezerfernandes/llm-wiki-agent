---
title: "Neural Processing Unit (NPU)"
type: concept
tags: [hardware, mobile, ai-accelerator, mlsysbook, energy]
sources: [mlsysbook-ch02-ml-systems, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Neural Processing Unit (NPU)

A **dedicated hardware block on a [[SystemOnChip|mobile SoC]] whose circuits are designed exclusively for low-precision matrix multiplication**. In [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]) it is what makes [[MobileML|Mobile ML]] feasible within a strict power budget.

By avoiding the power-intensive instruction-fetch/decode logic of a general-purpose CPU, an NPU yields a **10–100× gain in energy efficiency (TOPS/W)**, fitting high AI throughput inside a mobile device's <500 mW sustained budget. Flagship phones provide tens of INT8 TOPS this way (NPU inference ~5–20 ms for MobileNet). An INT8 model on an NPU achieves 3–4× higher throughput per watt than the same model in FP32 on a CPU — which is why "deploy one binary across all edge devices" is a pitfall: a binary tuned for an Arm Cortex-A78 underutilizes an Arm Ethos-U NPU.

## Connections

- [[SystemOnChip]] — the chip the NPU is integrated into.
- [[MobileML]] — the paradigm the NPU enables.
- [[Quantization]] — NPUs run fixed-function INT8 datapaths; quantization is the enabling step.
- [[GoogleTPU]] — the cloud-scale tensor accelerator; the NPU is the mobile analogue.
- [[IronLawOfMLSystems]] — the NPU improves the compute term's effective efficiency per watt.
- [[mlsysbook-ch02-ml-systems]] — source.
- [[mlsysbook-ch11-hardware-acceleration]] — Ch 11 details the NPU's mobile role: 10–100× energy efficiency from fixed-function tensor kernels, but *only* for supported operators — any unsupported op "falls back" to CPU/GPU and negates the advantage, the central scheduling constraint of heterogeneous [[SystemOnChip|SoCs]] (down to Ethos-U micro-NPUs at the MCU scale).
