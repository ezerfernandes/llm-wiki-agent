---
title: "Region Proposal Network (RPN)"
type: concept
tags: [computer-vision, object-detection, model-component]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Region Proposal Network (RPN)

Small, fully-convolutional network that generates [[ObjectDetection|object-detection]] region proposals from a backbone feature map. Introduced in [[FasterRCNN]] ([[ShaoqingRen|Ren]], [[KaimingHe|He]], [[RossGirshick|Girshick]] et al. 2015). Per [[d2l-computer-vision]] §`rcnn` — replaces the slow CPU-bound [[SelectiveSearch]] with a learned, GPU-resident, jointly-trained alternative.

## Four-step operation

1. **$3\times3$ conv** with padding 1 transforms the backbone feature map into a new $c$-channel map. Each spatial unit now has a length-$c$ feature vector.
2. **Anchor generation:** centered on each pixel of the feature map, place multiple [[AnchorBox|anchor boxes]] at varying scales and aspect ratios (typically 9 = 3 scales × 3 ratios).
3. **Per-anchor prediction heads:** two $1\times1$ convs over the $c$-dim feature vector — one outputs **binary classification** (object vs background) per anchor, the other outputs the **4-vector bbox offset** per anchor.
4. **NMS + top-K:** keep "object" anchors, apply [[NonMaxSuppression|NMS]], take the top-K (e.g. 300) as final region proposals.

## Joint training

RPN is trained jointly with the downstream Fast R-CNN head. The total loss is

$L = L_\text{RPN, cls} + L_\text{RPN, box} + L_\text{Fast, cls} + L_\text{Fast, box}$,

where RPN's classification loss is a binary cross-entropy over object/background labels (assigned by IoU thresholds: anchor is "positive" if max IoU with any ground-truth box > 0.7, "negative" if < 0.3, ignored otherwise). RPN's box loss is smooth-L1 on positive anchors only.

## Why this works

Anchor boxes give a dense, fixed parameterization of the proposal space; the RPN's job is just to learn which of them are likely to contain objects — a much easier learning problem than free-form region generation. The backbone features (already trained for classification) provide rich object-vs-background signal at every pixel.

## Speedup vs [[SelectiveSearch]]

- Selective search: ~2 seconds per image (CPU).
- RPN: ~10 ms per image (GPU).

→ end-to-end Faster R-CNN runs at ~5 FPS on a single GPU vs. R-CNN's ~10 seconds per image.

## Connections

- [[FasterRCNN]] (introducing paper) / [[MaskRCNN]] (also uses RPN).
- [[AnchorBox]] / [[SelectiveSearch]] (predecessor it replaces) / [[NonMaxSuppression]].
- Architectural cousin of [[SSD]]'s per-pixel class+bbox heads — but RPN is class-agnostic (binary), then the Fast R-CNN head does multi-class classification per RoI.
