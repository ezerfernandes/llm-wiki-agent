---
title: "Multiscale Object Detection"
type: concept
tags: [computer-vision, object-detection]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Multiscale Object Detection

Strategy for detecting objects of varying sizes using a CNN's hierarchical feature maps as a built-in scale pyramid. Generating [[AnchorBox|anchor boxes]] at every pixel of an input image is computationally infeasible — a $561\times728$ image with 5 anchors per pixel produces >2M anchors. The multiscale solution: place anchors on *feature maps at multiple depths*, where each unit's [[ReceptiveField|receptive field]] matches the target object size at that scale.

## Core mechanism ([[d2l-computer-vision]] §`multiscale-object-detection`)

- Feature maps **closer to the input** are larger spatially with small receptive fields → detect **smaller objects**, with many anchors.
- Feature maps **closer to the output** are smaller spatially with large receptive fields → detect **larger objects**, with fewer anchors.

If a layer outputs $c$ feature maps of shape $h \times w$, generate $hw$ sets of $a$ anchors each. The same $c$-channel feature vector at spatial position $(i, j)$ is then transformed (via a $3\times3$ conv) into:
- Class predictions: $a(q+1)$ output channels (where $q$ = number of object classes).
- Offset predictions: $4a$ output channels.

This packing of "$a$ anchors per pixel" into channel-space follows the [[NetworkInNetwork|NiN]] / [[SSD]] convention.

## Intuition (D2L's small-object argument)

"Smaller objects are more likely to appear on an image than larger ones. As an example, $1\times1$, $1\times2$, and $2\times2$ objects can appear on a $2\times2$ image in 4, 2, and 1 possible ways, respectively. Therefore, when using smaller anchor boxes to detect smaller objects, we can sample more regions, while for larger objects we can sample fewer regions."

## Operationalized in

- **[[SSD]]** — the canonical single-stage multiscale detector. Several feature-map blocks at progressively smaller resolutions, each with its own per-pixel anchor / class / offset prediction heads.
- **FPN (Feature Pyramid Networks; Lin et al. 2017)** — adds top-down + lateral connections to merge low-res-semantic and high-res-spatial features. Standard in modern detectors (RetinaNet, Mask R-CNN with FPN).

## Connections

- [[AnchorBox]] / [[BoundingBox]] / [[ReceptiveField]] / [[SSD]] / [[ObjectDetection]].
- The CNN-hierarchical-features insight is shared with [[FCN]] (semantic segmentation skip connections) and [[StyleTransfer]] (multi-layer style features) — all three exploit "different layers see different scales".
