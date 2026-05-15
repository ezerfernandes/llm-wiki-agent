---
title: "Saliency Maps"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/pixel-attribution.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
Pixel attribution methods highlight the pixels that were relevant for a certain image classification by a neural network. @fig-vanilla is an example of an explanation.

## Key Claims
- **Vanilla Gradient** — The idea of Vanilla Gradient, introduced by @simonyan2014deep as one of the first pixel attribution approaches, is quite simple if you already know backpropagation.
- **DeconvNet** — DeconvNet by @zeiler2014visualizing is almost identical to Vanilla Gradient.
- **Grad-CAM** — Grad-CAM [@selvaraju2017gradcam] provides visual explanations for CNN decisions.
- **Guided Grad-CAM** — From the description of Grad-CAM, you can guess that the localization is very coarse, since the last convolutional feature maps have a much coarser resolution compared to the input image.
- **SmoothGrad** — The idea of SmoothGrad by @smilkov2017smoothgrad is to make gradient-based explanations less noisy by adding noise and averaging over these artificially noisy gradients.
- **Examples** — Let's see some examples of what these maps look like and how the methods compare qualitatively.
- **Strengths** — The explanations are **visual** and we are quick to recognize images.
- **Limitations** — As with most interpretation methods, it's **difficult to know whether an explanation is correct**, and a huge part of the evaluation is only qualitative ("These explanations look about right, let's publish the paper already").
- **Software** — There are several software implementations of pixel attribution methods.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-cnn-features]] — referenced via @sec or [text](#cnn-features).
- [[imlbook-lime]] — referenced via @sec or [text](#lime).
- [[imlbook-shap]] — referenced via @sec or [text](#shap).
- [[imlbook-shapley]] — referenced via @sec or [text](#shapley).
- **Cited works** (sample): `adebayo2018sanity`, `alber2019innvestigate`, `bach2015pixelwise`, `ghorbani2019interpretation`, `kindermans2019unreliability`, `selvaraju2017gradcam`, `shrikumar2017learning`, `simonyan2014deep` (+5 more).

## Contradictions
None noted in this chapter.
