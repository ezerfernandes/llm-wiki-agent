---
title: "Fast Fourier Transform"
type: concept
tags: [algorithms, signal-processing, parallel-computing, divide-and-conquer]
sources: [parproc-ch13-audio-image-processing]
last_updated: 2026-05-17
---

# Fast Fourier Transform

The Fast Fourier Transform (FFT) is an O(n log n) divide-and-conquer algorithm for computing the [[DiscreteFourierTransform]] (DFT), developed by Cooley and Tukey. The naive DFT from its matrix definition requires O(n²) operations; the FFT reduces this by exploiting the recursive structure of the Vandermonde matrix.

## The Cooley-Tukey Recursion

Let n be even and m = n/2. The n-point DFT coefficient cₖ can be rewritten as:

cₖ = (1/n) [Σⱼ₌₀ᵐ⁻¹ x₂ⱼ zʲᵏ + qᵏ Σⱼ₌₀ᵐ⁻¹ x₂ⱼ₊₁ zʲᵏ]

where z = e^{−2πi/m} (the m-th root of unity). Each sum has exactly the form of an m-point DFT — the first over even-indexed samples, the second over odd-indexed samples. An n-point FFT is thus two n/2-point FFTs plus O(n) combination work.

Applying this recursively (assuming n is a power of 2), the total work is T(n) = 2T(n/2) + O(n), which solves to O(n log n). The recursion cuts sample size in half at each of log₂ n levels.

## Parallel Strategies

Two parallelization strategies are described in [[parproc-ch13-audio-image-processing]] §13.3:

### 1. Divide-and-Conquer Recursion
Analogous to parallel Quicksort from [[parproc-ch12-parallel-sorting]]:
- **Shared memory (OpenMP)**: recurse with parallel task spawning, as in §4.5 of [[parproc-ch04-introduction-to-openmp]].
- **Message passing (MPI)**: mirrors Hyperquicksort from Ch12; each level of the recursion distributes work across nodes.

Limitation in shared memory: as the recursion progresses, subproblem sizes shrink and fewer threads have work to do, causing load imbalance. This limits scalability beyond a few recursion levels.

### 2. Matrix Approach
Express the DFT as a dense matrix-vector product C = (1/n)AX (A is the n×n Vandermonde matrix of powers of q). Apply parallel matrix multiplication methods from [[parproc-ch11-parallel-matrix-operations]]. This approach does not suffer the thread-starvation problem of divide-and-conquer and is preferred in shared-memory settings ([[parproc-ch13-audio-image-processing]] §13.3.2).

Some digital signal processing chips implement the FFT in hardware using a special interconnection network corresponding to the butterfly structure.

## Inverse FFT

The inverse [[DiscreteFourierTransform]] has the same Vandermonde matrix form as the forward transform (with q replaced by 1/q). Therefore the same parallelization strategies — recursion and matrix multiply — apply directly to computing the inverse FFT.

## 2-D FFT via Separability

The 2-D DFT decomposes into row-wise and column-wise 1-D DFTs by the separability property. To compute the 2-D FFT:
1. Apply the 1-D FFT to each row of the data matrix.
2. Apply the 1-D FFT to each column of the intermediate result.

Parallelization: in stage one, threads/nodes own groups of rows; in stage two, they own groups of columns. Rows and columns can be interchanged.

## Available Implementations

| Library | Platform | Notes |
|---|---|---|
| R `fft()` | CPU (serial) | Handles multi-dim data; `inverse=TRUE`; unnormalized |
| [[CUFFT]] | GPU (CUDA) | Handles 1-D/2-D/3-D, real/complex, batched transforms |
| [[FFTW]] | CPU (OpenMP + MPI) | "Fastest Fourier Transform in the West"; fftw.org |

## Normalization Warning

R's `fft()` is "unnormalized": neither 1/n nor 1/√n appears in the forward direction. After applying `fft(..., inverse=TRUE)`, the user must divide by n to recover original values. [[CUFFT]] and [[FFTW]] normalization conventions should be verified before mixing outputs.

## Historical Note

The FFT algorithm is attributed to J.W. Cooley and J.W. Tukey (1965), though earlier independent discoveries exist. It is among the most widely cited algorithms in scientific computing.

## See Also

- [[DiscreteFourierTransform]] — the transform being computed.
- [[FourierSeries]] — the continuous analog.
- [[CUFFT]] — GPU FFT library.
- [[FFTW]] — CPU-parallel FFT library.
- [[MatrixMultiplication]] — the matrix-approach parallelization strategy.
- [[ImageSmoothing]] — application via low-pass filtering.
- [[EdgeDetection]] — application via high-pass filtering.
