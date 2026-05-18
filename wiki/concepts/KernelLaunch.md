---
title: "Kernel Launch (CUDA)"
type: concept
tags: [gpu, cuda, syntax, execution-model]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Kernel Launch (CUDA)

The syntax by which the host launches a [[CUDA]] kernel on the GPU. [[NVIDIA]]'s nvcc extends C with the **triple-angle-bracket** form:

```c
kernel<<<dimGrid, dimBlock>>>(args);
kernel<<<dimGrid, dimBlock, sharedBytes>>>(args);     // dynamic shared mem
```

The first two arguments declare the [[Grid]] and [[Block]] dimensions (both `dim3` structs); the optional third declares **dynamic shared-memory bytes** for an `extern __shared__` array ([[parproc-ch05-cuda-gpu-programming]] §5.3, §5.4.3).

## Kernel functions

A kernel is declared with the `__global__` qualifier:

```c
__global__ void find1elt(int *m, int *rs, int n) {
    int rownum = blockIdx.x;
    // ... per-thread work
}
```

Constraints ([[parproc-ch05-cuda-gpu-programming]] §5.3):

- Kernels return `void`. Outputs travel via pointer arguments to device memory.
- Each thread runs the kernel; each thread receives the same arguments.
- Thread/block identity is read from the built-in vars `blockIdx`, `threadIdx`, `gridDim`, `blockDim`.
- Helper functions called from kernels are declared `__device__` (these *can* return values).
- A kernel **cannot call host functions** — no C standard library, no `malloc` on the host side, no function pointers, no stack (functions are inlined).

## Asynchronous semantics

Kernel launches **do not block** — the host call returns immediately. To wait for the kernel to finish:

```c
cudaThreadSynchronize();    // explicit host-side wait
```

Or rely on implicit barriers:

- `cudaMemcpy()` blocks until prior kernel work is done.
- Two consecutive kernel launches have an implicit barrier between them when the second depends on outputs of the first.

## Worked example (row sums, §5.3)

```c
dim3 dimGrid(n, 1);              // n blocks
dim3 dimBlock(1, 1, 1);          // 1 thread per block (deliberately naive)
find1elt<<<dimGrid, dimBlock>>>(dm, drs, n);
cudaThreadSynchronize();
cudaMemcpy(hrs, drs, rssize, cudaMemcpyDeviceToHost);
```

## See also

- [[Grid]] / [[Block]] — declared by `dimGrid` / `dimBlock`.
- [[CUDA]] — the parent programming model.
- [[SharedMemory]] — sized by the optional third argument.
- [[parproc-ch05-cuda-gpu-programming]] — §5.3 / §5.4.4.
