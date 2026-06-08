---
title: "Image noise (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, random-number-generation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Image_noise
---

## Summary
The task asks the programmer to continuously generate and display a random black-and-white 320x240 image (each pixel independently black or white, like television static), while measuring and showing the frame rate in frames per second. The key challenge is performance: filling 76,800 pixels with random bits fast enough to report a meaningful FPS exercises the speed of random-number generation and raster blitting in each language.

## Task Requirements
- Generate a random black and white 320x240 image.
- Each pixel is independently chosen black or white (random noise / static).
- Render the image to the screen continuously in a loop.
- Compute and display the current frames per second (FPS).

## Language Coverage
56 languages implement this task, spanning low-level assembly through high-level scripting and array languages. Representative examples include C, C++, C#, Java, Python, Go, Haskell, Ruby, JavaScript, and 6502 Assembly.

## Connections
- [[RandomNumberGeneration]] — every pixel value comes from a pseudorandom source
- [[RasterGraphics]] — task is categorized under raster graphics operations
- [[Bitmap]] — the noise is written into a pixel buffer / bitmap
- [[PerformanceBenchmarking]] — FPS measurement turns the task into a throughput benchmark

## Contradictions
- None — reference task page.
