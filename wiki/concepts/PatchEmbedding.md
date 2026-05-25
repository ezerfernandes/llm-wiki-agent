---
title: "Patch Embedding"
type: concept
tags: [transformer, computer-vision]
sources: [d2l-attention-and-transformers, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Patch Embedding

The "tokenizer" of a [[VisionTransformer|Vision Transformer]]: splits an image into a grid of non-overlapping square patches and linearly projects each patch to a $d$-dimensional embedding — so an image becomes a sequence the [[Transformer|Transformer]] encoder can ingest.

## Implementation

For an $h \times w \times c$ image with patch size $p$:
- Number of patches: $m = (h/p)(w/p)$.
- Each patch is flattened from $p \times p \times c$ to a vector of length $cp^2$.
- A learned linear projection maps to $d$ dimensions: output shape $(\textrm{batch}, m, d)$.

**Implementation trick:** the split + flatten + linear can be expressed as a single 2-D convolution with kernel size $p$ and stride $p$:

```python
self.conv = nn.LazyConv2d(num_hiddens, kernel_size=patch_size, stride=patch_size)
```

A stride-$p$ kernel-$p$ convolution is mathematically equivalent to "non-overlapping patches → linear projection." This is the implementation used in ViT and many of its descendants.

## Parameters

- Typical ViT-Base: $p = 16$, $d = 768$, on $224 \times 224$ images → 196 patches + 1 `<cls>` = 197 tokens.
- D2L Fashion-MNIST toy: $p = 16$, $d = 512$, on $96 \times 96$ → 36 patches.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 frames patch embedding as **the image-tokenizer** — the structural analog of text tokenization that lets the Transformer encoder operate on images at all:

> *"Just like we are converting text into tokens of text, we are converting an image into patches of images. The flattened input of image patches can be thought of as the tokens in a piece of text. However, unlike tokens, we cannot just assign each patch with an ID since these patches will rarely be found in other images, unlike the vocabulary of a text. Instead, the patches are linearly embedded to create numerical representations, namely embeddings."*

The chapter is explicit that the linear projection is what makes the image tokens behave like text tokens. After the projection, *"the embeddings are passed to the encoder, they are treated as if they were textual tokens. From that point forward, there is no difference in how a text or image trains."* This is the structural justification for using [[VisionTransformer|ViT]] as the image encoder inside [[CLIP]] / [[BLIP2|BLIP-2]] / [[LLaVA15|LLaVA]].

## See also

- [[VisionTransformer]] · [[ClsToken]] · [[Transformer]] · [[CNN]] · [[OneByOneConvolution]] · [[Tokenization]] · [[CLIP]] · [[BLIP2]] · [[ImageEncoder]]
