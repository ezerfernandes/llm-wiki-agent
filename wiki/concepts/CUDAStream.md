---
title: "CUDA Stream"
type: concept
tags: [frameworks, gpu, cuda, concurrency]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# CUDA Stream

A **CUDA stream** is an independent execution queue on the GPU: operations execute sequentially *within* a stream but concurrently *across* streams. It is the framework abstraction that exposes the GPU's independent hardware units for computation (SM clusters) and data transfer (copy engines), enabling true simultaneous execution.

By placing [[DMA]] transfers on one stream and computation on another, effective latency approaches the theoretical minimum max(compute, transfer) rather than their sum — hiding the data-movement penalty $D_{\text{vol}}/\text{BW}$. Without explicit streams the GPU serializes everything on the default stream. **Correctness** across streams is enforced with **CUDA events** (`event.record()` / `event.wait()`), which block only the dependent stream — far cheaper than `torch.cuda.synchronize()`, which blocks all streams and the CPU, negating all overlap. A common production bug is leaving a debugging `synchronize()` in place, silently serializing an overlapped pipeline. Streams also underpin pipeline parallelism across model stages.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — overlapping computation and communication.
- [[DMA]] / [[PinnedMemory]] — the transfers streams overlap with compute.
- [[PipelineParallelism]] — built on per-stage streams + events.
- [[StreamingMultiprocessor]] — the compute units streams schedule onto; [[CUDA]] — the platform.
