---
title: "Activation-aware Weight Quantization (AWQ)"
type: concept
tags: [quantization, llm, inference, model-compression, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Activation-aware Weight Quantization (AWQ)

**An LLM weight-quantization method (Lin et al.) that protects only the ~1% most *salient* weights — salient by **activation** magnitude, not weight magnitude — in higher precision while quantizing the rest to INT4.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], the key distinction: a small weight times a large activation produces a large output contribution, so activation magnitude is the right salience signal.

## Systems impact

Protecting ~1% of weights enables effective INT4, reducing a 7B model from ~14 GB to ~3.5 GB. This attacks the primary bottleneck of generative inference — [[MemoryWall|memory-bandwidth-bound]] autoregressive decode, where the full weight set is reloaded every token — converting a bandwidth-bound bottleneck into a compute-bound operation on modern accelerators.

## Connections

- [[Quantization]] — weight-only quantization for LLMs; the chapter's decision framework recommends INT4 weights + FP16 activations for LLM decode.
- [[MemoryWall]] / [[ArithmeticIntensity]] — explains why bandwidth, not compute, is the LLM-decode binding constraint.
- [[Calibration]] — AWQ replaces uniform calibration with activation-aware salience.
- [[mlsysbook-ch10-model-compression]] — source.
