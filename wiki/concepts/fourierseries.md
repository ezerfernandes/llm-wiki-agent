---
title: "Fourier Series"
type: concept
tags: [mathematics, signal-processing, frequency-domain, parallel-computing]
sources: [parproc-ch13-audio-image-processing]
last_updated: 2026-05-17
---

# Fourier Series

A representation of a repeating (periodic) function as a weighted sum of sines and cosines at integer multiples of a fundamental frequency. For a function g(t) with period T and fundamental frequency f₀ = 1/T, the Fourier series is:

g(t) = Σₙ aₙ cos(2πnf₀t) + Σₙ bₙ sin(2πnf₀t)

The integer multiples nf₀ are called **harmonics**. The weights aₙ and bₙ form the **frequency spectrum** of g(). They are computed by integrating g(t) against each harmonic basis function over one period:

- a₀ = (1/T) ∫₀ᵀ g(t) dt
- aₙ = (2/T) ∫₀ᵀ g(t) cos(2πnf₀t) dt
- bₙ = (2/T) ∫₀ᵀ g(t) sin(2πnf₀t) dt

The complex form uses Euler's identity (e^{iθ} = cos θ + i sin θ) to write g(t) = Σⱼ cⱼ e^{2πij(t/T)}, where cⱼ are complex-valued spectral coefficients combining aⱼ and bⱼ. The complex form is more compact and is the basis for the [[DiscreteFourierTransform]].

## Time Domain vs Frequency Domain

The original signal g(t) — loudness against time for audio, intensity against position for images — is the **time-domain** (or **spatial-domain**) representation. The set of weights {aₙ, bₙ} (or equivalently {cⱼ}) is the **frequency-domain** representation. The two representations are in one-to-one correspondence; each recovers the other exactly.

## Two-Dimensional Extension

For images, g(u,v) is a function of two spatial coordinates. The 2-D Fourier series decomposes the image into 2-D sinusoidal basis functions. Pixel intensity for a gray-scale image ranges from 0 (black) to 255 (white); for color images, three separate intensity channels (R, G, B) are processed independently. The data for images is said to be in the **spatial domain** rather than the time domain.

## Why Periodicity Matters (and When It Doesn't)

The Fourier series formally requires a periodic function. For audio, individual phonemes exhibit local periodicity over short time intervals. For images, the mathematical formalism implicitly treats the image as tiled infinitely in both directions — but this is unimportant in practice, because the purpose is to measure "wiggliness" (spatial variation), and fitting linear combinations of trig functions achieves this regardless of the periodicity assumption ([[parproc-ch13-audio-image-processing]] §13.8).

## Discrete Counterpart

In practice g(t) is known only at discrete sample points. The [[DiscreteFourierTransform]] replaces the integrals with sums and the continuous spectrum with n frequency coefficients, one per sample point. The [[FastFourierTransform]] computes this in O(n log n) rather than O(n²).

## Applications (from [[parproc-ch13-audio-image-processing]])

- **Voice and speech recognition**: the frequency spectrum reveals pitch and formant structure; different voices concentrate power in different frequency bands.
- **[[ImageSmoothing]]**: zeroing high-frequency coefficients (low-pass filtering) removes noise and spatial roughness.
- **[[EdgeDetection]]**: zeroing low-frequency coefficients (high-pass filtering) isolates sharp intensity transitions.
- **Bandwidth analysis**: the effective bandwidth of a transmission medium corresponds to the frequency interval it can faithfully pass (§13.10).

## See Also

- [[DiscreteFourierTransform]] — the discrete analog for sampled data.
- [[FastFourierTransform]] — O(n log n) algorithm for computing the DFT.
- [[CUFFT]] — CUDA GPU-accelerated FFT library.
- [[FFTW]] — CPU-parallel FFT library (OpenMP + MPI versions).
- [[ImageSmoothing]] — low-pass filtering application.
- [[EdgeDetection]] — high-pass filtering application.
