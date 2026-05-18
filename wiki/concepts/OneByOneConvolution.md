---
title: "1×1 Convolution"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# 1×1 Convolution

A **$1\times1$ convolution** is a [[ConvolutionalLayer|convolutional layer]] with $k_h=k_w=1$. It has zero spatial extent — each output pixel depends only on the *same* pixel's channel values in the input. The only computation is a linear combination over the channel axis at each spatial location, using $c_o\cdot c_i$ weights (plus $c_o$ bias).

## What it really is

A per-pixel fully-connected layer. Equivalent to: "for each pixel position $(i,j)$, take the length-$c_i$ channel vector $\mathsf X_{i,j,:}$ and multiply by a $c_o\times c_i$ matrix $\mathsf W$ to produce the length-$c_o$ output vector $\mathsf H_{i,j,:}$." Because the same $\mathsf W$ is reused at every pixel, it's still a *convolution* — just one with no spatial mixing.

D2L's reference implementation collapses to a matrix-multiply:

```python
def corr2d_multi_in_out_1x1(X, K):
    c_i, h, w = X.shape
    c_o = K.shape[0]
    X = X.reshape(c_i, h * w)
    K = K.reshape(c_o, c_i)
    Y = K @ X
    return Y.reshape(c_o, h, w)
```

## Why use it

1. **Channel mixing without spatial mixing.** Cheap (no $k^2$ blow-up); the canonical way to change the number of channels.
2. **Bottleneck.** Sandwich expensive $3\times3$ convs between $1\times1$ convs that reduce + restore channels — the [[ResNet]] / [[Inception]] bottleneck pattern. Order-of-magnitude FLOP savings.
3. **Per-pixel nonlinearity.** Followed by ReLU, it adds expressive capacity without growing the receptive field — useful when stacking many "wide-and-thin" layers.
4. **Network-in-Network.** Lin, Chen, Yan (2013) introduced 1×1 convs as the explicit "tiny MLP per pixel" interpretation — implementing an MLP independently for each spatial location.

D2L: "the $1\times 1$ convolutional layer [is] a fully connected layer applied at every single pixel location to transform the $c_i$ corresponding input values into $c_o$ output values. Because this is still a convolutional layer, the weights are tied across pixel location."

## Cannot be folded into adjacent convs

[[ConvolutionalLayer|Convolutional layers]] are typically followed by nonlinearities (ReLU). A *linear* composition of a $1\times1$ conv and a $3\times3$ conv could in principle be merged into a single $3\times3$ conv, but the intervening nonlinearity prevents this. So $1\times1$ convs add genuine representational capacity, not just bookkeeping.

## Cost

$\mathcal O(h\cdot w\cdot c_i\cdot c_o)$ — no $k^2$ factor. For large images and channel counts, still dominant (most modern CNN FLOPs are $1\times1$ convs!).

## Connections

- [[ConvolutionalLayer]] / [[Convolution]] — the operator family.
- [[Channels]] — what $1\times1$ convs operate on exclusively.
- [[CNN]] — context.
- [[ResNet]] / [[Inception]] / [[NetworkInNetwork]] — architectures built around $1\times1$ convs.
- [[d2l-convolutional-neural-networks]] — canonical introduction.
- [[Bottleneck]] — the dominant use pattern.
