---
title: "RoI Pooling"
type: concept
tags: [computer-vision, object-detection, layer]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# RoI Pooling

Pooling layer that extracts a **fixed-shape** feature tensor from a **variable-shape** region of an input feature map. Introduced in [[FastRCNN]] (Girshick 2015). Per [[d2l-computer-vision]] §`rcnn`.

## How it differs from standard pooling

| | Standard pooling | RoI pooling |
|---|---|---|
| **Output shape** | Determined indirectly via (window, stride, padding) | Specified directly as a layer parameter ($h_2 \times w_2$) |
| **Input region** | Sliding window over the whole input | A single, externally-specified region (RoI) |
| **Purpose** | Local invariance / downsample | Fixed-shape per-region feature for per-RoI heads |

## Algorithm

For an RoI of shape $h \times w$ projected onto the feature map and target output shape $h_2 \times w_2$:

1. Divide the RoI into an $h_2 \times w_2$ grid of subwindows.
2. Each subwindow has approximate shape $(h/h_2) \times (w/w_2)$ — round up for non-integer divisions.
3. Each subwindow's output is the **max** of its feature values.

D2L worked example: a $3\times3$ RoI on a $4\times4$ feature map with target $2\times2$ produces a $2\times2$ output of subwindow-maxima.

## API

`torchvision.ops.roi_pool(X, rois, output_size, spatial_scale)` — `spatial_scale` scales RoI coordinates from input-image space to feature-map space (e.g. 0.1 for a backbone that downsamples 10×).

## Limitation → [[ROIAlign]]

RoI pooling **rounds** RoI coordinates to feature-map grid cells. The rounding errors (often ~1 pixel) accumulate through the subwindow grid and are catastrophic for pixel-level prediction tasks. [[MaskRCNN]] replaces RoI pooling with [[ROIAlign|RoI align]], which uses [[BilinearInterpolation|bilinear interpolation]] to sample at continuous coordinates without rounding — improving instance-segmentation mask quality by ~10% mAP.

## Connections

- [[FastRCNN]] / [[FasterRCNN]] (use RoI pooling); [[MaskRCNN]] (uses RoI align instead).
- [[ROIAlign]] — successor.
- [[BoundingBox]] / [[ObjectDetection]] / [[RegionProposalNetwork]] / [[SelectiveSearch]].
