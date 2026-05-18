---
title: "Christian Szegedy"
type: entity
tags: [person, researcher, deep-learning, cnn]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Christian Szegedy

German computer scientist; long-time researcher at [[google|Google]]. First author of **GoogLeNet** ([[ChristianSzegedy|Szegedy]] et al. 2015) and co-author with [[SergeyIoffe|Sergey Ioffe]] of the **batch normalization** paper (Ioffe & Szegedy 2015) — two of the most influential CNN-design contributions of the mid-2010s.

## Why he matters here

- **GoogLeNet / Inception (2014).** Introduced the **Inception block** — four parallel branches at different convolution scales concatenated along the channel axis — and the stem / body / head template adopted ever since ([[d2l-convolutional-modern]] §googlenet). ILSVRC 2014 winner.
- **Inception successors.** Szegedy et al. also wrote Inception-v2/v3 (Szegedy, Vanhoucke, Ioffe et al. 2016 — adds [[BatchNormalization|BN]] and label smoothing) and Inception-v4 / Inception-ResNet (Szegedy, Ioffe, Vanhoucke et al. 2017 — adds residual connections).
- **Batch normalization (2015).** Co-author with [[SergeyIoffe|Ioffe]] — see [[BatchNormalization]] / [[d2l-convolutional-modern]] §batch-norm.
- **Adversarial examples (pre-history).** Szegedy et al. (2013) — "Intriguing properties of neural networks" — introduced the adversarial-example phenomenon. (Not covered in this chapter but relevant historical context.)

## Affiliations

- [[google|Google Research]] — primary affiliation through the 2010s.
- Subsequent moves to xAI / startup work.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[GoogLeNet]] / [[Inception]] — first author.
- [[BatchNormalization]] — co-author.
- [[SergeyIoffe]] — BatchNorm co-author and frequent collaborator.
- [[google]] — institutional home for both GoogLeNet and BN.
- [[CNN]] / [[ImageNet]] — context.
