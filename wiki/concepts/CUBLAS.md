---
title: "CUBLAS"
type: concept
tags: [gpu, cuda, linear-algebra, library, blas]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# CUBLAS

[[NVIDIA]]'s GPU-accelerated implementation of BLAS (Basic Linear Algebra Subprograms), callable from straight C code. CUBLAS exposes the standard BLAS operations — vector/matrix dot products, vector scaling, matrix-vector / matrix-matrix multiplies — backed by [[CUDA]] kernels, so you get GPU performance *"in linear algebra contexts without directly programming in CUDA"* ([[parproc-ch05-cuda-gpu-programming]] §5.18.1).

## FORTRAN column-major convention

The most surprising CUBLAS quirk: matrices are stored in **column-major** order ("FORTRAN style"), not the C / row-major convention. A C programmer must transpose or fill matrices in column-major order before passing them to CUBLAS. This is the most common source of bugs when integrating CUBLAS into C/C++ code.

## Typical API flow

```c
#include <cublas.h>

cublasInit();                                                       // init
cublasAlloc(n*n, sizeof(float), (void**)&dm);                       // device alloc
cublasAlloc(n,   sizeof(float), (void**)&drs);
cublasSetMatrix(n, n, sizeof(float), hm, n, dm, n);                 // host -> device
cublasSetVector(n,    sizeof(float), ones, 1, drs, 1);
cublasSgemv('n', n, n, 1.0, dm, n, drs, 1, 0.0, drs, 1);            // matrix * vector
cublasGetVector(n,    sizeof(float), drs, 1, hrs, 1);               // device -> host
cublasFree(dm);
cublasFree(drs);
cublasShutdown();
```

The Ch5 row-sums-via-CUBLAS example uses `cublasSgemv` (single-precision general matrix-vector multiply) to post-multiply A by a column vector of all 1s — a clever reformulation of *sum each row* as *matrix times ones vector*.

## Compilation

- **Pure CUBLAS C code** — compile with regular `gcc`:
  ```
  gcc -g -I/usr/local/cuda/include -L/usr/local/cuda/lib64 RowSumsCB.c -lcublas
  ```
- **Mixed CUDA + CUBLAS** — must use `nvcc`:
  ```
  nvcc -g -G RowSumsCB.c -lcublas
  ```

## Caveats

- *"Each call to a function in these packages involves a CUDA kernel call — with the associated overhead."* ([[parproc-ch05-cuda-gpu-programming]] §5.18). Chaining many small CUBLAS calls amortizes badly.
- *"Even though these libraries have been highly optimized for what they are intended to do, they will not generally give you the fastest possible code for any given CUDA application."* — hand-tuned kernels can still beat library calls in specialized cases.
- `cublasStatus` return codes — check them; Ch5's example does not.

## See also

- [[CUDA]] — the substrate.
- [[CUFFT]] — sibling library for FFT.
- [[Thrust]] — higher-level template library spanning CUDA and OpenMP.
- [[NVIDIA]] — the vendor.
- [[parproc-ch05-cuda-gpu-programming]] — §5.18.1.
