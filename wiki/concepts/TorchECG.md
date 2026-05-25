---
title: "torch_ecg"
type: concept
tags: [stub, tool, python, ecg, pytorch]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# torch_ecg

*Stub — referenced as the ECG-augmentation framework in ECG-Chat.*

**Wen & Kang — *"torch_ecg: An ECG Deep Learning Framework Implemented using PyTorch."*** Open-source PyTorch toolkit for ECG deep-learning experimentation. In [[2408.08849-ecg-chat|ECG-Chat]] it supplies the three signal-domain augmentations applied during contrastive pretraining: **baseline wander, cut mix, random masking**.

## Connections
- [[2408.08849-ecg-chat]] — uses torch_ecg's augmentation primitives.
- [[ECG]] — modality.
- [[ECGEncoder]] — the 1d-ViT trained with torch_ecg augmentations.
