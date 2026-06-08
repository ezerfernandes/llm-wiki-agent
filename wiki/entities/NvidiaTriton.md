---
title: "NVIDIA Triton Inference Server"
type: entity
tags: [tool, serving, gpu, mlsysbook]
sources: [madewithml-mlops-serving, mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# NVIDIA Triton Inference Server

NVIDIA's high-performance multi-framework inference server. Mentioned alongside [[RayServe]], [[FastAPI]], and [[BentoML]] as a serving option in [[madewithml-mlops-serving]].

## In mlsysbook (Ch 13)

[[mlsysbook-ch13-model-serving|mlsysbook Ch 13]] cites Triton as the canonical [[InferenceServer|inference server]] — extending [[TensorFlowServing|TensorFlow Serving]]'s logic-from-infrastructure separation to **multi-framework support**, and implementing **model virtualization** (separating model lifecycle from application code via a model repository + control APIs for loading/unloading/versioning). Its dynamic-batching scheduler is the throughput-latency "brain."

## Connections

- [[InferenceServer]] — the architecture pattern.
- [[TensorFlowServing]] / [[TorchServe]] / [[vLLM]] — sibling inference servers.
- [[DynamicBatching]] / [[MIG]] / [[CUDAMPS]] — the throughput and multi-model mechanisms it uses.
- [[NVIDIA]] — the vendor.
- [[mlsysbook-ch13-model-serving]] — source.
