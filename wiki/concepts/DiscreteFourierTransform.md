---
title: "Discrete Fourier Transform"
type: concept
tags: [mathematics, signal-processing, frequency-domain, parallel-computing]
sources: [parproc-ch13-audio-image-processing]
last_updated: 2026-05-17
---

# Discrete Fourier Transform

The Discrete Fourier Transform (DFT) is the discrete analog of the [[FourierSeries]], applied when the function g() is known only at a finite number of sample points rather than continuously. Given n sampled values X = (x₀, x₁, ..., xₙ₋₁), the DFT produces n frequency-domain coefficients C = (c₀, c₁, ..., cₙ₋₁):

cₖ = (1/n) Σⱼ₌₀ⁿ⁻¹ xⱼ e^{−2πijk/n} = (1/n) Σⱼ₌₀ⁿ⁻¹ xⱼ qʲᵏ

where q = e^{−2πi/n} is a primitive n-th root of unity (qⁿ = 1). The sample array X is interpreted as one period of the underlying function, with period n and fundamental frequency 1/n.

## Matrix Form

The DFT is a matrix-vector product:

C = (1/n) A X

where A is an n×n Vandermonde matrix with element (j,k) equal to q^{jk}. This formulation connects the DFT directly to parallel matrix multiplication methods ([[parproc-ch11-parallel-matrix-operations]]).

## Inversion

The DFT is a one-to-one transformation. Because A is a Vandermonde matrix it is invertible, and:

[A(q)]⁻¹ = (1/n) A(1/q)

So the inverse DFT recovers the original samples:

xⱼ = Σₖ₌₀ⁿ⁻¹ cₖ e^{2πijk/n} = Σₖ₌₀ⁿ⁻¹ cₖ q^{−jk}

## Normalization Conventions

Different sources use different scaling factors:

- **Matloff (Ch13) convention**: 1/n in the forward transform, no factor in the inverse.
- **Symmetric convention**: 1/√n in both directions; simplifies inversion since [A(q)]⁻¹ = A(1/q).
- **R's `fft()` ("unnormalized")**: no 1/n or 1/√n factor in the forward direction; the user must divide by n after the inverse transform.

When combining results from different FFT libraries, verify which normalization is in use.

## Two-Dimensional DFT

For image data xᵤᵥ (row u, column v; u = 0,...,n−1, v = 0,...,m−1), the 2-D DFT is:

cᵣₛ = (1/n)(1/m) Σⱼ₌₀ⁿ⁻¹ Σₖ₌₀ᵐ⁻¹ xⱼₖ e^{−2πi(jr/n + ks/m)}

The **separability** property means this can be computed as 1-D DFTs applied row-by-row and then column-by-column. This is the basis for efficient parallel 2-D DFT computation ([[parproc-ch13-audio-image-processing]] §13.3.4).

## Real-Valued Input

When the input xⱼ is real (as with sound data), the DFT coefficients for indices k > n/2 are the complex conjugates of those for k < n/2. Only n/2 independent frequency values are produced.

## Applications

- **[[ImageSmoothing]]**: set high-frequency DFT coefficients to zero (low-pass filter), then invert.
- **[[EdgeDetection]]**: set low-frequency DFT coefficients to zero (high-pass filter), then invert.
- **Audio processing**: analyze spectral content for speech or voice recognition.

## Computational Complexity

Naive DFT from the matrix formulation is O(n²). The [[FastFourierTransform]] algorithm reduces this to O(n log n).

## Parallel Computation

Two strategies from [[parproc-ch13-audio-image-processing]] §13.3:

1. **FFT recursion**: divide-and-conquer analogous to Quicksort ([[parproc-ch12-parallel-sorting]]); effective for message-passing (mirrors Hyperquicksort); limited in shared-memory due to diminishing thread utilization.
2. **Matrix multiply**: treat C = (1/n)AX as a dense matrix-vector multiply and apply Ch11 parallel matrix methods; preferred in shared-memory settings.

## Available Implementations

- **R `fft()`**: serial; handles 1-D and multi-dimensional data; `inverse=TRUE` for inverse; unnormalized.
- **[[CUFFT]]**: CUDA GPU-accelerated; excellent for large transforms on GPU hardware.
- **[[FFTW]]**: CPU-parallel; provides OpenMP and MPI versions; available at fftw.org.

## See Also

- [[FourierSeries]] — the continuous analog.
- [[FastFourierTransform]] — efficient O(n log n) algorithm.
- [[CUFFT]] — GPU implementation.
- [[FFTW]] — CPU-parallel implementation.
- [[ImageSmoothing]] — frequency-domain application.
- [[EdgeDetection]] — frequency-domain application.
