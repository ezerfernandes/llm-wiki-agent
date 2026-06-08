---
title: "Image convolution (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, image-processing, linear-algebra, signal-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Image_convolution
---

## Summary
The task is to implement a generic image filter built on convolution with a small kernel matrix. Each output pixel is computed as the weighted sum of the pixels in a sliding window centered on it, using the kernel coefficients as weights. The key insight is that many classic image effects (blur, sharpen, edge detection, emboss) are just the same convolution operation with different kernels, so a single generic routine can express them all.

## Task Requirements
- Write a generic 3x3 kernel convolution filter for images.
- For a window centered at pixel (i, j), compute the new value as the sum over k, l of P(i+k, j+l) * K(k, l), where the kernel is square with width W = 2R+1.
- Handle grayscale directly; for color images, filter each channel independently.
- Optionally demonstrate end-user filters (e.g. blur, sharpen, edge detect) that call the generic convolution.
- The provided Read PPM / Write PPM file solutions may be used to load and save test images.

## Language Coverage
30 languages implement this task, ranging from low-level systems languages to array and functional languages. Representative implementations include C, Ada, D, Go, Java, JavaScript, Python, OCaml, Julia, Racket, Ruby, and the array-oriented J and Uiua.

## Connections
- [[Convolution]] — the core mathematical operation applied with a sliding window.
- [[KernelImageProcessing]] — the matrix of coefficients that defines each filter.
- [[ImageProcessing]] — the broader domain (blur, sharpen, edge detection) this task serves.
- [[MatrixMultiplication]] — the elementwise multiply-and-sum at the heart of each window evaluation.
- [[ReadPpmFile]] — companion task supplying the image I/O used for testing.

## Contradictions
- None — reference task page.
