---
title: "Canny edge detector (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, image-processing, computer-vision, convolution]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Canny_edge_detector
---

## Summary
This task asks the programmer to implement the Canny edge detector, a multi-stage image-processing pipeline that extracts clean, thin edges from a grayscale image. The key insight is that good edge detection is not a single operation but a sequence: smooth out noise, find where intensity changes fastest, keep only the local peaks, and then link those peaks into continuous contours using two thresholds rather than one.

## Task Requirements
- **Noise reduction** — smooth the image, typically with a Gaussian filter/blur.
- **Intensity gradient** — compute the horizontal and vertical gradients (Gx and Gy), usually via convolution with Sobel operators, and the gradient magnitude G = sqrt(Gx^2 + Gy^2).
- **Non-maximum suppression** — compute the gradient orientation theta = atan2(Gy, Gx), quantize it to one of four directions (0, 45, 90, 135 degrees), and zero out any pixel that is not a local maximum of G along its gradient direction.
- **Hysteresis edge tracing** — apply two thresholds Tmin and Tmax: start from strong pixels (N(p) >= Tmax) and follow connected paths of pixels with N(p) >= Tmin, emitting them to the output image.

## Language Coverage
18 languages implement this task, spanning low-level systems languages, array/math-oriented languages, and high-level scripting languages. Representative implementations include C, D, Go, Java, Julia, Python, Perl, Raku, MATLAB / Octave, Mathematica / Wolfram Language, J, and Tcl.

## Connections
- [[ImageProcessing]] — the broader domain this task belongs to.
- [[Convolution]] — the core operation applied for both blurring and gradient estimation.
- [[GaussianBlur]] — the noise-reduction stage.
- [[SobelOperator]] — the convolution kernels used to estimate intensity gradients.
- [[EdgeDetection]] — the computer-vision problem the algorithm solves.

## Contradictions
- None — reference task page.
