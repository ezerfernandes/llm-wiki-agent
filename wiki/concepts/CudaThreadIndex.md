---
title: "CUDA Thread Indexing (threadIdx / blockIdx / blockDim)"
type: concept
tags: [cuda, gpu, parallelism, programming-model]
sources: [dis-15-1-gpu, parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-18
---

# CUDA Thread Indexing — `threadIdx`, `blockIdx`, `blockDim`

The **built-in variables** [[CUDA]] makes available inside every `__global__` [[KernelFunction|kernel]] so each thread can compute *which slice of the data it owns*. Each thread runs the **same kernel code**; what distinguishes one thread from another is its **per-thread indices**.

## The three built-ins

| Variable | Type | Meaning |
|---|---|---|
| `threadIdx.{x,y,z}` | `uint3` | Index of *this thread* **within its [[Block|block]]** |
| `blockIdx.{x,y,z}` | `uint3` | Index of *this thread's block* **within the [[Grid|grid]]** |
| `blockDim.{x,y,z}` | `dim3` | Size of every block (threads per block in each axis) |
| `gridDim.{x,y,z}` | `dim3` | Size of the grid (blocks per grid in each axis) |

Each is a 3-component vector — the `.x` / `.y` / `.z` components mirror the **multidimensional [[KernelLaunch|launch configuration]]** the host specifies with the `<<<dim3 grid, dim3 block>>>` syntax.

## Canonical 1-D pattern

The textbook vector-add kernel maps **one thread to one array element**:

```cuda
__global__ void vecAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) c[i] = a[i] + b[i];
}
```

The arithmetic `blockIdx.x * blockDim.x + threadIdx.x` is the **global linear thread ID** across the entire grid — the canonical CUDA idiom that appears in essentially every introductory kernel.

The `if (i < n)` guard handles the case where the launch over-rounds (e.g., 1000 elements with 256 threads/block requires 4 blocks → 1024 threads — the last 24 must do nothing).

## 2-D pattern (matrices)

For a matrix of size `M × N`:

```cuda
__global__ void matAdd(float *A, float *B, float *C, int M, int N) {
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    if (row < M && col < N)
        C[row * N + col] = A[row * N + col] + B[row * N + col];
}
```

Launched with `dim3 block(16, 16); dim3 grid((N+15)/16, (M+15)/16); matAdd<<<grid, block>>>(...)` — the 2-D shape matches the data, simplifying the index arithmetic and improving cache / [[SharedMemory|shared-memory]] tiling.

## Why thread-private indices matter

Without thread-private `threadIdx` + `blockIdx`, every thread in a [[Warp]] would execute the *exact same* instructions on the *exact same* operands — useless data parallelism. The built-ins are what make [[SIMT|SIMT]] productive: same instructions, **different addresses**, computed from these per-thread identifiers.

## See also

- [[CUDA]] — the programming model that defines these built-ins.
- [[KernelLaunch]] — the `<<<grid, block>>>` syntax that **sets** `gridDim` and `blockDim`.
- [[Block]] / [[Grid]] / [[Warp]] / [[SIMT]] — the thread hierarchy `blockIdx` / `threadIdx` index into.
- [[KernelFunction]] / [[StreamingMultiprocessor]] — the execution substrate.
- [[dis-15-1-gpu]] — DIS introductory framing.
- [[parproc-ch05-cuda-gpu-programming]] — ParProc canonical depth.
