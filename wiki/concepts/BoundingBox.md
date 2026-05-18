---
title: "Bounding Box"
type: concept
tags: [computer-vision, object-detection]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Bounding Box

Rectangular axis-aligned region used to localize an object in an image — the primary geometric primitive of [[ObjectDetection]]. Origin convention in [[d2l-computer-vision]]: upper-left of the image is $(0, 0)$, +x right, +y down.

## Two equivalent representations

- **Corner format** $(x_1, y_1, x_2, y_2)$ — upper-left and lower-right pixel coordinates.
- **Center–size format** $(c_x, c_y, w, h)$ — center coordinates plus width and height.

D2L provides round-trip-correct converters `box_corner_to_center` and `box_center_to_corner`. Each representation has algorithmic advantages: corner format makes [[IntersectionOverUnion|IoU]] computation a simple `max(x1) / min(x2)` clip; center–size format makes offset regression and [[AnchorBox|anchor-box]] generation natural.

## Drawing

`matplotlib.patches.Rectangle(xy=(x1, y1), width=x2-x1, height=y2-y1, fill=False)`. D2L's `bbox_to_rect(bbox, color)` helper wraps this.

## In training labels

A detection training label for one object is typically `(class_id, x_1, y_1, x_2, y_2)` with pixel coordinates normalized to $[0, 1]$ by image width/height. Padded with `class_id = -1` rows for images with fewer objects than the batch maximum (so all images in a minibatch share label shape).

## Connections

- [[AnchorBox]] / [[IntersectionOverUnion]] / [[NonMaxSuppression]] / [[ObjectDetection]] — the bounding-box vocabulary stack.
- [[ROIPooling]] / [[ROIAlign]] — operate on bounding-box regions of a feature map.
- Future generalizations: rotated bounding boxes (text detection), polygon masks ([[InstanceSegmentation]]), point sets / keypoints (pose estimation).
