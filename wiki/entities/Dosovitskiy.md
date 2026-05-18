---
title: "Alexey Dosovitskiy"
type: entity
tags: [person, researcher, computer-vision, transformers]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Alexey Dosovitskiy

First author of the **Vision Transformer** paper — *An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale* (Dosovitskiy, Beyer, Kolesnikov et al. 2021) — that introduced [[VisionTransformer|ViT]] and demonstrated that with sufficient pretraining data (300M+ images, JFT-300M / ImageNet-21k), a pure-attention model outperforms ResNets on image classification.

## Why he matters here

- **[[VisionTransformer|ViT]] (2021).** Established the *patches-as-tokens* recipe (linear projection of $p\times p$ image patches → learnable [[ClsToken|`<cls>` token]] → standard Transformer encoder → classification head) as the default vision backbone for foundation models. The empirical thesis: **scalability trumps inductive biases.**
- **Architectural template downstream.** ViT's design propagated into [[CLIP]] (image encoder), [[DALLE2|DALL-E 2]] / [[Imagen]] / [[Parti]] (text-to-image), Swin Transformers, DeiT, MAE — and modern multimodal LLMs.

Previously at [[google|Google]] / Google Research; lead figure in pre-ViT generative modeling work (e.g. FlowNet for optical flow).

## Connections

- [[VisionTransformer]] — the architecture introduced.
- [[Transformer]] · [[SelfAttention]] · [[PatchEmbedding]] · [[ClsToken]] — the building blocks.
- [[d2l-attention-and-transformers]] — D2L's ViT chapter cites Dosovitskiy et al. 2021 directly.
- [[CNN]] · [[ResNet]] — the architectures ViT displaced for sufficiently-large-data settings.
