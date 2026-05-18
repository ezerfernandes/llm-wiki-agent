---
title: "Edge Detection"
type: concept
tags: [image-processing, signal-processing, frequency-domain, computer-vision, parallel-computing]
sources: [parproc-ch13-audio-image-processing]
last_updated: 2026-05-17
---

# Edge Detection

Edge detection identifies pixels in an image that form the boundaries of objects — places where pixel intensity changes sharply in the horizontal or vertical direction. It is a core operation in computer vision, used for face recognition, object segmentation, and speech segmentation.

## What Is an Edge?

An edge is a set of pixels at which there is a sharp change in intensity. Mathematically, this corresponds to a large magnitude of the spatial gradient (partial derivatives of intensity in the x and y directions). Edges appear as high-frequency components in the frequency domain.

## Spatial-Domain Approach

Compute approximate partial derivatives of intensity by finite differences between neighboring pixel values. This is equivalent to applying a gradient filter (e.g., a Sobel operator) convolved with the image. The result highlights areas of rapid intensity change.

## Frequency-Domain Approach (High-Pass Filter)

The Fourier-based method ([[parproc-ch13-audio-image-processing]] §13.5.3):

1. Compute the [[DiscreteFourierTransform]] (DFT) of the image.
2. Set the low-frequency DFT coefficients to zero — delete small-r, small-s terms.
3. Apply the inverse DFT to recover an edge-enhanced image in the spatial domain.

Since edges correspond to sharp intensity transitions, they are encoded in the high-frequency components. Removing the low-frequency (slowly-varying) components isolates the edges. This is called a **high-pass filter**: high frequencies pass through and low frequencies are blocked.

The result visually resembles a charcoal sketch — the smooth regions become dark (near-zero intensity) and the edges stand out as bright lines.

## Application to Audio / Speech

Edge detection concepts extend to 1-D signals: in speech recognition, finding where sounds like "ah" or "ee" begin and end is analogous to detecting edges in the time-domain signal. The high-pass filter approach identifies abrupt transitions in the audio waveform.

## Parallelization

Identical to [[ImageSmoothing]] parallelization:
- The forward 2-D DFT uses the separability property (row FFTs then column FFTs), parallelized across threads/nodes owning groups of rows and columns.
- The coefficient manipulation (zeroing low-frequency terms) is embarrassingly parallel.
- The inverse DFT is parallelized by the same strategies as the forward DFT.

## Relationship to Smoothing

Image smoothing ([[ImageSmoothing]]) and edge detection are dual frequency-domain operations:

| Operation | Filter type | Coefficients zeroed | Effect |
|---|---|---|---|
| Smoothing | Low-pass | High-frequency (large r, s) | Removes noise, blurs detail |
| Edge detection | High-pass | Low-frequency (small r, s) | Highlights boundaries |

Both share the same pipeline: forward DFT → coefficient manipulation → inverse DFT. Parallelization is identical in both cases.

## Pixel Intensity Clamping

After edge detection, intensity values may be negative or exceed 255. Negative values are discarded and large values are scaled down. The result may also be very faint (near zero) and may need amplification ([[parproc-ch13-audio-image-processing]] §13.7).

## See Also

- [[DiscreteFourierTransform]] — the transform used for frequency-domain edge detection.
- [[FastFourierTransform]] — efficient computation.
- [[ImageSmoothing]] — the dual low-pass filtering operation.
- [[FourierSeries]] — mathematical foundation.
- [[FFTW]] — CPU-parallel FFT library.
- [[CUFFT]] — GPU FFT library.
