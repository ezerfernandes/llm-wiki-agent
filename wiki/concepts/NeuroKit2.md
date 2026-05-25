---
title: "NeuroKit2"
type: concept
tags: [tool, python, signal-processing, physiology]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# NeuroKit2

**Makowski, Pham, Lau, Brammer, Lespinasse, Pham, Schölzel & Annabel Chen (Behavior Research Methods, 2021) — *"NeuroKit2: A Python toolbox for neurophysiological signal processing."*** Open-source Python library for processing physiological signals (ECG, EEG, EDA, EMG, PPG, RSP).

In [[2408.08849-ecg-chat|ECG-Chat]]: extracts **lead-II waveform morphology** per ECG record — RR interval, PR interval, QRS complex duration, QT/QTc interval, P/R/T wave peaks. These features are appended to the text report under [[WaveformDataEnhancement|WDE]], and also injected into [[ECGInstruct|ECG-Instruct]] prompts for GPT-4o to use when generating the instruction-tuning dataset.

## Connections
- [[2408.08849-ecg-chat]] — primary user.
- [[WaveformDataEnhancement]] — the augmentation trick built on NeuroKit2 outputs.
- [[ECGInstruct]] — the instruction-tuning dataset whose prompts include NeuroKit2 features.
- [[ECG]] — input modality.
