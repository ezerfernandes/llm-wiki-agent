---
title: "Anchor Box"
type: concept
tags: [computer-vision, object-detection]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Anchor Box

A pre-defined candidate [[BoundingBox|bounding box]] used to parameterize object hypotheses at training and inference time. Originated in [[FasterRCNN]]'s Region Proposal Network and popularized by [[SSD]]; central to almost every pre-DETR object detector.

## Generation (per [[d2l-computer-vision]] §`anchor`)

Centered on each pixel of an image of height $h$ and width $w$, generate boxes parameterized by:

- **Scale** $s \in (0, 1]$ — fraction of image dimension.
- **Aspect ratio** $r > 0$ — width-to-height ratio.

→ anchor width $= w s \sqrt{r}$, height $= h s / \sqrt{r}$.

For $n$ scales and $m$ aspect ratios, the naive product gives $whnm$ anchors. D2L's pragmatic shortcut: take only the $n + m - 1$ pairs that include $s_1$ or $r_1$, i.e.

$(s_1, r_1), (s_1, r_2), \ldots, (s_1, r_m), (s_2, r_1), \ldots, (s_n, r_1)$.

Implemented in `multibox_prior(data, sizes, ratios)` → tensor of shape `(1, num_anchors, 4)` with normalized corner coordinates.

## Anchor-box training labels = (class, offset)

Greedy assignment to ground-truth boxes via the $|A|\times|B|$ [[IntersectionOverUnion|IoU]] matrix:

1. Pick the max-IoU pair, assign that ground-truth box to that anchor, discard the row and column.
2. Repeat until all $n_b$ ground-truth boxes are assigned.
3. For remaining anchors, assign the highest-IoU ground-truth box only if IoU > `iou_threshold` (default 0.5); else label as **background**.

Offsets are encoded with normalization that yields uniformly-distributed targets:

$\left( \frac{(x_b - x_a)/w_a - \mu_x}{\sigma_x}, \frac{(y_b - y_a)/h_a - \mu_y}{\sigma_y}, \frac{\log(w_b / w_a) - \mu_w}{\sigma_w}, \frac{\log(h_b / h_a) - \mu_h}{\sigma_h}\right)$

with default $\mu = 0$, $\sigma_{xy} = 0.1$, $\sigma_{wh} = 0.2$. Negative (background) anchors get zero offset + mask = 0 so their loss is ignored.

## Multiscale anchors

Generating anchors at every pixel of a $561 \times 728$ image yields >2M anchors. Practical approach ([[MultiscaleObjectDetection]]): generate anchors on a *feature map* whose units' [[ReceptiveField|receptive fields]] match the object size at that scale — smaller maps (closer to output, larger receptive fields) detect larger objects.

## Connections

- [[BoundingBox]] / [[IntersectionOverUnion]] / [[NonMaxSuppression]] / [[MultiscaleObjectDetection]].
- [[SSD]] / [[FasterRCNN]] — use anchors as the candidate hypothesis space.
- Anchor-free detectors (CenterNet, FCOS, DETR) eliminate this primitive; flagged in [[d2l-computer-vision]] exercises as a research direction.
