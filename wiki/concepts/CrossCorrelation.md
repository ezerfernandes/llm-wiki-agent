---
title: "Cross-Correlation"
type: concept
tags: [deep-learning, cnn, math, signal-processing]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Cross-Correlation

The operator that deep-learning frameworks *actually* compute and (misleadingly) call "convolution." For a 2D input $\mathbf X$ of shape $n_h\times n_w$ and a kernel $\mathbf K$ of shape $k_h\times k_w$, the cross-correlation output at $(i,j)$ is

$$[\mathbf Y]_{i,j}=\sum_{a=0}^{k_h-1}\sum_{b=0}^{k_w-1}[\mathbf X]_{i+a,\,j+b}\cdot[\mathbf K]_{a,b}.$$

That is: slide the kernel window from upper-left to lower-right, multiply elementwise, sum. The output shape is $(n_h-k_h+1)\times(n_w-k_w+1)$ — strictly smaller than the input unless padded.

## vs. true [[Convolution]]

The only mathematical difference is a kernel flip:

| Operator | Indexing |
|---|---|
| True convolution | $g(i-a,\,j-b)$ |
| Cross-correlation | $g(i+a,\,j+b)$ |

Cross-correlation can be implemented as true convolution by first flipping the kernel both horizontally and vertically. Because CNN kernels are *learned*, this distinction is operationally invisible — the network learns whichever orientation the framework's operator expects ([[d2l-convolutional-neural-networks]] §conv-layer: "Cross-Correlation and Convolution").

## The `corr2d` reference implementation

D2L's pedagogical implementation (Python pseudocode):

```python
def corr2d(X, K):
    h, w = K.shape
    Y = zeros((X.shape[0] - h + 1, X.shape[1] - w + 1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i, j] = (X[i:i+h, j:j+w] * K).sum()
    return Y
```

Worked example: $X=[[0,1,2],[3,4,5],[6,7,8]]$, $K=[[0,1],[2,3]]$ produces $Y=[[19,25],[37,43]]$ via $0\cdot0+1\cdot1+3\cdot2+4\cdot3=19$, etc.

## Why frameworks renamed it

The deep-learning community settled on "convolution" for the cross-correlation operator because (a) the kernel-flip is meaningless when the kernel is learned, and (b) "convolution" was the established term in signal processing for the *family* of these operations. The wiki, like D2L, uses "convolution" loosely for both; reserves "cross-correlation" when the distinction matters (e.g., when reading classical signal-processing texts).

## Connections

- [[Convolution]] — the true mathematical operator; differs only by kernel flip.
- [[ConvolutionalLayer]] — wraps `corr2d` with a learnable kernel + bias.
- [[CNN]] — the architecture that stacks these.
- [[d2l-convolutional-neural-networks]] — defines the `corr2d` reference.
- [[Padding]] / [[Stride]] — modulate the output shape of `corr2d`.
- [[Channels]] — multi-channel `corr2d_multi_in_out`.
