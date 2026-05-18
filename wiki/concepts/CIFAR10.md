---
title: "CIFAR-10"
type: concept
tags: [computer-vision, dataset]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# CIFAR-10

Image-classification benchmark — 60,000 32×32 RGB images across 10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck). 50,000 train / 10,000 test in the canonical split. Released by Krizhevsky & Hinton (Toronto) circa 2009 as a smaller cousin of CIFAR-100.

## In [[d2l-computer-vision]]

Featured in three sections:
1. **§`image-augmentation`** — running benchmark for the [[DataAugmentation|image-augmentation]] worked example (CIFAR-10's per-image color + position variation makes augmentation effects more visible than [[FashionMNIST]]).
2. **§`kaggle-cifar10`** — Kaggle CIFAR-10 competition walk-through: 50k train + 300k test (290k unscored to deter manual labeling), raw png files + `trainLabels.csv` → reorganize into train/valid/test directories grouped by class → augmentation pipeline → train a [[ResNet|ResNet]] variant → submit predictions.
3. Used implicitly in §`kaggle-dog` as a contrast point for the higher-resolution dog-breed competition.

## D2L's Kaggle CIFAR-10 organization helper

`d2l.read_csv_labels(fname)`, `d2l.reorg_train_valid(data_dir, labels, valid_ratio)`, `d2l.reorg_test(data_dir)` — utility functions that move png files into a directory-of-class-directories structure that `torchvision.datasets.ImageFolder` can consume.

## Typical baseline

A ResNet-18 (or D2L's mini ResNet-18 variant) trained for ~10 epochs with standard augmentation (random crop with 4-pixel padding, random horizontal flip, normalize) achieves ~92% test accuracy. SOTA on the leaderboard is >99% (with extreme augmentation + ensembling).

## Connections

- [[DataAugmentation]] / [[FineTuning]] / [[ResNet]] / [[ImageNet]] (the bigger dataset; CIFAR-10 is its toy cousin).
- [[FashionMNIST]] / [[MNIST]] — even smaller pedagogical alternatives.
- [[Kaggle]] — host of the competition walk-through.
- [[d2l-image-augmentation|d2l-computer-vision]] §`image-augmentation` — running benchmark.
