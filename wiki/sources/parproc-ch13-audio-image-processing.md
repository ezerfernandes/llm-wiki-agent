---
title: "ParProcBook Ch13: Parallel Computation for Audio and Image Processing"
type: source
tags: [textbook, parallel-computing, fft, dft, image-processing, signal-processing]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch13: Parallel Computation for Audio and Image Processing

Chapter 13 (book pp. 273–290, PDF pp. 293–310) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. The chapter develops the mathematical foundations of [[FourierSeries]] and [[DiscreteFourierTransform|DFT]], derives the [[FastFourierTransform|FFT]] as a divide-and-conquer recursion, surveys parallel FFT strategies (FFT, matrix multiplication, inverse, 2-D separability), surveys available software ([[CUFFT]], [[FFTW]], R's `fft()`), and applies frequency-domain techniques to [[ImageSmoothing]] (low-pass filtering) and [[EdgeDetection]] (high-pass filtering). Optional sections cover vector-space foundations (13.9) and bandwidth (13.10).

## Summary

§13.1 motivates the chapter through sound waveforms and their decomposition into periodic components. A repeating function g(t) with period T and fundamental frequency f₀ = 1/T can be expressed as an infinite weighted sum of harmonics (sines and cosines at integer multiples of f₀) — the Fourier series. The weights aₙ and bₙ form the **frequency spectrum** and are computed by integrating g(t) against each basis function over one period. This transforms data from the **time domain** (or **spatial domain** for images) to the **frequency domain**. The complex form (using Euler's formula e^{iθ} = cos θ + i sin θ) produces a compact representation. The 2-D extension treats images as functions g(u,v) of horizontal and vertical coordinates, with pixel intensity as the function value.

§13.2 handles the discrete case. In practice g(t) is known only at n sample points X = (x₀,...,xₙ₋₁). The **Discrete Fourier Transform** maps these n time-domain samples to n frequency-domain coefficients: cₖ = (1/n) Σⱼ xⱼ q^{jk}, where q = e^{−2πi/n} is an n-th root of unity. This is a matrix-vector product C = (1/n)AX where A is a Vandermonde matrix of powers of q. Inversion is exact: A(q)⁻¹ = (1/n)A(1/q), so X = A(1/q)C. For 2-D data (images), the DFT separates into row-wise then column-wise 1-D DFTs — the **separability** property.

§13.3 introduces the [[FastFourierTransform]]. Cooley and Tukey's FFT rewrites the n-point DFT recursively as two n/2-point DFTs (over even-indexed and odd-indexed samples), reducing complexity from O(n²) to O(n log n). In shared-memory settings the divide-and-conquer recursion is parallelized analogously to Quicksort from Ch12; in message-passing settings the pattern mirrors Hyperquicksort. The matrix formulation (§13.3.2) recasts the DFT as a dense matrix-vector multiply and applies the parallel matrix methods from Ch11 — preferred when divide-and-conquer hits diminishing returns in shared-memory systems. The inverse transform has the same matrix structure and is parallelized identically. The 2-D DFT exploits separability: compute row DFTs first (parallelized across threads/nodes), then column DFTs on the result.

§13.4 surveys FFT software: R's serial `fft()` (handles 1-D and multi-dimensional data; set `inverse=TRUE` for inverse; 2-D parallelism via `parApply` from the Snow package); [[CUFFT]] (CUDA's GPU-accelerated FFT library, previously introduced in Ch5); and [[FFTW]] ("Fastest Fourier Transform in the West," free download at fftw.org, with versions callable from OpenMP and MPI).

§13.5 applies frequency-domain techniques to image processing. **Smoothing** (§13.5.1): noisy pixels can be replaced by a local mean/median, or a **low-pass filter** can be applied in the frequency domain — zero out the high-frequency DFT coefficients (large r and s), then invert; higher harmonics correspond to faster spatial variation ("wiggliness"), so removing them smooths the image. The amount of smoothing is controlled by the cutoff harmonic. **Audio smoothing in R** (§13.5.2): given a sound sequence `snd`, compute its FFT, zero all coefficients with index greater than `maxidx`, and invert — a five-line R function using `fft()`, vector concatenation, and `Re(fft(..., inverse=T)/n)`. **Edge detection** (§13.5.3): an edge is a sharp intensity transition; Fourier approach applies a **high-pass filter** — delete low-frequency terms and keep high ones; equivalent to taking partial derivatives of intensity. Parallelization mirrors the smoothing case.

§13.6 notes that R's `tuneR` and `pixmap` libraries extract raw numeric data from sound and image files for subsequent Fourier processing.

§13.7 addresses pixel intensity clamping: after Fourier operations, intensity values may fall outside [0, 255]; negative values should be discarded and values above 255 scaled down; very faint results (values near 0) may need multiplication by a constant.

§13.8 argues that the assumption of periodicity is not limiting in practice. For sounds, local periodicity holds over short intervals corresponding to individual phonemes. For images, the implicit duplication of the image frame in all directions does not affect the utility of the DFT as a measure of "wiggliness" — the goal is not fidelity to a physical repeating pattern but characterization of spatial variation.

§13.9 (optional) provides the vector-space justification: the vectors vₕ = (1, q^{−h}, q^{−2h}, ..., q^{−(n−1)h}) form an orthonormal basis for the space V of n-component complex arrays under the inner product [u,w] = (1/n) Σⱼ uⱼ w̄ⱼ. The DFT coefficients are the coordinates of X in this basis. The matrix A/n is orthogonal in the complex sense (its inverse is its conjugate transpose), which immediately yields the inversion formula.

§13.10 (optional) explains bandwidth: every transmission medium passes frequencies in a range [fₘᵢₙ, fₘₐₓ] called its effective bandwidth; the human voice concentrates power in [340, 3400] Hz, explaining the 8000-sample/second rate (Nyquist theorem: sample at twice the maximum frequency). High bit-rate digital signals require wide-bandwidth media.

## Key Claims

- **The Fourier series represents any repeating function as a weighted sum of harmonics.** A function g(t) with period T and fundamental frequency f₀ = 1/T can be written as g(t) = Σ aₙ cos(2πnf₀t) + Σ bₙ sin(2πnf₀t). The coefficients aₙ, bₙ are the frequency spectrum and are computed by integrating g(t) against each harmonic over [0, T]. (§13.1.1, pp. 274–275)

- **The DFT is a matrix-vector product over a Vandermonde matrix.** C = (1/n)AX where element (j,k) of A is q^{jk} and q = e^{−2πi/n}. The inverse is X = A(1/q)C — same structure, replacing q with 1/q. Normalization conventions vary: R's `fft()` is "unnormalized" (neither 1/n nor 1/√n in the forward direction). (§13.2.1–13.2.2, pp. 278–280)

- **The FFT reduces DFT complexity from O(n²) to O(n log n) via divide-and-conquer.** An n-point DFT decomposes into two n/2-point DFTs over even and odd samples. The recursion cuts sample size in half at each step. Shared-memory parallelization mirrors OpenMP Quicksort from Ch12; message-passing mirrors Hyperquicksort. (§13.3.1, p. 281)

- **The matrix formulation of the DFT enables use of parallel matrix-multiply methods.** In shared-memory systems, divide-and-conquer eventually leaves too few threads with work; the matrix approach (C = (1/n)AX, A is n×n) applies the blocked parallel matrix multiplication from Ch11 without this limitation. (§13.3.2, p. 282)

- **The 2-D DFT separates into sequential 1-D DFTs by the separability property.** Compute the 1-D DFT of each row, then the 1-D DFT of each resulting column (or vice versa). Parallelization: threads/nodes own groups of rows in stage one and groups of columns in stage two. (§13.3.4, pp. 282–283)

- **Image smoothing and edge detection are dual frequency-domain operations.** Smoothing applies a low-pass filter (zero high-frequency DFT coefficients, invert). Edge detection applies a high-pass filter (zero low-frequency DFT coefficients, invert). Both require a forward DFT, coefficient manipulation, and an inverse DFT. Parallelization is identical in both cases. (§13.5.1 and §13.5.3, pp. 284–285)

- **FFTW provides OpenMP- and MPI-callable FFT routines competitive with CUFFT on CPU clusters.** For GPU workloads, CUFFT (introduced in Ch5) is the appropriate choice. For CPU-parallel workloads, FFTW handles both cases. R's `fft()` is serial but can be made parallel for 2-D data via `parApply`. (§13.4, p. 283)

- **Pixel intensities must be clamped to [0, 255] after frequency-domain operations.** Fourier-based smoothing and edge detection can produce negative or super-255 values; negative values are typically discarded and positive values rescaled. (§13.7, p. 286)

## Key Quotes

> *"Mathematical computations involving images can become quite intensive, and thus parallel methods are of great interest. Here we will be primarily interested in methods involving Fourier analysis."* — p. 273. Chapter motivation.

> *"The weights aₙ and bₙ, n = 0, 1, 2, ... are called the frequency spectrum of g()."* — p. 275. Definition of the frequency spectrum.

> *"Speedy computation of a discrete Fourier transform was developed by Cooley and Tukey in their famous Fast Fourier Transform (FFT), which takes a 'divide and conquer' approach."* — p. 281. Attribution of the FFT.

> *"Divide-and-conquer tends not to work too well in shared-memory settings, because after some point, fewer and fewer threads will have work to do. Thus this matrix formulation is quite valuable."* — p. 282. Motivation for the matrix approach over FFT in shared-memory.

> *"The property [of 2-D DFT separability] is called separability. This certainly opens possibilities for parallelization. Each thread (shared memory case) or node (message passing case) could handle groups of rows of the original data, and in the second stage each thread could handle columns."* — p. 283.

> *"FFTW ('Fastest Fourier Transform in the West') is available for free download at http://www.fftw.org. It includes versions callable from OpenMP and MPI."* — p. 283.

## Connections

- [[NormMatloff]] — author.
- [[UCDavis]] — author's institution.
- [[FourierSeries]] — §13.1; mathematical foundation; representation of repeating functions as weighted sums of harmonics. This chapter is the primary source for this concept page.
- [[DiscreteFourierTransform]] — §13.2; new concept page; discrete analog of the Fourier series for sampled data.
- [[FastFourierTransform]] — §13.3.1; new concept page; O(n log n) divide-and-conquer DFT algorithm by Cooley and Tukey.
- [[ImageSmoothing]] — §13.5.1–13.5.2; new concept page; low-pass filtering in the frequency domain.
- [[EdgeDetection]] — §13.5.3; new concept page; high-pass filtering in the frequency domain for boundary detection.
- [[FFTW]] — §13.4.3; new concept page; CPU-parallel FFT library supporting OpenMP and MPI.
- [[CUFFT]] — §13.4.2; GPU FFT library (CUDA); cross-reference with Ch5 §5.18.3; updated with inverse-transform and 2-D transform notes.
- [[CUDA]] — §13.4.2; CUFFT is a CUDA library.
- [[OpenMP]] — §13.3.1 (parallel FFT), §13.4.1 (parApply for 2-D fft), §13.4.3 (FFTW OpenMP version).
- [[MPI]] — §13.3.1 (message-passing FFT analogous to Hyperquicksort), §13.4.3 (FFTW MPI version).
- [[Quicksort]] — §13.3.1; the shared-memory parallel FFT recursion is structurally analogous to OpenMP Quicksort from Ch12.
- [[Hyperquicksort]] — §13.3.1; the message-passing FFT pattern mirrors Hyperquicksort from Ch12.
- [[MatrixMultiplication]] — §13.3.2; DFT as matrix-vector multiply; parallelized via Ch11 methods.
- [[parproc-ch05-cuda-gpu-programming]] — §5.18.3 introduced CUFFT; Ch13 §13.4.2 adds context on inverse and 2-D use.
- [[parproc-ch11-parallel-matrix-operations]] — §13.3.2 references Ch11 matrix-multiply methods for parallel DFT.
- [[parproc-ch12-parallel-sorting]] — §13.3.1 explicitly references Ch12 Quicksort and Hyperquicksort as structural analogs for parallel FFT.

## Contradictions

- **No contradiction with [[CUFFT]].** Ch5 §5.18.3 established CUFFT as CUDA's FFT library. Ch13 §13.4.2 confirms this and adds: CUFFT handles inverse transforms (set `inverse=TRUE` equivalent) and multi-dimensional data. The Ch5 caveats (per-call overhead, optimized-but-not-always-optimal) are not repeated in Ch13 but are not contradicted.
- **Normalization convention gap.** §13.2.2.1 explicitly notes that R's `fft()` is "unnormalized" — it omits both the 1/n and 1/√n factors in the forward transform. The Ch5 CUFFT discussion does not address normalization. Users mixing CUFFT and R `fft()` results should check normalization conventions carefully.
- **Divide-and-conquer vs matrix approach trade-off in shared memory.** §13.3.2 states divide-and-conquer "tends not to work too well in shared-memory settings" because threads run out of work. Ch12 §12.1.2 applied divide-and-conquer Quicksort to shared memory without this caveat. The FFT context makes the limitation more acute because the recursion depth is shallower (log₂ n levels) and work imbalance appears earlier; this is consistent rather than contradictory but warrants awareness.
