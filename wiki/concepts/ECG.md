---
title: "ECG"
type: concept
tags: [signal, medical, cardiology, modality]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# ECG — Electrocardiogram

**Electrocardiography** is a non-invasive recording of the heart's electrical activity over time, captured via skin electrodes. Standard 12-lead ECGs are sampled at 500 Hz for 10 s in research datasets ([[MIMIC-IV-ECG]], [[PTB-XL]], [[CPSC2018]]) and are the canonical input modality for *cardiology* in the same way images are for *radiology* or text is for *clinical notes*.

The wave components an ECG-language model has to interpret: **P wave** (atrial depolarization), **QRS complex** (ventricular depolarization), **T wave** (ventricular repolarization), plus the **PR interval**, **QT/QTc interval**, **RR interval**, and the peaks themselves. [[NeuroKit2]] extracts these per-record from lead-II as a feature vector ECG-language models can append to a text description — the [[WaveformDataEnhancement|WDE]] trick at the heart of [[2408.08849-ecg-chat|ECG-Chat]]'s contrastive-training pipeline.

ECG-text modeling sits in a structurally harder regime than image-text or radiology-text: most labeled ECG corpora attach the *same* templated report ("normal sinus rhythm, no abnormalities detected") to many physiologically distinct records, collapsing the contrastive signal. [[2408.08849-ecg-chat|ECG-Chat]] reports zero-shot retrieval R@1 of just **2.14** on PTB-XL with a vanilla [[CoCa]] dual encoder — until WDE adds per-record morphology, lifting it to **64.7**.

## Connections
- [[2408.08849-ecg-chat]] — the first multimodal LLM dedicated to ECG; wiki anchor for this modality.
- [[MIMIC-IV-ECG]], [[PTB-XL]], [[CPSC2018]], [[ChampanShaoxingNingbo]], [[ShandongProvincialHospital]] — the five datasets composing the ECG corpus.
- [[NeuroKit2]] — the Python toolbox for extracting waveform morphology features.
- [[ECGEncoder]] — the 1d-ViT backbone over raw 12-lead signal.
- [[WaveformDataEnhancement]] — the text-side augmentation trick for ECG contrastive learning.
- [[MultimodalLLM]] — the broader category ECG-Chat extends to a new modality.
