---
title: "Selective Search"
type: concept
tags: [computer-vision, object-detection, classical]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Selective Search

Classical (pre-deep-learning) algorithm for generating object-detection **region proposals** — candidate bounding boxes likely to contain objects. Uijlings, Van de Sande, Gevers & Smeulders 2013 (`Uijlings.Van-De-Sande.Gevers.ea.2013`). Used as the proposal generator in [[RCNN]] (Girshick et al. 2014) and [[FastRCNN]] (Girshick 2015) before being replaced by the learned [[RegionProposalNetwork|RPN]] in [[FasterRCNN]] ([[ShaoqingRen|Ren]] et al. 2015).

## Algorithm

Bottom-up hierarchical grouping:

1. Over-segment the image into ~1000 small superpixels (e.g. via Felzenszwalb–Huttenlocher graph-based segmentation).
2. Compute pairwise similarities between adjacent regions across multiple cues (color histogram, texture, size, fill).
3. Greedily merge the most-similar adjacent regions, recompute similarities, repeat until one region remains.
4. Every region ever formed during the merging process becomes a region proposal — yielding ~2000 boxes per image at multiple scales and shapes.

## Strengths

- Hand-engineered to have **high recall** at the cost of low precision: ~98% of ground-truth objects are covered by at least one proposal.
- Multi-scale and multi-aspect-ratio by construction.
- Class-agnostic.

## Weaknesses (what motivated [[RegionProposalNetwork|RPN]])

- ~2 seconds per image on CPU — the dominant bottleneck in Fast R-CNN's wall-clock runtime.
- Hand-engineered similarity cues; not trainable; cannot adapt to new domains.
- ~2000 proposals required for good recall — 10× more than the ~300 RPN typically needs.

## Connections

- [[RCNN]] / [[FastRCNN]] — use selective search.
- [[FasterRCNN]] — replaces it with [[RegionProposalNetwork|RPN]].
- [[ObjectDetection]] / [[BoundingBox]] / [[AnchorBox]].
