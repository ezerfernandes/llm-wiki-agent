---
title: "ImageNet-C"
type: concept
tags: [benchmark, robustness, computer-vision]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# ImageNet-C

**Hendrycks & Dietterich (2019) robustness benchmark: ImageNet with 15 common visual corruptions applied at 5 severity levels.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], ImageNet-C and its sibling [[ImageNetP|ImageNet-P]] are the canonical [[Perturbation|perturbation]]-based robustness benchmarks for computer-vision models.

## The 15 corruptions

Including (per Ch 8): brightness changes, contrast changes, added snow, various noise types — applied at varying severity to standard ImageNet test images.

## Use case

Models trained on ImageNet are evaluated on ImageNet-C to assess their **distribution-shift robustness**. Strong ImageNet accuracy with weak ImageNet-C accuracy indicates the model overfits to the specific visual properties of the original test set.

## Defense pattern: train on perturbed data

Training on perturbed data (using ImageNet-C / ImageNet-P style corruptions) improves both clean accuracy and corruption robustness — the canonical [[Perturbation|perturbation-as-defense]] pattern.

## Connections

- [[Perturbation]] — the technique these benchmarks rely on.
- [[ImageNetP]] — sibling benchmark.
- [[ImageNet]] — the source dataset.
- [[OnePixelAttack]] — adjacent perturbation-attack research.
- [[DataAugmentation]] — adjacent technique (corruption applied for training, not evaluation).
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
