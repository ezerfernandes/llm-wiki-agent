---
title: "Fast Fourier transform (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, signal-processing, complex-numbers, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fast_Fourier_transform
---

## Summary
The task asks the programmer to compute the Fast Fourier Transform (FFT) of an input sequence, transforming it from the time domain to the frequency domain. The general case takes complex-number input and produces an equal-length complex-number output; for real-only inputs, the magnitude (sqrt(re² + im²)) of each complex result is reported. The canonical approach is the recursive Cooley–Tukey algorithm, which divides the sequence into even and odd indexed sub-sequences and combines them with twiddle factors.

## Task Requirements
- Calculate the FFT of an input sequence.
- Support complex-number input, producing an equal-length complex-number output sequence.
- For real-number-only output, report the magnitude sqrt(re² + im²) of each complex result.
- The classic recursive Cooley–Tukey FFT is the expected reference implementation; further optimizations are allowed but not required.

## Language Coverage
77 languages implement this task, spanning numeric/scientific platforms, array languages, and general-purpose languages. Representative implementations include C, C++, Python, Julia, Fortran, Haskell, J, MATLAB / Octave, Mathematica / Wolfram Language, and Rust.

## Connections
- [[FastFourierTransform]] — the algorithm the task implements
- [[CooleyTukeyAlgorithm]] — the classic recursive divide-and-conquer FFT
- [[ComplexNumbers]] — input and output domain of the transform
- [[DiscreteFourierTransform]] — the operation the FFT computes efficiently
- [[DivideAndConquer]] — the algorithmic strategy underlying the recursion

## Contradictions
- None — reference task page.
