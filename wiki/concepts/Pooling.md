---
title: "Pooling"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-neural-networks, madewithml-baselines]
last_updated: 2026-05-16
---

# Pooling

A **pooling layer** slides a fixed-shape window over a feature map (with [[Stride|stride]] and optional [[Padding|padding]]) and returns a single deterministic statistic per window — typically the **maximum** ([[MaxPooling]]) or **average** ([[AveragePooling]]) of the window. Unlike [[ConvolutionalLayer|convolutional layers]], pooling has **no learnable parameters** — no kernel, no bias.

## Purpose

1. **Spatial downsampling.** A $2\times2$ pool with stride 2 quarters the spatial resolution.
2. **Translation invariance to small shifts.** If a feature shifts by one pixel inside a $2\times2$ window, max-pool's output is unchanged. Helps the network tolerate camera jitter, tripod vibration, etc. ([[d2l-convolutional-neural-networks]] §pooling motivation).
3. **Receptive-field expansion.** Each deeper layer's pooled output reflects a larger region of the original input — supports global semantics ("does this image contain a cat?") from local features.

## Max vs. average

| Operator | Computation | Notes |
|---|---|---|
| **[[MaxPooling]]** | $\max$ over window | Introduced by Riesenhuber & Poggio 1999 (cognitive neuroscience); preferred "in almost all cases" today |
| **[[AveragePooling]]** | mean over window | "As old as CNNs"; akin to downsampling with low-pass smoothing; used in LeNet and as global-average-pooling at network end |

[[d2l-convolutional-neural-networks]] §pooling summary: "of the two popular pooling choices, max-pooling is preferable to average pooling, as it confers some degree of invariance to output."

## Key arithmetic property

Pooling is **applied per channel** — unlike convolution, which sums over input channels. So pooling leaves the number of channels unchanged: input $c\times h\times w$ → output $c\times h'\times w'$.

## Defaults

Most frameworks default **stride = window size** for pooling (non-overlapping windows). Override to get overlapping pooling.

## Variants beyond max/avg

- **Global average pooling** — window = entire feature map; replaces FC layers in fully-convolutional architectures.
- **Stochastic pooling** (Zeiler & Fergus 2013) — sample from window proportional to activation magnitude.
- **Fractional max-pooling** (Graham 2014) — non-integer downsampling factor.
- **Softmax / soft-attention pooling** — the route the field eventually took for [[Transformer|transformers]]: aggregate by attention weights rather than fixed max/avg.

## In code

```python
# PyTorch
pool = nn.MaxPool2d(kernel_size=2, stride=2)  # default stride = window size
pool = nn.AvgPool2d(kernel_size=2, stride=2)

# Keras / TF
pool = tf.keras.layers.MaxPool2D(pool_size=2)
pool = tf.keras.layers.AveragePooling2D(pool_size=2)

# Flax / JAX
nn.max_pool(x, window_shape=(2,2), strides=(2,2))
nn.avg_pool(x, window_shape=(2,2), strides=(2,2))
```

## Exercises worth knowing

- Max-pooling **cannot** be implemented as a single convolution (D2L §pooling exercise).
- Max-pooling **can** be implemented via convolutions + ReLU, since $\max(a,b)=\text{ReLU}(a-b)+b$.
- Average pooling **can** be implemented as a convolution with a uniform kernel.

## Connections

- [[MaxPooling]] / [[AveragePooling]] — the two dominant variants.
- [[ConvolutionalLayer]] — the layer pooling is typically interleaved with.
- [[Stride]] / [[Padding]] — pooling's shape knobs.
- [[CNN]] / [[LeNet]] — LeNet pools after each conv block.
- [[ReceptiveField]] — pooling enlarges it.
- [[TranslationInvariance]] — what pooling provides locally.
- [[d2l-convolutional-neural-networks]] — canonical reference.
- [[Attention]] — modern attention can be viewed as "learned soft pooling."
