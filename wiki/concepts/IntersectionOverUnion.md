---
title: "Intersection over Union (IoU)"
type: concept
tags: [computer-vision, object-detection, metric]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Intersection over Union (IoU)

The Jaccard index applied to bounding-box pixel sets. Defined for sets $\mathcal{A}, \mathcal{B}$ as

$J(\mathcal{A}, \mathcal{B}) = \frac{|\mathcal{A} \cap \mathcal{B}|}{|\mathcal{A} \cup \mathcal{B}|} \in [0, 1].$

For two boxes, IoU = (area of intersection) / (area of union). IoU = 0 → disjoint; IoU = 1 → identical. Per [[d2l-computer-vision]] §`anchor`: "Intersection over union (IoU), also known as Jaccard index, measures the similarity of two bounding boxes."

## Vectorized implementation

`box_iou(boxes1, boxes2)` ([[d2l-computer-vision]]):

```
inter_upperlefts = max(boxes1[:, None, :2], boxes2[:, :2])
inter_lowerrights = min(boxes1[:, None, 2:], boxes2[:, 2:])
inters = clamp(inter_lowerrights - inter_upperlefts, min=0)
inter_areas = inters[..., 0] * inters[..., 1]
return inter_areas / (areas1[:, None] + areas2 - inter_areas)
```

Returns a `(|boxes1|, |boxes2|)` matrix.

## Roles in detection

1. **Anchor↔ground-truth assignment** at training time: highest-IoU greedy matching, threshold = 0.5.
2. **[[NonMaxSuppression|NMS]]** at inference time: suppress predicted boxes whose IoU with a higher-scoring box exceeds threshold (default 0.5).
3. **Evaluation metric:** mean Average Precision (mAP) at IoU = 0.5 (Pascal VOC convention) or averaged over IoU = 0.5:0.05:0.95 (COCO convention).

## Variants flagged in [[d2l-computer-vision]] exercises

- **Soft-NMS** (Bodla et al. 2017) — replace hard removal with score decay.
- Differentiable IoU losses (GIoU, DIoU, CIoU) — used in modern detectors.

## Connections

- [[BoundingBox]] / [[AnchorBox]] / [[NonMaxSuppression]] / [[ObjectDetection]] / [[SSD]] / [[FasterRCNN]].
- [[JaccardIndex]] generalization — IoU on arbitrary set comparisons.
