---
title: "ECG Encoder"
type: concept
tags: [encoder, vit, signal, ecg-chat]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# ECG Encoder

In [[2408.08849-ecg-chat|ECG-Chat]], a **12-layer 1d-Vision-Transformer** that ingests raw 12-lead ECG signal (10 s × 500 Hz) and produces a token sequence consumable by both:
- A **contrastive head** aligned with the [[MedCPT]] text encoder via [[CoCa]] dual loss.
- A **2-layer MLP projector** that maps tokens into [[Vicuna13B]]'s embedding space for instruction tuning.

**Specs:** patch size 50, hidden 768, 12 heads, MLP dim 3072. Three signal-domain augmentations during training: baseline wander, cut mix, random masking (via [[TorchECG]]). Pretrained on 805K-record mixed corpus ([[MIMIC-IV-ECG]] + [[ChampanShaoxingNingbo|CSN]] + [[ShandongProvincialHospital|SPH]]) for 20 epochs, AdamW lr 1e-4, weight decay 0.1, batch 128/GPU on 8×V100 32GB.

**Scaling behavior** (paper Table VI): encoder capacity at 43M / 85M / 128M parameters moves PTB-XL F1 by less than a point (54.6 / 52.8 / 54.4) — **encoder is not the bottleneck**; labeled ECG-text pair count is.

## Connections
- [[2408.08849-ecg-chat]] — paper introducing the 1d-ViT encoder.
- [[CoCa]] — the contrastive-captioner architecture the encoder slots into.
- [[ECG]] — input modality.
- [[Vicuna13B]] — the LLM the projector feeds into.
- [[WaveformDataEnhancement]] — the text-side augmentation that makes encoder pretraining converge.
