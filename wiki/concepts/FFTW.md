---
title: "FFTW"
type: concept
tags: [library, fft, signal-processing, parallel-computing, openmp, mpi]
sources: [parproc-ch13-audio-image-processing]
last_updated: 2026-05-17
---

# FFTW

FFTW ("Fastest Fourier Transform in the West") is a free, open-source software library for computing the [[DiscreteFourierTransform]] and its inverse. It is available at http://www.fftw.org and provides callable interfaces for both [[OpenMP]] (shared-memory parallelism) and [[MPI]] (message-passing distributed-memory parallelism).

FFTW is the standard CPU-parallel FFT library for scientific computing on clusters and multicore systems. It automatically adapts its internal algorithm to the hardware and problem size via a planning phase that benchmarks several FFT strategies at startup.

## Key Properties

- **Platform**: CPU (multicore / cluster); the counterpart to [[CUFFT]] on GPU.
- **Parallel interfaces**: OpenMP version for shared-memory (multi-threaded), MPI version for distributed memory.
- **Data types**: handles 1-D, multi-dimensional, real-to-complex, and complex-to-complex transforms.
- **Self-tuning**: the planner selects optimal FFT decomposition strategies at runtime.
- **License**: free for non-commercial use; GPL license.

## Relationship to Other FFT Tools

| Library | Platform | Parallelism |
|---|---|---|
| R `fft()` | CPU (serial) | None |
| **FFTW** | CPU | OpenMP + MPI |
| [[CUFFT]] | GPU | CUDA threads |

For CPU-bound parallel workloads on clusters, FFTW is the standard choice. For GPU workloads, [[CUFFT]] is preferred. R's `fft()` can be made parallel for 2-D transforms via `parApply` from the Snow package, but FFTW provides better scalability for large transforms.

## Context in the ParProcBook

[[NormMatloff]] introduces FFTW in [[parproc-ch13-audio-image-processing]] §13.4.3 as part of the FFT software survey alongside R's `fft()` and [[CUFFT]]. No code example is provided for FFTW in the chapter; the reference is to its parallel capabilities.

## See Also

- [[FastFourierTransform]] — the algorithm FFTW implements.
- [[DiscreteFourierTransform]] — the mathematical transform.
- [[CUFFT]] — GPU-accelerated counterpart.
- [[OpenMP]] — the shared-memory interface.
- [[MPI]] — the distributed-memory interface.
