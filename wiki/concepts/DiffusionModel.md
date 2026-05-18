---
title: "Diffusion Model"
type: concept
tags: [generative-model, deep-learning]
sources: [d2l-introduction]
last_updated: 2026-05-16
---

# Diffusion Model

A deep generative model that **learns to reverse a noise-adding process**. Forward pass: gradually corrupt data with Gaussian noise over many steps. Reverse pass: train a network to **denoise**, iteratively converting random noise into a clean data sample.

Per [[d2l-introduction]]: "While the diffusion process gradually adds random noise to data samples, *diffusion models* learn the denoising process to gradually construct data samples from random noise, reversing the diffusion process."

## Historical lineage cited by D2L

- Sohl-Dickstein et al. 2015 — original deep-unsupervised-learning-via-nonequilibrium-thermodynamics paper.
- Song & Ermon 2019 — score-based generative modeling.
- Ho, Jain & Abbeel 2020 — DDPM (denoising diffusion probabilistic models); the modern recipe.
- Song et al. 2021 — score-based via SDEs.

## Why they replaced GANs

[[d2l-introduction]]: diffusion models "have started to replace [[generativeadversarialnetwork|generative adversarial networks]] in more recent deep generative models, such as in **DALL-E 2** (Ramesh et al. 2022) and **Imagen** (Saharia et al. 2022) for creative art and image generation based on text descriptions." Practical advantages over GANs: more stable training (no minimax saddle), better mode coverage, scales cleanly to text-conditional generation via classifier-free guidance.

## Connections

- [[generativeadversarialnetwork]] — predecessor generative-model family.
- [[UnsupervisedLearning]] — parent paradigm.
- [[d2l-introduction]] — corpus anchor.
