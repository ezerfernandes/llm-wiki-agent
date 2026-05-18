---
title: "Transposed Convolution"
type: concept
tags: [computer-vision, layer, upsampling]
sources: [d2l-computer-vision, d2l-generative-adversarial-networks]
last_updated: 2026-05-16
---

# Transposed Convolution

Convolutional layer that **upsamples** spatial dimensions — the dual of standard (downsampling) convolution. Also called *fractionally-strided convolution* (Dumoulin & Visin 2016). Per [[d2l-computer-vision]] §`transposed-conv`: "In contrast to the regular convolution that *reduces* input elements via the kernel, the transposed convolution *broadcasts* input elements via the kernel, thereby producing an output that is larger than the input."

## Basic operation

Given an $n_h \times n_w$ input tensor $X$ and a $k_h \times k_w$ kernel $K$:

1. For each position $(i, j)$ of $X$, multiply $K$ by the scalar $X_{i,j}$ to get a $k_h \times k_w$ "stamp".
2. Add this stamp to the output at position $(i:i+k_h, j:j+k_w)$.
3. Sum all stamps. Output shape: $(n_h + k_h - 1) \times (n_w + k_w - 1)$.

```python
# d2l implementation
def trans_conv(X, K):
    h, w = K.shape
    Y = zeros((X.shape[0] + h - 1, X.shape[1] + w - 1))
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Y[i:i+h, j:j+w] += X[i, j] * K
    return Y
```

## Padding and stride conventions (different from regular conv)

- **Padding** is applied to the **output**, not the input. Padding=1 → the first/last row and column of the would-be output are *trimmed*.
- **Stride** is specified for **intermediate results**, not for sampling the input. Stride=2 → each input element's stamp is placed 2 pixels apart in the output, doubling spatial dimensions.

## The "size up by $s\times$" recipe (used in [[FCN]])

For stride $s$, padding $s/2$ (integer), and kernel size $2s$, the transposed convolution increases spatial dimensions by **exactly $s\times$**. FCN's final upsampling layer uses $s=32$, padding 16, kernel 64.

## Why the name "transposed"

If a regular conv is matrix multiplication $\mathbf{y} = \mathbf{W}\mathbf{x}$ where $\mathbf{W}$ is a (sparse, structured) matrix expressing the kernel + sliding window, then transposed convolution computes $\mathbf{x}' = \mathbf{W}^\top \mathbf{y}'$. The output shape and forward computation are exactly what you'd expect from transposing the input/output relationship. **It is *not* an inverse** — applying transposed conv after regular conv does not recover the original input.

## Initialization with [[BilinearInterpolation|bilinear interpolation]]

A transposed-conv layer with a hand-designed bilinear-interpolation kernel performs exactly classical bilinear-upsample. FCN initializes its upsampling layer this way and learns refinements on top — much faster convergence than random init for shape-preserving tasks.

## Applications

- **[[FCN]]** — final layer upsamples backbone features back to input resolution for pixel-level prediction.
- **U-Net** — decoder path of the encoder-decoder.
- **GAN generators** ([[DCGAN]], StyleGAN) — successive transposed convs upsample noise → image; canonical reference in [[d2l-generative-adversarial-networks]] §`dcgan`.
- **Diffusion-model U-Nets** — same upsampling role in the denoiser.
- **Autoencoders** — decoder.

## Connections

- [[ConvolutionalLayer]] / [[CrossCorrelation]] / [[BilinearInterpolation]] / [[FCN]] / [[SemanticSegmentation]] / [[Autoencoder]].
- Common alternative: bilinear / nearest-neighbor upsampling followed by a regular conv ("upsample + conv" pattern; sometimes preferred to avoid checkerboard artifacts in generated images — Odena, Dumoulin & Olah 2016).
