---
title: "AMD (Advanced Micro Devices)"
type: entity
tags: [company, hardware, gpu, semiconductor]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# AMD — Advanced Micro Devices

**Santa Clara-based semiconductor company; the primary [[NVIDIA|NVIDIA]] competitor in AI accelerators.** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"The success of NVIDIA GPUs has inspired many accelerators designed to speed up AI workloads, including Advanced Micro Devices (AMD)'s newer generations of GPUs ..."*

## Why AMD matters for AI

- **MI300 series** — current frontier GPU competing with NVIDIA H100/H200/B200. Used by Microsoft, Meta, and others for production LLM serving.
- **[[ROCm]] (Radeon Open Compute)** — AMD's open-source CUDA alternative; the primary software stack for AMD AI workloads.
- **Habana Gaudi** — AMD acquired Intel's Habana inference/training accelerator family? No — Habana Gaudi is Intel, not AMD. AMD's own dedicated AI chip line is the **Instinct** (MI300) series.

## Position in the AI accelerator landscape

| Chip class | NVIDIA | AMD |
|---|---|---|
| Frontier training GPU | H100, B200 | MI300X, MI325X |
| Programming language | [[CUDA]] (proprietary) | [[ROCm]] / HIP (open source) |
| Mind share in AI | Dominant | Catching up |

## Reasons users adopt AMD

1. **Pricing leverage** — alternative supplier means less NVIDIA pricing power.
2. **Memory capacity** — MI300X ships with up to 192 GB HBM3 (vs H100's 80 GB).
3. **Open-source stack** — ROCm is fully open; CUDA isn't.
4. **Specific large-buyer relationships** — Microsoft, Meta have committed to AMD as part of their multi-vendor strategies.

## Where AMD appears in Ch 9

- Mentioned as one of the AI accelerators inspired by NVIDIA's success.
- ROCm is named as one of three GPU programming languages alongside CUDA and [[Triton]].

## Connections

- [[NVIDIA]] — the dominant competitor.
- [[ROCm]] — AMD's software stack.
- [[GPU]] / [[AIAccelerator]] — the broader category.
- [[InferenceOptimization]] — broader discipline AMD chips serve.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
