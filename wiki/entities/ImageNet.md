---
title: "ImageNet"
type: entity
tags: [dataset, computer-vision, benchmark]
sources: [d2l-introduction]
last_updated: 2026-05-16
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
