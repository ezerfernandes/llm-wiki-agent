---
title: "CUFFT"
type: concept
tags: [gpu, cuda, fft, library, signal-processing]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# CUFFT

[[NVIDIA]]'s GPU-accelerated Fast Fourier Transform (FFT) library for [[CUDA]]. *"CUFFT does for the Fast Fourier Transform what [[CUBLAS]] does for linear algebra, i.e. it provides CUDA-optimized FFT routines."* ([[parproc-ch05-cuda-gpu-programming]] §5.18.3).

## Position in the CUDA wrapper-library stack

CUFFT sits alongside:

- **[[CUBLAS]]** — BLAS / linear algebra primitives.
- **CUFFT** — Fourier transforms (1D / 2D / 3D, real / complex, single / double).
- **[[Thrust]]** — STL-style template library spanning CUDA and OpenMP.

All three follow the same operational pattern: programmer writes `cudaMalloc` + host→device transfer + library call + device→host transfer + `cudaFree`; the library calls invoke pre-tuned CUDA kernels under the hood.

## Why GPU FFT is interesting

The FFT decomposes into independent butterfly operations at each radix stage. The data-access pattern is regular but **non-contiguous** (stride-2, stride-4, ... at successive stages) — exactly the kind of bandwidth-bound, regular-but-strided kernel where careful [[MemoryCoalescing|coalescing]], [[SharedMemory|shared-memory]] staging, and [[Warp|warp]]-aligned indexing pay off. Hand-rolling these is non-trivial; CUFFT amortizes the tuning effort across users.

## Common caveats (inherited from §5.18)

- **Per-call kernel-launch overhead.** Many small transforms underperform; batch where possible (CUFFT has explicit batched-transform APIs).
- **Optimized but not optimal.** *"Even though these libraries have been highly optimized for what they are intended to do, they will not generally give you the fastest possible code for any given CUDA application."*
- **Status-code checking** is the programmer's responsibility.

## Inverse Transform and Multi-Dimensional Use (from Ch13)

[[parproc-ch13-audio-image-processing]] §13.4.2 confirms that CUFFT handles inverse transforms and multi-dimensional (2-D, 3-D) data in addition to 1-D transforms. For 2-D image processing the 2-D DFT can be computed directly via CUFFT, exploiting the separability property internally. CUFFT is the GPU-side counterpart to [[FFTW]] for CPU-parallel workloads.

## See also

- [[CUBLAS]] — the linear-algebra sibling.
- [[Thrust]] — the template-library sibling.
- [[CUDA]] — the substrate.
- [[NVIDIA]] — the vendor.
- [[parproc-ch05-cuda-gpu-programming]] — §5.18.3.
- [[parproc-ch13-audio-image-processing]] — §13.4.2; inverse and 2-D transform context.
- [[DiscreteFourierTransform]] — the transform CUFFT computes.
- [[FastFourierTransform]] — the algorithm underlying CUFFT.
- [[FFTW]] — CPU-parallel counterpart.
