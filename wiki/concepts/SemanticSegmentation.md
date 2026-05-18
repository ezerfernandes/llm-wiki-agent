---
title: "Semantic Segmentation"
type: concept
tags: [computer-vision, task]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Semantic Segmentation

Computer-vision task of assigning a **class label to every pixel** of an image. Per [[d2l-computer-vision]] §`semantic-segmentation-and-dataset`: "Semantic segmentation recognizes and understands what are in images in pixel level: its labeling and prediction of semantic regions are in pixel level."

## Distinguished from related tasks

| Task | Output | Class? | Instances? |
|---|---|---|---|
| **Image classification** | One label per image | Yes | No |
| **[[ObjectDetection|Object detection]]** | Per-object bbox + label | Yes | Yes |
| **Image segmentation** (low-level) | Pixel clusters | No | No |
| **Semantic segmentation** | Per-pixel label | Yes | **No** (two dogs are one "dog" mask) |
| **[[InstanceSegmentation|Instance segmentation]]** | Per-instance pixel mask + label | Yes | Yes |
| **Panoptic segmentation** | Combination of semantic + instance | Yes | Yes |

The semantic-vs-instance distinction matters: a semantic-segmentation model has no concept of "object instance" — two dogs touching each other become one connected "dog" region.

## Canonical dataset: [[PascalVOC2012]]

- 21 classes (20 object classes + background).
- Label is an RGB image *shape-matched to the input image*, with a fixed colormap (`VOC_COLORMAP` in D2L) mapping each class to a unique RGB triple.
- White borders mark ambiguous pixels (typically masked from the loss).

## Data-handling constraint

Random scaling distorts label boundaries, so the only safe augmentation is **random cropping applied jointly to (image, label)** pairs. The crop coordinates must be identical for both. This is structurally different from image-classification augmentation.

## Canonical model: [[FCN|Fully Convolutional Network]]

[[JonathanLong|Long]], [[EvanShelhamer|Shelhamer]] & [[TrevorDarrell|Darrell]] 2015. A pretrained classification CNN (e.g. [[ResNet|ResNet-18]]) is converted to a fully convolutional architecture by:
1. Removing the global-average-pool + FC head.
2. Adding a $1\times1$ conv that maps the feature-channel count to $K$ = number of classes.
3. Adding a [[TransposedConvolution|transposed-conv]] layer that upsamples the spatial dimensions back to the input image's resolution.

Output is shape `(batch, K, H, W)` of per-pixel class logits. Trained with per-pixel softmax cross-entropy.

## Successors (post-D2L)

- **U-Net** (Ronneberger et al. 2015) — encoder-decoder with skip connections; the de facto medical imaging baseline.
- **DeepLab v3+** (Chen et al. 2018) — atrous convolutions + atrous spatial pyramid pooling for dense prediction.
- **Mask2Former** / **SegFormer** — transformer-based semantic / panoptic segmentation.

## Connections

- [[ObjectDetection]] / [[InstanceSegmentation]] / [[FCN]] / [[TransposedConvolution]] / [[BilinearInterpolation]] / [[PascalVOC2012]] / [[CNN]] / [[ResNet]] / [[ComputerVision]].
- [[MaskRCNN]] does instance segmentation, which is a strict generalization of semantic segmentation (and uses an FCN-style mask head internally).
