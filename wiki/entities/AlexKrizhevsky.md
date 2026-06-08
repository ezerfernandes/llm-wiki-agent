---
title: "Alex Krizhevsky"
type: entity
tags: [person, researcher, cnn, deep-learning, mlsysbook]
sources: [d2l-convolutional-modern, d2l-multilayer-perceptrons, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Alex Krizhevsky

Ukrainian-Canadian computer scientist; PhD student of [[GeoffreyHinton|Geoffrey Hinton]] at the University of Toronto. First author of **AlexNet** ([[AlexKrizhevsky|Krizhevsky]], [[IlyaSutskever|Sutskever]], [[GeoffreyHinton|Hinton]] 2012) — the 8-layer CNN that won the [[ImageNet|ILSVRC 2012]] challenge by a wide margin and ignited the post-2012 deep-learning revival in computer vision.

## Why he matters here

- **AlexNet (2012).** Co-designed [[AlexNet]] and personally wrote `cuda-convnet`, the CUDA implementation of fast convolutions on two NVIDIA GTX 580 GPUs (3 GB each, 1.5 TFLOPs each). The dual-data-stream split he engineered to fit the model into 6 GB of GPU memory total was a defining constraint of the original AlexNet design — and `cuda-convnet` was the industry-standard CNN implementation for several years afterward ([[d2l-convolutional-modern]] §alexnet).
- **Dropout co-author.** [[NitishSrivastava|Srivastava]], [[GeoffreyHinton|Hinton]], **Krizhevsky** et al. (2014) — the [[Dropout]] paper. AlexNet was the first deployed system to use Dropout at scale.

## Connections

- [[d2l-convolutional-modern]] — chapter that walks through AlexNet's architecture and impact.
- [[AlexNet]] — the architecture; one-to-one to Krizhevsky's PhD work.
- [[IlyaSutskever]] / [[GeoffreyHinton]] — AlexNet co-authors.
- [[Dropout]] — co-authored the canonical 2014 paper.
- [[ImageNet]] — the dataset AlexNet broke through on.
- [[CNN]] — the architecture family AlexNet revived.
- [[mlsysbook-ch10-model-compression]] — Ch 10's opening war story: the GTX 580 (3 GB) couldn't hold the 60M-param net, so the two-tower split was *"a memory budget forced into the architecture"* — the chapter's anchor for "every model carries the fingerprints of the memory hierarchy it had to fit on."
