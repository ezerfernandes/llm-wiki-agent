---
title: "Atomic Operation (CUDA)"
type: concept
tags: [gpu, cuda, synchronization, concurrency]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Atomic Operation (CUDA)

In [[CUDA]], an **atomic operation** is a read-modify-write action on [[GlobalMemory|global]] or [[SharedMemory|shared]] memory that *"a thread can execute without pre-emption, i.e. without interruption"* ([[parproc-ch05-cuda-gpu-programming]] §5.5). Atomics are the primary mechanism for **inter-block** coordination — since `__syncthreads()` only works within a [[Block]] and SMs cannot barrier-sync with each other ([[parproc-ch05-cuda-gpu-programming]] §5.4.1).

## Available primitives

| Operation | Action | Use |
|---|---|---|
| [[AtomicAdd|`atomicAdd(addr, inc)`]] | Fetch-and-add | Reductions across blocks |
| `atomicExch(addr, val)` | Exchange | Lock release |
| `atomicCAS(addr, cmp, val)` | Compare-and-swap | Lock acquire, lock-free structures |
| `atomicMin` / `atomicMax` | Min / max update | Reductions |
| `atomicAnd` / `atomicOr` | Bitwise | Flag aggregation |

The return value of every atomic is the **previous value** at that address.

## Implementing a lock

```c
__device__ void lock(int *lockVar) {
    while (atomicCAS(lockVar, 0, 1) != 0) { ; }
}

__device__ void unlock(int *lockVar) {
    atomicExch(lockVar, 0);
}
```

(Compile with `nvcc -arch=sm_11` or higher to enable the atomics.)

## Why a barrier built from atomics is expensive

*"Though a barrier could in principle be constructed from the atomic operations, its overhead would be quite high. In earlier models that was near a microsecond, and though that problem has been ameliorated in more recent models, implementing a barrier in this manner would not be much faster than attaining interblock synchronization by returning to the host and calling `cudaThreadSynchronize()` there."* ([[parproc-ch05-cuda-gpu-programming]] §5.5).

So for **real inter-block synchronization** (iterative algorithms where all threads must wait at the end of each iteration), the standard pattern is to **end the kernel** between iterations:

```c
for (int it = 0; it < niter; it++) {
    kernel<<<grid, block>>>(...);
    cudaThreadSynchronize();   // implicit barrier
}
```

## See also

- [[AtomicAdd]] — the most common atomic.
- [[CudaThreadSynchronize]] — the host-side barrier alternative.
- [[ThreadBarrier]] — the intra-block alternative (`__syncthreads`).
- [[Block]] — atomics' raison d'être (only mechanism across blocks).
- [[CUDA]] — substrate.
- [[parproc-ch05-cuda-gpu-programming]] — §5.5.
