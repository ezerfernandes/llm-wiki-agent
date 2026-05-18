---
title: "Convolutional Layer"
type: concept
tags: [deep-learning, cnn, layer]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Convolutional Layer

A **convolutional layer** is the parameterized neural-network layer that wraps a [[CrossCorrelation|cross-correlation]] operator with a learnable kernel and a scalar (or per-output-channel) bias:

$$\mathbf Y = \text{corr2d}(\mathbf X, \mathbf W) + b.$$

The two learnable parameters per layer are the [[Filter|kernel]] $\mathbf W$ (shape $c_o\times c_i\times k_h\times k_w$ for multi-channel I/O) and the bias $b$. Kernels are initialized randomly (e.g., [[XavierInitialization|Xavier]]) and learned by [[Backpropagation]] just like an [[MultilayerPerceptron|MLP]] weight matrix.

## Forward pass (multi-channel)

For each output channel $d\in\{1,\dots,c_o\}$:

$$[\mathsf H]_{i,j,d}=b_d+\sum_{a=-\Delta}^{\Delta}\sum_{b=-\Delta}^{\Delta}\sum_{c=1}^{c_i}[\mathsf V]_{a,b,c,d}\,[\mathsf X]_{i+a,\,j+b,\,c}.$$

The $c_i$ input channels are summed (one cross-correlation per input channel, results added); the $c_o$ output channels are stacked into a 3-tensor.

## Output shape

For input $n_h\times n_w$, kernel $k_h\times k_w$, total padding $p_h\times p_w$, stride $s_h\times s_w$:

$$\left\lfloor\frac{n_h - k_h + p_h + s_h}{s_h}\right\rfloor \times \left\lfloor\frac{n_w - k_w + p_w + s_w}{s_w}\right\rfloor.$$

Setting $p=k-1$ preserves spatial dims (when $s=1$). See [[Padding]], [[Stride]].

## Parameter count

A conv layer has $c_o\cdot c_i\cdot k_h\cdot k_w + c_o$ parameters — *no dependence on spatial size $h\times w$*. This is the dramatic reduction over an FC layer that motivates CNNs ([[CNN]] derivation).

## Compute cost

$\mathcal O(h\cdot w\cdot k^2\cdot c_i\cdot c_o)$ multiplications per forward pass. A $256\times256$ image with $5\times5$ kernel and 128↔128 channels = >53 billion ops; motivates [[DepthwiseConvolution]] / [[ResNeXt|grouped convolutions]].

## Variants

- **[[OneByOneConvolution|$1\times1$ conv]]** — channel-mixing only, no spatial extent; cost $c_o\cdot c_i$ per pixel.
- **Strided conv** — $s>1$, used for downsampling instead of (or in addition to) pooling.
- **Padded conv** — $p>0$, used to preserve spatial size or avoid boundary loss.
- **[[DepthwiseConvolution|Depthwise / grouped]]** — kernel constrained to be block-diagonal in $c_i$; reduces cost by factor $g$.
- **Transposed / "deconvolution"** — fractional stride for upsampling (e.g., decoders).

## In code

```python
# PyTorch
conv = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=5, padding=2, stride=1)

# MXNet
conv = nn.Conv2D(channels=16, kernel_size=5, padding=2)

# Keras / TensorFlow
conv = tf.keras.layers.Conv2D(filters=16, kernel_size=5, padding='same')

# Flax / JAX
conv = nn.Conv(features=16, kernel_size=(5, 5), padding='SAME')
```

All four frameworks compute the same [[CrossCorrelation|cross-correlation]] under the "convolution" label.

## Connections

- [[Convolution]] / [[CrossCorrelation]] — the operator underneath.
- [[Filter]] / [[ConvolutionKernel]] — the learnable weights.
- [[CNN]] — the architecture that stacks these.
- [[Padding]] / [[Stride]] / [[Channels]] / [[OneByOneConvolution]] — operational siblings.
- [[Pooling]] — the parameter-free aggregator typically interleaved with conv layers.
- [[d2l-convolutional-neural-networks]] — pedagogical derivation.
- [[LeNet]] — first deployed instance.
- [[Backpropagation]] / [[XavierInitialization]] — training stack.
