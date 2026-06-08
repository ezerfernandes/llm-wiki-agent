---
title: "MobileNetV3"
type: concept
tags: [deep-learning, cnn, edge, efficient-architecture, nas, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# MobileNetV3

**A hardware-aware-NAS-optimized successor to [[MobileNetV2]], tuned specifically for mobile hardware.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], its NAS search included a latency-prediction model estimating inference time on Pixel phones, so discovered architectures run efficiently on real devices rather than just minimizing theoretical FLOPs.

## Design insights

NAS discovered that **inverted residual blocks with squeeze-and-excitation layers and the h-swish activation** beat any prior MobileNet variant on the accuracy-latency trade-off — insights manual exploration would likely miss.

## In the chapter

Headlines the "4× MobileNet win" example: unoptimized MobileNetV3 (FP32) runs 8 FPS on mid-tier Android (too slow to ship); INT8 [[Quantization|quantization]] → 35 FPS, 3× lower energy/frame.

## Connections

- [[MobileNetV2]] — its predecessor (a chapter Lighthouse Model); [[DepthwiseSeparableConvolution]] — the shared core operation.
- [[NeuralArchitectureSearch]] — hardware-aware NAS produced it; [[EfficientNet]] / MnasNet are siblings.
- [[Quantization]] — INT8 is what made the background-blur feature shippable.
- [[mlsysbook-ch10-model-compression]] — source.
