---
title: "Stable Diffusion"
type: concept
tags: [generative-models, diffusion, text-to-image, computer-vision]
sources: [practical-deep-learning-for-coders]
last_updated: 2026-06-04
---

# Stable Diffusion

A **latent text-to-image diffusion model**: it generates images by iteratively denoising a random latent tensor, conditioned on a text prompt via a cross-attention mechanism. Running diffusion in a compressed latent space (rather than pixel space) is what makes it fast enough for consumer GPUs. Its core pieces are a [[Autoencoder|variational autoencoder]] (latent encode/decode), a U-Net denoiser, and a text encoder, with [[transformer|attention]] tying text to image.

Stable Diffusion is the **capstone build of Part 2** of *[[practical-deep-learning-for-coders|Practical Deep Learning for Coders]]*, where [[JeremyHoward|Jeremy Howard]] reconstructs it from foundations (matrix multiplication → backprop → autoencoders → attention) so students understand every component rather than treating it as a black box.

## Connections
- [[practical-deep-learning-for-coders]] — the fast.ai course rebuilds it from scratch in Part 2.
- [[transformer]] — attention is the text-conditioning mechanism.
- [[Backpropagation]] / [[NeuralNetwork]] — the foundations the course assembles into it.
- [[HuggingFace]] — the `diffusers`/Transformers ecosystem hosts and serves these models.
