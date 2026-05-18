---
title: "FCN (Fully Convolutional Network)"
type: concept
tags: [computer-vision, semantic-segmentation, model]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# FCN (Fully Convolutional Network)

The canonical end-to-end model for [[SemanticSegmentation|semantic segmentation]]. [[JonathanLong|Long]], [[EvanShelhamer|Shelhamer]] & [[TrevorDarrell|Darrell]] 2015 (`Long.Shelhamer.Darrell.2015`). Per [[d2l-computer-vision]] §`fcn`: "A fully convolutional network (FCN) uses a convolutional neural network to transform image pixels to pixel classes."

## Core idea

Replace a classification CNN's fully-connected head with [[ConvolutionalLayer|convolutional]] + [[TransposedConvolution|transposed-convolution]] layers, so the output shape can be made to match the input image shape — yielding **one class prediction per input pixel**.

## Architecture (D2L's worked example)

Starting from [[ResNet|ResNet-18]] pretrained on [[ImageNet]] (input $3\times320\times480$):

1. **Backbone:** keep all of ResNet-18 *except* the final global-average-pool + FC layer. Output shape: $512\times10\times15$ (32× spatial reduction).
2. **$1\times1$ conv channel reduction:** map 512 channels → 21 classes (Pascal VOC).
3. **Transposed-conv upsampler:** kernel 64, padding 16, stride 32 → upsamples spatial dims by exactly 32×. Output: $21\times320\times480$ — one class logit per input pixel.

## Bilinear-interpolation initialization

The transposed-conv layer is *initialized* with a hand-designed [[BilinearInterpolation|bilinear-interpolation]] kernel (D2L's `bilinear_kernel` function), so the network's initial output is the (bilinearly-upsampled) class logits from the $1\times1$ conv. Training refines this from a sensible starting point. Without this trick, random initialization of a 32× upsampling layer requires enormous gradient flow to recover any spatial structure.

## Loss

Per-pixel softmax cross-entropy, averaged over the spatial dimensions. Pixels labeled "ignore" (e.g. white borders in Pascal VOC) are masked out.

## Why FCN is canonical

- **First end-to-end** semantic segmentation: no per-region classification, no patch-based sliding window, no graphical-model post-processing.
- **Reuses pretrained ImageNet features** — semantic segmentation labels are scarce; ImageNet labels are abundant.
- **Fully convolutional → arbitrary input size** at inference: the same network handles $300\times400$ and $1000\times2000$ images.
- Established the template that every successor (U-Net, DeepLab, SegFormer, Mask R-CNN's mask head) follows.

## Successors

- **U-Net** (Ronneberger et al. 2015) — encoder-decoder with skip connections at every resolution; standard in medical imaging.
- **DeepLab series** (Chen et al. 2014–2018) — atrous (dilated) convolutions + atrous spatial pyramid pooling for dense prediction without spatial reduction.
- **FCN-8s / FCN-16s** — the original paper's multi-stride variants that fuse predictions across multiple downsampled scales.

## Connections

- [[SemanticSegmentation]] / [[TransposedConvolution]] / [[BilinearInterpolation]] / [[CNN]] / [[ResNet]] / [[ImageNet]] / [[FineTuning]] / [[PascalVOC2012]].
- [[MaskRCNN]] uses an FCN-style head for per-RoI mask prediction.
- [[JonathanLong]] / [[EvanShelhamer]] / [[TrevorDarrell]] — authors.
