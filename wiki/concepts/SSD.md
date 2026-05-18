---
title: "SSD (Single-Shot Multibox Detection)"
type: concept
tags: [computer-vision, object-detection, model]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# SSD (Single-Shot Multibox Detection)

Single-stage anchor-based object detector. [[WeiLiu|Wei Liu]], Anguelov, Erhan et al. 2016 (`Liu.Anguelov.Erhan.ea.2016`). Per [[d2l-computer-vision]] §`ssd`: "This model is simple, fast, and widely used."

## Architecture

```
input image
   ↓
base network ([[VGG]] truncated before classifier, or [[ResNet]])
   ↓
[block 1]  feature map (e.g. 38×38) ──→ class head + bbox head
   ↓ downsample (halve spatial dims)
[block 2]  feature map (e.g. 19×19) ──→ class head + bbox head
   ↓ downsample
[block 3]  feature map (e.g. 10×10) ──→ class head + bbox head
   ↓ downsample
...
[block N]  feature map (e.g. 1×1)   ──→ class head + bbox head
   ↓
concatenate all anchors + predictions across scales
   ↓
[[NonMaxSuppression|NMS]] → final detections
```

## Class & bbox prediction heads

Each head is a $3\times3$ convolution that *preserves spatial dimensions* of the feature map (replacing fully-connected heads, which would have prohibitive parameter cost when $hwa$ anchors must be classified):

- **Class head:** output channels = $a(q+1)$ where $a$ = anchors per pixel, $q$ = object classes (+1 for background). Channel index $i(q+1) + j$ at spatial position $(x, y)$ = predicted class-$j$ probability for anchor $i$ centered at $(x, y)$.
- **Bbox head:** output channels = $4a$. Predicts the 4-vector offset relative to each anchor.

Per [[d2l-computer-vision]]: "Single-shot multibox detection uses the same technique to reduce model complexity" (referring to [[NetworkInNetwork|NiN]]'s use of channels-as-classes).

## Multiscale design

Each block halves the height and width, so each unit on a deeper feature map has a wider [[ReceptiveField|receptive field]] on the input image. Deeper blocks detect larger objects; earlier blocks detect smaller ones. See [[MultiscaleObjectDetection]] for the general principle.

## Training loss

Total = class loss + bbox loss, summed over all anchors:

- **Class loss:** softmax cross-entropy, including the background class (most anchors are negative).
- **Bbox loss:** smooth-L1 (Huber) on the offset residuals, multiplied by a mask that zeros out background anchors (their offsets don't matter).

## Inference

1. Forward pass produces per-anchor class probabilities + offsets.
2. Apply inverse offset transformation to recover absolute box coordinates (`offset_inverse`).
3. Run [[NonMaxSuppression|NMS]] per class (or class-agnostic).
4. Return surviving boxes above a confidence threshold.

## Pros / cons

- **Pros:** one forward pass, no separate proposal generation, GPU-friendly. Real-time on modest hardware.
- **Cons:** anchor design is sensitive (scales / aspect ratios must match data); single-stage detectors historically lagged two-stage on small-object accuracy until focal loss / FPN closed the gap.

## Connections

- [[ObjectDetection]] / [[AnchorBox]] / [[MultiscaleObjectDetection]] / [[NonMaxSuppression]].
- Contrast with two-stage: [[RCNN]] / [[FastRCNN]] / [[FasterRCNN]] / [[MaskRCNN]].
- Successors: RetinaNet (focal loss for class imbalance), YOLOv3+, EfficientDet, DETR (anchor-free).
- Base network: typically [[VGG]] or [[ResNet]] truncated before the classifier.
