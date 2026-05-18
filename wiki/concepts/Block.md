---
title: "Block (CUDA)"
type: concept
tags: [gpu, cuda, execution-model]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Block (CUDA)

A **block** in [[CUDA]] is a group of threads that the hardware assigns **entirely to one [[StreamingMultiprocessor|SM]]** for the lifetime of the kernel ([[parproc-ch05-cuda-gpu-programming]] §5.4.4, §5.6). The block is the **resource-allocation unit**:

- All threads in a block share that block's slice of [[SharedMemory|shared memory]] on its SM.
- The intra-block barrier `__syncthreads()` synchronizes only this block's threads.
- Threads in different blocks **cannot synchronize via barrier** — they must either use atomic operations on [[GlobalMemory|global memory]] or return to the host between kernels.

## Block dimensions and indexing

Blocks may be **up to 3-dimensional**:

```c
dim3 dimBlock(blkX, blkY, blkZ);
```

Within the kernel, each thread reads `threadIdx.x`, `threadIdx.y`, `threadIdx.z`. The block itself sits in a 2D grid at `blockIdx.x`, `blockIdx.y`. As with the [[Grid]], the multi-D coordinates are programmer conveniences with no physical hardware correlate.

## Constraints (Tesla baseline)

| Constraint | Limit |
|---|---|
| Max threads / block | 512 |
| Max threads / SM | 786 |
| Block size minimum | ≥ 32 (full [[Warp]]) |
| Block size optimum | 128–256, multiple of 32 |
| Block-to-SM assignment | Hardware-chosen, opaque |

*"A commonly-cited rule of thumb is to have between 128 and 256 threads per block."* (§5.6, p. 137).

## Block-size tradeoffs

| Factor | Argues for | Argues against |
|---|---|---|
| Shared-memory pressure | Larger blocks (more shared per block) | — |
| Barrier cost (`__syncthreads`) | Smaller blocks | — |
| Latency hiding via many warps | Larger blocks | — |
| [[ThreadDivergence]] concentration | — | Larger blocks |
| SM count saturation | At least as many blocks as SMs | — |

## See also

- [[Grid]] — the parent unit; a grid contains blocks.
- [[Warp]] — the child unit; a block is divided into 32-thread warps.
- [[StreamingMultiprocessor]] — the SM a block is bound to.
- [[SharedMemory]] — block-scoped on-chip memory.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.4 / §5.6.
