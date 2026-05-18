---
title: "Kaiming He"
type: entity
tags: [person, researcher, cnn, deep-learning]
sources: [d2l-convolutional-modern, d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Kaiming He

Chinese computer-vision researcher; first author of **ResNet** ([[KaimingHe|He]], [[XiangyuZhang|Zhang]], [[ShaoqingRen|Ren]] & [[JianSun|Sun]] 2015) at Microsoft Research Asia — the residual-network paper that won ILSVRC 2015 and remains "one of the most popular off-the-shelf architectures in computer vision" ([[d2l-convolutional-modern]] §resnet). Also first author of **He initialization** (He et al. 2015), Mask R-CNN (He et al. 2017), and Momentum Contrast / MoCo (He et al. 2020). Currently at [[fair|FAIR]] / [[meta|Meta]], then MIT.

## Why he matters here

- **ResNet (2015).** The residual-connection idea — $f(\mathbf{x})=\mathbf{x}+g(\mathbf{x})$ — that solved the **degradation problem** (deeper networks training to *worse* training error than shallower ones) and made networks with 152 layers routinely trainable. Residual connections subsequently propagated into Transformers, RNNs, and graph neural networks. ILSVRC 2015 winner ([[d2l-convolutional-modern]] §resnet).
- **He initialization.** [[HeInitialization|He init]] (He et al. 2015) — the ReLU-aware variance-scaling initializer that complements [[BatchNormalization|BatchNorm]] in modern CNN training ([[d2l-multilayer-perceptrons]] §init).
- **Bottleneck residual variants.** Deeper ResNet variants (50/101/152) use bottleneck residual blocks ($1\times1\to3\times3\to1\times1$) that ResNeXt later generalizes ([[d2l-convolutional-modern]] §resnext).
- **Mask R-CNN, MoCo.** Subsequent first-author works on instance segmentation (Mask R-CNN 2017) and self-supervised contrastive learning (MoCo 2019/2020). (Not directly in this chapter but defining for the post-ResNet era.)

## Affiliations

- Microsoft Research Asia (MSRA) — 2011–2016; ResNet was here.
- [[fair|FAIR]] (Facebook AI Research / Meta) — 2016–2024.
- MIT — current professor.

## Connections

- [[d2l-convolutional-modern]] — canonical reference for ResNet / ResNeXt.
- [[ResNet]] — first author.
- [[ResidualConnection]] / [[ResidualBlock]] — the primitive ResNet introduced.
- [[HeInitialization]] — ReLU-tuned initializer.
- [[microsoftresearch]] / [[fair]] / [[meta]] — institutional homes.
- [[CNN]] / [[ImageNet]] — context.
