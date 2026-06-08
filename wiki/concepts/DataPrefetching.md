---
title: "Data Prefetching"
type: concept
tags: [training, data-pipeline, performance, ml-systems, mlsysbook]
sources: [mlsysbook-ch08-model-training]
last_updated: 2026-06-05
---

# Data Prefetching

A training-pipeline optimization that **overlaps data movement with computation** by loading and preprocessing the *next* batch while the accelerator processes the *current* one. It targets the data-movement-latency bottleneck (the "Data" axis of the [[DAMTaxonomy]]) and raises hardware utilization ($\eta_{\text{hw}}$) in the [[IronLawOfTrainingPerformance|iron law of training]].

Per [[mlsysbook-ch08-model-training|mlsysbook Ch 8]], a well-pipelined system has iteration time governed by the *maximum* of its stage latencies rather than their *sum*: $t_{\text{iteration}} = \max(t_{\text{fetch}}, t_{\text{process}}, t_{\text{transfer}})$. Prefetching turns the serial storage→preprocess→transfer chain into a parallel pipeline where each memory tier operates concurrently on a different batch.

## Key Points

- Eliminates **[[AcceleratorBubble|accelerator bubbles]]** — idle silicon where the GPU waits for the next batch.
- Requires multiple host-memory buffers (prefetch + processing + transfer), so it *increases* host memory usage — a tension with memory-constrained configs.
- The motivating arithmetic: random-access data shuffling delivers only ~10% of sequential storage bandwidth, and a serialized Python data loader (the "GIL-locked GPU") can starve an entire accelerator fleet (Amdahl's Law). The fix is multiprocessing data loaders or offloading preprocessing to the accelerator (e.g., NVIDIA DALI).
- In the chapter's pipeline example, prefetching + overlap cut wall-clock time from ~105 s to ~55 s (~48%) and raised utilization above 95% on 8× V100 for GPT-2 tokenization.
- A high-impact, low-complexity optimization — should generally be applied *first*, before mixed precision or checkpointing.

## Connections

- [[AcceleratorBubble]] — the idle-time pathology prefetching removes.
- [[DAMTaxonomy]] — prefetching is the canonical fix for data-bound bottlenecks.
- [[IronLawOfTrainingPerformance]] — raises the $\eta_{\text{hw}}$ term.
- [[MemoryHierarchy]] / [[HBM]] — the storage→DRAM→HBM bandwidth ladder prefetching pipelines across.
- [[GradientAccumulation]] / [[MixedPrecisionTraining]] — composed alongside prefetching in the single-machine optimization toolkit.
- [[mlsysbook-ch08-model-training]] — defining source.
