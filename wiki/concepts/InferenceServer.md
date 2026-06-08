---
title: "Inference Server"
type: concept
tags: [serving, inference, scheduler, batching, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Inference Server

Not a wrapper around `model.predict()` but a **high-performance scheduler that manages concurrency, memory, and data movement** to bridge irregular user traffic and the steady, uniformly-sized batches accelerators require ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). Examples: [[NVIDIATriton|NVIDIA Triton]], [[TensorFlowServing|TensorFlow Serving]], [[TorchServe]].

A request traverses a staged pipeline: client → network ingress (HTTP/gRPC) → request queue → **dynamic batcher** → inference runner (TensorRT/ONNX) → accelerator. The architecture provides three functions: (1) **concurrency management** (async event loops / thread pools so network I/O never idles the accelerator), (2) **request transformation** (JSON/Protobuf → tensors, including NCHW-vs-NHWC layout conversion), and (3) **model management** (loading weights into VRAM, versioning, warmup before exposing to traffic). [[TensorFlowServing|TF Serving]] pioneered separating model logic from serving infrastructure; Triton extended it to multi-framework. Dynamic batching inside these servers can improve GPU utilization by up to 70% vs naive single-request serving (without it, ResNet-50 at batch-1 wastes ~85% of compute).

The **scheduler** is the "brain": it decides whether to run a request immediately (minimize latency) or wait for more to batch (maximize throughput), tuned via the [[DynamicBatching|batching window]] (0 ms = pure latency; 10–50 ms common for cloud).

## Connections

- [[NVIDIATriton]] / [[TensorFlowServing]] / [[TorchServe]] / [[vLLM]] — concrete inference servers.
- [[DynamicBatching]] — the scheduler's core throughput-latency lever.
- [[InferenceRuntime]] — the execution engine the runner invokes (TensorRT/ONNX Runtime).
- [[gRPC]] / [[REST]] — the ingress protocols.
- [[ModelServing]] / [[LoadBalancing]] — the practice and the layer above multiple servers.
- [[ColdStart]] — model loading + warmup the server must complete before serving.
- [[mlsysbook-ch13-model-serving]] — source.
