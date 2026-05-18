---
title: "AlexNet"
type: concept
tags: [deep-learning, cnn, architecture, computer-vision]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# AlexNet

The 8-layer CNN — 5 convolutional + 3 fully-connected — by [[AlexKrizhevsky|Krizhevsky]], [[IlyaSutskever|Sutskever]] & [[GeoffreyHinton|Hinton]] (2012, University of Toronto) that won the **[[ImageNet|ILSVRC 2012]]** challenge by a wide margin and is widely credited as the start of the modern deep-learning era in computer vision. "This network showed, for the first time, that the features obtained by learning can transcend manually-designed features, breaking the previous paradigm in computer vision" ([[d2l-convolutional-modern]] §alexnet).

## Architecture (D2L's streamlined version)

Input: $224\times224$ RGB (originally; D2L trains on Fashion-MNIST upsampled to $224\times224$).

| Layer | Op | Channels | Kernel | Stride | Padding |
|---|---|---|---|---|---|
| 1 | Conv + ReLU | 96 | $11\times11$ | 4 | 1 |
| 2 | MaxPool | — | $3\times3$ | 2 | — |
| 3 | Conv + ReLU | 256 | $5\times5$ | 1 | 2 |
| 4 | MaxPool | — | $3\times3$ | 2 | — |
| 5 | Conv + ReLU | 384 | $3\times3$ | 1 | 1 |
| 6 | Conv + ReLU | 384 | $3\times3$ | 1 | 1 |
| 7 | Conv + ReLU | 256 | $3\times3$ | 1 | 1 |
| 8 | MaxPool | — | $3\times3$ | 2 | — |
| 9 | FC + ReLU + Dropout 0.5 | 4096 | — | — | — |
| 10 | FC + ReLU + Dropout 0.5 | 4096 | — | — | — |
| 11 | FC (logits) | 1000 | — | — | — |

## Key ingredients (vs. [[LeNet]])

1. **Scale.** Trained on [[ImageNet]] (~1.4M images × 1000 classes; $224\times224$) instead of MNIST (60K × 10; $28\times28$).
2. **GPU compute.** Two NVIDIA GTX 580s × 3 GB × 1.5 TFLOPs; [[AlexKrizhevsky|Krizhevsky]]'s `cuda-convnet` was the industry standard for years.
3. **Dual-data-stream split.** The original AlexNet split the model across two GPUs to fit into 6 GB total — D2L's "streamlined version" drops this since modern GPUs have abundant memory.
4. **[[ReLU]] instead of sigmoid.** No exponential; non-saturating gradient on the positive interval; resists vanishing-gradient failure modes that plague sigmoid initialization.
5. **[[Dropout]] for FC-layer regularization.** AlexNet was the first deployed system to use Dropout at scale (Srivastava, Hinton, Krizhevsky et al. 2014).
6. **Image augmentation.** Flips, crops, color jitter — effectively expands the training set and reduces overfitting.

## The Achilles heel

AlexNet's last two FC layers are matrices of size $6400\times4096$ and $4096\times4096$ — ~164 MB and ~81 MFLOPs each. Nontrivial on mobile/embedded; one of the reasons later architectures ([[NetworkInNetwork|NiN]], [[GoogLeNet]]) replaced the FC head with [[GlobalAveragePooling|global average pooling]].

## Discussion (D2L)

> "AlexNet's structure bears a striking resemblance to LeNet, with a number of critical improvements, both for accuracy (dropout) and for ease of training (ReLU). What is equally striking is the amount of progress that has been made in terms of deep learning tooling. What was several months of work in 2012 can now be accomplished in a dozen lines of code using any modern framework."

## Connections

- [[d2l-convolutional-modern]] — canonical pedagogical reference.
- [[AlexKrizhevsky]] / [[IlyaSutskever]] / [[GeoffreyHinton]] — authors.
- [[CNN]] — parent family.
- [[LeNet]] — direct predecessor; AlexNet is "largely an evolutionary improvement over LeNet."
- [[ImageNet]] — the benchmark AlexNet won.
- [[ReLU]] / [[Dropout]] — the regularization/activation combo AlexNet popularized at scale.
- [[VGG]] / [[NetworkInNetwork]] / [[GoogLeNet]] / [[ResNet]] — successors.
- [[ConvolutionalLayer]] / [[MaxPooling]] / [[OneByOneConvolution]] — building blocks.
