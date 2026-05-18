---
title: "Pascal VOC 2012"
type: concept
tags: [computer-vision, dataset, semantic-segmentation]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Pascal VOC 2012

Classical computer-vision benchmark dataset; canonical for [[SemanticSegmentation|semantic segmentation]] in [[d2l-computer-vision]] §`semantic-segmentation-and-dataset`. ~2 GB. Hosted at [host.robots.ox.ac.uk/pascal/VOC/voc2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/).

## Layout

After extraction, the relevant subdirectories are:

- `ImageSets/Segmentation/{train,val}.txt` — image-ID splits.
- `JPEGImages/{id}.jpg` — input images.
- `SegmentationClass/{id}.png` — per-pixel class labels, encoded as a fixed RGB colormap.

## Semantic-segmentation labels

**21 classes** (20 object classes + background): `background, aeroplane, bicycle, bird, boat, bottle, bus, car, cat, chair, cow, diningtable, dog, horse, motorbike, person, potted plant, sheep, sofa, train, tv/monitor`. Each class maps to a unique RGB triple via the `VOC_COLORMAP` constant. White pixels mark ambiguous regions (typically masked from the loss).

D2L provides:
- `voc_colormap2label()` — builds a 256³-entry lookup table mapping RGB triples to class indices.
- `voc_label_indices(colormap, colormap2label)` — converts a label PNG to a `(H, W)` integer class-index tensor.

## Other tasks

Pascal VOC also supports:
- **Image classification:** which of the 20 classes are present.
- **[[ObjectDetection|Object detection]]:** bounding boxes for the 20 classes (the historical mAP@0.5 benchmark before COCO).
- **Action classification, person layout** (less common).

## Other benchmarks (post-VOC era)

- **COCO** (Common Objects in Context; Lin et al. 2014) — 80 classes, ~330k images, the modern standard.
- **Cityscapes** — 5k images of urban driving scenes; standard for autonomous-driving semantic segmentation.
- **ADE20K** — 150 classes, broader scene-parsing focus.

## Connections

- [[SemanticSegmentation]] (primary task in [[d2l-computer-vision]]).
- [[FCN]] — D2L's worked example trains an FCN on this dataset.
- [[ComputerVision]] / [[ImageNet]] (the larger pretraining source the backbones use).
