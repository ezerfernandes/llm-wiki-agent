---
title: "Computer Vision"
type: concept
tags: [application-domain]
sources: [d2l-preface, d2l-introduction, d2l-computer-vision]
last_updated: 2026-05-16
---

# Computer Vision

Application domain dealing with computational understanding of images and video. Per [[d2l-preface]], one of the fields most transformed by [[DeepLearning]]; [[CNN|convolutional neural networks]] "form the backbone of most modern computer vision systems."

## Pre-DL → DL transition (per [[d2l-introduction]])

Pre-deep-learning, CV was dominated by handcrafted feature extractors that "reigned supreme for over a decade":

- **Canny edge detector** (Canny 1987)
- **[[SIFT|Lowe's SIFT]]** (Lowe 2004)

These fed shallow classifiers. [[EndToEndTraining|End-to-end training]] of deep nets replaced both with automatically tuned filters; the [[ImageNet]] top-5 error plummeted from 28% (2010) to 2.25% (2017). [[d2l-introduction]] cites this as the cleanest legible illustration of the deep-learning revival.

## Modern frontiers ([[d2l-introduction]] preview)

- Object recognition / detection / segmentation.
- Image generation: [[generativeadversarialnetwork|GANs]] → [[DiffusionModel|diffusion models]] (DALL-E 2, Imagen).
- Self-driving perception ([[Tesla]] / NVIDIA / Waymo).
- Medical imaging (skin-cancer diagnosis cited as a near-human result).

## The four canonical task families (per [[d2l-computer-vision]])

1. **Image classification** — one label per image. [[CNN]] / [[ResNet]] / [[VGG]] / [[VisionTransformer|ViT]]. Pedagogical baseline.
2. **[[ObjectDetection|Object detection]]** — multiple `(class, bbox)` pairs per image. Two families: single-stage ([[SSD]] / YOLO / RetinaNet) and two-stage ([[RCNN]] → [[FastRCNN]] → [[FasterRCNN]] → [[MaskRCNN]]).
3. **Segmentation** — pixel-level labels.
   - [[SemanticSegmentation]] (per-pixel class, no instances) → canonical model [[FCN]] on [[PascalVOC2012]].
   - [[InstanceSegmentation]] (per-pixel class + instance ID) → canonical model [[MaskRCNN]].
   - Panoptic segmentation (semantic + instance unified).
4. **Generation / synthesis** — [[StyleTransfer|neural style transfer]] (Gatys et al. 2016), GANs, diffusion. Style transfer leverages a frozen pretrained CNN's hierarchical features as a content + style feature extractor; the *image itself* is the trainable variable.

## Universal toolkit (per [[d2l-computer-vision]])

Every modern CV pipeline combines:

- **Backbone CNN** ([[ResNet]] / [[VGG]] / [[ConvNeXt]] / [[VisionTransformer|ViT]]) pretrained on [[ImageNet]].
- **[[FineTuning]]** to adapt the backbone to the target task with a small LR on the backbone vs. larger LR on the new head.
- **[[DataAugmentation]]** (flip / crop / color-jitter / mixup / cutout) as cheap regularization.
- **[[TransposedConvolution]] + [[BilinearInterpolation]]** for any task requiring per-pixel output (segmentation, generation, super-resolution).
- **[[AnchorBox|Anchor boxes]] + [[IntersectionOverUnion|IoU]] + [[NonMaxSuppression|NMS]]** for detection (modulo anchor-free / DETR-style detectors).
- **[[ROIPooling|RoI pooling]] / [[ROIAlign|RoI align]]** for per-region feature extraction in two-stage detectors.

## Connections to the rest of the wiki

- [[CNN]] / [[AlexNet]] / [[VGG]] / [[ResNet]] / [[GoogLeNet]] / [[DenseNet]] / [[VisionTransformer]] — backbone networks.
- [[ImageNet]] / [[FashionMNIST]] / [[CIFAR10]] / [[MNIST]] / [[PascalVOC2012]] — datasets.
- [[d2l-convolutional-neural-networks]] / [[d2l-convolutional-modern]] / [[d2l-computer-vision]] — D2L's CV pedagogy.
- [[d2l-attention-and-transformers]] — Vision Transformer transition: "scalability trumps inductive biases".
- [[2205.14135-flashattention]] / [[gpumemoryhierarchy]] — modern attention is the substrate of ViT.
- [[Tesla]] — applied CV in autonomous driving.

## Authors and lineage

The CV lineage in [[d2l-computer-vision]] features [[RossGirshick]] (R-CNN family), [[WeiLiu]] (SSD), [[KaimingHe]] (Mask R-CNN, ResNet), [[JonathanLong]] / [[EvanShelhamer]] / [[TrevorDarrell]] (FCN), and [[LeonGatys]] / [[AlexanderEcker]] / [[MatthiasBethge]] (style transfer). Their work spans 2014–2017, the formative window between the [[AlexNet]] revival and the [[VisionTransformer|ViT]] transition.
