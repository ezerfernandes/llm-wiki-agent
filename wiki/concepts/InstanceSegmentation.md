---
title: "Instance Segmentation"
type: concept
tags: [computer-vision, task]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Instance Segmentation

Pixel-level recognition of *individual object instances* — a strict generalization of [[SemanticSegmentation|semantic segmentation]] that distinguishes between different instances of the same class. Per [[d2l-computer-vision]] §`semantic-segmentation-and-dataset`: "Instance segmentation is also called *simultaneous detection and segmentation*. It studies how to recognize the pixel-level regions of each object instance in an image. Different from semantic segmentation, instance segmentation needs to distinguish not only semantics, but also different object instances. For example, if there are two dogs in the image, instance segmentation needs to distinguish which of the two dogs a pixel belongs to."

## Output

A list of `(bounding_box, class_id, per-pixel_mask)` tuples — one per detected instance. Equivalent to [[ObjectDetection|detection]] + per-detection pixel mask.

## Canonical model: [[MaskRCNN]]

[[KaimingHe|He]], Gkioxari, Dollár & [[RossGirshick|Girshick]] 2017. Extends [[FasterRCNN]] with:
- [[ROIAlign|RoI align]] (replaces [[ROIPooling|RoI pooling]] to preserve sub-pixel alignment).
- A per-RoI mask head: small [[FCN]] outputting a $K\times k\times k$ tensor of per-class binary masks; the predicted-class mask is selected at inference.

## Why it matters

Most real-world CV applications (autonomous driving, robotic manipulation, medical imaging) need to track *individual objects*, not just regions. Two pedestrians in a crosswalk must be reasoned about separately; two tumors must be measured separately. Instance segmentation provides the per-object pixel resolution that detection alone cannot.

## Connections

- [[SemanticSegmentation]] (less strict; doesn't distinguish instances).
- [[ObjectDetection]] (less strict; only bounding boxes).
- Panoptic segmentation (semantic + instance unified).
- [[MaskRCNN]] / [[ROIAlign]] / [[FCN]] / [[FasterRCNN]] / [[BoundingBox]].
