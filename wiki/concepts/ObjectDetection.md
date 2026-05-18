---
title: "Object Detection"
type: concept
tags: [computer-vision, task]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Object Detection

Computer-vision task of identifying *both* the category and the spatial location of every object of interest in an image. Generalizes image classification (which assumes one major object per image) to multi-object localization. Per [[d2l-computer-vision]] §`bounding-box`: "We not only want to know their categories, but also their specific positions in the image."

## Output format

For each detected object: a class label + a [[BoundingBox|bounding box]] (and optionally a confidence score). Modern variants extend this with pixel-level masks ([[InstanceSegmentation]]) or 3D / keypoint information.

## Application domains (per [[d2l-computer-vision]])

- **Self-driving:** detect vehicles, pedestrians, road signs, obstacles ([[Tesla]] perception stack).
- **Robotics:** navigation, manipulation target identification.
- **Security:** intruder / weapon detection.
- **Medical imaging:** lesion / tumor localization.
- **Retail / inventory:** product counting on shelves.

## Two model families

1. **Single-stage detectors** — predict class + bbox per anchor in one forward pass.
   - [[SSD]] ([[WeiLiu|Liu]] et al. 2016) — multiscale feature maps + per-pixel anchor classification + offset regression.
   - YOLO family (Redmon et al. 2016+) — flagged in [[d2l-computer-vision]] exercises.
   - RetinaNet — adds focal loss to handle class imbalance.

2. **Two-stage detectors** — first propose regions, then classify.
   - [[RCNN]] ([[RossGirshick|Girshick]] et al. 2014) — selective-search proposals + per-proposal CNN + SVMs.
   - [[FastRCNN]] (Girshick 2015) — one CNN forward pass + [[ROIPooling]].
   - [[FasterRCNN]] ([[ShaoqingRen|Ren]], [[KaimingHe|He]], Girshick et al. 2015) — learned [[RegionProposalNetwork|Region Proposal Network]] replaces selective search.
   - [[MaskRCNN]] ([[KaimingHe|He]], Gkioxari, Dollár, Girshick 2017) — adds [[ROIAlign]] + pixel-mask head for [[InstanceSegmentation]].

3. **End-to-end set-prediction detectors** (post-D2L) — DETR (Carion et al. 2020) replaces anchors + NMS with bipartite matching on a fixed set of object queries; the current "anchor-free" frontier.

## Primitives the task requires

- [[BoundingBox]] (corner ↔ center-size representations).
- [[AnchorBox]] (candidate hypotheses parameterized by scale + aspect ratio).
- [[IntersectionOverUnion]] (similarity / matching metric).
- [[NonMaxSuppression]] (deduplication).
- [[MultiscaleObjectDetection]] (handle objects of varying sizes via feature pyramids).
- [[ROIPooling]] / [[ROIAlign]] (fixed-shape feature extraction from variable regions).
- [[RegionProposalNetwork]] (learned proposal generation).
- [[SelectiveSearch]] (classical proposal generation).

## Connections

- [[ComputerVision]] — parent task.
- [[SemanticSegmentation]] / [[InstanceSegmentation]] — denser-than-bbox alternatives.
- [[CNN]] / [[ResNet]] / [[VGG]] — backbone networks all detectors pretrain.
