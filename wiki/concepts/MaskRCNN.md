---
title: "Mask R-CNN"
type: concept
tags: [computer-vision, object-detection, instance-segmentation, model]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Mask R-CNN

Fourth-generation R-CNN. [[KaimingHe|He]], Gkioxari, Dollár & [[RossGirshick|Girshick]] 2017 (`He.Gkioxari.Dollar.ea.2017`). Extends [[FasterRCNN]] from object detection to [[InstanceSegmentation|instance segmentation]] by adding a pixel-level mask head and replacing [[ROIPooling|RoI pooling]] with [[ROIAlign|RoI align]]. Per [[d2l-computer-vision]] §`rcnn`.

## Two changes from [[FasterRCNN]]

1. **[[ROIAlign|RoI align]] replaces [[ROIPooling]].** RoI pooling rounds region coordinates to feature-map grid cells, introducing ~1-pixel spatial misalignment that's catastrophic for pixel-level prediction. RoI align uses *bilinear interpolation* to sample the feature map at continuously-valued coordinates, preserving spatial alignment.
2. **Per-RoI mask head.** A small [[FCN|fully convolutional network]] applied to each RoI's aligned feature tensor outputs a per-pixel binary mask (one channel per class). Decoupling class prediction from mask prediction (sigmoid per channel, not softmax across channels) avoids inter-class competition.

## Output per RoI

- Class probabilities ($q+1$ classes including background).
- Bounding-box offsets (4 numbers).
- Pixel-level binary mask ($k \times k$ per class, e.g. $28\times28$).

→ class + bbox + mask = full **instance** segmentation: one segmentation mask *per detected object instance*, distinguishing two dogs in the same image as two separate masks.

## Training loss

Multi-task: $L = L_\text{cls} + L_\text{box} + L_\text{mask}$, where $L_\text{mask}$ is per-pixel binary cross-entropy on the predicted-class channel only (other channels get zero gradient).

## Why this matters

Per [[d2l-computer-vision]]: "Based on the faster R-CNN, the mask R-CNN additionally introduces a fully convolutional network, so as to leverage pixel-level labels to further improve the accuracy of object detection." Mask R-CNN became the de facto baseline for instance segmentation on COCO from 2017 onward; the [[Detectron2]] framework was largely built around it.

## Connections

- [[RCNN]] → [[FastRCNN]] → [[FasterRCNN]] → Mask R-CNN (R-CNN family).
- [[ROIAlign]] / [[ROIPooling]] / [[BilinearInterpolation]] / [[FCN]] / [[InstanceSegmentation]] / [[SemanticSegmentation]] / [[ObjectDetection]].
- [[KaimingHe]] — also lead author of [[ResNet]] (the typical backbone here).
- Successors / variants: Mask R-CNN with FPN (Feature Pyramid Networks; the de facto recipe), Panoptic FPN (unifies semantic + instance segmentation).
