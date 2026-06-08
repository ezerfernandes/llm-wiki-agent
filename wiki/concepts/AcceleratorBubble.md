---
title: "Accelerator Bubble"
type: concept
tags: [training, performance, gpu, pipeline, ml-systems, mlsysbook]
sources: [mlsysbook-ch08-model-training]
last_updated: 2026-06-05
---

# Accelerator Bubble

An interval of **idle silicon** during training where the accelerator's compute units sit at ~0% utilization while waiting for another pipeline stage to catch up. Coined in [[mlsysbook-ch08-model-training|mlsysbook Ch 8]], which models a training system as a *staged system pipeline* (storage → CPU preprocessing → PCIe transfer → forward/backward → [[NVLink]] gradient sync) where any throughput mismatch between stages produces a bubble.

A systems engineer's primary task during training is to eliminate these bubbles — through asynchronous **[[DataPrefetching|prefetching]]** and pipeline overlapping, so the next batch is staged on the PCIe bus before the current backward pass completes.

## Key Points

- Bubbles appear as **white gaps in profiler GPU-activity traces** (e.g., the TensorFlow profiler's data-bound signature) where utilization drops to zero during data loading.
- Distinct from **[[PipelineParallelism|pipeline-parallelism bubbles]]**: those arise from sequential model-partition dependencies (downstream devices idle waiting for upstream activations), reducing naive model parallelism to 25–50% utilization. Both are "bubbles" — idle time from stage coupling — and microbatching / prefetching are the respective fixes.
- The min-of-three throughput rule means the *slowest* stage sets system throughput; a bubble is the symptom of a stage being slower than the accelerator.

## Connections

- [[DataPrefetching]] — the primary technique for eliminating data-side bubbles.
- [[PipelineParallelism]] — microbatching fills the analogous bubbles in distributed model parallelism.
- [[DAMTaxonomy]] — periodic utilization-to-zero is the data-bound signature.
- [[MFU]] / [[GPUUtilization]] — the metrics that reveal bubble cost.
- [[IronLawOfTrainingPerformance]] — bubbles erode the $\eta_{\text{hw}}$ term.
- [[mlsysbook-ch08-model-training]] — defining source.
