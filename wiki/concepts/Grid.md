---
title: "Grid (CUDA)"
type: concept
tags: [gpu, cuda, execution-model]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Grid (CUDA)

The **grid** is the totality of threads for one [[KernelLaunch|kernel launch]] in [[CUDA]]. A grid is composed of one or more **[[Block|blocks]]** of threads ([[parproc-ch05-cuda-gpu-programming]] §5.2, §5.4.4).

```
Grid  →  Blocks  →  Threads  →  Warps
```

## Grid dimensions

The grid is at most **two-dimensional** — each block has 2D coordinates `blockIdx.x` and `blockIdx.y` (a `.z` exists in newer compute capabilities but the chapter treats the grid as 2D). Grid size is declared at launch:

```c
dim3 dimGrid(n, 1);          // n × 1 grid of blocks
dim3 dimBlock(1, 1, 1);      // 1 × 1 × 1 block (1 thread)
kernel<<<dimGrid, dimBlock>>>(args);
```

The 2D shape is a programmer convenience for 2D problems (matrix tiling, 2D heat-flow stencils). *"This does not correspond to any physical arrangement in the hardware"* (§5.4.4) — the runtime serializes the 2D index into a linear sequence of blocks dispatched to [[StreamingMultiprocessor|SMs]].

## Grid lifetime and scope

- A grid exists for the **duration of one kernel launch**. The host call returns immediately (kernel calls are async), but the grid runs until completion.
- Subsequent kernel launches form **separate** grids. Data persists across grids only in [[GlobalMemory|global memory]] and [[ConstantMemory|constant memory]] (not [[SharedMemory|shared]] or registers, both of which are kernel-lifetime).
- An **implicit barrier** exists between two consecutive kernel calls if the second depends on the first's outputs.

## See also

- [[Block]] — the unit a grid is composed of.
- [[Thread]] — the leaf unit of execution.
- [[KernelLaunch]] — the `<<<grid, block, shmem>>>` syntax declaring grid dimensions.
- [[CUDA]] — the parent programming model.
- [[parproc-ch05-cuda-gpu-programming]] — §5.2 / §5.4.4.
