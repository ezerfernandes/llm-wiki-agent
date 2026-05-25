---
title: "KernelBench"
type: concept
tags: [benchmark, code-generation, cuda, gpu, nvidia]
sources: [2507.19457-gepa]
last_updated: 2026-05-22
---

# KernelBench

CUDA kernel generation benchmark (Ouyang et al., 2025). Tasks require generating CUDA kernels for [[PyTorch]] modules and target the **NVIDIA V100 GPU**. The primary metrics are the **$fast_p$** family: $fast_p = $ fraction of tasks for which the generated kernel runs at $\geq p\times$ the speed of PyTorch-eager. $fast_1$ means "beats PyTorch-eager"; $fast_{0.5}$ means "within 2× of PyTorch-eager".

Used by [[2507.19457-gepa|GEPA]] as the second [[InferenceTimeSearch|inference-time search]] test bed alongside [[NPUEval]] — together demonstrating that the same optimization machinery works across NVIDIA CUDA and AMD XDNA2 NPU code generation.

## Results from the GEPA paper (GPT-4o, 35-task "representative subset")

| Budget (rollouts) | $fast_1$ | $fast_{0.5}$ |
|---|---|---|
| 0 (baseline) | ~0% | ~0% |
| 1,000 | ~12% | ~30% |
| 2,000 | ~20% | ~50% |
| 3,000 | ~22% | ~52% |

Sequential5 (the underlying agent, 5 iterative refinements per task with compiler/profiler feedback) is augmented by GEPA's prompt evolution; the prompt is updated per-task as part of the inference-time-search loop.

## Connections
- [[2507.19457-gepa]] — paper that uses KernelBench as a core inference-time-search benchmark.
- [[NPUEval]] — sibling NPU benchmark.
- [[CUDA]] — target programming model.
- [[GPU]] — target hardware class (NVIDIA V100 specifically).
- [[InferenceTimeSearch]] — optimization mode.
- [[FeedbackFunction]] — compiler errors / profiler output drive the optimization.
- [[GEPA]] — the optimizer.
- [[PyTorch]] — the baseline; $fast_p$ is measured vs PyTorch-eager.
