---
title: "Shandong Provincial Hospital (SPH)"
type: concept
tags: [dataset, ecg, china]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# Shandong Provincial Hospital (SPH)

**Liu, Chen, Den, Chen, Zhang, Hu, Li, Bian, Shu & Wang (Scientific Data, 2022) — *"A large-scale multi-label 12-lead electrocardiogram database with standardized diagnostic statements."*** **25,770 ECG records from 24,666 patients**, recording lengths 10–60 s, sampling rate 500 Hz. Each diagnosis is annotated with statements conforming to AHA/ACC/HRS recommendations.

In [[2408.08849-ecg-chat|ECG-Chat]]:
- First 10 seconds intercepted per record for training-data uniformity.
- Standardized statements converted to free-text reports.
- **20,616 training samples** contributed to the 805K-record contrastive-pretraining mix.

## Connections
- [[2408.08849-ecg-chat]] — primary user.
- [[ECG]] — modality.
- [[MIMIC-IV-ECG]], [[ChampanShaoxingNingbo]] — the other two corpora in the ECG-Chat training mix.
