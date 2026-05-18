---
title: "AllReduce"
type: concept
tags: [distributed-training, collective-ops, parallelism, multi-gpu]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# AllReduce

The collective communication primitive at the heart of [[DataParallelism|data-parallel]] training: **given a vector on each of $k$ devices, sum them and broadcast the result to every device**. After AllReduce all devices hold the identical aggregated vector ([[d2l-computational-performance]] §`multiple-gpus` / §`parameterserver`).

## Mathematical form

For $k$ workers with local gradients $\mathbf{g}_1, \dots, \mathbf{g}_k$:

$$\mathbf{g} = \sum_{i=1}^k \mathbf{g}_i \quad\text{then}\quad \mathbf{g}_i \leftarrow \mathbf{g}\;\forall i.$$

This is a **commutative reduction** — the order of summation doesn't matter, which lets implementations optimize the network path freely.

## Naive D2L implementation

```python
def allreduce(data):
    for i in range(1, len(data)):
        data[0][:] += data[i].to(data[0].device)   # gather to device 0
    for i in range(1, len(data)):
        data[i][:] = data[0].to(data[i].device)    # broadcast back
```

This is $O(k)$ on a single bus and lumps all traffic on the device-0 link. Production implementations use [[RingAllReduce|ring all-reduce]] (constant-time independent of $k$) or hierarchical / tree variants.

## Strategy interaction with bus topology

D2L's 4-GPU example (160 MB gradients):

| Strategy | Time |
|---|---|
| Gather to GPU 0 over PCIe (each of 3 sends 10 ms) + broadcast back | ~60 ms |
| Send everything to CPU (each of 4 sends 10 ms + return) | ~80 ms |
| Split gradient into 4 chunks, each chunk aggregated on a different GPU in parallel via PCIe switch | ~15 ms |

Synchronization strategy is **inseparable from hardware topology** — which motivates [[NCCL]]'s topology-aware path selection and [[Horovod]]'s ring layout.

## Production implementations

- [[NCCL]] — NVIDIA's GPU collective library; the default backend for PyTorch DDP, MXNet KVStore, TensorFlow MultiWorkerMirroredStrategy on NVIDIA hardware.
- MPI (OpenMPI, MVAPICH) — CPU-side standard.
- Gloo — Facebook's portable backend (often used for CPU all-reduce in PyTorch).
- [[Horovod]] — wraps NCCL/MPI with the ring-allreduce algorithm.

## See also
- [[RingAllReduce]] — bandwidth-optimal AllReduce algorithm.
- [[DataParallelism]] — what consumes AllReduce.
- [[ParameterServer]] — the alternative "centralized" synchronization architecture.
- [[NCCL]] / [[Horovod]] — production implementations.
- [[d2l-computational-performance]] §`multiple-gpus` / §`parameterserver`.
