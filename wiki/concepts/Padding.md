---
title: "Padding"
type: concept
tags: [deep-learning, cnn, preprocessing, nlp]
sources: [d2l-convolutional-neural-networks, madewithml-preprocessing]
last_updated: 2026-05-16
---

# Padding

**Padding** adds extra elements (typically zeros) around the boundary of an input so a [[Convolution|convolution]] or other windowed operator can be applied without losing the boundary. In NLP, padding refers to appending filler tokens so variable-length sequences share a uniform shape for batching.

## In CNNs ([[d2l-convolutional-neural-networks]] §padding-and-strides)

Without padding, each $k_h\times k_w$ convolution shrinks the spatial dims by $(k_h-1, k_w-1)$. Ten stacked $5\times5$ convs on a $240\times240$ image cut the output to $200\times200$ — losing 30% of the image and obliterating boundary information. Pixels at the corners are also used much less than central ones (asymmetric utilization), which biases the network.

**Fix:** pad the input with $p_h$ total rows and $p_w$ total columns of zeros (roughly half on each side). Output shape with padding becomes

$$(n_h-k_h+p_h+1)\times(n_w-k_w+p_w+1).$$

**Same-padding convention:** setting $p_h=k_h-1$ and $p_w=k_w-1$ (with stride 1) keeps output dims equal to input dims. This is why CNNs prefer **odd kernel sizes** (1, 3, 5, 7) — you can pad symmetrically with $(k-1)/2$ on each side.

## Why zero-padding is the default

- **Computationally trivial** — no extra memory allocation needed; operators can encode the zero pattern implicitly.
- **Position information** — CNNs implicitly learn position via "where the whitespace is." Alsallakh et al. 2020 surveyed alternatives (reflective, mirror, replicate) without a clear case for replacing zero-padding in general.

## Padding modes

- **Zero / constant** (the default).
- **Reflect / mirror** — useful when zero-padding creates artifacts (e.g., spectrograms, super-resolution).
- **Replicate / edge** — repeats border pixels.
- **Circular / wrap** — for periodic data.

## In code

```python
# PyTorch: int p means p on each side (total 2p); also 'same'/'valid' in newer versions
conv = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, padding=1)  # SAME for k=3

# Keras: 'same' (auto) or 'valid' (no padding)
conv = tf.keras.layers.Conv2D(1, kernel_size=3, padding='same')

# Flax: 'SAME' or 'VALID' or explicit ((top, bot), (left, right))
conv = nn.Conv(1, kernel_size=(3, 3), padding='SAME')
```

## In NLP / sequence models

[[madewithml-preprocessing]] introduces padding for variable-length token sequences: pad with a `[PAD]` token to the batch's max length, mask the padding positions in [[Attention]] / loss. See [[AttentionMask]] for the transformer-specific story; the CNN padding here is *not* token-padding, just spatial zero-fill.

## Connections

- [[Convolution]] / [[CrossCorrelation]] / [[ConvolutionalLayer]] — the operator padding wraps.
- [[Stride]] — the *other* output-shape knob; co-applied.
- [[Pooling]] — also takes a padding argument.
- [[CNN]] / [[LeNet]] — architectures depending on padding choices (LeNet's first conv uses pad=2 to compensate for $5\times5$ kernel).
- [[d2l-convolutional-neural-networks]] — derivation + framework knobs.
- [[AttentionMask]] — analogous mechanism for transformer sequence-padding.
