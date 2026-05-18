---
title: "Image Smoothing"
type: concept
tags: [image-processing, signal-processing, frequency-domain, parallel-computing]
sources: [parproc-ch13-audio-image-processing]
last_updated: 2026-05-17
---

# Image Smoothing

Image smoothing reduces noise in a digital image by suppressing high-frequency variation in pixel intensities. Two broad approaches exist: spatial-domain averaging and frequency-domain low-pass filtering.

## Spatial-Domain Approach

Replace each pixel's intensity value with the mean or median of its immediate neighbors (typically the four or eight nearest neighbors). This is a simple, embarrassingly parallel operation — each output pixel depends only on a local neighborhood — but the amount of smoothing is coarsely controlled by neighborhood size.

## Frequency-Domain Approach (Low-Pass Filter)

The Fourier-based method treats smoothing as filtering in the frequency domain ([[parproc-ch13-audio-image-processing]] §13.5.1):

1. Compute the [[DiscreteFourierTransform]] (DFT) of the image. For a 2-D image, use the 2-D DFT (separable: row DFTs then column DFTs).
2. Set the high-frequency DFT coefficients to zero — specifically, set cᵣₛ = 0 for large values of r and s.
3. Apply the inverse DFT to recover a smoothed image in the spatial domain.

Higher harmonics correspond to faster spatial variation ("wiggliness"). Removing them eliminates fine-grained noise and sharp local transitions, producing a blurrier image. The cutoff harmonic controls the degree of smoothing.

This approach is called a **low-pass filter** because low frequencies pass through unchanged and high frequencies are blocked.

## Audio Smoothing in R

The same low-pass filtering logic applies to 1-D audio signals. The following R function smooths a sound sequence `snd` by retaining only the first `maxidx` DFT terms:

```r
p <- function(snd, maxidx) {
  four <- fft(snd)
  n <- length(four)
  newfour <- c(four[1:maxidx], rep(0, n-maxidx))
  return(Re(fft(newfour, inverse=T)/n))
}
```

`Re()` extracts the real part (discarding negligible imaginary components); the division by n corrects for R's unnormalized `fft()`.

## Parallelization

- **Spatial-domain neighbor averaging**: trivially parallel — each output pixel is independent. Assign groups of pixels to threads/nodes.
- **Frequency-domain low-pass filter**: parallelism comes from the parallel [[FastFourierTransform]] (divide-and-conquer or matrix approach), the parallel coefficient zeroing (embarrassingly parallel), and the parallel inverse FFT. See [[parproc-ch13-audio-image-processing]] §13.5.1.

## Dual Operation

Image smoothing (low-pass) and [[EdgeDetection]] (high-pass) are dual operations in the frequency domain. Smoothing removes high-frequency terms; edge detection removes low-frequency terms. Both follow the same pipeline: forward DFT, coefficient manipulation, inverse DFT.

## Pixel Intensity Clamping

After smoothing, some pixel values may fall outside the valid range [0, 255]. Negative values should be discarded; values above 255 should be scaled down. Very faint results (near 0) may need multiplication by a constant ([[parproc-ch13-audio-image-processing]] §13.7).

## See Also

- [[DiscreteFourierTransform]] — the transform used for frequency-domain smoothing.
- [[FastFourierTransform]] — efficient computation.
- [[EdgeDetection]] — the dual high-pass filtering operation.
- [[FourierSeries]] — mathematical foundation.
- [[FFTW]] — CPU-parallel FFT library for implementation.
- [[CUFFT]] — GPU FFT library for implementation.
