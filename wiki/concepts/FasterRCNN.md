---
title: "Faster R-CNN"
type: concept
tags: [computer-vision, object-detection, model]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Faster R-CNN

Third-generation R-CNN. [[ShaoqingRen|Ren]], [[KaimingHe|He]], [[RossGirshick|Girshick]] & Sun 2015 (`Ren.He.Girshick.ea.2015`). The major improvement over [[FastRCNN]]: replace the non-trainable, CPU-bound [[SelectiveSearch]] proposal generator with a **learned, jointly-trained [[RegionProposalNetwork|Region Proposal Network]] (RPN)**. Per [[d2l-computer-vision]] §`rcnn`.

## Pipeline

```
input image
   ↓
backbone CNN (e.g. [[ResNet|ResNet-50]] / [[VGG]])
   ↓
feature map
   ↓ ┌──────────────────────────────────┐
   ↓ │ Region Proposal Network (RPN):   │
   ↓ │  3×3 conv → c-dim feature        │
   ↓ │  per-pixel anchors at scales/    │
   ↓ │   aspect ratios                  │
   ↓ │  per-anchor:                     │
   ↓ │    binary class (obj/bg)         │
   ↓ │    bbox offset regression        │
   ↓ │  → NMS → top-N region proposals  │
   ↓ └──────────────────────────────────┘
   ↓        ↓
   └─→ [[ROIPooling|RoI pooling]] using RPN proposals on backbone features
                  ↓
            per-RoI head: class softmax + bbox regression
```

## Region Proposal Network

Per [[d2l-computer-vision]] §`rcnn`, the RPN works in four steps:

1. $3\times3$ conv with padding 1 transforms the backbone feature map into a new $c$-channel map. Each spatial unit now has a length-$c$ feature vector.
2. Centered on each pixel of the feature map, generate multiple [[AnchorBox|anchor boxes]] at different scales and aspect ratios.
3. The length-$c$ feature vector predicts (a) binary class (object vs background) and (b) 4-vector bbox offset for each of its anchors.
4. Keep only "object" predictions, apply [[NonMaxSuppression|NMS]]. The survivors are the region proposals fed to RoI pooling.

## End-to-end joint training

Critical innovation: "as part of the faster R-CNN model, the region proposal network is jointly trained with the rest of the model. In other words, the objective function of the faster R-CNN includes not only the class and bounding box prediction in object detection, but also the binary class and bounding box prediction of anchor boxes in the region proposal network" ([[d2l-computer-vision]]). The RPN *learns* what regions are likely to contain objects — yielding higher-quality proposals than [[SelectiveSearch]] with $\sim10\times$ fewer of them.

## Speedup

Selective search: ~2 seconds per image (CPU). RPN: ~10 ms per image (GPU). Net effect: Faster R-CNN is genuinely real-time or near-real-time on Pascal VOC at the time of publication.

## Connections

- [[RCNN]] → [[FastRCNN]] → Faster R-CNN → [[MaskRCNN]] (R-CNN family).
- [[RegionProposalNetwork]] / [[AnchorBox]] / [[ROIPooling]] / [[NonMaxSuppression]] / [[ObjectDetection]].
- [[ShaoqingRen]] / [[KaimingHe]] / [[RossGirshick]] — authors.
- Architectural cousin of [[SSD]]: both predict per-anchor class + offset from per-pixel feature vectors. RPN is a *binary* per-anchor classifier (then re-classified per RoI); SSD does the multi-class prediction in one shot.
