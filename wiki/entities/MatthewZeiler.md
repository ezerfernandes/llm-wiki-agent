---
title: "Matthew D. Zeiler"
type: entity
tags: [person, researcher, deep-learning, optimization]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Matthew D. Zeiler

American deep-learning researcher and entrepreneur; founder and CEO of Clarifai. PhD with Rob Fergus at [[nyu|NYU]]. Author of **[[Adadelta]]** (Zeiler 2012, arXiv:1212.5701) — the [[Adagrad]] variant that eliminates the global learning-rate hyperparameter by using a leaky average of *parameter changes* as the unit-matching factor.

## Why he matters here

- **Adadelta (2012).** Removes Adagrad's global learning rate by using $\sqrt{\Delta\mathbf{x}_{t-1}+\epsilon}$ as the numerator of the rescaling factor — yielding a "no-learning-rate" optimizer ([[d2l-optimization]] §adadelta).
- **Deconvolutional networks (2014).** Visualization of [[CNN]] feature maps via deconvolution (Zeiler & Fergus 2014) — one of the first interpretability tools for deep vision models.

## Affiliations

- Clarifai — founder & CEO.
- [[nyu|NYU]] — PhD with Rob Fergus.

## Connections

- [[d2l-optimization]] — cites Zeiler 2012.
- [[Adadelta]] — flagship contribution.
- [[Adagrad]] / [[RMSProp]] / [[Adam]] — the per-coordinate-adaptive family.
