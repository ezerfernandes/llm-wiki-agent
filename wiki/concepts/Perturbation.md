---
title: "Perturbation"
type: concept
tags: [data-augmentation, robustness, adversarial]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Perturbation

**Adding noise to existing data to generate new training examples.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], perturbation began as an *attack* class (tricking models into misclassification) but is now used as a *defense* (training on perturbed data improves robustness).

## The discovery

Researchers found that **perturbing a sample slightly can fool a model**. Adding white noise to a ship image misclassifies it as a car. Adding snow / brightness / contrast changes images of stop signs into "no entry" signs.

## [[OnePixelAttack|One-pixel attacks]]

Su et al. (2017): changing **just one pixel** misclassified:

- **67.97%** of Kaggle CIFAR-10 test images
- **16.04%** of ImageNet test images

Real-world risk: a self-driving car mistaking a lane divider for a lane; a system mistaking an attacker for an authorized employee.

## Perturbation as defense

Train on perturbed data. Results:

- **Improves accuracy** on clean data (regularization effect).
- **Improves robustness** against adversarial inputs.

Goodfellow et al. (2013); Moosavi-Dezfooli et al. (2015) established this defense pattern in vision.

## [[ImageNetC]] / [[ImageNetP]] (Hendrycks & Dietterich 2019)

15 common visual corruptions applied to ImageNet:

- Brightness changes
- Contrast changes
- Added snow
- Various noise types

These became robustness benchmarks — models trained without perturbation often crash on them.

## Text perturbation

[[bert|BERT]] training (Devlin et al. 2018) replaced **1.5% of tokens with random words**. The authors reported a small performance boost — text perturbation works analogously to image perturbation.

## Beyond robustness — bias mitigation

Per Ch 8, [[Snap|Snap's]] 2022 case study perturbed visual assets along skin color, body type, hairstyle, clothing, and facial expressions to generate diverse training data — mitigating implicit biases in the original dataset.

## Connections

- [[DataAugmentation]] — parent technique.
- [[OnePixelAttack]] — the canonical attack-style perturbation.
- [[ImageNetC]] / [[ImageNetP]] — robustness benchmarks built via perturbation.
- [[adversarialensemble]] / [[AdversarialPromptSearch]] — adjacent adversarial-attack research.
- [[RuleBasedDataSynthesis]] — parent class.
- [[bert|BERT]] — used token perturbation in pre-training.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
