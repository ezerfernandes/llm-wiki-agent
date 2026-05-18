---
title: "R-CNN (Regions with CNN features)"
type: concept
tags: [computer-vision, object-detection, model]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# R-CNN (Regions with CNN features)

The seminal CNN-based object detector. [[RossGirshick|Girshick]], Donahue, Darrell & Malik 2014 (`Girshick.Donahue.Darrell.ea.2014`) — the pioneering work that "started the [[ObjectDetection|object-detection]] era of deep learning" per [[d2l-computer-vision]] §`rcnn`.

## Pipeline

1. **Region proposals:** apply [[SelectiveSearch]] (Uijlings et al. 2013) to extract ~2000 candidate regions per image at multiple scales / shapes.
2. **Feature extraction:** for *each* region, resize to the CNN's input size and forward-propagate through a pretrained CNN (e.g. [[AlexNet]]) truncated before the classifier. Extract the fixed-length feature vector (typically the penultimate FC activation).
3. **Classification:** train one [[SVM|support vector machine]] per class on the extracted features.
4. **Bounding-box regression:** train a linear regressor to refine the proposal box to the ground-truth box.

## The fatal cost

The model performs ~2000 independent CNN forward passes per image — most of which compute redundant features over overlapping regions. Per [[d2l-computer-vision]]: "Imagine that we select thousands of region proposals from a single input image: this requires thousands of CNN forward propagations to perform object detection. This massive computing load makes it infeasible to widely use R-CNNs in real-world applications."

## Lineage of improvements

The bottleneck motivated three major successors, all by [[RossGirshick|Girshick]] and collaborators:

- **[[FastRCNN]]** (Girshick 2015) — share one CNN forward pass across all proposals via [[ROIPooling|RoI pooling]].
- **[[FasterRCNN]]** ([[ShaoqingRen|Ren]], [[KaimingHe|He]], Girshick et al. 2015) — replace [[SelectiveSearch]] with a learned [[RegionProposalNetwork|Region Proposal Network]].
- **[[MaskRCNN]]** ([[KaimingHe|He]], Gkioxari, Dollár, Girshick 2017) — add [[ROIAlign]] + pixel-mask head for [[InstanceSegmentation]].

This R-CNN → Fast → Faster → Mask lineage is the canonical two-stage detector family — contrast with the single-stage [[SSD]] / YOLO lineage.

## Why R-CNN historically matters

- Demonstrated that ImageNet-pretrained CNN features (transferred via [[FineTuning]]) dramatically outperformed hand-engineered features (HOG, SIFT) on detection benchmarks — a 30%+ mAP jump on Pascal VOC.
- Established the **region proposals → CNN features → per-region classification** template that survives in modified form through Faster / Mask R-CNN.

## Connections

- [[ObjectDetection]] / [[SelectiveSearch]] / [[FineTuning]] / [[TransferLearning]] / [[SVM]] / [[BoundingBox]].
- [[RossGirshick]] — lead author of the entire R-CNN family.
- [[FAIR]] / [[MicrosoftResearch]] — institutional origins (Berkeley → MSR → FAIR).
