---
title: "Residual block"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Residual block

The canonical [[ResNet]] building block: two convolutional layers with [[BatchNormalization|BN]] + [[ReLU]], wrapped in a [[ResidualConnection|residual connection]]. The single most-replicated CNN sub-module of the 2015-and-after era ([[d2l-convolutional-modern]] §resnet).

## Structure (basic / "ResNet-18 / 34" variant)

```
Y = ReLU(BN(Conv3x3(X)))
Y = BN(Conv3x3(Y))
if shape_mismatch:
    X = Conv1x1(X)   # match channels/resolution
return ReLU(Y + X)
```

- Two $3\times3$ convolutions with same output-channel count.
- BN after each conv; ReLU after the first; ReLU after the *sum* (not before).
- Optional $1\times1$ conv on the shortcut path when channels or resolution change.

## Bottleneck variant (ResNet-50+)

```
Y = ReLU(BN(Conv1x1(X, c/4)))     # reduce channels by 4×
Y = ReLU(BN(Conv3x3(Y, c/4)))     # 3×3 at reduced width
Y = BN(Conv1x1(Y, c))             # restore channels
if shape_mismatch:
    X = Conv1x1(X)
return ReLU(Y + X)
```

Used in deeper ResNet variants for compute frugality. Generalized by [[ResNeXt]] with grouped convolutions in the middle $3\times3$.

## Pre-activation variant (He et al. 2016 v2)

```
Y = Conv3x3(ReLU(BN(X)))
Y = Conv3x3(ReLU(BN(Y)))
return Y + X    # no ReLU after the sum
```

Order: BN → ReLU → conv. Marginally better convergence in very deep networks; used in [[DenseNet]]'s conv blocks. The pattern propagates into modern [[transformer|Transformer]] pre-norm designs.

## D2L PyTorch implementation

```python
class Residual(nn.Module):
    def __init__(self, num_channels, use_1x1conv=False, strides=1):
        super().__init__()
        self.conv1 = nn.LazyConv2d(num_channels, kernel_size=3, padding=1, stride=strides)
        self.conv2 = nn.LazyConv2d(num_channels, kernel_size=3, padding=1)
        self.conv3 = nn.LazyConv2d(num_channels, kernel_size=1, stride=strides) if use_1x1conv else None
        self.bn1 = nn.LazyBatchNorm2d()
        self.bn2 = nn.LazyBatchNorm2d()

    def forward(self, X):
        Y = F.relu(self.bn1(self.conv1(X)))
        Y = self.bn2(self.conv2(Y))
        if self.conv3: X = self.conv3(X)
        return F.relu(Y + X)
```

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[ResNet]] — the architecture built from residual blocks.
- [[ResidualConnection]] — the primitive inside it.
- [[ResNeXt]] — generalizes the bottleneck variant with grouped convolutions.
- [[Bottleneck]] — the $1\times1\to3\times3\to1\times1$ pattern.
- [[BatchNormalization]] / [[ReLU]] / [[OneByOneConvolution]] / [[ConvolutionalLayer]] — building blocks.
- [[CNN]] — parent family.
- [[KaimingHe]] — author.
