---
title: "Median filter (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, image-processing, digital-signal-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Median_filter
---

## Summary
This task asks the programmer to implement a median filter on an image: for each pixel, replace its color with the median color value taken over a surrounding neighbourhood (window) of pixels. Unlike a mean/blur filter, the median is robust to outliers, which makes it effective at removing salt-and-pepper noise while preserving edges. The task suggests reusing PPM read/write helpers to test the implementation on real images.

## Task Requirements
- For each pixel, examine its neighbourhood and compute the median color value.
- Replace the pixel with that median, producing the filtered output image.
- The neighbourhood (window size) is the region over which the median is taken.
- Use the linked Read PPM / Write PPM file solutions to load and save test images.

## Language Coverage
27 languages implement this task, spanning systems, scripting, and array-oriented styles. Representative implementations include C, Rust, Go, D, Ada, OCaml, Java, Python, Ruby, Perl, J, and Wren.

## Connections
- [[MedianFilter]] — the nonlinear filtering technique itself
- [[ImageProcessing]] — the broader domain this task belongs to
- [[NoiseReduction]] — the primary practical motivation (e.g. salt-and-pepper noise)
- [[Median]] — the order statistic computed per neighbourhood
- [[PPMFormat]] — the test image format used for input/output

## Contradictions
- None — reference task page.
