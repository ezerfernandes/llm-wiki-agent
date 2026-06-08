---
title: "Quantization Calibration"
type: concept
tags: [quantization, inference, model-compression, mlsysbook]
sources: [mlsysbook-ch10-model-compression, mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Quantization Calibration

**The [[PostTrainingQuantization|PTQ]] step that selects the clipping range $[\alpha, \beta]$ for mapping floating-point weights/activations into a lower-precision integer range, using a small representative dataset.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], the quality of this range directly governs quantization error — a poorly chosen range causes large accuracy degradation.

## Methods

- **Max** — uses the maximum absolute value; simple but outlier-susceptible.
- **Entropy** — minimizes KL divergence between original and quantized distributions; TensorRT's default.
- **Percentile** — clips to a percentile (e.g. 99%), avoiding the long-tail outliers visible in ResNet-50 activation histograms.

Ranges can be **symmetric** (equal ±, zero preserved) or **asymmetric** (skew-aware, uses a zero-point $z$). Affine quant: $s=(\beta-\alpha)/(2^b-1)$, $z=\text{round}(-\alpha/s)$.

## Granularity

Layerwise → groupwise (Q-BERT) → **channelwise (the current standard, best accuracy/overhead balance)** → sub-channelwise.

## Connections

- [[PostTrainingQuantization]] — calibration is its core sub-step (no retraining, just a calibration set).
- [[Quantization]] — affine/scale/zero-point mechanics; [[ActivationAwareWeightQuantization|AWQ]] is an activation-aware variant.
- [[mlsysbook-ch12-benchmarking]] — Ch 12 makes the calibration dataset a **reproducibility requirement**: INT8 accuracy preservation (95–99% of FP32) depends on the calibration data's similarity to deployment data, so an INT8 benchmark that omits the calibration dataset and procedure is not reproducible. (Distinct from confidence [[ModelCalibration]], which [[ExpectedCalibrationError|ECE]] measures.)
- [[mlsysbook-ch10-model-compression]] — source.
