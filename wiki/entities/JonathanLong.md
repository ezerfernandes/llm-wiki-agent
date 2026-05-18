---
title: "Jonathan Long"
type: entity
tags: [person, researcher, computer-vision]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Jonathan Long

Computer-vision researcher; lead author of the [[FCN|Fully Convolutional Networks]] paper (Long, [[EvanShelhamer|Shelhamer]] & [[TrevorDarrell|Darrell]] 2015, `Long.Shelhamer.Darrell.2015`) — the canonical end-to-end model for [[SemanticSegmentation|semantic segmentation]]. At UC Berkeley with [[TrevorDarrell|Trevor Darrell]] at time of FCN. Per [[d2l-computer-vision]] §`fcn`.

## FCN's contribution

Per [[d2l-computer-vision]]: "A fully convolutional network (FCN) uses a convolutional neural network to transform image pixels to pixel classes." Concretely: take a classification CNN, drop its global-average-pool + FC head, add a $1\times1$ conv to map feature channels to class channels, and a [[TransposedConvolution|transposed-conv]] layer to upsample spatial dims back to the input resolution. Output is `(batch, K, H, W)` — one class logit per input pixel.

Why it mattered:
- **First end-to-end semantic segmentation** — no patch-based sliding window, no graphical-model post-processing.
- **Reuses pretrained [[ImageNet]] features** at a time when segmentation labels were scarce.
- **Arbitrary input size at inference** — fully convolutional → no fixed input shape.
- The template every successor follows: U-Net (Ronneberger 2015), DeepLab (Chen 2014–2018), SegFormer, Mask R-CNN's mask head.

## Connections

- [[FCN]] / [[SemanticSegmentation]] / [[TransposedConvolution]] / [[BilinearInterpolation]] / [[CNN]] / [[ResNet]] / [[ImageNet]] / [[ComputerVision]].
- Co-authors: [[EvanShelhamer]], [[TrevorDarrell]] (advisor).
- [[UniversityOfCaliforniaBerkeley|UC Berkeley]] — institutional affiliation.
