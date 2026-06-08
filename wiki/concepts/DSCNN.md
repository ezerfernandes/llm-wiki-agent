---
title: "DS-CNN (Depthwise Separable CNN keyword spotter)"
type: concept
tags: [deep-learning, cnn, tinyml, keyword-spotting, efficient-architecture, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# DS-CNN (Depthwise Separable CNN keyword spotter)

**A depthwise-separable-convolution CNN used as the [[TinyML]] keyword-spotter Lighthouse Model throughout mlsysbook Vol 1.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], the ~500 KB DS-CNN is the *only* model in the deployment-gap table that fits a TinyML device (a ~512 KB budget) — purpose-built rather than compressed down from a larger net.

## Role in the compression chapter

The DS-CNN anchors the "Smart Doorbell Lighthouse": on an always-on microcontroller (~256 KB SRAM, coin-cell battery), FP32 consumes 4× more memory bandwidth and energy per inference than INT8, so [[Quantization|quantization]] toward INT4 or even binary becomes existential — *"a device that lasts one month on FP32 might last four months on INT8."*

## Connections

- [[DepthwiseSeparableConvolution]] — its core efficient operation.
- [[TinyML]] — the deployment regime it targets.
- [[Quantization]] / [[Binarization]] — required to fit the SRAM budget.
- [[ModelCompression]] — the discipline that makes the deployment possible.
- [[mlsysbook-ch10-model-compression]] — source.
