---
title: "NPUEval"
type: concept
tags: [benchmark, code-generation, hardware, npu, amd]
sources: [2507.19457-gepa]
last_updated: 2026-05-22
---

# NPUEval

A code-generation benchmark for **AMD XDNA2 NPU** (Neural Processing Unit) kernels (Kalade & Schelle, 2025). Tasks require generating low-level kernels — `abs`, `relu`, `bitwiseor`, `inverse`, `vectoradd`, `reducemax`, etc. — that compile and execute on AMD's AIE-ML architecture, with the primary metric being **vector utilization** (fraction of vector compute units active across the kernel's execution).

Used by [[2507.19457-gepa|GEPA]] as the **inference-time search** test bed for non-NVIDIA hardware.

## Results from the GEPA paper (GPT-4o)

| Method | Mean Vector Utilization |
|---|---|
| Sequential10 (10-iter agent w/ compiler feedback) | 4.25% |
| Sequential10 + RAG (architecture docs) | 16.33% |
| Sequential10 + RAG + [[MIPROv2]] | 19.03% |
| **GEPA (Pareto)** | **30.52%** |
| **Sequential10 + GEPA's single prompt (no RAG)** | **26.85%** |

Peak utilization for individual kernels: **~70%** under GEPA Pareto.

The standalone-prompt result (26.85% without RAG, using *only* the prompt GEPA evolved) is the load-bearing demonstration: GEPA can compress the architecture's coding conventions into a single declarative prompt that no longer needs runtime documentation retrieval.

## Why it matters

NPUs are a rapidly-growing hardware class (AMD XDNA2 for AI PCs; Apple Neural Engine; Qualcomm Hexagon NPU; Microsoft Copilot+ PCs require NPUs) but lack the deep tooling and documentation maturity of CUDA / NVIDIA. **Manual** porting of ML kernels to a new NPU architecture is expensive; GEPA's result suggests automated kernel discovery driven by compiler-error feedback can close a significant fraction of the gap with comparatively little human effort.

## Connections
- [[2507.19457-gepa]] — paper that introduces this benchmark to the wiki's corpus.
- [[XDNA2|AMD XDNA2]] — target architecture.
- [[KernelBench]] — sibling benchmark on NVIDIA CUDA / V100.
- [[InferenceTimeSearch]] — the optimization mode this benchmark exercises.
- [[FeedbackFunction]] — RAG-augmented $\mu_f$ is what makes NPUEval tractable.
- [[GEPA]] — the optimizer.
