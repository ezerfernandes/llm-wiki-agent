---
title: "TensorFlow Serving"
type: entity
tags: [google, inference-server, serving, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# TensorFlow Serving

Google's [[InferenceServer|inference server]] that **pioneered the separation of model logic from serving infrastructure** ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). It introduced the dynamic-batching scheduler pattern that improves GPU utilization by up to ~70% vs naive single-request serving, plus model lifecycle management (versioning, warmup, hot-loading).

[[NVIDIATriton|NVIDIA Triton]] later extended this design to multi-framework support. TensorFlow Serving defaults to NHWC tensor layout (efficient on CPUs), versus the NCHW layout PyTorch/TensorRT prefer on GPUs.

## Connections

- [[InferenceServer]] — the architecture pattern it pioneered.
- [[NVIDIATriton]] / [[TorchServe]] — sibling production inference servers.
- [[DynamicBatching]] — the scheduler optimization it introduced.
- [[TensorFlow]] — the framework it serves.
- [[Google]] — the vendor.
- [[mlsysbook-ch13-model-serving]] — source.
