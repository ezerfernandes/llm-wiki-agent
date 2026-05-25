---
title: "ImageNet"
type: entity
tags: [dataset, computer-vision, benchmark]
sources: [d2l-introduction, ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# ImageNet

The large-scale image-classification dataset and benchmark that anchored the deep-learning revival in [[ComputerVision|computer vision]]. ~1.4M labeled images across ~1000 categories; the **ImageNet Large Scale Visual Recognition Challenge (ILSVRC)** is the canonical evaluation venue.

## Why it matters per D2L

[[d2l-introduction]] uses ImageNet as the cleanest metric of the post-2010 deep-learning surge:

| Year | Source | Top-5 error |
|---|---|---|
| 2010 | NEC Labs + UIUC (Lin et al.) | 28% |
| 2017 | Hu, Shen & Sun | **2.25%** |

A >10× error reduction in seven years — the chapter likens the broader 2010s deep-learning progress to a "Cambrian explosion" of statistical-model evolution. ImageNet is the dataset where that revolution was most legible to the rest of the research community.

ImageNet is also a recurring training-time benchmark — [[d2l-introduction]] cites distributed-SGD work that pushed **ResNet-50 / ImageNet training time** from days to **< 7 minutes** on 1,024 GPUs (Li 2017, You-Gitman-Ginsburg 2017, Jia-Song-He et al. 2018) using 64,000-image aggregate minibatches.

## Connections

- [[ComputerVision]] — the field ImageNet drives.
- [[CNN]] — the model class that broke through on ImageNet (AlexNet 2012; ResNet, etc.).
- [[d2l-introduction]] — corpus anchor for the 28%→2.25% chronicle.
- [[DistributedTraining]] — large-batch ImageNet training as the canonical demo.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] in *AI Engineering* Ch 1 uses ImageNet as the **canonical illustration of the data-labeling-cost bottleneck** that motivated [[SelfSupervision|self-supervised learning]]:

- 1M images × 1,000 categories = the original ImageNet labeling target.
- 5¢ per image × 1M images = **$50,000** for one labeling pass.
- $50M to scale labels to 1M categories (real-world coverage).
- Specialized labeling (e.g., CT-scan cancer annotation) is *"astronomical."*

Ch 1's contrast: [[CLIP]] (2021) bypassed this entire cost curve via **[[NaturalLanguageSupervision|natural language supervision]]** — 400M (image, text) pairs from the internet, *400× larger than ImageNet, with zero labeling cost.* CLIP enabled the first zero-shot generalization across image classification tasks.

ImageNet is thus the **structural anchor** that lets Huyen explain *why* foundation models exist: they exist because the ImageNet labeling-cost regime would never have scaled to multimodal frontier capability.
