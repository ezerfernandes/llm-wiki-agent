---
title: "NCCL"
type: concept
tags: [distributed-training, collective-ops, nvidia, gpu, infrastructure]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# NCCL

**NVIDIA Collective Communications Library** — the de-facto GPU collective-ops backend for [[DataParallelism|data-parallel]] training. Implements [[AllReduce]], all-gather, reduce-scatter, broadcast, reduce, etc., across multiple GPUs on a single node (via PCIe / [[NVLink]]) or across nodes (via InfiniBand / RoCE / Ethernet).

## In D2L

[[d2l-computational-performance]] §`hardware`: *"We recommend to use NCCL to achieve high data transfer between GPUs."* The chapter's [[RingAllReduce|ring-allreduce]] analysis is exactly the algorithm NCCL implements (alongside tree- and double-tree variants for very large clusters).

## Why NCCL

- **Topology-aware path selection** — auto-detects the NVLink + PCIe + NIC topology and picks the optimal ring / tree.
- **GPU-direct RDMA** — moves bytes directly between GPU device memories without bouncing through host RAM.
- **Drop-in backend** for PyTorch DDP (`backend='nccl'`), TensorFlow's `MultiWorkerMirroredStrategy`, MXNet's KVStore (`device` / `dist_device_async`), [[Horovod]], DeepSpeed, FSDP.

## Architectural fit

```
PyTorch DDP / TF Strategy / Horovod   <- user API
              │
            NCCL                       <- collective algorithms (ring, tree)
              │
        CUDA driver                    <- GPU runtime
              │
   NVLink / PCIe / InfiniBand          <- physical fabric
```

## Limitations

- NVIDIA-only — AMD has RCCL (binary-compatible fork); Intel has OneCCL.
- Single-CPU-process per GPU traditionally; modern NCCL supports multi-rank per process.
- Synchronous by default; asynchronous needs careful stream management.

## See also
- [[AllReduce]] / [[RingAllReduce]] — the algorithms NCCL implements.
- [[NVLink]] / [[PCIe]] — the fabrics NCCL routes over.
- [[Horovod]] — common wrapper.
- [[CUDA]] / [[NVIDIA]] — the substrate.
- [[DistributedTraining]] / [[DataParallelism]] — the consumers.
- [[d2l-computational-performance]] §`hardware`.
