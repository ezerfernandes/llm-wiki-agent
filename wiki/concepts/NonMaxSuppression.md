---
title: "Non-Maximum Suppression (NMS)"
type: concept
tags: [computer-vision, object-detection, algorithm]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Non-Maximum Suppression (NMS)

Greedy deduplication algorithm for predicted bounding boxes. When a detector emits multiple overlapping high-confidence boxes for the same object, NMS keeps the highest-confidence one and removes its neighbors.

## Algorithm (per [[d2l-computer-vision]] §`anchor`)

Given a list $L$ of predicted bounding boxes sorted by confidence in descending order, and threshold $\epsilon$:

1. Pick $B_1$ = highest-confidence box; remove all remaining boxes whose [[IntersectionOverUnion|IoU]] with $B_1$ exceeds $\epsilon$.
2. Pick $B_2$ = next-highest-confidence surviving box; repeat the IoU filter.
3. Continue until every kept box has been used as a basis.
4. Output the kept set.

Implemented in `nms(boxes, scores, iou_threshold)` and the full classification + offset → final-box pipeline in `multibox_detection(cls_probs, offset_preds, anchors, nms_threshold=0.5, pos_threshold=0.01)`.

Output shape: `(batch, num_anchors, 6)` where each row is `(class_id, confidence, x1, y1, x2, y2)`. `class_id = -1` marks suppressed / below-threshold boxes.

## Tuning

- Lower $\epsilon$ → more aggressive suppression → fewer but more confident outputs (risks merging genuinely separate objects).
- Higher $\epsilon$ → keep more boxes (risks duplicate detections per object).
- Default 0.5.

## Variants

- **Soft-NMS** (Bodla, Singh, Chellappa et al. 2017) — instead of removing, decay overlapping boxes' scores proportional to IoU. Suggested in [[d2l-computer-vision]] exercises.
- **Learned NMS** (Hosang, Benenson & Schiele 2017) — a small network replaces the greedy rule. Also flagged in exercises.
- **DIoU-NMS** / **WBF (weighted box fusion)** — combine rather than discard overlapping boxes; popular in detection competitions.
- DETR-style **bipartite matching** loss eliminates NMS entirely; the synonym for "what comes after anchor-based detection."

## Connections

- [[IntersectionOverUnion]] / [[BoundingBox]] / [[AnchorBox]] / [[ObjectDetection]] / [[SSD]] / [[RCNN]] / [[FasterRCNN]].
- Modern alternatives: end-to-end set prediction (DETR), one-to-one matching (YOLOv8+ NMS-free heads).
