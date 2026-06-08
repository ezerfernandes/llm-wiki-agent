---
title: "Megatron"
type: entity
tags: [cs324, llm]
sources: [cs324-parallelism, cs324-environment]
last_updated: 2026-06-04
---

Megatron is NVIDIA's tensor/model-parallel Transformer training system, which partitions individual layers across multiple GPUs. It was used to train an 8.3B-parameter model on 512 GPUs and, combined with data and pipeline parallelism into 3D parallelism, to train a 1-trillion-parameter model on 3,072 GPUs.

## Connections
- [[ModelParallelism]] — Megatron implements intra-layer (tensor) model parallelism
- [[3DParallelism]] — combined with data and pipeline parallelism at trillion-parameter scale
- [[cs324-parallelism]] — discussed in this CS324 lecture
- [[cs324-environment]] — discussed in this CS324 lecture
