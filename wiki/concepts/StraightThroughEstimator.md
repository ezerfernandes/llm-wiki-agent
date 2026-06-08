---
title: "Straight-Through Estimator (STE)"
type: concept
tags: [quantization, training, model-compression, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Straight-Through Estimator (STE)

**The gradient trick that makes [[QuantizationAwareTraining|quantization-aware training]] possible: during backpropagation, treat the non-differentiable rounding/clipping operation as if it were the identity function (derivative = 1) within the valid range.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]] (Bengio et al. 2013), this lets gradients flow unchanged through fake-quantization nodes whose true derivative is zero almost everywhere.

## Why it works (and its flaw)

$$ \frac{\partial x_{\text{fake}}}{\partial x} = \begin{cases} 1 & x \in [x_{\min}, x_{\max}] \\ 0 & \text{otherwise} \end{cases} $$

The approximation is correct in magnitude but **wrong in direction for weights near quantization boundaries** — a weight at 0.501 (rounds to 1.0) gets nearly the same gradient as one at 0.001 (rounds to 0.0) despite opposite fates. QAT compensates by letting the model adapt to these systematic gradient errors during training, which is precisely why QAT recovers accuracy that [[PostTrainingQuantization|PTQ]] cannot. Also used for binary/ternary network training.

## Connections

- [[QuantizationAwareTraining]] — STE is its enabling mechanism (fake-quant forward, STE backward).
- [[Quantization]] / [[Binarization]] — the non-differentiable ops STE approximates.
- [[mlsysbook-ch10-model-compression]] — source.
