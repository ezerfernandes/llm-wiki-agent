---
title: "Constant Memory (CUDA)"
type: concept
tags: [gpu, cuda, memory]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Constant Memory (CUDA)

A **read-only-from-device, read/write-from-host** memory tier in [[CUDA]]. Constant memory lives off-chip but is **cached on-chip**, so frequently-read values hit the cache and run nearly as fast as registers ([[parproc-ch05-cuda-gpu-programming]] §5.4.3.5).

## Properties

| Property | Value |
|---|---|
| Scope | Global to application |
| Size | 64K (Tesla) |
| Location | Off-chip, with on-chip cache |
| Speed | Fast if cache hit, otherwise off-chip latency |
| Lifetime | Application |
| Host access | Yes (read/write) |
| Device access | **Read only** |

## Declaration and population

```c
__constant__ int x;                              // file-scope, outside any function

// Host code:
int y = 3;
cudaMemcpyToSymbol("x", &y, sizeof(int));

// Device code:
int z;
z = x;                                           // read the constant
```

The general form: `cudaMemcpyToSymbol(var_name, pointer_to_source, number_bytes_copy, cudaMemcpyHostToDevice)`.

## The "constant" misnomer

*"Note again that the name Constant refers to the fact that device code cannot change it. But host code certainly can change it between kernel calls."* ([[parproc-ch05-cuda-gpu-programming]] §5.4.3.5).

This makes constant memory the natural home for **per-iteration parameters in iterative algorithms**:

```
// host code
for 1 to number_of_iterations:
    set Constant array x
    call kernel (do scatter op)
    cudaThreadSynchronize()
    do gather op, using kernel results to form new x
```

The kernel reads `x` heavily (cache-friendly); the host updates `x` between kernels (which is when the device's read-only restriction matters not at all).

## Constant vs texture vs global

| Property | Constant | Texture | Global |
|---|---|---|---|
| Cached | Yes (1D-style) | Yes (**2D**) | No (Tesla) |
| Device write | No | No | Yes |
| Host write | Yes | Yes | Yes |
| Use case | Per-pass parameters | 2D-spatial access | General read/write |

## See also

- [[TextureMemory]] — the 2D-cached read-only sibling tier.
- [[GlobalMemory]] — uncached read/write counterpart.
- [[GPUMemoryHierarchy]] — full hierarchy.
- [[CUDA]] — parent programming model.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.3.5.
