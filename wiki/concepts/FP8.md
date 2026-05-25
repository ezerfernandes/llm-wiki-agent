---
title: "FP8 — 8-Bit Float"
type: concept
tags: [numerics, floating-point, quantization]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# FP8 — 8-Bit Float

An 8-bit "minifloat" — half the bits of [[FP16]], a quarter the bits of [[FP32]]. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]: *"You can keep parameter values as floats using one of the minifloat formats, such as FP8 (8 bits) and FP4 (4 bits)."*

## Two common variants

- **E4M3**: 1 sign + 4 exponent + 3 mantissa. More precision, less range. Used for forward-pass activations.
- **E5M2**: 1 sign + 5 exponent + 2 mantissa. More range, less precision. Used for gradients (which span more orders of magnitude).

Hardware (NVIDIA Hopper, Blackwell) supports both and lets workloads choose per-tensor.

## Where FP8 sits in the stack

FP8 is a **training-and-inference-viable** lower-precision format. Unlike [[INT8]] / [[INT4]] which are typically inference-only, FP8 retains enough range and precision for training when used in [[MixedPrecisionTraining|mixed precision]] (with FP32 master weights).

## Trade-offs

- **Memory**: 50% smaller than [[FP16]].
- **Throughput**: tensor cores can do 2× more FP8 ops/cycle than FP16.
- **Precision**: significant — gradient noise from FP8 can derail training if not paired with loss scaling + per-tensor scaling.

## Connections

- [[FP16]] / [[BF16]] / [[FP4]] — neighboring float formats.
- [[INT8]] — alternative 8-bit format (integer rather than float).
- [[Quantization]] — the family of techniques FP8 enables.
- [[MixedPrecisionTraining]] — typical usage mode.
- [[NumericalRepresentation]] — umbrella concept.
- [[NVIDIA]] — Hopper / Blackwell native support.
- [[ai-engineering-ch07-finetuning]] — primary source.
