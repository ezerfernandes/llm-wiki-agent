---
title: "Fashion-MNIST"
type: entity
tags: [dataset, computer-vision, benchmark]
sources: [d2l-linear-classification, d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Fashion-MNIST

A 10-class image-classification benchmark released by [[Zalando]] Research in 2017 (Xiao, Rasul & Vollgraf) as a **drop-in replacement for [[MNIST]]**: same 28×28 grayscale resolution, same 60,000 train / 10,000 test split, but with more discriminative content — clothing items rather than handwritten digits.

## Categories

`t-shirt`, `trouser`, `pullover`, `dress`, `coat`, `sandal`, `shirt`, `sneaker`, `bag`, `ankle boot` — 6,000 training and 1,000 test images per class.

## Why it displaced MNIST as a teaching benchmark

Per [[d2l-linear-classification]]: MNIST is too easy. "Even simple models by today's standards achieve classification accuracy over 95%, making it unsuitable for distinguishing between strong models and weaker ones." Fashion-MNIST preserves MNIST's pedagogical virtues (small, well-balanced, single-channel, free) while providing enough intra-class variation to separate model quality. Top-performing modern CNNs reach ~95% on Fashion-MNIST vs ~99.7% on MNIST — leaving room for a textbook to illustrate model improvements.

## Role in D2L

The **running benchmark** for [[d2l-linear-classification]] and most subsequent chapters: softmax regression, MLPs, CNNs (LeNet, AlexNet variants), and ResNet-style models are all first demonstrated on Fashion-MNIST before moving to ImageNet-scale problems. The `d2l.FashionMNIST` `DataModule` wraps each framework's native loader (`torchvision.datasets.FashionMNIST`, `gluon.data.vision.FashionMNIST`, `tf.keras.datasets.fashion_mnist`) into the D2L OO scaffold and is `#@save`-persisted into the `d2l` package.

## Connections

- [[MNIST]] — predecessor; Fashion-MNIST inherits its 28×28 format and 60k/10k split, deliberately.
- [[Zalando]] — source organization (Zalando Research, the e-commerce company's research arm).
- [[ImageNet]] — successor scale benchmark; D2L notes ImageNet is "too large for many of the examples and illustrations in this book."
- [[d2l-linear-classification]] — corpus anchor introducing the dataset.
- [[d2l-multilayer-perceptrons]] — running benchmark for the MLP-from-scratch + dropout-from-scratch implementations.
- [[D2LPackage]] — `d2l.FashionMNIST` `DataModule` wraps loaders for all four supported frameworks.
- [[Classification]] / [[Softmax]] / [[CrossEntropyLoss]] — what Fashion-MNIST is used to demonstrate.
