---
title: "Data Parallelism"
type: concept
tags: [distributed-training, parallelism, multi-gpu, deep-learning]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Data Parallelism

The dominant multi-GPU training strategy: **every GPU holds a full model replica**, the minibatch is sharded across GPUs, each GPU computes loss + gradient on its shard, gradients are [[AllReduce|all-reduced]] across GPUs, and each replica updates locally with the aggregated gradient ([[d2l-computational-performance]] §`multiple-gpus`).

## Procedure (k GPUs)

1. Split the random minibatch into $k$ equal shards; ship shard $i$ to GPU $i$.
2. Each GPU runs forward + backward independently on its replica with its shard → produces local gradient $\mathbf{g}_i$.
3. **All-reduce**: aggregate $\mathbf{g} = \sum_i \mathbf{g}_i$ and broadcast back to all GPUs.
4. Each GPU updates its local parameters with $\mathbf{g}$ → all replicas stay in sync.

## Why it dominates

D2L compares three multi-GPU strategies:

| Strategy | Memory per GPU | Sync cost | Recommended? |
|---|---|---|---|
| Network partitioning (layers across GPUs) | $1/k$ | Tight cross-layer sync, hard to load-balance | No |
| Layerwise / [[TensorParallelism|tensor]] partitioning (split channels) | $1/k$ | Sync at every layer, even higher bandwidth | No |
| **Data parallelism** | Full model | Sync once per minibatch | **Yes** |

> *"By and large, data parallelism is the most convenient way to proceed, provided that we have access to GPUs with sufficiently large memory."* — [[d2l-computational-performance]]

## Practical rules

- **Scale minibatch by $k$** so each GPU has the same per-step work as the single-GPU baseline.
- **Scale learning rate** accordingly (D2L tries 256→512 and 0.1→0.2 going from 1→2 GPUs).
- **[[BatchNormalization]] needs adjustment** — either keep per-GPU BN statistics (D2L's default) or use *SyncBN* for very small per-GPU batches.

## API

- PyTorch: `nn.DataParallel(net, device_ids=devices)` (single-process, multi-GPU; legacy) or `nn.parallel.DistributedDataParallel` (multi-process, multi-node; standard).
- MXNet: `gluon.Trainer` with `ctx=devices`.
- TensorFlow: `tf.distribute.MirroredStrategy`.
- Framework-agnostic: [[Horovod]], DeepSpeed.

## Limitations

- **Does not allow larger models** — each GPU still holds the full model. Use [[ModelParallelism]] / [[TensorParallelism]] / [[PipelineParallelism]] for that.
- **All-reduce bandwidth** eventually becomes the bottleneck at large scale — see [[RingAllReduce]] / [[ParameterServer]].

## See also
- [[AllReduce]] — the synchronization primitive.
- [[RingAllReduce]] — bandwidth-optimal all-reduce.
- [[ModelParallelism]] — for models that don't fit on one GPU.
- [[ParameterServer]] — multi-machine generalization.
- [[Horovod]] / [[NCCL]] — production implementations.
- [[DistributedTraining]] — parent concept.
- [[d2l-computational-performance]] §`multiple-gpus` / `multiple-gpus-concise`.
