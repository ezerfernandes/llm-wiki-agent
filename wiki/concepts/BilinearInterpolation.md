---
title: "Bilinear Interpolation"
type: concept
tags: [computer-vision, signal-processing, upsampling]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Bilinear Interpolation

Classical method for resampling a 2D grid at non-integer coordinates by computing a weighted average of the four nearest integer grid cells, with weights given by linear interpolation in each dimension. The standard image-upsampling primitive.

## Algorithm

To sample at continuous coordinate $(x', y')$ given the four surrounding integer-grid values $f(\lfloor x' \rfloor, \lfloor y' \rfloor)$, $f(\lceil x' \rceil, \lfloor y' \rfloor)$, $f(\lfloor x' \rfloor, \lceil y' \rceil)$, $f(\lceil x' \rceil, \lceil y' \rceil)$:

1. Let $\alpha = x' - \lfloor x' \rfloor$, $\beta = y' - \lfloor y' \rfloor$.
2. Linearly interpolate along $x$ at $y = \lfloor y' \rfloor$ and at $y = \lceil y' \rceil$.
3. Linearly interpolate the two results along $y$.

Equivalent to: $f(x', y') = (1-\alpha)(1-\beta) f_{00} + \alpha(1-\beta) f_{10} + (1-\alpha)\beta f_{01} + \alpha\beta f_{11}$.

## In [[d2l-computer-vision]]

Two distinct roles:

1. **[[FCN]] upsampling initialization:** the final [[TransposedConvolution|transposed-conv]] layer is initialized with a hand-designed bilinear kernel (`bilinear_kernel(in_channels, out_channels, kernel_size)`), giving the network a sensible starting point that classical bilinear-upsamples class logits to the input resolution. Training refines from there.
2. **[[ROIAlign|RoI align]] (in [[MaskRCNN]]):** sample feature-map values at non-integer RoI coordinates without the rounding artifacts of [[ROIPooling|RoI pooling]] — preserves sub-pixel spatial alignment critical for instance-segmentation masks.

## Bicubic alternative

Bicubic interpolation uses 16 surrounding pixels (vs. bilinear's 4) and a cubic kernel — smoother but more expensive. Common in PIL / Photoshop "high quality" resampling. Bilinear is preferred in ML pipelines for speed and differentiability.

## Connections

- [[TransposedConvolution]] / [[FCN]] / [[ROIAlign]] / [[MaskRCNN]].
- [[SemanticSegmentation]] / [[InstanceSegmentation]] — applications.
- Cousin techniques: nearest-neighbor (faster, blockier), bicubic (smoother, slower), Lanczos.
