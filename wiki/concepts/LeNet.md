---
title: "LeNet (LeNet-5)"
type: concept
tags: [deep-learning, cnn, architecture, computer-vision, history]
sources: [d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# LeNet

**LeNet** (specifically **LeNet-5**) is the [[CNN|convolutional neural network]] developed by [[YannLeCun|Yann LeCun]] at AT&T [[BellLabs]] in the 1990s for handwritten-digit recognition on [[MNIST]]. Canonical reference: LeCun, Bottou, Bengio, Haffner — "Gradient-based learning applied to document recognition," *Proceedings of the IEEE*, 1998. The first CNN to (a) be trained successfully end-to-end via [[Backpropagation]] (LeCun et al. 1989) and (b) match the accuracy of support-vector machines on a real task, then the dominant supervised-learning approach.

## Why it matters here

- **The deployed proof-of-concept of CNNs.** LeNet shipped — adopted by ATMs for check-deposit OCR. "Some ATMs still run the code that Yann LeCun and his colleague [[LeonBottou|Leon Bottou]] wrote in the 1990s" ([[d2l-convolutional-neural-networks]]).
- **The architectural ancestor of every modern CNN.** "LeNet is much more similar to [ResNet] than to [MLPs]" ([[d2l-convolutional-neural-networks]] §lenet summary). The conv→pool→conv→pool→flatten→FC→FC→softmax skeleton is intact in modern networks; differences are quantitative (depth, width) and detail-level (ReLU vs sigmoid, MaxPool vs AvgPool, BatchNorm, skip connections).

## Architecture

Two blocks ([[d2l-convolutional-neural-networks]] §lenet):

**1. Convolutional encoder** (extracts features, increases channels, decreases resolution)

| Layer | Op | Output |
|---|---|---|
| Input | — | $1\times28\times28$ (Fashion-MNIST or MNIST, padded from $28\times28$) |
| Conv | $6\times1\times5\times5$, padding $2$, sigmoid | $6\times28\times28$ |
| Pool | AvgPool $2\times2$, stride $2$ | $6\times14\times14$ |
| Conv | $16\times6\times5\times5$, sigmoid | $16\times10\times10$ |
| Pool | AvgPool $2\times2$, stride $2$ | $16\times5\times5$ |

**2. Dense block** (classifies)

| Layer | Op | Output |
|---|---|---|
| Flatten | — | $400$ |
| FC + sigmoid | — | $120$ |
| FC + sigmoid | — | $84$ |
| FC | (softmax outside) | $10$ |

Total: 2 conv layers, 2 avg-pool layers, 3 FC layers. About 60k parameters.

## Training recipe

- **Initialization:** [[XavierInitialization|Xavier]] (D2L's modernization; original LeNet used a similar variance-scaled scheme).
- **Loss:** [[CrossEntropyLoss|softmax cross-entropy]] (D2L). Original LeNet-5 used a Gaussian-decoder layer + RBF outputs — replaced by softmax in D2L's port for simplicity, but otherwise architecturally faithful.
- **Optimizer:** [[MinibatchSGD]], lr ≈ 0.1, batch size 128, 10 epochs (D2L's recipe).
- **Activation:** [[Sigmoid|sigmoid]] throughout — predates [[ReLU]]. D2L's exercises walk through replacing sigmoid→ReLU and AvgPool→MaxPool as a "modernize LeNet" challenge.

## Why each design choice

- **$5\times5$ kernels:** small enough to be efficient, large enough to capture digit strokes. Padding $=2$ on the first conv preserves the input resolution.
- **Channel progression $1\to 6\to 16$:** spatial info gets compressed, channel info expanded — D2L's general design principle ("trade off spatial resolution for greater channel depth").
- **Average pooling:** what was available in 1989. Modern variants use [[MaxPooling|max-pooling]].
- **Sigmoid:** smooth, differentiable, bounded — pre-[[ReLU]] norm. [[VanishingGradient|vanishing gradients]] in deep nets is what eventually killed it.
- **Flatten → FC → FC → FC:** classifier head. Modern fully-convolutional designs replace this with global average pooling.

## Historical significance

- **First CNN trained with backpropagation** (LeCun, Boser, Denker et al. 1989).
- **First CNN to match SVMs** (<1% per-digit error on MNIST when SVMs were SOTA).
- **First CNN deployed in industry** (ATM OCR).
- **Pre-revival cred** (a decade before [[AlexNet]] 2012 / [[ImageNet]] sparked the deep-learning revival).
- "LeNet-5 ... remains meaningful, even to this day" ([[d2l-convolutional-neural-networks]] §summary).

## Connections

- [[YannLeCun]] — architect and namesake.
- [[LeonBottou]] — co-author of the deployed code.
- [[BellLabs]] — institutional home.
- [[CNN]] — the family LeNet seeded.
- [[ConvolutionalLayer]] / [[AveragePooling]] / [[Sigmoid]] — components.
- [[MNIST]] / [[FashionMNIST]] — benchmark datasets (D2L trains on Fashion-MNIST).
- [[Backpropagation]] / [[XavierInitialization]] / [[MinibatchSGD]] / [[CrossEntropyLoss]] — training stack.
- [[d2l-convolutional-neural-networks]] — chapter that re-implements LeNet from scratch.
- [[AlexNet]] / [[ResNet]] — modern descendants.
- [[VanishingGradient]] — why sigmoid + deep stacks lost; what ReLU + BatchNorm fixed.
