---
title: "Distributed Training"
type: concept
tags: [training, infrastructure, parallelism]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Distributed Training

Training a single model across multiple [[GPU|GPUs]] and/or nodes via [[DataParallelism|data parallelism]], [[TensorParallelism|tensor]] / [[ModelParallelism|model]] parallelism, or [[PipelineParallelism|pipeline]] parallelism. Tools include PyTorch DDP/FSDP, DeepSpeed, [[Horovod]], and Ray Train; requires [[Checkpoint|checkpointing]] and dictates the [[gpumemoryhierarchy]] strategy.

## Canonical pedagogical reference

[[d2l-computational-performance]] is the wiki's full-textbook derivation: (1) why [[DataParallelism|data parallelism]] is the recommended default; (2) the from-scratch [[AllReduce]] primitive; (3) [[RingAllReduce|ring-allreduce]]'s constant-time scaling; (4) the [[ParameterServer]] alternative; (5) the [[KeyValueStore|key–value store]] abstraction; (6) the hardware-topology argument (PCIe / NVLink / Ethernet bandwidth tiers).

## Synchronization architectures

| | [[AllReduce]] (decentralized) | [[ParameterServer]] (centralized) |
|---|---|---|
| Topology | Symmetric ring/tree | Hub-and-spoke |
| Modern default | Yes (NCCL-backed DDP, FSDP) | Less common except sparse-embedding workloads |
| Failure model | Hard restart | PS shard replacement |

## Parallelism strategies (orthogonal)

- **[[DataParallelism]]** — replicate model, shard batch. Default; needed at all scales.
- **[[ModelParallelism]] / [[TensorParallelism]]** — shard the parameters of each layer across GPUs. Needed when the model doesn't fit on one GPU.
- **[[PipelineParallelism]]** — shard the model by *layer* across GPUs. Companion to tensor parallelism for trillion-parameter LLMs.
- **3D parallelism** — combine all three (Megatron-LM, DeepSpeed-Megatron).

## See also
- [[d2l-computational-performance]] — textbook foundation.
- [[DataParallelism]] / [[ModelParallelism]] / [[TensorParallelism]] / [[PipelineParallelism]].
- [[AllReduce]] / [[RingAllReduce]] / [[ParameterServer]] — synchronization.
- [[NCCL]] / [[Horovod]] — production libraries.
- [[DistributedComputing]] — the broader parent concept.
