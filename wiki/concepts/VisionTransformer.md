---
title: "Vision Transformer (ViT)"
type: concept
tags: [transformer, computer-vision, architecture]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Vision Transformer (ViT)

The application of the [[Transformer|Transformer]] encoder to image classification, introduced by **Dosovitskiy et al. 2021** ("An Image Is Worth 16x16 Words"). ViT discarded the [[CNN|convolutional]] inductive biases of [[Locality|locality]] and [[TranslationInvariance|translation invariance]] in favor of pure self-attention over image patches — and demonstrated that with sufficient pretraining data (300M+ images), pure-attention models outperform ResNets on ImageNet by a large margin. The empirical thesis: **scalability trumps inductive biases.**

## Architecture

For an $h \times w \times c$ input image with patch size $p$:

1. **[[PatchEmbedding|Patch embedding]].** Split into $m = hw/p^2$ patches; flatten each to a $cp^2$-dim vector; linearly project to dimension $d$ — implementable as a stride-$p$, kernel-$p$ 2-D convolution.
2. **`<cls>` token.** Prepend a learnable [[ClsToken|`<cls>` token]] embedding; total sequence length $m+1$.
3. **Positional embeddings.** Add *learned* 1-D positional embeddings to the $m+1$ token embeddings (no sinusoidal scheme).
4. **Transformer encoder stack.** Stack of [[VisionTransformerBlock|ViT blocks]] using [[PreNorm|pre-normalization]] (LayerNorm *before* MHA/MLP) + [[MultiHeadAttention]] + [[GELU]] MLP + dropout + [[ResidualConnection|residual connections]].
5. **Classification head.** The output `<cls>` representation passes through a final LayerNorm + linear layer to logits.

## Differences from the Vanilla Transformer

- **Pre-norm vs post-norm.** ViT applies LayerNorm before each sublayer; the [[1706.03762-attention-is-all-you-need|original Transformer]] applies it after the residual addition. Pre-norm "leads to more effective or efficient training" ([[baevski2018adaptive|Baevski & Auli 2018]]; [[xiong2020layer|Xiong et al. 2020]]) and is now dominant in modern Transformers.
- **GELU instead of ReLU.** "A smoother version of the ReLU" ([[Hendrycks.Gimpel.2016|Hendrycks & Gimpel 2016]]).
- **Learned positional embeddings**, not sinusoidal.
- **Encoder-only** — there is no decoder.

## Limits

- **Small-data regime.** On Fashion-MNIST or ImageNet (1.2M images), ViT does *not* beat ResNet — it lacks convolution's data-efficiency priors. The crossover happens at very large pretraining datasets.
- **Quadratic compute.** $O(n^2 d)$ in number of patches makes high-resolution images expensive (motivates [[SwinTransformer|Swin Transformers]]).
- **Data-efficient training.** DeiT ([[touvron2021training|Touvron et al. 2021]]) recovers competitive ImageNet performance without 300M-image pretraining via distillation + augmentation.

## Downstream

ViT is the visual backbone of [[CLIP]], [[DALLE2|DALL-E 2]], multimodal LLMs, and modern image-generation systems. [[SwinTransformer|Swin Transformers]] address the quadratic complexity for general-purpose computer vision.

## See also

- [[Transformer]] · [[SelfAttention]] · [[MultiHeadAttention]] · [[PatchEmbedding]] · [[ClsToken]] · [[PreNorm]] · [[GELU]] · [[CNN]] · [[ResNet]] · [[Dosovitskiy]]
