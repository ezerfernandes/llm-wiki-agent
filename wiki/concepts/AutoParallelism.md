---
title: "Automatic Parallelism"
type: concept
tags: [deep-learning, performance, parallelism, frameworks]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Automatic Parallelism

The framework's runtime scheduler exploits the [[ComputationalGraph|dependency graph]] to execute independent ops *in parallel* on multiple devices — without the user writing any explicit parallel code ([[d2l-computational-performance]] §`auto-parallelism`).

## Two axes

1. **Cross-device computation parallelism.** Two independent ops on `gpu0` and `gpu1` finish in $\max(t_0, t_1)$ rather than $t_0 + t_1$, provided the frontend doesn't insert a barrier between them. D2L shows this explicitly: removing `torch.cuda.synchronize` / `npx.waitall` between two `run(x_gpuN)` blocks lets total time drop below the sum of parts.
2. **Computation–communication overlap.** A backward pass produces gradients top-to-bottom; we can begin **shipping the first gradient to the CPU / parameter server** while the next layer's gradient is still computing. In PyTorch, `tensor.to('cpu', non_blocking=True)` and `tensor.copy_(other, non_blocking=True)` enable this. Production [[AllReduce]] (e.g. [[NCCL]] / [[Horovod]]) is designed precisely to overlap with backprop.

## Caveats

- **Single-device single-op parallelism is rarely useful** — one matmul kernel already uses all SMs / all CPU cores. Parallelization matters between *devices*.
- **Async without barriers can blow up memory** — if the frontend dispatches faster than the backend can compute, the task queue grows unboundedly. D2L recommends synchronizing once per minibatch.
- **Dependent ops cannot be parallelized.** The dep graph forbids it.

## See also
- [[AsyncComputation]] — the substrate auto-parallelism runs on.
- [[ComputationalGraph]] — what the scheduler walks.
- [[DataParallelism]] — what most multi-GPU training relies on; auto-parallelism overlaps the per-GPU work with the all-reduce.
- [[d2l-computational-performance]] §`auto-parallelism`.
