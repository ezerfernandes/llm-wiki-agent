---
title: "Data Augmentation"
type: concept
tags: [training, regularization, computer-vision, data-selection, mlsysbook]
sources: [d2l-computer-vision, ai-engineering-ch08-dataset-engineering, mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
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

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

[[ChipHuyen|Huyen]] in Ch 8 distinguishes **augmentation** (derives from real data — flips, rotations, word swaps, [[Perturbation|perturbation]]) from **[[DataSynthesis|synthesis]]** (mimics real-data properties — templates, simulations, AI generation):

> "Data augmentation creates new data from existing data (which is real). … Data synthesis generates data to mimic the properties of real data."

In practice, the terms are often used interchangeably "since the goal of both augmentation and synthesis is to automate data creation."

### Text augmentation forms named in Ch 8

- **Synonym replacement** — "She's a fantastic nurse" → "She's a great nurse" via dictionary or embedding-space neighbors.
- **Bias-mitigation rewriting** — token-level gender / race / family-role swap (table in Ch 8: "Mr. Alex Wang" → "Ms. Alexa Wang"; "Emily" → "Mohammed").
- **AI-driven paraphrasing / translation** — extends manual word swap with model-based rewrites.
- **[[Perturbation|Perturbation]]** — [[bert|BERT]] training replaced 1.5% of tokens with random words and reported a small performance boost.

### Vision augmentation specifics (Ch 8 references)

- Krizhevsky et al. (2012) — [[AlexNet]] credit augmentation for the ImageNet win.
- [[OnePixelAttack|One-pixel attacks]] (Su et al. 2017) — single-pixel changes fool 67.97% of CIFAR-10.
- [[ImageNetC]] / [[ImageNetP]] (Hendrycks & Dietterich 2019) — 15 corruption types as benchmarks.
- [[Snap|Snap's]] 2022 case study — synthesizing diverse characters (skin color, body type, hairstyle, clothing, facial expression) to mitigate implicit biases.

### Augmentation as bias mitigation

The chapter's most operational claim: if your training data has gender bias (e.g., "nurse" → female; "doctor" → male), augmentation by replacing gendered tokens with their opposites can rebalance the distribution before training. This is one of the most accessible bias-mitigation techniques in the [[DatasetEngineering]] toolkit.

## In [[mlsysbook-ch09-data-selection|Machine Learning Systems Ch 9]]

Reddi Ch 9 frames augmentation as the lowest-cost form of [[SyntheticDataGeneration|synthetic generation]] (stage 3 of [[DataSelection|data selection]]) — multiplying training-set diversity by applying label-preserving transformations. Advanced methods: [[Cutout]] (random masks), [[MixUp]] (image/label blending), [[CutMix]] (patch pasting). Policy search via [[AutoAugment]] (15,000 GPU-hours) was displaced by [[RandAugment]] (2 hyperparameters). Text: [[BackTranslation|back-translation]], synonym replacement. Capacity-constrained models (MobileNet) rely on aggressive augmentation as the primary overfitting defense; heavy augmentation can make the CPU pipeline the bottleneck, motivating [[DataEchoing|data echoing]].

## Connections

- [[SyntheticDataGeneration]] / [[DataSelection]] — augmentation as pipeline stage 3 (Ch 9).
- [[Cutout]] / [[MixUp]] / [[CutMix]] / [[RandAugment]] / [[AutoAugment]] — the augmentation method family.
- [[ConsistencyRegularization]] — uses augmentations as a loss term (not extra data).
- [[DataEchoing]] — addresses the CPU cost of heavy augmentation.
- [[d2l-computer-vision]] / [[ai-engineering-ch08-dataset-engineering]] / [[mlsysbook-ch09-data-selection]] — sources.
