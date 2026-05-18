---
title: "Max-Pooling"
type: concept
tags: [deep-learning, cnn]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Max-Pooling

A [[Pooling|pooling]] operator that returns the **maximum** value within each pooling window:

$$[\mathbf Y]_{i,j} = \max_{(a,b)\in W}\,[\mathbf X]_{i+a,\,j+b}.$$

Introduced in cognitive-neuroscience modeling of object recognition by Riesenhuber & Poggio (1999), with an earlier appearance in speech recognition (Yamaguchi et al. 1990). The dominant pooling choice in modern CNN architectures.

## Why max is preferred

- **Local translation invariance:** if a strong activation shifts by one pixel within the window, the max is unchanged.
- **Sparse signal preservation:** keeps the strongest feature response, discards distractors.
- **Gradient routing:** during backprop the gradient flows only to the max-position; this can be seen as a learned-routing inductive bias.

[[d2l-convolutional-neural-networks]] §pooling: "In almost all cases, max-pooling ... is preferable to average pooling."

## Typical recipe

`MaxPool2d(kernel_size=2, stride=2)` — the canonical "halve spatial resolution" pool used after each conv block in VGG, ResNet (input stem), and most modern CNNs. Older architectures (LeNet) use [[AveragePooling]].

## Modernizing LeNet

[[d2l-convolutional-neural-networks]] §lenet exercises explicitly suggest: *replace AvgPool with MaxPool, replace sigmoid with ReLU*. This single change typically improves accuracy and training speed on MNIST/Fashion-MNIST.

## Connections

- [[Pooling]] — the parent operator family.
- [[AveragePooling]] — the alternative; older, less preferred.
- [[CNN]] — primary use site.
- [[LeNet]] — uses AvgPool; modern variants substitute MaxPool.
- [[d2l-convolutional-neural-networks]] — canonical reference; preference statement and history.
- [[TranslationInvariance]] — the property max-pooling provides locally.
