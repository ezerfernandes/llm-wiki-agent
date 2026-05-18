---
title: "MNIST"
type: entity
tags: [dataset, computer-vision, benchmark]
sources: [d2l-introduction, d2l-linear-classification, d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# MNIST

The 60,000-image handwritten-digit recognition dataset that served as the canonical small ML benchmark from the late 1990s through the early 2010s. Each example is a 28×28 grayscale image labeled with its digit (0–9).

## Why it matters per D2L

[[d2l-introduction]] uses MNIST as the **negative space** marker for the small-data era that preceded the deep-learning revival: "datasets were relatively small. In fact, Fisher's Iris dataset from 1936 was still a popular tool for testing the efficacy of algorithms. **The MNIST dataset with its 60,000 handwritten digits was considered huge.**"

MNIST grew out of the **OCR-based mail-sorting systems** the chapter cites as deployed since the 1990s — read-the-zip-code becomes recognize-the-digits, and the labeled examples accumulated en route to the modern training set.

## Successors

ImageNet (1.4M images, 1000 classes — see [[ImageNet]]) and CIFAR-10/100 displaced MNIST as the default CV benchmark once GPU compute made larger problems tractable. [[FashionMNIST|Fashion-MNIST]] ([[Zalando]] Research, 2017) is the **pedagogical** drop-in replacement: same 28×28 grayscale / 60k+10k format, but discriminative enough to separate model quality. Per [[d2l-linear-classification]]: "Today, MNIST serves as more of a sanity check than as a benchmark."

## Connections

- [[FashionMNIST]] — pedagogical successor used as the running benchmark in [[d2l-linear-classification]] and most subsequent D2L chapters.
- [[Zalando]] — releaser of Fashion-MNIST.
- [[ImageNet]] — successor scale-benchmark dataset that replaced MNIST as the front-line CV benchmark.
- [[ComputerVision]] — the application domain MNIST is from.
- [[d2l-introduction]] / [[d2l-linear-classification]] — corpus anchors for the "considered huge" framing and the "displaced by Fashion-MNIST" framing.
