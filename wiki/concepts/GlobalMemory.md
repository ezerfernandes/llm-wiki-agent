---
title: "Global Memory (CUDA)"
type: concept
tags: [gpu, cuda, memory]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Global Memory (CUDA)

The largest, slowest tier of the GPU [[GPUMemoryHierarchy|memory hierarchy]] in [[CUDA]]. Global memory lives **off-chip** in HBM/GDDR, is **accessible from all threads in all blocks**, persists across kernel calls for the lifetime of the application, and is reachable from the host via `cudaMemcpy()` ([[parproc-ch05-cuda-gpu-programming]] §5.4.3.1).

## Properties (Tesla baseline)

| Property | Value |
|---|---|
| Scope | Global to application |
| Size | Large (GBs) |
| Location | Off-chip |
| Speed | "Molasses" — *hundreds of clock cycles per access* |
| Lifetime | Application |
| Host access | Yes (`cudaMemcpy`) |
| Cached (Tesla) | No |

## Allocation patterns

**Dynamic** — from the host:

```c
int *dm;
cudaMalloc((void**)&dm, msize);
cudaMemcpy(dm, hm, msize, cudaMemcpyHostToDevice);
// ... kernel uses dm ...
cudaMemcpy(hm, dm, msize, cudaMemcpyDeviceToHost);
cudaFree(dm);
```

**Static** — file-scope `__device__` declaration:

```c
__device__ int z[100];      // global memory, but NOT host-accessible
```

A static `__device__` variable is global to all kernels but **not accessible from the host** — only `cudaMalloc`-allocated regions are addressable for `cudaMemcpy`.

## Performance mitigations

Global memory is the GPU's biggest performance pitfall. Two hardware mechanisms ameliorate the cost:

- **[[LatencyHiding|Latency hiding]]** — when a [[Warp]] issues a slow global access, the [[StreamingMultiprocessor|SM]] schedules another ready warp to run. This is the SM's "[[OSInHardware|OS in hardware]]" pattern applied to memory I/O. *"While one warp is fetching data from memory, another warp can be executing, thus not losing time due to the long fetch delay."* (§5.4.2.3).
- **[[MemoryCoalescing|Coalescing]]** — when threads in a half-warp access consecutive words, the hardware merges them into a single transaction of up to 32 words. *"This works because the memory is low-order interleaved."* (§5.4.3.2).

Together, these encourage the CUDA design pattern of **many small threads** — overcommitted warps maximize latency-hiding opportunities, and uniform access strides maximize coalescing.

## Local memory: not what the name suggests

The CUDA "local memory" tier is **physically part of global memory** — it is the compiler-allocated overflow store for per-thread variables that don't fit in registers ([[RegisterSpill|register spill]]). Despite the "local" label it suffers the full global-memory latency.

## See also

- [[SharedMemory]] — on-chip, fast, block-scope alternative used as a programmer-managed cache.
- [[MemoryCoalescing]] — the main bandwidth optimization for global memory.
- [[GPUMemoryHierarchy]] — the full hierarchy table.
- [[CUDA]] — the parent programming model.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.3.1 / §5.4.3.2.
