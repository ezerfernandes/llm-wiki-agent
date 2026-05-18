---
title: "Horovod"
type: concept
tags: [distributed-training, infrastructure, collective-ops]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Horovod

Uber's open-source library for [[DistributedTraining]] using MPI-style [[RingAllReduce|ring-allreduce]] across [[PyTorch]] / [[TensorFlow]] / [[MXNet]] workers. Predecessor and complement to PyTorch DDP; sometimes used inside [[Kubeflow]] training operators.

## In D2L

[[d2l-computational-performance]] §`parameterserver` cites Sergeev & Del-Balso 2018 (the Horovod paper) for the technique of **overlapping gradient synchronization with backprop**: begin all-reducing the top-layer gradients while the lower-layer gradients are still being computed. Horovod made ring-allreduce ergonomic in 2018 by wrapping MPI / [[NCCL]] behind a single-line decorator (`hvd.DistributedOptimizer`).

## Architecture

- Underlying transport: MPI (OpenMPI / MVAPICH) or [[NCCL]] (NVIDIA hardware).
- Algorithm: [[RingAllReduce]] across all worker ranks.
- API: `hvd.init()`, `hvd.DistributedOptimizer(opt)`, `hvd.broadcast_parameters(...)`. Drop-in replacement for the optimizer step in PyTorch / TF / MXNet.
- Backprop overlap: tensor-fusion + hierarchical-allreduce optimizations.

## See also
- [[RingAllReduce]] — the algorithm.
- [[NCCL]] — the NVIDIA backend.
- [[AllReduce]] / [[ParameterServer]] — the synchronization-architecture choice.
- [[DataParallelism]] / [[DistributedTraining]] — the consumers.
- [[d2l-computational-performance]] §`parameterserver`.
