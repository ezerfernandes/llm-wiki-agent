---
title: "Average Pooling"
type: concept
tags: [deep-learning, cnn]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Average Pooling

A [[Pooling|pooling]] operator that returns the **arithmetic mean** of each pooling window:

$$[\mathbf Y]_{i,j} = \frac{1}{|W|}\sum_{(a,b)\in W}\,[\mathbf X]_{i+a,\,j+b}.$$

"Essentially as old as CNNs" ([[d2l-convolutional-neural-networks]] §pooling). The historical pooling choice in [[LeNet|LeNet-5]] (1989/1998) and most pre-2010 CNNs; superseded by [[MaxPooling|max-pooling]] in modern architectures.

## Where it still appears

- **LeNet and pedagogical CNNs** — D2L's LeNet implementation uses `AvgPool2d(2, stride=2)` to faithfully reproduce the original architecture.
- **Global Average Pooling (GAP)** — a single average over the *entire* feature map, replacing the flatten + FC head in fully-convolutional networks (NIN, GoogLeNet, ResNet). One scalar per channel; cheap and translation-invariant by construction.
- **Smoothing / signal preservation** — averaging combines information from multiple adjacent pixels (better SNR) where max would discard it.

## Why it lost to max-pooling

D2L: "max-pooling ... is preferable to average pooling, as it confers some degree of invariance to output." Averaging dilutes a strong local activation by combining it with weaker neighbors; max preserves it.

## Implementation as convolution

Average pooling is equivalent to a convolution with a uniform kernel of value $1/|W|$ — i.e., it is a special case of convolution, unlike max-pooling.

## Connections

- [[Pooling]] — parent operator family.
- [[MaxPooling]] — the preferred modern alternative.
- [[LeNet]] — original deployer of average pooling.
- [[CNN]] — historical use site.
- [[d2l-convolutional-neural-networks]] — reference + preference statement.
