---
title: "atomicAdd (CUDA)"
type: concept
tags: [gpu, cuda, synchronization, atomic]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# atomicAdd (CUDA)

A [[CUDA]] [[AtomicOperation|atomic operation]] that performs a **fetch-and-add** without pre-emption — the canonical primitive for cross-block reduction in [[parproc-ch05-cuda-gpu-programming]] §5.5 / §5.9.

## Signature

```c
int atomicAdd(int *address, int inc);
```

- Reads the integer at `*address`.
- Atomically adds `inc` to it.
- Returns the **previous** value of `*address`.

Available on both [[GlobalMemory|global]] and [[SharedMemory|shared]] memory operands.

## Canonical inter-block reduction (mutual outlinks, §5.9)

```c
__global__ void procpairs(int *m, int *tot, int n) {
    int totth = gridDim.x * blockDim.x;
    int me = blockIdx.x * blockDim.x + threadIdx.x;
    int sum = 0;
    // ... per-thread accumulation into local sum ...
    atomicAdd(tot, sum);              // <-- combine across blocks
}
```

Every thread computes a private partial sum, then **one** atomic per thread aggregates into a single global counter `tot`. With thousands of threads, this is far cheaper than alternative inter-block synchronization (lock-based or host-roundtrip) because each `atomicAdd` is bounded-time and uncontended in the common case.

## When to prefer atomics over reductions

- **Per-thread contribution is small.** Each thread contributes one number; many threads contribute.
- **Final result is a scalar.** Vector reductions are usually better done via [[Thrust]]'s `thrust::reduce` or a hand-rolled tree reduction.
- **Inter-block** scope. Within a block, use `__syncthreads()` + [[SharedMemory|shared memory]] reduction instead.

## Hardware caveats

- **Contention is the enemy.** Many threads racing on the same address serialize. A common optimization is to first reduce within each block (in shared memory) and then have one thread per block do the global atomic.
- **Counter overflow.** `atomicAdd` on a 32-bit int can overflow silently; use 64-bit variants for large reductions.

## See also

- [[AtomicOperation]] — the parent category.
- [[CUDA]] — substrate.
- [[parproc-ch05-cuda-gpu-programming]] — §5.5 / §5.9.
