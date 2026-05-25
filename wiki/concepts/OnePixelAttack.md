---
title: "One-Pixel Attack"
type: concept
tags: [adversarial, robustness, computer-vision]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# One-Pixel Attack

**An adversarial-perturbation attack that misclassifies images by changing just one pixel.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], the canonical reference is *"One Pixel Attack for Fooling Deep Neural Networks"* (Su et al. 2017).

## The headline numbers

| Dataset | Misclassification rate by one-pixel change |
|---|---|
| Kaggle CIFAR-10 | **67.97%** of natural test images |
| ImageNet | **16.04%** of test images |

## Real-world implications

> "An attacker could trick an AI model into misidentifying them as an authorized employee or make a self-driving car mistake a divider for a lane, leading to accidents."

The single-pixel constraint makes the perturbation visually undetectable to humans — a foundational adversarial-ML result for vision systems.

## Defense: train on perturbed data

Training on perturbed inputs **both improves performance and robustness** (Goodfellow et al. 2013; Moosavi-Dezfooli et al. 2015). Subsequent benchmarks [[ImageNetC]] / [[ImageNetP]] (Hendrycks & Dietterich 2019) formalized this defense paradigm.

## Connections

- [[Perturbation]] — parent technique.
- [[ImageNetC]] / [[ImageNetP]] — robustness benchmarks built from this insight.
- [[AdversarialPromptSearch]] — analogous attack in the prompting / language space.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
