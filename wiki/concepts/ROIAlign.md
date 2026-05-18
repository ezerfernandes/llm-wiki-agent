---
title: "RoI Align"
type: concept
tags: [computer-vision, object-detection, instance-segmentation, layer]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# RoI Align

Pooling layer that extracts a fixed-shape feature tensor from a variable-shape region of a feature map — like [[ROIPooling|RoI pooling]] — but uses [[BilinearInterpolation|bilinear interpolation]] instead of nearest-neighbor rounding to avoid spatial misalignment. Introduced in [[MaskRCNN]] ([[KaimingHe|He]], Gkioxari, Dollár & [[RossGirshick|Girshick]] 2017). Per [[d2l-computer-vision]] §`rcnn`: "This region of interest alignment layer uses bilinear interpolation to preserve the spatial information on the feature maps, which is more suitable for pixel-level prediction."

## Why bilinear interpolation matters

[[ROIPooling]] rounds RoI coordinates to integer grid cells at *two* levels:
1. When projecting the RoI from input-image coordinates to feature-map coordinates (`floor(x * spatial_scale)`).
2. When dividing the RoI into the output-shape grid of subwindows (rounding subwindow boundaries to integers).

Each rounding step introduces ~1 pixel of misalignment. For [[InstanceSegmentation|instance-segmentation]] masks at $28\times28$ output resolution that's a ~3.5% relative error per dimension — large enough to misalign object boundaries by full pixels in the final mask.

RoI align eliminates both rounding steps:
- RoI coordinates stay continuous (floating-point).
- Subwindow boundaries stay continuous.
- Each subwindow samples its feature value at 4 regularly-spaced continuous points via [[BilinearInterpolation|bilinear interpolation]] from the 4 nearest integer feature-map cells, then averages (or max-pools) those 4 samples.

## Empirical impact

In [[MaskRCNN]], swapping RoI pooling → RoI align improves instance-segmentation mask AP by ~10% (a substantial single-change improvement). The improvement is concentrated in small objects and tight masks.

## API

`torchvision.ops.roi_align(X, rois, output_size, spatial_scale, sampling_ratio)` — `sampling_ratio = 2` is typical (4 sample points per subwindow).

## Connections

- [[ROIPooling]] (predecessor; the thing RoI align replaces).
- [[BilinearInterpolation]] — the underlying interpolation primitive.
- [[MaskRCNN]] — introducing paper.
- [[InstanceSegmentation]] / [[ObjectDetection]] — applications.
