---
title: "Data Augmentation"
type: concept
tags: [training, regularization, computer-vision]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Data Augmentation

Generating additional training examples via random label-preserving transformations of existing ones. The cheapest form of regularization in deep learning — expands the effective training set, reduces model dependence on incidental attributes (object position, scale, color), and is "indispensable for the success of [[AlexNet]]" per [[d2l-computer-vision]] §`image-augmentation`.

## Common operations (per [[d2l-computer-vision]])

- **Geometric:** `RandomHorizontalFlip` / `RandomVerticalFlip` (each with $p=0.5$); `RandomResizedCrop(size, scale=(0.1, 1.0), ratio=(0.5, 2.0))` — random area + aspect-ratio crop rescaled to a fixed input shape.
- **Color:** `ColorJitter(brightness, contrast, saturation, hue)` — independent multiplicative perturbations to each channel.
- **Combination:** `torchvision.transforms.Compose([...])` to chain ops, followed by `ToTensor` + per-channel `Normalize` with ImageNet statistics `mean=[0.485, 0.456, 0.406]` / `std=[0.229, 0.224, 0.225]`.

## Application rule

Apply **only at training time**; test-time predictions must be deterministic ("we usually only apply image augmentation to training examples, and do not use image augmentation with random operations during prediction" — [[d2l-computer-vision]]). At test time, deterministic resize + center-crop are used instead.

## Beyond image classification

Object-detection augmentation is non-trivial: cropping may exclude or partially clip a labeled object, so the [[BoundingBox]] labels must be transformed jointly with the image. [[SemanticSegmentation]] requires the same (image, label) coupling — only random crops on `(image, label_map)` pairs are safe; arbitrary scaling distorts the label boundaries.

## Connections

- [[Overfitting]] / [[Generalization]] — augmentation reduces overfitting empirically.
- [[AlexNet]] — first ImageNet-winning CNN to credit augmentation for its success.
- [[DataAugmentation]] is one of the regularizers in the [[d2l-multilayer-perceptrons]] / [[d2l-linear-regression]] regularization toolkit (alongside [[WeightDecay]], [[Dropout]], [[EarlyStopping]]).
- For NLP analogues: back-translation, span masking ([[MaskedLanguageModeling|MLM]]), token deletion / swap.
