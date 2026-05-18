---
title: "Fast R-CNN"
type: concept
tags: [computer-vision, object-detection, model]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Fast R-CNN

Second-generation R-CNN. [[RossGirshick|Girshick]] 2015 (`Girshick.2015`). The major improvement over [[RCNN]]: **the CNN forward pass is performed once on the entire image**, not once per region proposal. Per [[d2l-computer-vision]] §`rcnn`.

## Pipeline

1. **Whole-image CNN forward pass:** input the *whole image* to a trainable backbone CNN. Output: feature maps of shape $1 \times c \times h_1 \times w_1$.
2. **Region proposals:** [[SelectiveSearch]] still generates ~2000 proposals (this is the remaining bottleneck that [[FasterRCNN]] will eliminate).
3. **[[ROIPooling|RoI pooling]]:** for each proposal, extract a fixed $h_2 \times w_2$ feature tensor from the appropriate region of the backbone's feature map (regardless of the proposal's input-image shape).
4. **Per-RoI heads:** flatten + FC → predict (a) class via softmax over $q+1$ classes (replacing R-CNN's per-class SVMs) and (b) bbox-offset via linear regression.

## Why this is fast

- The expensive CNN forward pass is **amortized across all proposals** instead of repeated 2000× per image.
- The CNN is now *trainable* end-to-end (R-CNN's CNN was frozen feature extractor + SVM head — a multi-stage pipeline).
- Per-proposal cost is just an RoI-pool + small FC head — milliseconds, not seconds.

## [[ROIPooling]] mechanics

RoI pooling differs from standard max-pooling in that *the output shape is fixed by the layer*, not by the pooling-window arithmetic. For a region of shape $h \times w$ projected onto the feature map and a target output shape $h_2 \times w_2$:

1. Divide the region into an $h_2 \times w_2$ grid of subwindows.
2. Each subwindow has approximate shape $(h/h_2) \times (w/w_2)$.
3. Output the **max** of each subwindow.

D2L's worked example: a $3\times3$ region on a $4\times4$ feature map with target $2\times2$ output produces a $2\times2$ tensor of subwindow-maxima. PyTorch implementation: `torchvision.ops.roi_pool(X, rois, output_size, spatial_scale)`.

## Limitation that [[FasterRCNN]] fixes

[[SelectiveSearch]] proposal generation is still a non-trainable, CPU-bound bottleneck that dominates wall-clock time at inference. [[FasterRCNN]]'s [[RegionProposalNetwork|Region Proposal Network]] makes proposal generation a *learned, GPU-resident, jointly trained* component.

## Connections

- [[RCNN]] (predecessor) → Fast R-CNN → [[FasterRCNN]] → [[MaskRCNN]] (R-CNN family).
- [[ROIPooling]] / [[SelectiveSearch]] / [[ObjectDetection]] / [[BoundingBox]].
- [[RossGirshick]] — author.
